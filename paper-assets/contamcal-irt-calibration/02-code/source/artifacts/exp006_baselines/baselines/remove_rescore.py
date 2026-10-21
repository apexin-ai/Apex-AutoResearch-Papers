"""Baseline 4: Remove-and-rescore — drop high-exposure items."""
import numpy as np
from .utils import wilson_ci, make_result


def calibrate(model_name, benchmark, item_scores, exposure_scores,
              threshold=0.5, **kwargs):
    mask = exposure_scores <= threshold
    n_kept = int(np.sum(mask))
    if n_kept == 0:
        return make_result(
            calibrated_accuracy=np.nan,
            ci_lower=np.nan,
            ci_upper=np.nan,
            method_name="remove_rescore",
            details={"threshold": threshold, "n_kept": 0, "n_removed": len(item_scores)},
        )
    kept_scores = item_scores[mask]
    n_correct = int(np.sum(kept_scores))
    acc, ci_lo, ci_hi = wilson_ci(n_correct, n_kept)
    return make_result(
        calibrated_accuracy=np.mean(kept_scores),
        ci_lower=ci_lo,
        ci_upper=ci_hi,
        method_name="remove_rescore",
        details={
            "threshold": threshold,
            "n_kept": n_kept,
            "n_removed": int(len(item_scores) - n_kept),
            "frac_removed": float(1 - n_kept / len(item_scores)),
        },
    )
