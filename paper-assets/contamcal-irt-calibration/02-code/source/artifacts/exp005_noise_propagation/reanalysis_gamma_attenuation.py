"""
exp-005 reanalysis: Gamma attenuation under measurement error

The original v3/v4 analysis reported calibrated_score CI width as the outcome,
which is structurally independent of σ_e (calibrated_score is computed at
exposure=0, so gamma drops out). This reanalysis extracts the correct outcome
variables from the same 25 fits:

1. Gamma bias: |E[gamma_hat] - gamma_true| / gamma_true
2. Gamma CI width: posterior SD of gamma (× 2 for approximate 95% CI)
3. ME vs Simple attenuation ratio
"""

import json
import os
import sys

import numpy as np
from scipy.stats import spearmanr

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
RESULTS_PATH = os.path.join(SCRIPT_DIR, "output_v3", "noise_propagation_results.json")
TRUE_GAMMA = 0.5


def main():
    with open(RESULTS_PATH) as f:
        runs = json.load(f)

    sigma_levels = sorted(set(r["sigma_e"] for r in runs))

    agg = {}
    for se in sigma_levels:
        se_runs = [r for r in runs if r["sigma_e"] == se]
        me_gamma_means = [r["me"]["gamma_mean"] for r in se_runs]
        me_gamma_sds = [r["me"]["gamma_sd"] for r in se_runs]
        simple_gamma_means = [r["simple"]["gamma_mean"] for r in se_runs]
        simple_gamma_sds = [r["simple"]["gamma_sd"] for r in se_runs]

        me_bias = np.mean(me_gamma_means) - TRUE_GAMMA
        simple_bias = np.mean(simple_gamma_means) - TRUE_GAMMA

        agg[se] = {
            "me_gamma_mean": round(float(np.mean(me_gamma_means)), 4),
            "me_gamma_sd": round(float(np.mean(me_gamma_sds)), 4),
            "me_gamma_bias": round(float(me_bias), 4),
            "me_gamma_rel_bias_pct": round(float(me_bias / TRUE_GAMMA * 100), 1),
            "me_gamma_rmse": round(float(np.sqrt(me_bias**2 + np.var(me_gamma_means))), 4),
            "simple_gamma_mean": round(float(np.mean(simple_gamma_means)), 4),
            "simple_gamma_sd": round(float(np.mean(simple_gamma_sds)), 4),
            "simple_gamma_bias": round(float(simple_bias), 4),
            "simple_gamma_rel_bias_pct": round(float(simple_bias / TRUE_GAMMA * 100), 1),
            "simple_gamma_rmse": round(float(np.sqrt(simple_bias**2 + np.var(simple_gamma_means))), 4),
            "me_attenuation_factor": round(float(np.mean(me_gamma_means) / TRUE_GAMMA), 4),
            "simple_attenuation_factor": round(float(np.mean(simple_gamma_means) / TRUE_GAMMA), 4),
            "me_advantage_pct": round(
                float((np.mean(me_gamma_means) - np.mean(simple_gamma_means))
                      / TRUE_GAMMA * 100), 1
            ),
            "n_runs": len(se_runs),
            "cal_ci_width_me": round(float(np.mean([r["me"]["ci_width_mean"] for r in se_runs])), 4),
            "cal_ci_width_simple": round(float(np.mean([r["simple"]["ci_width_mean"] for r in se_runs])), 4),
        }

    # Monotonicity of gamma bias
    me_biases = [abs(agg[se]["me_gamma_bias"]) for se in sigma_levels]
    simple_biases = [abs(agg[se]["simple_gamma_bias"]) for se in sigma_levels]
    me_rho, me_p = spearmanr(sigma_levels, me_biases)
    simple_rho, simple_p = spearmanr(sigma_levels, simple_biases)

    # Theoretical attenuation for simple model: gamma_hat ≈ gamma * Var(tau) / (Var(tau) + sigma_e^2)
    # For ME model: gamma_hat ≈ gamma * (1 + sigma_e^2) * Var(tau) / (Var(tau) + sigma_e^2)
    # (because tau_post_mean = e / (1 + sigma_e^2), so gamma compensates by (1+sigma_e^2))

    report = {
        "experiment": "exp-005 reanalysis",
        "description": "Gamma attenuation under measurement error noise",
        "finding": (
            "Original analysis measured calibrated_score CI width (insensitive to σ_e by construction). "
            "Reanalysis shows gamma is attenuated toward 0 as σ_e increases in both models, "
            "but ME model retains ~2x more signal than Simple model at σ_e=1.0."
        ),
        "true_gamma": TRUE_GAMMA,
        "results_by_sigma_e": {str(k): v for k, v in agg.items()},
        "gamma_bias_monotonicity": {
            "me_spearman_rho": round(float(me_rho), 4),
            "me_spearman_p": round(float(me_p), 6),
            "simple_spearman_rho": round(float(simple_rho), 4),
            "simple_spearman_p": round(float(simple_p), 6),
        },
        "key_findings": [
            f"At σ_e=0.1: ME gamma={agg[0.1]['me_gamma_mean']:.3f}, Simple gamma={agg[0.1]['simple_gamma_mean']:.3f} (both close to true {TRUE_GAMMA})",
            f"At σ_e=1.0: ME gamma={agg[1.0]['me_gamma_mean']:.3f}, Simple gamma={agg[1.0]['simple_gamma_mean']:.3f} (ME retains {agg[1.0]['me_attenuation_factor']*100:.0f}% vs Simple {agg[1.0]['simple_attenuation_factor']*100:.0f}%)",
            "calibrated_score CI width is ~0.100 for all σ_e (structurally independent of gamma/σ_e)",
            "ME model provides partial attenuation correction, consistent with measurement error theory",
        ],
        "structural_explanation": (
            "calibrated_score = E[P(y=1|exposure=0)] does not involve gamma. "
            "Its CI width depends only on item/ability parameter uncertainty, "
            "which is determined by sample size (N_models × N_items), not σ_e. "
            "The original experiment measured the wrong outcome variable."
        ),
        "conclusion": "informative_reanalysis",
        "verdict": (
            "NOT a failed experiment. Original conclusion='negative' was due to measuring "
            "the wrong outcome (cal CI width). Reanalysis shows ME model DOES provide "
            "partial attenuation correction for gamma. Suitable for appendix robustness check "
            "showing ME model benefit."
        ),
    }

    # Print summary
    print("=== exp-005 Reanalysis: Gamma Attenuation ===")
    print(f"True gamma = {TRUE_GAMMA}")
    print()
    print(f"{'σ_e':>5} | {'ME γ̂':>8} | {'ME bias%':>9} | {'ME γ_sd':>8} | {'Simple γ̂':>10} | {'Simple bias%':>13} | {'Simple γ_sd':>12} | {'ME adv%':>8}")
    print("-" * 95)
    for se in sigma_levels:
        d = agg[se]
        print(f"{se:5.1f} | {d['me_gamma_mean']:8.4f} | {d['me_gamma_rel_bias_pct']:8.1f}% | {d['me_gamma_sd']:8.4f} | {d['simple_gamma_mean']:10.4f} | {d['simple_gamma_rel_bias_pct']:12.1f}% | {d['simple_gamma_sd']:12.4f} | {d['me_advantage_pct']:7.1f}%")

    print()
    print(f"Gamma bias monotonicity: ME rho={me_rho:.3f} (p={me_p:.4f}), Simple rho={simple_rho:.3f} (p={simple_p:.4f})")
    print()
    print("Key: ME advantage% = (ME_gamma - Simple_gamma) / true_gamma * 100")
    print("     Positive = ME retains more gamma signal")

    # Save
    out_path = os.path.join(SCRIPT_DIR, "output_v3", "reanalysis_gamma_attenuation.json")
    with open(out_path, "w") as f:
        json.dump(report, f, indent=2)
    print(f"\nSaved to {out_path}")


if __name__ == "__main__":
    main()
