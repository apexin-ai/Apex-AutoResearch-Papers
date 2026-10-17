#!/usr/bin/env python3
"""Beta Regression + ε Sensitivity analysis.

Part A: Beta regression (GLM Binomial/logit) vs OLS on log-transformed ASR.
Part B: ε sensitivity for canonical log-log OLS across {1e-3, 1e-6, 1e-9}.
"""

import sys
import json
import os
import itertools
import numpy as np
import statsmodels.api as sm
from statsmodels.stats.multitest import multipletests

sys.path.insert(0, "/root/cert_manip_resist_eval")
from src.unified_data_loader import load_all_scores, load_mi_data, load_pairs, ALL_MODELS, DATASETS, ATTACKS, _is_valid_score

FDR_ALPHA = 0.05
BETA_EPS = 1e-6  # clamp for beta regression


def majority_vote(votes):
    counts = {"A": 0, "B": 0, "tie": 0}
    for v in votes:
        counts[v] = counts.get(v, 0) + 1
    mx = max(counts.values())
    winners = [k for k, c in counts.items() if c == mx]
    if len(winners) == 1:
        return winners[0]
    for w in winners:
        if w != "tie":
            return w
    return "tie"


def compute_individual_asr(clean_list, attacked_list, pairs):
    n = min(len(clean_list), len(attacked_list), len(pairs))
    n_flips = n_correct = 0
    for i in range(n):
        if not _is_valid_score(clean_list[i]) or not _is_valid_score(attacked_list[i]):
            continue
        gt = pairs[i]["ground_truth_winner"]
        if clean_list[i]["winner"] == gt:
            n_correct += 1
            if attacked_list[i]["winner"] != gt:
                n_flips += 1
    return n_flips / max(n_correct, 1)


def compute_panel_asr(jids, clean, attacked, pairs):
    n = min(len(pairs), *(len(clean[j]) for j in jids), *(len(attacked[j]) for j in jids))
    n_flips = n_correct = 0
    for i in range(n):
        if not all(_is_valid_score(clean[j][i]) for j in jids):
            continue
        if not all(_is_valid_score(attacked[j][i]) for j in jids):
            continue
        gt = pairs[i]["ground_truth_winner"]
        cv = majority_vote([clean[j][i]["winner"] for j in jids])
        if cv != gt:
            continue
        n_correct += 1
        av = majority_vote([attacked[j][i]["winner"] for j in jids])
        if av != gt:
            n_flips += 1
    return n_flips / max(n_correct, 1)


def build_condition_data(ds, atk, clean, attacked, pairs_list, mi_data, all_models):
    """Build arrays of (panel_asr, keff, eta_max) for one condition."""
    ind_asr = {}
    for m in all_models:
        if m in clean[ds] and m in attacked[ds].get(atk, {}):
            ind_asr[m] = compute_individual_asr(
                clean[ds][m], attacked[ds][atk][m], pairs_list[ds]
            )

    keff_panels = mi_data.get("keff_per_panel", {}).get(ds, {})

    p_asrs, p_keffs, p_etas = [], [], []
    for combo in itertools.combinations(all_models, 3):
        jids = list(combo)
        pk = "|".join(jids)
        if pk not in keff_panels:
            continue
        if not all(j in ind_asr for j in jids):
            continue
        if not all(j in clean[ds] and j in attacked[ds].get(atk, {}) for j in jids):
            continue

        asr = compute_panel_asr(jids, clean[ds], attacked[ds][atk], pairs_list[ds])
        keff = keff_panels[pk]["keff"]
        eta_max = max(ind_asr[j] for j in jids)

        p_asrs.append(asr)
        p_keffs.append(keff)
        p_etas.append(eta_max)

    return np.array(p_asrs), np.array(p_keffs), np.array(p_etas)


def run_beta_regression(p_asrs, p_keffs, p_etas):
    """Beta regression via GLM Binomial(logit link)."""
    y = np.clip(p_asrs, BETA_EPS, 1 - BETA_EPS)
    log_keff = np.log(p_keffs)
    log_eta = np.log(p_etas + BETA_EPS)
    X = sm.add_constant(np.column_stack([log_keff, log_eta]))

    model = sm.GLM(y, X, family=sm.families.Binomial(link=sm.families.links.Logit()))
    result = model.fit()

    sd_y = np.std(y)
    keff_std_beta = float(result.params[1] * np.std(log_keff) / sd_y) if sd_y > 0 else 0.0
    eta_std_beta = float(result.params[2] * np.std(log_eta) / sd_y) if sd_y > 0 else 0.0

    pseudo_r2 = 1.0 - result.deviance / result.null_deviance if result.null_deviance > 0 else 0.0

    return {
        "eta_std_beta": round(eta_std_beta, 6),
        "eta_p": float(result.pvalues[2]),
        "keff_std_beta": round(keff_std_beta, 6),
        "keff_p": float(result.pvalues[1]),
        "pseudo_r2": round(float(pseudo_r2), 6),
        "n_panels": len(p_asrs),
    }


def run_ols(p_asrs, p_keffs, p_etas, eps):
    """Canonical log-log OLS."""
    y = np.log(p_asrs + eps)
    log_keff = np.log(p_keffs)
    log_eta = np.log(p_etas + eps)
    X = sm.add_constant(np.column_stack([log_keff, log_eta]))

    result = sm.OLS(y, X).fit()

    sd_y = np.std(y)
    keff_std_beta = float(result.params[1] * np.std(log_keff) / sd_y) if sd_y > 0 else 0.0
    eta_std_beta = float(result.params[2] * np.std(log_eta) / sd_y) if sd_y > 0 else 0.0

    return {
        "eta_std_beta": round(eta_std_beta, 6),
        "eta_p": float(result.pvalues[2]),
        "keff_std_beta": round(keff_std_beta, 6),
        "keff_p": float(result.pvalues[1]),
        "r2": round(float(result.rsquared), 6),
    }


def main():
    print("Loading data...")
    clean, attacked = load_all_scores()
    pairs_list = load_pairs()
    mi_data = load_mi_data()

    conditions = [(ds, atk) for ds in DATASETS for atk in ATTACKS]

    # ---- Part A: Beta Regression ----
    print("Running beta regression...")
    beta_results = {}
    ols_baseline = {}
    beta_eta_ps, beta_keff_ps = [], []
    ols_eta_ps, ols_keff_ps = [], []
    valid_keys = []

    for ds, atk in conditions:
        ck = f"{ds}__{atk}"
        p_asrs, p_keffs, p_etas = build_condition_data(
            ds, atk, clean, attacked, pairs_list, mi_data, ALL_MODELS
        )
        if len(p_asrs) < 10:
            print(f"  SKIP {ck}: only {len(p_asrs)} panels")
            continue

        valid_keys.append(ck)

        br = run_beta_regression(p_asrs, p_keffs, p_etas)
        beta_results[ck] = br
        beta_eta_ps.append(br["eta_p"])
        beta_keff_ps.append(br["keff_p"])

        ol = run_ols(p_asrs, p_keffs, p_etas, eps=1e-6)
        ols_baseline[ck] = ol
        ols_eta_ps.append(ol["eta_p"])
        ols_keff_ps.append(ol["keff_p"])

    # FDR correction for beta regression
    if beta_eta_ps:
        _, fdr_eta, _, _ = multipletests(beta_eta_ps, method="fdr_bh")
        _, fdr_keff, _, _ = multipletests(beta_keff_ps, method="fdr_bh")
        for i, ck in enumerate(valid_keys):
            beta_results[ck]["eta_fdr_p"] = float(fdr_eta[i])
            beta_results[ck]["keff_fdr_p"] = float(fdr_keff[i])

    # FDR correction for OLS baseline
    if ols_eta_ps:
        _, fdr_eta_ols, _, _ = multipletests(ols_eta_ps, method="fdr_bh")
        _, fdr_keff_ols, _, _ = multipletests(ols_keff_ps, method="fdr_bh")
        for i, ck in enumerate(valid_keys):
            ols_baseline[ck]["eta_fdr_p"] = float(fdr_eta_ols[i])
            ols_baseline[ck]["keff_fdr_p"] = float(fdr_keff_ols[i])

    # Summarize beta regression
    beta_eta_sig = sum(1 for ck in valid_keys if beta_results[ck].get("eta_fdr_p", 1) < FDR_ALPHA)
    beta_keff_sig = sum(1 for ck in valid_keys if beta_results[ck].get("keff_fdr_p", 1) < FDR_ALPHA)
    beta_eta_dom = sum(
        1 for ck in valid_keys
        if abs(beta_results[ck]["eta_std_beta"]) > abs(beta_results[ck]["keff_std_beta"])
    )

    # Compare ranking with OLS
    ranking_matches = 0
    for ck in valid_keys:
        beta_eta_dom_flag = abs(beta_results[ck]["eta_std_beta"]) > abs(beta_results[ck]["keff_std_beta"])
        ols_eta_dom_flag = abs(ols_baseline[ck]["eta_std_beta"]) > abs(ols_baseline[ck]["keff_std_beta"])
        if beta_eta_dom_flag == ols_eta_dom_flag:
            ranking_matches += 1

    vs_ols = "ranking_preserved" if ranking_matches == len(valid_keys) else "ranking_changed"
    n_total = len(valid_keys)

    # ---- Part B: ε Sensitivity ----
    print("Running epsilon sensitivity...")
    epsilons = [1e-3, 1e-6, 1e-9]
    eps_results = {}

    for eps in epsilons:
        eps_key = f"{eps:.0e}"
        cond_results = {}
        eta_ps, keff_ps = [], []
        eps_valid = []

        for ds, atk in conditions:
            ck = f"{ds}__{atk}"
            p_asrs, p_keffs, p_etas = build_condition_data(
                ds, atk, clean, attacked, pairs_list, mi_data, ALL_MODELS
            )
            if len(p_asrs) < 10:
                continue
            eps_valid.append(ck)
            ol = run_ols(p_asrs, p_keffs, p_etas, eps=eps)
            cond_results[ck] = ol
            eta_ps.append(ol["eta_p"])
            keff_ps.append(ol["keff_p"])

        if eta_ps:
            _, fdr_eta, _, _ = multipletests(eta_ps, method="fdr_bh")
            _, fdr_keff, _, _ = multipletests(keff_ps, method="fdr_bh")
            for i, ck in enumerate(eps_valid):
                cond_results[ck]["eta_fdr_p"] = float(fdr_eta[i])
                cond_results[ck]["keff_fdr_p"] = float(fdr_keff[i])

        eta_fdr_sig = sum(1 for ck in eps_valid if cond_results[ck].get("eta_fdr_p", 1) < FDR_ALPHA)
        keff_fdr_sig = sum(1 for ck in eps_valid if cond_results[ck].get("keff_fdr_p", 1) < FDR_ALPHA)

        eps_results[eps_key] = {
            "eta_fdr_sig": f"{eta_fdr_sig}/{len(eps_valid)}",
            "keff_fdr_sig": f"{keff_fdr_sig}/{len(eps_valid)}",
            "per_condition": {ck: {
                "eta_std_beta": cond_results[ck]["eta_std_beta"],
                "keff_std_beta": cond_results[ck]["keff_std_beta"],
            } for ck in eps_valid},
        }

    # Compute max beta change relative to 1e-6 baseline
    baseline_key = "1e-06"
    max_beta_change = 0.0
    for eps_key in eps_results:
        if eps_key == baseline_key:
            continue
        for ck in eps_results[eps_key]["per_condition"]:
            if ck in eps_results[baseline_key]["per_condition"]:
                base_eta = eps_results[baseline_key]["per_condition"][ck]["eta_std_beta"]
                base_keff = eps_results[baseline_key]["per_condition"][ck]["keff_std_beta"]
                cur_eta = eps_results[eps_key]["per_condition"][ck]["eta_std_beta"]
                cur_keff = eps_results[eps_key]["per_condition"][ck]["keff_std_beta"]

                if abs(base_eta) > 1e-10:
                    max_beta_change = max(max_beta_change, abs((cur_eta - base_eta) / base_eta) * 100)
                if abs(base_keff) > 1e-10:
                    max_beta_change = max(max_beta_change, abs((cur_keff - base_keff) / base_keff) * 100)

    # Strip per_condition from eps_results for output
    eps_output = {}
    for ek in eps_results:
        eps_output[ek] = {
            "eta_fdr_sig": eps_results[ek]["eta_fdr_sig"],
            "keff_fdr_sig": eps_results[ek]["keff_fdr_sig"],
        }

    # ---- Assemble output ----
    output = {
        "beta_regression": {
            "per_condition": {ck: {
                "eta_std_beta": beta_results[ck]["eta_std_beta"],
                "eta_p": round(beta_results[ck].get("eta_fdr_p", beta_results[ck]["eta_p"]), 6),
                "keff_std_beta": beta_results[ck]["keff_std_beta"],
                "keff_p": round(beta_results[ck].get("keff_fdr_p", beta_results[ck]["keff_p"]), 6),
                "pseudo_r2": beta_results[ck]["pseudo_r2"],
            } for ck in valid_keys},
            "summary": {
                "eta_fdr_sig": f"{beta_eta_sig}/{n_total}",
                "keff_fdr_sig": f"{beta_keff_sig}/{n_total}",
                "eta_dominates": f"{beta_eta_dom}/{n_total}",
            },
            "vs_ols": vs_ols,
            "ranking_match_detail": f"{ranking_matches}/{n_total}",
        },
        "epsilon_sensitivity": {
            **eps_output,
            "max_beta_change_pct": round(max_beta_change, 2),
        },
    }

    out_path = "/root/cert_manip_resist_eval/artifacts/results/plan001/beta_reg_epsilon.json"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"Saved to {out_path}")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
