"""
Depth Degradation Atlas v2 — 3x3 matrix analysis framework.

Reads artifacts/atlas_v2/matrix_data.json and computes:
  1. Monotonicity scores (Spearman rho per feature per cell)
  2. EDD (Effective Degradation Depth)
  3. Cross-model heatmap data
  4. Feature trajectory summaries
  5. Cross-strategy Jaccard similarity

Usage:
  python src/atlas_v2.py                     # run all analyses
  python src/atlas_v2.py --analysis mono     # single analysis
  python src/atlas_v2.py --output-dir /path  # custom output
"""
import argparse
import json
import os
from collections import defaultdict
from itertools import combinations
from pathlib import Path

PROJ_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_MATRIX = PROJ_ROOT / "artifacts" / "atlas_v2" / "matrix_data.json"
DEFAULT_OUTPUT = PROJ_ROOT / "artifacts" / "atlas_v2"

MODELS = ["Pythia-1.4B", "OLMo-1B", "GPT-2-XL"]
STRATEGIES = ["nucleus_p095", "temperature_09", "topk_k50"]
STRATEGY_LABELS = {"nucleus_p095": "Nucleus p=0.95", "temperature_09": "Temp τ=0.9", "topk_k50": "Top-k k=50"}


def load_matrix(path: str | Path = DEFAULT_MATRIX) -> dict:
    with open(path) as f:
        return json.load(f)


def completed_cells(data: dict) -> dict:
    return {k: v for k, v in data["cells"].items() if v.get("status") == "done"}


# ---------------------------------------------------------------------------
# 1. Monotonicity: Spearman rho of each feature importance across depths
# ---------------------------------------------------------------------------
def compute_monotonicity(data: dict) -> dict:
    """For cells with feature_trajectory, compute Spearman rho of each feature vs depth."""
    from scipy.stats import spearmanr

    results = {}
    for cell_key, cell in completed_cells(data).items():
        traj = cell.get("feature_trajectory", {})
        if not traj.get("available"):
            results[cell_key] = {"available": False}
            continue

        means = traj["depth_means"]
        depths = sorted(means.keys(), key=int)
        features = list(means[depths[0]].keys())

        rhos = {}
        for feat in features:
            vals = [means[d][feat] for d in depths]
            depth_ints = [int(d) for d in depths]
            rho, pval = spearmanr(depth_ints, vals)
            rhos[feat] = {"rho": round(rho, 4), "pvalue": round(pval, 4)}

        n_monotonic_neg = sum(1 for v in rhos.values() if v["rho"] <= -0.8)
        n_monotonic_pos = sum(1 for v in rhos.values() if v["rho"] >= 0.8)
        results[cell_key] = {
            "available": True,
            "feature_rhos": rhos,
            "n_monotonic_decreasing": n_monotonic_neg,
            "n_monotonic_increasing": n_monotonic_pos,
            "summary": f"{n_monotonic_neg} features monotonically decrease, {n_monotonic_pos} increase with depth"
        }
    return results


# ---------------------------------------------------------------------------
# 2. EDD (Effective Degradation Depth)
# ---------------------------------------------------------------------------
def compute_edd(data: dict, threshold: float = 0.7) -> dict:
    """EDD = first adjacent-depth pair where pairwise AUC drops below threshold."""
    results = {}
    for cell_key, cell in completed_cells(data).items():
        auc = cell["pairwise_auc"]["random_forest"]
        adjacent_pairs = [
            ("d0v1", 0, 1),
            ("d1v2", 1, 2),
            ("d2v3", 2, 3),
        ]
        edd = None
        pair_aucs = {}
        for pair_key, d_lo, d_hi in adjacent_pairs:
            val = auc[pair_key]
            pair_aucs[f"depth{d_lo}_vs_depth{d_hi}"] = val
            if val < threshold and edd is None:
                edd = d_hi

        saturated = auc["d2v3"] >= threshold
        results[cell_key] = {
            "edd": edd,
            "saturated": not saturated,
            "adjacent_aucs": pair_aucs,
            "threshold": threshold,
            "interpretation": (
                f"Signal saturates at depth {edd}" if edd
                else "Signal persists through depth 3 (no saturation within measured range)"
            )
        }
    return results


# ---------------------------------------------------------------------------
# 3. Cross-model heatmap data
# ---------------------------------------------------------------------------
def compute_heatmap(data: dict) -> dict:
    """Build 3x3 heatmap matrices for key metrics."""
    grid = data["grid"]
    metrics_to_extract = {
        "rf_4class_acc": lambda c: c["acc_4class"]["random_forest"],
        "d1v2_auc": lambda c: c["pairwise_auc"]["random_forest"]["d1v2"],
        "d2v3_auc": lambda c: c["pairwise_auc"]["random_forest"]["d2v3"],
    }

    heatmaps = {}
    for metric_name, extractor in metrics_to_extract.items():
        matrix = []
        for model in MODELS:
            row = []
            for strategy in STRATEGIES:
                cell_key = grid["cell_keys"][model][strategy]
                if cell_key and cell_key in data["cells"]:
                    cell = data["cells"][cell_key]
                    if cell.get("status") == "done":
                        row.append(round(extractor(cell), 4))
                    else:
                        row.append(None)
                else:
                    row.append(None)
            matrix.append(row)
        heatmaps[metric_name] = {
            "rows": MODELS,
            "cols": [STRATEGY_LABELS[s] for s in STRATEGIES],
            "values": matrix,
        }
    return heatmaps


# ---------------------------------------------------------------------------
# 4. Feature trajectory summary
# ---------------------------------------------------------------------------
def compute_feature_trajectory_summary(data: dict) -> dict:
    """Summarize feature trajectories: direction, magnitude of change d0->d3."""
    results = {}
    for cell_key, cell in completed_cells(data).items():
        traj = cell.get("feature_trajectory", {})
        if not traj.get("available"):
            results[cell_key] = {"available": False}
            continue

        means = traj["depth_means"]
        d0, d3 = means["0"], means["3"]
        features = list(d0.keys())

        changes = {}
        for feat in features:
            v0, v3 = d0[feat], d3[feat]
            if abs(v0) > 1e-10:
                pct_change = (v3 - v0) / abs(v0)
            else:
                pct_change = 0.0
            direction = "decrease" if v3 < v0 else "increase" if v3 > v0 else "stable"
            changes[feat] = {
                "d0": round(v0, 4),
                "d3": round(v3, 4),
                "pct_change": round(pct_change, 4),
                "direction": direction,
            }

        results[cell_key] = {
            "available": True,
            "feature_changes_d0_to_d3": changes,
            "strongest_decrease": max(
                [(f, abs(c["pct_change"])) for f, c in changes.items() if c["direction"] == "decrease"],
                key=lambda x: x[1], default=("none", 0)
            )[0],
            "strongest_increase": max(
                [(f, abs(c["pct_change"])) for f, c in changes.items() if c["direction"] == "increase"],
                key=lambda x: x[1], default=("none", 0)
            )[0],
        }
    return results


# ---------------------------------------------------------------------------
# 5. Cross-strategy Jaccard
# ---------------------------------------------------------------------------
def compute_jaccard(data: dict, top_n: int = 5) -> dict:
    """Jaccard similarity of top-N features between strategies for the same model."""
    grid = data["grid"]
    results = {}

    for model in MODELS:
        strategy_features = {}
        for strategy in STRATEGIES:
            cell_key = grid["cell_keys"][model][strategy]
            if cell_key and cell_key in data["cells"]:
                cell = data["cells"][cell_key]
                if cell.get("status") == "done" and "top5_features" in cell:
                    strategy_features[strategy] = set(cell["top5_features"][:top_n])

        pairs = {}
        for s1, s2 in combinations(strategy_features.keys(), 2):
            f1, f2 = strategy_features[s1], strategy_features[s2]
            intersection = f1 & f2
            union = f1 | f2
            jaccard = len(intersection) / len(union) if union else 0.0
            pair_key = f"{STRATEGY_LABELS[s1]} vs {STRATEGY_LABELS[s2]}"
            pairs[pair_key] = {
                "jaccard": round(jaccard, 4),
                "overlap": sorted(intersection),
                "only_first": sorted(f1 - f2),
                "only_second": sorted(f2 - f1),
            }

        results[model] = {
            "strategy_features": {STRATEGY_LABELS[s]: sorted(f) for s, f in strategy_features.items()},
            "pairwise_jaccard": pairs,
        }
    return results


# ---------------------------------------------------------------------------
# Runner
# ---------------------------------------------------------------------------
ANALYSES = {
    "mono": ("monotonicity_scores.json", compute_monotonicity),
    "edd": ("edd_analysis.json", compute_edd),
    "heatmap": ("cross_model_heatmap.json", compute_heatmap),
    "trajectory": ("feature_trajectory_summary.json", compute_feature_trajectory_summary),
    "jaccard": ("jaccard_matrix.json", compute_jaccard),
}


def run(matrix_path: str, output_dir: str, analysis: str | None = None):
    data = load_matrix(matrix_path)
    os.makedirs(output_dir, exist_ok=True)

    targets = {analysis: ANALYSES[analysis]} if analysis else ANALYSES

    for key, (filename, func) in targets.items():
        print(f"Computing {key}...")
        result = func(data)
        out_path = os.path.join(output_dir, filename)
        with open(out_path, "w") as f:
            json.dump(result, f, indent=2, ensure_ascii=False, default=str)
        print(f"  -> {out_path}")

    print_summary(data)


def print_summary(data: dict):
    cells = data["cells"]
    done = [k for k, v in cells.items() if v.get("status") == "done"]
    running = [k for k, v in cells.items() if v.get("status") == "running"]

    print(f"\n{'='*60}")
    print(f"Atlas v2 Summary: {len(done)}/9 cells completed")
    print(f"{'='*60}")

    print("\n3x3 Matrix (RF 4-class accuracy):")
    print(f"{'':20s} {'Nucleus':>10s} {'Temp09':>10s} {'TopK50':>10s}")
    grid = data["grid"]
    for model in MODELS:
        row = f"{model:20s}"
        for strategy in STRATEGIES:
            ck = grid["cell_keys"][model][strategy]
            if ck and ck in cells and cells[ck].get("status") == "done":
                acc = cells[ck]["acc_4class"]["random_forest"]
                row += f" {acc:>9.1%}"
            else:
                row += f" {'---':>10s}"
        print(row)

    if running:
        print(f"\nPending: {', '.join(running)}")


def main():
    parser = argparse.ArgumentParser(description="Depth Degradation Atlas v2")
    parser.add_argument("--matrix", default=str(DEFAULT_MATRIX))
    parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT))
    parser.add_argument("--analysis", choices=list(ANALYSES.keys()), default=None,
                        help="Run single analysis (default: all)")
    args = parser.parse_args()
    run(args.matrix, args.output_dir, args.analysis)


if __name__ == "__main__":
    main()
