#!/usr/bin/env python3
"""Diagnostics, not formal certification, for the deterministic derivative construction."""
from __future__ import annotations
import argparse, hashlib, json, time
from pathlib import Path
from datetime import datetime, timezone
import mpmath as mp
mp.mp.dps = 100
alpha = mp.sqrt(2)

def require(value, message):
    if not value:
        raise ArithmeticError(message)

def harmonic(k):
    if k < 1:
        raise ValueError('positive harmonic index required')
    return mp.digamma(k + 1) + mp.euler

def phase(k):
    return mp.exp(2 * mp.pi * mp.j * alpha * k)

def profile(n, z, limit=400):
    h = harmonic(n + 1)
    lam, r = mp.sqrt(h), abs(z)
    d = 1 / ((n + 2) * (mp.sqrt(h + 1 / mp.mpf(n + 2)) + lam))
    require(d * r < 1, 'majorant outside domain')
    kap = d / lam
    eps = -(1 + 1 / kap) * mp.log1p(-d * r) - lam * r
    bound = mp.exp(lam * r) * mp.expm1(eps)
    a = g = mp.mpc(1)
    ta = tg = mp.mpc(1)
    ma = mg = mp.mpf(1)
    for k in range(1, limit + 1):
        h += 1 / mp.mpf(n + k + 1)
        multiplier = mp.sqrt(h)
        ta *= multiplier * z / k
        tg *= lam * z / k
        ph = phase(k * k + 2 * n * k)
        a += ph * ta
        g += ph * tg
        ma *= multiplier * r / k
        mg *= lam * r / k
        ra = mp.sqrt(h + 1 / mp.mpf(n + k + 2)) * r / (k + 1)
        rg = lam * r / (k + 1)
        if ra < 1 and rg < 1:
            ea, eg = ma * ra / (1 - ra), mg * rg / (1 - rg)
            if max(ea, eg) < mp.mpf('1e-80'):
                break
    else:
        raise ArithmeticError('tail budget exceeded')
    discrepancy = abs(a - g)
    require(discrepancy + ea + eg <= bound, 'comparison bound violated')
    return {'n': n, 'z': str(z), 'lambda': str(lam), 'terms': k,
            'observed_difference': str(discrepancy), 'analytic_bound': str(bound),
            'truncation_tail_bound_sum': str(ea + eg)}

def run():
    rows = [profile(n, z) for n in [10, 100, 1000, 10**6]
            for z in [mp.mpc('.3', '.4'), mp.mpc(1), mp.mpc(-1, '.75'), mp.mpc(0, 2)]]
    concavity = 0
    for n in list(range(60)) + [100, 1000, 10**6]:
        h = harmonic(n + 1)
        v = mp.sqrt(h)
        nxt = mp.sqrt(h + 1 / mp.mpf(n + 2))
        after = mp.sqrt(h + 1 / mp.mpf(n + 2) + 1 / mp.mpf(n + 3))
        require(0 < after - nxt < nxt - v, 'concavity failed')
        d = nxt - v
        require(abs(d - 1 / ((n + 2) * (nxt + v))) < mp.mpf('1e-90'), 'increment identity')
        for j in [0, 1, 2, 5, 10, 25]:
            require(mp.sqrt(harmonic(n + j + 1)) <= v + j * d + mp.mpf('1e-90'), 'tangent bound')
            concavity += 1
    degree = 30
    weights = [mp.mpf(1)]
    for k in range(1, degree + 1):
        weights.append(weights[-1] * mp.sqrt(harmonic(k + 1)))
    polynomial = 0
    for n in range(9):
        for z in [mp.mpc('.2', '.3'), mp.mpc(-1), mp.mpc(0, 1)]:
            direct = mp.fsum(phase(k * k) * weights[k] * z**(k - n) / mp.factorial(k - n)
                            for k in range(n, degree + 1))
            direct /= phase(n * n) * weights[n]
            product, shifted = mp.mpf(1), mp.mpc(1)
            for j in range(1, degree - n + 1):
                product *= mp.sqrt(harmonic(n + j + 1))
                shifted += phase(j * j + 2 * n * j) * product * z**j / mp.factorial(j)
            require(abs(direct - shifted) < mp.mpf('1e-85') * (1 + abs(shifted)), 'polynomial derivative')
            polynomial += 1
    negative = 0
    for n, k in [(1, 1), (3, 2), (7, 5)]:
        require(abs(phase((n + k)**2 - n * n) - phase(k * k)) > mp.mpf('1e-8'), 'missing phase not detected')
        negative += 1
    try:
        profile(0, mp.mpc(100))
    except ArithmeticError:
        negative += 1
    else:
        raise ArithmeticError('invalid domain accepted')
    return {'status': 'high-precision supporting checks passed', 'precision_decimal_digits': 100,
            'phase_profile_cases': len(rows), 'concavity_tangent_cases': concavity,
            'independent_polynomial_cases': polynomial, 'negative_controls': negative, 'rows': rows,
            'full_analytic_theorem_machine_verified': False, 'interval_arithmetic_certification': False,
            'scope': 'Diagnostics only; the unrestricted argument uses the cited Eremenko-Ostrovskii theorem and the analytic addendum.'}

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--out', type=Path, required=True)
    args = p.parse_args()
    started = time.monotonic()
    result = run()
    result.update(checked_at_utc=datetime.now(timezone.utc).isoformat(),
                  elapsed_seconds=round(time.monotonic() - started, 3),
                  source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k: v for k, v in result.items() if k != 'rows'}, indent=2))
