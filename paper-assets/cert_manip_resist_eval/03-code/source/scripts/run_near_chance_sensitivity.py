#!/usr/bin/env python3
"""Near-chance model sensitivity analysis.

Reviewer concern: qwen2.5-14b (MMLU=0.253) and qwen2.5-72b (MMLU=0.333) are
near random chance (0.25 for 4-choice). The diversity-vulnerability positive
association might be trivially driven by "panels containing random judges are
more vulnerable." This script removes all panels containing either model and
re-runs OLS, WCB, and fractional logit regressions for K=3,5,7.

Panel data is computed once per condition; full vs filtered share the same
ASR computation with a mask-based split.
"""

import os
os.environ["HF_HOME"] = "/root/autodl-tmp/.hf_cache"
import sys
sys.path.insert(0, "/root/cert_manip_resist_eval")

import json
import time
import argparse
import itertools
import warnings
import numpy as np
import statsmodels.api as sm
from pathlib import Path
from statsmodels.genmod.families import Binomial
from statsmodels.stats.multitest import multipletests

warnings.filterwarnings("ignore")

from src.unified_data_loader import (
    ALL_MODELS, DATASETS, ATTACKS,
    load_all_scores, load_pairs, load_mi_data,
    _is_valid_score,
)

EPS = 1e-6
FDR_ALPHA = 0.05
NEAR_CHANCE = {"qwen2.5-72b", "qwen2.5-14b"}
EXCLUDE_IDX = frozenset(i for i, m in enumerate(ALL_MODELS) if m in NEAR_CHANCE)
N_MODELS = len(ALL_MODELS)


def _jd(o):
    if isinstance(o, np.floating):
        v = float(o)
        return None if np.isnan(v) or np.isinf(v) else v
    if isinstance(o, np.integer):
        return int(o)
    if isinstance(o, np.ndarray):
        return o.tolist()
    if isinstance(o, np.bool_):
        return bool(o)
    if isinstance(o, (set, frozenset)):
        return sorted(o)
    raise TypeError(type(o))


def majority_vote(votes):
    c = {"A": 0, "B": 0, "tie": 0}
    for v in votes:
        c[v] = c.get(v, 0) + 1
    mx = max(c.values())
    w = [k for k, v in c.items() if v == mx]
    return w[0] if len(w) == 1 else next((x for x in w if x != "tie"), "tie")


def individual_asr(cl, at, pairs):
    n = min(len(cl), len(at), len(pairs))
    flips = correct = 0
    for i in range(n):
        if not _is_valid_score(cl[i]) or not _is_valid_score(at[i]):
            continue
        gt = pairs[i]["ground_truth_winner"]
        if cl[i]["winner"] == gt:
            correct += 1
            if at[i]["winner"] != gt:
                flips += 1
    return flips / max(correct, 1)


def compute_panel_asr(jids, cl, at, pairs):
    n = min(len(pairs), *(len(cl[j]) for j in jids), *(len(at[j]) for j in jids))
    flips = correct = 0
    for i in range(n):
        if not all(_is_valid_score(cl[j][i]) for j in jids):
            continue
        if not all(_is_valid_score(at[j][i]) for j in jids):
            continue
        gt = pairs[i]["ground_truth_winner"]
        if majority_vote([cl[j][i]["winner"] for j in jids]) != gt:
            continue
        correct += 1
        if majority_vote([at[j][i]["winner"] for j in jids]) != gt:
            flips += 1
    return flips / max(correct, 1)


def mi_keff(mi, idx):
    K = len(idx)
    if K <= 1:
        return 1.0
    s = 0.0
    for i in idx:
        t = 1.0
        for j in idx:
            if i != j:
                t += np.exp(-2 * mi[i, j])
        s += t
    return s / K


def wcb_vec(y, X, cids, B, seed, tidx):
    """Vectorized wild cluster bootstrap."""
    n, p = X.shape
    uq = np.unique(cids)
    G = len(uq)
    c2i = {c: i for i, c in enumerate(uq)}
    ci = np.array([c2i[c] for c in cids])

    try:
        XtXi = np.linalg.inv(X.T @ X)
    except np.linalg.LinAlgError:
        return 1.0, G

    P = XtXi @ X.T
    b = P @ y
    r = y - X @ b
    s2 = np.sum(r**2) / (n - p)
    se = np.sqrt(max(s2 * XtXi[tidx, tidx], 1e-30))
    t0 = b[tidx] / se

    keep = [i for i in range(p) if i != tidx]
    Xr = X[:, keep]
    try:
        br = np.linalg.solve(Xr.T @ Xr, Xr.T @ y)
    except np.linalg.LinAlgError:
        return 1.0, G
    yh = Xr @ br
    er = y - yh

    rng = np.random.RandomState(seed)
    W = rng.choice([-1.0, 1.0], size=(B, G))
    Wp = W[:, ci]
    Yb = yh[None, :] + Wp * er[None, :]
    Bb = P @ Yb.T
    Rb = Yb.T - X @ Bb
    S2 = np.sum(Rb**2, axis=0) / (n - p)
    SE = np.sqrt(np.maximum(S2 * XtXi[tidx, tidx], 1e-30))
    Tb = Bb[tidx, :] / SE

    pv = (1 + np.sum(np.abs(Tb) >= np.abs(t0))) / (1 + B)
    return float(pv), G


def analyze_one(asr_arr, keff_arr, eta_arr, combos, K, B, seed):
    """Run OLS + WCB + fractional logit for one condition on one subset."""
    n = len(asr_arr)
    if n < 10:
        return {"skipped": True, "n": n}

    yl = np.log(asr_arr + EPS)
    x1 = np.log(keff_arr)
    x2 = np.log(eta_arr + EPS)
    X = sm.add_constant(np.column_stack([x1, x2]))

    # OLS
    f = sm.OLS(yl, X).fit()
    sdy = np.std(yl) or 1.0
    ols = {
        "keff_beta": float(f.params[1]),
        "keff_std_beta": float(f.params[1] * np.std(x1) / sdy),
        "keff_p": float(f.pvalues[1]),
        "eta_beta": float(f.params[2]),
        "eta_std_beta": float(f.params[2] * np.std(x2) / sdy),
        "eta_p": float(f.pvalues[2]),
        "r2": float(f.rsquared),
    }

    # WCB: K-position max-p
    kps, eps_ = [], []
    for pos in range(K):
        ci = np.array([c[pos] for c in combos])
        kp, _ = wcb_vec(yl, X, ci, B, seed, 1)
        ep, _ = wcb_vec(yl, X, ci, B, seed, 2)
        kps.append(kp)
        eps_.append(ep)
    wcb = {
        "keff_final_p": float(max(kps)),
        "eta_final_p": float(max(eps_)),
        "keff_pos_ps": kps,
        "eta_pos_ps": eps_,
    }

    # Fractional logit GLM(Binomial, logit) with clustered SE max-p
    yf = np.clip(asr_arr, EPS, 1 - EPS)
    try:
        gf = sm.GLM(yf, X, family=Binomial()).fit()
        fkp, fep = [], []
        for pos in range(K):
            ci = np.array([c[pos] for c in combos])
            uq = sorted(set(ci.tolist()))
            cm = {c: i for i, c in enumerate(uq)}
            cint = np.array([cm[c] for c in ci.tolist()])
            try:
                gc = gf.get_robustcov_results(cov_type='cluster', groups=cint)
                fkp.append(float(gc.pvalues[1]))
                fep.append(float(gc.pvalues[2]))
            except Exception:
                fkp.append(1.0)
                fep.append(1.0)
        frac = {
            "keff_coef": float(gf.params[1]),
            "keff_p": float(max(fkp)),
            "eta_coef": float(gf.params[2]),
            "eta_p": float(max(fep)),
            "pseudo_r2": float(1 - gf.deviance / gf.null_deviance)
            if gf.null_deviance > 0 else 0,
        }
    except Exception as e:
        frac = {"skipped": True, "error": str(e)}

    return {"n": n, "ols": ols, "wcb": wcb, "frac_logit": frac, "skipped": False}


def apply_fdr(results, mkey, pkey, fdrkey):
    vk = [k for k in sorted(results) if not results[k].get("skipped")
          and mkey in results[k] and not results[k][mkey].get("skipped")]
    if not vk:
        return
    raw = [results[k][mkey][pkey] for k in vk]
    _, fdr, _, _ = multipletests(raw, method="fdr_bh")
    for i, k in enumerate(vk):
        results[k][mkey][fdrkey] = float(fdr[i])


def sig_count(results, mkey, fdrkey):
    return sum(1 for k in results if not results[k].get("skipped")
               and mkey in results[k] and not results[k][mkey].get("skipped")
               and results[k][mkey].get(fdrkey, 1.0) < FDR_ALPHA)


def make_summary(results):
    vk = [k for k in sorted(results) if not results[k].get("skipped")]
    return {
        "ols_keff_sig": sig_count(results, "ols", "keff_fdr_p"),
        "ols_eta_sig": sig_count(results, "ols", "eta_fdr_p"),
        "wcb_keff_sig": sig_count(results, "wcb", "keff_fdr_p"),
        "wcb_eta_sig": sig_count(results, "wcb", "eta_fdr_p"),
        "frac_keff_sig": sig_count(results, "frac_logit", "keff_fdr_p"),
        "frac_eta_sig": sig_count(results, "frac_logit", "eta_fdr_p"),
        "mean_r2": float(np.mean([results[k]["ols"]["r2"] for k in vk])) if vk else 0,
        "mean_keff_std_beta": float(np.mean(
            [results[k]["ols"]["keff_std_beta"] for k in vk])) if vk else 0,
        "n_valid": len(vk),
    }


def do_fdr(results):
    apply_fdr(results, "ols", "keff_p", "keff_fdr_p")
    apply_fdr(results, "ols", "eta_p", "eta_fdr_p")
    apply_fdr(results, "wcb", "keff_final_p", "keff_fdr_p")
    apply_fdr(results, "wcb", "eta_final_p", "eta_fdr_p")
    apply_fdr(results, "frac_logit", "keff_p", "keff_fdr_p")
    apply_fdr(results, "frac_logit", "eta_p", "eta_fdr_p")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--B", type=int, default=9999)
    ap.add_argument("--seed", type=int, default=42)
    args = ap.parse_args()
    B, seed = args.B, args.seed
    t_total = time.time()

    print(f"Near-Chance Sensitivity Analysis (B={B}, seed={seed})")
    print(f"Excluding: {sorted(NEAR_CHANCE)}, indices: {sorted(EXCLUDE_IDX)}")
    print(f"Retained: {N_MODELS - len(EXCLUDE_IDX)} / {N_MODELS} models")
    print("=" * 70)

    mi_data = load_mi_data()
    pairs = load_pairs()
    clean, attacked = load_all_scores()

    iasr = {}
    for ds in DATASETS:
        for atk in ATTACKS:
            for m in ALL_MODELS:
                if m in clean[ds] and m in attacked[ds][atk]:
                    iasr[(ds, atk, m)] = individual_asr(
                        clean[ds][m], attacked[ds][atk][m], pairs[ds])
    print(f"Individual ASR: {len(iasr)} entries")

    output = {"meta": {
        "analysis": "near_chance_sensitivity",
        "near_chance_models": sorted(NEAR_CHANCE),
        "near_chance_mmlu": {"qwen2.5-14b": 0.253, "qwen2.5-72b": 0.333},
        "threshold": 0.35,
        "exclude_indices": sorted(EXCLUDE_IDX),
        "n_full": N_MODELS,
        "n_filtered": N_MODELS - len(EXCLUDE_IDX),
        "B": B, "seed": seed, "fdr_alpha": FDR_ALPHA, "eps": EPS,
        "models_full": ALL_MODELS,
        "models_filtered": [ALL_MODELS[i] for i in range(N_MODELS) if i not in EXCLUDE_IDX],
    }}

    for K in [3, 5, 7]:
        print(f"\n{'='*70}\nK={K}")
        all_combos = list(itertools.combinations(range(N_MODELS), K))
        n_full = len(all_combos)
        n_filt = sum(1 for c in all_combos if not (EXCLUDE_IDX & frozenset(c)))
        print(f"  Full: {n_full}, Filtered: {n_filt}")

        full_res, filt_res = {}, {}

        for ds in DATASETS:
            mi_np = np.array(mi_data["mi_matrix"][ds])
            for atk in ATTACKS:
                ck = f"{ds}x{atk}"
                t0 = time.time()

                # Compute panel data for ALL combos once
                asr_v, keff_v, eta_v, vc = [], [], [], []
                for combo in all_combos:
                    jids = [ALL_MODELS[i] for i in combo]
                    if not all(j in clean[ds] and j in attacked[ds][atk] for j in jids):
                        continue
                    a = compute_panel_asr(jids, clean[ds], attacked[ds][atk], pairs[ds])
                    k = mi_keff(mi_np, list(combo))
                    e = max(iasr.get((ds, atk, ALL_MODELS[i]), 0) for i in combo)
                    asr_v.append(a)
                    keff_v.append(k)
                    eta_v.append(e)
                    vc.append(combo)

                asr_a = np.array(asr_v)
                keff_a = np.array(keff_v)
                eta_a = np.array(eta_v)
                fm = np.array([not bool(EXCLUDE_IDX & frozenset(c)) for c in vc])

                # Full
                r_full = analyze_one(asr_a, keff_a, eta_a, vc, K, B, seed)
                full_res[ck] = r_full

                # Filtered
                if fm.sum() >= 10:
                    vc_f = [c for c, m in zip(vc, fm) if m]
                    r_filt = analyze_one(
                        asr_a[fm], keff_a[fm], eta_a[fm], vc_f, K, B, seed)
                else:
                    r_filt = {"skipped": True, "n": int(fm.sum())}
                filt_res[ck] = r_filt

                dt = time.time() - t0
                if not r_full.get("skipped") and not r_filt.get("skipped"):
                    print(
                        f"  {ck}: "
                        f"full(β={r_full['ols']['keff_std_beta']:.3f} "
                        f"wcb={r_full['wcb']['keff_final_p']:.4f}) "
                        f"filt(β={r_filt['ols']['keff_std_beta']:.3f} "
                        f"wcb={r_filt['wcb']['keff_final_p']:.4f}) "
                        f"{dt:.1f}s")

        # FDR correction
        do_fdr(full_res)
        do_fdr(filt_res)

        fs = make_summary(full_res)
        rs = make_summary(filt_res)

        output[f"K{K}"] = {
            "n_full": n_full, "n_filtered": n_filt,
            "full_summary": fs, "filtered_summary": rs,
            "full_conditions": full_res, "filtered_conditions": filt_res,
        }

        print(f"\n  K={K} Full:     OLS={fs['ols_keff_sig']}/12 "
              f"WCB={fs['wcb_keff_sig']}/12 "
              f"Frac={fs['frac_keff_sig']}/12 "
              f"η_WCB={fs['wcb_eta_sig']}/12 "
              f"R²={fs['mean_r2']:.4f} β_std={fs['mean_keff_std_beta']:.4f}")
        print(f"  K={K} Filtered: OLS={rs['ols_keff_sig']}/12 "
              f"WCB={rs['wcb_keff_sig']}/12 "
              f"Frac={rs['frac_keff_sig']}/12 "
              f"η_WCB={rs['wcb_eta_sig']}/12 "
              f"R²={rs['mean_r2']:.4f} β_std={rs['mean_keff_std_beta']:.4f}")

    # Print comparison table
    print(f"\n{'='*70}")
    print("COMPARISON: Full (15 models) vs Filtered (13 models)")
    print(f"{'='*70}")
    hdr = f"  {'Metric':<24} {'K':>3} {'Full':>8} {'Filt':>8} {'Delta':>6}"
    print(hdr)
    print("-" * 58)
    for K in [3, 5, 7]:
        kd = output.get(f"K{K}", {})
        f = kd.get("full_summary", {})
        r = kd.get("filtered_summary", {})
        for mk, ml in [
            ("ols_keff_sig", "OLS K_eff"),
            ("wcb_keff_sig", "WCB K_eff"),
            ("frac_keff_sig", "Frac K_eff"),
            ("wcb_eta_sig", "WCB eta_max"),
        ]:
            fv, rv = f.get(mk, 0), r.get(mk, 0)
            print(f"  {ml:<24} {K:>3} {fv:>5}/12 {rv:>5}/12 {rv-fv:>+5d}")
        for mk, ml in [
            ("mean_r2", "Mean R2"),
            ("mean_keff_std_beta", "Mean beta_std(K_eff)"),
        ]:
            fv, rv = f.get(mk, 0), r.get(mk, 0)
            print(f"  {ml:<24} {K:>3} {fv:>8.4f} {rv:>8.4f} {rv-fv:>+6.4f}")
        if K < 7:
            print()

    output["elapsed_seconds"] = time.time() - t_total
    print(f"\nTotal: {output['elapsed_seconds']:.0f}s")

    out_path = Path("/root/cert_manip_resist_eval/artifacts/results/plan001/"
                    "near_chance_sensitivity.json")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2, default=_jd, ensure_ascii=False)
    print(f"Saved: {out_path}")


if __name__ == "__main__":
    main()
