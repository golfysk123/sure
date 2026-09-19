#!/usr/bin/env python3
"""Prepare a target-scoped audit of a fixed raw-Lean project, without editing its proof."""
from __future__ import annotations
import hashlib, json, os, pathlib, shutil, subprocess, sys
ROOT = pathlib.Path(sys.argv[1]).resolve()
PROOF = ROOT / 'proof/justin-sun-prize/JSP000690/complete'
OUT = ROOT / 'out'
OUT.mkdir(exist_ok=True)
COMMIT = 'c669ae41f2fa55b7e0c3a034bf3b4a0f19c07f0f'
SKILL_COMMIT = '38e63c424c7196f8d4ceb664c5c25f0c0529d5e2'
bridge = '''import Challenge
namespace PreSubmissionReview
/-- Finite simple hypergraph existence, formulated without submission-defined predicates. -/
theorem original_chromatic_question :
    ∃ n : Nat, 0 < n ∧ ∃ H : Finset (Finset (Fin n)),
      (∀ e ∈ H, e.card = 3) ∧
      (∀ v : Fin n, 7 ≤ (H.filter (fun e => v ∈ e)).card) ∧
      (∃ c : Fin n → Fin 3, ∀ e ∈ H, ∃ u ∈ e, ∃ v ∈ e, c u ≠ c v) ∧
      (∀ k : Nat, k < 3 → ¬ ∃ c : Fin n → Fin k,
        ∀ e ∈ H, ∃ u ∈ e, ∃ v ∈ e, c u ≠ c v) ∧
      (∀ (U : Finset (Fin n)) (F : Finset (Finset (Fin n))),
        F ⊆ H → (∀ e ∈ F, e ⊆ U) → (U ≠ Finset.univ ∨ F ≠ H) →
        ∃ c : {v : Fin n // v ∈ U} → Fin 2,
          ∀ e ∈ F, ∃ u v : {x : Fin n // x ∈ U},
            u.val ∈ e ∧ v.val ∈ e ∧ c u ≠ c v) := by
  obtain ⟨H, _, hu, hd, _, hc, hn, hs⟩ := JSP690Challenge.original_problem
  exact ⟨9, by decide, H, hu, hd, hc, hn, hs⟩
end PreSubmissionReview
'''
# This untracked bridge is the auditing harness, not part of the selected proof commit.
(PROOF/'SkillBridge.lean').write_text(bridge)
names = ['chromatic_original_problem','every_proper_subhypergraph','every_edge_deletion',
         'not_two_colourable','three_uniform','edge_count','min_degree','min_degree_attained']
targets=[{'id':n,'problem':'JSP-000690','role':'theorem','module':'JSP690',
          'source':'JSP690.lean','declaration':'JSP690.'+n} for n in names]
targets += [
 {'id':'expanded','problem':'JSP-000690','role':'theorem','module':'Challenge',
  'source':'Challenge.lean','declaration':'JSP690Challenge.original_problem'},
 {'id':'independent_bridge','problem':'JSP-000690','role':'bridge','module':'SkillBridge',
  'source':'SkillBridge.lean','declaration':'PreSubmissionReview.original_chromatic_question'}]
requirements=[
 ('existence','There exists a finite simple hypergraph; no assumed conclusion or empty-domain shortcut.', ['chromatic_original_problem','expanded','independent_bridge','edge_count']),
 ('uniformity','Every hyperedge is a three-element set.', ['three_uniform','expanded']),
 ('degree','Every vertex has degree at least seven; the witness additionally attains seven.', ['min_degree','min_degree_attained','expanded']),
 ('chromatic','The weak chromatic number is exactly three, quantifying over all colour maps.', ['not_two_colourable','chromatic_original_problem','expanded']),
 ('criticality','Every proper subhypergraph under arbitrary vertex/edge deletion is two-colourable on the actual remaining vertices.', ['every_edge_deletion','every_proper_subhypergraph','independent_bridge'])]
manifest={'schema_version':1,'project':{'root':str(PROOF),'repository':'https://github.com/golfysk123/sure',
 'commit':COMMIT,'toolchain':'leanprover/lean4:v4.19.0'},'problems':[{'id':'JSP-000690',
 'source':'https://arxiv.org/html/2512.24850v1',
 'requirements':[{'id':i,'description':d,'targets':t,'coverage':'pending'} for i,d,t in requirements]}], 'targets':targets}
(OUT/'targets.json').write_text(json.dumps(manifest,indent=2)+'\n')
meta={'proof_repository':'golfysk123/sure','proof_commit':COMMIT,'proof_branch':'justin-sun-prize-jsp000690',
      'skill_repository':'TheJustinSunPrize/awards','skill_commit':SKILL_COMMIT,
      'route':'raw Lean manual-equivalent route expressly allowed by reproduction.md sections 1 and 3',
      'semantic_verdict':'not_determined_by_script',
      'controller_commit':os.environ.get('GITHUB_SHA'),'run_id':os.environ.get('GITHUB_RUN_ID')}
(OUT/'metadata.json').write_text(json.dumps(meta,indent=2)+'\n')
script=ROOT/'awards/skills/lean-verify/scripts/audit.py'
for action in ['preflight','prepare']:
 p=subprocess.run([sys.executable,str(script),action,str(OUT/'targets.json'),'--out',str(OUT/action)],
                  text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,timeout=60)
 (OUT/(action+'.log')).write_text(p.stdout)
 result=json.loads((OUT/action/'result.json').read_text())
 if p.returncode!=2 or set(result['issues'])!={'lake_config_missing','dependency_lock_missing'}:
  raise RuntimeError('Unexpected preflight result; inspect '+action)
# No dummy Lake files are added. Existing exact dependency pins are in the selected CI profile.
(OUT/'manual-route.txt').write_text('Official preflight and prepare returned 2 only because this submitted project uses direct Lean, not Lake. No fake Lake file or dependency manifest was added. The documented raw-source manual-equivalent checks follow.\n')
(OUT/'source-hashes.json').write_text(json.dumps({f:hashlib.sha256((PROOF/f).read_bytes()).hexdigest() for f in ['JSP690.lean','Challenge.lean','Audit.lean','verify.py','lean-toolchain']},indent=2)+'\n')
# Preserve the prepared audit inputs and the explicitly separate bridge.
shutil.copy2(PROOF/'SkillBridge.lean',OUT/'SkillBridge.lean')
