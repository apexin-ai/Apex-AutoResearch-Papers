"""
exp-008 Signal Survival Analysis — main script (v3).

Analyzes how contamination detection signals survive across training regimes
(base → SFT-clean → SFT-contam → RL-aligned). Supports paper C2 claim:
"cliff-like signal degradation under RL alignment."

Input:
  - Per-regime signal directories from exp-002 compute_signals.py.
    Directory structure: {regime_dir}/{benchmark}/ containing
    signal_{type}_{benchmark}.json or signals_merged_{benchmark}.json.
    Record format: [{"index": int, "benchmark": str, "s1_embedding": float, ...}]
  - Contamination labels per benchmark: JSON {str(index): 0 | 1}
  - (Optional) RRF aggregated scores: rrf_{benchmark}.json or
    exposure_rrf_{benchmark}.json from aggregate_rrf.py

Output (to --output-dir):
  - per_benchmark/{benchmark}/survival_report.json
  - cliff_analysis.json — cliff vs gradual degradation detection
  - cross_benchmark_summary.json — aggregated statistics
  - Console summary table

Dependencies: numpy, scipy, sklearn
"""

import argparse
import json
import logging
import sys
from collections import OrderedDict
from pathlib import Path

import numpy as np
from scipy import stats
from sklearn.metrics import roc_auc_score

logger = logging.getLogger(__name__)

ALL_SIGNAL_KEYS = [
    "s1_embedding", "s2_minkpp", "s3_constat", "s4_selfcritique", "rrf_score",
]
SIGNAL_LABELS = {
    "s1_embedding": "Embedding",
    "s2_minkpp": "Min-K%++",
    "s3_constat": "ConStat",
    "s4_selfcritique": "Self-Critique",
    "rrf_score": "RRF (fused)",
}
DEFAULT_BENCHMARKS = ["mmlu", "gsm8k", "arc_challenge"]
CLIFF_THRESHOLD = 0.7


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------

def load_signals_for_benchmark(
    signals_dir: Path, benchmark: str,
) -> dict[str, list[dict]]:
    """Load all available signal files for one benchmark from a regime directory."""
    signals = {}

    merged_path = signals_dir / f"signals_merged_{benchmark}.json"
    if merged_path.exists():
        with open(merged_path) as f:
            merged = json.load(f)
        for sig_key in ALL_SIGNAL_KEYS:
            if any(sig_key in r for r in merged):
                signals[sig_key] = merged
        return signals

    prefix_map = {
        "s1_embedding": f"signal_embedding_{benchmark}",
        "s2_minkpp": f"signal_minkpp_{benchmark}",
        "s3_constat": f"signal_constat_{benchmark}",
        "s4_selfcritique": f"signal_selfcritique_{benchmark}",
    }
    for sig_key, prefix in prefix_map.items():
        fpath = signals_dir / f"{prefix}.json"
        if fpath.exists():
            with open(fpath) as f:
                signals[sig_key] = json.load(f)

    for rrf_name in [f"rrf_{benchmark}.json", f"exposure_rrf_{benchmark}.json"]:
        rrf_path = signals_dir / rrf_name
        if rrf_path.exists():
            with open(rrf_path) as f:
                signals["rrf_score"] = json.load(f)
            break

    return signals


def load_labels(labels_file: Path) -> dict[int, int]:
    with open(labels_file) as f:
        raw = json.load(f)
    return {int(k): int(v) for k, v in raw.items()}


# ---------------------------------------------------------------------------
# Statistical primitives
# ---------------------------------------------------------------------------

def cohens_d(group1: np.ndarray, group2: np.ndarray) -> float:
    n1, n2 = len(group1), len(group2)
    if n1 < 2 or n2 < 2:
        return float("nan")
    var1, var2 = group1.var(ddof=1), group2.var(ddof=1)
    pooled_std = np.sqrt(((n1 - 1) * var1 + (n2 - 1) * var2) / (n1 + n2 - 2))
    if pooled_std == 0:
        return float("nan")
    return float((group1.mean() - group2.mean()) / pooled_std)


def compute_auroc(values: np.ndarray, labels: np.ndarray) -> float | None:
    mask = ~(np.isnan(values) | np.isnan(labels))
    v, lab = values[mask], labels[mask].astype(int)
    if lab.sum() == 0 or (1 - lab).sum() == 0:
        return None
    return round(float(roc_auc_score(lab, v)), 4)


def _round_or_none(val, digits=4):
    if val is None or (isinstance(val, float) and np.isnan(val)):
        return None
    return round(val, digits)


# ---------------------------------------------------------------------------
# Vector extraction
# ---------------------------------------------------------------------------

def extract_aligned_vectors(
    regime_signals: OrderedDict,
    sig_key: str,
    regime_names: list[str],
    labels: dict[int, int],
) -> tuple[OrderedDict | None, np.ndarray | None]:
    """Extract per-regime signal vectors aligned by common item indices."""
    regime_maps = {}
    for rname in regime_names:
        data = regime_signals[rname].get(sig_key, [])
        regime_maps[rname] = {r["index"]: r.get(sig_key) for r in data}

    common_idx = set(labels.keys())
    for rname in regime_names:
        common_idx &= set(regime_maps[rname].keys())
    common_idx = sorted(common_idx)

    if len(common_idx) < 10:
        return None, None

    lab_arr = np.array([labels[i] for i in common_idx], dtype=float)
    vectors = OrderedDict()
    for rname in regime_names:
        vectors[rname] = np.array(
            [regime_maps[rname][i] for i in common_idx], dtype=float,
        )
    return vectors, lab_arr


# ---------------------------------------------------------------------------
# Pairwise metrics
# ---------------------------------------------------------------------------

def compute_pairwise_metrics(
    v_a: np.ndarray, v_b: np.ndarray, labels: np.ndarray,
) -> dict:
    """Statistical tests between two regime vectors for one signal."""
    mask = ~(np.isnan(v_a) | np.isnan(v_b) | np.isnan(labels))
    va, vb, lab = v_a[mask], v_b[mask], labels[mask].astype(int)
    contam, clean = lab == 1, lab == 0

    result = {
        "n_items": int(mask.sum()),
        "n_contaminated": int(contam.sum()),
        "n_clean": int(clean.sum()),
    }

    d_a = cohens_d(va[contam], va[clean])
    d_b = cohens_d(vb[contam], vb[clean])
    result["effect_size_a"] = _round_or_none(d_a)
    result["effect_size_b"] = _round_or_none(d_b)
    result["effect_size_ratio"] = (
        _round_or_none(d_b / d_a) if d_a != 0 and not np.isnan(d_a) else None
    )

    if contam.sum() > 0 and clean.sum() > 0:
        auc_a = roc_auc_score(lab, va)
        auc_b = roc_auc_score(lab, vb)
        result["auc_a"] = round(auc_a, 4)
        result["auc_b"] = round(auc_b, 4)
        result["auc_ratio"] = round(auc_b / auc_a, 4) if auc_a > 0 else None
    else:
        result["auc_a"] = result["auc_b"] = result["auc_ratio"] = None

    if len(va) >= 3:
        rho, rho_p = stats.spearmanr(va, vb)
        result["spearman_rho"] = round(float(rho), 4)
        result["spearman_p"] = float(f"{rho_p:.2e}")
    else:
        result["spearman_rho"] = result["spearman_p"] = None

    diffs = vb - va
    nonzero = diffs[diffs != 0]
    if len(nonzero) >= 10:
        w_stat, w_p = stats.wilcoxon(nonzero)
        result["wilcoxon_stat"] = float(w_stat)
        result["wilcoxon_p"] = float(f"{w_p:.2e}")
    else:
        result["wilcoxon_stat"] = result["wilcoxon_p"] = None

    return result


# ---------------------------------------------------------------------------
# Per-benchmark survival analysis
# ---------------------------------------------------------------------------

def analyze_signal_survival(
    regime_signals: OrderedDict,
    labels: dict[int, int],
) -> dict:
    """
    Survival analysis for one benchmark.

    Returns AUC matrix (signal × regime), effect-size matrix, pairwise tests
    between adjacent regimes, and survival classification.
    """
    regime_names = list(regime_signals.keys())

    all_sigs = set()
    for rname in regime_names:
        all_sigs |= set(regime_signals[rname].keys())
    signal_keys = [s for s in ALL_SIGNAL_KEYS if s in all_sigs]

    auc_matrix = {}
    effect_size_matrix = {}
    pairwise_tests = OrderedDict()
    adjacent = [
        (regime_names[i], regime_names[i + 1])
        for i in range(len(regime_names) - 1)
    ]
    for ra, rb in adjacent:
        pairwise_tests[f"{ra}_vs_{rb}"] = {}

    for sig_key in signal_keys:
        vectors, lab_arr = extract_aligned_vectors(
            regime_signals, sig_key, regime_names, labels,
        )
        if vectors is None:
            logger.warning("Skipping %s: <10 common items", sig_key)
            continue

        auc_matrix[sig_key] = {}
        effect_size_matrix[sig_key] = {}
        for rname in regime_names:
            v = vectors[rname]
            auc_matrix[sig_key][rname] = compute_auroc(v, lab_arr)
            contam, clean = lab_arr == 1, lab_arr == 0
            d = cohens_d(v[contam], v[clean])
            effect_size_matrix[sig_key][rname] = _round_or_none(d)

        for ra, rb in adjacent:
            pm = compute_pairwise_metrics(vectors[ra], vectors[rb], lab_arr)
            pm["signal_label"] = SIGNAL_LABELS.get(sig_key, sig_key)
            pairwise_tests[f"{ra}_vs_{rb}"][sig_key] = pm

    first_r, last_r = regime_names[0], regime_names[-1]
    surviving = []
    for sig in auc_matrix:
        auc_last = auc_matrix[sig].get(last_r)
        d_first = effect_size_matrix.get(sig, {}).get(first_r)
        d_last = effect_size_matrix.get(sig, {}).get(last_r)
        if (
            auc_last is not None and auc_last >= 0.6
            and d_first is not None and d_last is not None
            and d_first != 0 and abs(d_last / d_first) >= 0.5
        ):
            surviving.append(sig)

    return {
        "regime_names": regime_names,
        "auc_matrix": auc_matrix,
        "effect_size_matrix": effect_size_matrix,
        "pairwise_tests": dict(pairwise_tests),
        "n_signals_analyzed": len(auc_matrix),
        "n_signals_surviving": len(surviving),
        "surviving_signals": surviving,
    }


# ---------------------------------------------------------------------------
# Cliff detection
# ---------------------------------------------------------------------------

def detect_cliff_pattern(
    auc_trajectory: list[float | None],
    regime_names: list[str],
    threshold: float = CLIFF_THRESHOLD,
) -> dict:
    """
    Classify AUC trajectory as cliff-like or gradual.

    cliff_ratio = max_single_step_drop / total_drop.
    If cliff_ratio >= threshold, the degradation is concentrated at one
    transition ("cliff"); otherwise it is spread across transitions ("gradual").
    Total drop < 0.02 is classified as "stable" (signal preserved).
    """
    valid = [(i, v) for i, v in enumerate(auc_trajectory) if v is not None]
    if len(valid) < 2:
        return {"pattern": "insufficient_data", "cliff_ratio": None}

    indices = [v[0] for v in valid]
    values = [v[1] for v in valid]
    total_drop = values[0] - values[-1]

    deltas = []
    for k in range(len(values) - 1):
        drop = values[k] - values[k + 1]
        deltas.append({
            "from": regime_names[indices[k]],
            "to": regime_names[indices[k + 1]],
            "delta_auc": round(drop, 4),
        })

    if abs(total_drop) < 0.02:
        return {
            "pattern": "stable",
            "total_drop": round(total_drop, 4),
            "cliff_ratio": 0.0,
            "deltas": deltas,
        }

    max_drop = max(d["delta_auc"] for d in deltas)
    cliff_ratio = max_drop / total_drop if total_drop > 0 else 0.0
    cliff_idx = max(range(len(deltas)), key=lambda i: deltas[i]["delta_auc"])

    return {
        "pattern": "cliff" if cliff_ratio >= threshold else "gradual",
        "cliff_ratio": round(cliff_ratio, 4),
        "total_drop": round(total_drop, 4),
        "max_single_step_drop": round(max_drop, 4),
        "cliff_transition": (
            f"{deltas[cliff_idx]['from']} -> {deltas[cliff_idx]['to']}"
        ),
        "deltas": deltas,
    }


# ---------------------------------------------------------------------------
# Cross-benchmark aggregation
# ---------------------------------------------------------------------------

def aggregate_cross_benchmark(
    per_benchmark: dict, regime_names: list[str],
) -> dict:
    """Mean/std AUC per signal across benchmarks, plus survival counts."""
    signal_keys = set()
    for br in per_benchmark.values():
        signal_keys |= set(br.get("auc_matrix", {}).keys())
    signal_keys = sorted(signal_keys)

    aggregated = {}
    for sig in signal_keys:
        entry = {"label": SIGNAL_LABELS.get(sig, sig)}
        for rname in regime_names:
            vals = [
                br["auc_matrix"][sig][rname]
                for br in per_benchmark.values()
                if sig in br.get("auc_matrix", {})
                and br["auc_matrix"][sig].get(rname) is not None
            ]
            entry[f"mean_auc_{rname}"] = (
                round(float(np.mean(vals)), 4) if vals else None
            )
            entry[f"std_auc_{rname}"] = (
                round(float(np.std(vals, ddof=1)), 4) if len(vals) > 1 else None
            )
        aggregated[sig] = entry

    survival_counts = {}
    for sig in signal_keys:
        survival_counts[sig] = sum(
            1 for br in per_benchmark.values()
            if sig in br.get("surviving_signals", [])
        )

    return {
        "regime_names": regime_names,
        "benchmarks": list(per_benchmark.keys()),
        "per_signal_aggregated": aggregated,
        "survival_counts": survival_counts,
        "n_benchmarks": len(per_benchmark),
    }


# ---------------------------------------------------------------------------
# Mock data generation
# ---------------------------------------------------------------------------

def generate_mock_data(
    n_items: int = 200,
    regime_names: list[str] | None = None,
    benchmarks: list[str] | None = None,
    contamination_rate: float = 0.3,
    seed: int = 42,
) -> tuple:
    """
    Synthetic data for dry-run. Simulates different attenuation profiles:
    embedding (gradual decay), minkpp/constat/selfcritique (cliff at RL),
    rrf (moderate cliff). Returns (all_data, all_labels, regime_names).
    """
    if regime_names is None:
        regime_names = ["base", "sft_clean", "sft_contam", "rl_aligned"]
    if benchmarks is None:
        benchmarks = list(DEFAULT_BENCHMARKS)

    rng = np.random.RandomState(seed)

    attenuation = {
        "s1_embedding":     [1.0, 0.95, 0.90, 0.85],
        "s2_minkpp":        [1.0, 0.98, 0.95, 0.55],
        "s3_constat":       [1.0, 0.90, 0.80, 0.40],
        "s4_selfcritique":  [1.0, 0.92, 0.88, 0.35],
        "rrf_score":        [1.0, 0.95, 0.88, 0.50],
    }

    all_data = {}
    all_labels = {}

    for bench in benchmarks:
        n_contam = int(n_items * contamination_rate)
        labels = {i: (1 if i < n_contam else 0) for i in range(n_items)}
        all_labels[bench] = labels

        bench_regimes = OrderedDict()
        for r_idx, rname in enumerate(regime_names):
            bench_regimes[rname] = {}
            for sig_key in ALL_SIGNAL_KEYS:
                att = attenuation[sig_key]
                att_factor = att[min(r_idx, len(att) - 1)]
                records = []
                for i in range(n_items):
                    if labels[i] == 1:
                        base_val = rng.normal(0.75 * att_factor, 0.12)
                    else:
                        base_val = rng.normal(0.30, 0.12)
                    val = float(np.clip(base_val + rng.normal(0, 0.03), 0, 1))
                    records.append({
                        "index": i,
                        "benchmark": bench,
                        sig_key: round(val, 4),
                    })
                bench_regimes[rname][sig_key] = records
        all_data[bench] = bench_regimes

    return all_data, all_labels, regime_names


# ---------------------------------------------------------------------------
# Console output
# ---------------------------------------------------------------------------

def print_summary(per_benchmark, cliff_analysis, cross_benchmark, regime_names):
    col_w = 12
    divider = "=" * 80

    print(f"\n{divider}")
    print(
        f"Signal Survival Analysis -- "
        f"{len(regime_names)} regimes: {' -> '.join(regime_names)}"
    )
    print(divider)

    for bench, result in per_benchmark.items():
        auc_mat = result.get("auc_matrix", {})
        if not auc_mat:
            continue
        print(f"\n--- {bench.upper()} ---")
        header = f"{'Signal':<16}" + "".join(f"{r:>{col_w}}" for r in regime_names)
        print(header)
        print("-" * len(header))
        for sig in ALL_SIGNAL_KEYS:
            if sig not in auc_mat:
                continue
            vals = []
            for r in regime_names:
                v = auc_mat[sig].get(r)
                vals.append(f"{v:.4f}" if v is not None else "N/A")
            print(
                f"{SIGNAL_LABELS.get(sig, sig):<16}"
                + "".join(f"{v:>{col_w}}" for v in vals)
            )
        surv = result.get("surviving_signals", [])
        print(
            f"  Surviving: {len(surv)}/{result.get('n_signals_analyzed', 0)} "
            f"({', '.join(SIGNAL_LABELS.get(s, s) for s in surv) or 'none'})"
        )

    print(f"\n{divider}")
    print("Cliff Detection (threshold={:.2f})".format(CLIFF_THRESHOLD))
    print(divider)
    for sig in ALL_SIGNAL_KEYS:
        if sig not in cliff_analysis:
            continue
        bench_cliffs = cliff_analysis[sig]
        patterns = []
        ratios = []
        for bench, c in bench_cliffs.items():
            p = c.get("pattern", "?")
            patterns.append(f"{bench}={p}")
            r = c.get("cliff_ratio")
            if r is not None:
                ratios.append(r)
        mean_r = f"{np.mean(ratios):.3f}" if ratios else "N/A"
        transitions = set()
        for c in bench_cliffs.values():
            t = c.get("cliff_transition")
            if t:
                transitions.add(t)
        trans_str = ", ".join(transitions) if transitions else ""
        print(
            f"  {SIGNAL_LABELS.get(sig, sig):<16}  "
            f"mean_cliff_ratio={mean_r}  [{', '.join(patterns)}]"
            + (f"  at: {trans_str}" if trans_str else "")
        )

    agg = cross_benchmark.get("per_signal_aggregated", {})
    if agg:
        print(f"\n{divider}")
        print("Cross-benchmark Mean AUC")
        print(divider)
        header = f"{'Signal':<16}" + "".join(f"{r:>{col_w}}" for r in regime_names)
        print(header)
        print("-" * len(header))
        for sig in ALL_SIGNAL_KEYS:
            if sig not in agg:
                continue
            vals = []
            for r in regime_names:
                v = agg[sig].get(f"mean_auc_{r}")
                vals.append(f"{v:.4f}" if v is not None else "N/A")
            print(
                f"{SIGNAL_LABELS.get(sig, sig):<16}"
                + "".join(f"{v:>{col_w}}" for v in vals)
            )

    print(f"{divider}\n")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description=(
            "exp-008: Signal Survival Analysis — per-benchmark breakdown "
            "with cliff detection and RRF support"
        ),
    )
    parser.add_argument(
        "--regime-dirs", nargs="+", metavar="NAME=PATH",
        help=(
            "Regime signal directories as NAME=PATH pairs (order matters). "
            "Under each path: {benchmark}/ subdirectories with signal files."
        ),
    )
    parser.add_argument(
        "--benchmarks", nargs="+", default=DEFAULT_BENCHMARKS,
        help="Benchmarks to analyze (default: mmlu gsm8k arc_challenge)",
    )
    parser.add_argument(
        "--labels-dir", type=str,
        help="Directory containing labels_{benchmark}.json files",
    )
    parser.add_argument("--output-dir", type=str, default="./exp008_output")
    parser.add_argument(
        "--cliff-threshold", type=float, default=CLIFF_THRESHOLD,
        help="Cliff ratio threshold for pattern classification (default: 0.7)",
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Generate and analyze synthetic mock data for validation",
    )
    parser.add_argument("--max-items", type=int, default=None)
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
    )

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # --- Load data ---
    if args.dry_run:
        logger.info(
            "DRY-RUN: generating mock data (%d items)",
            args.max_items or 200,
        )
        all_data, all_labels, regime_names = generate_mock_data(
            n_items=args.max_items or 200,
        )
        benchmarks = list(all_data.keys())
    else:
        if not args.regime_dirs:
            parser.error("--regime-dirs required (or use --dry-run)")
        if not args.labels_dir:
            parser.error("--labels-dir required")

        regime_dirs = OrderedDict()
        for arg in args.regime_dirs:
            if "=" not in arg:
                sys.exit(f"Invalid regime-dir '{arg}': expected NAME=PATH")
            name, path = arg.split("=", 1)
            regime_dirs[name] = Path(path)
        regime_names = list(regime_dirs.keys())
        benchmarks = args.benchmarks

        all_data = {}
        all_labels = {}
        labels_dir = Path(args.labels_dir)
        for bench in benchmarks:
            lpath = labels_dir / f"labels_{bench}.json"
            if not lpath.exists():
                logger.warning("Labels not found: %s, skipping %s", lpath, bench)
                continue
            all_labels[bench] = load_labels(lpath)
            bench_regimes = OrderedDict()
            for rname, rdir in regime_dirs.items():
                bench_dir = rdir / bench
                if not bench_dir.is_dir():
                    bench_dir = rdir
                logger.info("Loading %s / %s from %s", rname, bench, bench_dir)
                bench_regimes[rname] = load_signals_for_benchmark(bench_dir, bench)
            all_data[bench] = bench_regimes
        benchmarks = [b for b in benchmarks if b in all_labels]

    if not benchmarks:
        sys.exit("No benchmarks to analyze.")

    # --- Per-benchmark survival analysis ---
    per_benchmark = {}
    for bench in benchmarks:
        logger.info("Analyzing: %s", bench)
        result = analyze_signal_survival(all_data[bench], all_labels[bench])
        per_benchmark[bench] = result

        bench_out = output_dir / "per_benchmark" / bench
        bench_out.mkdir(parents=True, exist_ok=True)
        with open(bench_out / "survival_report.json", "w") as f:
            json.dump(result, f, indent=2)

    # --- Cliff detection ---
    cliff_analysis = {}
    for sig in ALL_SIGNAL_KEYS:
        per_bench_cliff = {}
        for bench, result in per_benchmark.items():
            trajectory = [
                result.get("auc_matrix", {}).get(sig, {}).get(r)
                for r in regime_names
            ]
            per_bench_cliff[bench] = detect_cliff_pattern(
                trajectory, regime_names, threshold=args.cliff_threshold,
            )
        if per_bench_cliff:
            cliff_analysis[sig] = per_bench_cliff

    with open(output_dir / "cliff_analysis.json", "w") as f:
        json.dump(cliff_analysis, f, indent=2)

    # --- Cross-benchmark aggregation ---
    cross_benchmark = aggregate_cross_benchmark(per_benchmark, regime_names)
    with open(output_dir / "cross_benchmark_summary.json", "w") as f:
        json.dump(cross_benchmark, f, indent=2)

    # --- Console summary ---
    print_summary(per_benchmark, cliff_analysis, cross_benchmark, regime_names)

    logger.info("All outputs saved to %s", output_dir)


if __name__ == "__main__":
    main()
