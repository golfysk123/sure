# JSP-000690 — independent Lean verification

AI-assisted independent formalization attempt for **JSP-000690**, the existence of a critically 3-chromatic 3-uniform hypergraph of minimum degree at least 7.

## Attribution boundary

The 9-vertex, 22-edge mathematical witness is **not a new discovery here**. It is the published witness of Ruiliang Li, *On the chromatic number and minimum degree of uniform hypergraphs*, arXiv:2512.24850v1 (2025), equation (5). Mathematical discovery credit remains with the cited source. This work only independently encodes and kernel-checks finite properties of that witness.

## Machine-checked scope

`Prize690.lean` uses only Lean core and checks:
- 22 hyperedges on 9 vertices;
- minimum vertex degree at least 7;
- an explicit proper 3-colouring;
- exhaustive rejection of all 512 binary colourings;
- every single-edge deletion is 2-colourable;
- no isolated vertices.

Edge-deletion criticality plus no isolated vertices yields the ordinary proper edge/vertex-subhypergraph criticality by restriction. The source deliberately does not claim mathematical novelty or first-formalization priority.

## Verification

Compiled with the official Lean release:

`Lean 4.19.0, x86_64-unknown-linux-gnu, commit 6caaee842e94, Release`

Kernel output:

```
'Prize690.finite_witness' depends on axioms: [propext]
'Prize690.not_two_colourable' depends on axioms: [propext]
```

No `sorry`, `admit`, `native_decide`, or custom axiom is present.

## Status

Proof evidence for review only. Earlier public JSP-000690 formalizations exist and must be considered for priority under the official prize rules. This repository does not announce an award or payment entitlement.
