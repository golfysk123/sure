# Jacobi–Lobatto nodes and the coefficient-one question in Erdős 1131

Research manuscript, 20 September 2026. Project directed by GitHub account `golfysk123`, with the derivation and implementation developed with ChatGPT in the associated authoring session. This is a proposed theorem with an analytic proof, not an independently certified result. No first-priority, official acceptance, or award entitlement is asserted.

## Statement and scope

For distinct nodes X={x_1,...,x_n} in [-1,1], let l_j be their Lagrange cardinal polynomials and let

$$I(X)=\int_{-1}^1\sum_j l_j(x)^2\,dx,\qquad M_n=\inf_{|X|=n}I(X).$$

[Erdős Problem 1131](https://www.erdosproblems.com/latex/1131) explicitly asks whether

$$M_n=2-\frac{1+o(1)}n.$$

It also asks for the minimum more generally. The result below contradicts the displayed coefficient-one conjecture, but does **not** determine the exact minimum or prove a globally optimal first-order constant. The prize catalog JSP-000938 asks the broader minimization question; its scope must not silently be replaced by the narrower conjecture.

**Theorem (proposed).** Fix 1<a<3/2, put b=a-1, and let X_(m+2,a) consist of -1, 1, and all m zeros of the conventionally normalized Jacobi polynomial P_m^(a,a). Then

$$I(X_{m+2,a})=2-\frac{c(b)}{m+2}+o(m^{-1}),\qquad c(b)=\frac{2\Gamma(1+b)\Gamma(3/2-b)}{\Gamma(1/2+b)\Gamma(1-b)}.$$

For 0<b<1/2, c(b)>1. Its unique maximum **within this family** is at b=1/4:

$$c_*=2\left(\frac{\Gamma(5/4)}{\Gamma(3/4)}\right)^2=1.0942198076132383194\ldots.$$

Thus liminf n(2-M_n) >= c_*>1, contradicting the coefficient-one conjecture if the argument withstands independent review. The little-o statement is for fixed a, not uniform at the parameter endpoints.

## 1. Classical inputs

Write P=P_m^(a,a), w(t)=(1-t^2)^a, p_m=P(1), and

$$d_m=\frac{m(m+2a+1)}{2(a+1)}.$$

Standard Jacobi identities give

$$(1-x^2)P''-2(a+1)xP'+m(m+2a+1)P=0,$$
$$p_m=\frac{\Gamma(m+a+1)}{\Gamma(a+1)\Gamma(m+1)},\qquad P'(1)/P(1)=d_m.$$

The Gaussian quadrature weights for w(t)dt at the zeros t_i of P satisfy

$$\lambda_i=\frac{K_m}{(1-t_i^2)P'(t_i)^2},\quad K_m=\frac{2^{2a+1}\Gamma(m+a+1)^2}{\Gamma(m+1)\Gamma(m+2a+1)}\to K_\infty=2^{2a+1}.$$

Orthogonality for a positive interior weight ensures that the m zeros are simple and interior; hence the nodes are admissible. The normalization, differential equation, derivative, and quadrature facts are classical, not claimed as new. See NIST DLMF [18.3](https://dlmf.nist.gov/18.3), [18.8](https://dlmf.nist.gov/18.8), [18.9](https://dlmf.nist.gov/18.9), and [3.5(v)](https://dlmf.nist.gov/3.5#v).

The Darboux formula ([DLMF 18.15.4_5](https://dlmf.nist.gov/18.15#E4_5)) is, uniformly on compact interior theta-intervals,

$$P_m(\cos\theta)=\frac{2^{a+1/2}}{\sqrt{\pi m}}(\sin\theta)^{-a-1/2}\cos((m+a+1/2)\theta-(a+1/2)\pi/2)+O(m^{-3/2}).$$

The endpoint-uniform Bessel expansion [18.15.6–7](https://dlmf.nist.gov/18.15#E6), symmetry, and the endpoint bound [18.14.1](https://dlmf.nist.gov/18.14#E1) imply

$$|P_m(x)|\le C m^{-1/2}(1-x^2)^{-a/2-1/4},\qquad |P_m(x)|\le C m^a.$$

For the first estimate, the Bessel bounds J_a(m theta)=O((m theta)^(-1/2)) for theta >= c/m and O((m theta)^a) for theta <= c/m give the two regimes. Constants depend on fixed a. No interior formula is assumed uniform at an endpoint.

## 2. Exact cardinal-square identity

Let W=(1-x^2)P. Hermite interpolation of the constant polynomial gives

$$1=\sum_{r\in X}\left[1-\frac{W''(r)}{W'(r)}(x-r)\right]l_r(x)^2.$$

The sum has value 1 and derivative 0 at every node, and degree at most 2|X|-1. Subtracting 1 produces a polynomial with |X| double zeros, proving the identity.

At interior nodes W''/W'=2b t_i/(1-t_i^2). At the endpoints the ratios are beta_m and -beta_m, where beta_m=1+2d_m. The endpoints contribute

$$-\frac{\beta_m}{2p_m^2}(1-x^2)P(x)^2$$

to the sum of cardinal squares minus 1.

Define

$$Q_m(x)=\int_{-1}^1\frac{P(x)-P(t)}{x-t}w(t)dt,\quad R_m=Q_m/P,$$
$$C_m=\sum_i\frac{\lambda_i}{1-t_i},\qquad D_m=\sum_i\frac{\lambda_i}{(1-t_i)^2}.$$

The difference quotient is a polynomial in t of degree m-1. Gaussian exactness gives R_m(x)=sum_i lambda_i/(x-t_i). Symmetry and partial fractions yield

$$(1-x^2)^2\sum_i\frac{\lambda_i t_i}{(1-t_i^2)^2(x-t_i)}=xR_m(x)-\frac{C_m}2(1+x^2)-\frac{D_m}2(1-x^2).$$

Consequently the following is an exact polynomial identity:

$$\begin{aligned}
S_m(x):=\sum_{r\in X}l_r(x)^2
=1+\frac{2b}{K_m}\left[xP Q_m-\frac{C_m}2(1+x^2)P^2-\frac{D_m}2(1-x^2)P^2\right]
-\frac{\beta_m}{2p_m^2}(1-x^2)P^2.
\end{aligned}$$

The rational calculation away from the nodes proves equality everywhere by removable singularities.

## 3. Endpoint corrections

Let C_inf=int w(t)/(1-t)dt and D_inf=int w(t)/(1-t)^2dt. These are finite since a>1. Rodrigues' formula and m integrations by parts give

$$\int\frac{P(t)w(t)}{1-t}dt=2^{2a}B(a,m+a+1),$$
$$\int\frac{P(t)w(t)}{(1-t)^2}dt=(m+1)2^{2a-1}B(a-1,m+a+1).$$

All integrals without displayed bounds are over [-1,1]. Boundary terms vanish. From the Stieltjes-transform error J(z)/P(z), where J(z)=int P(t)w(t)/(z-t)dt, obtain

$$\Delta C_m:=C_\infty-C_m=\frac{2^{2a}\Gamma(a)\Gamma(a+1)\Gamma(m+1)}{\Gamma(m+2a+1)}=O(m^{-2a}),$$
$$\Delta D_m:=D_\infty-D_m=\Delta C_m\left[d_m+\frac{(m+1)(m+2a)}{2(a-1)}\right]=O(m^{2-2a}).$$

The second identity follows by differentiating J(z)/P(z) at z=1. The endpoint integrals are finite, so this derivative is justified.

Splitting at distance m^(-2) from each endpoint, the Jacobi bounds imply

$$\int P^2=O(m^{2a-2}),\qquad J_m:=\int(1-x^2)P^2=O(m^{-1}).$$

The latter uses 1/2-a>-1. Replacing C_m,D_m by C_inf,D_inf in the integrated exact identity therefore changes it by O(m^(-2))+O(m^(1-2a))=o(m^(-1)). The endpoint-cardinal term has integral beta_m J_m/(2p_m^2)=O(m^(1-2a))=o(m^(-1)).

## 4. A vanishing mixed term

Use H_f(x)=pv int f(t)/(x-t)dt. Then Q_m=P H_w-H_(wP). We need

$$T_m:=\int xP(x)H_{wP}(x)dx=o(m^{-1}).$$

The signed measures dnu_m=sqrt(m)P_m(x)dx have uniformly bounded total variation and converge weakly to zero. Indeed the bound by C(1-x^2)^(-a/2-1/4) is integrable since a<3/2. Darboux and Riemann–Lebesgue give weak convergence on compact interior intervals; this common bound controls the removed endpoints uniformly.

Symmetrize first with the exclusion |x-t|>epsilon and then take epsilon down to zero:

$$T_m=\frac12\iint P(x)P(t)\mathcal K(x,t)\,dt\,dx,\quad \mathcal K(x,t)=\frac{xw(t)-tw(x)}{x-t}.$$

Since a>1, w is C^1 on the closed interval. The kernel extends continuously to the closed square with diagonal value w(x)-xw'(x). Dominated convergence justifies the symmetric integral. Uniform approximation of this continuous kernel by finite sums f_j(x)g_j(t), weak convergence of nu_m, and bounded total variation now give mT_m ->0.

## 5. Evaluate the surviving limit

Put

$$B_a(x)=xH_w(x)-\frac{C_\infty}2(1+x^2)-\frac{D_\infty}2(1-x^2).$$

The preceding steps reduce the functional to

$$I(X_{m+2,a})-2=\frac{2b}{K_m}\int B_a(x)P_m(x)^2dx+o(m^{-1}).$$

Let v_b(t)=(1-t^2)^(b-1) and V_b=int v_b=B(1/2,b). The continuous partial-fraction identity gives

$$B_a(x)=(1-x^2)^2[xH_{v_b}(x)-V_b].$$

Here is a direct evaluation of the needed transform. For G(z)=int v_b(t)/(z-t)dt, integration by parts applied to (1-t^2)^b/(z-t) gives

$$(1-z^2)G'(z)-2(1-b)zG(z)=(2b-1)V_b.$$

The real boundary value inside the interval is the smooth principal-value transform. It is odd. Solve this ODE with H_(v_b)(0)=0:

$$H_{v_b}(x)=(2b-1)V_b(1-x^2)^{b-1}A_b(x),\qquad A_b(x)=\int_0^x(1-s^2)^{-b}ds.$$

A_b is bounded at the endpoints since b<1. Therefore B_a(x)=O((1-x^2)^a).

On compact interior intervals, the squared Darboux formula and averaging of cos^2 give

$$m\int B_aP_m^2\longrightarrow\frac{K_\infty}{2\pi}\int (1-x^2)^{1/2-b}[xH_{v_b}(x)-V_b]dx.$$

This also holds on the full interval: the absolute integrand m B_a P_m^2 is bounded by C(1-x^2)^(-1/2), using the global Jacobi bound and the endpoint order of B_a. One removes the endpoints uniformly, takes the interior oscillatory limit, and restores them. A pointwise limit of cos^2 is not used.

Let U_b=B(1/2,3/2-b). An integration by parts, with zero boundary term because A_b is bounded, gives

$$\int\frac{xA_b(x)}{\sqrt{1-x^2}}dx=\int(1-x^2)^{1/2-b}dx=U_b.$$

Thus

$$\int(1-x^2)^{1/2-b}[V_b-xH_{v_b}(x)]dx=2(1-b)V_bU_b.$$

Combining these identities proves

$$\lim_m m[2-I(X_{m+2,a})]=\frac{2b(1-b)}\pi B(1/2,b)B(1/2,3/2-b)=c(b).$$

Replacing m by n=m+2 changes no first-order coefficient.

## 6. Why c(b)>1

Let g(b)=log c(b). The gamma identities give g(0)=g(1/2)=0 by continuous extension and

$$g''(b)=\psi_1(1+b)-\psi_1(1/2+b)+\psi_1(3/2-b)-\psi_1(1-b)<0.$$

Indeed psi_1(t)=sum_(k>=0)(t+k)^(-2) is strictly decreasing. Hence g is strictly concave and positive between its endpoints. Symmetry c(b)=c(1/2-b) gives the unique maximum in this family at b=1/4. See also [DLMF 5.15](https://dlmf.nist.gov/5.15). This is an analytic inequality, not a floating-point sign test.

## Numerical and exact checks

For a=5/4, independent node-based Gaussian integration and exact rational evaluation of the polynomial identity agree. Selected values of n[2-I(X_(n,5/4))] are:

| n | scaled deficit |
|---:|---:|
|16|1.10096866233836|
|32|1.09692253175326|
|64|1.09540481429866|
|128|1.09477083805962|
|256|1.09448495769493|
|512|1.09434978989702|

Author-side executed checks included 56 rational Jacobi ODE/orthogonality cases, 48 exact endpoint quadrature-error cases, 22 classical Legendre–Lobatto controls, direct symbolic Lagrange integrations at n=4,5, and 28 independent quadrature comparisons (maximum absolute discrepancy 1.6e-15). These finite checks are diagnostic support, not the proof of the infinite limit.

## Remaining boundaries

- No Lean formalization or independent human verification is claimed.
- The exact minimization problem and the globally optimal asymptotic coefficient remain unresolved by this manuscript.
- No comprehensive novelty or priority determination has been completed. Searches found no prize PR/issue with the exact JSP-000938 ID at the time checked, but this is not proof of absence of earlier work.
- The original five-comment discussion thread was inaccessible through the available web reader. A January 2026 preprint by Rafik Zeraoulia on the same problem was located; it makes conditional endpoint-universality claims and is not used here: https://www.preprints.org/manuscript/202601.0875 .
- No award application is made. Prize scope, originality, verification, candidate publication, review and confirmation are distinct from the author-side argument.

Additional bibliography: P. Erdős, J. Szabados, A. K. Varma and P. Vértesi, *On an interpolation theoretical extremal problem*, Studia Sci. Math. Hungar. (1994), 55–60, as listed by the original problem page. The original paper was not independently retrieved in this session. Gamma-ratio asymptotics: https://dlmf.nist.gov/5.11#iii .
