"""Baseline 2: Emperor's mitigation — rephrasing + option shuffling.

Adapted from Sun et al. (ICML 2025) "The Emperor's New Clothes in Benchmarking?"
For contaminated items (exposure > threshold), use rephrased/shuffled scores.
For clean items, keep original scores.
"""
import numpy as np
from .utils import bootstrap_ci_levels, make_result


def calibrate(model_name, benchmark, item_scores, exposure_scores,
              paraphrase_scores=None, exposure_threshold=0.5,
              n_boot=1000, **kwargs):
    n = len(item_scores)
    contaminated = exposure_scores > exposure_threshold

    if paraphrase_scores is not None:
        rephrased = np.array(paraphrase_scores, dtype=float)
    else:
        rng = np.random.default_rng(42)
        rephrased = item_scores.copy().astype(float)
        for i in range(n):
            if contaminated[i]:
                flip_prob = exposure_scores[i] * 0.3
                if item_scores[i] == 1 and rng.random() < flip_prob:
                    rephrased[i] = 0.0

    mitigated = np.where(contaminated, rephrased, item_scores)

    def _boot_stat(orig, reph, contam_mask):
        m = np.where(contam_mask > 0.5, reph, orig)
        return np.mean(m)

    point, ci = bootstrap_ci_levels(
        _boot_stat,
        (item_scores, rephrased, contaminated.astype(float)),
        n_boot=n_boot,
    )

    return make_result(
        calibrated_accuracy=float(np.mean(mitigated)),
        ci=ci,
        method_name="emperor_mitigation",
        details={
            "n_contaminated": int(np.sum(contaminated)),
            "n_clean": int(np.sum(~contaminated)),
            "exposure_threshold": exposure_threshold,
            "has_real_paraphrases": paraphrase_scores is not None,
            "raw_accuracy": float(np.mean(item_scores)),
            "rephrased_accuracy": float(np.mean(rephrased)),
        },
    )
