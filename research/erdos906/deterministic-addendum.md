# Deterministic cofinite derivative zeros with arbitrarily slow excess growth

Analytic addendum, 22 September 2026. Project account `golfysk123`, developed with ChatGPT assistance. Offered for independent mathematical and prior-work review. No Lean verification, first-priority determination or award entitlement is asserted.

## Established input and proposed theorems

Fix `alpha = sqrt(2)`, put `q = exp(2 pi i alpha)`, and define

$$G(z)=\sum_{m\ge0}q^{m^2}\frac{z^m}{m!}.$$

Eremenko–Ostrovskii, *On the pits effect of Littlewood and Offord*, Bull. London Math. Soc. 39 (2007), 929–939, Theorem 3, proves completely regular growth with constant indicator one. We use its equivalent subharmonic-potential formulation

$$t^{-1}\log|G(tz)|\longrightarrow |z|\quad\text{in }L^1_{\mathrm{loc}}(\mathbb C),\quad t\to\infty.\tag{1}$$

The author preprint arXiv:0710.2870v2 states distribution convergence; local upper bounds and subharmonic compactness give the same local L1 convergence. A constant indicator without complete regularity would not suffice. This is an established input, not our contribution.

**Theorem 1 (proposed).** Let `(lambda_n)` be positive, nondecreasing and unbounded, with nonincreasing increments `d_n = lambda_(n+1)-lambda_n` and `lambda_n = o(log(n+2))`. Define

$$A_0=1,\quad A_k=\prod_{j=1}^k\lambda_j,\qquad f(z)=\sum_{k\ge0}q^{k^2}\frac{A_k}{k!}z^k.\tag{2}$$

Then f is transcendental entire and its derivative zeros, counted with multiplicity, satisfy

$$\lambda_n^{-1}\sum_{f^{(n)}(z)=0}m_z\delta_z\longrightarrow \frac{dA(z)}{2\pi|z|}\quad\text{vaguely on }\mathbb C.\tag{3}$$

The density is locally integrable at zero and has no atom there. In particular, for every nonempty open U there is N(U) such that all derivatives of order n >= N(U) have a zero in U.

**Theorem 2 (proposed sharp growth boundary).** For every positive nondecreasing function `omega(R)` tending to infinity, f can be chosen with the preceding property and

$$\log M_f(R)\le R\omega(R)\quad\text{for all sufficiently large }R.\tag{4}$$

The function has order exactly one and infinite type. No transcendental entire function of finite exponential type has the cofinite zero-hitting property. Thus there is no least unbounded excess-growth envelope above exponential type.

The original existence problem was already addressed by Hou and earlier Gaussian proposals credited below. We do not claim first resolution of that question or originality of the quadratic phase and (1). The proposed additions are the slowly varying derivative comparison, the deterministic zero-measure limit and the arbitrary-envelope construction. Their novelty has not been independently certified.

## 1. An exact derivative comparison

Since `A_k <= lambda_k^k` and `(A_k/k!)^(1/k) <= e lambda_k/k -> 0`, (2) is entire. Every coefficient is nonzero, so it is not a polynomial.

Unboundedness and concavity imply d_n>0 at every finite index, and

$$\lambda_n\le\lambda_{n+j}\le\lambda_n+jd_n,\qquad nd_n\le\lambda_n-\lambda_0<\lambda_n\quad(n\ge1).\tag{5}$$

Put `kappa_n=d_n/lambda_n`. For fixed R and d_n R<1, the generalized binomial series gives the exact majorant

$$S_n(R):=\sum_{m\ge0}\frac{\prod_{j=1}^m\lambda_{n+j}}{m!}R^m\le(1-d_nR)^{-1-1/\kappa_n}.\tag{6}$$

Indeed the product is at most `d_n^m (1+1/kappa_n)_m`. Define

$$\epsilon_n(R)=-(1+1/\kappa_n)\log(1-d_nR)-\lambda_nR.$$

The elementary logarithmic-series estimate and (5) give, eventually,

$$0\le\epsilon_n(R)\le d_nR+\frac{(\kappa_n+1)\kappa_n(\lambda_nR)^2}{2(1-d_nR)}\le C_R\lambda_n^2/n\longrightarrow0.\tag{7}$$

Normalize by nonzero constants: `F_n(z)=q^(-n^2) f^(n)(z)/A_n`. The identity `(n+m)^2-n^2=m^2+2nm` gives

$$F_n(z)-G(\lambda_nq^{2n}z)=\sum_{m\ge0}q^{m^2+2nm}\left(\prod_{j=1}^m\lambda_{n+j}-\lambda_n^m\right)\frac{z^m}{m!}.$$

The real coefficient differences are nonnegative. Consequently, uniformly for |z|<=R,

$$|F_n(z)-G(\lambda_nq^{2n}z)|\le S_n(R)-e^{\lambda_nR}\le C'_R\frac{\lambda_n^2}{n}e^{\lambda_nR}=:E_n(R),\tag{8}$$

and

$$\frac{\log E_n(R)}{\lambda_n}\longrightarrow-\infty.\tag{9}$$

The last assertion follows from `lambda_n=o(log n)`: its upper bound is `R-log(n)/lambda_n+O(log(lambda_n))/lambda_n`. This comparison covers the infinite series, not merely a truncation.

## 2. Logarithmic stability and zero measures

Set `u_n=lambda_n^(-1) log|F_n|` and `v_n=lambda_n^(-1) log|G(lambda_n q^(2n) z)|`. The limit (1) is radial. Rotating the integration variable in a disk centered at zero therefore proves `v_n -> |z|` in local L1 even though the rotations change at every n.

By (6)–(7), u_n are subharmonic and uniformly bounded above on compact sets. Also `u_n(0)=0`, since `F_n(0)=1`. Subharmonic compactness gives locally L1-convergent subsequences, not collapse to minus infinity. Given any such subsequence, pass further until both u_n and v_n converge almost everywhere. At almost every point the latter limit is finite. The error (9) is exponentially smaller than `|G(lambda_n q^(2n)z)|` there, so `u_n-v_n -> 0`. Every subsequential L1 limit is |z|. Hence

$$\lambda_n^{-1}\log|F_n(z)|\longrightarrow |z|\quad\text{in }L^1_{\mathrm{loc}}.\tag{10}$$

This explicitly handles zeros and cancellations; absolute closeness alone is not asserted to imply pointwise relative closeness everywhere.

In the convention `Delta log|F| = 2 pi sum m_z delta_z`, apply the Laplacian distributionally to (10). Since `Delta |z|=1/|z|` with no atom at zero, this proves (3); positivity turns distribution convergence into vague convergence of measures. A nonnegative nonzero smooth bump supported in any nonempty open set has positive integral against the limit measure. Its integral against the derivative-zero measure is then positive for every sufficiently large n, yielding a zero at every such order. This proves Theorem 1.

For each fixed R>0, the limit measure has no mass on the boundary circle, so the number of derivative zeros in `|z|<R`, counted with multiplicity, is `R lambda_n+o(lambda_n)`.

## 3. A concrete computable choice

Choose

$$\lambda_n=\sqrt{h_{n+1}},\qquad h_j=\sum_{k=1}^j1/k.$$

Then

$$d_n=\frac1{(n+2)(\sqrt{h_{n+2}}+\sqrt{h_{n+1}})}$$

is positive and decreasing, and `lambda_n ~ sqrt(log n)`. Formula (2), with q fixed above, now has no random sample or unspecified coefficient choice.

It obeys the explicit bound

$$M_f(R)\le2\exp(2R\sqrt{\log R})\qquad(R\ge e^{16}).\tag{11}$$

Let `u=log R`, `J=ceil(16 R sqrt(u))`. Then `1+log(J+2)<=2u`, so `lambda_(J+1)<=2 sqrt(u)`. The positive-series prefix is at most `exp(R lambda_J)<=exp(2R sqrt(u))`. Concavity with lambda_0>0 implies that `lambda_k/k` decreases, since `k d_k<lambda_k`. Hence all subsequent term ratios are at most `R lambda_(J+1)/(J+1)<=1/8`. The tail is at most one seventh of the last prefix term, proving (11).

## 4. Arbitrarily slow excess growth

Given omega in Theorem 2, set `eta(R)=min(omega(R),sqrt(R))`, and, for t>=1,

$$\phi(t)=\min\{\sqrt{\log(t+e)},\eta(\sqrt t)/8\}.$$

Choose integers b_j with `b_(j+1)>=2b_j` and `phi(b_j)>=2j+4`, for j>=1. Such choices exist. Put

$$L(t)=1+\sum_{j\ge1}\min(t/b_j,1)\quad(t\ge0),\qquad\lambda_n=L(n).\tag{12}$$

The series converges uniformly on compact sets, is unbounded, nondecreasing and concave, and has L(0)=1. For `b_j<=t<b_(j+1)`, its unsaturated tail is at most `2t/b_(j+1)<=2`, whence `L(t)<=j+3<=phi(t)`. Therefore the sequence satisfies Theorem 1 and eventually `lambda_n<=eta(sqrt(n))/8`.

For large R set `J=ceil(2R eta(R))`. Because `eta(R)<=sqrt(R)`, we have `J+1<=R^2`, so `lambda_(J+1)<=eta(R)/8`. The positive-series prefix is at most `exp(R eta(R)/8)`. Again `lambda_k/k` decreases, making every remaining term ratio at most `R lambda_(J+1)/(J+1)<=1/16`. Thus

$$M_f(R)\le(16/15)e^{R\eta(R)/8}\le e^{R\eta(R)}\le e^{R\omega(R)}$$

for sufficiently large R, proving (4).

The finite-exponential-type obstruction is elementary. If g has a zero in a disk of radius r, segment integration gives `M_g(r)<=2r M_g'(r)`. If `|f(z)|<=A exp(tau |z|)`, Cauchy's estimate gives `M_(f^(n))(r)<=A exp(tau r)(e tau)^n`. Choosing `r=1/(4e tau)`, cofinite zero-hitting instead forces `M_(f^(N+k))(r)>=(2e tau)^k M_(f^(N))(r)` with a positive last factor for a transcendental f: a contradiction. The constructed sequence is eventually bounded by `sqrt(log(n+e))`, so the same cutoff estimate as (11) gives order at most one. The obstruction gives order exactly one and infinite type, completing Theorem 2.

## Scope and review boundary

This addendum uses the established Eremenko–Ostrovskii theorem, not a formalization of it. Sections 1–4 give the proposed unrestricted analytic argument; they have not been independently refereed or checked in Lean. Finite high-precision diagnostics cannot certify the subharmonic limit, novelty or prize eligibility. The earlier probabilistic manuscript remains a separate validly stated proposed construction; the present route is deterministic and uses an additional classical input.

The original cofinite existence property has earlier sources. A stronger growth theorem is not automatically a first-solver claim for that problem. Recognition as a separate contribution or target requires organizer review.

## References

1. A. Eremenko and I. Ostrovskii, *On the pits effect of Littlewood and Offord*, Bull. London Math. Soc. 39 (2007), 929–939, DOI 10.1112/blms/bdm079. Author preprint arXiv:0710.2870v2, Theorem 3 and discussion of subharmonic convergence. https://arxiv.org/abs/0710.2870 . The parsed theorem and surrounding text were read; a separate PDF screenshot fetch was unavailable.
2. E. Hou, *Cofinite Zeros of High Derivatives*, arXiv:2607.20816v1 (2026). https://arxiv.org/abs/2607.20816 . Existing cofinite existence and order-two construction.
3. Hou's later author manuscript at commit `27e2206b984c3a0a284eb411a92eb18d5f097e6a` credits April 2026 Gaussian proposed solutions by Adriano Almeida and Przemek Chojecki. Those original proposals were not independently verified here. https://github.com/erichou1/cofinite-derivative-zeros .
4. Erdős Problem 906, https://www.erdosproblems.com/906 . Administrative cross-reference JSP-000752. The nonvacuous transcendental formulation is used.
