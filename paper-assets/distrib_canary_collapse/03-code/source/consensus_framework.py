"""
Multi-method consensus framework for canary→downstream association robustness.

Formalizes "robust association": a pair is robust only when ≥method_threshold
independent statistical methods agree (each requiring ≥seed_threshold seeds
significant). Two-stage aggregation: seed→method verdict, then method→consensus.

Input:  results/mvp/analysis/method_ablation.json
Output: consensus classification, sensitivity heatmap, FPR/FNR table (JSON)

Dependencies: numpy, json (stdlib)
"""

import json
import os

import numpy as np

METHOD_NAMES = [
    "naive_pearson",
    "differenced_xcorr",
    "threshold_onset",
    "toda_yamamoto",
    "permutation_granger",
]

# differenced_xcorr is the FP ground truth (index 1)
DIFF_INDEX = 1


def _to_native(obj):
    """Convert numpy types to Python native for JSON serialization."""
    if isinstance(obj, (np.integer,)):
        return int(obj)
    if isinstance(obj, (np.floating,)):
        return float(obj)
    if isinstance(obj, (np.bool_,)):
        return bool(obj)
    if isinstance(obj, np.ndarray):
        return obj.tolist()
    return obj


class NumpyEncoder(json.JSONEncoder):
    """JSON encoder that handles numpy types."""
    def default(self, obj):
        native = _to_native(obj)
        if native is not obj:
            return native
        return super().default(obj)


def load_sig_matrix(ablation_path, apply_fdr=True):
    """
    Load method_ablation.json into a boolean significance tensor.

    Args:
        ablation_path: path to method_ablation.json

    Returns:
        sig_matrix: np.ndarray, shape (5, 16, 4), dtype bool
                    axes = (method, pair, seed)
        pair_names: list of (canary, downstream) tuples, len 16
        method_names: list of str, len 5
        seeds: list of int, e.g. [42, 43, 44, 45]
    """
    with open(ablation_path) as f:
        data = json.load(f)

    pairs = data["pairs"]
    seeds = data["meta"]["seeds"]
    n_m = len(METHOD_NAMES)
    n_p = len(pairs)
    n_s = len(seeds)

    sig = np.zeros((n_m, n_p, n_s), dtype=bool)
    pair_names = []

    for pi, pair in enumerate(pairs):
        pair_names.append((pair["canary"], pair["downstream"]))
        for si, seed_rec in enumerate(pair["per_seed"]):
            for mi, method in enumerate(METHOD_NAMES):
                if method in seed_rec:
                    if apply_fdr:
                        if method == "threshold_onset":
                            # Non-statistical test, no FDR version exists
                            sig[mi, pi, si] = seed_rec[method].get("significant", False)
                        else:
                            sig[mi, pi, si] = seed_rec[method].get("significant_fdr", False)
                    else:
                        sig[mi, pi, si] = seed_rec[method].get("significant", False)

    return sig, pair_names, list(METHOD_NAMES), seeds


def classify_robust(sig_matrix, method_threshold, seed_threshold):
    """
    Two-stage consensus classification.

    Stage 1 (seed aggregation): method M calls pair P "significant" if
        ≥seed_threshold of n_seeds show significance for (M, P).
    Stage 2 (method consensus): pair P is "robust" if ≥method_threshold
        methods call it significant.

    Args:
        sig_matrix: bool array, shape (n_methods, n_pairs, n_seeds)
        method_threshold: int, min methods required
        seed_threshold: int, min seeds required per method

    Returns:
        dict with:
          classifications: list of per-pair dicts (pair_index, is_robust,
                           n_sig_methods, method_verdicts, seed_counts)
          n_robust, n_non_robust: int
          params: dict of threshold parameters
    """
    n_methods, n_pairs, n_seeds = sig_matrix.shape

    seed_counts = sig_matrix.sum(axis=2)            # (n_methods, n_pairs)
    method_verdicts = seed_counts >= seed_threshold  # (n_methods, n_pairs)
    method_counts = method_verdicts.sum(axis=0)      # (n_pairs,)
    is_robust = method_counts >= method_threshold

    classifications = []
    for pi in range(n_pairs):
        classifications.append({
            "pair_index": pi,
            "n_sig_methods": int(method_counts[pi]),
            "is_robust": bool(is_robust[pi]),
            "method_verdicts": method_verdicts[:, pi].tolist(),
            "seed_counts": seed_counts[:, pi].astype(int).tolist(),
        })

    return {
        "classifications": classifications,
        "n_robust": int(is_robust.sum()),
        "n_non_robust": int((~is_robust).sum()),
        "params": {
            "method_threshold": method_threshold,
            "seed_threshold": seed_threshold,
            "n_methods": n_methods,
            "n_seeds": n_seeds,
        },
    }


def sensitivity_analysis(sig_matrix, pair_names, method_names,
                         method_thresholds=None, seed_thresholds=None):
    """
    Sweep classify_robust over a grid of (method_threshold, seed_threshold).

    Args:
        sig_matrix: bool, (n_methods, n_pairs, n_seeds)
        pair_names: list of (canary, downstream)
        method_names: list of str
        method_thresholds: list[int]; default [K-2, K-1, K]
        seed_thresholds: list[int]; default [2, 3, 4]

    Returns:
        dict with grid (list of config results), pair_stability (per-pair
        fraction of configs where robust), pair_labels
    """
    n_methods, n_pairs, n_seeds = sig_matrix.shape
    K = n_methods

    if method_thresholds is None:
        method_thresholds = [K - 2, K - 1, K]
    if seed_thresholds is None:
        seed_thresholds = [2, 3, 4]

    pair_labels = [f"{c}→{d}" for c, d in pair_names]
    grid = []

    for mt in method_thresholds:
        for st in seed_thresholds:
            result = classify_robust(sig_matrix, mt, st)
            entry = {
                "method_threshold": mt,
                "seed_threshold": st,
                "label": f"≥{mt}/{K} methods, ≥{st}/{n_seeds} seeds",
                "n_robust": result["n_robust"],
                "robust_pairs": [],
                "pair_status": {},
            }
            for cl in result["classifications"]:
                pi = cl["pair_index"]
                lbl = pair_labels[pi]
                entry["pair_status"][lbl] = cl["is_robust"]
                if cl["is_robust"]:
                    entry["robust_pairs"].append(lbl)
            grid.append(entry)

    pair_stability = {}
    for lbl in pair_labels:
        rc = sum(1 for g in grid if g["pair_status"].get(lbl, False))
        pair_stability[lbl] = {
            "robust_in_n_configs": rc,
            "total_configs": len(grid),
            "stability": round(rc / len(grid), 3),
        }

    return {
        "method_thresholds": method_thresholds,
        "seed_thresholds": seed_thresholds,
        "n_configs": len(grid),
        "grid": grid,
        "pair_stability": pair_stability,
        "pair_labels": pair_labels,
    }


def compute_fpr_fnr_diff(sig_matrix, pair_names, method_names,
                    consensus_method_thresh=None, consensus_seed_thresh=3):
    """
    Per-method FPR and FNR at seed level.

    FPR ground truth: differenced_xcorr.
      A (pair, seed) is "truly negative" when differenced is not significant.
      FP(M) = M sig AND differenced not sig.
      FPR(M) = FP(M) / N_negatives.

    FNR ground truth: multi-method consensus (pair level).
      All seeds of consensus-robust pairs are "truly positive".
      FN(M) = robust-pair seed AND M not sig.
      FNR(M) = FN(M) / N_positives.

    Args:
        sig_matrix: bool, (n_methods, n_pairs, n_seeds)
        pair_names: list of (canary, downstream)
        method_names: list of str
        consensus_method_thresh: int; default K-1
        consensus_seed_thresh: int; default 3

    Returns:
        dict with per_method_fpr, per_method_fnr, consensus row, summary table
    """
    n_methods, n_pairs, n_seeds = sig_matrix.shape
    K = n_methods
    if consensus_method_thresh is None:
        consensus_method_thresh = K - 1

    # --- FPR ground truth: differenced ---
    diff_sig = sig_matrix[DIFF_INDEX]        # (n_pairs, n_seeds)
    diff_neg = ~diff_sig                     # true negatives at seed level
    n_neg = int(diff_neg.sum())

    fpr_results = {}
    for mi, mname in enumerate(method_names):
        msig = sig_matrix[mi]                # (n_pairs, n_seeds)
        fp = int((msig & diff_neg).sum())
        fpr_results[mname] = {
            "fp": fp,
            "total_negatives": n_neg,
            "fpr": round(fp / n_neg, 4) if n_neg > 0 else 0.0,
        }

    # --- FNR ground truth: consensus ---
    consensus = classify_robust(sig_matrix, consensus_method_thresh, consensus_seed_thresh)
    robust_mask = np.array([c["is_robust"] for c in consensus["classifications"]])
    # Broadcast pair-level mask to seed level
    robust_seed = np.broadcast_to(robust_mask[:, None], (n_pairs, n_seeds))
    n_pos = int(robust_seed.sum())

    fnr_results = {}
    for mi, mname in enumerate(method_names):
        msig = sig_matrix[mi]
        fn = int((robust_seed & ~msig).sum())
        fnr_results[mname] = {
            "fn": fn,
            "total_positives": n_pos,
            "fnr": round(fn / n_pos, 4) if n_pos > 0 else 0.0,
        }

    # --- Consensus own metrics ---
    # Pair-level FPR: consensus-robust vs differenced verdict
    diff_pair_sig = diff_sig.sum(axis=1) >= consensus_seed_thresh  # (n_pairs,)
    diff_pair_neg = ~diff_pair_sig
    n_pair_neg = int(diff_pair_neg.sum())
    cons_fp_pair = int((robust_mask & diff_pair_neg).sum())

    # Seed-level FPR: treat all seeds of robust pairs as "consensus sig"
    cons_seed_sig = np.broadcast_to(robust_mask[:, None], (n_pairs, n_seeds))
    cons_fp_seed = int((cons_seed_sig & diff_neg).sum())

    robust_pair_labels = [
        f"{pair_names[i][0]}→{pair_names[i][1]}"
        for i in range(n_pairs) if robust_mask[i]
    ]

    consensus_row = {
        "fpr_pair_level": {
            "fp": cons_fp_pair,
            "total_negatives": n_pair_neg,
            "fpr": round(cons_fp_pair / n_pair_neg, 4) if n_pair_neg > 0 else 0.0,
        },
        "fpr_seed_level": {
            "fp": cons_fp_seed,
            "total_negatives": n_neg,
            "fpr": round(cons_fp_seed / n_neg, 4) if n_neg > 0 else 0.0,
        },
        "fnr": 0.0,
        "fnr_note": "0 by construction (consensus IS the FNR ground truth)",
        "n_robust_pairs": int(robust_mask.sum()),
        "robust_pairs": robust_pair_labels,
    }

    # Summary table
    table = []
    for mi, mname in enumerate(method_names):
        table.append({
            "method": mname,
            "fpr": fpr_results[mname]["fpr"],
            "fpr_detail": fpr_results[mname],
            "fnr": fnr_results[mname]["fnr"],
            "fnr_detail": fnr_results[mname],
            "sig_count_pair": int((sig_matrix[mi].sum(axis=1) >= consensus_seed_thresh).sum()),
            "sig_count_seed": int(sig_matrix[mi].sum()),
        })
    table.append({
        "method": "consensus",
        "fpr": consensus_row["fpr_seed_level"]["fpr"],
        "fpr_detail": consensus_row["fpr_seed_level"],
        "fnr": 0.0,
        "fnr_note": "0 by construction",
        "n_robust": consensus_row["n_robust_pairs"],
    })

    return {
        "ground_truth": {
            "fpr_ground_truth": "differenced_xcorr (seed level)",
            "fnr_ground_truth": (f"consensus (≥{consensus_method_thresh}/{K} methods, "
                                 f"≥{consensus_seed_thresh}/{n_seeds} seeds)"),
            "n_negatives_seed": n_neg,
            "n_positives_seed": n_pos,
        },
        "per_method_fpr": fpr_results,
        "per_method_fnr": fnr_results,
        "consensus": consensus_row,
        "table": table,
    }




# Phase 2 method names (different from MVP method names)
PHASE2_METHOD_MAP = {
    "naive": "naive_pearson",
    "differenced": "differenced_xcorr",
    "threshold": "threshold_onset",
    "permutation_granger": "permutation_granger",
    "TY": "toda_yamamoto",
}

PHASE2_METHODS = ["naive", "differenced", "threshold", "permutation_granger", "TY"]


def _bh_fdr(pvals, alpha=0.05):
    """Benjamini-Hochberg FDR correction. Returns (adjusted_p, significant_bool)."""
    pvals = np.array(pvals, dtype=float)
    n = len(pvals)
    if n == 0:
        return np.array([]), np.array([], dtype=bool)
    sorted_idx = np.argsort(pvals)
    sorted_p = pvals[sorted_idx]
    adjusted = np.zeros(n)
    adjusted[sorted_idx[-1]] = sorted_p[-1]
    for i in range(n - 2, -1, -1):
        adjusted[sorted_idx[i]] = min(sorted_p[i] * n / (i + 1),
                                       adjusted[sorted_idx[i + 1]])
    adjusted = np.minimum(adjusted, 1.0)
    return adjusted, adjusted <= alpha


def load_null_control_data(phase2_path):
    """
    Load alpha=0.0 records from Phase 2 panel as null control significance.

    Returns:
        null_sig: dict mapping method_name -> list of bool (per-pair significance)
        null_sig_fdr: dict mapping method_name -> list of bool (BH-corrected)
        null_pvals: dict mapping method_name -> list of float or None
        pairs: list of (canary, downstream) tuples
    """
    with open(phase2_path) as f:
        data = json.load(f)

    a0 = [r for r in data["panel"] if r["alpha"] == 0.0]
    pairs = [(r["canary"], r["downstream"]) for r in a0]

    null_sig = {}
    null_sig_fdr = {}
    null_pvals = {}

    for m in PHASE2_METHODS:
        sigs = [r["methods"][m].get("significant", False) for r in a0]
        pvals = [r["methods"][m].get("p_value", None) for r in a0]
        null_sig[m] = sigs
        null_pvals[m] = pvals

        valid_p = [p for p in pvals if p is not None]
        if len(valid_p) > 0 and m != "threshold":
            adj_p, sig_fdr = _bh_fdr(valid_p)
            null_sig_fdr[m] = sig_fdr.tolist()
        else:
            null_sig_fdr[m] = list(sigs)

    return null_sig, null_sig_fdr, null_pvals, pairs


def compute_fpr_null_control(phase2_path):
    """
    FPR from alpha=0.0 null control: any significance at alpha=0.0 is a false positive.

    Returns dict with per-method FPR (raw and BH-corrected).
    """
    null_sig, null_sig_fdr, null_pvals, pairs = load_null_control_data(phase2_path)
    n_pairs = len(pairs)

    table = []
    for m in PHASE2_METHODS:
        n_sig_raw = sum(null_sig[m])
        n_sig_fdr = sum(null_sig_fdr[m])
        row = {
            "method": m,
            "fpr_p_raw": round(n_sig_raw / n_pairs, 4),
            "sig_raw": n_sig_raw,
            "fpr_p_fdr": round(n_sig_fdr / n_pairs, 4),
            "sig_fdr": n_sig_fdr,
            "total": n_pairs,
        }
        pv = null_pvals[m]
        if any(p is not None for p in pv):
            row["p_values_raw"] = pv
        table.append(row)

    return {
        "description": "FPR from alpha=0.0 null control (no canary injection)",
        "ground_truth": "alpha=0.0 (any significance is false positive by definition)",
        "n_pairs": n_pairs,
        "seed": 42,
        "note": "single seed — interpret with caution",
        "table": table,
        "pairs": [f"{c}->{d}" for c, d in pairs],
    }


def compute_phase2_fdr_sig_rates(phase2_path):
    """
    Recompute Phase 2 method x alpha sig rates with BH FDR correction.

    Returns dict of alpha -> method -> {rate_raw, rate_fdr, ...}.
    """
    with open(phase2_path) as f:
        data = json.load(f)

    panel = data["panel"]
    alphas = sorted(set(r["alpha"] for r in panel))
    result = {}

    for alpha in alphas:
        a_recs = [r for r in panel if r["alpha"] == alpha]
        result[str(alpha)] = {}

        for m in PHASE2_METHODS:
            sigs = [r["methods"][m].get("significant", False) for r in a_recs]
            pvals = [r["methods"][m].get("p_value", None) for r in a_recs]
            n = len(sigs)
            n_sig_raw = sum(sigs)

            if m == "threshold":
                result[str(alpha)][m] = {
                    "sig_raw": n_sig_raw, "total": n,
                    "rate_p_raw": round(n_sig_raw / n, 4),
                    "rate_p_fdr": round(n_sig_raw / n, 4),
                    "note": "non-statistical",
                }
            else:
                valid_p = [p for p in pvals if p is not None]
                if valid_p:
                    adj_p, sig_fdr = _bh_fdr(valid_p)
                    n_sig_fdr = int(sig_fdr.sum())
                else:
                    n_sig_fdr = 0
                result[str(alpha)][m] = {
                    "sig_raw": n_sig_raw, "total": n,
                    "rate_p_raw": round(n_sig_raw / n, 4),
                    "sig_fdr": n_sig_fdr,
                    "rate_p_fdr": round(n_sig_fdr / n, 4) if n > 0 else 0.0,
                }

    return {"alphas": alphas, "rates": result}


def compute_fpr_fnr_loo(sig_matrix, pair_names, method_names, seed_threshold=3):
    """Leave-one-out FPR/FNR: ground truth = consensus of remaining K-1 methods (threshold K-2)."""
    n_methods, n_pairs, n_seeds = sig_matrix.shape
    K = n_methods

    results = {}
    for mi, mname in enumerate(method_names):
        other_sig = np.delete(sig_matrix, mi, axis=0)
        loo_consensus = classify_robust(other_sig, K - 2, seed_threshold)

        gt_robust = np.array([c["is_robust"] for c in loo_consensus["classifications"]])
        gt_positive = np.broadcast_to(gt_robust[:, None], (n_pairs, n_seeds))
        gt_negative = ~gt_positive

        n_pos = int(gt_positive.sum())
        n_neg = int(gt_negative.sum())

        m_sig = sig_matrix[mi]
        fp = int((m_sig & gt_negative).sum())
        fpr = round(fp / n_neg, 4) if n_neg > 0 else 0.0
        fn = int((~m_sig & gt_positive).sum())
        fnr = round(fn / n_pos, 4) if n_pos > 0 else 0.0

        results[mname] = {
            "fpr_loo": fpr,
            "fnr_loo": fnr,
            "fp": fp,
            "fn": fn,
            "n_positives": n_pos,
            "n_negatives": n_neg,
            "loo_n_robust": int(gt_robust.sum()),
            "loo_robust_pairs": [
                f"{pair_names[i][0]}\u2192{pair_names[i][1]}"
                for i in range(n_pairs) if gt_robust[i]
            ],
        }

    return results


def main():
    """Run all three sub-tasks and save results."""
    base = "/root/autodl-tmp/distrib_canary_collapse"
    ablation_path = os.path.join(base, "results/mvp/analysis/method_ablation.json")
    out_dir = os.path.join(base, "results/mvp/analysis/consensus")
    os.makedirs(out_dir, exist_ok=True)

    sig_matrix, pair_names, method_names, seeds = load_sig_matrix(ablation_path)
    K = len(method_names)
    n_seeds = len(seeds)
    pair_labels = [f"{c}→{d}" for c, d in pair_names]

    print(f"Loaded: {sig_matrix.shape} (methods={K}, pairs={len(pair_names)}, seeds={n_seeds})")
    print(f"Methods: {method_names}")
    print(f"Seeds: {seeds}")
    print()

    # ── Sub-task 1: Consensus classification ──
    default_mt = K - 1
    default_st = 3
    consensus = classify_robust(sig_matrix, default_mt, default_st)
    for cl in consensus["classifications"]:
        pi = cl["pair_index"]
        cl["canary"] = pair_names[pi][0]
        cl["downstream"] = pair_names[pi][1]
        cl["pair_label"] = pair_labels[pi]

    print(f"=== Sub-task 1: Consensus (≥{default_mt}/{K} methods, ≥{default_st}/{n_seeds} seeds) ===")
    print(f"Robust: {consensus['n_robust']}, Non-robust: {consensus['n_non_robust']}")
    for cl in consensus["classifications"]:
        tag = "ROBUST" if cl["is_robust"] else "non-robust"
        methods_str = "/".join(
            method_names[i][:6] for i, v in enumerate(cl["method_verdicts"]) if v
        )
        print(f"  {cl['pair_label']:<35s} {tag:<12s} "
              f"{cl['n_sig_methods']}/{K} methods  seeds={cl['seed_counts']}  [{methods_str}]")
    print()

    # ── Sub-task 2: Sensitivity analysis ──
    sa = sensitivity_analysis(sig_matrix, pair_names, method_names,
                              method_thresholds=[K - 2, K - 1, K],
                              seed_thresholds=[2, 3, 4])

    print(f"=== Sub-task 2: Sensitivity ({sa['n_configs']} configs) ===")
    for g in sa["grid"]:
        rp_str = ", ".join(g["robust_pairs"]) if g["robust_pairs"] else "(none)"
        print(f"  {g['label']:<35s}: {g['n_robust']:>2} robust  [{rp_str}]")
    print()
    print("Pair stability (fraction of configs where robust):")
    for lbl in pair_labels:
        ps = sa["pair_stability"][lbl]
        bar = "█" * ps["robust_in_n_configs"] + "░" * (ps["total_configs"] - ps["robust_in_n_configs"])
        print(f"  {lbl:<35s} {bar} {ps['robust_in_n_configs']}/{ps['total_configs']} ({ps['stability']:.0%})")
    print()

    # ── Sub-task 3: FPR / FNR ──
    fpr_fnr = compute_fpr_fnr_diff(sig_matrix, pair_names, method_names,
                                consensus_method_thresh=default_mt,
                               consensus_seed_thresh=default_st)

    print(f"=== Sub-task 3: FPR/FNR ===")
    gt = fpr_fnr["ground_truth"]
    print(f"FPR ground truth: {gt['fpr_ground_truth']} (N_neg={gt['n_negatives_seed']})")
    print(f"FNR ground truth: {gt['fnr_ground_truth']} (N_pos={gt['n_positives_seed']})")
    print()
    hdr = f"  {'Method':<24s} {'FPR':>8s} {'FNR':>8s} {'Sig(pair)':>10s} {'Sig(seed)':>10s}"
    print(hdr)
    print("  " + "-" * 62)
    for row in fpr_fnr["table"]:
        fpr_s = f"{row['fpr']:.1%}"
        fnr_v = row.get("fnr", 0)
        fnr_s = f"{fnr_v:.1%}" if isinstance(fnr_v, (int, float)) else str(fnr_v)
        sig_p = str(row.get("sig_count_pair", row.get("n_robust", "")))
        sig_s = str(row.get("sig_count_seed", ""))
        print(f"  {row['method']:<24s} {fpr_s:>8s} {fnr_s:>8s} {sig_p:>10s} {sig_s:>10s}")
    print()

    # ── Sub-task 4: LOO FPR/FNR ──
    loo = compute_fpr_fnr_loo(sig_matrix, pair_names, method_names,
                               seed_threshold=default_st)

    print(f"=== Sub-task 4: LOO FPR/FNR (K-2 consensus ground truth) ===")
    hdr_loo = f"  {'Method':<24s} {'FPR_loo':>8s} {'FNR_loo':>8s} {'FP':>5s} {'FN':>5s} {'N_pos':>6s} {'N_neg':>6s} {'LOO_robust':>10s}"
    print(hdr_loo)
    print("  " + "-" * 75)
    for mname in method_names:
        r = loo[mname]
        print(f"  {mname:<24s} {r['fpr_loo']:>7.1%} {r['fnr_loo']:>7.1%} "
              f"{r['fp']:>5d} {r['fn']:>5d} {r['n_positives']:>6d} {r['n_negatives']:>6d} "
              f"{r['loo_n_robust']:>10d}")
    print()

    # ── Save ──
    with open(os.path.join(out_dir, "consensus_classification.json"), "w") as f:
        json.dump(consensus, f, indent=2, cls=NumpyEncoder)
    with open(os.path.join(out_dir, "sensitivity_analysis.json"), "w") as f:
        json.dump(sa, f, indent=2, cls=NumpyEncoder)
    with open(os.path.join(out_dir, "fpr_fnr_table.json"), "w") as f:
        json.dump(fpr_fnr, f, indent=2, cls=NumpyEncoder)

    with open(os.path.join(out_dir, "fpr_fnr_loo.json"), "w") as f:
        json.dump(loo, f, indent=2, cls=NumpyEncoder)

    print(f"Saved to {out_dir}/")
    return consensus, sa, fpr_fnr


if __name__ == "__main__":
    main()
