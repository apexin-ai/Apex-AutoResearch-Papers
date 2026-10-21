"""Compute annotation-error bias via probability limit calculations.

Uses precomputed sufficient statistics from large-sample DGP simulations
to compute OLS plim as a function of confusion matrix C, avoiding MC.
"""

import warnings
import numpy as np
from .dgp import DEFAULT_PARAMS, HAS_TREATMENT, GEN_FUNCS, TOPOLOGIES
from .confusion import validate_confusion_matrix

_N_PRECOMP = 2_000_000
_precomp_cache = {}


def _params_key(params):
    items = []
    for k, v in sorted(params.items()):
        if isinstance(v, np.ndarray):
            items.append((k, tuple(v.flat)))
        else:
            items.append((k, v))
    return tuple(items)


def _precompute(topology, params, K, seed=999):
    """Precompute sufficient statistics for plim calculation."""
    cache_key = (topology, _params_key(params), K)
    if cache_key in _precomp_cache:
        return _precomp_cache[cache_key]

    rng = np.random.default_rng(seed)
    data = GEN_FUNCS[topology](_N_PRECOMP, params=params, rng=rng)
    Y = data["Y"]
    A = data["A"]

    DA = np.zeros((_N_PRECOMP, K))
    for k in range(K):
        DA[:, k] = (A == k).astype(float)

    stats = {
        "E_Y": Y.mean(),
        "E_DA": DA.mean(0),
        "E_DA_Y": (DA * Y[:, None]).mean(0),
    }

    if topology in HAS_TREATMENT:
        T = data["T"]
        stats.update({
            "E_T": T.mean(),
            "E_T2": (T ** 2).mean(),
            "E_TY": (T * Y).mean(),
            "E_DA_T": (DA * T[:, None]).mean(0),
        })

    if topology == "iv":
        Z = data["Z"]
        Zc = Z - Z.mean()
        var_Z = (Zc ** 2).mean()
        stats["RF"] = (Zc * (Y - Y.mean())).mean() / var_Z
        FS = np.zeros(K)
        for k in range(K):
            FS[k] = (Zc * (DA[:, k] - DA[:, k].mean())).mean() / var_Z
        stats["FS"] = FS

    _precomp_cache[cache_key] = stats
    return stats


def _plim_with_T(C, stats, K):
    """OLS plim for Y ~ 1 + T + D*_1 + ... + D*_{K-1}."""
    ds = C @ stats["E_DA"]
    dst = C @ stats["E_DA_T"]
    dsy = C @ stats["E_DA_Y"]
    ET, ET2 = stats["E_T"], stats["E_T2"]
    EY, ETY = stats["E_Y"], stats["E_TY"]

    dim = 1 + K  # intercept + T + (K-1) dummies
    EZZ = np.zeros((dim, dim))
    EZZ[0, 0] = 1.0
    EZZ[0, 1] = EZZ[1, 0] = ET
    EZZ[1, 1] = ET2
    for j in range(1, K):
        idx = j + 1
        EZZ[0, idx] = EZZ[idx, 0] = ds[j]
        EZZ[1, idx] = EZZ[idx, 1] = dst[j]
        EZZ[idx, idx] = ds[j]

    EZY = np.zeros(dim)
    EZY[0] = EY
    EZY[1] = ETY
    for j in range(1, K):
        EZY[j + 1] = dsy[j]

    cond = np.linalg.cond(EZZ)
    if cond > 1e12:
        warnings.warn(
            f"EZZ condition number {cond:.1e} — plim may be numerically unstable"
        )

    return np.linalg.solve(EZZ, EZY)


def _plim_no_T(C, stats, K):
    """OLS plim for Y ~ 1 + D*_1 + ... + D*_{K-1}."""
    ds = C @ stats["E_DA"]
    dsy = C @ stats["E_DA_Y"]
    EY = stats["E_Y"]

    dim = K  # intercept + (K-1) dummies
    EZZ = np.zeros((dim, dim))
    EZZ[0, 0] = 1.0
    for j in range(1, K):
        EZZ[0, j] = EZZ[j, 0] = ds[j]
        EZZ[j, j] = ds[j]

    EZY = np.zeros(dim)
    EZY[0] = EY
    for j in range(1, K):
        EZY[j] = dsy[j]

    cond = np.linalg.cond(EZZ)
    if cond > 1e12:
        warnings.warn(
            f"EZZ condition number {cond:.1e} — plim may be numerically unstable"
        )

    return np.linalg.solve(EZZ, EZY)


def _plim_iv(C, stats, K):
    """Wald estimator plim: RF / (C @ FS)[1]."""
    FS_star = C @ stats["FS"]
    denom = FS_star[1]
    if abs(denom) < 1e-15:
        return np.nan
    return stats["RF"] / denom


def _get_tau(topology, C, stats, K):
    """Extract target coefficient from plim vector.

    For IV: Wald estimator RF / (C @ FS)[1].
    For topologies with T: OLS coefficient index 1 (treatment effect).
    For topologies without T: OLS coefficient index 1 (first dummy).
    """
    if topology == "iv":
        return _plim_iv(C, stats, K)
    if topology in HAS_TREATMENT:
        coefs = _plim_with_T(C, stats, K)
    else:
        coefs = _plim_no_T(C, stats, K)
    return coefs[1]


def compute_bias(topology, C, params=None):
    """Compute annotation-error bias for a given topology and confusion matrix.

    Args:
        topology: one of "confounding", "mediation", "collider", "exposure",
                  "mbias", "iv", "frontdoor"
        C: (K, K) column-stochastic confusion matrix, C[j,i] = P(A*=j|A=i)
        params: optional DGP parameters dict, None uses defaults

    Returns:
        dict with tau_true, tau_biased, bias, bias_pct, topology
    """
    if topology not in TOPOLOGIES:
        raise ValueError(f"Unknown topology: {topology}. Choose from {TOPOLOGIES}")
    if not validate_confusion_matrix(C):
        raise ValueError("C must be a square, non-negative, column-stochastic matrix")

    K = C.shape[0]
    merged = dict(DEFAULT_PARAMS[topology])
    if params is not None:
        merged.update(params)

    stats = _precompute(topology, merged, K)
    tau_true = _get_tau(topology, np.eye(K), stats, K)
    tau_biased = _get_tau(topology, C, stats, K)
    bias = tau_biased - tau_true
    bias_pct = 100.0 * bias / tau_true if abs(tau_true) > 1e-12 else float("nan")

    return {
        "tau_true": float(tau_true),
        "tau_biased": float(tau_biased),
        "bias": float(bias),
        "bias_pct": float(bias_pct),
        "topology": topology,
    }


def clear_cache():
    """Clear the precomputed statistics cache."""
    _precomp_cache.clear()
