# Prior-work update — 22 September 2026

This note supplements, and does not alter or backdate, the manuscript first published at `af00c073e7743b6664ceb46eaac34c4240be6714`.

## Earlier disproof located

The repository `seanm27lol/erdos-1131-lean` contains a human-readable disproof and a claimed complete Lean development for the same coefficient-one conjecture. Its commit `31574acf09ae50430c08da92288800fe7d26c7fd` is dated 23 July 2026. The construction uses roots of `T_n - (1/6)T_(n-2)` and gives an eventual scaled-defect bound of `106/105 > 1`.

- Statement and build map: https://github.com/seanm27lol/erdos-1131-lean/blob/31574acf09ae50430c08da92288800fe7d26c7fd/README.md
- Mathematical argument: https://github.com/seanm27lol/erdos-1131-lean/blob/31574acf09ae50430c08da92288800fe7d26c7fd/SOLUTION.md

We have read the mathematical source but have not independently rebuilt its Lean dependency closure or established the date of first public visibility. A commit date by itself does not settle priority. Nevertheless, this earlier-source claim must be disclosed, and our project does not claim the first disproof of the coefficient-one question.

## Older numerical literature

Brutman and Toledano, *An extremal problem of Erdős in interpolation theory*, Computers & Mathematics with Applications 34(12), 37–47 (1997), DOI `10.1016/S0898-1221(97)00232-0`, reports numerical minimization and asymptotic extrapolation. The publisher abstract was located; its full paper was not obtained in this session, so no conclusion about whether our exact Jacobi coefficient appears there is asserted.

## What remains our stated contribution

The September 20 manuscript proposes a Jacobi–Lobatto family asymptotic formula with coefficient `2[Gamma(5/4)/Gamma(3/4)]^2`, approximately `1.0942198076`, and optimization within that one-parameter family. It does not establish the global minimum over arbitrary nodes, comprehensive novelty, first priority, or award eligibility. Its analytic argument still requires independent mathematical review; successful finite-check CI does not certify it.

Project account: `golfysk123`; developed with ChatGPT assistance. No source code from the earlier disproof was copied into our original Jacobi manuscript or its supporting implementation.
