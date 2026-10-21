#!/usr/bin/env python3
"""Aggregation regression: log-log OLS for 4 aggregation methods.

For each of 12 conditions (2 datasets x 6 attacks) x 4 aggregation methods, runs:
    log(ASR + eps) ~ log(K_eff) + log(eta_max + eps)
with BH FDR correction per method.

Output:
  - artifacts/results/plan001/aggregation_regression_15model_loglog.json
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
from statsmodels.stats.multitest import multipletests

from src.utils import setup_logging
from src.unified_data_loader import (
    ALL_MODELS, DATASETS, ATTACKS,
    load_all_scores, load_pairs, load_mi_data,
    compute_clean_accuracy, _is_valid_score,
)

logger = setup_logging("aggregation_loglog")

EPS = 1e-6
FDR_ALPHA = 0.05
METHODS = ["majority_vote", "weighted_vote", "threshold_unanimous", "bayesian"]


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


def majority_vote(votes):
    counts = {"A": 0, "B": 0, "tie": 0}
    for v in votes:
        counts[v] = counts.get(v, 0) + 1
    mc = max(counts.values())
    winners = [k for k, c in counts.items() if c == mc]
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


def compute_panel_asr_all_methods(jids, clean, attacked, pairs, accs):
    n = min(len(pairs), *(len(clean[j]) for j in jids),
            *(len(attacked[j]) for j in jids))

    mv_flips = mv_correct = 0
    wv_flips = wv_correct = 0
    th_flips = th_denom = 0
    by_flips = by_correct = 0

    for i in range(n):
        if not all(_is_valid_score(clean[j][i]) for j in jids):
            continue
        if not all(_is_valid_score(attacked[j][i]) for j in jids):
            continue
        gt = pairs[i]["ground_truth_winner"]

        c_votes = [clean[j][i]["winner"] for j in jids]
        a_votes = [attacked[j][i]["winner"] for j in jids]

        # --- Majority Vote ---
        cv = majority_vote(c_votes)
        if cv == gt:
            mv_correct += 1
            if majority_vote(a_votes) != gt:
                mv_flips += 1

        # --- Weighted Vote ---
        w_a_c = sum(a for v, a in zip(c_votes, accs) if v == "A")
        w_b_c = sum(a for v, a in zip(c_votes, accs) if v == "B")
        cv_w = "A" if w_a_c > w_b_c else ("B" if w_b_c > w_a_c else "tie")
        if cv_w == gt:
            wv_correct += 1
            w_a_a = sum(a for v, a in zip(a_votes, accs) if v == "A")
            w_b_a = sum(a for v, a in zip(a_votes, accs) if v == "B")
            av_w = "A" if w_a_a > w_b_a else ("B" if w_b_a > w_a_a else "tie")
            if av_w != gt:
                wv_flips += 1

        # --- Threshold (Unanimous) ---
        if len(set(c_votes)) == 1 and c_votes[0] == gt:
            th_denom += 1
            if len(set(a_votes)) != 1 or a_votes[0] != gt:
                th_flips += 1

        # --- Bayesian ---
        log_odds_c = 0.0
        for v, ac in zip(c_votes, accs):
            a = max(min(ac, 0.999), 0.001)
            if v == gt:
                log_odds_c += np.log(a / (1 - a))
            else:
                log_odds_c += np.log((1 - a) / a)
        if log_odds_c > 0:
            by_correct += 1
            log_odds_a = 0.0
            for v, ac in zip(a_votes, accs):
                a = max(min(ac, 0.999), 0.001)
                if v == gt:
                    log_odds_a += np.log(a / (1 - a))
                else:
                    log_odds_a += np.log((1 - a) / a)
            if log_odds_a <= 0:
                by_flips += 1

    return {
        "majority_vote": (mv_flips / max(mv_correct, 1), mv_correct),
        "weighted_vote": (wv_flips / max(wv_correct, 1), wv_correct),
        "threshold_unanimous": (th_flips / max(th_denom, 1), th_denom),
        "bayesian": (by_flips / max(by_correct, 1), by_correct),
    }


def main():
    logger.info("=" * 60)
    logger.info("Aggregation Regression (log-log OLS, 4 methods)")
    logger.info("=" * 60)

    mi_data = load_mi_data()
    pairs = load_pairs()
    clean, attacked = load_all_scores()

    clean_acc = compute_clean_accuracy(clean, pairs)
    logger.info(f"Clean accuracy: {len(clean_acc)} (model, dataset) pairs")

    ind_asr = {}
    for ds in DATASETS:
        for atk in ATTACKS:
            for mid in ALL_MODELS:
                if mid in clean[ds] and mid in attacked[ds][atk]:
                    ind_asr[(ds, atk, mid)] = compute_individual_asr(
                        clean[ds][mid], attacked[ds][atk][mid], pairs[ds]
                    )
    logger.info(f"Individual ASR: {len(ind_asr)} values")

    all_combos = list(itertools.combinations(range(len(ALL_MODELS)), 3))
    logger.info(f"Total panels: {len(all_combos)}")

    method_results = {
        m: {"raw_eta_ps": [], "raw_keff_ps": [], "valid_keys": [], "conditions": {}}
        for m in METHODS
    }

    for ds in DATASETS:
        keff_data = mi_data["keff_per_panel"].get(ds, {})
        for atk in ATTACKS:
            cond = f"{ds}x{atk}"
            logger.info(f"\n--- {cond} ---")

            method_panels = {m: {"asrs": [], "keffs": [], "etas": []} for m in METHODS}
            skipped = 0

            for combo in all_combos:
                jids = [ALL_MODELS[i] for i in combo]
                if not all((ds, atk, j) in ind_asr for j in jids):
                    skipped += 1
                    continue
                pk = "|".join(jids)
                if pk not in keff_data:
                    skipped += 1
                    continue

                keff = keff_data[pk]["keff"]
                eta_max = max(ind_asr[(ds, atk, j)] for j in jids)

                cs = {j: clean[ds][j] for j in jids}
                ats = {j: attacked[ds][atk][j] for j in jids}
                panel_accs = [clean_acc.get((j, ds), 0.5) for j in jids]

                results = compute_panel_asr_all_methods(
                    jids, cs, ats, pairs[ds], panel_accs
                )

                for m in METHODS:
                    asr, denom = results[m]
                    if m == "threshold_unanimous" and denom == 0:
                        continue
                    method_panels[m]["asrs"].append(asr)
                    method_panels[m]["keffs"].append(keff)
                    method_panels[m]["etas"].append(eta_max)

            logger.info(
                f"  majority={len(method_panels['majority_vote']['asrs'])}, "
                f"threshold={len(method_panels['threshold_unanimous']['asrs'])}, "
                f"skipped={skipped}"
            )

            for m in METHODS:
                mp = method_panels[m]
                n_panels = len(mp["asrs"])

                if n_panels < 10:
                    logger.warning(f"  {m}: {n_panels} panels, skipping")
                    continue

                p_asrs = np.array(mp["asrs"])
                p_keffs = np.array(mp["keffs"])
                p_etas = np.array(mp["etas"])

                if np.std(p_asrs) < 1e-10:
                    logger.warning(f"  {m}: constant ASR ({p_asrs[0]:.4f}), skipping")
                    continue

                log_keff = np.log(p_keffs)
                log_eta = np.log(p_etas + EPS)
                y = np.log(p_asrs + EPS)

                X = np.column_stack([log_keff, log_eta])
                Xc = sm.add_constant(X)
                fit = sm.OLS(y, Xc).fit()

                keff_p = float(fit.pvalues[1])
                eta_p = float(fit.pvalues[2])

                sd_y = np.std(y)
                keff_std_beta = float(fit.params[1] * np.std(log_keff) / sd_y)
                eta_std_beta = float(fit.params[2] * np.std(log_eta) / sd_y)

                cd = {
                    "condition": cond,
                    "method": m,
                    "dataset": ds,
                    "attack": atk,
                    "n_panels": n_panels,
                    "eta_std_beta": eta_std_beta,
                    "eta_raw_p": eta_p,
                    "keff_std_beta": keff_std_beta,
                    "keff_raw_p": keff_p,
                    "R2": float(fit.rsquared),
                }

                method_results[m]["conditions"][cond] = cd
                method_results[m]["raw_eta_ps"].append(eta_p)
                method_results[m]["raw_keff_ps"].append(keff_p)
                method_results[m]["valid_keys"].append(cond)

                logger.info(
                    f"  {m}: beta_eta={eta_std_beta:+.4f} (p={eta_p:.2e}), "
                    f"beta_K={keff_std_beta:+.4f} (p={keff_p:.2e}), R2={fit.rsquared:.4f}"
                )

    # FDR correction per method
    for m in METHODS:
        mr = method_results[m]
        if not mr["valid_keys"]:
            continue
        _, fdr_eta, _, _ = multipletests(mr["raw_eta_ps"], method="fdr_bh")
        _, fdr_keff, _, _ = multipletests(mr["raw_keff_ps"], method="fdr_bh")
        for i, ck in enumerate(mr["valid_keys"]):
            mr["conditions"][ck]["eta_fdr_p"] = float(fdr_eta[i])
            mr["conditions"][ck]["keff_fdr_p"] = float(fdr_keff[i])

    # ── Summary table ──────────────────────────────────────────────
    logger.info("\n" + "=" * 100)
    logger.info("SUMMARY TABLE")
    logger.info("=" * 100)
    logger.info(
        f"{'Method':<24} {'eta_FDR_sig':>12} {'K_FDR_sig':>12} "
        f"{'K_pos':>6} {'K_neg':>6} {'Mean_R2':>8}"
    )

    for m in METHODS:
        mr = method_results[m]
        vk = mr["valid_keys"]
        n_eta = sum(1 for ck in vk if mr["conditions"][ck].get("eta_fdr_p", 1) < FDR_ALPHA)
        n_keff = sum(1 for ck in vk if mr["conditions"][ck].get("keff_fdr_p", 1) < FDR_ALPHA)
        n_pos = sum(1 for ck in vk
                    if mr["conditions"][ck].get("keff_fdr_p", 1) < FDR_ALPHA
                    and mr["conditions"][ck]["keff_std_beta"] > 0)
        n_neg = sum(1 for ck in vk
                    if mr["conditions"][ck].get("keff_fdr_p", 1) < FDR_ALPHA
                    and mr["conditions"][ck]["keff_std_beta"] < 0)
        nt = len(vk)
        mean_r2 = float(np.mean([mr["conditions"][ck]["R2"] for ck in vk])) if vk else 0
        logger.info(
            f"{m:<24} {n_eta:>5}/{nt:<5} {n_keff:>5}/{nt:<5} "
            f"{n_pos:>6} {n_neg:>6} {mean_r2:>8.4f}"
        )

    # ── Detailed table ─────────────────────────────────────────────
    logger.info("\n" + "=" * 150)
    logger.info("DETAILED TABLE")
    logger.info("=" * 150)
    logger.info(
        f"{'Condition':<32} {'Method':<24} {'eta_beta':>8} {'eta_raw_p':>10} "
        f"{'eta_fdr_p':>10} {'K_beta':>8} {'K_raw_p':>10} {'K_fdr_p':>10} "
        f"{'R2':>6} {'n':>5}"
    )

    for m in METHODS:
        mr = method_results[m]
        for ck in mr["valid_keys"]:
            cd = mr["conditions"][ck]
            logger.info(
                f"{cd['condition']:<32} {cd['method']:<24} "
                f"{cd['eta_std_beta']:>+8.4f} {cd['eta_raw_p']:>10.2e} "
                f"{cd.get('eta_fdr_p', float('nan')):>10.2e} "
                f"{cd['keff_std_beta']:>+8.4f} {cd['keff_raw_p']:>10.2e} "
                f"{cd.get('keff_fdr_p', float('nan')):>10.2e} "
                f"{cd['R2']:>6.4f} {cd['n_panels']:>5}"
            )

    # ── Sanity check ───────────────────────────────────────────────
    logger.info("\n" + "=" * 60)
    logger.info("SANITY CHECK: majority_vote vs dominance analysis")
    logger.info("=" * 60)
    mr_mv = method_results["majority_vote"]
    vk = mr_mv["valid_keys"]
    n_eta = sum(1 for ck in vk if mr_mv["conditions"][ck].get("eta_fdr_p", 1) < FDR_ALPHA)
    n_keff = sum(1 for ck in vk if mr_mv["conditions"][ck].get("keff_fdr_p", 1) < FDR_ALPHA)
    n_pos = sum(1 for ck in vk
                if mr_mv["conditions"][ck].get("keff_fdr_p", 1) < FDR_ALPHA
                and mr_mv["conditions"][ck]["keff_std_beta"] > 0)
    n_neg = sum(1 for ck in vk
                if mr_mv["conditions"][ck].get("keff_fdr_p", 1) < FDR_ALPHA
                and mr_mv["conditions"][ck]["keff_std_beta"] < 0)

    logger.info(f"  eta_max FDR sig: {n_eta}/12 (expected 11/12)")
    logger.info(f"  K_eff FDR sig:   {n_keff}/12 (expected 8/12)")
    logger.info(f"    positive: {n_pos} (expected 7)")
    logger.info(f"    negative: {n_neg} (expected 1)")

    passed = n_eta == 11 and n_keff == 8 and n_pos == 7 and n_neg == 1
    if passed:
        logger.info("  PASSED")
    else:
        logger.warning("  FAILED")
        for ck in vk:
            cd = mr_mv["conditions"][ck]
            e_s = "sig" if cd.get("eta_fdr_p", 1) < FDR_ALPHA else "ns"
            k_s = "sig" if cd.get("keff_fdr_p", 1) < FDR_ALPHA else "ns"
            logger.info(
                f"    {ck}: eta={e_s} (fdr={cd.get('eta_fdr_p', float('nan')):.4e}), "
                f"K={k_s} (fdr={cd.get('keff_fdr_p', float('nan')):.4e}, "
                f"beta={cd['keff_std_beta']:+.4f})"
            )

    # ── Save JSON ──────────────────────────────────────────────────
    detail_rows = []
    for m in METHODS:
        mr = method_results[m]
        for ck in mr["valid_keys"]:
            detail_rows.append(mr["conditions"][ck])

    summary = {}
    for m in METHODS:
        mr = method_results[m]
        vk = mr["valid_keys"]
        n_eta = sum(1 for ck in vk if mr["conditions"][ck].get("eta_fdr_p", 1) < FDR_ALPHA)
        n_keff = sum(1 for ck in vk if mr["conditions"][ck].get("keff_fdr_p", 1) < FDR_ALPHA)
        n_pos = sum(1 for ck in vk
                    if mr["conditions"][ck].get("keff_fdr_p", 1) < FDR_ALPHA
                    and mr["conditions"][ck]["keff_std_beta"] > 0)
        n_neg = sum(1 for ck in vk
                    if mr["conditions"][ck].get("keff_fdr_p", 1) < FDR_ALPHA
                    and mr["conditions"][ck]["keff_std_beta"] < 0)
        nt = len(vk)
        mean_r2 = float(np.mean([mr["conditions"][ck]["R2"] for ck in vk])) if vk else 0
        summary[m] = {
            "eta_fdr_sig": n_eta,
            "keff_fdr_sig": n_keff,
            "keff_sig_positive": n_pos,
            "keff_sig_negative": n_neg,
            "n_conditions": nt,
            "mean_R2": mean_r2,
        }

    output = {
        "analysis": "aggregation_regression_loglog_15model",
        "n_models": len(ALL_MODELS),
        "models": ALL_MODELS,
        "methods": METHODS,
        "fdr_alpha": FDR_ALPHA,
        "eps": EPS,
        "summary": summary,
        "detail": detail_rows,
    }

    out_dir = Path("/root/cert_manip_resist_eval/artifacts/results/plan001")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "aggregation_regression_15model_loglog.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2, default=_json_default, ensure_ascii=False)
    logger.info(f"\nSaved: {out_path}")


if __name__ == "__main__":
    main()
