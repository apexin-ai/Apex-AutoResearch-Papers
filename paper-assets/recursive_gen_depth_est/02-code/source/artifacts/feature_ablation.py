"""
Feature ablation study for R3-N2 reviewer response.

Input:  9 cell feature files (JSONL, 19 features each with depth + sample_id)
Output: results/feature_ablation/
  - top_k_ablation.json       : top-k feature subset accuracy (k=1,2,3,5,10,15,19)
  - per_category_ablation.json: per-category and leave-one-category-out accuracy
  - forward_selection.json    : greedy forward selection path
  - vif.json                  : variance inflation factors
  - correlation_matrix.json   : 19x19 Pearson correlation matrix

RF: n_estimators=100, random_state=42, 5-fold stratified CV
"""

import json
import os
import sys
import numpy as np
from collections import OrderedDict

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold
from sklearn.inspection import permutation_importance
from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.preprocessing import StandardScaler

# ── Feature schema (matches extract_features.py / baselines.py) ──

FEATURE_NAMES = [
    "mean_ppl", "var_ppl", "skewness_ppl", "kurtosis_ppl",
    "p10_ppl", "p25_ppl", "p50_ppl", "p75_ppl", "p90_ppl",
    "mean_surprisal", "var_surprisal", "entropy_of_surprisal",
    "type_token_ratio", "hapax_ratio", "bigram_entropy", "trigram_entropy",
    "rep_2gram", "rep_3gram", "rep_4gram",
]

CELLS = {
    'pythia_nucleus':  'data/features_all.jsonl',
    'pythia_temp09':   'data/pythia_temp09/features.jsonl',
    'pythia_topk50':   'results/pythia_topk50/features.jsonl',
    'olmo_nucleus':    'data/olmo/features.jsonl',
    'olmo_temp09':     'results/olmo_temp09/features.jsonl',
    'olmo_topk50':     'results/olmo_topk50/features.jsonl',
    'gpt2xl_nucleus':  'data/gpt2xl/features.jsonl',
    'gpt2xl_temp09':   'results/gpt2xl_temp09/features.jsonl',
    'gpt2xl_topk50':   'results/gpt2xl_topk50/features.jsonl',
}

FEATURE_CATEGORIES = OrderedDict({
    "perplexity": ["mean_ppl", "var_ppl", "skewness_ppl", "kurtosis_ppl",
                   "p10_ppl", "p25_ppl", "p50_ppl", "p75_ppl", "p90_ppl"],
    "surprisal":  ["mean_surprisal", "var_surprisal", "entropy_of_surprisal"],
    "lexical":    ["type_token_ratio", "hapax_ratio"],
    "ngram_entropy": ["bigram_entropy", "trigram_entropy"],
    "repetition": ["rep_2gram", "rep_3gram", "rep_4gram"],
})

SEED = 42
N_FOLDS = 5
N_ESTIMATORS = 100
TOP_K_VALUES = [1, 2, 3, 5, 10, 15, 19]

BASE_DIR = '/root/autodl-tmp/recursive_gen_depth_est'
OUT_DIR = os.path.join(BASE_DIR, 'results', 'feature_ablation')


def load_features(path):
    records = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            records.append(json.loads(line))
    X = np.array([[r[k] for k in FEATURE_NAMES] for r in records], dtype=np.float64)
    y = np.array([r["depth"] for r in records], dtype=np.int64)
    X = np.nan_to_num(X, nan=0.0, posinf=0.0, neginf=0.0)
    return X, y


def cv_accuracy(X, y, feature_indices, seed=SEED, n_folds=N_FOLDS):
    """5-fold stratified CV accuracy with given feature subset."""
    if len(feature_indices) == 0:
        return 0.0, 0.0
    X_sub = X[:, feature_indices]
    skf = StratifiedKFold(n_splits=n_folds, shuffle=True, random_state=seed)
    accs = []
    for train_idx, test_idx in skf.split(X_sub, y):
        rf = RandomForestClassifier(n_estimators=N_ESTIMATORS, random_state=seed, n_jobs=4)
        rf.fit(X_sub[train_idx], y[train_idx])
        accs.append(rf.score(X_sub[test_idx], y[test_idx]))
    return float(np.mean(accs)), float(np.std(accs))


def get_permutation_importance_ranking(X, y, seed=SEED):
    """Train RF on all features; return feature indices sorted by permutation importance (desc)."""
    rf = RandomForestClassifier(n_estimators=N_ESTIMATORS, random_state=seed, n_jobs=4)
    rf.fit(X, y)
    result = permutation_importance(rf, X, y, n_repeats=10, random_state=seed, n_jobs=4)
    ranking = np.argsort(result.importances_mean)[::-1]
    return ranking, result.importances_mean


# ── 1. Top-k ablation ──

def run_top_k_ablation(X, y, cell_name):
    print(f"  [top-k] {cell_name}: computing permutation importance...", flush=True)
    ranking, imp_values = get_permutation_importance_ranking(X, y)

    results = {
        "feature_ranking": [[FEATURE_NAMES[i], float(imp_values[i])] for i in ranking],
        "top_k": {}
    }
    for k in TOP_K_VALUES:
        indices = ranking[:k].tolist()
        acc_mean, acc_std = cv_accuracy(X, y, indices)
        feat_names = [FEATURE_NAMES[i] for i in indices]
        results["top_k"][str(k)] = {
            "accuracy_mean": round(acc_mean, 4),
            "accuracy_std": round(acc_std, 4),
            "features": feat_names,
        }
        print(f"    top-{k:2d}: {acc_mean:.4f} ± {acc_std:.4f}", flush=True)
    return results


# ── 2. Per-category ablation ──

def run_per_category_ablation(X, y, cell_name):
    print(f"  [category] {cell_name}", flush=True)
    results = {"single_category": {}, "leave_one_out": {}}

    for cat_name, cat_feats in FEATURE_CATEGORIES.items():
        indices = [FEATURE_NAMES.index(f) for f in cat_feats]
        acc_mean, acc_std = cv_accuracy(X, y, indices)
        results["single_category"][cat_name] = {
            "accuracy_mean": round(acc_mean, 4),
            "accuracy_std": round(acc_std, 4),
            "n_features": len(indices),
            "features": cat_feats,
        }
        print(f"    {cat_name} only ({len(indices)}): {acc_mean:.4f} ± {acc_std:.4f}", flush=True)

    all_indices = list(range(len(FEATURE_NAMES)))
    for cat_name, cat_feats in FEATURE_CATEGORIES.items():
        drop_indices = [FEATURE_NAMES.index(f) for f in cat_feats]
        keep_indices = [i for i in all_indices if i not in drop_indices]
        acc_mean, acc_std = cv_accuracy(X, y, keep_indices)
        results["leave_one_out"][cat_name] = {
            "accuracy_mean": round(acc_mean, 4),
            "accuracy_std": round(acc_std, 4),
            "n_features_kept": len(keep_indices),
            "dropped_features": cat_feats,
        }
        print(f"    w/o {cat_name} ({len(keep_indices)} feats): {acc_mean:.4f} ± {acc_std:.4f}", flush=True)

    return results


# ── 3. Forward selection ──

def run_forward_selection(X, y, cell_name):
    print(f"  [forward] {cell_name}", flush=True)
    remaining = list(range(len(FEATURE_NAMES)))
    selected = []
    path = []

    for step in range(len(FEATURE_NAMES)):
        best_feat = None
        best_acc = -1.0
        best_std = 0.0

        for f_idx in remaining:
            candidate = selected + [f_idx]
            acc_mean, acc_std = cv_accuracy(X, y, candidate)
            if acc_mean > best_acc:
                best_acc = acc_mean
                best_std = acc_std
                best_feat = f_idx

        selected.append(best_feat)
        remaining.remove(best_feat)
        path.append({
            "step": step + 1,
            "added_feature": FEATURE_NAMES[best_feat],
            "accuracy_mean": round(best_acc, 4),
            "accuracy_std": round(best_std, 4),
            "features": [FEATURE_NAMES[i] for i in selected],
        })
        print(f"    step {step+1:2d}: +{FEATURE_NAMES[best_feat]:25s} -> {best_acc:.4f} ± {best_std:.4f}", flush=True)

    return {"path": path}


# ── 4. VIF ──

def run_vif(X, cell_name):
    print(f"  [VIF] {cell_name}", flush=True)
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    X_scaled = np.nan_to_num(X_scaled, nan=0.0, posinf=0.0, neginf=0.0)

    vif_values = {}
    for i in range(X_scaled.shape[1]):
        try:
            v = variance_inflation_factor(X_scaled, i)
            vif_values[FEATURE_NAMES[i]] = round(float(v), 2)
        except Exception:
            vif_values[FEATURE_NAMES[i]] = None

    high_vif = {k: v for k, v in vif_values.items() if v is not None and v > 10}
    print(f"    Features with VIF > 10: {len(high_vif)}/{len(FEATURE_NAMES)}", flush=True)
    for k, v in sorted(high_vif.items(), key=lambda x: -x[1]):
        print(f"      {k}: {v}", flush=True)
    return {"vif": vif_values, "high_vif_count": len(high_vif)}


# ── 5. Correlation matrix ──

def run_correlation_matrix(X, cell_name):
    print(f"  [corr] {cell_name}", flush=True)
    corr = np.corrcoef(X.T)
    corr = np.nan_to_num(corr, nan=0.0)
    corr_dict = {}
    for i in range(len(FEATURE_NAMES)):
        corr_dict[FEATURE_NAMES[i]] = {
            FEATURE_NAMES[j]: round(float(corr[i, j]), 4) for j in range(len(FEATURE_NAMES))
        }

    high_pairs = []
    for i in range(len(FEATURE_NAMES)):
        for j in range(i + 1, len(FEATURE_NAMES)):
            r = abs(corr[i, j])
            if r > 0.8:
                high_pairs.append({
                    "f1": FEATURE_NAMES[i], "f2": FEATURE_NAMES[j],
                    "pearson_r": round(float(corr[i, j]), 4)
                })
    high_pairs.sort(key=lambda x: -abs(x["pearson_r"]))
    print(f"    Pairs with |r| > 0.8: {len(high_pairs)}", flush=True)
    for p in high_pairs[:5]:
        print(f"      {p['f1']} <-> {p['f2']}: {p['pearson_r']:.4f}", flush=True)
    return {"matrix": corr_dict, "high_correlation_pairs": high_pairs}


# ── Main ──

def save_json(data, name):
    path = os.path.join(OUT_DIR, name)
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"Saved: {path}", flush=True)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)

    all_topk = {}
    all_category = {}
    all_forward = {}
    all_vif = {}
    all_corr = {}

    for cell_name, rel_path in CELLS.items():
        full_path = os.path.join(BASE_DIR, rel_path)
        print(f"\n{'='*60}")
        print(f"  Cell: {cell_name}")
        print(f"  Path: {full_path}")
        print(f"{'='*60}", flush=True)

        X, y = load_features(full_path)
        print(f"  Loaded: {X.shape[0]} samples, {X.shape[1]} features")
        print(f"  Depths: {dict(zip(*np.unique(y, return_counts=True)))}", flush=True)

        all_topk[cell_name] = run_top_k_ablation(X, y, cell_name)
        all_category[cell_name] = run_per_category_ablation(X, y, cell_name)
        all_forward[cell_name] = run_forward_selection(X, y, cell_name)
        all_vif[cell_name] = run_vif(X, cell_name)
        all_corr[cell_name] = run_correlation_matrix(X, cell_name)

        save_json(all_topk, "top_k_ablation.json")
        save_json(all_category, "per_category_ablation.json")
        save_json(all_forward, "forward_selection.json")
        save_json(all_vif, "vif.json")
        save_json(all_corr, "correlation_matrix.json")
        print(f"  [checkpoint] {cell_name} done, results saved.", flush=True)

    # ── Summary ──
    print(f"\n{'='*80}")
    print("  SUMMARY")
    print(f"{'='*80}")

    print("\n  Top-k ablation (accuracy across 9 cells):")
    print(f"  {'Cell':<20s}", end="")
    for k in TOP_K_VALUES:
        print(f"  k={k:<3d}", end="")
    print()
    for cell_name in CELLS:
        print(f"  {cell_name:<20s}", end="")
        for k in TOP_K_VALUES:
            acc = all_topk[cell_name]["top_k"][str(k)]["accuracy_mean"]
            print(f"  {acc:.3f}", end="")
        print()

    # Mean across cells
    print(f"  {'MEAN':<20s}", end="")
    for k in TOP_K_VALUES:
        accs = [all_topk[c]["top_k"][str(k)]["accuracy_mean"] for c in CELLS]
        print(f"  {np.mean(accs):.3f}", end="")
    print()

    print("\n  Per-category (single category, mean across 9 cells):")
    for cat_name in FEATURE_CATEGORIES:
        accs = [all_category[c]["single_category"][cat_name]["accuracy_mean"] for c in CELLS]
        n = len(FEATURE_CATEGORIES[cat_name])
        print(f"    {cat_name:<16s} ({n} feats): {np.mean(accs):.4f} ± {np.std(accs):.4f}")

    print("\n  Leave-one-category-out (mean across 9 cells):")
    for cat_name in FEATURE_CATEGORIES:
        accs = [all_category[c]["leave_one_out"][cat_name]["accuracy_mean"] for c in CELLS]
        n_drop = len(FEATURE_CATEGORIES[cat_name])
        print(f"    w/o {cat_name:<16s} (-{n_drop}): {np.mean(accs):.4f} ± {np.std(accs):.4f}")

    # Effective dimensions: find smallest k where mean acc >= 95% of k=19 acc
    accs_19 = [all_topk[c]["top_k"]["19"]["accuracy_mean"] for c in CELLS]
    mean_19 = np.mean(accs_19)
    threshold = mean_19 * 0.95
    eff_k = 19
    for k in TOP_K_VALUES:
        accs_k = [all_topk[c]["top_k"][str(k)]["accuracy_mean"] for c in CELLS]
        if np.mean(accs_k) >= threshold:
            eff_k = k
            break
    print(f"\n  Effective independent dimensions (95% of full acc): {eff_k}")
    print(f"  Full acc (19 feats, mean): {mean_19:.4f}")
    print(f"  95% threshold: {threshold:.4f}")

    # Forward selection saturation point
    print("\n  Forward selection saturation (first step reaching 95% of full):")
    for cell_name in CELLS:
        full_acc = all_topk[cell_name]["top_k"]["19"]["accuracy_mean"]
        thresh = full_acc * 0.95
        sat = 19
        for entry in all_forward[cell_name]["path"]:
            if entry["accuracy_mean"] >= thresh:
                sat = entry["step"]
                break
        print(f"    {cell_name:<20s}: step {sat} ({all_forward[cell_name]['path'][sat-1]['added_feature']})")

    print("\nDONE")


if __name__ == "__main__":
    main()
