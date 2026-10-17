"""
Plan 003: Random-fault simulation vs adaptive attack comparison.
Proves K_eff is effective under independent faults but fails under adaptive attacks.
"""

import json
import numpy as np
import statsmodels.api as sm
from itertools import combinations
from pathlib import Path

SEED = 42
N_SIM = 1000
N_SAMPLES = 300
EPS = 0.001

STEP2_PATH = "/root/cert_manip_resist_eval/artifacts/results/results_step2v3_regression_20260522_031307.json"
TAXONOMY_PATH = "/root/cert_manip_resist_eval/artifacts/results/results_taxonomy_broadspectrum_20260522_044539.json"
OUTPUT_PATH = "/root/cert_manip_resist_eval/artifacts/results/results_plan003_random_fault.json"


def load_data():
    with open(STEP2_PATH) as f:
        step2 = json.load(f)
    with open(TAXONOMY_PATH) as f:
        taxonomy = json.load(f)
    return step2, taxonomy


def run_random_fault_sim(eta_js, n_samples, n_sim, rng):
    """Vectorized random-fault simulation for a 3-judge majority-vote panel.

    eta_js: list of 3 individual ASR values
    Returns: (mean_asr, std_asr)
    """
    eta_arr = np.array(eta_js)  # (3,)
    # (n_sim, n_samples, 3) Bernoulli draws
    faults = rng.random((n_sim, n_samples, 3)) < eta_arr[None, None, :]
    # majority vote: panel fails if >= 2 judges fail
    panel_fails = faults.sum(axis=2) >= 2  # (n_sim, n_samples)
    sim_asrs = panel_fails.mean(axis=1)  # (n_sim,)
    return float(sim_asrs.mean()), float(sim_asrs.std())


def run_regression(panels_data):
    """OLS: log(ASR + eps) ~ log(K_eff) + log(eta_max + eps)"""
    if len(panels_data) < 5:
        return {"beta_keff": None, "p_keff": None, "beta_eta_max": None, "p_eta_max": None, "R2": None}

    y = np.log(np.array([p["asr"] for p in panels_data]) + EPS)
    x1 = np.log(np.array([p["keff"] for p in panels_data]))
    x2 = np.log(np.array([p["eta_max"] for p in panels_data]) + EPS)
    X = sm.add_constant(np.column_stack([x1, x2]))

    model = sm.OLS(y, X).fit()
    return {
        "beta_keff": float(model.params[1]),
        "p_keff": float(model.pvalues[1]),
        "beta_eta_max": float(model.params[2]),
        "p_eta_max": float(model.pvalues[2]),
        "R2": float(model.rsquared),
    }


def process_source(data, attack_names, source_label, rng):
    """Process one data source (step2 or taxonomy)."""
    panels = data["all_20_panels"]
    individual_asr = data["individual_asr"]
    datasets = list(individual_asr.keys())

    results = {}

    for ds in datasets:
        for attack in attack_names:
            if attack not in individual_asr[ds]:
                continue

            condition_key = f"{ds}×{attack}"
            panel_records = []

            for panel in panels:
                judge_ids = panel["judge_ids"]
                keff = panel["k_eff"][ds]
                adaptive_asr = panel["asr_by_attack"][ds][attack]
                eta_max = panel["eta_max_by_attack"][ds][attack]

                # Get individual ASRs for panel members
                eta_js = [individual_asr[ds][attack][j] for j in judge_ids]

                # Random-fault simulation
                rf_mean, rf_std = run_random_fault_sim(eta_js, N_SAMPLES, N_SIM, rng)

                panel_records.append({
                    "panel": judge_ids,
                    "keff": keff,
                    "eta_max": eta_max,
                    "adaptive_asr": adaptive_asr,
                    "rf_asr_mean": rf_mean,
                    "rf_asr_std": rf_std,
                })

            # Regression on adaptive ASR
            adaptive_reg_data = [{"asr": p["adaptive_asr"], "keff": p["keff"], "eta_max": p["eta_max"]} for p in panel_records]
            adaptive_reg = run_regression(adaptive_reg_data)

            # Regression on random-fault ASR
            rf_reg_data = [{"asr": p["rf_asr_mean"], "keff": p["keff"], "eta_max": p["eta_max"]} for p in panel_records]
            rf_reg = run_regression(rf_reg_data)

            results[condition_key] = {
                "adaptive_keff_beta": adaptive_reg["beta_keff"],
                "adaptive_keff_p": adaptive_reg["p_keff"],
                "random_fault_keff_beta": rf_reg["beta_keff"],
                "random_fault_keff_p": rf_reg["p_keff"],
                "adaptive_eta_max_beta": adaptive_reg["beta_eta_max"],
                "adaptive_eta_max_p": adaptive_reg["p_eta_max"],
                "random_fault_eta_max_beta": rf_reg["beta_eta_max"],
                "random_fault_eta_max_p": rf_reg["p_eta_max"],
                "adaptive_R2": adaptive_reg["R2"],
                "random_fault_R2": rf_reg["R2"],
                "panels": panel_records,
            }

    return results


def main():
    rng = np.random.default_rng(SEED)
    step2, taxonomy = load_data()

    step2_attacks = step2["metadata"]["attack_names"]
    taxonomy_attacks = list(taxonomy["individual_asr"][list(taxonomy["individual_asr"].keys())[0]].keys())

    conditions = {}
    conditions.update(process_source(step2, step2_attacks, "step2", rng))
    conditions.update(process_source(taxonomy, taxonomy_attacks, "taxonomy", rng))

    # Summary
    total = len(conditions)
    adaptive_sig_neg = sum(
        1 for c in conditions.values()
        if c["adaptive_keff_p"] is not None and c["adaptive_keff_p"] < 0.05 and c["adaptive_keff_beta"] < 0
    )
    rf_sig_neg = sum(
        1 for c in conditions.values()
        if c["random_fault_keff_p"] is not None and c["random_fault_keff_p"] < 0.05 and c["random_fault_keff_beta"] < 0
    )

    # Build interpretation
    if rf_sig_neg > adaptive_sig_neg:
        interpretation = (
            f"Under random (independent) faults, K_eff is significantly negative in {rf_sig_neg}/{total} conditions, "
            f"confirming diversity-based defense works when faults are independent. "
            f"Under adaptive attacks, K_eff is significant in only {adaptive_sig_neg}/{total} conditions. "
            f"This gap demonstrates that adaptive attackers violate the BFT independence assumption, "
            f"rendering panel diversity ineffective as a defense."
        )
    else:
        interpretation = (
            f"Random-fault K_eff significant negative: {rf_sig_neg}/{total}; "
            f"Adaptive K_eff significant negative: {adaptive_sig_neg}/{total}. "
            f"Results require further analysis."
        )

    output = {
        "conditions": conditions,
        "summary": {
            "adaptive_keff_sig_negative": f"{adaptive_sig_neg}/{total}",
            "random_fault_keff_sig_negative": f"{rf_sig_neg}/{total}",
            "interpretation": interpretation,
        },
        "metadata": {
            "n_sim": N_SIM,
            "n_samples": N_SAMPLES,
            "seed": SEED,
            "epsilon": EPS,
            "step2_source": STEP2_PATH,
            "taxonomy_source": TAXONOMY_PATH,
        },
    }

    Path(OUTPUT_PATH).parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_PATH, "w") as f:
        json.dump(output, f, indent=2)

    print(f"Results written to {OUTPUT_PATH}")
    print(f"\nSummary:")
    print(f"  Adaptive K_eff sig negative: {adaptive_sig_neg}/{total}")
    print(f"  Random-fault K_eff sig negative: {rf_sig_neg}/{total}")
    print(f"\nPer-condition details:")
    for cond, vals in conditions.items():
        ad_p = vals["adaptive_keff_p"]
        rf_p = vals["random_fault_keff_p"]
        ad_b = vals["adaptive_keff_beta"]
        rf_b = vals["random_fault_keff_beta"]
        ad_r2 = vals["adaptive_R2"]
        rf_r2 = vals["random_fault_R2"]
        print(f"  {cond:40s}  adaptive: β={ad_b:+.3f} p={ad_p:.4f} R²={ad_r2:.3f}  |  random-fault: β={rf_b:+.3f} p={rf_p:.4f} R²={rf_r2:.3f}")


if __name__ == "__main__":
    main()
