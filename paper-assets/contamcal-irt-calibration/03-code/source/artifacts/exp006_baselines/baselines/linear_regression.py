"""Baseline 3: Linear exposure regression with bootstrap CI."""
import numpy as np
from .utils import bootstrap_ci, make_result


def calibrate(model_name, benchmark, item_scores, exposure_scores, n_boot=1000, **kwargs):
    def _fit_intercept(scores, exposure):
        if np.std(exposure) < 1e-10:
            return np.mean(scores)
        beta1 = np.sum((exposure - exposure.mean()) * (scores - scores.mean())) / np.sum((exposure - exposure.mean())**2)
        beta0 = scores.mean() - beta1 * exposure.mean()
        return np.clip(beta0, 0, 1)

    point = _fit_intercept(item_scores, exposure_scores)
    _, ci_lo, ci_hi = bootstrap_ci(
        _fit_intercept,
        (item_scores, exposure_scores),
        n_boot=n_boot,
    )

    slope = 0.0
    if np.std(exposure_scores) > 1e-10:
        slope = float(np.sum((exposure_scores - exposure_scores.mean()) * (item_scores - item_scores.mean()))
                       / np.sum((exposure_scores - exposure_scores.mean())**2))

    return make_result(
        calibrated_accuracy=point,
        ci_lower=ci_lo,
        ci_upper=ci_hi,
        method_name="linear_regression",
        details={"slope": slope, "intercept": float(point)},
    )
