#!/usr/bin/env python3
"""Manual-equivalent checks in an unprivileged, network-disabled container."""
import hashlib, importlib.util, json, os, pathlib, re, subprocess, time
out=pathlib.Path('/out'); work=pathlib.Path('/work'); build=work/'build'; build.mkdir(exist_ok=True)
logs=out/'expanded-logs'; logs.mkdir(exist_ok=True)
spec=importlib.util.spec_from_file_location('official_audit','/skill/scripts/audit.py')
a=importlib.util.module_from_spec(spec); spec.loader.exec_module(a)
man=json.loads((out/'targets.json').read_text()); before=json.loads((out/'source-hashes.json').read_text())
lean='/tools/bin/lean'; env=dict(os.environ)
paths=[build,pathlib.Path('/mathlib/.lake/build/lib/lean')]+list(pathlib.Path('/mathlib/.lake/packages').glob('*/.lake/build/lib/lean'))
env['LEAN_PATH']=':'.join(map(str,paths))
result={'mechanical_status':'incomplete','semantic_verdict':'not_determined_by_script',
        'route':'documented manual-equivalent raw Lean route','commands':[],'targets':[]}
started=time.monotonic()
def run(label,cmd):
 t=time.monotonic()
 p=subprocess.run(cmd,cwd='/source',env=env,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,timeout=180)
 log=logs/(label+'.log');log.write_text(p.stdout)
 result['commands'].append({'label':label,'argv':cmd,'cwd':'/source','exit_code':p.returncode,
                            'seconds':round(time.monotonic()-t,3),'log':str(log),
                            'sha256':hashlib.sha256(log.read_bytes()).hexdigest()})
 if p.returncode:raise RuntimeError(label+' failed')
 return p.stdout
try:
 version=run('lean-version',[lean,'--version'])
 if 'version 4.19.0,' not in version:raise RuntimeError('Wrong toolchain')
 run('lake-version',['/tools/bin/lake','--version'])
 run('lean-help',[lean,'--help'])
 result['source_hashes_match_before']=all(hashlib.sha256((pathlib.Path('/source')/f).read_bytes()).hexdigest()==h for f,h in before.items())
 if not result['source_hashes_match_before']:raise RuntimeError('Input mismatch')
 for module in ['JSP690','Challenge']:
  run('fresh-'+module,[lean,'-o',str(build/(module+'.olean')),'/source/'+module+'.lean'])
 run('fresh-SkillBridge',[lean,'-o',str(build/'SkillBridge.olean'),'/out/SkillBridge.lean'])
 for i,target in enumerate(man['targets']):
  name=target['declaration']; source=out/'prepare'/f'Audit{i:04d}.lean'
  text=run('target-'+target['id'],[lean,str(source)])
  axioms=a.parse_axioms(text,name); status=a.classify(axioms)
  result['targets'].append({'id':target['id'],'declaration':name,'axioms':axioms,'status':status})
  if status!='standard_axioms_only':raise RuntimeError('Target dependency audit failed: '+name)
 defs=['JSP690.V','JSP690.Hypergraph','JSP690.edges','JSP690.Proper','JSP690.Colourable','JSP690.degree','JSP690.ProperOn']
 audit=work/'Definitions.lean'
 audit.write_text('import JSP690\nset_option pp.all true\n'+'\n'.join('#check @'+n+'\n#print '+n for n in defs)+'\n')
 run('key-definitions',[lean,str(audit)])
 (out/'Definitions.lean').write_text(audit.read_text())
 risky=r'\b(?:sorry|admit|axiom|native_decide|ofReduceBool|trustCompiler|debug\.skipKernelTC|implemented_by|extern)\b'
 findings={f:re.findall(risky,(pathlib.Path('/source')/f).read_text()) for f in ['JSP690.lean','Challenge.lean']}
 (out/'source-risk-scan.json').write_text(json.dumps(findings,indent=2)+'\n')
 if any(findings.values()):raise RuntimeError('Source mechanisms need review')
 result['source_hashes_match_after']=all(hashlib.sha256((pathlib.Path('/source')/f).read_bytes()).hexdigest()==h for f,h in before.items())
 if not result['source_hashes_match_after']:raise RuntimeError('Inputs changed')
 result['mechanical_status']='standard_axioms_only'
 result['environment']={'uid':os.getuid(),'network':'none (Docker launch recorded in workflow)',
  'read_only_root':True,'capabilities':'ALL dropped','memory_limit':'5 GiB','cpu_limit':2,
  'submitted_source_mount':'read-only','tools_and_dependencies':'read-only','credentials_mounted':False}
 result['kernel_replay_note']='No bundled leanchecker in original 4.19 toolchain. Separate public run 35439431281 replays the unchanged source using the explicitly pinned 4.34 CI profile; it is supplemental, not a 4.19 replay or independently implemented checker.'
finally:
 result['seconds']=round(time.monotonic()-started,3)
 (out/'manual-mechanical-result.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
