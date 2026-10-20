"""MVP 结果自动分析：Phase C/D/E 汇总。

读取 v3 三方法 circuit 数据，计算 CSS matrix、off-diagonal 比率、
按 ACDC threshold 敏感性分析，生成可视化，输出 pass/fail 判定。

Usage:
    python analyze_mvp_results.py [--results-dir /root/structfuse-context] [--output-dir ./analysis]
    python analyze_mvp_results.py --dry-run   # mock data 验证
"""

import argparse
import itertools
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

import numpy as np


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------

def _find_cache_files(results_dir: Path) -> Dict[str, Path]:
    """Auto-detect per-method cache files under results_dir.

    Searches for:
      1. cache_<method>.json  (old MVP flat layout)
      2. cache/<model_slug>/<task>/<method>_*.json  (run_circus.py structured cache)
      3. Keys inside mvp_results.json that embed raw scores
    """
    found: Dict[str, Path] = {}
    method_names = ["eap_ig", "edge_pruning", "acdc", "ifr"]

    for m in method_names:
        flat = results_dir / f"cache_{m}.json"
        if flat.exists():
            found[m] = flat

    cache_dir = results_dir / "cache"
    if cache_dir.is_dir():
        for p in cache_dir.rglob("*.json"):
            for m in method_names:
                if p.stem.startswith(m):
                    found.setdefault(m, p)

    return found


def _load_scores_from_file(path: Path) -> Dict[str, float]:
    """Load edge scores from a cache JSON (handles both flat and structured)."""
    with open(path) as f:
        data = json.load(f)

    if isinstance(data, dict) and "scores" in data:
        return {str(k): float(v) for k, v in data["scores"].items()}
    if isinstance(data, dict) and all(isinstance(v, (int, float)) for v in data.values()):
        return {str(k): float(v) for k, v in data.items()}
    if isinstance(data, list):
        return {str(item["edge"]): float(item["score"]) for item in data if "edge" in item}
    raise ValueError(f"Unrecognized cache format in {path}")


def _load_pipeline_results(results_dir: Path) -> Optional[Dict[str, Any]]:
    """Load mvp_results.json or run_circus output."""
    for name in ["mvp_results.json", "results/mvp_results.json"]:
        p = results_dir / name
        if p.exists():
            with open(p) as f:
                return json.load(f)
    results_subdir = results_dir / "results"
    if results_subdir.is_dir():
        jsons = sorted(results_subdir.glob("*.json"), key=lambda x: x.stat().st_mtime, reverse=True)
        if jsons:
            with open(jsons[0]) as f:
                return json.load(f)
    return None


def load_all_data(results_dir: Path) -> Tuple[
    Dict[str, Dict[str, float]],  # method -> edge scores
    Optional[Dict[str, Any]],     # pipeline results JSON
]:
    """Load all available method scores and pipeline results."""
    cache_files = _find_cache_files(results_dir)
    all_scores: Dict[str, Dict[str, float]] = {}

    for method, path in cache_files.items():
        try:
            all_scores[method] = _load_scores_from_file(path)
            print(f"  Loaded {method}: {len(all_scores[method])} edges from {path}")
        except Exception as e:
            print(f"  WARNING: failed to load {method} from {path}: {e}")

    pipeline = _load_pipeline_results(results_dir)
    if pipeline:
        print(f"  Loaded pipeline results: {list(pipeline.keys())}")

    if not all_scores:
        print("  WARNING: no per-method score files found")

    return all_scores, pipeline


# ---------------------------------------------------------------------------
# Binarization (no torch dependency)
# ---------------------------------------------------------------------------

def binarize_topn(scores: Dict[str, float], n: int = 200) -> Set[str]:
    sorted_edges = sorted(scores.items(), key=lambda x: abs(x[1]), reverse=True)
    return {e for e, _ in sorted_edges[:n]}


def binarize_threshold(scores: Dict[str, float], threshold: float = 0.5) -> Set[str]:
    return {e for e, s in scores.items() if s >= threshold}


def binarize_acdc(scores: Dict[str, float], tau: float = 0.05) -> Set[str]:
    return {e for e, s in scores.items() if abs(s) > tau}


def binarize_method(
    scores: Dict[str, float], method: str,
    top_n: int = 200, acdc_tau: float = 0.05,
) -> Set[str]:
    if method == "acdc":
        return binarize_acdc(scores, tau=acdc_tau)
    elif method == "edge_pruning":
        return binarize_threshold(scores, threshold=0.5)
    else:
        return binarize_topn(scores, n=top_n)


# ---------------------------------------------------------------------------
# CSS / Jaccard / cross-tabulation
# ---------------------------------------------------------------------------

def jaccard(a: Set[str], b: Set[str]) -> float:
    if not a and not b:
        return 1.0
    union = a | b
    if not union:
        return 0.0
    return len(a & b) / len(union)


def compute_pairwise_css(circuits: Dict[str, Set[str]]) -> Dict[str, float]:
    methods = sorted(circuits.keys())
    result = {}
    for m1, m2 in itertools.combinations(methods, 2):
        result[f"{m1} vs {m2}"] = jaccard(circuits[m1], circuits[m2])
    return result


def compute_css_matrix_full(
    circuits: Dict[str, Set[str]],
) -> Dict[str, Any]:
    """Full 2^K cross-tabulation."""
    methods = sorted(circuits.keys())
    K = len(methods)
    all_edges: Set[str] = set()
    for edges in circuits.values():
        all_edges |= edges

    cell_counts: Dict[str, int] = Counter()
    for edge in all_edges:
        cell = tuple(1 if edge in circuits[m] else 0 for m in methods)
        cell_counts[str(cell)] += 1

    all_ones = str(tuple(1 for _ in range(K)))
    all_zeros = str(tuple(0 for _ in range(K)))

    agree_in = cell_counts.get(all_ones, 0)
    total_with_any = sum(c for label, c in cell_counts.items() if label != all_zeros)
    off_diagonal = total_with_any - agree_in

    return {
        "cell_counts": dict(cell_counts),
        "agree_all_in": agree_in,
        "agree_all_out_of_union": 0,
        "off_diagonal": off_diagonal,
        "total_union": total_with_any,
        "off_diagonal_pct": off_diagonal / total_with_any if total_with_any > 0 else 0.0,
        "methods": methods,
    }


def compute_circus_tiers(
    scores: Dict[str, float], B: int = 10,
    core_thr: float = 1.0, contingent_thr: float = 0.5,
) -> Dict[str, str]:
    if not scores:
        return {}
    vals = np.array(list(scores.values()))
    edges = list(scores.keys())
    percentiles = np.linspace(100 / (B + 1), 100 * B / (B + 1), B)
    thresholds = np.percentile(vals, percentiles)
    stability = sum((vals >= t).astype(float) for t in thresholds) / B
    tiers = {}
    for edge, s in zip(edges, stability):
        if s >= core_thr:
            tiers[edge] = "core"
        elif s >= contingent_thr:
            tiers[edge] = "contingent"
        else:
            tiers[edge] = "noise"
    return tiers


def compute_cross_table(
    tiers: Dict[str, str],
    circuits: Dict[str, Set[str]],
    css_threshold: float = 0.67,
    K: int = 3,
) -> Dict[str, Any]:
    all_edges: Set[str] = set(tiers.keys())
    for c in circuits.values():
        all_edges |= c

    css_scores: Dict[str, float] = {}
    for edge in all_edges:
        css_scores[edge] = sum(1 for c in circuits.values() if edge in c) / K

    stable_core = set()
    method_specific = set()
    cross_unstable = set()
    noise = set()

    for e in all_edges:
        is_core = tiers.get(e) == "core"
        is_high = css_scores.get(e, 0.0) >= css_threshold - 0.01
        if is_core and is_high:
            stable_core.add(e)
        elif is_core:
            method_specific.add(e)
        elif is_high:
            cross_unstable.add(e)
        else:
            noise.add(e)

    core_total = len(stable_core) + len(method_specific)
    off_diag = len(method_specific) / core_total if core_total > 0 else 0.0

    return {
        "stable_core": len(stable_core),
        "method_specific": len(method_specific),
        "cross_unstable": len(cross_unstable),
        "noise": len(noise),
        "core_total": core_total,
        "off_diagonal_pct": off_diag,
    }


# ---------------------------------------------------------------------------
# ACDC threshold sensitivity
# ---------------------------------------------------------------------------

ACDC_TAUS = [0.01, 0.03, 0.05, 0.1, 0.3]


def acdc_sensitivity(
    all_scores: Dict[str, Dict[str, float]],
    top_n: int = 200,
    taus: Optional[List[float]] = None,
) -> List[Dict[str, Any]]:
    """Sweep ACDC thresholds, recompute off-diagonal for each."""
    if "acdc" not in all_scores:
        return []

    taus = taus or ACDC_TAUS
    other_methods = {m: s for m, s in all_scores.items() if m != "acdc"}
    if not other_methods:
        return []

    results = []
    for tau in taus:
        circuits: Dict[str, Set[str]] = {}
        for m, s in other_methods.items():
            circuits[m] = binarize_method(s, m, top_n=top_n)
        circuits["acdc"] = binarize_acdc(all_scores["acdc"], tau=tau)

        css_result = compute_css_matrix_full(circuits)
        results.append({
            "tau": tau,
            "acdc_size": len(circuits["acdc"]),
            "off_diagonal": css_result["off_diagonal"],
            "off_diagonal_pct": css_result["off_diagonal_pct"],
            "total_union": css_result["total_union"],
        })
    return results


# ---------------------------------------------------------------------------
# Gate judgment
# ---------------------------------------------------------------------------

def gate_judgment(off_diagonal_pct: float) -> Dict[str, str]:
    pct = off_diagonal_pct * 100
    if pct >= 10:
        return {
            "verdict": "PASS_MAIN",
            "action": f"Off-diagonal {pct:.1f}% >= 10% → Main track",
        }
    elif pct >= 5:
        return {
            "verdict": "PASS_FINDINGS",
            "action": f"Off-diagonal {pct:.1f}% in [5-10%) → Findings + Arithmetic 追加验证",
        }
    elif pct >= 2:
        return {
            "verdict": "MARGINAL",
            "action": f"Off-diagonal {pct:.1f}% in [2-5%) → Findings 确认",
        }
    else:
        return {
            "verdict": "KILL",
            "action": f"Off-diagonal {pct:.1f}% < 2% → Kill (if ΔF 无统计差异)",
        }


# ---------------------------------------------------------------------------
# Visualization
# ---------------------------------------------------------------------------

def save_css_heatmap(
    pairwise: Dict[str, float],
    methods: List[str],
    output_path: Path,
) -> None:
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        print("  matplotlib not available, skipping heatmap")
        return

    K = len(methods)
    matrix = np.eye(K)
    for i, m1 in enumerate(methods):
        for j, m2 in enumerate(methods):
            if i == j:
                continue
            key = f"{min(m1,m2)} vs {max(m1,m2)}"
            if key not in pairwise:
                key = f"{m1} vs {m2}"
                if key not in pairwise:
                    key = f"{m2} vs {m1}"
            matrix[i, j] = pairwise.get(key, 0.0)

    fig, ax = plt.subplots(figsize=(6, 5))
    im = ax.imshow(matrix, cmap="YlOrRd", vmin=0, vmax=1)
    ax.set_xticks(range(K))
    ax.set_yticks(range(K))
    ax.set_xticklabels(methods, rotation=45, ha="right")
    ax.set_yticklabels(methods)
    for i in range(K):
        for j in range(K):
            ax.text(j, i, f"{matrix[i, j]:.3f}", ha="center", va="center",
                    color="white" if matrix[i, j] > 0.5 else "black", fontsize=11)
    ax.set_title("Pairwise Jaccard Similarity (CSS)")
    fig.colorbar(im, ax=ax, shrink=0.8)
    fig.tight_layout()
    fig.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved heatmap → {output_path}")


def save_venn_or_bar(
    circuits: Dict[str, Set[str]],
    output_path: Path,
) -> None:
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        print("  matplotlib not available, skipping overlap chart")
        return

    methods = sorted(circuits.keys())
    if len(methods) != 3:
        _save_overlap_bar(circuits, output_path, plt)
        return

    try:
        from matplotlib_venn import venn3
        a, b, c = [circuits[m] for m in methods]
        fig, ax = plt.subplots(figsize=(7, 6))
        venn3([a, b, c], set_labels=methods, ax=ax)
        ax.set_title("Edge Overlap (3-method Venn)")
        fig.tight_layout()
        fig.savefig(output_path, dpi=150, bbox_inches="tight")
        plt.close(fig)
        print(f"  Saved Venn diagram → {output_path}")
    except ImportError:
        _save_overlap_bar(circuits, output_path, plt)


def _save_overlap_bar(circuits: Dict[str, Set[str]], output_path: Path, plt) -> None:
    methods = sorted(circuits.keys())
    all_edges: Set[str] = set()
    for c in circuits.values():
        all_edges |= c

    counts_by_agreement = Counter()
    for edge in all_edges:
        n = sum(1 for m in methods if edge in circuits[m])
        counts_by_agreement[n] += 1

    labels = [f"{k}/{len(methods)}" for k in sorted(counts_by_agreement.keys())]
    values = [counts_by_agreement[k] for k in sorted(counts_by_agreement.keys())]

    fig, ax = plt.subplots(figsize=(6, 4))
    bars = ax.bar(labels, values, color=["#d62728", "#ff7f0e", "#2ca02c"][:len(labels)])
    ax.set_xlabel("Methods agreeing")
    ax.set_ylabel("Number of edges")
    ax.set_title("Edge Agreement Distribution")
    for bar, v in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1,
                str(v), ha="center", va="bottom", fontsize=10)
    fig.tight_layout()
    fig.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved overlap bar chart → {output_path}")


# ---------------------------------------------------------------------------
# Mock data for --dry-run
# ---------------------------------------------------------------------------

def generate_mock_data() -> Dict[str, Dict[str, float]]:
    rng = np.random.RandomState(42)
    n_total = 500
    edge_names = [f"blocks.{l}.attn.hook_result[{h}] -> blocks.{l+1}.attn.hook_q[{h2}]"
                  for l in range(12) for h in range(12) for h2 in range(12)
                  if l * 144 + h * 12 + h2 < n_total]
    edge_names = edge_names[:n_total]

    eap_ig = {e: float(rng.randn()) for e in edge_names}
    ep_scores = {e: float(rng.uniform(0, 1)) for e in edge_names}
    acdc_scores = {}
    for e in edge_names:
        acdc_scores[e] = float(rng.choice([0.0, 0.02, 0.05, 0.1, 0.5, 1.0],
                                           p=[0.5, 0.1, 0.1, 0.1, 0.1, 0.1]))

    return {"eap_ig": eap_ig, "edge_pruning": ep_scores, "acdc": acdc_scores}


# ---------------------------------------------------------------------------
# Main analysis
# ---------------------------------------------------------------------------

def run_analysis(
    results_dir: Path,
    output_dir: Path,
    top_n: int = 200,
    dry_run: bool = False,
) -> Dict[str, Any]:
    output_dir.mkdir(parents=True, exist_ok=True)

    # --- Load data ---
    print("=== Data Loading ===")
    if dry_run:
        print("  [dry-run] Using mock data")
        all_scores = generate_mock_data()
        pipeline = None
    else:
        all_scores, pipeline = load_all_data(results_dir)

    if not all_scores:
        print("ERROR: No method scores available. Check --results-dir.")
        sys.exit(1)

    methods = sorted(all_scores.keys())
    K = len(methods)
    print(f"  Methods found: {methods} (K={K})")

    # --- Binarize ---
    print("\n=== Binarization ===")
    circuits: Dict[str, Set[str]] = {}
    for m in methods:
        circuits[m] = binarize_method(all_scores[m], m, top_n=top_n)
        print(f"  {m}: {len(circuits[m])} edges selected")

    all_edges: Set[str] = set()
    for c in circuits.values():
        all_edges |= c
    total_union = len(all_edges)

    # --- Per-method stats ---
    print(f"\n{'='*55}")
    print("=== MVP Results Analysis ===")
    print(f"{'='*55}")
    print(f"\nPer-method circuit size:")
    for m in methods:
        n = len(circuits[m])
        pct = n / total_union * 100 if total_union > 0 else 0
        print(f"  {m:<20s} {n:>5d} edges ({pct:5.1f}% of union {total_union})")

    # --- Pairwise Jaccard ---
    pairwise = compute_pairwise_css(circuits)
    print(f"\nPairwise CSS (Jaccard similarity):")
    for pair, val in pairwise.items():
        print(f"  {pair:<30s} {val:.4f}")

    # --- Full cross-tabulation ---
    css_result = compute_css_matrix_full(circuits)
    print(f"\nCross-tabulation (K={K}):")
    all_ones_key = str(tuple(1 for _ in range(K)))
    agree_in = css_result["agree_all_in"]
    off_diag = css_result["off_diagonal"]
    print(f"  {all_ones_key} all agree IN:   {agree_in:>5d} ({agree_in/total_union*100:5.1f}%)" if total_union else "")
    print(f"  off-diagonal:              {off_diag:>5d} ({off_diag/total_union*100:5.1f}%)" if total_union else "")
    off_diag_pct = css_result["off_diagonal_pct"]

    for cell_label, count in sorted(css_result["cell_counts"].items()):
        pct_str = f"{count/total_union*100:5.1f}%" if total_union else "N/A"
        print(f"    {cell_label}: {count:>5d} ({pct_str})")

    # --- CIRCUS tiers + cross-table (if primary method has continuous scores) ---
    primary = methods[0]
    tiers = compute_circus_tiers(all_scores[primary])
    tier_counts = Counter(tiers.values())
    print(f"\nCIRCUS tiers ({primary}):")
    for t in ("core", "contingent", "noise"):
        print(f"  {t}: {tier_counts.get(t, 0)}")

    xtab = compute_cross_table(tiers, circuits, css_threshold=0.67, K=K)
    print(f"\nCIRCUS-core x CSS cross-table:")
    print(f"  stable_core:    {xtab['stable_core']:>5d}")
    print(f"  method_specific:{xtab['method_specific']:>5d}")
    print(f"  cross_unstable: {xtab['cross_unstable']:>5d}")
    print(f"  noise:          {xtab['noise']:>5d}")
    print(f"  core off-diag:  {xtab['off_diagonal_pct']*100:.1f}%")

    # --- ACDC threshold sensitivity ---
    sensitivity = acdc_sensitivity(all_scores, top_n=top_n)
    if sensitivity:
        print(f"\nACDC threshold sensitivity:")
        for row in sensitivity:
            print(f"  τ={row['tau']:<5.2f}: off_diag={row['off_diagonal_pct']*100:5.1f}%, "
                  f"ACDC_size={row['acdc_size']}, union={row['total_union']}")

    # --- Gate judgment ---
    gate = gate_judgment(off_diag_pct)
    print(f"\n{'='*55}")
    print(f"=== MVP GATE: {gate['verdict']} ===")
    print(f"  {gate['action']}")
    print(f"{'='*55}")

    # --- Visualization ---
    print("\n=== Visualization ===")
    save_css_heatmap(pairwise, methods, output_dir / "css_heatmap.png")
    save_venn_or_bar(circuits, output_dir / "edge_overlap.png")

    # --- JSON output ---
    output = {
        "methods": methods,
        "K": K,
        "per_method_edges": {m: len(circuits[m]) for m in methods},
        "total_union": total_union,
        "pairwise_jaccard": pairwise,
        "css_cross_tabulation": {
            k: v for k, v in css_result.items()
            if k not in ("cell_counts",)
        },
        "css_cell_counts": css_result["cell_counts"],
        "off_diagonal_pct": off_diag_pct,
        "circus_tiers": dict(tier_counts),
        "circus_cross_table": xtab,
        "acdc_sensitivity": sensitivity,
        "gate": gate,
    }

    if pipeline:
        output["pipeline_summary"] = {
            k: v for k, v in pipeline.items()
            if k in ("config", "timings_sec", "css_distribution", "circus_tiers", "cross_table", "gate_verdict")
        }

    json_path = output_dir / "analysis_results.json"
    with open(json_path, "w") as f:
        json.dump(output, f, indent=2, default=str)
    print(f"\n  Saved JSON → {json_path}")

    return output


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="StructFuse MVP results analysis")
    parser.add_argument("--results-dir", type=str, default="/root/structfuse-context",
                        help="Directory containing cache files and/or mvp_results.json")
    parser.add_argument("--output-dir", type=str, default="./analysis",
                        help="Output directory for plots and JSON")
    parser.add_argument("--top-n", type=int, default=200,
                        help="Top-N edges for EAP-IG/IFR binarization")
    parser.add_argument("--dry-run", action="store_true",
                        help="Run with mock data to verify analysis pipeline")
    args = parser.parse_args()

    run_analysis(
        results_dir=Path(args.results_dir),
        output_dir=Path(args.output_dir),
        top_n=args.top_n,
        dry_run=args.dry_run,
    )


if __name__ == "__main__":
    main()
