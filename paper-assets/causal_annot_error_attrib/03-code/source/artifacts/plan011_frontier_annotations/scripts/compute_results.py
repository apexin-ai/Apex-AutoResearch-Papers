#!/usr/bin/env python3
"""
plan011: Compute confusion matrices + downstream bias + ASV across 7 DAG
topologies for VAST (K=3) + CivilComments (K=2) frontier-model annotations.

Inputs:
  results/{dataset}/{model}_zero-shot.jsonl  (from annotate_frontier.py)

Outputs:
  frontier_results.json
  results/{dataset}/{model}_zero-shot_confusion_matrix.npz
  results/{dataset}/{model}_zero-shot_confusion_matrix.json
"""
import json
import os
import sys
from collections import Counter
from pathlib import Path

import numpy as np

# Reuse plan_006 K-general ASV pipeline by importing.
PROJ_ROOT = Path("/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib")
sys.path.insert(0, str(PROJ_ROOT))

from plan_006_asv_empirical import (  # type: ignore  # noqa: E402
    TOPOLOGIES,
    make_dgp_params,
    make_p_A,
    precompute_suff_stats,
    compute_plim,
    extract_tau,
    compute_asv_for_matrix,
    compute_f1_from_C,
)

PLAN_DIR = PROJ_ROOT / "artifacts" / "plan011_frontier_annotations"
RESULTS_DIR = PLAN_DIR / "results"

DATASETS = {
    "vast": {"K": 3, "classes": ["Con", "Pro", "Neutral"]},
    "civil_comments": {"K": 2, "classes": ["non-toxic", "toxic"]},
}
MODELS = ["llama4", "qwen3", "deepseek"]

ZERO_MATRIX_TRACE_EPS = 0.01
ASV_SAFE_THRESHOLD = 1.0
BIAS_PCT_THRESHOLD = 0.1  # used internally by compute_asv_for_matrix


def load_annotations(jsonl_path):
    """Read JSONL of {gold_label, pred_label, error, ...}.

    Returns: list of dicts with keys gold_label, pred_label, error.
    """
    if not jsonl_path.exists():
        return None
    recs = []
    with open(jsonl_path) as f:
        for line in f:
            line = line.strip()
            if line:
                recs.append(json.loads(line))
    return recs


def build_confusion_matrix(records, classes):
    """Column-stochastic confusion matrix C[j,k] = P(pred=j | gold=k).

    Skips records with pred_label=None or labels not in `classes`.
    Returns (C, stats_dict).
    """
    K = len(classes)
    idx = {c: i for i, c in enumerate(classes)}
    counts = np.zeros((K, K), dtype=float)
    n_total = len(records)
    n_skipped = 0
    n_used = 0
    n_correct = 0
    gold_dist = Counter()
    pred_dist = Counter()
    for r in records:
        g = r.get("gold_label")
        p = r.get("pred_label")
        if g not in idx or p not in idx:
            n_skipped += 1
            continue
        counts[idx[p], idx[g]] += 1
        n_used += 1
        if p == g:
            n_correct += 1
        gold_dist[g] += 1
        pred_dist[p] += 1
    col_sums = counts.sum(axis=0)
    col_safe = np.where(col_sums < 1, 1.0, col_sums)
    C = counts / col_safe
    stats = {
        "n_total": n_total,
        "n_used": n_used,
        "n_skipped": n_skipped,
        "coverage": n_used / n_total if n_total else 0.0,
        "accuracy": n_correct / n_used if n_used else 0.0,
        "raw_counts": counts.tolist(),
        "gold_dist": dict(gold_dist),
        "pred_dist": dict(pred_dist),
        "per_column_counts": {c: int(col_sums[idx[c]]) for c in classes},
    }
    return C, stats


def macro_f1(records, classes):
    """Empirical macro-F1 from gold/pred records (skips invalid)."""
    K = len(classes)
    idx = {c: i for i, c in enumerate(classes)}
    tp = np.zeros(K); fp = np.zeros(K); fn = np.zeros(K)
    for r in records:
        g = r.get("gold_label"); p = r.get("pred_label")
        if g not in idx:
            continue
        gi = idx[g]
        if p in idx:
            pi = idx[p]
            if pi == gi:
                tp[gi] += 1
            else:
                fp[pi] += 1
                fn[gi] += 1
        else:
            fn[gi] += 1
    f1 = np.zeros(K)
    for k in range(K):
        prec = tp[k] / max(tp[k] + fp[k], 1e-9)
        rec = tp[k] / max(tp[k] + fn[k], 1e-9)
        f1[k] = 2 * prec * rec / max(prec + rec, 1e-9) if (prec + rec) > 0 else 0.0
    return float(f1.mean()), [float(x) for x in f1]


def precompute_all_suff_stats(K_values):
    """Precompute sufficient statistics + tau_true for each K × topology."""
    all_st = {}
    all_tau_true = {}
    for K in K_values:
        params = make_dgp_params(K)
        for topo in TOPOLOGIES:
            seed = K * 1000 + abs(hash(topo)) % 1000
            st = precompute_suff_stats(K, topo, params[topo], seed=seed)
            all_st[(K, topo)] = st
            plim_I = compute_plim(np.eye(K), st, K)
            tau_true = extract_tau(plim_I, topo)
            all_tau_true[(K, topo)] = tau_true
    return all_st, all_tau_true


def _to_json_safe(obj):
    if isinstance(obj, (np.integer,)):
        return int(obj)
    if isinstance(obj, (np.floating, float)):
        v = float(obj)
        return None if (np.isnan(v) or np.isinf(v)) else v
    if isinstance(obj, np.ndarray):
        return _to_json_safe(obj.tolist())
    if isinstance(obj, (bool, np.bool_)):
        return bool(obj)
    if isinstance(obj, dict):
        return {str(k): _to_json_safe(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [_to_json_safe(x) for x in obj]
    return obj


def save_confusion_matrix(C, classes, stats, dataset, model_key):
    out_dir = RESULTS_DIR / dataset
    out_dir.mkdir(parents=True, exist_ok=True)
    npz_path = out_dir / f"{model_key}_zero-shot_confusion_matrix.npz"
    json_path = out_dir / f"{model_key}_zero-shot_confusion_matrix.json"
    np.savez(
        npz_path,
        C=C,
        classes=np.array(classes, dtype=object),
        raw_counts=np.array(stats["raw_counts"]),
    )
    with open(json_path, "w") as f:
        json.dump(_to_json_safe({
            "C": C.tolist(),
            "classes": classes,
            "stats": stats,
        }), f, indent=2)
    return npz_path, json_path


def main():
    print("=" * 70)
    print("plan011: Frontier-model bias + ASV analysis")
    print("=" * 70)

    K_values = sorted({info["K"] for info in DATASETS.values()})
    print(f"\n[1] Precomputing sufficient statistics for K={K_values}, "
          f"topologies={TOPOLOGIES} ...")
    all_st, all_tau_true = precompute_all_suff_stats(K_values)
    for (K, topo), tt in all_tau_true.items():
        print(f"  K={K:>2} {topo:<13} tau_true={tt:.6f}")

    confusion_matrices = {}
    f1_scores = []
    biases = []
    asvs = []
    config_status = []
    n_zero_matrices = 0

    for dataset, info in DATASETS.items():
        K = info["K"]
        classes = info["classes"]
        for model_key in MODELS:
            config = f"{dataset}_{model_key}_zero-shot"
            jsonl_path = RESULTS_DIR / dataset / f"{model_key}_zero-shot.jsonl"
            recs = load_annotations(jsonl_path)
            if recs is None:
                print(f"\n  [SKIP] {config}: no annotation file at {jsonl_path}")
                config_status.append({"config": config, "status": "missing_file"})
                continue

            C, stats = build_confusion_matrix(recs, classes)
            mf1, pf1 = macro_f1(recs, classes)

            tr = float(np.trace(C))
            if tr < ZERO_MATRIX_TRACE_EPS:
                print(f"\n  [ZERO-MATRIX] {config}: trace(C)={tr:.4f} — flagged, excluded "
                      f"from ASV analysis")
                config_status.append({
                    "config": config, "status": "zero_matrix",
                    "trace": tr, "stats": stats,
                })
                n_zero_matrices += 1
                # Still record the matrix + F1 for transparency
                confusion_matrices[config] = C.tolist()
                f1_scores.append({
                    "config": config, "dataset": dataset, "model": model_key,
                    "K": K, "n_used": stats["n_used"], "coverage": stats["coverage"],
                    "accuracy": stats["accuracy"], "macro_f1": mf1,
                    "per_class_f1": pf1,
                    "f1_from_C_macro": compute_f1_from_C(C, K, make_p_A(K))["macro_f1"],
                })
                continue

            npz_p, json_p = save_confusion_matrix(C, classes, stats, dataset, model_key)
            confusion_matrices[config] = C.tolist()

            f1_from_C = compute_f1_from_C(C, K, make_p_A(K))
            f1_scores.append({
                "config": config, "dataset": dataset, "model": model_key,
                "K": K, "n_used": stats["n_used"], "coverage": stats["coverage"],
                "accuracy": stats["accuracy"], "macro_f1": mf1,
                "per_class_f1": pf1,
                "f1_from_C_macro": f1_from_C["macro_f1"],
                "f1_from_C_weighted": f1_from_C["weighted_f1"],
            })

            print(f"\n  [{config}]")
            print(f"    n_used={stats['n_used']}/{stats['n_total']} "
                  f"coverage={stats['coverage']:.1%} acc={stats['accuracy']:.3f} "
                  f"macro_F1={mf1:.3f} trace(C)={tr:.4f}")

            for topo in TOPOLOGIES:
                st = all_st[(K, topo)]
                tau_true = all_tau_true[(K, topo)]
                plim_result = compute_plim(C, st, K)
                tau_hat = extract_tau(plim_result, topo)
                if np.isfinite(tau_hat) and np.isfinite(tau_true) and abs(tau_true) > 1e-12:
                    bias_abs = abs(tau_hat - tau_true)
                    bias_pct = bias_abs / abs(tau_true)
                    sign_flip = bool(np.sign(tau_hat) != np.sign(tau_true))
                else:
                    bias_abs = None
                    bias_pct = None
                    sign_flip = False
                biases.append({
                    "config": config, "dataset": dataset, "model": model_key,
                    "K": K, "topology": topo,
                    "tau_true": float(tau_true) if np.isfinite(tau_true) else None,
                    "tau_biased": float(tau_hat) if np.isfinite(tau_hat) else None,
                    "bias_abs": float(bias_abs) if bias_abs is not None else None,
                    "bias_pct": float(bias_pct) if bias_pct is not None else None,
                    "sign_flip": sign_flip,
                })

                masv = compute_asv_for_matrix(C, K, topo, st, tau_true, "magnitude")
                asv_safe = bool(masv is None or masv > ASV_SAFE_THRESHOLD)
                asvs.append({
                    "config": config, "dataset": dataset, "model": model_key,
                    "K": K, "topology": topo,
                    "magnitude_asv": float(masv) if masv is not None else None,
                    "asv_safe": asv_safe,
                })

            config_status.append({"config": config, "status": "ok",
                                  "trace": tr, "n_used": stats["n_used"]})

    # ── Summary ──────────────────────────────────────────────────────────────
    per_dataset_summary = {}
    for dataset in DATASETS:
        sub_b = [b for b in biases if b["dataset"] == dataset and b["bias_pct"] is not None]
        sub_a = [a for a in asvs if a["dataset"] == dataset]
        sub_sf = [b for b in biases if b["dataset"] == dataset and b["sign_flip"]]
        if sub_b:
            mean_bias = float(np.mean([b["bias_pct"] for b in sub_b]))
            median_bias = float(np.median([b["bias_pct"] for b in sub_b]))
        else:
            mean_bias, median_bias = None, None
        if sub_a:
            asv_unsafe = sum(1 for a in sub_a if not a["asv_safe"])
            asv_unsafe_pct = asv_unsafe / len(sub_a) * 100
        else:
            asv_unsafe, asv_unsafe_pct = 0, 0.0
        per_dataset_summary[dataset] = {
            "K": DATASETS[dataset]["K"],
            "n_scenarios": len(sub_a),
            "mean_bias_pct": mean_bias,
            "median_bias_pct": median_bias,
            "asv_unsafe_count": asv_unsafe,
            "asv_unsafe_pct": asv_unsafe_pct,
            "n_sign_flips": len(sub_sf),
        }

    sign_flips_total = sum(1 for b in biases if b["sign_flip"])

    output = _to_json_safe({
        "meta": {
            "n_configs": len(confusion_matrices),
            "datasets": list(DATASETS.keys()),
            "models": MODELS,
            "prompt": "zero-shot",
            "scope": "Frontier models on VAST (K=3) + CivilComments (K=2)",
            "topologies": list(TOPOLOGIES),
            "asv_safe_threshold": ASV_SAFE_THRESHOLD,
            "bias_threshold_pct": BIAS_PCT_THRESHOLD,
            "zero_matrix_trace_eps": ZERO_MATRIX_TRACE_EPS,
            "n_zero_matrices_flagged": n_zero_matrices,
        },
        "confusion_matrices": confusion_matrices,
        "f1_scores": f1_scores,
        "biases": biases,
        "asvs": asvs,
        "config_status": config_status,
        "summary": {
            "per_dataset": per_dataset_summary,
            "sign_flips": sign_flips_total,
            "total_scenarios": len(asvs),
        },
    })

    out_path = PLAN_DIR / "frontier_results.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nResults saved to {out_path}")

    # Print summary table
    print("\n" + "=" * 70)
    print("Summary")
    print("=" * 70)
    for ds, s in per_dataset_summary.items():
        print(f"  {ds:<14} (K={s['K']}): scenarios={s['n_scenarios']:<3} "
              f"mean_bias={s['mean_bias_pct']!r}  asv_unsafe="
              f"{s['asv_unsafe_count']}/{s['n_scenarios']} "
              f"({s['asv_unsafe_pct']:.1f}%)  sign_flips={s['n_sign_flips']}")
    print(f"\nTotal scenarios: {len(asvs)} | Total sign flips: {sign_flips_total} | "
          f"Zero-matrix configs: {n_zero_matrices}")


if __name__ == "__main__":
    main()
