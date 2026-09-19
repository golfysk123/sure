# JSP-000690: complete chromatic statement

This development supersedes the incomplete statement coverage of the older `../Prize690.lean` finite certificate. The older source and its history remain available; its acceptance did not prove this strengthened statement.

## Mathematical scope

`JSP690.chromatic_original_problem` proves existence of a finite simple hypergraph on `Fin 9` with 22 distinct edges, every edge of size 3, minimum degree exactly 7, chromatic number exactly 3 under weak vertex colourings, and a proper 2-colouring of every proper subhypergraph obtained by deleting arbitrary vertices, edges, or both. Colourings of a subhypergraph are functions on its actual remaining vertex subtype.

`Colourable H k` means `∃ c : α → Fin k, Proper H c`. Therefore the non-2-colourability theorem quantifies over ALL functions, not a list of unconnected bit masks. Standard Mathlib finite-function enumeration is used by kernel `decide`. The 22 explicit masks only supply edge-deletion witnesses; each is checked by the kernel. The universal subhypergraph conclusion is proved symbolically by restriction, not inferred from a test script.

This is the **chromatic reading explicitly stated by JSP-000690**, not the different transversal-number interpretation of Erdős 834. It proves no theorem about the minimum size of a hitting set. Broader organizer scope requirements would need separate work and review.

## Attribution and priority

Mathematical construction: Ruiliang Li, *On an Erdős–Lovász problem: 3-critical 3-graphs of minimum degree 7*, arXiv:2512.24850v1, Theorem 1.2 and equation (5): https://arxiv.org/html/2512.24850v1

Formalization project: GitHub account `golfysk123` directed this work and requested proof development. ChatGPT implemented this new finite-set encoding, quantified colouring statements, subhypergraph restriction proof, and verification harness in the associated authoring session. No mathematical discovery, sole manual authorship, independent human certification, or first-formalization priority is claimed.

Earlier competing public submissions include TheJustinSunPrize/awards PRs #21, #35, #39, #845, #1097, #1099, #1152 and #1613. PR #35 and its September 16 history belong to `superpilot69`, **not** `golfysk123`. None of that contributor's dates, source, or identity is claimed here. The old September 19 finite certificate is not a backdated priority anchor for this new complete statement.

## Verification status

A fresh local build with official Lean 4.19.0 and Mathlib `c44e0c8ee63ca166450922a373c7409c5d26b00b` completed with exit code 0. All eight audited declarations used only `propext`, `Classical.choice`, and `Quot.sound`. Both deliberately false controls were rejected. This contributor-run check took 37.749 seconds; it is not an organizer decision.

The committed workflow independently reruns source compilation on GitHub-hosted runners using pinned Lean/Mathlib versions 4.19.0 and 4.34.0. The 4.34 job additionally requires bundled `leanchecker` replay. Do not infer its outcome from this README: inspect the actual run and receipt for the selected commit. Bundled replay shares Lean's kernel implementation and is not an independently implemented proof checker.

Source SHA-256 (JSP690.lean): `f3d59c927a3b00d1ab6ba6426b1f6ffbf19ec5164e0852a5718b6859c2912fa6`.

## Reproduction

Prepare the exact Mathlib checkout and official Lean release using `.github/workflows/jsp000690.yml`, then set `LEAN_PATH` to absolute paths for that checkout's built import closure. Run:

```sh
python3 verify.py --lean /absolute/path/to/lean --expected-version 4.19.0 --out verification
```

For the 4.34.0 verification target use the matching version, Mathlib `5ed2965256430c3649e86755f9576b54eca72435`, and add `--replay /absolute/path/to/leanchecker`. `verify.py` deletes existing target oleans, rebuilds, imports the new module in an audit, checks the exact axiom allowlist, rejects false arithmetic and a false edge-deletion claim, and writes source hashes, exit codes and actual outcomes. It performs no network requests.

## Award status

No official award PR, accepted candidate record, verified identity, completed 14-day review, award confirmation, or payment entitlement is asserted. Existing earlier valid work can defeat priority. A passing build is evidence for review, not permission to claim money. The mathematical solver must be reviewed and registered before the Lean contribution under the current process.

Keep source and build evidence here. Any future awards-repository PR must contain catalog references only and disclose earlier contributions. Never submit another person's proof as this account's work.
