#!/usr/bin/env python3
"""
Numerical verification of the Director's closed-form formula for V_B'(1).

V_B(δ) = Var(E[g(A) | A*_δ])  where C(δ) = (1-δ)I + δC₀

Director's formula:
  V_B'(1) = Σ_j (p_j + q_j) e_j² − Σ_{j≠k} (C₀)_{jk} p_k (g_j − g_k)²

where:
  q_j = Σ_k (C₀)_{jk} p_k
  μ_j = Σ_k g_k (C₀)_{jk} p_k / q_j
  e_j = g_j − μ_j

Three-way cross-check:
  Method A: Numerical differentiation [V_B(1) − V_B(1−h)] / h
  Method B: Original derivative formula (eq:dVB from appendix_proofs.tex)
  Method C: Director's closed-form
"""

import numpy as np
import json
import os

SEED = 42
N_TRIALS = 50_000
K_VALUES = [2, 3, 4, 5, 7, 10]
H = 1e-7


def random_column_stochastic(K, rng, min_diag=0.0):
    C0 = rng.dirichlet(np.ones(K), size=K).T  # columns are Dirichlet
    if min_diag > 0:
        for k in range(K):
            C0[k, k] = max(C0[k, k], min_diag)
            C0[:, k] /= C0[:, k].sum()
    return C0


def random_p(K, rng):
    p = rng.dirichlet(np.ones(K))
    return p


def random_g(K, rng):
    return rng.standard_normal(K)


def compute_VB(C, p, g):
    """V_B = Var(E[g(A) | A*]) = Σ_j N_j²/q_j − ḡ²"""
    q = C @ p
    N = C @ (p * g)
    gbar = p @ g
    return np.sum(N**2 / q) - gbar**2


def method_A_numerical(C0, p, g, h=H):
    """Numerical differentiation at δ=1."""
    I = np.eye(len(p))
    C1 = C0.copy()
    C1h = (1 - (1 - h)) * I + (1 - h) * C0  # = hI + (1-h)C0
    VB1 = compute_VB(C1, p, g)
    VB1h = compute_VB(C1h, p, g)
    return (VB1 - VB1h) / h


def method_B_original(C0, p, g):
    """Original derivative formula: dV_B/dδ = −Σ_{j,k} [(C₀)_{jk} − δ_{jk}] p_k (g_k − μ_j)²"""
    K = len(p)
    I = np.eye(K)
    q = C0 @ p
    N = C0 @ (p * g)
    mu = N / q

    result = 0.0
    for j in range(K):
        for k in range(K):
            coeff = C0[j, k] - I[j, k]
            result -= coeff * p[k] * (g[k] - mu[j])**2
    return result


def method_C_director(C0, p, g):
    """Director's formula: Σ_j (p_j + q_j) e_j² − Σ_{j≠k} (C₀)_{jk} p_k (g_j − g_k)²"""
    K = len(p)
    q = C0 @ p
    N = C0 @ (p * g)
    mu = N / q
    e = g - mu

    term1 = np.sum((p + q) * e**2)

    term2 = 0.0
    for j in range(K):
        for k in range(K):
            if j != k:
                term2 += C0[j, k] * p[k] * (g[j] - g[k])**2

    return term1 - term2


def verify_key_identity(C0, p, g):
    """Verify e_j = (1/q_j) Σ_{k≠j} (C₀)_{jk} p_k (g_j − g_k)"""
    K = len(p)
    q = C0 @ p
    N = C0 @ (p * g)
    mu = N / q
    e = g - mu

    e_identity = np.zeros(K)
    for j in range(K):
        s = 0.0
        for k in range(K):
            if k != j:
                s += C0[j, k] * p[k] * (g[j] - g[k])
        e_identity[j] = s / q[j]

    return np.max(np.abs(e - e_identity))


def method_C_matrix(C0, p, g):
    """Matrix form: V_B'(1) = g^T M g where M = LHS_matrix − RHS_matrix."""
    K = len(p)
    W = C0 * p[np.newaxis, :]  # W_{jk} = (C0)_{jk} p_k
    q = W.sum(axis=1)
    Dq_inv = np.diag(1.0 / q)
    T = Dq_inv @ W  # row-stochastic
    D_pq = np.diag(p + q)

    ImT = np.eye(K) - T
    lhs_matrix = ImT.T @ D_pq @ ImT
    rhs_matrix = D_pq - 2 * W

    M = lhs_matrix - rhs_matrix
    return g @ M @ g, M


def run_verification():
    rng = np.random.default_rng(SEED)

    results = {
        'description': 'Three-way verification of V_B\'(1) formula',
        'n_trials': N_TRIALS,
        'K_values': K_VALUES,
        'h_numerical': H,
        'per_K': {},
        'overall': {},
    }

    all_errors_AB = []
    all_errors_AC = []
    all_errors_BC = []
    all_errors_identity = []
    all_errors_matrix = []
    n_VBp1_positive = 0
    n_total = 0
    worst_violation = {'eps': 0.0}

    for K in K_VALUES:
        errors_AB = []
        errors_AC = []
        errors_BC = []
        errors_id = []
        errors_mat = []
        n_pos = 0
        n_K = N_TRIALS // len(K_VALUES)

        for _ in range(n_K):
            C0 = random_column_stochastic(K, rng)
            p = random_p(K, rng)
            g = random_g(K, rng)

            vA = method_A_numerical(C0, p, g)
            vB = method_B_original(C0, p, g)
            vC = method_C_director(C0, p, g)
            vM, M = method_C_matrix(C0, p, g)
            id_err = verify_key_identity(C0, p, g)

            scale = max(abs(vB), abs(vC), 1e-15)

            errors_AB.append(abs(vA - vB) / scale)
            errors_AC.append(abs(vA - vC) / scale)
            errors_BC.append(abs(vB - vC) / scale)
            errors_id.append(id_err)
            errors_mat.append(abs(vC - vM) / max(abs(vC), 1e-15))

            if vC > 1e-10:
                n_pos += 1
                if vC > worst_violation['eps']:
                    worst_violation = {
                        'eps': float(vC),
                        'K': K,
                        'VBp1': float(vC),
                        'C0_diag': [float(C0[j, j]) for j in range(K)],
                        'C0_diag_min': float(min(C0[j, j] for j in range(K))),
                        'p': p.tolist(),
                        'g': g.tolist(),
                    }

            n_total += 1

        errors_AB = np.array(errors_AB)
        errors_AC = np.array(errors_AC)
        errors_BC = np.array(errors_BC)
        errors_id = np.array(errors_id)
        errors_mat = np.array(errors_mat)

        n_VBp1_positive += n_pos

        all_errors_AB.extend(errors_AB)
        all_errors_AC.extend(errors_AC)
        all_errors_BC.extend(errors_BC)
        all_errors_identity.extend(errors_id)
        all_errors_matrix.extend(errors_mat)

        results['per_K'][str(K)] = {
            'n_trials': n_K,
            'AB_max_rel_error': float(errors_AB.max()),
            'AB_mean_rel_error': float(errors_AB.mean()),
            'AC_max_rel_error': float(errors_AC.max()),
            'AC_mean_rel_error': float(errors_AC.mean()),
            'BC_max_rel_error': float(errors_BC.max()),
            'BC_mean_rel_error': float(errors_BC.mean()),
            'identity_max_error': float(errors_id.max()),
            'matrix_max_rel_error': float(errors_mat.max()),
            'n_VBp1_positive': n_pos,
            'frac_VBp1_positive': n_pos / n_K,
        }

        print(f"K={K:>2}: AB_max={errors_AB.max():.2e}  "
              f"BC_max={errors_BC.max():.2e}  "
              f"id_max={errors_id.max():.2e}  "
              f"mat_max={errors_mat.max():.2e}  "
              f"V'>0: {n_pos}/{n_K} ({100*n_pos/n_K:.1f}%)")

    all_AB = np.array(all_errors_AB)
    all_AC = np.array(all_errors_AC)
    all_BC = np.array(all_errors_BC)
    all_id = np.array(all_errors_identity)
    all_mat = np.array(all_errors_matrix)

    results['overall'] = {
        'n_total': n_total,
        'AB_max_rel_error': float(all_AB.max()),
        'AC_max_rel_error': float(all_AC.max()),
        'BC_max_rel_error': float(all_BC.max()),
        'identity_max_error': float(all_id.max()),
        'matrix_max_rel_error': float(all_mat.max()),
        'n_VBp1_positive': n_VBp1_positive,
        'frac_VBp1_positive': n_VBp1_positive / n_total,
        'analytic_methods_consistent': bool(all_BC.max() < 1e-6),
        'formula_verified': bool(all_BC.max() < 1e-6),
    }
    results['worst_VBp1_positive'] = worst_violation

    # Additional test: diagonal dominance condition
    print("\n--- Diagonal dominance condition test ---")
    n_dd_test = 20_000
    n_dd_satisfied = 0
    n_dd_implies_neg = 0
    n_dd_violated_but_neg = 0

    for _ in range(n_dd_test):
        K = rng.choice([3, 5, 7])
        C0 = random_column_stochastic(K, rng, min_diag=0.3)
        p = random_p(K, rng)
        g = random_g(K, rng)

        q = C0 @ p
        alpha = np.diag(C0)

        dd_ok = all(alpha[j] >= q[j] / (p[j] + q[j]) for j in range(K))

        vC = method_C_director(C0, p, g)

        if dd_ok:
            n_dd_satisfied += 1
            if vC <= 1e-10:
                n_dd_implies_neg += 1
        else:
            if vC <= 1e-10:
                n_dd_violated_but_neg += 1

    results['diagonal_dominance_test'] = {
        'n_tests': n_dd_test,
        'n_condition_satisfied': n_dd_satisfied,
        'n_condition_implies_negative': n_dd_implies_neg,
        'condition_is_sufficient': n_dd_satisfied == n_dd_implies_neg,
        'n_violated_but_still_negative': n_dd_violated_but_neg,
    }

    print(f"DD condition satisfied: {n_dd_satisfied}/{n_dd_test}")
    print(f"DD → V'(1)≤0: {n_dd_implies_neg}/{n_dd_satisfied} "
          f"({'SUFFICIENT' if n_dd_satisfied == n_dd_implies_neg else 'NOT sufficient'})")

    # Eigenvalue test for doubly stochastic symmetric case
    print("\n--- Doubly stochastic symmetric eigenvalue test ---")
    n_ds_test = 10_000
    n_ds_neg = 0

    for _ in range(n_ds_test):
        K = rng.choice([3, 5, 7, 10])
        alpha_min = rng.uniform(0.5, 0.95)
        c = (1 - alpha_min) / (K - 1)
        C0 = np.full((K, K), c)
        np.fill_diagonal(C0, alpha_min)

        p = np.ones(K) / K  # uniform
        g = random_g(K, rng)

        vC = method_C_director(C0, p, g)
        if vC <= 1e-10:
            n_ds_neg += 1

    results['doubly_stochastic_symmetric_test'] = {
        'n_tests': n_ds_test,
        'n_VBp1_negative': n_ds_neg,
        'all_negative': n_ds_neg == n_ds_test,
    }
    print(f"DS symmetric + uniform p: V'(1)≤0 in {n_ds_neg}/{n_ds_test} "
          f"({'ALL' if n_ds_neg == n_ds_test else 'NOT all'})")

    # Eigenvalue analysis
    print("\n--- M matrix eigenvalue analysis ---")
    n_eig = 5000
    max_pos_eig = 0.0
    max_pos_eig_info = {}

    for _ in range(n_eig):
        K = rng.choice([3, 5, 7])
        C0 = random_column_stochastic(K, rng)
        p = random_p(K, rng)

        W = C0 * p[np.newaxis, :]
        q = W.sum(axis=1)
        T = np.diag(1.0 / q) @ W
        D_pq = np.diag(p + q)
        ImT = np.eye(K) - T
        M = ImT.T @ D_pq @ ImT - (D_pq - 2 * W)
        Ms = (M + M.T) / 2
        eigs = np.linalg.eigvalsh(Ms)
        max_eig = eigs.max()

        if max_eig > max_pos_eig:
            max_pos_eig = max_eig
            max_pos_eig_info = {
                'max_eigenvalue': float(max_eig),
                'all_eigenvalues': eigs.tolist(),
                'K': K,
                'C0_diag': np.diag(C0).tolist(),
                'C0_diag_min': float(np.diag(C0).min()),
            }

    results['eigenvalue_analysis'] = {
        'n_tests': n_eig,
        'max_positive_eigenvalue': float(max_pos_eig),
        'worst_case': max_pos_eig_info,
    }
    print(f"Max positive eigenvalue of M_sym: {max_pos_eig:.6f}")

    def jsonify(obj):
        if isinstance(obj, (np.integer,)):
            return int(obj)
        if isinstance(obj, (np.floating,)):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        raise TypeError(f'{type(obj)} not serializable')

    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            'conjecture1_formula_verify_results.json')
    with open(out_path, 'w') as f:
        json.dump(results, f, indent=2, default=jsonify)

    print(f"\n{'='*60}")
    print(f"VERIFICATION {'PASSED' if results['overall']['formula_verified'] else 'FAILED'}")
    print(f"  B↔C max relative error: {all_BC.max():.2e}")
    print(f"  A↔B max relative error: {all_AB.max():.2e}")
    print(f"  Key identity max error:  {all_id.max():.2e}")
    print(f"  V_B'(1) > 0 fraction:   {n_VBp1_positive}/{n_total} ({100*n_VBp1_positive/n_total:.1f}%)")
    print(f"  Results → {out_path}")
    print(f"{'='*60}")


if __name__ == '__main__':
    run_verification()
