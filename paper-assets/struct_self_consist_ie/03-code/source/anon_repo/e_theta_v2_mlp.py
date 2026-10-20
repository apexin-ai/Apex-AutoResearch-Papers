#!/usr/bin/env python3
"""E_theta Variant 2: Full Features + 2-Layer MLP
Leave-one-config-out CV to predict optimal theta from per-config features.
"""

import json
import math
import os
import sys
import time
import numpy as np
from collections import defaultdict, Counter

BASE = "/root/autodl-tmp/struct_self_consist_ie"
OUTPUT_DIR = f"{BASE}/artifacts/e_theta"
N_USE = 8  # subsample to N=8

THETA_GRID = [0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7]

CONFIGS = {
    # Qwen3-8B-FT x SciERC
    "Qwen_SciERC_s42": {"path": f"{BASE}/output/exp_001_seed42_v2/samples.jsonl", "model": "Qwen3-8B", "dataset": "scierc"},
    "Qwen_SciERC_s123": {"path": f"{BASE}/output/exp_001_seed123_v2/samples.jsonl", "model": "Qwen3-8B", "dataset": "scierc"},
    "Qwen_SciERC_s456": {"path": f"{BASE}/output/exp_001_seed456_v2/samples.jsonl", "model": "Qwen3-8B", "dataset": "scierc"},
    # Qwen3-8B-FT x CoNLL
    "Qwen_CoNLL_s42": {"path": f"{BASE}/output/exp_002_conll_n16/samples.jsonl", "model": "Qwen3-8B", "dataset": "conll"},
    "Qwen_CoNLL_s123": {"path": f"{BASE}/output/exp_002_conll_n16_seed123/samples.jsonl", "model": "Qwen3-8B", "dataset": "conll"},
    "Qwen_CoNLL_s456": {"path": f"{BASE}/output/exp_002_conll_n16_seed456/samples.jsonl", "model": "Qwen3-8B", "dataset": "conll"},
    # Qwen3-8B-FT x FewNERD
    "Qwen_FewNERD_s42": {"path": f"{BASE}/output/exp_021_inference/samples.jsonl", "model": "Qwen3-8B", "dataset": "fewnerd"},
    "Qwen_FewNERD_s123": {"path": f"{BASE}/output/exp_021_fewnerd_n8_seed123/samples.jsonl", "model": "Qwen3-8B", "dataset": "fewnerd"},
    "Qwen_FewNERD_s456": {"path": f"{BASE}/output/exp_021_fewnerd_n8_seed456/samples.jsonl", "model": "Qwen3-8B", "dataset": "fewnerd"},
    # LLaMA-3.1-8B-FT x SciERC
    "LLaMA_SciERC_s42": {"path": f"{BASE}/output/exp_007_llama_n16_r1024/samples.jsonl", "model": "LLaMA-8B", "dataset": "scierc"},
    "LLaMA_SciERC_s123": {"path": f"{BASE}/output/exp_018_llama_scierc_seed123/samples.jsonl", "model": "LLaMA-8B", "dataset": "scierc"},
    "LLaMA_SciERC_s456": {"path": f"{BASE}/output/exp_018_llama_scierc_seed456/samples.jsonl", "model": "LLaMA-8B", "dataset": "scierc"},
    # LLaMA-3.1-8B-FT x CoNLL
    "LLaMA_CoNLL_s42": {"path": f"{BASE}/output/exp_017_llama_conll_n16/samples.jsonl", "model": "LLaMA-8B", "dataset": "conll"},
    "LLaMA_CoNLL_s123": {"path": f"{BASE}/output/exp_017_llama_conll_n16_s123/samples.jsonl", "model": "LLaMA-8B", "dataset": "conll"},
    "LLaMA_CoNLL_s456": {"path": f"{BASE}/output/exp_017_llama_conll_n16_s456/samples.jsonl", "model": "LLaMA-8B", "dataset": "conll"},
    # LLaMA-3.1-8B-FT x FewNERD
    "LLaMA_FewNERD_s42": {"path": f"{BASE}/output/llama_fewnerd_s42/samples.jsonl", "model": "LLaMA-8B", "dataset": "fewnerd"},
    "LLaMA_FewNERD_s123": {"path": f"{BASE}/output/llama_fewnerd_s123/samples.jsonl", "model": "LLaMA-8B", "dataset": "fewnerd"},
    "LLaMA_FewNERD_s456": {"path": f"{BASE}/output/llama_fewnerd_s456/samples.jsonl", "model": "LLaMA-8B", "dataset": "fewnerd"},
}

DATASET_MAP = {"scierc": 0, "conll": 1, "fewnerd": 2}
MODEL_MAP = {"Qwen3-8B": 0, "LLaMA-8B": 1}

# ---- helpers ----

def entity_set(entities):
    return {(e["start"], e["end"], e["type"]) for e in entities}

def load_data(path):
    instances = []
    with open(path) as f:
        for line in f:
            if not line.strip():
                continue
            obj = json.loads(line)
            if not obj["gold"].get("entities", []):
                continue
            instances.append(obj)
    return instances

def micro_f1(tp, fp, fn):
    if tp == 0:
        return 0.0
    p = tp / (tp + fp)
    r = tp / (tp + fn)
    return 2 * p * r / (p + r)

def compute_f1_at_theta(instances, theta, n=N_USE):
    """Compute entity-level micro F1 at a given theta using majority vote."""
    total_tp, total_fp, total_fn = 0, 0, 0
    for inst in instances:
        samples = inst["samples"][:n]
        gold = entity_set(inst["gold"]["entities"])
        entity_counts = Counter()
        for s in samples:
            seen = set()
            for e in s.get("entities", []):
                key = (e["start"], e["end"], e["type"])
                if key not in seen:
                    entity_counts[key] += 1
                    seen.add(key)
        pred = set()
        for key, count in entity_counts.items():
            if count / n >= theta:
                pred.add(key)
        tp = len(pred & gold)
        fp = len(pred - gold)
        fn = len(gold - pred)
        total_tp += tp
        total_fp += fp
        total_fn += fn
    return micro_f1(total_tp, total_fp, total_fn)

def compute_features(instances, n=N_USE):
    """Compute per-config features from instances."""
    # degeneracy_level: fraction of instances where all N samples produce identical entity sets
    n_degen = 0
    all_agreement_ratios = []
    all_n_unique = []
    all_lp_vars = []

    for inst in instances:
        samples = inst["samples"][:n]

        # Entity sets per sample
        esets = [frozenset((e["start"], e["end"], e["type"]) for e in s.get("entities", []))
                 for s in samples]
        if len(set(esets)) == 1:
            n_degen += 1

        # Agreement: for each unique entity, what fraction of samples contain it
        entity_counts = Counter()
        for es in esets:
            for e in es:
                entity_counts[e] += 1
        if entity_counts:
            agreements = [c / n for c in entity_counts.values()]
            all_agreement_ratios.extend(agreements)

        # Unique entities per instance
        all_entities = set()
        for es in esets:
            all_entities.update(es)
        all_n_unique.append(len(all_entities))

        # LP variance across samples
        logprobs_list = inst.get("logprobs", None)
        lps = []
        for i, s in enumerate(samples):
            lp = s.get("mean_logprob", None)
            if lp is None and logprobs_list is not None and i < len(logprobs_list):
                lp = logprobs_list[i]
            if lp is not None and math.isfinite(lp):
                lps.append(lp)
        if len(lps) >= 2:
            all_lp_vars.append(np.var(lps))

    degeneracy_level = n_degen / len(instances)
    lp_variance = float(np.mean(all_lp_vars)) if all_lp_vars else 0.0
    agreement_mean = float(np.mean(all_agreement_ratios)) if all_agreement_ratios else 0.0
    n_unique_entities = float(np.mean(all_n_unique)) if all_n_unique else 0.0

    return {
        "degeneracy_level": degeneracy_level,
        "lp_variance": lp_variance,
        "sample_count_N": n,
        "agreement_mean": agreement_mean,
        "n_unique_entities": n_unique_entities,
    }

# ---- main ----

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    t_start = time.time()

    # Step 1-3: Load data, compute F1 at each theta, extract features
    config_data = {}
    print("=" * 70)
    print("Step 1-3: Loading data, computing F1 grid, extracting features")
    print("=" * 70)

    for cfg_name, cfg in CONFIGS.items():
        if not os.path.exists(cfg["path"]):
            print(f"  SKIP {cfg_name}: file not found")
            continue

        t0 = time.time()
        instances = load_data(cfg["path"])
        n_avail = len(instances[0]["samples"])
        n_use = min(N_USE, n_avail)
        print(f"  {cfg_name}: {len(instances)} instances, N_avail={n_avail}, using N={n_use}", end="", flush=True)

        # F1 at each theta
        f1_by_theta = {}
        for theta in THETA_GRID:
            f1 = compute_f1_at_theta(instances, theta, n=n_use)
            f1_by_theta[theta] = f1

        # Oracle theta
        oracle_theta = max(THETA_GRID, key=lambda t: f1_by_theta[t])
        oracle_f1 = f1_by_theta[oracle_theta]
        fixed_f1 = f1_by_theta[0.5]

        # Features
        features = compute_features(instances, n=n_use)
        features["dataset_id"] = DATASET_MAP[cfg["dataset"]]
        features["model_id"] = MODEL_MAP[cfg["model"]]

        config_data[cfg_name] = {
            "cfg": cfg,
            "n_instances": len(instances),
            "n_use": n_use,
            "f1_by_theta": {str(t): f for t, f in f1_by_theta.items()},
            "oracle_theta": oracle_theta,
            "oracle_f1": oracle_f1,
            "fixed_f1_05": fixed_f1,
            "features": features,
        }

        elapsed = time.time() - t0
        print(f"  oracle_θ={oracle_theta}, F1={oracle_f1:.4f}, fixed@0.5={fixed_f1:.4f} ({elapsed:.1f}s)")

    print(f"\nLoaded {len(config_data)} configs in {time.time()-t_start:.1f}s\n")

    # Print F1 grid
    print("F1 Grid (config × theta):")
    print(f"  {'Config':<25}", end="")
    for t in THETA_GRID:
        print(f"  {t:.2f}", end="")
    print("  oracle")
    print("  " + "-" * 100)
    for cfg_name, cd in config_data.items():
        print(f"  {cfg_name:<25}", end="")
        for t in THETA_GRID:
            f1 = cd["f1_by_theta"][str(t)]
            marker = " *" if t == cd["oracle_theta"] else "  "
            print(f" {f1:.4f}{marker[0]}", end="")
        print(f"  {cd['oracle_theta']:.2f}")

    # Print features
    print(f"\nFeatures per config:")
    feat_names = ["degeneracy_level", "lp_variance", "sample_count_N", "dataset_id", "model_id", "agreement_mean", "n_unique_entities"]
    print(f"  {'Config':<25}", end="")
    for fn in feat_names:
        print(f"  {fn[:12]:>12}", end="")
    print()
    for cfg_name, cd in config_data.items():
        print(f"  {cfg_name:<25}", end="")
        for fn in feat_names:
            v = cd["features"][fn]
            print(f"  {v:>12.4f}", end="")
        print()

    # Step 4: MLP Training (Leave-One-Config-Out)
    print("\n" + "=" * 70)
    print("Step 4: MLP Training (Leave-One-Config-Out CV)")
    print("=" * 70)

    from sklearn.neural_network import MLPRegressor
    from sklearn.preprocessing import StandardScaler

    cfg_names = sorted(config_data.keys())
    n_cfgs = len(cfg_names)

    # Build feature matrix and target
    X_all = []
    y_all = []  # continuous oracle theta
    for cn in cfg_names:
        cd = config_data[cn]
        feat = cd["features"]
        X_all.append([feat[fn] for fn in feat_names])
        y_all.append(cd["oracle_theta"])

    X_all = np.array(X_all)
    y_all = np.array(y_all)

    print(f"  X shape: {X_all.shape}, y values: {sorted(set(y_all.tolist()))}")

    # LOCO CV
    predictions = {}
    for i, test_cfg in enumerate(cfg_names):
        train_idx = [j for j in range(n_cfgs) if j != i]
        test_idx = [i]

        X_train = X_all[train_idx]
        y_train = y_all[train_idx]
        X_test = X_all[test_idx]

        scaler = StandardScaler()
        X_train_s = scaler.fit_transform(X_train)
        X_test_s = scaler.transform(X_test)

        mlp = MLPRegressor(
            hidden_layer_sizes=(64,),
            activation='relu',
            max_iter=2000,
            random_state=42,
            early_stopping=True,
            validation_fraction=0.15,
            n_iter_no_change=50,
            learning_rate_init=0.001,
        )
        mlp.fit(X_train_s, y_train)

        pred_theta_cont = mlp.predict(X_test_s)[0]
        # Round to nearest grid point
        pred_theta = min(THETA_GRID, key=lambda t: abs(t - pred_theta_cont))

        cd = config_data[test_cfg]
        pred_f1 = cd["f1_by_theta"][str(pred_theta)]
        oracle_f1 = cd["oracle_f1"]
        fixed_f1 = cd["fixed_f1_05"]

        predictions[test_cfg] = {
            "pred_theta_raw": float(pred_theta_cont),
            "pred_theta": pred_theta,
            "oracle_theta": cd["oracle_theta"],
            "pred_f1": pred_f1,
            "oracle_f1": oracle_f1,
            "fixed_f1_05": fixed_f1,
        }

        print(f"  [{i+1:2d}/{n_cfgs}] {test_cfg:<25} pred_θ={pred_theta:.2f} (raw={pred_theta_cont:.3f}), "
              f"oracle_θ={cd['oracle_theta']:.2f}, "
              f"F1: pred={pred_f1:.4f}, oracle={oracle_f1:.4f}, fixed@0.5={fixed_f1:.4f}")

    # Step 5: Evaluation
    print("\n" + "=" * 70)
    print("Step 5: Evaluation Summary")
    print("=" * 70)

    # Per-config F1 comparison
    adaptive_f1s = []
    fixed_f1s = []
    oracle_f1s = []
    for cn in cfg_names:
        p = predictions[cn]
        adaptive_f1s.append(p["pred_f1"])
        fixed_f1s.append(p["fixed_f1_05"])
        oracle_f1s.append(p["oracle_f1"])

    adaptive_f1s = np.array(adaptive_f1s)
    fixed_f1s = np.array(fixed_f1s)
    oracle_f1s = np.array(oracle_f1s)

    print(f"\n  Mean F1 across {n_cfgs} configs:")
    print(f"    Fixed θ=0.5:   {fixed_f1s.mean():.4f} (std={fixed_f1s.std():.4f})")
    print(f"    Adaptive MLP:  {adaptive_f1s.mean():.4f} (std={adaptive_f1s.std():.4f})")
    print(f"    Oracle θ:      {oracle_f1s.mean():.4f} (std={oracle_f1s.std():.4f})")
    print(f"    Δ(MLP-Fixed):  {(adaptive_f1s - fixed_f1s).mean():+.4f}")
    print(f"    Δ(Oracle-Fixed): {(oracle_f1s - fixed_f1s).mean():+.4f}")
    print(f"    Gap closed:    {np.mean([(a - f) / (o - f) * 100 if abs(o - f) >= 1e-3 else 0.0 for a, f, o in zip(adaptive_f1s, fixed_f1s, oracle_f1s)]):.1f}%")

    # Theta prediction accuracy
    theta_exact = sum(1 for cn in cfg_names if predictions[cn]["pred_theta"] == predictions[cn]["oracle_theta"])
    theta_within_005 = sum(1 for cn in cfg_names if abs(predictions[cn]["pred_theta"] - predictions[cn]["oracle_theta"]) <= 0.05)
    theta_within_010 = sum(1 for cn in cfg_names if abs(predictions[cn]["pred_theta"] - predictions[cn]["oracle_theta"]) <= 0.10)

    print(f"\n  θ prediction accuracy:")
    print(f"    Exact match:   {theta_exact}/{n_cfgs} ({theta_exact/n_cfgs*100:.1f}%)")
    print(f"    Within ±0.05:  {theta_within_005}/{n_cfgs} ({theta_within_005/n_cfgs*100:.1f}%)")
    print(f"    Within ±0.10:  {theta_within_010}/{n_cfgs} ({theta_within_010/n_cfgs*100:.1f}%)")

    # Win/tie/loss vs fixed
    wins = sum(1 for i in range(n_cfgs) if adaptive_f1s[i] > fixed_f1s[i] + 1e-6)
    ties = sum(1 for i in range(n_cfgs) if abs(adaptive_f1s[i] - fixed_f1s[i]) <= 1e-6)
    losses = sum(1 for i in range(n_cfgs) if adaptive_f1s[i] < fixed_f1s[i] - 1e-6)
    print(f"\n  MLP vs Fixed θ=0.5: {wins}W/{ties}T/{losses}L")

    # Per-config detailed table
    print(f"\n  {'Config':<25} {'pred_θ':>7} {'oracle_θ':>8} {'F1_pred':>8} {'F1_fixed':>8} {'F1_oracle':>9} {'Δ':>6}")
    print("  " + "-" * 80)
    for cn in cfg_names:
        p = predictions[cn]
        delta = p["pred_f1"] - p["fixed_f1_05"]
        marker = "+" if delta > 1e-4 else ("-" if delta < -1e-4 else "=")
        print(f"  {cn:<25} {p['pred_theta']:>7.2f} {p['oracle_theta']:>8.2f} "
              f"{p['pred_f1']:>8.4f} {p['fixed_f1_05']:>8.4f} {p['oracle_f1']:>9.4f} {delta:>+6.4f} {marker}")

    # Save results
    results = {
        "experiment": "E_theta_v2_mlp",
        "description": "Full features + 2-layer MLP (hidden=64, ReLU) for adaptive theta prediction",
        "n_configs": n_cfgs,
        "n_samples_per_instance": N_USE,
        "theta_grid": THETA_GRID,
        "feature_names": feat_names,
        "model": "MLPRegressor(hidden=64, relu, StandardScaler, LOCO-CV)",
        "summary": {
            "mean_f1_fixed_05": float(fixed_f1s.mean()),
            "mean_f1_adaptive_mlp": float(adaptive_f1s.mean()),
            "mean_f1_oracle": float(oracle_f1s.mean()),
            "delta_mlp_minus_fixed": float((adaptive_f1s - fixed_f1s).mean()),
            "delta_oracle_minus_fixed": float((oracle_f1s - fixed_f1s).mean()),
            "gap_closed_pct": float(np.mean([(a - f) / (o - f) * 100 if abs(o - f) >= 1e-3 else 0.0 for a, f, o in zip(adaptive_f1s, fixed_f1s, oracle_f1s)])),
            "theta_exact_match": theta_exact,
            "theta_within_005": theta_within_005,
            "theta_within_010": theta_within_010,
            "win_tie_loss_vs_fixed": {"win": wins, "tie": ties, "loss": losses},
        },
        "per_config": {},
    }

    for cn in cfg_names:
        p = predictions[cn]
        cd = config_data[cn]
        results["per_config"][cn] = {
            "model": cd["cfg"]["model"],
            "dataset": cd["cfg"]["dataset"],
            "n_instances": cd["n_instances"],
            "features": cd["features"],
            "f1_by_theta": cd["f1_by_theta"],
            "oracle_theta": cd["oracle_theta"],
            "pred_theta_raw": p["pred_theta_raw"],
            "pred_theta": p["pred_theta"],
            "f1_pred": p["pred_f1"],
            "f1_fixed_05": p["fixed_f1_05"],
            "f1_oracle": p["oracle_f1"],
        }

    out_path = os.path.join(OUTPUT_DIR, "v2_mlp_results.json")
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved: {out_path}")

    print(f"\nTotal time: {time.time()-t_start:.1f}s")
    print("DONE")


if __name__ == "__main__":
    main()
