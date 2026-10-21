"""Baseline 6: Single-signal 2PL+gamma IRT.

2PL (discrimination + difficulty, no guessing/upper asymptote)
with gamma contamination parameter.
"""
import numpy as np
import os
from .utils import make_result, posterior_ci_levels

STAN_MODEL_DIR = "/root/contamcal-irt-calibration/stan_models"


def calibrate(model_name, benchmark, item_scores, exposure_scores,
              all_y=None, all_exposure=None, model_idx=0, stan_model_path=None,
              n_chains=4, n_samples=1000, **kwargs):
    if all_y is None:
        all_y = item_scores.reshape(1, -1)
        all_exposure = exposure_scores.reshape(1, -1)
        model_idx = 0

    nan_ci = {f"ci_{l}_{b}": np.nan for l in [50, 80, 95] for b in ["lower", "upper"]}

    try:
        from cmdstanpy import CmdStanModel
    except ImportError:
        return make_result(np.nan, nan_ci, "single_signal_2pl_gamma",
                           {"error": "cmdstanpy not installed"})

    if stan_model_path is None:
        stan_model_path = os.path.join(STAN_MODEL_DIR, "contam_irt_2pl_gamma.stan")

    N_models, N_items = all_y.shape
    stan_data = {
        "N_models": N_models,
        "N_items": N_items,
        "y": all_y.tolist(),
        "exposure": all_exposure.tolist(),
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
        return make_result(np.nan, nan_ci, "single_signal_2pl_gamma",
                           {"error": str(e)})

    cal_samples = fit.stan_variable("calibrated_score")[:, model_idx]
    gamma_samples = fit.stan_variable("gamma")

    point = float(np.mean(cal_samples))
    ci = posterior_ci_levels(cal_samples)

    diagnostics = {
        "gamma_mean": float(np.mean(gamma_samples)),
        "gamma_sd": float(np.std(gamma_samples)),
    }
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
        ci=ci,
        method_name="single_signal_2pl_gamma",
        details=diagnostics,
    )
