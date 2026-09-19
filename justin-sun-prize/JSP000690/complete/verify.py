#!/usr/bin/env python3
"""Rebuild the exact Lean source, audit dependencies, and reject two false controls.
Prepare the pinned Mathlib import closure first; no network requests occur here.
"""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import time

TARGETS = ['chromatic_original_problem', 'every_proper_subhypergraph',
           'every_edge_deletion', 'not_two_colourable', 'three_uniform',
           'edge_count', 'min_degree', 'min_degree_attained']
NAMES = ['JSP690.' + t for t in TARGETS] + ['JSP690Challenge.original_problem']
ALLOWED = {'propext', 'Classical.choice', 'Quot.sound'}

def audit(text: str) -> dict[str, list[str]]:
    reports: dict[str, list[str]] = {}
    for name in NAMES:
        matches = re.findall(r"'" + re.escape(name) + r"' depends on axioms: \[([^\]]*)\]", text)
        if len(matches) != 1:
            raise ValueError('Expected exactly one axiom report for ' + name)
        axioms = [s.strip() for s in matches[0].split(',') if s.strip()]
        if set(axioms) - ALLOWED:
            raise ValueError('Unpermitted axiom in ' + name + ': ' + ', '.join(axioms))
        reports[name] = axioms
    return reports

def is_false_proposition_rejection(returncode: int, text: str) -> bool:
    """Accept only the witnessed Lean 4.19/4.34 false-proposition diagnostics.

    A crash, an import/syntax error, or a zero exit status is never a valid
    negative control. The two explicit spellings reflect upstream formatting,
    not a relaxation of the required mathematical rejection.
    """
    if returncode != 1 or text.count('error:') != 1:
        return False
    match = re.search(
        r"error: (?:tactic 'decide'|Tactic `decide`) proved that the proposition\r?\n"
        r"(?P<proposition>.+?)\r?\nis false(?:\r?\n|$)", text, re.DOTALL)
    return match is not None and bool(match.group('proposition').strip())


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--lean', default='lean')
    ap.add_argument('--expected-version', required=True)
    ap.add_argument('--out', type=Path, default=Path('verification'))
    ap.add_argument('--replay', help='Path to the matching bundled leanchecker')
    args = ap.parse_args()
    root = Path(__file__).resolve().parent
    out = args.out.resolve(); out.mkdir(parents=True, exist_ok=True)
    env = dict(os.environ)
    env['LEAN_PATH'] = str(root) + os.pathsep + env.get('LEAN_PATH', '')
    lean = shutil.which(args.lean)
    if not lean:
        raise RuntimeError('Lean executable not found')
    receipt = {'schema_version': 2, 'steps': [], 'success': False,
               'created_at_utc': datetime.now(timezone.utc).isoformat(),
               'github_commit': env.get('GITHUB_SHA'), 'github_run_id': env.get('GITHUB_RUN_ID'),
               'scope': 'Contributor-produced verification; not organizer or independent human approval.'}
    started = time.monotonic()
    def run(label: str, cmd: list[str], should_pass: bool = True) -> str:
        p = subprocess.run(cmd, cwd=root, env=env, stdout=subprocess.PIPE,
                           stderr=subprocess.STDOUT, text=True, timeout=420)
        (out / (label + '.log')).write_text(p.stdout)
        receipt['steps'].append({'name': label, 'exit_code': p.returncode,
                                 'expected': 'success' if should_pass else 'Lean rejection'})
        if should_pass and p.returncode != 0:
            raise RuntimeError(label + ' failed; inspect its log')
        if not should_pass and not is_false_proposition_rejection(p.returncode, p.stdout):
            raise RuntimeError(label + ' did not produce the required Lean rejection')
        return p.stdout
    try:
        version = run('version', [lean, '--version'])
        if ('version ' + args.expected_version + ',') not in version:
            raise RuntimeError('Unexpected Lean version: ' + version.strip())
        receipt['lean_version'] = version.strip()
        receipt['source_sha256'] = {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                                    for p in [root/'JSP690.lean', root/'Challenge.lean', root/'Audit.lean', Path(__file__)]}
        for module in ['JSP690', 'Challenge']:
            for suffix in ['.olean', '.olean.private', '.olean.server', '.ilean', '.ir']:
                (root / (module + suffix)).unlink(missing_ok=True)
            source = (root/(module + '.lean')).read_text()
            if re.search(r'\b(sorry|admit|native_decide|axiom)\b', source):
                raise RuntimeError('Disallowed proof token in ' + module)
            run('clean-build-' + module, [lean, '-o', str(root/(module + '.olean')), str(root/(module + '.lean'))])
        text = run('axiom-audit', [lean, str(root/'Audit.lean')])
        receipt['axiom_reports'] = audit(text)
        if args.replay:
            run('kernel-replay', [args.replay, 'Challenge'])
            receipt['replay_limit'] = 'Bundled leanchecker shares Lean kernel implementation; it is not an independent checker implementation.'
        controls = {
            'false-arithmetic': 'example : (1 : Nat) = 2 := by decide\n',
            'false-edge-deletion': ('import JSP690\nset_option maxRecDepth 200000\n'
                'set_option maxHeartbeats 16000000\n'
                'example : ¬ JSP690.Colourable (JSP690.edges.erase {0, 1, 2}) 2 := by decide\n')}
        for label, source in controls.items():
            p = root/('Negative_'+label.replace('-', '_')+'.lean')
            p.write_text(source)
            try:
                run(label, [lean, str(p)], should_pass=False)
            finally:
                p.unlink(missing_ok=True)
        receipt['success'] = True
    finally:
        receipt['elapsed_seconds'] = round(time.monotonic() - started, 3)
        (out/'receipt.json').write_text(json.dumps(receipt, indent=2)+'\n')
    print(json.dumps(receipt, indent=2))
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
