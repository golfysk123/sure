#!/usr/bin/env python3
"""Supporting scalar checks; not a formal verification of the analytic theorem."""
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, math, os

@lru_cache(None)
def H(n):
    if n < 0: raise ValueError('negative index')
    return sum((F(1,k) for k in range(1,n+1)), F(0))
def L(n): return H(n+1)**2
def d(n): return 2*H(n+1)/F(n+2)+F(1,(n+2)**2)
def check(p, message):
    if not p: raise ArithmeticError(message)

def enclosure(n, r, cut):
    if n < 0 or r < 0 or cut < 1: raise ValueError('invalid input')
    term=total=F(1)
    for m in range(1,cut+1):
        term*=r*L(n+m)/m
        total+=term
    q=r*L(n+cut+1)/F(cut+1)
    if q>=1: raise ValueError('tail does not contract')
    # Discrete concavity proves that all subsequent term ratios are <= q.
    return total,total+term*q/(1-q)

def run():
    tangent=coefficient=tail_count=0
    for n in range(81):
        check(L(n+1)-L(n)==d(n),'increment identity')
        rhs=2*(H(n+1)-1)/F((n+2)*(n+3))+F(2*n+5,(n+2)**2*(n+3)**2)
        check(d(n)-d(n+1)==rhs and rhs>0,'concavity identity')
        for j in range(31):
            check(L(n)<=L(n+j)<=L(n)+j*d(n),'tangent bound')
            tangent+=1
    for n in [0,1,2,3,5,10,20,40]:
        actual=major=F(1);k=d(n)/L(n)
        for m in range(1,41):
            actual*=L(n+m)/m;major*=L(n)*(1+m*k)/m
            check(actual<=major,'majorant coefficient')
            rising=math.prod((1+1/k+j for j in range(m)))
            check(major==d(n)**m*rising/math.factorial(m),'binomial coefficient identity')
            check(L(n+m+1)/F(m+1)<L(n+m)/m,'tail-ratio monotonicity')
            coefficient+=1
    for n in [0,1,2]:
        for r in [F(1,8),F(1,4),F(1,2)]:
            q=d(n)*r;check(q<1,'majorant domain')
            low,high=enclosure(n,r,24);power=1+L(n)/d(n)
            check(low<=high,'enclosure order')
            check(high**power.denominator<(1-q)**(-power.numerator),'infinite majorant enclosure')
            tail_count+=1
    try: enclosure(0,F(10),1)
    except ValueError: pass
    else: raise ArithmeticError('invalid tail accepted')
    for n in [0,1,10]:
        check(2*H(n+1)/F(n+3)+F(1,(n+3)**2)!=L(n+1)-L(n),'mutated formula not detected')
    return {'tangent_cases':tangent,'coefficient_cases':coefficient,'infinite_tail_enclosure_cases':tail_count,
            'negative_controls':4}

if __name__=='__main__':
    result={'status':'exact supporting checks passed','checks':run(),
            'analytic_theorem_machine_verified':False,'independent_human_review':False,
            'novelty_confirmed':False,'prize_eligibility_confirmed':False,
            'commit':os.environ.get('GITHUB_SHA'),'run_id':os.environ.get('GITHUB_RUN_ID'),
            'checked_at_utc':datetime.now(timezone.utc).isoformat(),
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    out=Path('evidence');out.mkdir(exist_ok=True)
    (out/'checks.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
