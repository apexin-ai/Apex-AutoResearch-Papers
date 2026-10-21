#!/usr/bin/env python3
"""Alternative diversity metrics + practical effect size analysis.

Part A: Q-statistic, disagreement rate, κ-based diversity → log-log regressions
Part B: Canonical OLS effect sizes, practical Δ_ASR (IQR), clustered SE CI
"""

import sys
sys.path.insert(0, "/root/cert_manip_resist_eval")

import json
import itertools
import numpy as np
import statsmodels.api as sm
from pathlib import Path
from scipy import stats as scipy_stats
from scipy.stats import t as t_dist
from statsmodels.stats.multitest import multipletests

from src.unified_data_loader import (
    ALL_MODELS, DATASETS, ATTACKS,
    load_all_scores, load_pairs, load_mi_data,
    _is_valid_score,
)

EPS = 1e-6
FDR_ALPHA = 0.05
N_MODELS = 15


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


def compute_panel_asr(jids, clean_ds, attacked_ds_atk, pairs):
    n = min(len(pairs), *(len(clean_ds[j]) for j in jids),
            *(len(attacked_ds_atk[j]) for j in jids))
    n_flips = n_correct = 0
    for i in range(n):
        if not all(_is_valid_score(clean_ds[j][i]) for j in jids):
            continue
        if not all(_is_valid_score(attacked_ds_atk[j][i]) for j in jids):
            continue
        gt = pairs[i]["ground_truth_winner"]
        cv = majority_vote([clean_ds[j][i]["winner"] for j in jids])
        if cv != gt:
            continue
        n_correct += 1
        av = majority_vote([attacked_ds_atk[j][i]["winner"] for j in jids])
        if av != gt:
            n_flips += 1
    return n_flips / max(n_correct, 1)


# ── Pairwise diversity metrics (computed on clean data) ──

def pairwise_q(clean_i, clean_j, pairs):
    n = min(len(clean_i), len(clean_j), len(pairs))
    a = b = c = d = 0
    for idx in range(n):
        if not _is_valid_score(clean_i[idx]) or not _is_valid_score(clean_j[idx]):
            continue
        gt = pairs[idx]["ground_truth_winner"]
        ci = clean_i[idx]["winner"] == gt
        cj = clean_j[idx]["winner"] == gt
        if ci and cj:
            a += 1
        elif ci and not cj:
            b += 1
        elif not ci and cj:
            c += 1
        else:
            d += 1
    denom = a * d + b * c
    if denom == 0:
        return 1.0 if (b == 0 and c == 0) else 0.0
    return (a * d - b * c) / denom


def pairwise_disagreement(clean_i, clean_j):
    n = min(len(clean_i), len(clean_j))
    n_valid = nd = 0
    for idx in range(n):
        if not _is_valid_score(clean_i[idx]) or not _is_valid_score(clean_j[idx]):
            continue
        n_valid += 1
        if clean_i[idx]["winner"] != clean_j[idx]["winner"]:
            nd += 1
    return nd / max(n_valid, 1)


def pairwise_kappa(clean_i, clean_j):
    n = min(len(clean_i), len(clean_j))
    categories = ["A", "B", "tie"]
    n_valid = n_agree = 0
    cnt_i = {c: 0 for c in categories}
    cnt_j = {c: 0 for c in categories}
    for idx in range(n):
        if not _is_valid_score(clean_i[idx]) or not _is_valid_score(clean_j[idx]):
            continue
        n_valid += 1
        vi = clean_i[idx]["winner"]
        vj = clean_j[idx]["winner"]
        cnt_i[vi] += 1
        cnt_j[vj] += 1
        if vi == vj:
            n_agree += 1
    p_o = n_agree / max(n_valid, 1)
    p_e = sum(cnt_i[c] * cnt_j[c] for c in categories) / max(n_valid * n_valid, 1)
    if p_e >= 1.0:
        return 0.0
    return (p_o - p_e) / (1 - p_e)


def panel_diversity(jids, clean_ds, pairs):
    idx_pairs = [(0, 1), (0, 2), (1, 2)]
    qs, ds, ks = [], [], []
    for a, b in idx_pairs:
        qs.append(pairwise_q(clean_ds[jids[a]], clean_ds[jids[b]], pairs))
        ds.append(pairwise_disagreement(clean_ds[jids[a]], clean_ds[jids[b]]))
        ks.append(pairwise_kappa(clean_ds[jids[a]], clean_ds[jids[b]]))
    return {
        "Q_div": 1 - np.mean(qs),
        "D": np.mean(ds),
        "kappa_div": 1 - np.mean(ks),
    }


def std_beta(x_col, y, raw_b):
    return raw_b * np.std(x_col) / np.std(y)


def main():
    print("Loading data...")
    clean, attacked = load_all_scores()
    pairs = load_pairs()
    mi_data = load_mi_data()

    models = mi_data["models"]
    assert len(models) == N_MODELS
    all_combos = list(itertools.combinations(range(N_MODELS), 3))
    assert len(all_combos) == 455
    print(f"Models: {N_MODELS}, Panels: {len(all_combos)}")

    # ── Pre-compute individual ASR ──
    print("Pre-computing individual ASR...")
    ind_asr = {}
    for ds in DATASETS:
        for atk in ATTACKS:
            for mid in models:
                if mid in clean[ds] and mid in attacked[ds][atk]:
                    ind_asr[(ds, atk, mid)] = compute_individual_asr(
                        clean[ds][mid], attacked[ds][atk][mid], pairs[ds]
                    )

    # ── Pre-compute panel diversity metrics (per dataset, attack-independent) ──
    print("Pre-computing panel diversity metrics...")
    pdiv = {}
    for combo in all_combos:
        jids = [models[i] for i in combo]
        pk = "|".join(jids)
        for ds in DATASETS:
            if all(j in clean[ds] for j in jids):
                pdiv[(pk, ds)] = panel_diversity(jids, clean[ds], pairs[ds])

    # Sanity checks
    for ds in DATASETS:
        vals = {m: [] for m in ["Q_div", "D", "kappa_div"]}
        for combo in all_combos:
            pk = "|".join([models[i] for i in combo])
            if (pk, ds) in pdiv:
                for m in vals:
                    vals[m].append(pdiv[(pk, ds)][m])
        for m, v in vals.items():
            print(f"  {ds} {m}: [{min(v):.4f}, {max(v):.4f}], mean={np.mean(v):.4f}")

    # ── Pre-compute panel ASR (all 455 × 12 conditions) ──
    print("Pre-computing panel ASR (455 × 12 conditions)...")
    panel_asr_cache = {}
    for ds in DATASETS:
        for atk in ATTACKS:
            for combo in all_combos:
                jids = [models[i] for i in combo]
                pk = "|".join(jids)
                if (all(j in clean[ds] for j in jids) and
                        all(j in attacked[ds][atk] for j in jids)):
                    panel_asr_cache[(pk, ds, atk)] = compute_panel_asr(
                        jids, clean[ds], attacked[ds][atk], pairs[ds]
                    )
    print(f"  Cached {len(panel_asr_cache)} panel ASR values")

    # ═══════════════════════════════════════════════════════════════════
    # Part A: Alternative Diversity Metrics
    # ═══════════════════════════════════════════════════════════════════
    print("\n=== Part A: Alternative Diversity Metrics ===")

    metric_specs = {
        "Q_statistic": "Q_div",
        "disagreement_rate": "D",
        "kappa_diversity": "kappa_div",
    }

    alt_results = {}

    for metric_name, div_key in metric_specs.items():
        per_cond = {}
        cond_keys_ordered = []

        for ds in DATASETS:
            for atk in ATTACKS:
                ck = f"{ds}x{atk}"
                cond_keys_ordered.append(ck)

                asrs, divs, etas = [], [], []
                for combo in all_combos:
                    jids = [models[i] for i in combo]
                    pk = "|".join(jids)

                    if not all((ds, atk, j) in ind_asr for j in jids):
                        continue
                    if (pk, ds) not in pdiv:
                        continue
                    if (pk, ds, atk) not in panel_asr_cache:
                        continue

                    asrs.append(panel_asr_cache[(pk, ds, atk)])
                    divs.append(pdiv[(pk, ds)][div_key])
                    etas.append(max(ind_asr[(ds, atk, j)] for j in jids))

                asrs = np.array(asrs)
                divs = np.array(divs)
                etas = np.array(etas)

                log_y = np.log(asrs + EPS)
                log_d = np.log(divs + EPS)
                log_e = np.log(etas + EPS)

                X = sm.add_constant(np.column_stack([log_d, log_e]))
                fit = sm.OLS(log_y, X).fit()

                per_cond[ck] = {
                    "n": len(asrs),
                    "beta_D": float(fit.params[1]),
                    "beta_eta": float(fit.params[2]),
                    "std_beta_D": float(std_beta(log_d, log_y, fit.params[1])),
                    "std_beta_eta": float(std_beta(log_e, log_y, fit.params[2])),
                    "p_D": float(fit.pvalues[1]),
                    "p_eta": float(fit.pvalues[2]),
                    "R2": float(fit.rsquared),
                }

        # FDR correction (per predictor, across 12 conditions)
        p_D_arr = [per_cond[ck]["p_D"] for ck in cond_keys_ordered]
        p_eta_arr = [per_cond[ck]["p_eta"] for ck in cond_keys_ordered]
        _, fdr_D, _, _ = multipletests(p_D_arr, method="fdr_bh")
        _, fdr_eta, _, _ = multipletests(p_eta_arr, method="fdr_bh")

        for i, ck in enumerate(cond_keys_ordered):
            per_cond[ck]["fdr_p_D"] = float(fdr_D[i])
            per_cond[ck]["fdr_p_eta"] = float(fdr_eta[i])

        eta_sig = sum(1 for p in fdr_eta if p < FDR_ALPHA)
        D_sig = sum(1 for p in fdr_D if p < FDR_ALPHA)
        D_pos = sum(1 for i, ck in enumerate(cond_keys_ordered)
                    if fdr_D[i] < FDR_ALPHA and per_cond[ck]["beta_D"] > 0)
        D_neg = D_sig - D_pos

        # Correlation with K_eff (per dataset)
        corr_p, corr_s = [], []
        corr_p_ds, corr_s_ds = {}, {}
        for ds in DATASETS:
            keffs, divvals = [], []
            for combo in all_combos:
                pk = "|".join([models[i] for i in combo])
                if (pk, ds) in pdiv and pk in mi_data["keff_per_panel"][ds]:
                    keffs.append(mi_data["keff_per_panel"][ds][pk]["keff"])
                    divvals.append(pdiv[(pk, ds)][div_key])
            rp, _ = scipy_stats.pearsonr(keffs, divvals)
            rs, _ = scipy_stats.spearmanr(keffs, divvals)
            corr_p.append(rp)
            corr_s.append(rs)
            corr_p_ds[ds] = float(rp)
            corr_s_ds[ds] = float(rs)

        alt_results[metric_name] = {
            "per_condition": per_cond,
            "summary": {
                "eta_fdr_sig": f"{eta_sig}/12",
                "D_fdr_sig": f"{D_sig}/12",
                "D_sig_pos": D_pos,
                "D_sig_neg": D_neg,
            },
            "corr_with_keff": {
                "pearson": float(np.mean(corr_p)),
                "spearman": float(np.mean(corr_s)),
                "pearson_per_dataset": corr_p_ds,
                "spearman_per_dataset": corr_s_ds,
            },
        }

        print(f"  {metric_name}: η_max {eta_sig}/12, D {D_sig}/12 "
              f"({D_pos}+/{D_neg}-), r(K_eff)={np.mean(corr_p):.3f}")

    # ═══════════════════════════════════════════════════════════════════
    # Part B: Effect Sizes
    # ═══════════════════════════════════════════════════════════════════
    print("\n=== Part B: Effect Sizes ===")

    # B1: Canonical OLS standardized betas
    print("B1: Canonical OLS standardized betas...")
    canonical_ols = {}
    eta_std_all, keff_std_all = [], []
    cond_keys_ordered = []

    # Also cache regression fits for B2
    regression_fits = {}

    for ds in DATASETS:
        for atk in ATTACKS:
            ck = f"{ds}x{atk}"
            cond_keys_ordered.append(ck)

            asrs, keffs, etas = [], [], []
            judge_ids_list = []
            for combo in all_combos:
                jids = [models[i] for i in combo]
                pk = "|".join(jids)
                if not all((ds, atk, j) in ind_asr for j in jids):
                    continue
                if pk not in mi_data["keff_per_panel"][ds]:
                    continue
                if (pk, ds, atk) not in panel_asr_cache:
                    continue

                asrs.append(panel_asr_cache[(pk, ds, atk)])
                keffs.append(mi_data["keff_per_panel"][ds][pk]["keff"])
                etas.append(max(ind_asr[(ds, atk, j)] for j in jids))
                judge_ids_list.append(jids)

            asrs = np.array(asrs)
            keffs = np.array(keffs)
            etas = np.array(etas)

            log_y = np.log(asrs + EPS)
            log_k = np.log(keffs)
            log_e = np.log(etas + EPS)

            X = sm.add_constant(np.column_stack([log_k, log_e]))
            fit = sm.OLS(log_y, X).fit()

            sb_k = std_beta(log_k, log_y, fit.params[1])
            sb_e = std_beta(log_e, log_y, fit.params[2])

            canonical_ols[ck] = {
                "beta_keff": float(fit.params[1]),
                "beta_eta": float(fit.params[2]),
                "std_beta_keff": float(sb_k),
                "std_beta_eta": float(sb_e),
                "p_keff": float(fit.pvalues[1]),
                "p_eta": float(fit.pvalues[2]),
                "R2": float(fit.rsquared),
            }
            eta_std_all.append(sb_e)
            keff_std_all.append(sb_k)

            regression_fits[ck] = {
                "fit": fit,
                "log_k": log_k,
                "log_e": log_e,
                "keffs": keffs,
                "etas": etas,
                "judge_ids_list": judge_ids_list,
            }

    print(f"  η_max std β: {np.mean(eta_std_all):.3f} ± {np.std(eta_std_all):.3f}")
    print(f"  K_eff std β: {np.mean(keff_std_all):.3f} ± {np.std(keff_std_all):.3f}")

    # B2: Practical Δ_ASR (IQR method)
    print("B2: Practical Δ_ASR (IQR)...")
    practical_delta = {}
    delta_asrs = []

    for ck in cond_keys_ordered:
        rf = regression_fits[ck]
        fit = rf["fit"]
        log_k = rf["log_k"]
        log_e = rf["log_e"]

        eta_med = np.median(log_e)
        k25 = np.percentile(log_k, 25)
        k75 = np.percentile(log_k, 75)

        pred_25 = fit.params[0] + fit.params[1] * k25 + fit.params[2] * eta_med
        pred_75 = fit.params[0] + fit.params[1] * k75 + fit.params[2] * eta_med
        d_asr = float(np.exp(pred_75) - np.exp(pred_25))

        practical_delta[ck] = {
            "keff_25th": float(np.exp(k25)),
            "keff_75th": float(np.exp(k75)),
            "eta_median": float(np.exp(eta_med)),
            "pred_asr_at_k25": float(np.exp(pred_25)),
            "pred_asr_at_k75": float(np.exp(pred_75)),
            "delta_asr": d_asr,
        }
        delta_asrs.append(d_asr)

    print(f"  Mean Δ_ASR: {np.mean(delta_asrs):.4f} ± {np.std(delta_asrs):.4f}")

    # B3: Clustered SE CI
    print("B3: Clustered SE confidence intervals...")
    cl_path = Path("/root/cert_manip_resist_eval/artifacts/results/plan001/clustered_se_analysis.json")
    with open(cl_path) as f:
        cl_data = json.load(f)

    clustered_ci = {}
    keff_ci_zero = 0
    eta_ci_zero = 0

    for cond_key, cond_val in cl_data["conditions"].items():
        cl = cond_val["clustered"]
        n_panels = cond_val["n_panels"]
        df = n_panels - 3
        tc = t_dist.ppf(0.975, df)

        beta_k = cl["params"][1]
        se_k = cl["max_clustered_se"][1]
        ci_k = [beta_k - tc * se_k, beta_k + tc * se_k]

        beta_e = cl["params"][2]
        se_e = cl["max_clustered_se"][2]
        ci_e = [beta_e - tc * se_e, beta_e + tc * se_e]

        k_has_zero = ci_k[0] <= 0 <= ci_k[1]
        e_has_zero = ci_e[0] <= 0 <= ci_e[1]
        if k_has_zero:
            keff_ci_zero += 1
        if e_has_zero:
            eta_ci_zero += 1

        clustered_ci[cond_key] = {
            "keff_beta": float(beta_k),
            "keff_clustered_se": float(se_k),
            "keff_ci_95": [float(ci_k[0]), float(ci_k[1])],
            "keff_ci_contains_zero": bool(k_has_zero),
            "eta_beta": float(beta_e),
            "eta_clustered_se": float(se_e),
            "eta_ci_95": [float(ci_e[0]), float(ci_e[1])],
            "eta_ci_contains_zero": bool(e_has_zero),
        }

    print(f"  K_eff CI contains 0: {keff_ci_zero}/12")
    print(f"  η_max CI contains 0: {eta_ci_zero}/12")

    # ═══════════════════════════════════════════════════════════════════
    # Assemble & save
    # ═══════════════════════════════════════════════════════════════════
    output = {
        "alternative_metrics": alt_results,
        "effect_size": {
            "canonical_ols": {
                "per_condition": canonical_ols,
                "eta_std_beta": {
                    "mean": float(np.mean(eta_std_all)),
                    "sd": float(np.std(eta_std_all)),
                },
                "keff_std_beta": {
                    "mean": float(np.mean(keff_std_all)),
                    "sd": float(np.std(keff_std_all)),
                },
            },
            "practical_delta_asr": {
                "per_condition": practical_delta,
                "mean": float(np.mean(delta_asrs)),
                "sd": float(np.std(delta_asrs)),
            },
            "clustered_se_ci": {
                "per_condition": clustered_ci,
                "keff_ci_contains_zero": f"{keff_ci_zero}/12",
                "eta_ci_contains_zero": f"{eta_ci_zero}/12",
            },
        },
    }

    out_path = Path("/root/cert_manip_resist_eval/artifacts/results/plan001/alt_diversity_effect_size.json")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2, default=_json_default, ensure_ascii=False)

    print(f"\nSaved: {out_path}")

    # Final summary
    print(f"\n{'='*70}")
    print("FINAL SUMMARY")
    print(f"{'='*70}")
    print("\nPart A: Alternative Diversity Metrics")
    for mn, r in alt_results.items():
        s = r["summary"]
        c = r["corr_with_keff"]
        print(f"  {mn:25s}: η {s['eta_fdr_sig']:>5} | D {s['D_fdr_sig']:>5} "
              f"({s['D_sig_pos']}+/{s['D_sig_neg']}-) | "
              f"r(K_eff)={c['pearson']:.3f}, ρ={c['spearman']:.3f}")

    print(f"\nPart B: Effect Sizes")
    print(f"  η_max std β: {np.mean(eta_std_all):.3f} ± {np.std(eta_std_all):.3f}")
    print(f"  K_eff std β: {np.mean(keff_std_all):.3f} ± {np.std(keff_std_all):.3f}")
    print(f"  Practical Δ_ASR: {np.mean(delta_asrs):.4f} ± {np.std(delta_asrs):.4f}")
    print(f"  Clustered SE: K_eff 0∈CI {keff_ci_zero}/12, η_max 0∈CI {eta_ci_zero}/12")


if __name__ == "__main__":
    main()
