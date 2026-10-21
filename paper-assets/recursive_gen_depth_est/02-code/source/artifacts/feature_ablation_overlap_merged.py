"""Feature ablation: overlap-6 and merged-30 RF classifiers (4-class depth)."""
import json
import os
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold, cross_val_score

PROJECT_ROOT = "/root/autodl-tmp/recursive_gen_depth_est"

CELLS = {
    "pythia_nucleus": {
        "jsonl": f"{PROJECT_ROOT}/data/features_all.jsonl",
        "npz":   f"{PROJECT_ROOT}/results/pythia_nucleus_bino_features.npz",
    },
    "pythia_temp09": {
        "jsonl": f"{PROJECT_ROOT}/data/pythia_temp09/features.jsonl",
        "npz":   f"{PROJECT_ROOT}/results/pythia_temp09_bino_features.npz",
    },
    "pythia_topk50": {
        "jsonl": f"{PROJECT_ROOT}/results/pythia_topk50/features.jsonl",
        "npz":   f"{PROJECT_ROOT}/results/pythia_topk50_bino_features.npz",
    },
    "olmo_nucleus": {
        "jsonl": f"{PROJECT_ROOT}/data/olmo/features.jsonl",
        "npz":   f"{PROJECT_ROOT}/results/olmo_nucleus_bino_features.npz",
    },
    "olmo_temp09": {
        "jsonl": f"{PROJECT_ROOT}/results/olmo_temp09/features.jsonl",
        "npz":   f"{PROJECT_ROOT}/results/olmo_temp09_bino_features.npz",
    },
    "olmo_topk50": {
        "jsonl": f"{PROJECT_ROOT}/results/olmo_topk50/features.jsonl",
        "npz":   f"{PROJECT_ROOT}/results/olmo_topk50_bino_features.npz",
    },
    "gpt2xl_nucleus": {
        "jsonl": f"{PROJECT_ROOT}/data/gpt2xl/features.jsonl",
        "npz":   f"{PROJECT_ROOT}/results/gpt2xl_nucleus_bino_features.npz",
    },
    "gpt2xl_temp09": {
        "jsonl": f"{PROJECT_ROOT}/results/gpt2xl_temp09/features.jsonl",
        "npz":   f"{PROJECT_ROOT}/results/gpt2xl_temp09_bino_features.npz",
    },
    "gpt2xl_topk50": {
        "jsonl": f"{PROJECT_ROOT}/results/gpt2xl_topk50/features.jsonl",
        "npz":   f"{PROJECT_ROOT}/results/gpt2xl_topk50_bino_features.npz",
    },
}

FEAT_19 = [
    "mean_ppl", "var_ppl", "skewness_ppl", "kurtosis_ppl",
    "p10_ppl", "p25_ppl", "p50_ppl", "p75_ppl", "p90_ppl",
    "mean_surprisal", "var_surprisal", "entropy_of_surprisal",
    "type_token_ratio", "hapax_ratio",
    "bigram_entropy", "trigram_entropy",
    "rep_2gram", "rep_3gram", "rep_4gram",
]

OVERLAP_6 = ["mean_ppl", "var_ppl", "p50_ppl", "p10_ppl", "p90_ppl", "skewness_ppl"]

BINO_11 = [
    "bino_score", "ppl_mean", "ppl_var", "ppl_median", "ppl_p10",
    "ppl_p90", "ppl_skew", "xppl_mean", "xppl_var", "xppl_median",
    "bino_score_median",
]

MERGED_FEATURES = FEAT_19 + BINO_11


def load_jsonl_features(path, feature_names):
    X, y = [], []
    with open(path) as f:
        for line in f:
            row = json.loads(line)
            X.append([row[k] for k in feature_names])
            y.append(row["depth"])
    X = np.array(X, dtype=np.float64)
    y = np.array(y, dtype=np.int64)
    X = np.nan_to_num(X, nan=0.0, posinf=0.0, neginf=0.0)
    return X, y


def load_npz_features(path, feature_names):
    d = np.load(path)
    X = np.column_stack([d[k] for k in feature_names])
    y = d["labels"]
    X = np.nan_to_num(X, nan=0.0, posinf=0.0, neginf=0.0)
    return X, y


def run_rf_cv(X, y, n_estimators=200, random_state=42, n_splits=5):
    clf = RandomForestClassifier(n_estimators=n_estimators, random_state=random_state, n_jobs=-1)
    cv = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=random_state)
    scores = cross_val_score(clf, X, y, cv=cv, scoring="accuracy")
    return float(scores.mean()), float(scores.std()), scores.tolist()


def experiment_overlap(cell_name, cell_paths):
    X, y = load_jsonl_features(cell_paths["jsonl"], OVERLAP_6)
    mean_acc, std_acc, fold_scores = run_rf_cv(X, y)
    return {
        "cell": cell_name,
        "n_features": len(OVERLAP_6),
        "features": OVERLAP_6,
        "n_samples": len(y),
        "accuracy_mean": round(mean_acc, 4),
        "accuracy_std": round(std_acc, 4),
        "fold_scores": [round(s, 4) for s in fold_scores],
    }


def experiment_merged(cell_name, cell_paths):
    X_19, y_19 = load_jsonl_features(cell_paths["jsonl"], FEAT_19)
    X_bino, y_bino = load_npz_features(cell_paths["npz"], BINO_11)

    assert np.array_equal(y_19, y_bino), f"Label mismatch for {cell_name}"

    n = min(len(y_19), len(y_bino))
    X_merged = np.hstack([X_19[:n], X_bino[:n]])
    y = y_19[:n]

    mean_acc, std_acc, fold_scores = run_rf_cv(X_merged, y)
    return {
        "cell": cell_name,
        "n_features": len(MERGED_FEATURES),
        "features": MERGED_FEATURES,
        "n_samples": len(y),
        "accuracy_mean": round(mean_acc, 4),
        "accuracy_std": round(std_acc, 4),
        "fold_scores": [round(s, 4) for s in fold_scores],
    }


def run_all(experiment_fn, output_path):
    results = []
    for cell_name, cell_paths in CELLS.items():
        print(f"  {cell_name} ...", end=" ", flush=True)
        r = experiment_fn(cell_name, cell_paths)
        print(f"acc={r['accuracy_mean']:.4f} +/- {r['accuracy_std']:.4f}")
        results.append(r)

    mean_acc = np.mean([r["accuracy_mean"] for r in results])
    summary = {
        "experiment": os.path.basename(output_path).replace("_results.json", ""),
        "n_cells": len(results),
        "mean_accuracy_across_cells": round(float(mean_acc), 4),
        "per_cell": results,
    }

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(summary, f, indent=2)
    print(f"  Saved -> {output_path}")
    return summary


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["overlap", "merged", "both", "dry-run"], default="both")
    args = parser.parse_args()

    out_dir = f"{PROJECT_ROOT}/results/feature_ablation"

    if args.mode == "dry-run":
        cell_name = "pythia_nucleus"
        cell_paths = CELLS[cell_name]
        print("[dry-run] Overlap-6 on pythia_nucleus:")
        r = experiment_overlap(cell_name, cell_paths)
        print(f"  acc={r['accuracy_mean']:.4f} +/- {r['accuracy_std']:.4f}")
        print("[dry-run] Merged-30 on pythia_nucleus:")
        r = experiment_merged(cell_name, cell_paths)
        print(f"  acc={r['accuracy_mean']:.4f} +/- {r['accuracy_std']:.4f}")
        print("[dry-run] OK")

    if args.mode in ("overlap", "both"):
        print("\n=== Experiment A: Overlap 6-feature RF ===")
        run_all(experiment_overlap, f"{out_dir}/overlap_6feat_results.json")

    if args.mode in ("merged", "both"):
        print("\n=== Experiment B: Merged 30-feature RF ===")
        run_all(experiment_merged, f"{out_dir}/merged_30feat_results.json")
