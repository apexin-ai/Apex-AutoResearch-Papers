"""Baseline 4: Remove-and-rescore — drop high-exposure items."""
import numpy as np
from .utils import wilson_ci_levels, make_result


def calibrate(model_name, benchmark, item_scores, exposure_scores,
              threshold=0.5, **kwargs):
    mask = exposure_scores <= threshold
    n_kept = int(np.sum(mask))
    if n_kept == 0:
        nan_ci = {f"ci_{l}_{b}": np.nan for l in [50, 80, 95] for b in ["lower", "upper"]}
        return make_result(
            calibrated_accuracy=np.nan,
            ci=nan_ci,
            method_name="remove_rescore",
            details={"threshold": threshold, "n_kept": 0, "n_removed": len(item_scores)},
        )
    kept_scores = item_scores[mask]
    n_correct = int(np.sum(kept_scores))
    ci = wilson_ci_levels(n_correct, n_kept)
    return make_result(
        calibrated_accuracy=np.mean(kept_scores),
        ci=ci,
        method_name="remove_rescore",
        details={
            "threshold": threshold,
            "n_kept": n_kept,
            "n_removed": int(len(item_scores) - n_kept),
            "frac_removed": float(1 - n_kept / len(item_scores)),
        },
    )
