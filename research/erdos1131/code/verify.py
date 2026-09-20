#!/usr/bin/env python3
"""Independent finite checks. No numerical limit is called a mathematical proof."""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import time
import numpy as np
import scipy
from scipy.special import roots_jacobi, roots_legendre
import sympy as sp
from exact import add, scale, mul, integ, value, deriv, jacobi, compute

def require(cond, label):
    if not cond:
        raise ArithmeticError(label)

def moments(a, count):
    out=[F(1)]
    for k in range(1,count+1):out.append(out[-1]*F(2*k-1,2)/(a+F(2*k+1,2)))
    return out

def weighted_int(poly, mu):
    return sum((x*mu[i//2] for i,x in enumerate(poly) if i%2==0),F(0))

def independent_float(n,a):
    x=np.r_[-1.,roots_jacobi(n-2,float(a),float(a))[0],1.]
    y,w=roots_legendre(n+3)
    gap=x[:,None]-x[None,:];np.fill_diagonal(gap,1.)
    logw=-np.log(np.abs(gap)).sum(axis=1)
    bary=np.exp(logw-logw.max())*np.prod(np.sign(gap),axis=1)
    diff=y[:,None]-x[None,:]
    match=diff==0;safe=diff.copy();safe[match]=1
    temp=bary/safe
    L=temp/temp.sum(axis=1)[:,None]
    for i in np.flatnonzero(match.any(axis=1)):L[i]=match[i]
    return float(np.sum(w[:,None]*L*L))

def direct_symbolic(n):
    x=sp.Symbol('x')
    if n==4:
        r=sp.sqrt(sp.Rational(2,11));nodes=[-1,-r,r,1]
    elif n==5:
        r=sp.sqrt(sp.Rational(2,5));nodes=[-1,-r,0,r,1]
    else:raise ValueError('Only independently hand-specified n=4,5 controls')
    polynomials=[]
    for i,xi in enumerate(nodes):
        ell=sp.prod((x-xj)/(xi-xj) for j,xj in enumerate(nodes) if i!=j)
        polynomials.append(sp.expand(ell))
    total=sp.Poly(sp.simplify(sum(ell**2 for ell in polynomials)),x)
    return sp.simplify(sum(c*sp.Rational(2,k[0]+1) for k,c in total.terms() if k[0]%2==0))

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--out',type=Path,default=Path('verification.json'))
    args=parser.parse_args();start=time.monotonic();checks=[]
    count=0
    for a in [F(1),F(5,4),F(7,5),F(3,2)]:
        for m in range(1,15):
            p=jacobi(m,a)
            ode=add(add(mul(deriv(deriv(p)),[1,0,-1]),scale([F(0)]+deriv(p),-2*(a+1))),scale(p,m*(m+2*a+1)))
            require(all(c==0 for c in ode),'Jacobi differential equation')
            mu=moments(a,2*m)
            for k in range(m):require(weighted_int([F(0)]*k+p,mu)==0,'Jacobi orthogonality')
            count+=1
    checks.append({'check':'rational Jacobi ODE and all lower-degree weighted moments','cases':count,'passed':True})
    count=0
    for a in [F(5,4),F(7,5),F(3,2)]:
        for m in range(1,17):
            p=jacobi(m,a);mu=moments(a,m);q=[F(0)]*m
            for j,pj in enumerate(p):
                for t in range(0,j,2):q[j-1-t]+=pj*mu[t//2]
            p1=value(p);dp=value(deriv(p));q1=value(q)
            C=q1/p1;D=(q1*dp-value(deriv(q))*p1)/(p1*p1)
            Cin=(2*a+1)/(2*a);Din=(2*a+1)/(2*(a-1))
            delta=Cin
            for k in range(m):delta*=F(k+1)/(2*a+1+k)
            require(Cin-C==delta,'C quadrature error')
            require(Din-D==delta*(dp/p1+F(m+1)*(m+2*a)/(2*(a-1))),'D quadrature error')
            count+=1
    checks.append({'check':'exact endpoint C,D quadrature-error identities','cases':count,'passed':True})
    for n in range(3,25):require(F(compute(n,F(1))['I'])==2-F(2,2*n-1),'classical Lobatto control')
    checks.append({'check':'classical Legendre-Lobatto exact value','cases':22,'passed':True})
    for n in [4,5]:
        rational=F(compute(n)['I'])
        require(direct_symbolic(n)==sp.Rational(rational.numerator,rational.denominator),'direct Lagrange integral')
    checks.append({'check':'direct symbolic product-definition Lagrange integrals, independent nodes','n':[4,5],'passed':True})
    rows=[];maxerror=0.
    for a in [F(1),F(5,4),F(7,5),F(3,2)]:
        for n in [3,4,5,8,16,32,64]:
            exact=compute(n,a);quad=independent_float(n,a);error=abs(quad-exact['I_float'])
            require(error<2e-11,'independent quadrature agreement')
            maxerror=max(maxerror,error)
            rows.append({'n':n,'a':str(a),'exact_I':exact['I'],'quadrature_I':quad,'absolute_error':error})
    checks.append({'check':'independent root-based barycentric Gaussian integration','cases':len(rows),'max_absolute_error':maxerror,'passed':True})
    # This is numerical support, not an independent proof of the limit.
    import mpmath as mp
    mp.mp.dps=60;c=2*(mp.gamma(mp.mpf(5)/4)/mp.gamma(mp.mpf(3)/4))**2
    table=[{'n':n,'I':independent_float(n,F(5,4))} for n in [16,32,64,128,256,512]]
    for row in table:row['n_times_deficit']=row['n']*(2-row['I'])
    result={'status':'finite checks passed','proof_status':'analytic manuscript only; no Lean proof or independent human review',
            'checks':checks,'crosschecks':rows,'predicted_limit_decimal':str(c),'numerical_table':table,
            'seconds':round(time.monotonic()-start,3),
            'versions':{'numpy':np.__version__,'scipy':scipy.__version__,'sympy':sp.__version__,'mpmath':mp.__version__},
            'sources_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in Path(__file__).parent.glob('*.py')}}
    args.out.parent.mkdir(parents=True,exist_ok=True);args.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ['crosschecks']},indent=2))

if __name__=='__main__':main()
