#!/usr/bin/env python3
"""Exact rational evaluation for endpoints plus zeros of a symmetric Jacobi polynomial.

No root approximation is used. This evaluates the manuscript's exact identity;
it is not itself a formal proof of its asymptotic conclusion.
"""
from fractions import Fraction as F
from math import factorial
import argparse, json, time
from pathlib import Path
# Polynomials in ascending coefficients; all arithmetic exact.
def add(a,b):
 c=[F(0)]*max(len(a),len(b))
 for i,x in enumerate(a):c[i]+=x
 for i,x in enumerate(b):c[i]+=x
 while len(c)>1 and not c[-1]:c.pop()
 return c

def scale(a,s):return [x*s for x in a]
def mul(a,b):
 c=[F(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]+=x*y
 return c

def integ(a):return sum((2*x/F(i+1) for i,x in enumerate(a) if i%2==0),F(0))
def value(a,x=F(1)):
 s=F(0)
 for t in a[::-1]:s=s*x+t
 return s

def deriv(a):return [i*x for i,x in enumerate(a)][1:]
def jacobi(m,a):
 # Symmetric Jacobi recurrence (DLMF 18.9.2); explicit rational recurrence.
 p0=[F(1)]
 if m==0:return p0
 p1=[F(0),a+1]
 for n in range(1,m):
  lhs=2*(n+1)*(n+2*a+1)*(2*n+2*a)
  u=(2*n+2*a+1)*(2*n+2*a)*(2*n+2*a+2)
  v=2*(n+a)**2*(2*n+2*a+2)
  p2=scale(add(scale([F(0)]+p1,u),scale(p0,-v)),1/lhs)
  p0,p1=p1,p2
 return p1

def compute(n,a=F(5,4)):
 m=n-2;p=jacobi(m,a)
 mu=[F(1)]
 for k in range(1,m+1):mu.append(mu[-1]*F(2*k-1,2)/(a+F(2*k+1,2)))
 q=[F(0)]*m
 for j,pj in enumerate(p):
  for t in range(0,j,2):q[j-1-t]+=pj*mu[t//2]
 p1=value(p); dp1=value(deriv(p)); q1=value(q); dq1=value(deriv(q))
 c=q1/p1;d=(q1*dp1-dq1*p1)/p1**2
 K=2*a+1
 for j in range(m):K*=((a+1+j)**2)/((j+1)*(2*a+1+j))
 pp=mul(p,p);J=integ(mul(pp,[1,0,-1])); B=1+2*dp1/p1
 S=integ([F(0)]+mul(p,q))-c*integ(mul(pp,[1,0,1]))/2-d*J/2
 ans=2+2*(a-1)*S/K-B*J/(2*p1*p1)
 return {'n':n,'alpha':str(a),'I':str(ans),'n_deficit':str(n*(2-ans)),
         'I_float':float(ans),'n_deficit_float':float(n*(2-ans))}
if __name__ == '__main__':
 parser = argparse.ArgumentParser(description='Exact rational evaluation of the Jacobi–Lobatto interpolation functional.')
 parser.add_argument('--out', type=Path, default=Path('exact-results.json'))
 args = parser.parse_args()
 t=time.monotonic(); rows=[]
 for n in [4,8,16,32,64]:
  r=compute(n); rows.append(r)
  print(n,r['I_float'],r['n_deficit_float'],flush=True)
 args.out.parent.mkdir(parents=True, exist_ok=True)
 args.out.write_text(json.dumps({'rows':rows,'elapsed_seconds':time.monotonic()-t,
  'scope':'Exact finite polynomial identities only; the asymptotic proof is in the manuscript.'},indent=2)+'\n')
