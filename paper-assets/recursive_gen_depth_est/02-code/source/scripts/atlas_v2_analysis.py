"""
Depth Degradation Atlas v2 Analysis

Input:  artifacts/atlas/atlas_v2_data.json (7/9 cells, 3 models x 3 strategies)
Output: artifacts/atlas/atlas_v2_results.json
"""

import json
import sys
from itertools import combinations
from pathlib import Path

import numpy as np
from scipy import stats

ROOT = Path("/root/autodl-tmp/recursive_gen_depth_est")
DATA_FILE = ROOT / "artifacts" / "atlas" / "atlas_v2_data.json"
OUT_FILE = ROOT / "artifacts" / "atlas" / "atlas_v2_results.json"


def load_data():
    with open(DATA_FILE) as f:
        return json.load(f)


# ── 1. Signal Strength Heatmap (model × strategy → acc) ──

def signal_strength_heatmap(data):
    models = data["grid"]["models"]
    strategies = data["grid"]["strategies"]
    cell_keys = data["grid"]["cell_keys"]

    heatmap_rf = {}
    heatmap_lr = {}
    for model in models:
        heatmap_rf[model] = {}
        heatmap_lr[model] = {}
        for strat in strategies:
            key = cell_keys[model].get(strat)
            if key and key in data["cells"]:
                cell = data["cells"][key]
                heatmap_rf[model][strat] = cell["acc_4class"]["random_forest"]
                heatmap_lr[model][strat] = cell["acc_4class"]["logistic_regression"]
            else:
                heatmap_rf[model][strat] = None
                heatmap_lr[model][strat] = None

    valid_rf = [v for m in heatmap_rf.values() for v in m.values() if v is not None]
    return {
        "random_forest": heatmap_rf,
        "logistic_regression": heatmap_lr,
        "summary": {
            "mean_rf_acc": round(np.mean(valid_rf), 4),
            "std_rf_acc": round(np.std(valid_rf), 4),
            "min_rf_acc": round(min(valid_rf), 4),
            "max_rf_acc": round(max(valid_rf), 4),
            "best_cell": max(data["cells"].items(),
                            key=lambda x: x[1]["acc_4class"]["random_forest"])[0],
            "worst_cell": min(data["cells"].items(),
                             key=lambda x: x[1]["acc_4class"]["random_forest"])[0],
        }
    }


# ── 2. Cross-Strategy Monotonicity ──

def cross_strategy_monotonicity(data):
    """For each model, check how acc/AUC changes across strategies."""
    models = data["grid"]["models"]
    strategies = data["grid"]["strategies"]
    cell_keys = data["grid"]["cell_keys"]

    results = {}
    for model in models:
        model_cells = {}
        for strat in strategies:
            key = cell_keys[model].get(strat)
            if key and key in data["cells"]:
                model_cells[strat] = data["cells"][key]

        if len(model_cells) < 2:
            continue

        strat_accs = {s: c["acc_4class"]["random_forest"] for s, c in model_cells.items()}
        strat_mean_auc = {}
        for s, c in model_cells.items():
            aucs = list(c["auc"]["random_forest"].values())
            strat_mean_auc[s] = round(np.mean(aucs), 4)

        hardest_pair_auc = {}
        for s, c in model_cells.items():
            hardest_pair_auc[s] = c["auc"]["random_forest"]["depth2_vs_depth3"]

        results[model] = {
            "acc_by_strategy": strat_accs,
            "mean_auc_by_strategy": strat_mean_auc,
            "d2d3_auc_by_strategy": hardest_pair_auc,
            "n_strategies": len(model_cells),
            "acc_range": round(max(strat_accs.values()) - min(strat_accs.values()), 4),
        }

    return results


# ── 3. Cross-Model Rank Correlation ──

def cross_model_rank_correlation(data):
    """For each strategy, compute Spearman rho of feature importance ranks across models."""
    strategies = data["grid"]["strategies"]
    cell_keys = data["grid"]["cell_keys"]
    models = data["grid"]["models"]

    features = list(data["cells"][list(data["cells"].keys())[0]]["feature_importance"].keys())

    results = {}
    for strat in strategies:
        strat_cells = {}
        for model in models:
            key = cell_keys[model].get(strat)
            if key and key in data["cells"]:
                strat_cells[model] = data["cells"][key]

        if len(strat_cells) < 2:
            results[strat] = {"status": "insufficient_data", "n_models": len(strat_cells)}
            continue

        model_names = list(strat_cells.keys())
        pairwise_rho = {}
        for m1, m2 in combinations(model_names, 2):
            imp1 = strat_cells[m1]["feature_importance"]
            imp2 = strat_cells[m2]["feature_importance"]
            ranks1 = [imp1.get(f, 0) for f in features]
            ranks2 = [imp2.get(f, 0) for f in features]
            rho, p = stats.spearmanr(ranks1, ranks2)
            pairwise_rho[f"{m1}_vs_{m2}"] = {"rho": round(float(rho), 4), "p": float(p)}

        all_rhos = [v["rho"] for v in pairwise_rho.values()]
        results[strat] = {
            "pairwise": pairwise_rho,
            "mean_rho": round(np.mean(all_rhos), 4),
            "n_models": len(strat_cells),
        }

    return results


# ── 4. EDD (Effective Degradation Depth) ──

def compute_edd(data, threshold=0.80):
    """EDD = max depth d such that AUC(d-1 vs d) >= threshold."""
    results = {}
    for cell_name, cell in data["cells"].items():
        aucs_rf = cell["auc"]["random_forest"]
        consecutive = {
            "0v1": aucs_rf["depth0_vs_depth1"],
            "1v2": aucs_rf["depth1_vs_depth2"],
            "2v3": aucs_rf["depth2_vs_depth3"],
        }
        edd = 0
        for pair, label in [("0v1", 1), ("1v2", 2), ("2v3", 3)]:
            if consecutive[pair] >= threshold:
                edd = label
            else:
                break
        results[cell_name] = {
            "edd": edd,
            "consecutive_aucs": consecutive,
            "model": cell["model"],
            "strategy": cell["strategy"],
        }

    edd_matrix = {}
    for cell_name, r in results.items():
        model = r["model"]
        strat = r["strategy"]
        if model not in edd_matrix:
            edd_matrix[model] = {}
        edd_matrix[model][strat] = r["edd"]

    return {"per_cell": results, "matrix": edd_matrix, "threshold": threshold}


# ── 5. Cross-Cell Jaccard Similarity ──

def cross_cell_jaccard(data, top_k=5):
    """Jaccard similarity of top-k feature sets across all cell pairs."""
    cell_names = list(data["cells"].keys())
    top_features = {}
    for name in cell_names:
        top_features[name] = set(data["cells"][name]["top5_features"][:top_k])

    pairwise = {}
    for c1, c2 in combinations(cell_names, 2):
        s1, s2 = top_features[c1], top_features[c2]
        jaccard = len(s1 & s2) / len(s1 | s2) if (s1 | s2) else 0
        pairwise[f"{c1}_vs_{c2}"] = round(jaccard, 4)

    jaccards = list(pairwise.values())

    same_model = {}
    same_strategy = {}
    for pair_key, j in pairwise.items():
        c1, c2 = pair_key.split("_vs_")
        m1, m2 = data["cells"][c1]["model"], data["cells"][c2]["model"]
        s1, s2 = data["cells"][c1]["strategy"], data["cells"][c2]["strategy"]
        if m1 == m2:
            same_model.setdefault(m1, []).append(j)
        if s1 == s2:
            same_strategy.setdefault(s1, []).append(j)

    return {
        "pairwise": pairwise,
        "mean_jaccard": round(np.mean(jaccards), 4),
        "std_jaccard": round(np.std(jaccards), 4),
        "same_model_mean": {k: round(np.mean(v), 4) for k, v in same_model.items()},
        "same_strategy_mean": {k: round(np.mean(v), 4) for k, v in same_strategy.items()},
        "top_k": top_k,
    }


# ── 6. Universal Feature Ranking ──

def universal_feature_ranking(data):
    """Aggregate feature importance across all cells."""
    all_importances = {}
    for cell_name, cell in data["cells"].items():
        for feat, imp in cell["feature_importance"].items():
            all_importances.setdefault(feat, []).append(imp)

    mean_importance = {f: round(np.mean(v), 4) for f, v in all_importances.items()}
    std_importance = {f: round(np.std(v), 4) for f, v in all_importances.items()}

    ranked = sorted(mean_importance.items(), key=lambda x: -x[1])
    return {
        "mean_importance": dict(ranked),
        "std_importance": std_importance,
        "top5_universal": [f for f, _ in ranked[:5]],
        "top5_stable": sorted(ranked[:10], key=lambda x: std_importance[x[0]])[:5],
    }


# ── Main ──

def main():
    data = load_data()
    cells = data["cells"]
    n = len(cells)
    print(f"Loaded {n}/9 cells")

    results = {}

    print("\n[1] Signal Strength Heatmap")
    results["signal_strength"] = signal_strength_heatmap(data)
    ss = results["signal_strength"]
    print(f"    Mean RF acc: {ss['summary']['mean_rf_acc']}")
    print(f"    Range: {ss['summary']['min_rf_acc']} - {ss['summary']['max_rf_acc']}")
    print(f"    Best: {ss['summary']['best_cell']}, Worst: {ss['summary']['worst_cell']}")
    for model in data["grid"]["models"]:
        row = [f"{ss['random_forest'][model].get(s, '---'):>8}" if ss['random_forest'][model].get(s) else "     ---"
               for s in data["grid"]["strategies"]]
        print(f"    {model:>12}: {' '.join(row)}")

    print("\n[2] Cross-Strategy Monotonicity")
    results["cross_strategy"] = cross_strategy_monotonicity(data)
    for model, r in results["cross_strategy"].items():
        print(f"    {model}: acc range={r['acc_range']}, "
              f"d2d3 AUCs={r['d2d3_auc_by_strategy']}")

    print("\n[3] Cross-Model Rank Correlation")
    results["cross_model_rank"] = cross_model_rank_correlation(data)
    for strat, r in results["cross_model_rank"].items():
        if "mean_rho" in r:
            print(f"    {strat}: mean ρ={r['mean_rho']}")
        else:
            print(f"    {strat}: {r['status']}")

    print("\n[4] EDD (threshold=0.80)")
    results["edd"] = compute_edd(data)
    for cell, r in results["edd"]["per_cell"].items():
        aucs_str = ", ".join(f"{k}={v:.3f}" for k, v in r["consecutive_aucs"].items())
        print(f"    {cell:>20}: EDD={r['edd']}  ({aucs_str})")
    print("    EDD Matrix:")
    for model, strats in results["edd"]["matrix"].items():
        print(f"      {model:>12}: {strats}")

    print("\n[5] Cross-Cell Jaccard (top-5 features)")
    results["jaccard"] = cross_cell_jaccard(data)
    j = results["jaccard"]
    print(f"    Mean Jaccard: {j['mean_jaccard']} ± {j['std_jaccard']}")
    print(f"    Same-model:    {j['same_model_mean']}")
    print(f"    Same-strategy: {j['same_strategy_mean']}")

    print("\n[6] Universal Feature Ranking")
    results["universal_features"] = universal_feature_ranking(data)
    uf = results["universal_features"]
    print(f"    Top-5 universal: {uf['top5_universal']}")
    top5_stable = [(f, imp) for f, imp in uf["top5_stable"]]
    print(f"    Top-5 stable:    {[f for f, _ in top5_stable]}")

    results["metadata"] = {
        "n_cells": n,
        "n_missing": 9 - n,
        "missing_cells": list(data.get("missing_cells", {}).keys()),
        "generated_at": "2026-05-15",
        "atlas_version": "v2",
    }

    with open(OUT_FILE, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to {OUT_FILE}")


if __name__ == "__main__":
    main()
