"""Shared utilities for baseline calibration methods."""
import numpy as np
from scipy import stats


def wilson_ci(n_correct, n_total, alpha=0.05):
    """Wilson score interval for binomial proportion."""
    if n_total == 0:
        return 0.0, 0.0, 0.0
    p_hat = n_correct / n_total
    z = stats.norm.ppf(1 - alpha / 2)
    denom = 1 + z**2 / n_total
    center = (p_hat + z**2 / (2 * n_total)) / denom
    margin = z * np.sqrt(p_hat * (1 - p_hat) / n_total + z**2 / (4 * n_total**2)) / denom
    return center, max(0, center - margin), min(1, center + margin)


def bootstrap_ci(statistic_fn, data, n_boot=1000, alpha=0.05, rng=None):
    """Bootstrap confidence interval for an arbitrary statistic.

    Args:
        statistic_fn: callable that takes resampled data and returns a scalar
        data: tuple of arrays to resample (resampled jointly by row)
        n_boot: number of bootstrap resamples
        alpha: significance level
        rng: numpy random generator

    Returns:
        (point_estimate, ci_lower, ci_upper)
    """
    if rng is None:
        rng = np.random.default_rng(42)
    n = len(data[0])
    boot_stats = np.empty(n_boot)
    for b in range(n_boot):
        idx = rng.integers(0, n, size=n)
        resampled = tuple(arr[idx] for arr in data)
        boot_stats[b] = statistic_fn(*resampled)
    point = statistic_fn(*data)
    lo = np.percentile(boot_stats, 100 * alpha / 2)
    hi = np.percentile(boot_stats, 100 * (1 - alpha / 2))
    return point, lo, hi


def make_result(calibrated_accuracy, ci_lower, ci_upper, method_name, details=None):
    """Standardized result dict."""
    return {
        "calibrated_accuracy": float(calibrated_accuracy),
        "ci_lower": float(ci_lower),
        "ci_upper": float(ci_upper),
        "method_name": method_name,
        "details": details or {},
    }
