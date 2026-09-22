# Minimal growth order for cofinite zero-hitting by derivatives

Research manuscript, 22 September 2026. Project account: `golfysk123`. Developed with ChatGPT assistance in the associated research session. This is an analytic proof offered for review, not an independent referee report, Lean verification, first-priority determination, or award announcement.

## Statement and prior-work boundary

Let $M_f(R)=\max_{|z|\le R}|f(z)|$. Say that a transcendental entire function has property (C) if, for every nonempty open $U\subset\mathbb C$, some $N(U)$ satisfies

$$n\ge N(U)\quad\Longrightarrow\quad f^{(n)}\text{ has a zero in }U.$$

Equivalently, the union of the zero sets along every strictly increasing sequence of derivative orders is dense. If a fixed open set is missed at infinitely many orders, those orders give a counterexample subsequence; a cofinite set of orders meets every increasing subsequence. The nonpolynomial hypothesis excludes the vacuous polynomial case.

**Theorem.** There exists a transcendental entire function with property (C) and

$$M_f(R)\le 2\exp\bigl(4R(\log R)^2\bigr)\qquad(R\ge e^{16}).$$

No transcendental entire function of finite exponential type has property (C). Consequently the example has order exactly one and infinite type; one is the smallest possible growth order, and this minimum is attained.

Order means $\rho(f)=\limsup_{R\to\infty}\log\log M_f(R)/\log R$. Finite exponential type means $|f(z)|\le A e^{\tau|z|}$ for finite $A,\tau>0$.

**Attribution.** Eric Hou's *Cofinite Zeros of High Derivatives*, arXiv:2607.20816v1, already gives the existence assertion (C), with an order-at-most-two bound, by a bounded random Fock series. His later author manuscript also acknowledges earlier April 2026 Gaussian proposals by Adriano Almeida and Przemek Chojecki. We claim neither the original existence result nor the broad small-ball/mean-value/Borel--Cantelli strategy as new. The contribution proposed here is the slower rational-weight construction, its exact negative-binomial majorant, and the matching finite-exponential-type obstruction. Novelty of this strengthening has not been independently certified.

## 1. Obstruction to finite exponential type

If an analytic function $g$ has a zero in the closed disk of radius $r$, integration along the segment from that zero to any point of the disk gives

$$\max_{|z|\le r}|g(z)|\le 2r\max_{|z|\le r}|g'(z)|.$$

Suppose $f$ is transcendental, satisfies (C), and $|f(z)|\le A e^{\tau|z|}$ with $\tau>0$. Put $B_n(r)=\max_{|z|\le r}|f^{(n)}(z)|$. Cauchy's estimate on a circle of radius $n/\tau$ about each $z$, together with $n!\le n^n$, gives

$$B_n(r)\le A e^{\tau r}n!e^n(\tau/n)^n\le A e^{\tau r}(e\tau)^n.$$

Take $r=1/(4e\tau)$. Property (C) supplies a zero in this disk for every $n\ge N$. Thus

$$B_{N+k}(r)\ge(2r)^{-k}B_N(r)=(2e\tau)^k B_N(r).$$

Here $B_N(r)>0$, because no derivative of a transcendental entire function is identically zero. Combining the bounds and dividing by $(e\tau)^k$ would bound $2^kB_N(r)$ by a fixed constant, a contradiction. This argument does not use the disputed order-two theorem discussed in Hou's paper.

## 2. Discrete concavity of rational multipliers

Define harmonic numbers $h_j=\sum_{k=1}^j1/k$ for $j\ge1$, and put

$$\lambda_n=h_{n+1}^2\quad(n\ge0),\qquad A_0=1,\qquad A_n=\prod_{k=1}^n\lambda_k.$$

Set

$$d_n=\lambda_{n+1}-\lambda_n=\frac{2h_{n+1}}{n+2}+\frac1{(n+2)^2},\qquad \kappa_n=d_n/\lambda_n.$$

Direct substitution gives the exact positive identity

$$d_n-d_{n+1}=\frac{2(h_{n+1}-1)}{(n+2)(n+3)}+\frac{2n+5}{(n+2)^2(n+3)^2}>0.$$

The increments therefore decrease. Telescoping proves, for every $n,j\ge0$,

$$\lambda_n\le\lambda_{n+j}\le\lambda_n+jd_n=\lambda_n(1+j\kappa_n).\tag{1}$$

Integral comparison gives $\log(j+1)\le h_j\le1+\log j$, and hence

$$\lambda_n\sim(\log n)^2,\qquad d_n\to0,\qquad d_n\lambda_n=O((\log n)^3/n)\to0.\tag{2}$$

In particular $\lambda_n/\log n\to\infty$.

## 3. The entire series and its growth

Let $\xi_k$ be independent variables uniform on the closed complex unit disk, with normalized area law. Define

$$f(z)=\sum_{k\ge0}\xi_k\frac{A_k}{k!}z^k.\tag{3}$$

For every sample $|\xi_k|\le1$. Since $A_k\le(1+\log(k+1))^{2k}$ and $k!\ge(k/e)^k$, the root test gives normal convergence on all compact sets, uniformly over samples. Thus every sample is entire and may be differentiated termwise. Almost surely every $\xi_k$ is nonzero, so almost surely (3) is not a polynomial.

For the advertised growth bound, take $R\ge e^{16}$, $u=\log R$, and $J=\lceil16Ru^2\rceil$. Then $J+2\le18Ru^2$ and

$$1+\log(J+2)\le1+u+2\log u+\log18\le2u.$$

The last inequality holds at $u=16$ and persists because $u-2\log u$ increases there. For $t_k=A_kR^k/k!$, monotonicity gives

$$\sum_{k=0}^Jt_k\le e^{R\lambda_J}\le e^{4Ru^2}.$$

The function $(1+\log(x+1))^2/x$ decreases for $x\ge e^2$. Therefore, for $k\ge J$,

$$t_{k+1}/t_k=R h_{k+2}^2/(k+1)\le4Ru^2/J\le1/4.$$

The remaining tail is at most $t_J/3$, proving $M_f(R)\le2e^{4R(\log R)^2}$. Every sample thus has order at most one.

## 4. Exact derivative majorants

Writing $F_n=f^{(n)}$, termwise differentiation gives

$$F_n(z)=A_n\sum_{m\ge0}\xi_{n+m}\frac{\lambda_{n+1}\cdots\lambda_{n+m}}{m!}z^m.\tag{4}$$

Empty products equal one. For $q=d_nr=\kappa_n\lambda_nr<1$, (1) yields

$$\begin{aligned}
S_n(r)&:=\sum_{m\ge0}\frac{\lambda_{n+1}\cdots\lambda_{n+m}}{m!}r^m\\
&\le\sum_{m\ge0}\frac{(1+1/\kappa_n)_m}{m!}(\kappa_n\lambda_nr)^m
=(1-q)^{-1-1/\kappa_n}.
\end{aligned}\tag{5}$$

The last equality is the Taylor expansion of $(1-q)^{-a}$; $(a)_m$ is the rising factorial. It is an exact majorant of the infinite series, not a truncation.

For a fixed $R>0$ and sufficiently large $n$ define

$$\epsilon_n(R)=-(1+1/\kappa_n)\log(1-d_nR)-\lambda_nR.$$

The elementary inequality $-\log(1-q)\le q+q^2/[2(1-q)]$ implies

$$0\le\epsilon_n(R)\le d_nR+\frac{(\kappa_n+1)\kappa_n(\lambda_nR)^2}{2(1-d_nR)}\longrightarrow0,\tag{6}$$

using (2). The error is increasing in $R$. Consequently, uniformly for $|z|\le R$,

$$\log|F_n(z)|\le p_n(z)+\epsilon_n(R),\qquad p_n(z)=\log A_n+\lambda_n|z|.\tag{7}$$

A lower estimate uses a single coefficient. For $x\ge0$ and $m=\lfloor x\rfloor$,

$$x^m/m!\ge e^{x-2}/(1+x),\tag{8}$$

with $0^0=1$. For $x<1$ this is immediate. Otherwise use $\log m!\le m\log m-m+1+\log m$ (integral comparison), and $m\le x<m+1$. Select $x=\lambda_n|z|$. By (1), the coefficient multiplying $\xi_{n+m}$ in (4) has modulus at least

$$\exp\{p_n(z)-B_n(R)\},\qquad B_n(R)=2+\log(1+R\lambda_n).\tag{9}$$

At $z=0$ use $m=0$. Thus the estimate is uniform on the whole disk, not only an annulus.

## 5. A summable hole bound

For a uniform unit-disk variable $\xi$, nonzero $a$, arbitrary $b$, and $s\ge0$, area comparison gives $\mathbb P(|a\xi+b|<s)\le s^2/|a|^2$. Condition (4) on every coefficient except the one selected in (9). Normal convergence ensures the remaining sum is defined, and independence permits conditioning. We obtain, for $t\ge0$,

$$\mathbb P\{D_n(z)>t\}\le e^{-2t},\qquad D_n(z)=(p_n(z)-B_n(R)-\log|F_n(z)|)_+.$$

Thus $\mathbb E e^{D_n(z)}\le2$: integrate $e^D=1+\int_0^D e^t\,dt$. Logarithms at zeros may be assigned the extended value $-\infty$. The integrability just proved, and isolated zeros of a nonzero analytic function, justify the circular integrals. Joint measurability follows from normal convergence of measurable partial sums.

Fix $c\in\mathbb C$, $r>0$, and $R=|c|+r$. Define

$$\gamma(c,r)=\frac1{2\pi}\int_0^{2\pi}|c+re^{i\theta}|\,d\theta-|c|.$$

It has the explicit positive lower bound

$$\gamma(c,r)\ge g(c,r):=\frac{r^2}{4(|c|+r)}.\tag{10}$$

Indeed rotate $c$ onto the positive real axis, put $a=c+r\cos\theta$, $b=r\sin\theta$, and use
$\sqrt{a^2+b^2}-a=b^2/(\sqrt{a^2+b^2}+a)\ge b^2/[2(c+r)]$ whenever the denominator is positive; the remaining cases are immediate. Averaging uses the mean $1/2$ of $\sin^2\theta$.

Let $\overline D_n$ be the circular mean of $D_n(c+re^{i\theta})$. Jensen's inequality for the real exponential, followed by Tonelli, proves

$$\mathbb E e^{\overline D_n}\le2,\qquad \mathbb P(\overline D_n\ge t)\le2e^{-t}.\tag{11}$$

If $F_n$ has no zero in $B(c,2r)$, then $\log|F_n|$ is harmonic near the closed inner disk. Its circular mean equals its center value. By (7) and the definition of $D_n$ this implies

$$\overline D_n\ge\lambda_n\gamma(c,r)-B_n(R)-\epsilon_n(R)
\ge\lambda_ng(c,r)-B_n(R)-\epsilon_n(R).$$

For every $n$ with $d_nR<1$, (11) therefore gives

$$\mathbb P^*\{F_n\text{ is zero-free in }B(c,2r)\}
\le\min\{1,\;2\exp[-g(c,r)\lambda_n+B_n(R)+\epsilon_n(R)]\}.\tag{12}$$

Outer probability avoids a separate measurability requirement for the zero-free event: the containing circular-mean event is measurable. Since $\lambda_n\sim(\log n)^2$, $B_n(R)=O(\log\log n)$, and $\epsilon_n(R)\to0$, the bound is eventually at most $2\exp[-g(c,r)(\log n)^2/3]$. Its sum over $n$ is finite.

## 6. One sample, every open set, and the minimum order

Apply the first Borel--Cantelli estimate to each disk in the countable rational disk basis. No independence between derivatives is needed. Outside an outer-null set each disk is zero-free for only finitely many derivatives. The countable union of exceptions is outer-null. Intersect its complement with the probability-one event that every coefficient is nonzero and select a sample there. Every open set contains a basis disk, so its function is transcendental and has (C).

The deterministic growth bound gives order at most one. If its order were less than one, it would have finite exponential type, contrary to Section 1. Finite type at order one is excluded by the same argument. This proves the theorem.

This is an existence construction, not an explicitly computed coefficient sample. The theorem does not assert the smallest possible infinite-type growth envelope. Its sharpness concerns growth order and the exclusion of finite exponential type.

## Verification and award boundaries

Sections 1--6 give the unrestricted analytic argument. Finite arithmetic and high-precision checks are supplementary, not a proof of eventual zero-hitting, semantic correctness, or novelty. No Lean formalization or independent human verification of this theorem is claimed.

The original Erdős existence problem was already addressed by earlier authors. This stronger growth theorem does not by itself establish a first-solver claim or prize entitlement. Mathematical correctness, the novelty of the growth refinement, recognized problem scope, and award eligibility require separate review.

## Sources

- Eric Hou, *Cofinite Zeros of High Derivatives*, arXiv:2607.20816v1, submitted 23 July 2026: https://arxiv.org/html/2607.20816v1 . Existing order-two construction and the broad probabilistic strategy.
- Hou's later author manuscript, introduction, inspected at commit `27e2206b984c3a0a284eb411a92eb18d5f097e6a`: https://github.com/erichou1/cofinite-derivative-zeros/blob/27e2206b984c3a0a284eb411a92eb18d5f097e6a/paper.tex . It acknowledges April 2026 Gaussian proposals by Almeida and Chojecki. Those proposals and the retained Lean code were not independently verified here. No repository code was copied.
- Erdős Problem 906: https://www.erdosproblems.com/906 . The intended transcendental formulation is used, as in Hou's Section 1.
- Justin Sun Prize catalog JSP-000752: https://github.com/TheJustinSunPrize/awards/blob/main/problems/catalog-0701-0800.md#JSP-000752 . This administrative cross-reference is not an analytic input or an assertion of eligibility.
