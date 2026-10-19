"""
Numerical verification: K=3 symmetric confusion matrix monotonicity.

For C₀[i,i] = 1-2c, C₀[i,j] = c (i≠j), c ∈ (0,1/3),
along C(δ) = (1-δ)I + δC₀ = (1-3cδ)I + cδ𝟏𝟏ᵀ:

1. Confounding (proportional): |B(δ)| non-decreasing ✓ (proven)
2. Confounding (general): |B(δ)| non-decreasing (check)
3. Mediation (proportional): |B(δ)| non-decreasing ✓ (same structure)
4. Collider (proportional): |B(δ)| non-increasing ✓ (reverse direction)
"""

import numpy as np
from scipy.special import softmax
import json

np.random.seed(42)

def make_symmetric_C(c, delta):
    s = c * delta
    C = np.full((3, 3), s)
    np.fill_diagonal(C, 1 - 2*s)
    return C

def compute_VB(s, p, h):
    """V_B(s) = (1-3s)^2 Σ_j p_j^2 h_j^2 / q_j"""
    q = (1 - 3*s) * p + s
    return (1 - 3*s)**2 * np.sum(p**2 * h**2 / q)

def compute_dVB_ds(s, p, h):
    """dV_B/ds = (1-3s) Σ_j p_j^2 h_j^2 [-3(1-3s)p_j - 1 - 3s] / q_j^2"""
    q = (1 - 3*s) * p + s
    bracket = -3*(1-3*s)*p - 1 - 3*s
    return (1-3*s) * np.sum(p**2 * h**2 * bracket / q**2)


# ====== Test 1: Verify dV_B/ds < 0 analytically ======
print("=" * 60)
print("Test 1: Verify dV_B/ds < 0 for random (p, g, c, s)")
print("=" * 60)

n_tests = 100000
violations = 0
for _ in range(n_tests):
    p = np.random.dirichlet([1, 1, 1])
    g = np.random.randn(3)
    g_bar = p @ g
    h = g - g_bar
    c = np.random.uniform(0.01, 0.33)
    s = np.random.uniform(0, c)

    deriv = compute_dVB_ds(s, p, h)
    if deriv > 1e-12:
        violations += 1

print(f"Violations: {violations}/{n_tests}")
assert violations == 0, "dV_B/ds > 0 found!"
print("PASS: dV_B/ds ≤ 0 everywhere\n")


# ====== Test 2: Confounding bias monotonicity (proportional) ======
print("=" * 60)
print("Test 2: Confounding |B(δ)| non-decreasing (proportional f=λg)")
print("=" * 60)

n_configs = 10000
n_delta = 200
deltas = np.linspace(0, 1, n_delta)
max_violation = 0
violation_count = 0

for _ in range(n_configs):
    p = np.random.dirichlet([1, 1, 1])
    g = np.random.randn(3)
    g_bar = p @ g
    h = g - g_bar
    V = p @ h**2
    if V < 1e-8:
        continue
    sigma_T2 = np.random.uniform(0.1, 3.0)
    lam = np.random.randn()
    c = np.random.uniform(0.01, 0.33)

    abs_B = np.zeros(n_delta)
    for i, d in enumerate(deltas):
        s = c * d
        VB = compute_VB(s, p, h)
        VW = V - VB
        B = lam * VW / (VW + sigma_T2)
        abs_B[i] = abs(B)

    diffs = np.diff(abs_B)
    min_diff = diffs.min()
    if min_diff < -1e-10:
        violation_count += 1
        max_violation = min(max_violation, min_diff)

print(f"Violations: {violation_count}/{n_configs}")
print(f"Max violation magnitude: {abs(max_violation):.2e}")
assert violation_count == 0
print("PASS\n")


# ====== Test 3: Confounding bias monotonicity (general f) ======
print("=" * 60)
print("Test 3: Confounding |B(δ)| non-decreasing (general f)")
print("=" * 60)

n_configs = 50000
violation_count = 0
max_violation = 0
worst_config = None

for _ in range(n_configs):
    p = np.random.dirichlet([1, 1, 1])
    g = np.random.randn(3)
    f = np.random.randn(3)
    g_bar = p @ g
    f_bar = p @ f
    hg = g - g_bar
    hf = f - f_bar
    Vg = p @ hg**2
    if Vg < 1e-8:
        continue
    sigma_T2 = np.random.uniform(0.1, 3.0)
    c = np.random.uniform(0.01, 0.33)
    cov_gf = p @ (hg * hf)

    abs_B = np.zeros(n_delta)
    for i, d in enumerate(deltas):
        s = c * d
        q = (1-3*s)*p + s
        Phi_gf = (1-3*s)**2 * np.sum(p**2 * hg * hf / q)
        Phi_gg = (1-3*s)**2 * np.sum(p**2 * hg**2 / q)
        R = cov_gf - Phi_gf
        D = sigma_T2 + Vg - Phi_gg
        B = R / D
        abs_B[i] = abs(B)

    diffs = np.diff(abs_B)
    min_diff = diffs.min()
    if min_diff < -1e-8:
        violation_count += 1
        if min_diff < max_violation:
            max_violation = min_diff
            worst_config = (p.copy(), g.copy(), f.copy(), sigma_T2, c)

test3_violations = violation_count
test3_max_violation = max_violation

print(f"Violations: {test3_violations}/{n_configs}")
print(f"Max violation magnitude: {abs(test3_max_violation):.2e}")
if test3_violations > 0:
    print(f"Violation rate: {test3_violations/n_configs*100:.2f}%")
    p_, g_, f_, st2, c_ = worst_config
    print(f"Worst config: p={p_}, g={g_}, f={f_}, σ_T²={st2:.3f}, c={c_:.3f}")
print()


# ====== Test 4: Collider bias monotonicity (proportional) ======
print("=" * 60)
print("Test 4: Collider |B(δ)| non-increasing (proportional h=λg)")
print("=" * 60)

n_configs = 10000
violation_count = 0

for _ in range(n_configs):
    p = np.random.dirichlet([1, 1, 1])
    g = np.random.randn(3)
    g_bar = p @ g
    h = g - g_bar
    V = p @ h**2
    if V < 1e-8:
        continue
    var_T = np.random.uniform(V + 0.1, V + 5.0)  # Var(T) > Var(g(A))
    lam = np.random.randn()
    c = np.random.uniform(0.01, 0.33)

    abs_B = np.zeros(n_delta)
    for i, d in enumerate(deltas):
        s = c * d
        VB = compute_VB(s, p, h)
        B_col = -lam * VB / (var_T - VB)
        abs_B[i] = abs(B_col)

    diffs = np.diff(abs_B)
    max_diff = diffs.max()
    if max_diff > 1e-10:
        violation_count += 1

print(f"Violations: {violation_count}/{n_configs}")
assert violation_count == 0
print("PASS\n")


# ====== Test 5: Mediation bias monotonicity (proportional) ======
print("=" * 60)
print("Test 5: Mediation |B(δ)| non-decreasing (proportional f=λg)")
print("=" * 60)

n_configs = 10000
violation_count = 0

for _ in range(n_configs):
    p = np.random.dirichlet([1, 1, 1])
    g = np.random.randn(3)
    g_bar = p @ g
    h = g - g_bar
    V = p @ h**2
    if V < 1e-8:
        continue
    sigma_eps2 = np.random.uniform(0.1, 3.0)  # E[Var(T|A)]
    lam = np.random.randn()
    c = np.random.uniform(0.01, 0.33)

    abs_B = np.zeros(n_delta)
    for i, d in enumerate(deltas):
        s = c * d
        VB = compute_VB(s, p, h)
        VW = V - VB
        B = lam * VW / (VW + sigma_eps2)
        abs_B[i] = abs(B)

    diffs = np.diff(abs_B)
    min_diff = diffs.min()
    if min_diff < -1e-10:
        violation_count += 1

print(f"Violations: {violation_count}/{n_configs}")
assert violation_count == 0
print("PASS\n")


# ====== Test 6: Derivative formula vs finite differences ======
print("=" * 60)
print("Test 6: Derivative formula accuracy (vs finite differences)")
print("=" * 60)

n_checks = 10000
max_rel_err = 0
eps_fd = 1e-7
for _ in range(n_checks):
    p = np.random.dirichlet([1, 1, 1])
    g = np.random.randn(3)
    g_bar = p @ g
    h = g - g_bar
    s = np.random.uniform(0.01, 0.32)

    analytic = compute_dVB_ds(s, p, h)
    fd = (compute_VB(s + eps_fd, p, h) - compute_VB(s - eps_fd, p, h)) / (2 * eps_fd)
    if abs(analytic) > 1e-10:
        rel_err = abs(analytic - fd) / abs(analytic)
        max_rel_err = max(max_rel_err, rel_err)

print(f"Max relative error: {max_rel_err:.2e}")
assert max_rel_err < 1e-4
print("PASS\n")


# ====== Summary ======
results = {
    "test1_dVB_sign": {"n": n_tests, "violations": 0, "status": "PASS"},
    "test2_confounding_proportional": {"n": 10000, "violations": 0, "status": "PASS"},
    "test3_confounding_general": {"n": 50000, "violations": test3_violations,
                                   "max_violation": float(abs(test3_max_violation)),
                                   "violation_rate_pct": round(test3_violations/50000*100, 2),
                                   "status": "APPROXIMATE"},
    "test4_collider_proportional": {"n": 10000, "violations": 0, "status": "PASS"},
    "test5_mediation_proportional": {"n": 10000, "violations": 0, "status": "PASS"},
    "test6_derivative_accuracy": {"max_rel_error": float(max_rel_err), "status": "PASS"},
}

print("=" * 60)
print("Summary")
print("=" * 60)
for name, r in results.items():
    if 'violations' in r:
        print(f"  {name}: {r['status']} ({r['violations']}/{r['n']})")
    else:
        print(f"  {name}: {r['status']}")

with open("artifacts/k3_symmetric_verify_results.json", "w") as f:
    json.dump(results, f, indent=2)

print("\nResults saved to artifacts/k3_symmetric_verify_results.json")
