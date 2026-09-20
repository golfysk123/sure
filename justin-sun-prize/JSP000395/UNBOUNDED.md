# Unbounded density amplification for finite sets of multiples

Research note, 20 September 2026. Prepared in the `golfysk123` / ChatGPT research session. This note supplies a complete mathematical argument. Independent specialist review and novelty are not established. It does not announce an award, claim first priority, or claim a complete Lean formalization.

## Prior work and contribution boundary

The corrected multiples version of Erdős #488 / JSP-000395 asks whether F_A(m)/m < 2 F_A(n)/n for every finite nonempty set A of positive integers and m>n>=max(A), where F_A(x) counts positive integers at most x divisible by at least one member of A.

Declan Gessel's public September 2026 smooth-number construction already refutes that original inequality. Its mathematical discovery and Lean formalization are not this account's work. The construction below adapts the odd-smooth/power-of-two lifting mechanism to unbounded amplification, a primitive dyadic band, arbitrary separation between n and max(A), and limiting natural density. An exponent-box argument supplies an explicit sufficient scale. We have not established first priority for these refinements.

Sources:
- Original corrected question and discussion: https://www.erdosproblems.com/488 and https://www.erdosproblems.com/forum/thread/488 . The discussion considers an unspecified replacement constant, m tending to infinity, and max(A)=o(n).
- Gessel's earlier public note and exact-statement adapter: https://gist.github.com/declangessel/d8e15e5ff1b6c7e99e3d86d7c66f1d08 .
- Earlier pinned Lean source: https://github.com/WoshuaJolk/jig-verifier/blob/ccf4a26cb8a8c49f476d44304070a2b677da4d7e/Submissions/ErdosMultiplesSmoothRefuted/Counterexample.lean .

## Theorem

Let

$$F_A(x)=\#\{j\in\mathbb N:1\le j\le x,\ \exists a\in A\ (a\mid j)\}.$$

For every real C>0, D>=1 and X>=0, there exist positive integers T,n,m and a finite nonempty set A such that:

- A is contained in (T,2T], contains 2T, and min(A)>X.
- No distinct members of A divide one another.
- m>n>=D max(A), and (F_A(m)/m)/(F_A(n)/n)>C.
- The natural density delta(A) of the multiples of A exists and delta(A)/(F_A(n)/n)>C.

All denominators are positive. A varies with C,D,X; this is not a claim of unbounded oscillation for one fixed periodic set. The construction uses composite generators and does not address the primes-only restriction.

## Parameters

Choose an even integer r>=2, set B=2^r, and require

$$\sqrt B/(4r)>C,\qquad B/2\ge D.$$

For example, s=ceil(8C)+ceil(D)+4 and r=2s work: 2^s>=s^2 for integers s>=4 by induction, so 2^s/(8s)>C, while 2^(2s-1)>=s>=D.

Let P be all primes at most B, S=P minus {2}, and

$$d=|S|\ge1,\quad Q=\prod_{p\in S}p,\quad \kappa=\varphi(Q)/Q=\prod_{p\in S}(1-1/p).$$

The totient product follows by inclusion-exclusion for the squarefree integer Q. Call a positive integer S-smooth when all its prime factors belong to S, including 1, and let H(t) count such integers at most t.

Choose

$$L=r(rd+r+1)^{d-1}+\lfloor X\rfloor+1,\qquad k=dL,\qquad T=B^k.$$

Then L>=r(rd+r+1)^(d-1) and T>X, since L>X and B^(dL)>=2^L>=L+1.

## 1. Explicit smooth-count doubling

We show H(BT)<=2H(T). Every exponent vector with 0<=e_p<=L for p in S gives a different smooth number, and its product is at most B^(dL)=T. Hence

$$H(T)\ge(L+1)^d.$$

Fix p_0 in S. For a smooth u in (T,BT], fix the exponents at primes other than p_0. Each of those d-1 exponents is at most r(k+1), because u<=2^(r(k+1)) and every prime is at least 2.

For a fixed choice of those coordinates, at most r exponents at p_0 are possible. Otherwise two exponents differ by at least r; the larger number is at least p_0^r>=B times the smaller, so it exceeds BT, as the smaller is strictly above T. Consequently

$$H(BT)-H(T)\le r\bigl(r(k+1)+1\bigr)^{d-1}.$$

Since k=dL and r(k+1)+1<= (rd+r+1)(L+1),

$$H(BT)-H(T)\le r(rd+r+1)^{d-1}(L+1)^{d-1}\le(L+1)^d\le H(T).$$

This includes d=1. It is a finite exponent-box proof, not an asymptotic estimate or an assumption that a search succeeds.

## 2. Coprime proportion

The odd primes at most B are among 3,5,...,B-1. Adding the odd composite factors, each strictly between 0 and 1, can only decrease the product. With M=B/2-1,

$$\kappa\ge\prod_{j=1}^{M}\frac{2j}{2j+1}.$$

Since (2j)^2>=(2j-1)(2j+1),

$$\left(\prod_{j=1}^{M}\frac{2j}{2j+1}\right)^2\ge\prod_{j=1}^{M}\frac{2j-1}{2j+1}=\frac1{B-1}.$$

Positivity therefore gives kappa>=1/sqrt(B-1)>1/sqrt(B). No prime number theorem or Mertens estimate is needed.

## 3. The primitive band and early count

Set

$$A=\{a\in\mathbb N:T<a\le2T,\ a\text{ is P-smooth}\},\qquad n=BT.$$

Since T is a power of two, 2T belongs to A. Thus max(A)=2T and F_A(n)>0. If a<b in A and a divides b, then b>=2a>2T, impossible. Also n/max(A)=B/2>=D.

If j<=BT is covered by A, write j=ac with a in A. Then c is a positive integer less than B, so it has no prime factor greater than B. Thus j is P-smooth and lies in (T,BT]. Write j=2^e u uniquely, with u S-smooth and u<=BT. For each u, at most r exponents occur, by the same multiplicative-interval argument. Therefore

$$F_A(n)\le rH(BT)\le2rH(T).$$

Only containment of the covered set in this window is needed; equality with the entire smooth window is not assumed.

## 4. Disjoint late multiples

For each S-smooth u<=T, choose the least e(u)>=0 with c_u=2^e(u)u>T. Existence follows from unbounded powers of two. Minimality and u<=T give T<c_u<=2T, so c_u belongs to A.

Let R consist of the integers q in [1,BQ] coprime to Q. There are B complete residue blocks and hence |R|=B phi(Q).

The map (u,q) to c_u q is injective. For every prime p in S, the p-adic valuation of c_u q equals that of u, because neither 2 nor q has p as a prime factor. Equality of two images therefore forces equality of all prime valuations of the two S-smooth numbers, so they agree. The corresponding c_u are equal and positive, and cancellation gives equality of q as well.

Set m=2TBQ. Every image is a positive covered integer at most m. Thus

$$F_A(m)\ge B\varphi(Q)H(T).$$

Moreover m/n=2Q>=2, so m>n without any further primorial estimate.

## 5. Finish

With h=H(T)>=1, the two count bounds and positivity yield

$$\frac{nF_A(m)}{mF_A(n)}\ge\frac{(BT)B\varphi(Q)h}{(2TBQ)2rh}=\frac{B\kappa}{4r}>\frac{\sqrt B}{4r}>C.$$

This proves all finite assertions.

For the density conclusion, the set of multiples of A is periodic with positive period lcm(A), so delta(A) exists. For each of the finitely many S-smooth u<=T, the set

$$E_u=\{c_uq:q\ge1,\ \gcd(q,Q)=1\}$$

has density kappa/c_u, by counting residue blocks. The E_u are pairwise disjoint by the preceding injection argument, and their union is contained in the multiples of A. Therefore

$$\delta(A)\ge\kappa\sum_{u\le T,\ u\ S\text{-smooth}}\frac1{c_u}\ge\frac{\kappa H(T)}{2T}.$$

Dividing by F_A(n)/n<=2rH(T)/(BT) gives the same strict bound >C. Finite additivity is legitimate because T is fixed and only finitely many u are used. In particular, for this A,n the finite ratio exceeds C for all sufficiently large m. This completes the proof.

## Exact symbolic instance

The sharper finite product at r=10, B=1024 has d=171, and, with Phi the product of p-1 over odd primes at most 1024,

$$4129(40Q)<1000(1024\Phi).$$

Choose L=10*1721^170, k=1710*1721^170, T=1024^k, A as above, n=1024T and m=2048TQ. The complete argument then gives

$$n=512\max(A),\qquad \frac{F_A(m)/m}{F_A(n)/n}>4129/1000>4>2.$$

The limiting-density ratio has the same bound. These are exactly specified finite objects, not an enumerated list of all elements of A or evaluated exact counts. No practical-size or smallest-counterexample claim is made. The earlier Gessel construction has a smaller proven search bound for its original fixed-constant target.

## What was actually checked

The authoring session executed two prime-generation methods, two smooth-number enumerations, exact finite shell and early-count tests, 20,528 disjoint-lift pairs, 42 exact inclusion-exclusion density comparisons, and negative controls. Python normal and optimized runs passed. They are consistency checks, not the basis for the unbounded conclusion.

Official Lean 4.19.0 with Mathlib c44e0c8ee63ca166450922a373c7409c5d26b00b checked 14 supporting declarations: exponent span, primitive dyadic bands, arithmetic closure of the box estimate, a universal rational-product inequality, a parameter inequality, cross-multiplication, and numeric constants on an explicit factor list. Only propext, Classical.choice and Quot.sound appeared. Two deliberately false propositions were rejected. The prime-list completeness check was performed in Python, not silently assumed to follow from the constant theorem.

This does NOT establish a complete Lean formalization of the main theorem: the smooth-counting, image-disjointness and limiting-density bridges are not all formalized. There is no independent external-checker or human-review claim, no first-refutation claim, and no award claim. The full mathematical argument above is the research contribution submitted for scrutiny.
