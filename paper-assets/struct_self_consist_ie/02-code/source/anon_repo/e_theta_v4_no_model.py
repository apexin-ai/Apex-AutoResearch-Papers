#!/usr/bin/env python3
"""E_theta Variant 4: Without model_id (Dataset-General) + LogReg
Tests cross-model generalization by removing model_id features."""

import json
import numpy as np
from collections import Counter
from pathlib import Path

BASE = Path("/root/autodl-tmp/struct_self_consist_ie")

CONFIGS = [
    {"name": "scierc_qwen_s42",  "path": "results/exp_freeform_ablation/samples.jsonl",
     "dataset": "scierc", "model": "qwen3", "dataset_id": 0, "model_id": 0},
    {"name": "scierc_qwen_s123", "path": "output/exp_018_qwen_scierc_seed123/samples.jsonl",
     "dataset": "scierc", "model": "qwen3", "dataset_id": 0, "model_id": 0},
    {"name": "scierc_qwen_s456", "path": "results/exp_freeform_ablation_seed456/samples.jsonl",
     "dataset": "scierc", "model": "qwen3", "dataset_id": 0, "model_id": 0},
    {"name": "conll_qwen_s123",  "path": "output/exp_002_conll_n8_seed123/samples.jsonl",
     "dataset": "conll", "model": "qwen3", "dataset_id": 1, "model_id": 0},
    {"name": "fewnerd_qwen_s123","path": "output/exp_021_fewnerd_n8_seed123/samples.jsonl",
     "dataset": "fewnerd", "model": "qwen3", "dataset_id": 2, "model_id": 0},
    {"name": "scierc_llama_s42", "path": "output/exp_018_llama_scierc_seed42_r1024/samples.jsonl",
     "dataset": "scierc", "model": "llama", "dataset_id": 0, "model_id": 1},
    {"name": "conll_llama_s42",  "path": "output/exp_017_llama_conll_infer/samples.jsonl",
     "dataset": "conll", "model": "llama", "dataset_id": 1, "model_id": 1},
]

THETA_GRID = np.array([0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7])

FEATURE_NAMES = [
    "degeneracy_level", "lp_variance", "sample_count_N",
    "is_scierc", "is_conll", "is_fewnerd",
    "agreement_mean", "n_unique_entities"
]


def entity_set(entities):
    return frozenset((e["text"], e["type"]) for e in entities)


def compute_f1(pred_set, gold_set):
    if not pred_set and not gold_set:
        return 1.0
    if not pred_set or not gold_set:
        return 0.0
    tp = len(pred_set & gold_set)
    p = tp / len(pred_set)
    r = tp / len(gold_set)
    return 2 * p * r / (p + r) if (p + r) > 0 else 0.0


def process_instance(inst, config):
    gold_ents = entity_set(inst["gold"]["entities"])
    samples = inst.get("samples", [])
    N = len(samples)
    if N < 2:
        return None

    sample_sets = [entity_set(s["entities"]) for s in samples]
    all_ents = set()
    for s in sample_sets:
        all_ents |= s

    agreement = {}
    for ent in all_ents:
        agreement[ent] = sum(1 for s in sample_sets if ent in s) / N

    theta_f1s = {}
    for theta in THETA_GRID:
        constructed = frozenset(e for e, a in agreement.items() if a >= theta)
        theta_f1s[float(theta)] = compute_f1(constructed, gold_ents)

    best_f1 = max(theta_f1s.values())
    best_theta = min(
        [t for t in THETA_GRID if theta_f1s[float(t)] == best_f1],
        key=lambda t: abs(t - 0.5)
    )

    counts = Counter(sample_sets)
    degeneracy = max(counts.values()) / N

    logprobs = inst.get("logprobs", [])
    if logprobs and len(logprobs) >= 2:
        lp_var = float(np.std(logprobs))
    else:
        lps = [s.get("mean_logprob", 0) for s in samples]
        lp_var = float(np.std(lps)) if len(lps) >= 2 else 0.0

    agr_vals = list(agreement.values())
    agr_mean = float(np.mean(agr_vals)) if agr_vals else 1.0

    features = np.array([
        degeneracy,
        lp_var,
        float(N),
        float(config["dataset_id"] == 0),  # is_scierc
        float(config["dataset_id"] == 1),  # is_conll
        float(config["dataset_id"] == 2),  # is_fewnerd
        agr_mean,
        float(len(all_ents)),
    ])

    return {
        "oracle_theta": float(best_theta),
        "oracle_f1": best_f1,
        "theta_f1s": theta_f1s,
        "features": features,
    }


def ridge_fit(X, y, alpha=1.0):
    d = X.shape[1]
    return np.linalg.solve(X.T @ X + alpha * np.eye(d), X.T @ y)


def main():
    print("=" * 60)
    print("E_theta V4: No model_id + LogReg (Ridge)")
    print("=" * 60)

    all_data = {}
    for config in CONFIGS:
        path = BASE / config["path"]
        print(f"\nLoading {config['name']} from {path}")
        if not path.exists():
            print(f"  WARNING: {path} not found, skipping")
            continue

        results = []
        with open(path) as f:
            for i, line in enumerate(f):
                inst = json.loads(line)
                r = process_instance(inst, config)
                if r is not None:
                    results.append(r)
                if (i + 1) % 10000 == 0:
                    print(f"  {i+1} lines ...", flush=True)

        all_data[config["name"]] = results
        thetas = [r["oracle_theta"] for r in results]
        print(f"  -> {len(results)} instances")
        print(f"     oracle theta top-5: {Counter(thetas).most_common(5)}")

    config_names = list(all_data.keys())
    X_list, y_list, labels, tf1_list = [], [], [], []
    for cname in config_names:
        for inst in all_data[cname]:
            X_list.append(inst["features"])
            y_list.append(inst["oracle_theta"])
            labels.append(cname)
            tf1_list.append(inst["theta_f1s"])

    X = np.array(X_list)
    y = np.array(y_list)
    labels = np.array(labels)

    print(f"\nTotal: {len(X)} instances across {len(config_names)} configs")
    print(f"Overall oracle theta dist: {Counter(y).most_common()}")

    # Leave-one-config-out CV
    per_config = {}
    all_adap, all_fix, all_orac = [], [], []

    for held_out in config_names:
        tr = labels != held_out
        te = labels == held_out

        X_tr, y_tr = X[tr], y[tr]
        X_te = X[te]

        mu, sigma = X_tr.mean(0), X_tr.std(0)
        sigma[sigma == 0] = 1.0
        X_tr_s = (X_tr - mu) / sigma
        X_te_s = (X_te - mu) / sigma

        beta = ridge_fit(X_tr_s, y_tr, alpha=1.0)
        y_pred_raw = X_te_s @ beta
        y_pred = np.array([THETA_GRID[np.argmin(np.abs(THETA_GRID - p))] for p in y_pred_raw])

        test_idx = np.where(te)[0]
        adap, fix, orac = [], [], []
        for j, idx in enumerate(test_idx):
            tf = tf1_list[idx]
            pt = float(y_pred[j])
            adap.append(tf.get(pt, tf[0.5]))
            fix.append(tf[0.5])
            orac.append(max(tf.values()))

        ma, mf, mo = np.mean(adap), np.mean(fix), np.mean(orac)
        per_config[held_out] = {
            "n_instances": int(te.sum()),
            "adaptive_f1": round(float(ma), 6),
            "fixed_theta05_f1": round(float(mf), 6),
            "oracle_f1": round(float(mo), 6),
            "delta_adaptive_vs_fixed": round(float(ma - mf), 6),
            "predicted_theta_dist": {str(k): int(v) for k, v in Counter(y_pred.tolist()).most_common()},
        }
        all_adap.extend(adap)
        all_fix.extend(fix)
        all_orac.extend(orac)
        print(f"  {held_out:25s}  adap={ma:.4f}  fix={mf:.4f}  orac={mo:.4f}  delta={ma-mf:+.5f}")

    mu_a, sig_a = X.mean(0), X.std(0)
    sig_a[sig_a == 0] = 1.0
    beta_all = ridge_fit((X - mu_a) / sig_a, y, alpha=1.0)
    feat_imp = {n: round(float(c), 6) for n, c in zip(FEATURE_NAMES, beta_all)}

    oa = float(np.mean(all_adap))
    of_ = float(np.mean(all_fix))
    oo = float(np.mean(all_orac))

    # Compare with v1
    v1_path = BASE / "output" / "e_theta_v1_logreg_results.json"
    v1_comparison = {}
    if v1_path.exists():
        with open(v1_path) as f:
            v1 = json.load(f)
        v1_adap = v1["overall_adaptive_f1"]
        v1_delta = v1["delta_adaptive_vs_fixed"]
        v4_delta = oa - of_
        v1_comparison = {
            "v1_overall_adaptive_f1": v1_adap,
            "v1_overall_fixed_f1": v1["overall_fixed_f1"],
            "v1_delta_adaptive_vs_fixed": v1_delta,
            "v4_delta_adaptive_vs_fixed": round(v4_delta, 6),
            "gap_v4_minus_v1_delta": round(v4_delta - v1_delta, 6),
            "gap_v4_minus_v1_adaptive_f1": round(oa - v1_adap, 6),
            "model_id_matters": abs(oa - v1_adap) > 0.01,
        }

    output = {
        "variant": "v4_no_model_id_logreg",
        "description": "No model_id features (is_qwen, is_llama removed). Tests cross-model generalization.",
        "features_used": FEATURE_NAMES,
        "per_config_results": per_config,
        "overall_adaptive_f1": round(oa, 6),
        "overall_fixed_f1": round(of_, 6),
        "overall_oracle_f1": round(oo, 6),
        "delta_adaptive_vs_fixed": round(oa - of_, 6),
        "feature_importance": feat_imp,
        "n_configs": len(config_names),
        "n_instances_total": len(X),
        "theta_grid": THETA_GRID.tolist(),
        "v1_comparison": v1_comparison,
    }

    out_path = BASE / "output" / "e_theta_v4_no_model_results.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)

    print(f"\n{'='*60}")
    print(f"OVERALL: adaptive={oa:.4f}  fixed={of_:.4f}  oracle={oo:.4f}")
    print(f"  delta(adaptive - fixed) = {oa - of_:+.5f}")
    print(f"  delta(oracle - fixed)   = {oo - of_:+.5f}")
    print(f"\nFeature importance:")
    for name, coef in sorted(feat_imp.items(), key=lambda x: abs(x[1]), reverse=True):
        print(f"  {name:25s} {coef:+.6f}")
    if v1_comparison:
        print(f"\n--- V1 comparison ---")
        print(f"  v1 adaptive F1: {v1_comparison['v1_overall_adaptive_f1']:.6f}")
        print(f"  v4 adaptive F1: {oa:.6f}")
        print(f"  gap (v4-v1):    {v1_comparison['gap_v4_minus_v1_adaptive_f1']:+.6f}")
        print(f"  model_id matters: {v1_comparison['model_id_matters']}")
    print(f"\nSaved to {out_path}")


if __name__ == "__main__":
    main()
