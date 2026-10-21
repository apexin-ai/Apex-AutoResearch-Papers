"""
exp-008: Signal Survival Analysis — main orchestration script.

Evaluates how 4 contamination detection signals degrade across training regimes:
  base (pretrained) → SFT-clean (d000) → SFT-contam (d005) → RL-aligned (Instruct)

Workflow:
  1. Load existing exp-002 signals for SFT regimes (d000, d005 from exp-002 outputs)
  2. Compute signals for base + RL-aligned regimes (via compute_signals_on_model.py)
  3. Load d005 contamination labels as ground truth (mixed 0/1 — AUC-computable)
  4. Run AUC analysis + heatmap + bootstrap CI via analyze_survival.py

Usage:
  # Full run (compute new signals + analyze)
  python run_signal_survival.py --gpu 0

  # Analysis only (skip signal computation, use existing data)
  python run_signal_survival.py --skip-compute

  # Dry-run with mock data
  python run_signal_survival.py --dry-run

  # Use exp-002 data only (3-regime: d000/d005/d100, no base/RL)
  python run_signal_survival.py --exp002-only

Dependencies: numpy, scipy, sklearn, matplotlib
"""

import argparse
import json
import logging
import sys
from collections import OrderedDict
from pathlib import Path

import numpy as np

logger = logging.getLogger(__name__)

# ── Path conventions ──
CHECKPOINT_ROOT = Path("/root/autodl-tmp/exp001/checkpoints")
SFT_DATA_ROOT = Path("/root/autodl-tmp/exp001/sft_data")
EXP002_SIGNALS = Path("/root/autodl-tmp/exp002/signals")
EXP008_OUTPUT = Path("/root/autodl-tmp/exp008")
CACHE_DIR = "/root/autodl-tmp/.hf_cache"

BASE_MODEL = "/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B"
INSTRUCT_MODEL = "/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B-Instruct"
D000_ADAPTER = str(CHECKPOINT_ROOT / "Qwen2.5-0.5B_d000_s42/lora_adapter")
D005_ADAPTER = str(CHECKPOINT_ROOT / "Qwen2.5-0.5B_d005_s42/lora_adapter")

BENCHMARKS = ["mmlu", "gsm8k", "arc_challenge"]
SEED = "s42"

# Ground truth uses d005 labels: 5% contaminated → mixed 0/1 → AUC computable
LABELS_DOSAGE = "d005"

SIGNAL_KEYS = ["s1_embedding", "s2_minkpp", "s3_constat", "s4_selfcritique"]


# ── Regime definitions ──

def get_regime_config(exp002_only: bool = False) -> OrderedDict:
    """Define training regimes with signal source paths."""
    if exp002_only:
        return OrderedDict([
            ("SFT-clean\n(d000)", {
                "source": "exp002",
                "signals_dir": EXP002_SIGNALS / "Qwen2.5-0.5B_d000_s42",
            }),
            ("SFT-contam\n(d005)", {
                "source": "exp002",
                "signals_dir": EXP002_SIGNALS / "Qwen2.5-0.5B_d005_s42",
            }),
            ("SFT-contam\n(d100)", {
                "source": "exp002",
                "signals_dir": EXP002_SIGNALS / "Qwen2.5-0.5B_d100_s42",
            }),
        ])

    return OrderedDict([
        ("Base\n(pretrained)", {
            "source": "compute",
            "model_path": BASE_MODEL,
            "ref_model_path": BASE_MODEL,
            "signals_dir": EXP008_OUTPUT / "signals" / "base",
        }),
        ("SFT-clean\n(d000)", {
            "source": "exp002",
            "signals_dir": EXP002_SIGNALS / "Qwen2.5-0.5B_d000_s42",
        }),
        ("SFT-contam\n(d005)", {
            "source": "exp002",
            "signals_dir": EXP002_SIGNALS / "Qwen2.5-0.5B_d005_s42",
        }),
        ("RL-aligned\n(Instruct)", {
            "source": "compute",
            "model_path": INSTRUCT_MODEL,
            "ref_model_path": BASE_MODEL,
            "signals_dir": EXP008_OUTPUT / "signals" / "rl_aligned",
        }),
    ])


# ── Data loading ──

def load_labels_for_benchmark(benchmark: str) -> dict[int, int]:
    """Load d005 contamination labels, converting list format to {index: label}."""
    labels_path = SFT_DATA_ROOT / f"contamination_labels_{benchmark}_{LABELS_DOSAGE}.json"
    if not labels_path.exists():
        raise FileNotFoundError(f"Labels not found: {labels_path}")

    with open(labels_path) as f:
        raw = json.load(f)

    if isinstance(raw, dict) and "labels" in raw:
        return {i: int(v) for i, v in enumerate(raw["labels"])}
    elif isinstance(raw, dict):
        return {int(k): int(v) for k, v in raw.items()}
    elif isinstance(raw, list):
        return {i: int(v) for i, v in enumerate(raw)}
    else:
        raise ValueError(f"Unexpected labels format in {labels_path}")


def load_signals_from_dir(
    signals_dir: Path, benchmark: str,
) -> dict[str, list[dict]]:
    """Load signal data for one benchmark from a directory.

    Handles both flat (exp-002) and nested (exp-008) directory layouts:
      flat:   {signals_dir}/signals_merged_{benchmark}.json
      nested: {signals_dir}/{benchmark}/signals_merged_{benchmark}.json
    """
    for base in [signals_dir, signals_dir / benchmark]:
        merged_path = base / f"signals_merged_{benchmark}.json"
        if merged_path.exists():
            with open(merged_path) as f:
                records = json.load(f)
            signals = {}
            for key in SIGNAL_KEYS:
                if any(key in r for r in records):
                    signals[key] = records
            logger.info(
                "Loaded %s [%s]: %d items, %d signals",
                signals_dir.name, benchmark, len(records), len(signals),
            )
            return signals

    # Fallback: individual signal files
    signals = {}
    prefix_map = {
        "s1_embedding": f"signal_embedding_{benchmark}",
        "s2_minkpp": f"signal_minkpp_{benchmark}",
        "s3_constat": f"signal_constat_{benchmark}",
        "s4_selfcritique": f"signal_selfcritique_{benchmark}",
    }
    for base in [signals_dir, signals_dir / benchmark]:
        for sig_key, prefix in prefix_map.items():
            if sig_key in signals:
                continue
            fpath = base / f"{prefix}.json"
            if fpath.exists():
                with open(fpath) as f:
                    signals[sig_key] = json.load(f)

    if signals:
        logger.info(
            "Loaded %s [%s]: %d signals (individual files)",
            signals_dir.name, benchmark, len(signals),
        )
    else:
        logger.warning("No signals found in %s for %s", signals_dir, benchmark)
    return signals


def compute_regime_signals(regime_cfg: dict, benchmarks: list[str], gpu: str | None):
    """Compute signals for a regime that needs fresh computation."""
    from compute_signals_on_model import compute_all_signals

    for benchmark in benchmarks:
        bench_output = Path(regime_cfg["signals_dir"]) / benchmark
        merged = bench_output / f"signals_merged_{benchmark}.json"
        if merged.exists():
            logger.info("Skipping computation (cached): %s / %s", regime_cfg["signals_dir"].name, benchmark)
            continue

        logger.info("Computing signals: %s / %s", regime_cfg["model_path"], benchmark)
        import os
        if gpu is not None:
            os.environ["CUDA_VISIBLE_DEVICES"] = gpu
        import torch
        device = "cuda" if torch.cuda.is_available() else "cpu"

        compute_all_signals(
            model_path=regime_cfg["model_path"],
            ref_model_path=regime_cfg["ref_model_path"],
            sft_data_path=str(SFT_DATA_ROOT / f"sft_dosage_005.jsonl"),
            benchmark=benchmark,
            output_dir=bench_output,
            signals=["embedding", "minkpp", "selfcritique"],
            device=device,
            cache_dir=CACHE_DIR,
        )


def generate_mock_data(
    n_items: int = 200,
    regime_names: list[str] | None = None,
    seed: int = 42,
) -> tuple[dict, dict, list[str]]:
    """Generate synthetic data for dry-run validation.

    Returns: (all_data, all_labels, regime_names)
      all_data: {benchmark: {regime_name: {signal_key: [records]}}}
      all_labels: {benchmark: {item_index: 0|1}}
    """
    if regime_names is None:
        regime_names = ["Base", "SFT-clean", "SFT-contam", "RL-aligned"]

    rng = np.random.RandomState(seed)
    n_contam = int(n_items * 0.05)  # 5% contamination like d005

    benchmarks = ["mmlu", "gsm8k", "arc_challenge"]
    all_labels = {}
    all_data = {}

    for bench in benchmarks:
        labels = {i: (1 if i < n_contam else 0) for i in range(n_items)}
        all_labels[bench] = labels

        bench_regimes = OrderedDict()
        for r_idx, rname in enumerate(regime_names):
            regime_signals = {}
            for sig_key in SIGNAL_KEYS:
                if sig_key == "s3_constat":
                    continue
                records = []
                for i in range(n_items):
                    if labels[i] == 1:
                        # Signal strength decays with regime progression
                        base_val = rng.normal(0.75, 0.1)
                        decay = 0.15 * r_idx
                        val = base_val - decay + rng.normal(0, 0.05)
                    else:
                        val = rng.normal(0.4, 0.15)
                    records.append({
                        "index": i,
                        "benchmark": bench,
                        sig_key: float(np.clip(val, 0, 1)),
                    })
                regime_signals[sig_key] = records
            bench_regimes[rname] = regime_signals
        all_data[bench] = bench_regimes

    return all_data, all_labels, regime_names


# ── Main ──

def main():
    parser = argparse.ArgumentParser(
        description="exp-008: Signal Survival Analysis across training regimes"
    )
    parser.add_argument("--gpu", type=str, default=None)
    parser.add_argument("--output-dir", type=str,
                        default=str(EXP008_OUTPUT / "results"))
    parser.add_argument("--benchmarks", type=str, nargs="+", default=BENCHMARKS)
    parser.add_argument("--skip-compute", action="store_true",
                        help="Skip signal computation, use existing data only")
    parser.add_argument("--exp002-only", action="store_true",
                        help="Use only exp-002 SFT regimes (d000/d005/d100)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Use synthetic mock data for pipeline validation")
    parser.add_argument("--max-items", type=int, default=None,
                        help="Limit items per benchmark (for debugging)")
    parser.add_argument("--n-bootstrap", type=int, default=1000,
                        help="Bootstrap iterations for CI computation")
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
    )

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    if args.dry_run:
        logger.info("DRY-RUN: generating mock data")
        all_data, all_labels, regime_names = generate_mock_data(
            n_items=args.max_items or 200,
        )
        benchmarks = list(all_data.keys())
    else:
        regime_config = get_regime_config(exp002_only=args.exp002_only)
        regime_names = list(regime_config.keys())
        benchmarks = args.benchmarks

        # Step 1: Compute signals for regimes that need it
        if not args.skip_compute:
            for rname, rcfg in regime_config.items():
                if rcfg["source"] == "compute":
                    logger.info("Computing signals for regime: %s", rname)
                    compute_regime_signals(rcfg, benchmarks, args.gpu)

        # Step 2: Load all signals
        all_data = {}
        all_labels = {}
        for bench in benchmarks:
            try:
                all_labels[bench] = load_labels_for_benchmark(bench)
            except FileNotFoundError as e:
                logger.warning("Skipping %s: %s", bench, e)
                continue

            bench_regimes = OrderedDict()
            for rname, rcfg in regime_config.items():
                signals = load_signals_from_dir(rcfg["signals_dir"], bench)
                if not signals:
                    logger.warning("No signals for %s / %s, inserting empty", rname, bench)
                bench_regimes[rname] = signals
            all_data[bench] = bench_regimes

        benchmarks = [b for b in benchmarks if b in all_labels and b in all_data]

    if not benchmarks:
        sys.exit("No benchmarks with both signals and labels found.")

    # Step 3: Data summary
    logger.info("=" * 60)
    logger.info("exp-008 Signal Survival Analysis")
    logger.info("=" * 60)
    logger.info("Regimes: %s", regime_names)
    logger.info("Benchmarks: %s", benchmarks)
    for bench in benchmarks:
        labels = all_labels[bench]
        n_pos = sum(v for v in labels.values())
        n_total = len(labels)
        logger.info(
            "  %s: %d items, %d contaminated (%.1f%%)",
            bench, n_total, n_pos, 100 * n_pos / n_total,
        )
        for rname in regime_names:
            sigs = all_data[bench].get(rname, {})
            sig_names = [k for k in SIGNAL_KEYS if k in sigs]
            logger.info("    %s: %s", rname.replace("\n", " "), sig_names)

    # Step 4: Run analysis
    from analyze_survival import (
        compute_auc_matrix,
        compute_bootstrap_ci,
        plot_auc_heatmap,
        plot_signal_trajectory,
        save_analysis_report,
    )

    auc_results = {}
    bootstrap_results = {}

    for bench in benchmarks:
        logger.info("--- Analyzing: %s ---", bench)
        labels = all_labels[bench]
        regime_signals = all_data[bench]

        auc_matrix = compute_auc_matrix(regime_signals, labels, regime_names)
        auc_results[bench] = auc_matrix

        ci_matrix = compute_bootstrap_ci(
            regime_signals, labels, regime_names,
            n_bootstrap=args.n_bootstrap, max_items=args.max_items,
        )
        bootstrap_results[bench] = ci_matrix

    # Step 5: Output
    report = {
        "regime_names": regime_names,
        "benchmarks": benchmarks,
        "auc_results": auc_results,
        "bootstrap_ci": bootstrap_results,
        "labels_dosage": LABELS_DOSAGE,
    }
    save_analysis_report(report, output_dir)

    # Aggregate across benchmarks for heatmap
    agg_auc = _aggregate_auc(auc_results, regime_names, benchmarks)
    agg_ci = _aggregate_ci(bootstrap_results, regime_names, benchmarks)

    plot_auc_heatmap(agg_auc, agg_ci, regime_names, output_dir / "survival_auc_heatmap.pdf")
    plot_signal_trajectory(agg_auc, regime_names, output_dir / "signal_trajectory.pdf")

    # Per-benchmark heatmaps
    for bench in benchmarks:
        plot_auc_heatmap(
            auc_results[bench], bootstrap_results[bench], regime_names,
            output_dir / f"auc_heatmap_{bench}.pdf",
            title_suffix=f" ({bench})",
        )

    _print_summary(agg_auc, agg_ci, regime_names, benchmarks)
    logger.info("All outputs saved to %s", output_dir)


def _aggregate_auc(
    per_bench: dict, regime_names: list[str], benchmarks: list[str],
) -> dict[str, dict[str, float | None]]:
    """Average AUC across benchmarks for each signal × regime."""
    agg = {}
    for sig_key in SIGNAL_KEYS:
        agg[sig_key] = {}
        for rname in regime_names:
            values = [
                per_bench[b][sig_key][rname]
                for b in benchmarks
                if sig_key in per_bench[b] and rname in per_bench[b][sig_key]
                and per_bench[b][sig_key][rname] is not None
            ]
            agg[sig_key][rname] = round(float(np.mean(values)), 4) if values else None
    return agg


def _aggregate_ci(
    per_bench: dict, regime_names: list[str], benchmarks: list[str],
) -> dict[str, dict[str, tuple[float, float] | None]]:
    """Average bootstrap CI across benchmarks."""
    agg = {}
    for sig_key in SIGNAL_KEYS:
        agg[sig_key] = {}
        for rname in regime_names:
            lows, highs = [], []
            for b in benchmarks:
                if sig_key in per_bench.get(b, {}) and rname in per_bench[b].get(sig_key, {}):
                    ci = per_bench[b][sig_key][rname]
                    if ci is not None:
                        lows.append(ci[0])
                        highs.append(ci[1])
            if lows:
                agg[sig_key][rname] = (round(float(np.mean(lows)), 4), round(float(np.mean(highs)), 4))
            else:
                agg[sig_key][rname] = None
    return agg


def _print_summary(agg_auc, agg_ci, regime_names, benchmarks):
    """Print summary table to console."""
    sig_labels = {
        "s1_embedding": "Embedding",
        "s2_minkpp": "Min-K%++",
        "s3_constat": "ConStat",
        "s4_selfcritique": "Self-Critique",
    }

    clean_names = [r.replace("\n", " ") for r in regime_names]
    col_w = 18
    sig_w = 14

    header = f"{'Signal':<{sig_w}} " + " ".join(f"{n:>{col_w}}" for n in clean_names)
    print("\n" + "=" * len(header))
    print(f"Signal Survival: Mean AUC across {benchmarks}")
    print("=" * len(header))
    print(header)
    print("-" * len(header))

    for sig_key in SIGNAL_KEYS:
        if sig_key not in agg_auc:
            continue
        label = sig_labels.get(sig_key, sig_key)
        parts = [f"{label:<{sig_w}}"]
        for rname in regime_names:
            v = agg_auc[sig_key].get(rname)
            ci = agg_ci.get(sig_key, {}).get(rname)
            if v is not None and ci is not None:
                s = f"{v:.3f} [{ci[0]:.3f},{ci[1]:.3f}]"
            elif v is not None:
                s = f"{v:.3f}"
            else:
                s = "N/A"
            parts.append(f"{s:>{col_w}}")
        print(" ".join(parts))

    print("=" * len(header))

    # Signal degradation summary
    for sig_key in SIGNAL_KEYS:
        if sig_key not in agg_auc or len(regime_names) < 2:
            continue
        first_rname = regime_names[0]
        last_rname = regime_names[-1]
        v_first = agg_auc[sig_key].get(first_rname)
        v_last = agg_auc[sig_key].get(last_rname)
        if v_first is not None and v_last is not None:
            delta = v_last - v_first
            label = sig_labels.get(sig_key, sig_key)
            print(f"  {label}: {v_first:.3f} -> {v_last:.3f} (delta={delta:+.3f})")

    print()


if __name__ == "__main__":
    main()
