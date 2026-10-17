"""W1 reviewer response: feature correlation matrix + permutation importance."""

import json
import numpy as np
import pandas as pd
from pathlib import Path
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold
from sklearn.inspection import permutation_importance
from scipy.stats import spearmanr

FEATURES = [
    "mean_ppl", "var_ppl", "skewness_ppl", "kurtosis_ppl",
    "p10_ppl", "p25_ppl", "p50_ppl", "p75_ppl", "p90_ppl",
    "mean_surprisal", "var_surprisal", "entropy_of_surprisal",
    "type_token_ratio", "hapax_ratio",
    "bigram_entropy", "trigram_entropy",
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

ROOT = Path("/root/autodl-tmp/recursive_gen_depth_est")


def load_cell(path):
    rows = []
    with open(path) as f:
        for line in f:
            rows.append(json.loads(line))
    df = pd.DataFrame(rows)
    X = df[FEATURES].values.astype(np.float64)
    X = np.nan_to_num(X, nan=0.0, posinf=np.finfo(np.float64).max / 10,
                      neginf=np.finfo(np.float64).min / 10)
    X = np.clip(X, -1e15, 1e15)
    y = df["depth"].values
    return X, y, df[FEATURES]


def part_a_correlation():
    """Compute 19x19 Pearson correlation on pythia_nucleus095 as representative."""
    _, _, df = load_cell(ROOT / CELLS["pythia_nucleus095"])
    corr = df.corr(method="pearson")

    high_pairs = []
    for i in range(len(FEATURES)):
        for j in range(i + 1, len(FEATURES)):
            r = corr.iloc[i, j]
            if abs(r) > 0.8:
                high_pairs.append({
                    "f1": FEATURES[i],
                    "f2": FEATURES[j],
                    "r": round(float(r), 4),
                })
    high_pairs.sort(key=lambda x: -abs(x["r"]))

    result = {
        "cell": "pythia_nucleus095",
        "correlation_matrix": {
            "features": FEATURES,
            "matrix": [[round(float(corr.iloc[i, j]), 4) for j in range(19)] for i in range(19)],
        },
        "high_corr_pairs_abs_gt_0.8": high_pairs,
        "num_high_corr_pairs": len(high_pairs),
    }
    return result


def part_b_permutation_importance():
    """5-fold CV permutation importance for all 9 cells."""
    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    all_results = {}

    for cell_name, rel_path in CELLS.items():
        X, y, _ = load_cell(ROOT / rel_path)
        n_features = X.shape[1]

        perm_imp_folds = np.zeros((5, n_features))
        gini_imp_folds = np.zeros((5, n_features))

        for fold_idx, (train_idx, test_idx) in enumerate(skf.split(X, y)):
            X_train, X_test = X[train_idx], X[test_idx]
            y_train, y_test = y[train_idx], y[test_idx]

            rf = RandomForestClassifier(n_estimators=200, random_state=42, n_jobs=-1)
            rf.fit(X_train, y_train)

            gini_imp_folds[fold_idx] = rf.feature_importances_

            perm_result = permutation_importance(
                rf, X_test, y_test,
                n_repeats=10, random_state=42, scoring="accuracy", n_jobs=-1,
            )
            perm_imp_folds[fold_idx] = perm_result.importances_mean

        mean_perm = perm_imp_folds.mean(axis=0)
        mean_gini = gini_imp_folds.mean(axis=0)

        perm_rank = np.argsort(-mean_perm)
        gini_rank = np.argsort(-mean_gini)

        perm_ranking = [(FEATURES[i], round(float(mean_perm[i]), 6)) for i in perm_rank]
        gini_ranking = [(FEATURES[i], round(float(mean_gini[i]), 6)) for i in gini_rank]

        perm_rank_arr = np.empty(n_features, dtype=int)
        gini_rank_arr = np.empty(n_features, dtype=int)
        for rank, idx in enumerate(perm_rank):
            perm_rank_arr[idx] = rank
        for rank, idx in enumerate(gini_rank):
            gini_rank_arr[idx] = rank

        rho, pval = spearmanr(perm_rank_arr, gini_rank_arr)

        perm_top5 = [FEATURES[i] for i in perm_rank[:5]]
        gini_top5 = [FEATURES[i] for i in gini_rank[:5]]

        p90_perm_rank = int(perm_rank_arr[FEATURES.index("p90_ppl")])
        var_surp_perm_rank = int(perm_rank_arr[FEATURES.index("var_surprisal")])
        p90_gini_rank = int(gini_rank_arr[FEATURES.index("p90_ppl")])
        var_surp_gini_rank = int(gini_rank_arr[FEATURES.index("var_surprisal")])

        all_results[cell_name] = {
            "permutation_importance_ranking": perm_ranking,
            "gini_importance_ranking": gini_ranking,
            "spearman_rho_perm_vs_gini": round(float(rho), 4),
            "spearman_pval": float(pval),
            "perm_top5": perm_top5,
            "gini_top5": gini_top5,
            "key_features": {
                "p90_ppl": {"perm_rank": p90_perm_rank, "gini_rank": p90_gini_rank},
                "var_surprisal": {"perm_rank": var_surp_perm_rank, "gini_rank": var_surp_gini_rank},
            },
        }
        print(f"  {cell_name}: spearman={rho:.4f}, perm_top5={perm_top5}")

    return all_results


def summarize(perm_results):
    """Print summary statistics."""
    p90_perm_top2 = 0
    var_surp_perm_top2 = 0
    p90_gini_top2 = 0
    var_surp_gini_top2 = 0

    for cell, res in perm_results.items():
        kf = res["key_features"]
        if kf["p90_ppl"]["perm_rank"] < 2:
            p90_perm_top2 += 1
        if kf["var_surprisal"]["perm_rank"] < 2:
            var_surp_perm_top2 += 1
        if kf["p90_ppl"]["gini_rank"] < 2:
            p90_gini_top2 += 1
        if kf["var_surprisal"]["gini_rank"] < 2:
            var_surp_gini_top2 += 1

    print(f"\n=== Summary ===")
    print(f"p90_ppl top-2 rate:      Gini={p90_gini_top2}/9, Perm={p90_perm_top2}/9")
    print(f"var_surprisal top-2 rate: Gini={var_surp_gini_top2}/9, Perm={var_surp_perm_top2}/9")

    rhos = [res["spearman_rho_perm_vs_gini"] for res in perm_results.values()]
    print(f"Spearman rho (Perm vs Gini): mean={np.mean(rhos):.4f}, min={np.min(rhos):.4f}, max={np.max(rhos):.4f}")

    return {
        "p90_ppl_top2": {"gini": f"{p90_gini_top2}/9", "perm": f"{p90_perm_top2}/9"},
        "var_surprisal_top2": {"gini": f"{var_surp_gini_top2}/9", "perm": f"{var_surp_perm_top2}/9"},
        "spearman_rho_mean": round(float(np.mean(rhos)), 4),
    }


if __name__ == "__main__":
    out_dir = ROOT / "results"
    out_dir.mkdir(exist_ok=True)

    print("=== Part A: Correlation Matrix ===")
    corr_result = part_a_correlation()
    print(f"High-corr pairs (|r|>0.8): {corr_result['num_high_corr_pairs']}")
    for p in corr_result["high_corr_pairs_abs_gt_0.8"]:
        print(f"  {p['f1']} <-> {p['f2']}: r={p['r']}")

    with open(out_dir / "w1_correlation_matrix.json", "w") as f:
        json.dump(corr_result, f, indent=2)
    print(f"Saved: {out_dir / 'w1_correlation_matrix.json'}")

    print("\n=== Part B: Permutation Importance (9 cells) ===")
    perm_results = part_b_permutation_importance()

    summary = summarize(perm_results)
    perm_results["_summary"] = summary

    with open(out_dir / "w1_permutation_importance_9cell.json", "w") as f:
        json.dump(perm_results, f, indent=2)
    print(f"Saved: {out_dir / 'w1_permutation_importance_9cell.json'}")
