"""Baseline 7: Raw scores — no calibration, trivial anchor point."""
import numpy as np
from .utils import wilson_ci, make_result


def calibrate(model_name, benchmark, item_scores, exposure_scores, **kwargs):
    n_correct = int(np.sum(item_scores))
    n_total = len(item_scores)
    acc, ci_lo, ci_hi = wilson_ci(n_correct, n_total)
    return make_result(
        calibrated_accuracy=np.mean(item_scores),
        ci_lower=ci_lo,
        ci_upper=ci_hi,
        method_name="raw_scores",
        details={"n_items": n_total, "n_correct": n_correct},
    )
