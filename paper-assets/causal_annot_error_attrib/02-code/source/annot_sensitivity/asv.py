"""Annotation Sensitivity Value (ASV) computation.

ASV measures how much misclassification is needed to cross a bias threshold,
using the C(delta) = (1-delta)*I + delta*C0 interpolation path.
"""

import numpy as np
from .bias import _precompute, _get_tau
from .confusion import validate_confusion_matrix, interpolate_confusion, delta_range
from .dgp import DEFAULT_PARAMS, TOPOLOGIES


def _compute_bias_curve(topology, C0, stats, K, tau_true, n_grid=1500):
    dmin, dmax = delta_range(C0)
    deltas = np.linspace(dmin, dmax, n_grid)
    tau_curve = np.zeros(n_grid)
    for i, d in enumerate(deltas):
        C_d = interpolate_confusion(C0, d)
        tau_curve[i] = _get_tau(topology, C_d, stats, K)
    bias_abs = np.abs(tau_curve - tau_true)
    return deltas, bias_abs, tau_curve


def _compute_envelope(bias_abs):
    env = np.zeros_like(bias_abs)
    running_max = 0.0
    for i in range(len(bias_abs)):
        v = bias_abs[i]
        if not np.isnan(v):
            running_max = max(running_max, v)
        env[i] = running_max
    return env


def _find_threshold_crossing(envelope, deltas, tau_curve, tau_true,
                             threshold_type, threshold_value):
    if threshold_type == "magnitude":
        if abs(tau_true) < 1e-12:
            return None
        thresh = threshold_value * abs(tau_true)
        for i in range(len(deltas)):
            if envelope[i] > thresh:
                return float(deltas[i])
        return None
    elif threshold_type == "sign_flip":
        if abs(tau_true) < 1e-12:
            return None
        baseline_sign = np.sign(tau_true)
        for i in range(len(deltas)):
            if np.isnan(tau_curve[i]):
                continue
            if np.sign(tau_curve[i]) != baseline_sign:
                return float(deltas[i])
        return None
    elif threshold_type == "significance":
        z_crit = 1.96
        for i in range(len(deltas)):
            if np.isnan(tau_curve[i]):
                continue
            if abs(tau_curve[i]) < z_crit * threshold_value:
                return float(deltas[i])
        return None
    else:
        raise ValueError(
            f"Unknown threshold_type: {threshold_type}. "
            f"Choose from 'magnitude', 'significance', 'sign_flip'"
        )


def compute_asv(topology, C0, params=None, threshold_type="magnitude",
                threshold_value=0.1, n_grid=1500):
    """Compute Annotation Sensitivity Value for a topology and base confusion matrix.

    ASV is the minimum interpolation delta at which a bias threshold is crossed
    along the path C(delta) = (1-delta)*I + delta*C0.

    Args:
        topology: one of 7 DAG types
        C0: (K, K) base confusion matrix
        params: optional DGP parameters dict
        threshold_type: "magnitude" (relative to tau_true),
                        "significance" (threshold_value = SE),
                        "sign_flip" (sign of tau changes)
        threshold_value: threshold parameter (meaning depends on threshold_type)
        n_grid: number of delta grid points

    Returns:
        dict with asv, bias_curve, envelope, deltas, tau_true
    """
    if topology not in TOPOLOGIES:
        raise ValueError(f"Unknown topology: {topology}. Choose from {TOPOLOGIES}")
    if not validate_confusion_matrix(C0):
        raise ValueError("C0 must be a valid column-stochastic matrix")

    K = C0.shape[0]
    merged = dict(DEFAULT_PARAMS[topology])
    if params is not None:
        merged.update(params)

    stats = _precompute(topology, merged, K)
    tau_true = _get_tau(topology, np.eye(K), stats, K)

    deltas, bias_abs, tau_curve = _compute_bias_curve(
        topology, C0, stats, K, tau_true, n_grid
    )
    envelope = _compute_envelope(bias_abs)

    asv = _find_threshold_crossing(
        envelope, deltas, tau_curve, tau_true, threshold_type, threshold_value
    )

    return {
        "asv": asv,
        "bias_curve": bias_abs,
        "envelope": envelope,
        "deltas": deltas,
        "tau_true": float(tau_true),
    }
