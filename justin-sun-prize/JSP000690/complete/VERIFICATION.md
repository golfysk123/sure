# Verification history and statement interface

The core mathematical source `JSP690.lean` has SHA-256 `f3d59c927a3b00d1ab6ba6426b1f6ffbf19ec5164e0852a5718b6859c2912fa6`.

At source commit `63f939758b0cff0e87701b045b64aa244f95b41f`, GitHub Actions run https://github.com/golfysk123/sure/actions/runs/35438565610 passed both official Lean 4.19.0 and Lean 4.34.0 jobs. Actual downloaded receipts show clean compilation, eight declaration audits and both false controls with the expected exit codes. The 4.34 job additionally passed bundled `leanchecker` replay.

Artifact hashes:
- Lean 4.19.0 ZIP: `dbc2eb2fe4b0ead55b8c0938b259bedf224965273ceabcdf34970640fb2d0b75`.
- Lean 4.34.0 ZIP: `e1fb4ffaeee7f980aa4cc5594964e56f38118b3f35e5ee3a4108e5f07ee45721`.

The next verification revision retains those core source bytes and adds `Challenge.lean`, an expanded statement without project-defined predicates in its type. Its proof unfolds the audited definitions. It adds a ninth axiom target, requires the negative controls specifically to be rejected because their propositions are false (not merely any syntax/import error), and rejects duplicate or missing axiom reports. Seven Python audit-parser tests passed locally. The workflow reruns for this revision; inspect its actual receipt rather than treating the earlier run as verification of changed files.

Read `Challenge.lean` first for statement correspondence, then `JSP690.lean` for the proof. This is the full chromatic reading. It does not formalize the separate transversal-number reading.

These are contributor-produced and CI-reproduced checks, not independent human certification, an independently implemented kernel, organizer verification, confirmed eligibility, or an award.
