# Feature ablation analysis across all 9 cells (3 models x 3 strategies).
# Sub-tasks: A) Top-k ablation, B) Per-category ablation, C) Forward selection, D) Correlation + VIF.
# RF params match existing pipeline: n_estimators=200, random_state=42, 5-fold stratified CV.

import json
import warnings
import numpy as np
import pandas as pd
from pathlib import Path
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold
from statsmodels.stats.outliers_influence import variance_inflation_factor

warnings.filterwarnings("ignore", category=RuntimeWarning)

ROOT = Path("/root/autodl-tmp/recursive_gen_depth_est")
OUT_DIR = ROOT / "results" / "feature_ablation"
OUT_DIR.mkdir(parents=True, exist_ok=True)

FEATURES = [
    "mean_ppl", "var_ppl", "skewness_ppl", "kurtosis_ppl",
    "p10_ppl", "p25_ppl", "p50_ppl", "p75_ppl", "p90_ppl",
    "mean_surprisal", "var_surprisal", "entropy_of_surprisal",
    "type_token_ratio", "hapax_ratio", "bigram_entropy", "trigram_entropy",
    "rep_2gram", "rep_3gram", "rep_4gram",
]

CELLS = {
    "pythia_nucleus095": "data/features_all.jsonl",
    "pythia_temp09": "data/pythia_temp09/features.jsonl",
    "pythia_topk50": "results/pythia_topk50/features.jsonl",
    "gpt2xl_nucleus095": "data/gpt2xl/features.jsonl",
    "gpt2xl_temp09": "results/gpt2xl_temp09/features.jsonl",
    "gpt2xl_topk50": "results/gpt2xl_topk50/features.jsonl",
    "olmo_nucleus095": "data/olmo/features.jsonl",
    "olmo_temp09": "results/olmo_temp09/features.jsonl",
    "olmo_topk50": "results/olmo_topk50/features.jsonl",
}

CATEGORIES = {
    "perplexity": ["mean_ppl", "var_ppl", "skewness_ppl", "kurtosis_ppl",
                   "p10_ppl", "p25_ppl", "p50_ppl", "p75_ppl", "p90_ppl"],
    "surprisal": ["mean_surprisal", "var_surprisal", "entropy_of_surprisal"],
    "lexical_diversity": ["type_token_ratio", "hapax_ratio"],
    "ngram_entropy": ["bigram_entropy", "trigram_entropy"],
    "repetition": ["rep_2gram", "rep_3gram", "rep_4gram"],
}

RF_PARAMS = dict(n_estimators=200, random_state=42, n_jobs=-1)
SKF = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)


def load_cell(rel_path):
    rows = []
    with open(ROOT / rel_path) as f:
        for line in f:
            if line.strip():
                rows.append(json.loads(line))
    df = pd.DataFrame(rows)
    X = df[FEATURES].values.astype(np.float64)
    X = np.nan_to_num(X, nan=0.0, posinf=1e15, neginf=-1e15)
    X = np.clip(X, -1e15, 1e15)
    y = df["depth"].values
    return X, y


def cv_accuracy(X, y, feature_indices=None):
    if feature_indices is not None:
        X_sub = X[:, feature_indices]
    else:
        X_sub = X
    if X_sub.shape[1] == 0:
        return 0.0, 0.0
    accs = []
    for train_idx, test_idx in SKF.split(X_sub, y):
        rf = RandomForestClassifier(**RF_PARAMS)
        rf.fit(X_sub[train_idx], y[train_idx])
        accs.append(rf.score(X_sub[test_idx], y[test_idx]))
    return float(np.mean(accs)), float(np.std(accs))


def load_perm_importance():
    path = ROOT / "results" / "w1_permutation_importance_9cell.json"
    with open(path) as f:
        data = json.load(f)
    rankings = {}
    for cell_name in CELLS:
        ranked_features = [item[0] for item in data[cell_name]["permutation_importance_ranking"]]
        rankings[cell_name] = ranked_features
    return rankings


# === Sub-task A: Top-k ablation ===
def run_topk_ablation(perm_rankings):
    print("=== Sub-task A: Top-k Ablation ===", flush=True)
    ks = [1, 2, 3, 5, 10, 15, 19]
    results = {}
    for cell_name, rel_path in CELLS.items():
        X, y = load_cell(rel_path)
        ranked = perm_rankings[cell_name]
        cell_results = {}
        for k in ks:
            top_features = ranked[:k]
            indices = [FEATURES.index(f) for f in top_features]
            acc_mean, acc_std = cv_accuracy(X, y, indices)
            cell_results[k] = {"acc_mean": round(acc_mean, 6), "acc_std": round(acc_std, 6),
                                "features": top_features}
        results[cell_name] = cell_results
        full_acc = cell_results[19]["acc_mean"]
        top5_acc = cell_results[5]["acc_mean"]
        print(f"  {cell_name}: full={full_acc:.4f}, top5={top5_acc:.4f}", flush=True)
    return results


# === Sub-task B: Per-category ablation ===
def run_category_ablation():
    print("\n=== Sub-task B: Per-category Ablation ===", flush=True)
    results = {}
    for cell_name, rel_path in CELLS.items():
        X, y = load_cell(rel_path)
        cell_results = {}
        for cat_name, cat_features in CATEGORIES.items():
            indices = [FEATURES.index(f) for f in cat_features]
            acc_mean, acc_std = cv_accuracy(X, y, indices)
            cell_results[cat_name] = {
                "acc_mean": round(acc_mean, 6), "acc_std": round(acc_std, 6),
                "features": cat_features, "n_features": len(cat_features),
            }
        results[cell_name] = cell_results
        best_cat = max(cell_results.items(), key=lambda x: x[1]["acc_mean"])
        print(f"  {cell_name}: best={best_cat[0]} ({best_cat[1]['acc_mean']:.4f})", flush=True)
    return results


# === Sub-task C: Forward feature selection ===
def run_forward_selection(perm_rankings):
    print("\n=== Sub-task C: Forward Feature Selection ===", flush=True)
    results = {}
    for cell_name, rel_path in CELLS.items():
        X, y = load_cell(rel_path)
        selected = []
        remaining = list(range(len(FEATURES)))
        steps = []
        for step in range(len(FEATURES)):
            best_acc = -1
            best_feat_idx = None
            for feat_idx in remaining:
                trial = selected + [feat_idx]
                acc_mean, _ = cv_accuracy(X, y, trial)
                if acc_mean > best_acc:
                    best_acc = acc_mean
                    best_feat_idx = feat_idx
            selected.append(best_feat_idx)
            remaining.remove(best_feat_idx)
            acc_mean, acc_std = cv_accuracy(X, y, selected)
            steps.append({
                "step": step + 1,
                "feature": FEATURES[best_feat_idx],
                "acc_mean": round(acc_mean, 6),
                "acc_std": round(acc_std, 6),
                "selected_features": [FEATURES[i] for i in selected],
            })
        results[cell_name] = steps
        n95 = next((s["step"] for s in steps if s["acc_mean"] >= 0.95 * steps[-1]["acc_mean"]), len(FEATURES))
        print(f"  {cell_name}: 95% of full at k={n95}, full={steps[-1]['acc_mean']:.4f}", flush=True)
    return results


# === Sub-task D: Correlation matrix + VIF ===
def run_correlation_vif():
    print("\n=== Sub-task D: Correlation Matrix + VIF ===", flush=True)
    X, _ = load_cell(CELLS["pythia_nucleus095"])
    df = pd.DataFrame(X, columns=FEATURES)

    corr = df.corr(method="pearson")
    corr.to_csv(OUT_DIR / "correlation_matrix.csv")
    print(f"  Saved correlation_matrix.csv ({corr.shape})", flush=True)

    from sklearn.preprocessing import StandardScaler
    X_scaled = StandardScaler().fit_transform(X)
    X_scaled_df = pd.DataFrame(X_scaled, columns=FEATURES)
    X_with_const = np.column_stack([np.ones(X_scaled.shape[0]), X_scaled])

    vif_data = {}
    for i, feat in enumerate(FEATURES):
        vif_val = variance_inflation_factor(X_with_const, i + 1)
        vif_data[feat] = round(float(vif_val), 4)
    print(f"  VIF range: {min(vif_data.values()):.1f} - {max(vif_data.values()):.1f}", flush=True)

    with open(OUT_DIR / "vif_table.json", "w") as f:
        json.dump(vif_data, f, indent=2)

    return corr, vif_data


# === Plotting ===
def plot_correlation_heatmap(corr):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(12, 10))
    im = ax.imshow(corr.values, cmap="RdBu_r", vmin=-1, vmax=1, aspect="equal")
    ax.set_xticks(range(len(FEATURES)))
    ax.set_yticks(range(len(FEATURES)))
    short_names = [f.replace("_ppl", "").replace("_surprisal", "_sur").replace("entropy_of_surprisal", "ent_sur")
                   .replace("type_token_ratio", "ttr").replace("hapax_ratio", "hapax")
                   .replace("bigram_entropy", "bi_ent").replace("trigram_entropy", "tri_ent") for f in FEATURES]
    ax.set_xticklabels(short_names, rotation=45, ha="right", fontsize=8)
    ax.set_yticklabels(short_names, fontsize=8)
    cbar = fig.colorbar(im, ax=ax, shrink=0.8)
    cbar.set_label("Pearson r", fontsize=10)
    ax.set_title("Feature Correlation Matrix (19 features)", fontsize=12)
    fig.tight_layout()
    fig.savefig(OUT_DIR / "correlation_heatmap.pdf", dpi=150, bbox_inches="tight")
    fig.savefig(OUT_DIR / "correlation_heatmap.png", dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved correlation_heatmap.pdf/png", flush=True)


def plot_forward_selection(fwd_results):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(10, 6))
    all_accs = []
    for cell_name, steps in fwd_results.items():
        ks = [s["step"] for s in steps]
        accs = [s["acc_mean"] for s in steps]
        all_accs.append(accs)
        ax.plot(ks, accs, alpha=0.4, linewidth=1, label=cell_name)

    mean_accs = np.mean(all_accs, axis=0)
    ax.plot(range(1, 20), mean_accs, color="black", linewidth=2.5, label="Mean", zorder=10)
    ax.set_xlabel("Number of Features", fontsize=12)
    ax.set_ylabel("4-class Accuracy (5-fold CV)", fontsize=12)
    ax.set_title("Forward Feature Selection (9 cells)", fontsize=12)
    ax.set_xticks(range(1, 20, 2))
    ax.legend(fontsize=7, ncol=2, loc="lower right")
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(OUT_DIR / "forward_selection_curve.pdf", dpi=150, bbox_inches="tight")
    fig.savefig(OUT_DIR / "forward_selection_curve.png", dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved forward_selection_curve.pdf/png", flush=True)


# === Summary ===
def build_summary(topk_results, category_results, fwd_results):
    summary = {}

    # Top-k stats across 9 cells
    for k in [2, 5]:
        accs = [topk_results[c][k]["acc_mean"] for c in CELLS]
        summary[f"topk_{k}_mean_acc"] = round(float(np.mean(accs)), 6)
        summary[f"topk_{k}_std_acc"] = round(float(np.std(accs)), 6)

    # Full model baseline
    full_accs = [topk_results[c][19]["acc_mean"] for c in CELLS]
    summary["full_19_mean_acc"] = round(float(np.mean(full_accs)), 6)
    summary["full_19_std_acc"] = round(float(np.std(full_accs)), 6)

    # Features needed for 95% of full performance (per cell)
    n95_list = []
    for cell_name in CELLS:
        full_acc = topk_results[cell_name][19]["acc_mean"]
        threshold = 0.95 * full_acc
        for k in [1, 2, 3, 5, 10, 15, 19]:
            if topk_results[cell_name][k]["acc_mean"] >= threshold:
                n95_list.append(k)
                break
    summary["n_features_95pct_full"] = {
        "per_cell": {cell: n for cell, n in zip(CELLS.keys(), n95_list)},
        "mean": round(float(np.mean(n95_list)), 1),
        "max": int(np.max(n95_list)),
    }

    # Best category per cell
    best_cats = {}
    for cell_name in CELLS:
        best = max(category_results[cell_name].items(), key=lambda x: x[1]["acc_mean"])
        best_cats[cell_name] = best[0]
    summary["best_category_per_cell"] = best_cats

    # Category mean across cells
    cat_means = {}
    for cat in CATEGORIES:
        accs = [category_results[c][cat]["acc_mean"] for c in CELLS]
        cat_means[cat] = {"mean": round(float(np.mean(accs)), 6), "std": round(float(np.std(accs)), 6)}
    summary["category_mean_accuracy"] = cat_means

    # Forward selection: first feature chosen across cells
    first_features = {}
    for cell_name in CELLS:
        first_features[cell_name] = fwd_results[cell_name][0]["feature"]
    summary["forward_selection_first_feature"] = first_features

    return summary


if __name__ == "__main__":
    import time
    t0 = time.time()

    perm_rankings = load_perm_importance()

    # A: Top-k ablation
    topk_results = run_topk_ablation(perm_rankings)
    with open(OUT_DIR / "topk_ablation.json", "w") as f:
        json.dump(topk_results, f, indent=2)
    print(f"  Saved topk_ablation.json ({time.time()-t0:.0f}s elapsed)", flush=True)

    # B: Category ablation
    category_results = run_category_ablation()
    with open(OUT_DIR / "category_ablation.json", "w") as f:
        json.dump(category_results, f, indent=2)
    print(f"  Saved category_ablation.json ({time.time()-t0:.0f}s elapsed)", flush=True)

    # C: Forward selection
    fwd_results = run_forward_selection(perm_rankings)
    with open(OUT_DIR / "forward_selection.json", "w") as f:
        json.dump(fwd_results, f, indent=2)
    print(f"  Saved forward_selection.json ({time.time()-t0:.0f}s elapsed)", flush=True)

    # D: Correlation + VIF
    corr, vif_data = run_correlation_vif()
    print(f"  Saved correlation + VIF ({time.time()-t0:.0f}s elapsed)", flush=True)

    # Summary
    summary = build_summary(topk_results, category_results, fwd_results)
    with open(OUT_DIR / "summary.json", "w") as f:
        json.dump(summary, f, indent=2)

    # Plots
    print("\n=== Generating Plots ===", flush=True)
    plot_correlation_heatmap(corr)
    plot_forward_selection(fwd_results)

    elapsed = time.time() - t0
    print(f"\nAll done in {elapsed:.0f}s. Results in {OUT_DIR}", flush=True)
