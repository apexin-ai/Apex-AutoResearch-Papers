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


def wilson_ci_levels(n_correct, n_total):
    """Wilson CIs at 50%, 80%, 95% levels."""
    ci = {}
    for level, alpha in [(50, 0.50), (80, 0.20), (95, 0.05)]:
        _, lo, hi = wilson_ci(n_correct, n_total, alpha=alpha)
        ci[f"ci_{level}_lower"] = float(lo)
        ci[f"ci_{level}_upper"] = float(hi)
    return ci


def bootstrap_ci(statistic_fn, data, n_boot=1000, alpha=0.05, rng=None):
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


def bootstrap_ci_levels(statistic_fn, data, n_boot=1000, rng=None):
    """Bootstrap CIs at 50%, 80%, 95% levels."""
    if rng is None:
        rng = np.random.default_rng(42)
    n = len(data[0])
    boot_stats = np.empty(n_boot)
    for b in range(n_boot):
        idx = rng.integers(0, n, size=n)
        resampled = tuple(arr[idx] for arr in data)
        boot_stats[b] = statistic_fn(*resampled)
    point = statistic_fn(*data)
    ci = {}
    for level, alpha in [(50, 0.50), (80, 0.20), (95, 0.05)]:
        ci[f"ci_{level}_lower"] = float(np.percentile(boot_stats, 100 * alpha / 2))
        ci[f"ci_{level}_upper"] = float(np.percentile(boot_stats, 100 * (1 - alpha / 2)))
    return point, ci


def posterior_ci_levels(samples):
    """Extract 50/80/95% CIs from posterior samples."""
    return {
        "ci_50_lower": float(np.percentile(samples, 25)),
        "ci_50_upper": float(np.percentile(samples, 75)),
        "ci_80_lower": float(np.percentile(samples, 10)),
        "ci_80_upper": float(np.percentile(samples, 90)),
        "ci_95_lower": float(np.percentile(samples, 2.5)),
        "ci_95_upper": float(np.percentile(samples, 97.5)),
    }


def make_result(calibrated_accuracy, ci, method_name, details=None):
    result = {
        "calibrated_accuracy": float(calibrated_accuracy),
        "method_name": method_name,
        "details": details or {},
    }
    result.update(ci)
    return result
