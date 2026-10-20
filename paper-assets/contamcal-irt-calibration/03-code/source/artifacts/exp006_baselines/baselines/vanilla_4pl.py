"""Baseline 5: Vanilla 4PL IRT without γ — standard IRT calibration.

Uses CmdStanPy to fit a 4PL model without the contamination parameter γ.
Requires multi-model data via kwargs.
"""
import numpy as np
import os
import tempfile
from .utils import make_result

STAN_MODEL_DIR = "/root/contamcal-irt-calibration/stan_models"


def calibrate(model_name, benchmark, item_scores, exposure_scores,
              all_y=None, all_exposure=None, model_idx=0, stan_model_path=None,
              n_chains=4, n_samples=1000, **kwargs):
    """
    Args:
        all_y: (N_models, N_items) binary response matrix
        all_exposure: (N_models, N_items) exposure matrix (unused in vanilla 4PL)
        model_idx: index of the target model in all_y
        stan_model_path: path to vanilla_4pl.stan
    """
    if all_y is None:
        all_y = item_scores.reshape(1, -1)
        model_idx = 0

    try:
        from cmdstanpy import CmdStanModel
    except ImportError:
        return make_result(np.nan, np.nan, np.nan, "vanilla_4pl",
                           {"error": "cmdstanpy not installed"})

    if stan_model_path is None:
        stan_model_path = os.path.join(STAN_MODEL_DIR, "vanilla_4pl.stan")

    N_models, N_items = all_y.shape
    stan_data = {
        "N_models": N_models,
        "N_items": N_items,
        "y": all_y.tolist(),
    }

    try:
        model = CmdStanModel(stan_file=stan_model_path)
        fit = model.sample(
            data=stan_data,
            chains=n_chains,
            iter_sampling=n_samples,
            iter_warmup=n_samples,
            seed=42,
            show_progress=False,
            show_console=False,
        )
    except Exception as e:
        return make_result(np.nan, np.nan, np.nan, "vanilla_4pl",
                           {"error": str(e)})

    cal_key = f"calibrated_score[{model_idx + 1}]"
    cal_samples = fit.stan_variable("calibrated_score")[:, model_idx]

    point = float(np.mean(cal_samples))
    ci_lo = float(np.percentile(cal_samples, 2.5))
    ci_hi = float(np.percentile(cal_samples, 97.5))

    diagnostics = {}
    try:
        summary = fit.summary()
        diagnostics["max_rhat"] = float(summary["R_hat"].max())
        diagnostics["min_ess"] = float(summary["N_Eff"].min())
    except Exception:
        pass
    diagnostics["n_models"] = N_models
    diagnostics["n_items"] = N_items

    return make_result(
        calibrated_accuracy=point,
        ci_lower=ci_lo,
        ci_upper=ci_hi,
        method_name="vanilla_4pl",
        details=diagnostics,
    )
