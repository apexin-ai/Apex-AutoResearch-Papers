"""Correction methods and recommendation engine for annotation-error bias.

Five correction methods:
  - naive_plugin: C^{-1} correction of dummy indicators
  - dsl: EM-based joint estimation of regression params and C
  - ppi: PPI++ combining gold-standard and full-sample estimates
  - mcsimex: MC-SIMEX extrapolation to lambda=-1
  - mla: Matrix-based label adjustment via D*_full @ C^{-1}

Key finding (FWL theorem): naive_plugin and mla correct dummy coefficients
but NOT the treatment coefficient in regressions with a separate treatment T.
"""

import numpy as np
from .utils import ols, ols_with_se, make_dummies, make_full_dummies, misclassify

METHODS = ["naive_plugin", "dsl", "ppi", "mcsimex", "mla"]

_EM_MAX_ITER = 100
_EM_TOL = 1e-6
_SIMEX_LAMBDAS = [0.5, 1.0, 1.5, 2.0]
_SIMEX_B = 50


def correct_naive_plugin(X_other, Y, Astar, C, tau_idx=1):
    """Correct using C^{-1} applied per-observation to dummy indicators.

    Args:
        X_other: (N, p) non-A regressors (includes intercept)
        Y: (N,) outcome
        Astar: (N,) misclassified labels
        C: (K, K) confusion matrix
        tau_idx: index of target coefficient in full design

    Returns:
        (tau_hat, se, success) tuple
    """
    cond = np.linalg.cond(C)
    if cond > 1e12:
        return np.nan, np.nan, False
    try:
        C_inv = np.linalg.inv(C)
    except np.linalg.LinAlgError:
        return np.nan, np.nan, False
    D_corrected = C_inv[:, Astar].T[:, 1:]
    X = np.column_stack([X_other, D_corrected])
    try:
        beta, se = ols_with_se(X, Y)
        return float(beta[tau_idx]), float(se[tau_idx]), True
    except Exception:
        return np.nan, np.nan, False


def correct_dsl(X_other, Y, Astar, A_gold, gold_mask, tau_idx=1):
    """EM-based joint estimation of regression params and C.

    Args:
        X_other: (N, p) non-A regressors (includes intercept)
        Y: (N,) outcome
        Astar: (N,) misclassified labels
        A_gold: (N,) gold-standard labels (only gold_mask positions used)
        gold_mask: (N,) boolean mask for gold-standard observations
        tau_idx: index of target coefficient

    Returns:
        (tau_hat, se, success) tuple
    """
    N = len(Y)
    K = int(max(Astar.max(), A_gold[gold_mask].max())) + 1
    n_other = X_other.shape[1]

    C_est = np.zeros((K, K))
    for j in range(K):
        for k in range(K):
            C_est[k, j] = (
                (A_gold[gold_mask] == j) & (Astar[gold_mask] == k)
            ).sum()
    col_sums = C_est.sum(axis=0)
    col_sums[col_sums == 0] = 1.0
    C_est /= col_sums
    C_est = 0.9 * C_est + 0.1 / K * np.ones((K, K))

    D_star = make_dummies(Astar, K)
    X_init = np.column_stack([X_other, D_star])
    try:
        beta = ols(X_init, Y)
    except Exception:
        return np.nan, np.nan, False
    sigma2 = 1.0

    for _ in range(_EM_MAX_ITER):
        base = X_other @ beta[:n_other]
        resp = np.zeros((N, K))
        for j in range(K):
            mu_j = base + (beta[n_other + j - 1] if j > 0 else 0.0)
            resp[:, j] = (
                -0.5 * (Y - mu_j) ** 2 / sigma2
                + np.log(np.clip(C_est[Astar, j], 1e-15, None))
            )
        resp -= resp.max(axis=1, keepdims=True)
        resp = np.exp(resp)
        resp /= resp.sum(axis=1, keepdims=True)
        resp[gold_mask] = 0.0
        resp[gold_mask, A_gold[gold_mask]] = 1.0

        D_exp = resp[:, 1:]
        X_new = np.column_stack([X_other, D_exp])
        try:
            beta_new = ols(X_new, Y)
        except Exception:
            return np.nan, np.nan, False
        sigma2_new = max(np.mean((Y - X_new @ beta_new) ** 2), 1e-6)

        C_new = np.zeros((K, K))
        for j in range(K):
            for k in range(K):
                C_new[k, j] = resp[Astar == k, j].sum()
        cs = C_new.sum(axis=0)
        cs[cs == 0] = 1.0
        C_new /= cs

        converged = (
            np.max(np.abs(beta_new - beta)) < _EM_TOL
            and np.max(np.abs(C_new - C_est)) < _EM_TOL
        )
        beta, C_est, sigma2 = beta_new, C_new, sigma2_new
        if converged:
            break

    X_final = np.column_stack([X_other, resp[:, 1:]])
    try:
        beta_f, se_f = ols_with_se(X_final, Y)
        return float(beta_f[tau_idx]), float(se_f[tau_idx]), True
    except Exception:
        return np.nan, np.nan, False


def correct_ppi(X_other, Y, Astar, A_gold, gold_mask, tau_idx=1, rng=None):
    """PPI++ with bootstrap lambda tuning.

    Args:
        X_other: (N, p) non-A regressors (includes intercept)
        Y: (N,) outcome
        Astar: (N,) misclassified labels
        A_gold: (N,) gold-standard labels
        gold_mask: (N,) boolean mask for gold-standard observations
        tau_idx: index of target coefficient
        rng: numpy random Generator

    Returns:
        (tau_hat, se, success) tuple
    """
    if rng is None:
        rng = np.random.default_rng()
    K = int(max(Astar.max(), A_gold[gold_mask].max())) + 1
    gold_idx = np.where(gold_mask)[0]
    n_gold = len(gold_idx)

    D_g_true = make_dummies(A_gold[gold_mask], K)
    X_g_true = np.column_stack([X_other[gold_mask], D_g_true])
    D_g_star = make_dummies(Astar[gold_mask], K)
    X_g_star = np.column_stack([X_other[gold_mask], D_g_star])
    D_all_star = make_dummies(Astar, K)
    X_all_star = np.column_stack([X_other, D_all_star])

    try:
        b_g_true = ols(X_g_true, Y[gold_mask])
        b_g_star = ols(X_g_star, Y[gold_mask])
        b_all_star = ols(X_all_star, Y)
    except Exception:
        return np.nan, np.nan, False

    n_boot = 50
    tau_true_boot = np.zeros(n_boot)
    tau_rect_boot = np.zeros(n_boot)
    for b in range(n_boot):
        idx = rng.choice(gold_idx, size=n_gold, replace=True)
        try:
            bt = ols(
                np.column_stack([X_other[idx], make_dummies(A_gold[idx], K)]),
                Y[idx],
            )
            bs = ols(
                np.column_stack([X_other[idx], make_dummies(Astar[idx], K)]),
                Y[idx],
            )
            tau_true_boot[b] = bt[tau_idx]
            tau_rect_boot[b] = bs[tau_idx] - bt[tau_idx]
        except Exception:
            tau_true_boot[b] = tau_rect_boot[b] = np.nan

    valid = np.isfinite(tau_true_boot) & np.isfinite(tau_rect_boot)
    if valid.sum() > 5:
        var_r = np.var(tau_rect_boot[valid])
        cov_tr = np.cov(tau_true_boot[valid], tau_rect_boot[valid])[0, 1]
        lam = np.clip(-cov_tr / var_r, 0, 1) if var_r > 1e-12 else 1.0
    else:
        lam = 1.0

    tau_ppi = b_g_true[tau_idx] + lam * (b_all_star[tau_idx] - b_g_star[tau_idx])
    se_est = float(np.std(tau_true_boot[valid])) if valid.sum() > 1 else np.nan
    return float(tau_ppi), se_est, True


def correct_mcsimex(X_other, Y, Astar, C, tau_idx=1, rng=None):
    """MC-SIMEX: add extra misclassification at levels lambda, extrapolate to -1.

    Args:
        X_other: (N, p) non-A regressors (includes intercept)
        Y: (N,) outcome
        Astar: (N,) misclassified labels
        C: (K, K) confusion matrix
        tau_idx: index of target coefficient
        rng: numpy random Generator

    Returns:
        (tau_hat, se, success) tuple
    """
    if rng is None:
        rng = np.random.default_rng()
    K = C.shape[0]
    try:
        eigvals, eigvecs = np.linalg.eig(C)
        eigvecs_inv = np.linalg.inv(eigvecs)
    except np.linalg.LinAlgError:
        return np.nan, np.nan, False

    lambdas = np.array([0.0] + _SIMEX_LAMBDAS)
    tau_lam = np.zeros(len(lambdas))

    for li, lam_val in enumerate(lambdas):
        if lam_val == 0.0:
            D_star = make_dummies(Astar, K)
            X = np.column_stack([X_other, D_star])
            try:
                tau_lam[li] = ols(X, Y)[tau_idx]
            except Exception:
                return np.nan, np.nan, False
        else:
            C_lam_raw = np.real((eigvecs * (eigvals ** lam_val)) @ eigvecs_inv)
            C_lam = np.clip(C_lam_raw, 0, None)
            cs = C_lam.sum(axis=0)
            cs[cs == 0] = 1.0
            C_lam /= cs

            tau_b = np.zeros(_SIMEX_B)
            for b in range(_SIMEX_B):
                rng_b = np.random.default_rng(
                    rng.integers(0, 2 ** 31) + b * 1000 + li * 100000
                )
                A_extra = misclassify(Astar, C_lam, rng_b)
                D_extra = make_dummies(A_extra, K)
                X_extra = np.column_stack([X_other, D_extra])
                try:
                    tau_b[b] = ols(X_extra, Y)[tau_idx]
                except Exception:
                    tau_b[b] = np.nan
            ok = np.isfinite(tau_b)
            if ok.sum() < _SIMEX_B // 2:
                return np.nan, np.nan, False
            tau_lam[li] = tau_b[ok].mean()

    try:
        coeffs = np.polyfit(lambdas, tau_lam, 2)
        tau_simex = float(np.polyval(coeffs, -1.0))
    except Exception:
        return np.nan, np.nan, False

    D_star = make_dummies(Astar, K)
    X = np.column_stack([X_other, D_star])
    try:
        _, se = ols_with_se(X, Y)
        return tau_simex, float(se[tau_idx]), True
    except Exception:
        return tau_simex, np.nan, True


def correct_mla(X_other, Y, Astar, C, tau_idx=1):
    """MLA: D_corrected = D*_full @ C^{-1}, drop reference category.

    Args:
        X_other: (N, p) non-A regressors (includes intercept)
        Y: (N,) outcome
        Astar: (N,) misclassified labels
        C: (K, K) confusion matrix
        tau_idx: index of target coefficient

    Returns:
        (tau_hat, se, success) tuple
    """
    cond = np.linalg.cond(C)
    if cond > 1e12:
        return np.nan, np.nan, False
    try:
        C_inv = np.linalg.inv(C)
    except np.linalg.LinAlgError:
        return np.nan, np.nan, False
    K = C.shape[0]
    D_full = make_full_dummies(Astar, K)
    D_corrected = (D_full @ C_inv)[:, 1:]
    X = np.column_stack([X_other, D_corrected])
    try:
        beta, se = ols_with_se(X, Y)
        return float(beta[tau_idx]), float(se[tau_idx]), True
    except Exception:
        return np.nan, np.nan, False


def recommend_correction(topology, C, has_gold=False, gold_fraction=0.1):
    """Recommend the best correction method based on topology and data availability.

    Rules (from plan_007 conclusions):
      - has_gold=True  -> PPI++ (93.8% bias reduction, 96.8% coverage)
      - has_gold=False + confounding/mediation -> DSL
      - has_gold=False + other topologies -> MC-SIMEX
      - naive_plugin/MLA: only correct dummy coefficients (FWL theorem)

    Args:
        topology: one of 7 DAG types
        C: (K, K) confusion matrix (used for diagnostics)
        has_gold: whether gold-standard labels are available
        gold_fraction: fraction of data with gold labels

    Returns:
        dict with recommended, ranking, notes
    """
    dsl_safe = topology in ("confounding", "mediation")

    if has_gold:
        recommended = "ppi"
    elif dsl_safe:
        recommended = "dsl"
    else:
        recommended = "mcsimex"

    ranking = []

    # PPI++
    if has_gold:
        ranking.append({
            "method": "ppi",
            "applicable": True,
            "expected_bias_reduction": 0.938,
            "notes": "Best with gold labels (93.8% bias reduction, 96.8% coverage)",
        })
    else:
        ranking.append({
            "method": "ppi",
            "applicable": False,
            "expected_bias_reduction": 0.0,
            "notes": "Requires gold-standard labels",
        })

    # DSL
    if dsl_safe:
        ranking.append({
            "method": "dsl",
            "applicable": True,
            "expected_bias_reduction": 0.75,
            "notes": "Good for confounding/mediation"
                     + (" (best with gold for initialization)" if not has_gold else ""),
        })
    else:
        ranking.append({
            "method": "dsl",
            "applicable": False,
            "expected_bias_reduction": -5.0,
            "notes": f"Catastrophic for {topology} (e.g., mbias yields -768%)",
        })

    # MC-SIMEX
    ranking.append({
        "method": "mcsimex",
        "applicable": True,
        "expected_bias_reduction": 0.209,
        "notes": "Moderate (20.9%) but broadly applicable; requires known C",
    })

    # Naive Plugin
    ranking.append({
        "method": "naive_plugin",
        "applicable": True,
        "expected_bias_reduction": 0.0,
        "notes": "Only corrects dummy coefficients, NOT treatment coefficient (FWL theorem)",
    })

    # MLA
    ranking.append({
        "method": "mla",
        "applicable": True,
        "expected_bias_reduction": 0.0,
        "notes": "Only corrects dummy coefficients, NOT treatment coefficient (FWL theorem)",
    })

    ranking.sort(key=lambda m: -m["expected_bias_reduction"])

    notes = []
    if has_gold:
        notes.append(f"Gold labels available ({gold_fraction:.0%} of data)")
        notes.append("PPI++ recommended: highest bias reduction with valid coverage")
    else:
        notes.append("No gold labels available")
        if dsl_safe:
            notes.append(f"DSL recommended for {topology} (EM-based, works with known C)")
        else:
            notes.append(
                f"MC-SIMEX recommended; DSL is catastrophic for {topology}"
            )

    cond = np.linalg.cond(C)
    if cond > 100:
        notes.append(
            f"WARNING: C condition number = {cond:.0f}, "
            f"inverse-based methods may be unstable"
        )

    return {
        "recommended": recommended,
        "ranking": ranking,
        "notes": notes,
    }
