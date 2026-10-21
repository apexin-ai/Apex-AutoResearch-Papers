#!/usr/bin/env python3
"""P2: 15-model 4-aggregation-strategy regression (455 panels x 12 conditions).

Aggregation methods: majority_vote, weighted_vote, threshold_vote, bayesian
For each: compute panel ASR, run residualized regression log(ASR+eps) ~ K_eff_resid + eta_max
FDR correction across 12 conditions per method.
"""

import os
os.environ["HF_HOME"] = "/root/autodl-tmp/.hf_cache"

import sys
sys.path.insert(0, "/root/cert_manip_resist_eval")

import json
import itertools
import numpy as np
import statsmodels.api as sm
from pathlib import Path
from collections import Counter
from sklearn.linear_model import LinearRegression
from statsmodels.stats.multitest import multipletests

from src.unified_data_loader import (
    ALL_MODELS, DATASETS, ATTACKS,
    load_all_scores, load_pairs, load_mi_data,
    compute_clean_accuracy,
)

EPS = 0.001

def _json_default(obj):
    if isinstance(obj, np.floating):
        v = float(obj)
        return None if (np.isnan(v) or np.isinf(v)) else v
    if isinstance(obj, np.integer):
        return int(obj)
    if isinstance(obj, np.ndarray):
        return obj.tolist()
    if isinstance(obj, np.bool_):
        return bool(obj)
    raise TypeError(f"Not JSON serializable: {type(obj)}")


def _is_valid_score(score):
    return score.get("winner") is not None and not score.get("error")


# ── Aggregation Methods ──────────────────────────────────────────────

def agg_majority(votes, _weights):
    counts = Counter(votes)
    mc = counts.most_common()
    if len(mc) == 1:
        return mc[0][0]
    if mc[0][1] > mc[1][1]:
        return mc[0][0]
    for k, _ in mc:
        if k != "tie":
            return k
    return "tie"


def agg_weighted(votes, weights):
    scores = {}
    for v, w in zip(votes, weights):
        scores[v] = scores.get(v, 0.0) + w
    ranked = sorted(scores.items(), key=lambda x: -x[1])
    if len(ranked) >= 2 and abs(ranked[0][1] - ranked[1][1]) < 1e-12:
        return "TIE"
    return ranked[0][0]


def agg_threshold(votes, _weights):
    if votes[0] == votes[1] == votes[2]:
        return votes[0]
    return "UNCERTAIN"


def agg_bayesian(votes, reliabilities):
    log_pa, log_pb = 0.0, 0.0
    for v, p in zip(votes, reliabilities):
        p = max(min(p, 0.999), 0.001)
        lp = np.log(p)
        l1p = np.log(1.0 - p)
        log_pa += lp if v == "A" else l1p
        log_pb += lp if v == "B" else l1p
    if log_pa > log_pb:
        return "A"
    if log_pb > log_pa:
        return "B"
    return "TIE"


METHODS = {
    "majority_vote": agg_majority,
    "weighted_vote": agg_weighted,
    "threshold_vote": agg_threshold,
    "bayesian": agg_bayesian,
}


# ── Panel ASR with error filtering ──────────────────────────────────

def compute_panel_asr_agg(jids, clean_ds, attacked_ds_atk, pairs_ds,
                          agg_fn, weights_per_judge, threshold_mode=False):
    """Compute error-corrected panel ASR under a given aggregation rule.

    For threshold_mode: only count samples where aggregation produces a
    definitive verdict (not UNCERTAIN).
    """
    n = min(len(pairs_ds), *(len(clean_ds[j]) for j in jids),
            *(len(attacked_ds_atk[j]) for j in jids))
    n_flips = n_correct = n_filtered = n_uncertain_clean = 0
    weights = [weights_per_judge[j] for j in jids]

    for i in range(n):
        any_invalid = False
        for j in jids:
            if not _is_valid_score(clean_ds[j][i]) or not _is_valid_score(attacked_ds_atk[j][i]):
                any_invalid = True
                break
        if any_invalid:
            n_filtered += 1
            continue

        gt = pairs_ds[i]["ground_truth_winner"]
        clean_votes = [clean_ds[j][i]["winner"] for j in jids]
        cv = agg_fn(clean_votes, weights)

        if threshold_mode and cv == "UNCERTAIN":
            n_uncertain_clean += 1
            continue

        if cv != gt:
            continue
        n_correct += 1

        atk_votes = [attacked_ds_atk[j][i]["winner"] for j in jids]
        av = agg_fn(atk_votes, weights)

        if threshold_mode and av == "UNCERTAIN":
            continue

        if av != gt:
            n_flips += 1

    asr = n_flips / max(n_correct, 1)
    return asr, n_correct, n_filtered


def compute_individual_corrected_asr(clean_list, attacked_list, pairs_ds):
    n = min(len(clean_list), len(attacked_list), len(pairs_ds))
    n_flips = n_correct = 0
    for i in range(n):
        if not _is_valid_score(clean_list[i]) or not _is_valid_score(attacked_list[i]):
            continue
        gt = pairs_ds[i]["ground_truth_winner"]
        if clean_list[i]["winner"] == gt:
            n_correct += 1
            if attacked_list[i]["winner"] != gt:
                n_flips += 1
    return n_flips / max(n_correct, 1)


# ── Regression ───────────────────────────────────────────────────────

def run_residualized_regression(panel_asrs, keffs, eta_maxs):
    y = np.log(panel_asrs + EPS)
    x1 = np.log(keffs)
    x2 = np.log(eta_maxs + EPS)

    X_orig = sm.add_constant(np.column_stack([x1, x2]))
    fit_orig = sm.OLS(y, X_orig).fit()

    reg = LinearRegression().fit(x2.reshape(-1, 1), x1)
    keff_resid = x1 - reg.predict(x2.reshape(-1, 1))

    X_resid = sm.add_constant(np.column_stack([keff_resid, x2]))
    fit_resid = sm.OLS(y, X_resid).fit()

    return {
        "eta_max_beta": float(fit_orig.params[2]),
        "eta_max_p": float(fit_orig.pvalues[2]),
        "keff_beta": float(fit_orig.params[1]),
        "keff_p": float(fit_orig.pvalues[1]),
        "keff_resid_beta": float(fit_resid.params[1]),
        "keff_resid_p": float(fit_resid.pvalues[1]),
        "eta_max_resid_beta": float(fit_resid.params[2]),
        "eta_max_resid_p": float(fit_resid.pvalues[2]),
        "R2_orig": float(fit_orig.rsquared),
        "R2_resid": float(fit_resid.rsquared),
        "n_panels": len(panel_asrs),
        "corr_keff_eta": float(np.corrcoef(x1, x2)[0, 1]),
        "asr_mean": float(np.mean(panel_asrs)),
        "asr_std": float(np.std(panel_asrs)),
    }


def main():
    print("Loading data...")
    mi_data = load_mi_data()
    pairs = load_pairs()
    clean, attacked = load_all_scores()

    clean_acc = compute_clean_accuracy(clean, pairs)
    print(f"Clean accuracy computed for {len(clean_acc)} (model, dataset) pairs")
    for (mid, ds), acc in sorted(clean_acc.items(), key=lambda x: x[1]):
        if acc < 0.6:
            print(f"  Low: {mid} on {ds}: {acc:.3f}")

    ind_asr = {}
    for ds in DATASETS:
        for atk in ATTACKS:
            for mid in ALL_MODELS:
                if mid in clean[ds] and mid in attacked[ds][atk]:
                    ind_asr[(ds, atk, mid)] = compute_individual_corrected_asr(
                        clean[ds][mid], attacked[ds][atk][mid], pairs[ds]
                    )
    print(f"Individual ASR: {len(ind_asr)} values")

    all_combos = list(itertools.combinations(range(len(ALL_MODELS)), 3))
    print(f"Total panels: {len(all_combos)}")

    output = {
        "analysis": "aggregation_regression_15model",
        "n_models": len(ALL_MODELS),
        "n_panels": len(all_combos),
        "models": ALL_MODELS,
        "datasets": DATASETS,
        "attacks": ATTACKS,
        "aggregation_methods": {},
    }

    for method_name, agg_fn in METHODS.items():
        print(f"\n{'='*80}")
        print(f"Aggregation: {method_name}")
        print(f"{'='*80}")

        is_threshold = method_name == "threshold_vote"
        conditions = {}
        raw_eta_ps = []
        raw_keff_resid_ps = []
        valid_cond_keys = []

        for ds in DATASETS:
            keff_data = mi_data["keff_per_panel"].get(ds, {})

            for atk in ATTACKS:
                cond = f"{ds}x{atk}"
                p_asrs, p_keffs, p_etas = [], [], []

                for combo in all_combos:
                    jids = [ALL_MODELS[i] for i in combo]

                    if not all((ds, atk, j) in ind_asr for j in jids):
                        continue
                    pk = "|".join(jids)
                    if pk not in keff_data:
                        continue

                    weights = {}
                    for j in jids:
                        weights[j] = clean_acc.get((j, ds), 0.5)

                    asr, n_correct, _ = compute_panel_asr_agg(
                        jids,
                        clean[ds], attacked[ds][atk],
                        pairs[ds],
                        agg_fn, weights,
                        threshold_mode=is_threshold,
                    )

                    keff = keff_data[pk]["keff"]
                    eta_max = max(ind_asr[(ds, atk, j)] for j in jids)

                    p_asrs.append(asr)
                    p_keffs.append(keff)
                    p_etas.append(eta_max)

                p_asrs = np.array(p_asrs)
                p_keffs = np.array(p_keffs)
                p_etas = np.array(p_etas)

                if len(p_asrs) < 10 or np.std(p_asrs) < 1e-10:
                    print(f"  {cond}: SKIPPED (n={len(p_asrs)}, std={np.std(p_asrs) if len(p_asrs)>0 else 0:.6f})")
                    conditions[cond] = {"skipped": True, "n_panels": len(p_asrs),
                                        "reason": "insufficient variance"}
                    continue

                res = run_residualized_regression(p_asrs, p_keffs, p_etas)
                conditions[cond] = res
                raw_eta_ps.append(res["eta_max_p"])
                raw_keff_resid_ps.append(res["keff_resid_p"])
                valid_cond_keys.append(cond)

                sig_e = "***" if res["eta_max_p"] < 0.001 else "**" if res["eta_max_p"] < 0.01 else "*" if res["eta_max_p"] < 0.05 else "ns"
                sig_k = "***" if res["keff_resid_p"] < 0.001 else "**" if res["keff_resid_p"] < 0.01 else "*" if res["keff_resid_p"] < 0.05 else "ns"
                print(f"  {cond:<30} R2={res['R2_resid']:.4f}  "
                      f"eta_max: B={res['eta_max_resid_beta']:+.4f} p={res['eta_max_resid_p']:.4e} {sig_e}  "
                      f"K_resid: B={res['keff_resid_beta']:+.4f} p={res['keff_resid_p']:.4e} {sig_k}  "
                      f"ASR={res['asr_mean']:.4f}±{res['asr_std']:.4f}  n={res['n_panels']}")

        if raw_eta_ps:
            _, fdr_eta, _, _ = multipletests(raw_eta_ps, method="fdr_bh")
            _, fdr_keff, _, _ = multipletests(raw_keff_resid_ps, method="fdr_bh")
            for i, ck in enumerate(valid_cond_keys):
                conditions[ck]["eta_max_fdr_p"] = float(fdr_eta[i])
                conditions[ck]["keff_resid_fdr_p"] = float(fdr_keff[i])

        n_valid = len(valid_cond_keys)
        eta_fdr_sig = sum(1 for ck in valid_cond_keys
                          if conditions[ck].get("eta_max_fdr_p", 1) < 0.05)
        keff_fdr_sig = sum(1 for ck in valid_cond_keys
                           if conditions[ck].get("keff_resid_fdr_p", 1) < 0.05)
        keff_neg = sum(1 for ck in valid_cond_keys
                       if conditions[ck]["keff_resid_beta"] < 0)
        mean_r2 = float(np.mean([conditions[ck]["R2_resid"] for ck in valid_cond_keys])) if valid_cond_keys else 0.0

        summary = {
            "eta_max_fdr_sig": f"{eta_fdr_sig}/{n_valid}",
            "keff_resid_fdr_sig": f"{keff_fdr_sig}/{n_valid}",
            "keff_resid_negative": f"{keff_neg}/{n_valid}",
            "mean_R2_resid": mean_r2,
        }

        print(f"\n  Summary: eta_max FDR sig={summary['eta_max_fdr_sig']}, "
              f"K_eff_resid FDR sig={summary['keff_resid_fdr_sig']}, "
              f"K_eff_resid negative={summary['keff_resid_negative']}, "
              f"mean R2={summary['mean_R2_resid']:.4f}")

        output["aggregation_methods"][method_name] = {
            "conditions": conditions,
            "summary": summary,
        }

    # ── Cross-method comparison ──────────────────────────────────────
    print(f"\n{'='*100}")
    print("CROSS-METHOD COMPARISON")
    print(f"{'='*100}")
    print(f"{'Method':<20} {'η_max FDR sig':>15} {'K_resid FDR sig':>17} {'K_resid neg':>13} {'Mean R²':>10}")
    print("-" * 80)
    for m in METHODS:
        s = output["aggregation_methods"][m]["summary"]
        print(f"  {m:<18} {s['eta_max_fdr_sig']:>15} {s['keff_resid_fdr_sig']:>17} "
              f"{s['keff_resid_negative']:>13} {s['mean_R2_resid']:>10.4f}")

    # Compare bayesian vs majority eta_max significance
    maj_conds = output["aggregation_methods"]["majority_vote"]["conditions"]
    bay_conds = output["aggregation_methods"]["bayesian"]["conditions"]
    maj_eta_sig = sum(1 for ck, v in maj_conds.items()
                      if not v.get("skipped") and v.get("eta_max_fdr_p", 1) < 0.05)
    bay_eta_sig = sum(1 for ck, v in bay_conds.items()
                      if not v.get("skipped") and v.get("eta_max_fdr_p", 1) < 0.05)
    n_maj = sum(1 for v in maj_conds.values() if not v.get("skipped"))
    n_bay = sum(1 for v in bay_conds.values() if not v.get("skipped"))

    output["comparison"] = {
        "majority_eta_max_fdr_sig": f"{maj_eta_sig}/{n_maj}",
        "bayesian_eta_max_fdr_sig": f"{bay_eta_sig}/{n_bay}",
        "bayesian_reduces_weakest_link": bay_eta_sig < maj_eta_sig,
    }
    print(f"\nBayesian vs Majority η_max FDR sig: {bay_eta_sig}/{n_bay} vs {maj_eta_sig}/{n_maj}")
    print(f"Bayesian reduces weakest-link effect: {bay_eta_sig < maj_eta_sig}")

    out_dir = Path("/root/cert_manip_resist_eval/artifacts/results/plan001")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "aggregation_regression_15model.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2, default=_json_default, ensure_ascii=False)
    print(f"\nSaved: {out_path}")


if __name__ == "__main__":
    main()
