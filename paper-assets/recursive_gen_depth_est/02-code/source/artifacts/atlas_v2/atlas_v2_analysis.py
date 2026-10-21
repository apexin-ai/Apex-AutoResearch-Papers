# Atlas v2 full 9-cell analysis — feature importance, monotonicity, EDD, cross-comparison
import json
import os
import numpy as np
from pathlib import Path
from scipy import stats
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score, accuracy_score
from sklearn.model_selection import StratifiedKFold
from itertools import combinations

BASE = Path("/root/autodl-tmp/recursive_gen_depth_est")
OUT_DIR = BASE / "artifacts" / "atlas_v2"

CELL_PATHS = {
    "pythia_nucleus095": BASE / "data" / "features_all.jsonl",
    "pythia_temp09":     BASE / "data" / "pythia_temp09" / "features.jsonl",
    "pythia_topk50":     BASE / "results" / "pythia_topk50" / "features.jsonl",
    "gpt2xl_nucleus095": BASE / "data" / "gpt2xl" / "features.jsonl",
    "gpt2xl_temp09":     BASE / "results" / "gpt2xl_temp09" / "features.jsonl",
    "gpt2xl_topk50":     BASE / "results" / "gpt2xl_topk50" / "features.jsonl",
    "olmo_nucleus095":   BASE / "data" / "olmo" / "features.jsonl",
    "olmo_temp09":       BASE / "results" / "olmo_temp09" / "features.jsonl",
    "olmo_topk50":       BASE / "results" / "olmo_topk50" / "features.jsonl",
}

FEATURE_NAMES = [
    "mean_ppl", "var_ppl", "skewness_ppl", "kurtosis_ppl",
    "p10_ppl", "p25_ppl", "p50_ppl", "p75_ppl", "p90_ppl",
    "mean_surprisal", "var_surprisal", "entropy_of_surprisal",
    "type_token_ratio", "hapax_ratio", "bigram_entropy", "trigram_entropy",
    "rep_2gram", "rep_3gram", "rep_4gram",
]

MODELS = {
    "Pythia-1.4B": ["pythia_nucleus095", "pythia_temp09", "pythia_topk50"],
    "GPT-2 XL":    ["gpt2xl_nucleus095", "gpt2xl_temp09", "gpt2xl_topk50"],
    "OLMo-1B":     ["olmo_nucleus095", "olmo_temp09", "olmo_topk50"],
}

STRATEGIES = {
    "nucleus095": ["pythia_nucleus095", "gpt2xl_nucleus095", "olmo_nucleus095"],
    "temp09":     ["pythia_temp09", "gpt2xl_temp09", "olmo_temp09"],
    "topk50":     ["pythia_topk50", "gpt2xl_topk50", "olmo_topk50"],
}


def load_cell(path):
    X, y = [], []
    with open(path) as f:
        for line in f:
            d = json.loads(line)
            X.append([d[fn] for fn in FEATURE_NAMES])
            y.append(d["depth"])
    return np.array(X), np.array(y)


def run_feature_importance(cells_data):
    """RF 4-class per cell, return importances and accuracy."""
    result = {}
    for cell, (X, y) in cells_data.items():
        rf = RandomForestClassifier(n_estimators=200, random_state=42, n_jobs=-1)
        rf.fit(X, y)
        imp = rf.feature_importances_
        ranking = sorted(range(len(imp)), key=lambda i: imp[i], reverse=True)
        top2_names = [FEATURE_NAMES[i] for i in ranking[:2]]

        cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
        accs = []
        for tr, te in cv.split(X, y):
            m = RandomForestClassifier(n_estimators=200, random_state=42, n_jobs=-1)
            m.fit(X[tr], y[tr])
            accs.append(accuracy_score(y[te], m.predict(X[te])))

        result[cell] = {
            "importances": {FEATURE_NAMES[i]: float(imp[i]) for i in range(len(imp))},
            "ranking": [FEATURE_NAMES[i] for i in ranking],
            "top2": top2_names,
            "cv5_accuracy_mean": float(np.mean(accs)),
            "cv5_accuracy_std": float(np.std(accs)),
        }

    p90_top2_count = sum(1 for c in result.values() if "p90_ppl" in c["top2"])
    var_surp_top2_count = sum(1 for c in result.values() if "var_surprisal" in c["top2"])

    return {
        "per_cell": result,
        "summary": {
            "p90_ppl_in_top2": p90_top2_count,
            "var_surprisal_in_top2": var_surp_top2_count,
            "total_cells": 9,
        },
    }


def run_monotonicity(cells_data):
    """Spearman correlation of feature mean vs depth for top-5 features per cell."""
    result = {}
    for cell, (X, y) in cells_data.items():
        depths = sorted(np.unique(y))
        rf = RandomForestClassifier(n_estimators=200, random_state=42, n_jobs=-1)
        rf.fit(X, y)
        imp = rf.feature_importances_
        top5_idx = sorted(range(len(imp)), key=lambda i: imp[i], reverse=True)[:5]

        cell_mono = {}
        for fi in top5_idx:
            fname = FEATURE_NAMES[fi]
            means = [float(np.mean(X[y == d, fi])) for d in depths]
            rho, pval = stats.spearmanr(depths, means)
            cell_mono[fname] = {
                "spearman_rho": float(rho),
                "p_value": float(pval),
                "means_by_depth": {str(d): m for d, m in zip(depths, means)},
            }
        result[cell] = cell_mono

    return {"per_cell": result}


def run_edd_analysis(cells_data):
    """Pairwise adjacent-depth AUC and EDD at multiple thresholds."""
    depth_pairs = [(0, 1), (1, 2), (2, 3)]
    pair_labels = ["d0v1", "d1v2", "d2v3"]
    thresholds = [0.65, 0.70, 0.75, 0.80]

    result = {}
    for cell, (X, y) in cells_data.items():
        pair_aucs = {}
        for (da, db), label in zip(depth_pairs, pair_labels):
            mask = (y == da) | (y == db)
            Xp = X[mask]
            yp = (y[mask] == db).astype(int)

            cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
            aucs = []
            for tr, te in cv.split(Xp, yp):
                m = RandomForestClassifier(n_estimators=200, random_state=42, n_jobs=-1)
                m.fit(Xp[tr], yp[tr])
                prob = m.predict_proba(Xp[te])[:, 1]
                aucs.append(roc_auc_score(yp[te], prob))
            pair_aucs[label] = {
                "auc_mean": float(np.mean(aucs)),
                "auc_std": float(np.std(aucs)),
            }

        edd_by_threshold = {}
        for T in thresholds:
            edd = 0
            for i, label in enumerate(pair_labels):
                if pair_aucs[label]["auc_mean"] >= T:
                    edd = i + 1
                else:
                    break
            edd_by_threshold[str(T)] = edd

        result[cell] = {
            "pair_aucs": pair_aucs,
            "edd_by_threshold": edd_by_threshold,
        }

    edd75_count = sum(1 for c in result.values() if c["edd_by_threshold"]["0.75"] == 3)
    return {
        "per_cell": result,
        "summary": {
            "edd_equals_3_at_T075": edd75_count,
            "total_cells": 9,
            "edd_distribution_T075": {
                str(e): sum(1 for c in result.values() if c["edd_by_threshold"]["0.75"] == e)
                for e in range(4)
            },
        },
    }


def run_cross_comparison(cells_data, fi_result):
    """Cross-model/strategy consistency."""
    per_cell_fi = fi_result["per_cell"]

    # 1. Cross-model rank correlation (within each strategy)
    cross_model_rank = {}
    for strat, cells in STRATEGIES.items():
        rankings = {c: per_cell_fi[c]["ranking"][:5] for c in cells}
        pairs = list(combinations(cells, 2))
        corrs = []
        for c1, c2 in pairs:
            r1 = per_cell_fi[c1]["ranking"]
            r2 = per_cell_fi[c2]["ranking"]
            rank1 = [r1.index(f) for f in FEATURE_NAMES]
            rank2 = [r2.index(f) for f in FEATURE_NAMES]
            rho, _ = stats.spearmanr(rank1, rank2)
            corrs.append({"pair": f"{c1}_vs_{c2}", "spearman_rho": float(rho)})
        cross_model_rank[strat] = corrs

    # 2. Cross-strategy rank correlation (within each model)
    cross_strategy_rank = {}
    for model, cells in MODELS.items():
        pairs = list(combinations(cells, 2))
        corrs = []
        for c1, c2 in pairs:
            r1 = per_cell_fi[c1]["ranking"]
            r2 = per_cell_fi[c2]["ranking"]
            rank1 = [r1.index(f) for f in FEATURE_NAMES]
            rank2 = [r2.index(f) for f in FEATURE_NAMES]
            rho, _ = stats.spearmanr(rank1, rank2)
            corrs.append({"pair": f"{c1}_vs_{c2}", "spearman_rho": float(rho)})
        cross_strategy_rank[model] = corrs

    # 3. Jaccard similarity of top-3 features
    jaccard_by_strategy = {}
    for strat, cells in STRATEGIES.items():
        top3s = {c: set(per_cell_fi[c]["ranking"][:3]) for c in cells}
        pairs = list(combinations(cells, 2))
        jaccards = []
        for c1, c2 in pairs:
            inter = len(top3s[c1] & top3s[c2])
            union = len(top3s[c1] | top3s[c2])
            jaccards.append({"pair": f"{c1}_vs_{c2}", "jaccard": float(inter / union)})
        jaccard_by_strategy[strat] = jaccards

    jaccard_by_model = {}
    for model, cells in MODELS.items():
        top3s = {c: set(per_cell_fi[c]["ranking"][:3]) for c in cells}
        pairs = list(combinations(cells, 2))
        jaccards = []
        for c1, c2 in pairs:
            inter = len(top3s[c1] & top3s[c2])
            union = len(top3s[c1] | top3s[c2])
            jaccards.append({"pair": f"{c1}_vs_{c2}", "jaccard": float(inter / union)})
        jaccard_by_model[model] = jaccards

    # 4. Cross-model consistency: per strategy, mean±std of 4-class acc
    cross_model_consistency = {}
    for strat, cells in STRATEGIES.items():
        accs = [per_cell_fi[c]["cv5_accuracy_mean"] for c in cells]
        cross_model_consistency[strat] = {
            "mean_acc": float(np.mean(accs)),
            "std_acc": float(np.std(accs)),
            "per_model": {c: per_cell_fi[c]["cv5_accuracy_mean"] for c in cells},
        }

    # 5. Cross-strategy consistency: per model, mean±std of 4-class acc
    cross_strategy_consistency = {}
    for model, cells in MODELS.items():
        accs = [per_cell_fi[c]["cv5_accuracy_mean"] for c in cells]
        cross_strategy_consistency[model] = {
            "mean_acc": float(np.mean(accs)),
            "std_acc": float(np.std(accs)),
            "per_strategy": {c: per_cell_fi[c]["cv5_accuracy_mean"] for c in cells},
        }

    # Aggregate rank correlation ranges
    all_rhos = []
    for corrs in cross_model_rank.values():
        all_rhos.extend([c["spearman_rho"] for c in corrs])
    for corrs in cross_strategy_rank.values():
        all_rhos.extend([c["spearman_rho"] for c in corrs])

    return {
        "cross_model_rank_correlation": cross_model_rank,
        "cross_strategy_rank_correlation": cross_strategy_rank,
        "jaccard_top3_by_strategy": jaccard_by_strategy,
        "jaccard_top3_by_model": jaccard_by_model,
        "cross_model_accuracy_consistency": cross_model_consistency,
        "cross_strategy_accuracy_consistency": cross_strategy_consistency,
        "summary": {
            "rank_corr_min": float(min(all_rhos)),
            "rank_corr_max": float(max(all_rhos)),
            "rank_corr_mean": float(np.mean(all_rhos)),
        },
    }


def main():
    os.makedirs(OUT_DIR, exist_ok=True)

    print("Loading 9 cells...")
    cells_data = {}
    for cell, path in CELL_PATHS.items():
        X, y = load_cell(path)
        print(f"  {cell}: {X.shape[0]} samples, depths {sorted(np.unique(y))}")
        cells_data[cell] = (X, y)

    print("\n[1/4] Feature importance...")
    fi = run_feature_importance(cells_data)
    with open(OUT_DIR / "feature_importance_9cell.json", "w") as f:
        json.dump(fi, f, indent=2)
    print(f"  p90_ppl top-2: {fi['summary']['p90_ppl_in_top2']}/9")
    print(f"  var_surprisal top-2: {fi['summary']['var_surprisal_in_top2']}/9")

    print("\n[2/4] Monotonicity scores...")
    mono = run_monotonicity(cells_data)
    with open(OUT_DIR / "monotonicity_scores_9cell.json", "w") as f:
        json.dump(mono, f, indent=2)
    for cell in list(mono["per_cell"].keys())[:2]:
        for fname, vals in mono["per_cell"][cell].items():
            print(f"  {cell}/{fname}: rho={vals['spearman_rho']:.3f}")

    print("\n[3/4] EDD analysis...")
    edd = run_edd_analysis(cells_data)
    with open(OUT_DIR / "edd_analysis_9cell.json", "w") as f:
        json.dump(edd, f, indent=2)
    print(f"  EDD=3 @T=0.75: {edd['summary']['edd_equals_3_at_T075']}/9")
    print(f"  Distribution: {edd['summary']['edd_distribution_T075']}")

    print("\n[4/4] Cross-model comparison...")
    cross = run_cross_comparison(cells_data, fi)
    with open(OUT_DIR / "cross_comparison_9cell.json", "w") as f:
        json.dump(cross, f, indent=2)
    s = cross["summary"]
    print(f"  Rank corr range: [{s['rank_corr_min']:.3f}, {s['rank_corr_max']:.3f}]")
    print(f"  Rank corr mean: {s['rank_corr_mean']:.3f}")

    print("\nDone. Artifacts in", OUT_DIR)


if __name__ == "__main__":
    main()
