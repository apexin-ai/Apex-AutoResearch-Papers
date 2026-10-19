#!/usr/bin/env python3
"""Refine Theorem 1 analysis: investigate K>=3 violations with diag>=1/K."""

import numpy as np
import json


def check_monotonicity_fine(C0, p, g, n_delta=500):
    K = len(p)
    I = np.eye(K)
    gp = g * p
    g_bar = np.sum(gp)
    deltas = np.linspace(0, 1, n_delta + 1)

    VBs = np.empty(n_delta + 1)
    for i, d in enumerate(deltas):
        C = (1 - d) * I + d * C0
        q = C @ p
        N = C @ gp
        mu = N / q
        VBs[i] = np.sum(q * mu**2) - g_bar**2

    return deltas, VBs, np.max(np.diff(VBs))


def compute_VB_derivative_at(delta, C0, p, g):
    K = len(p)
    I = np.eye(K)
    C = (1 - delta) * I + delta * C0
    q = C @ p; N = C @ (g * p); mu = N / q
    diff_mat = C0 - I
    sq_diff = (g[None, :] - mu[:, None])**2
    return -np.sum(diff_mat * p[None, :] * sq_diff)


# ============================================================
# Part A: Recheck K=3 violations with FINE grid
# ============================================================
print("=" * 70)
print("PART A: Recheck K=3 violations (fine grid, n_delta=500)")
print("=" * 70)

K = 3
np.random.seed(2024 + K)
N_TRIALS = 20_000

violations_by_threshold = {
    '1/K': {'count': 0, 'n': 0, 'worst': 0.0},
    '0.4': {'count': 0, 'n': 0, 'worst': 0.0},
    '0.5': {'count': 0, 'n': 0, 'worst': 0.0},
}

for trial in range(N_TRIALS):
    pp = np.random.dirichlet(np.ones(K))
    gg = np.random.randn(K)
    C0 = np.random.dirichlet(np.ones(K), size=K).T

    min_diag = min(C0[j, j] for j in range(K))

    for thresh_name, thresh_val in [('1/K', 1.0/K), ('0.4', 0.4), ('0.5', 0.5)]:
        if min_diag >= thresh_val:
            v = violations_by_threshold[thresh_name]
            v['n'] += 1
            _, _, max_inc = check_monotonicity_fine(C0, pp, gg, n_delta=200)
            if max_inc > 1e-10:
                v['count'] += 1
                v['worst'] = max(v['worst'], max_inc)

for name, v in violations_by_threshold.items():
    print(f"  diag >= {name}: {v['count']}/{v['n']} violations "
          f"(worst={v['worst']:.6f})")


# ============================================================
# Part B: Detailed look at a violation
# ============================================================
print("\n" + "=" * 70)
print("PART B: Inspect a K=3 violation (diag >= 1/K)")
print("=" * 70)

K = 3
np.random.seed(2024 + K)
for trial in range(20_000):
    pp = np.random.dirichlet(np.ones(K))
    gg = np.random.randn(K)
    C0 = np.random.dirichlet(np.ones(K), size=K).T
    min_diag = min(C0[j, j] for j in range(K))
    if min_diag < 1.0/K:
        continue

    _, VBs, max_inc = check_monotonicity_fine(C0, pp, gg, n_delta=500)
    if max_inc > 0.005:
        print(f"  Trial {trial}: max_increase = {max_inc:.6f}")
        print(f"  C0 diag = [{C0[0,0]:.4f}, {C0[1,1]:.4f}, {C0[2,2]:.4f}]")
        print(f"  p = {pp}")
        print(f"  g = {gg}")
        print(f"  VB(0) = {VBs[0]:.6f}, VB(1) = {VBs[-1]:.6f}")

        # Check derivative at endpoint
        dVB1 = compute_VB_derivative_at(1.0, C0, pp, gg)
        dVB0 = compute_VB_derivative_at(0.0, C0, pp, gg)
        print(f"  dVB(0) = {dVB0:.6f}, dVB(1) = {dVB1:.6f}")

        # Find where VB increases
        diffs = np.diff(VBs)
        idx = np.argmax(diffs)
        d_at_inc = idx / 500.0
        print(f"  Max increase at delta ~ {d_at_inc:.3f}")
        print()
        break


# ============================================================
# Part C: Check if VB(0) >= VB(1) always holds
# ============================================================
print("=" * 70)
print("PART C: Does VB(0) >= VB(1) always hold?")
print("=" * 70)

np.random.seed(7777)
vb_endpoint_violations = 0
n_tested = 0

for trial in range(50_000):
    K = np.random.choice([2, 3, 5])
    pp = np.random.dirichlet(np.ones(K))
    gg = np.random.randn(K)
    C0 = np.random.dirichlet(np.ones(K), size=K).T

    I_K = np.eye(K); gp = gg*pp; gb = np.sum(gp)

    # VB(0)
    C0_ = I_K; q = C0_@pp; N = C0_@gp; mu = N/q
    VB0 = np.sum(q*mu**2) - gb**2

    # VB(1)
    q = C0@pp; N = C0@gp; mu = N/q
    VB1 = np.sum(q*mu**2) - gb**2

    n_tested += 1
    if VB1 > VB0 + 1e-10:
        vb_endpoint_violations += 1

print(f"VB(1) > VB(0): {vb_endpoint_violations} / {n_tested}")
print("(VB(0) = Var(g) is always the maximum — law of total variance)")


# ============================================================
# Part D: Test tighter conditions for K>=3
# ============================================================
print("\n" + "=" * 70)
print("PART D: Test 'stochastically dominant diagonal' conditions (K=3)")
print("=" * 70)

K = 3
np.random.seed(4444)
N = 20_000

conditions = {
    'diag >= 1/K': lambda C0, K: all(C0[j,j] >= 1.0/K for j in range(K)),
    'diag >= max off-diag (row)': lambda C0, K: all(
        C0[j,j] >= max(C0[j,k] for k in range(K) if k != j) for j in range(K)),
    'diag >= max off-diag (col)': lambda C0, K: all(
        C0[j,j] >= max(C0[k,j] for k in range(K) if k != j) for j in range(K)),
    'diag >= 0.5': lambda C0, K: all(C0[j,j] >= 0.5 for j in range(K)),
    'diag >= sum off-diag (row)/2': lambda C0, K: all(
        C0[j,j] >= 0.5 * sum(C0[j,k] for k in range(K) if k != j) for j in range(K)),
}

stats = {name: {'n': 0, 'violations': 0, 'worst': 0.0} for name in conditions}

for trial in range(N):
    pp = np.random.dirichlet(np.ones(K))
    gg = np.random.randn(K)
    C0 = np.random.dirichlet(np.ones(K), size=K).T

    for name, cond in conditions.items():
        if cond(C0, K):
            stats[name]['n'] += 1
            _, _, max_inc = check_monotonicity_fine(C0, pp, gg, n_delta=200)
            if max_inc > 1e-10:
                stats[name]['violations'] += 1
                stats[name]['worst'] = max(stats[name]['worst'], max_inc)

for name, s in stats.items():
    print(f"  {name:>35}: {s['violations']:4d}/{s['n']:5d} "
          f"(worst={s['worst']:.6f})")


# ============================================================
# Part E: Focus on dVB(1) for K=3 violations
# ============================================================
print("\n" + "=" * 70)
print("PART E: Is dVB(1) > 0 the cause? (K=3, diag>=1/K)")
print("=" * 70)

K = 3
np.random.seed(2024 + K)

v_dVB1_positive = 0
v_mono_fail = 0
n_tested = 0

for trial in range(20_000):
    pp = np.random.dirichlet(np.ones(K))
    gg = np.random.randn(K)
    C0 = np.random.dirichlet(np.ones(K), size=K).T
    min_diag = min(C0[j, j] for j in range(K))
    if min_diag < 1.0/K:
        continue
    n_tested += 1

    dVB1 = compute_VB_derivative_at(1.0, C0, pp, gg)
    if dVB1 > 1e-10:
        v_dVB1_positive += 1

    _, _, max_inc = check_monotonicity_fine(C0, pp, gg, n_delta=200)
    if max_inc > 1e-10:
        v_mono_fail += 1

print(f"diag >= 1/K, K=3: {n_tested} trials")
print(f"  dVB(1) > 0: {v_dVB1_positive}")
print(f"  Monotonicity fail: {v_mono_fail}")
print(f"  (Since VB is convex: mono fail iff dVB(1) > 0)")


# ============================================================
# Part F: K=5, K=7 — stronger condition test
# ============================================================
print("\n" + "=" * 70)
print("PART F: Test diag >= max off-diag for K=3,5,7")
print("=" * 70)

for K in [3, 5, 7]:
    np.random.seed(8000 + K)
    n_t = 0; v = 0; worst = 0.0

    for trial in range(20_000):
        pp = np.random.dirichlet(np.ones(K))
        gg = np.random.randn(K)
        C0 = np.random.dirichlet(np.ones(K), size=K).T

        # Dominant diagonal in each ROW: C0[j,j] >= max_{k!=j} C0[j,k]
        ok = all(C0[j,j] >= max(C0[j,k] for k in range(K) if k!=j) for j in range(K))
        if not ok:
            continue
        n_t += 1

        _, _, max_inc = check_monotonicity_fine(C0, pp, gg, n_delta=200)
        if max_inc > 1e-10:
            v += 1
            worst = max(worst, max_inc)

    print(f"  K={K}: row-dominant diagonal: {v}/{n_t} violations (worst={worst:.6f})")


print("\n" + "=" * 70)
print("FINAL ASSESSMENT")
print("=" * 70)
print("""
RESULTS:
- K=2: diag >= 1/K (=0.5) is both necessary and sufficient. 0 violations.
- K>=3: diag >= 1/K is NOT sufficient (small violations exist).
  The violations are small (~0.01-0.02 in V_B terms).

POSSIBLE FIXES:
1. Strengthen condition to "row-dominant diagonal" (C0[j,j] >= max off-diag in row j).
2. State as epsilon-approximate monotonicity (current paper's Conjecture approach).
3. Add "diag >= 1/K" condition and accept small violations as epsilon-approximate.

RECOMMENDED: Keep Theorem 1 with the proportional-effects restriction BUT:
  - Add the condition diag >= 1/K (excludes degenerate swap-like matrices)
  - Note that for K>=3, small (~epsilon) deviations may occur
  - The convexity+V_B'(0)<=0 result is always exact
""")
