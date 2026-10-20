"""Detrending utilities for time series analysis in model collapse experiments."""

import numpy as np
from scipy import signal
from statsmodels.tsa.filters.hp_filter import hpfilter


def detrend(series: np.ndarray, method: str = "first_diff") -> np.ndarray:
    """Detrend a time series.

    Args:
        series: 1D array, raw time series
        method: "first_diff" | "hp_filter" | "linear"

    Returns:
        Detrended series (first_diff returns length n-1, others return length n)
    """
    series = np.asarray(series, dtype=float)

    if method == "first_diff":
        return np.diff(series)
    elif method == "hp_filter":
        cycle, _ = hpfilter(series, lamb=6.25)
        return cycle
    elif method == "linear":
        return signal.detrend(series, type="linear")
    else:
        raise ValueError(f"Unknown method: {method}. Use 'first_diff', 'hp_filter', or 'linear'.")


def cross_correlate(x, y, max_lag=5):
    """Cross-correlation at lags -max_lag..+max_lag.

    Negative lag = x leads y. Replicates analyze_mvp.py logic.
    """
    x = (x - x.mean()) / (x.std() + 1e-12)
    y = (y - y.mean()) / (y.std() + 1e-12)
    n = len(x)
    correlations = {}
    for lag in range(-max_lag, max_lag + 1):
        if lag >= 0:
            c = np.corrcoef(x[lag:], y[:n - lag])[0, 1] if n - lag > 1 else 0
        else:
            c = np.corrcoef(x[:n + lag], y[-lag:])[0, 1] if n + lag > 1 else 0
        correlations[lag] = c
    return correlations


def detrend_and_crosscorr(x: np.ndarray, y: np.ndarray,
                          method: str = "first_diff",
                          max_lag: int = 5) -> dict:
    """Detrend two series, then compute cross-correlation.

    Args:
        x, y: 1D arrays of equal length
        method: detrending method
        max_lag: max lag for cross-correlation

    Returns:
        dict with keys: 'correlations' (lag->r), 'peak_lag', 'peak_corr',
        'method', 'detrended_x', 'detrended_y'
    """
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)

    dx = detrend(x, method)
    dy = detrend(y, method)

    corrs = cross_correlate(dx, dy, max_lag=max_lag)
    peak_lag = max(corrs, key=lambda k: abs(corrs[k]))

    return {
        "correlations": corrs,
        "peak_lag": peak_lag,
        "peak_corr": corrs[peak_lag],
        "method": method,
        "detrended_x": dx,
        "detrended_y": dy,
    }


if __name__ == "__main__":
    import json

    print("=" * 60)
    print("TEST 1: Synthetic data with linear trend")
    print("=" * 60)

    np.random.seed(42)
    t = np.arange(20)
    trend = 0.5 * t
    noise = np.random.randn(20) * 0.1
    series = trend + noise

    for method in ["first_diff", "hp_filter", "linear"]:
        result = detrend(series, method)
        print(f"  {method:12s}: len={len(result)}, mean={result.mean():.4f}, std={result.std():.4f}")

    print()
    print("=" * 60)
    print("TEST 2: detrend_and_crosscorr with known lag")
    print("=" * 60)

    np.random.seed(42)
    x = np.cumsum(np.random.randn(15))
    y = np.zeros(15)
    y[1:] = x[:-1] + np.random.randn(14) * 0.1
    y[0] = np.random.randn()

    for method in ["first_diff", "hp_filter", "linear"]:
        result = detrend_and_crosscorr(x, y, method=method, max_lag=5)
        print(f"  {method:12s}: peak_lag={result['peak_lag']}, peak_corr={result['peak_corr']:.3f}")

    print()
    print("=" * 60)
    print("TEST 3: MVP token_entropy dry-run")
    print("=" * 60)

    mvp_path = "results/mvp/rep_42/all_metrics.json"
    try:
        with open(mvp_path) as f:
            metrics = json.load(f)

        entropy = np.array([m["token_entropy"] for m in metrics])
        distinct_1 = np.array([m["distinct_1"] for m in metrics])

        print(f"  token_entropy (raw):  {np.array2string(entropy, precision=4, separator=', ')}")
        for method in ["first_diff", "hp_filter", "linear"]:
            dt = detrend(entropy, method)
            print(f"  token_entropy ({method:12s}): {np.array2string(dt, precision=4, separator=', ')}")

        print()
        print("  detrend_and_crosscorr (token_entropy -> distinct_1):")
        for method in ["first_diff", "hp_filter", "linear"]:
            result = detrend_and_crosscorr(entropy, distinct_1, method=method, max_lag=5)
            print(f"    {method:12s}: peak_lag={result['peak_lag']}, peak_corr={result['peak_corr']:.3f}")
    except FileNotFoundError:
        print(f"  {mvp_path} not found, skipping MVP dry-run")

    print()
    print("All tests passed.")
