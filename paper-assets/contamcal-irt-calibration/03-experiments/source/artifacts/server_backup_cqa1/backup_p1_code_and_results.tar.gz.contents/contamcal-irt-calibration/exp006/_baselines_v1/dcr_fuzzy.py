"""Baseline 1: DCR fuzzy inference (adapted from Xu et al., EMNLP 2025).

Original DCR uses 4-level probing to get S1-S4 scores, then fuzzy inference
to compute a DCR Factor for multiplicative discounting.

Adaptation: We derive S1-S4 from per-item exposure scores by computing the
fraction of items exceeding increasing contamination thresholds.
"""
import numpy as np
from .utils import bootstrap_ci_levels, make_result


def _trapmf(x, abcd):
    a, b, c, d = abcd
    y = np.zeros_like(x, dtype=float)
    mask_rise = (x >= a) & (x < b)
    if b > a:
        y[mask_rise] = (x[mask_rise] - a) / (b - a)
    y[(x >= b) & (x <= c)] = 1.0
    mask_fall = (x > c) & (x <= d)
    if d > c:
        y[mask_fall] = (d - x[mask_fall]) / (d - c)
    return y


def _trimf(x, abc):
    return _trapmf(x, [abc[0], abc[1], abc[1], abc[2]])


def _compute_contamination_levels(exposure_scores):
    thresholds = [0.1, 0.3, 0.5, 0.7]
    return np.array([float(np.mean(exposure_scores > t)) for t in thresholds])


def _fuzzy_dcr(s_values):
    if np.mean(s_values) < 0.02:
        return 0.0

    x_in = np.linspace(0, 1, 101)
    in_low = _trapmf(x_in, [0, 0, 0.1, 0.3])
    in_med = _trapmf(x_in, [0.2, 0.4, 0.5, 0.6])
    in_high = _trapmf(x_in, [0.5, 0.8, 1.0, 1.0])

    x_out = np.linspace(0, 1, 101)
    out_negligible = _trapmf(x_out, [0, 0, 0.1, 0.3])
    out_minor = _trimf(x_out, [0.1, 0.3, 0.5])
    out_moderate = _trimf(x_out, [0.3, 0.5, 0.7])
    out_significant = _trimf(x_out, [0.5, 0.7, 0.9])
    out_severe = _trapmf(x_out, [0.7, 0.9, 1.0, 1.0])

    min_memb = max(0.001, np.mean(s_values))
    memberships = []
    for s in s_values:
        low_val = max(float(np.interp(s, x_in, in_low)), min_memb * 0.1)
        med_val = max(float(np.interp(s, x_in, in_med)), min_memb * 0.1)
        high_val = max(float(np.interp(s, x_in, in_high)), min_memb * 0.1)
        memberships.append({"Low": low_val, "Medium": med_val, "High": high_val})

    r0 = min(m["Low"] for m in memberships)
    r1 = max(memberships[2]["High"], memberships[3]["High"])
    r2 = max(memberships[0]["High"], memberships[1]["High"])
    avg_med = np.mean([m["Medium"] for m in memberships])
    r3 = avg_med
    r4 = max(memberships[0]["Medium"], memberships[1]["Low"])

    aggregated = np.fmax(
        np.fmin(r0, out_negligible),
        np.fmax(
            np.fmin(r1, out_severe),
            np.fmax(
                np.fmin(r2, out_significant),
                np.fmax(
                    np.fmin(r3, out_moderate),
                    np.fmin(r4, out_minor),
                ),
            ),
        ),
    )

    if np.max(aggregated) < 0.06:
        aggregated = np.fmax(aggregated, out_negligible * min_memb)

    total = np.sum(aggregated)
    if total < 1e-10:
        return min_memb
    dcr_factor = np.sum(x_out * aggregated) / total
    return float(np.clip(dcr_factor, 0, 1))


def calibrate(model_name, benchmark, item_scores, exposure_scores, n_boot=1000, **kwargs):
    # Adapted from Xu et al. (EMNLP 2025): uses continuous exposure score threshold
    # instead of original 4-level probing, as our pipeline produces per-item exposure scores.
    s_values = _compute_contamination_levels(exposure_scores)
    dcr_factor = _fuzzy_dcr(s_values)
    raw_acc = np.mean(item_scores)
    adj_acc = raw_acc * (1 - dcr_factor)

    def _boot_stat(scores, exposure):
        s = _compute_contamination_levels(exposure)
        f = _fuzzy_dcr(s)
        return np.mean(scores) * (1 - f)

    _, ci = bootstrap_ci_levels(
        _boot_stat,
        (item_scores, exposure_scores),
        n_boot=n_boot,
    )

    return make_result(
        calibrated_accuracy=adj_acc,
        ci=ci,
        method_name="dcr_fuzzy",
        details={
            "dcr_factor": dcr_factor,
            "raw_accuracy": float(raw_acc),
            "s_levels": s_values.tolist(),
        },
    )
