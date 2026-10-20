"""
exp-008 Signal Survival — end-to-end execution script.
v2: Extended from SFT/RL pairwise to N-regime comparison.

Usage:
  python run_signal_survival.py \
    --regime-dirs base=/path/base SFT_clean=/path/sft RL=/path/rl \
    --labels-file /path/to/labels.json \
    --output-dir /path/to/exp008_output/

  # Legacy 2-regime (still works):
  python run_signal_survival.py \
    --sft-signals-dir /path/sft/ --rl-signals-dir /path/rl/ \
    --labels-file labels.json

  # Quick validation with mock data:
  python run_signal_survival.py --dry-run --max-items 10
  python run_signal_survival.py --dry-run --max-items 10 --regime-names base SFT RL DPO

Dependencies: numpy, scipy, sklearn
"""

import argparse
import json
import logging
import sys
from collections import OrderedDict
from pathlib import Path

import numpy as np

from signal_survival_analysis import (
    SIGNAL_KEYS,
    print_summary_table,
    run_survival_analysis,
    save_report,
)

logger = logging.getLogger(__name__)


def load_signal_file(path: Path, signal_key: str) -> list[dict]:
    """Load a signal JSON file and validate it has expected fields."""
    with open(path) as f:
        data = json.load(f)
    if not isinstance(data, list) or len(data) == 0:
        raise ValueError(f"Expected non-empty list in {path}")
    if signal_key not in data[0]:
        raise ValueError(f"Signal key '{signal_key}' not found in {path}")
    return data


def load_signals_from_dir(signals_dir: Path) -> dict[str, list[dict]]:
    """
    Load all signal files from a directory.
    Returns {signal_key: [records]}.
    """
    signals = {}

    merged_files = list(signals_dir.glob("signals_merged_*.json"))
    if merged_files:
        logger.info("Found merged signal file: %s", merged_files[0])
        with open(merged_files[0]) as f:
            merged = json.load(f)
        for sig_key in SIGNAL_KEYS:
            if any(sig_key in r for r in merged):
                signals[sig_key] = merged
        return signals

    key_to_filename_prefix = {
        "s1_embedding": "signal_embedding_",
        "s2_minkpp": "signal_minkpp_",
        "s3_constat": "signal_constat_",
        "s4_selfcritique": "signal_selfcritique_",
    }
    for sig_key, prefix in key_to_filename_prefix.items():
        matches = list(signals_dir.glob(f"{prefix}*.json"))
        if matches:
            signals[sig_key] = load_signal_file(matches[0], sig_key)
            logger.info("Loaded %s from %s (%d items)", sig_key, matches[0], len(signals[sig_key]))
        else:
            logger.warning("No file found for %s in %s", sig_key, signals_dir)

    return signals


def load_labels(labels_file: Path) -> dict[int, int]:
    """Load contamination labels: {item_index: 0 or 1}."""
    with open(labels_file) as f:
        raw = json.load(f)
    return {int(k): int(v) for k, v in raw.items()}


def parse_regime_dirs(regime_dir_args: list[str]) -> OrderedDict:
    """Parse key=value regime dir arguments into OrderedDict."""
    regimes = OrderedDict()
    for arg in regime_dir_args:
        if "=" not in arg:
            raise ValueError(f"Invalid regime-dir format: '{arg}'. Expected NAME=PATH")
        name, path = arg.split("=", 1)
        regimes[name] = Path(path)
    return regimes


def generate_mock_data(
    n_items: int = 100,
    contamination_rate: float = 0.3,
    seed: int = 42,
    regime_names: list[str] | None = None,
) -> tuple:
    """
    Generate synthetic signal data for N regimes.
    Each subsequent regime attenuates the signal via a chain model:
      regime[k] = 0.6 * regime[k-1] + 0.4 * noise.
    For N=2 with default names ["SFT","RL"], random draws match the original.
    """
    if regime_names is None:
        regime_names = ["SFT", "RL"]

    rng = np.random.RandomState(seed)
    n_contam = int(n_items * contamination_rate)
    labels = {i: (1 if i < n_contam else 0) for i in range(n_items)}

    regime_signals: OrderedDict[str, dict] = OrderedDict()
    for name in regime_names:
        regime_signals[name] = {}

    for sig_key in SIGNAL_KEYS:
        for name in regime_names:
            regime_signals[name][sig_key] = []

        for i in range(n_items):
            base = rng.normal(0.7, 0.15) if labels[i] == 1 else rng.normal(0.3, 0.15)
            prev_val = float(np.clip(base, 0, 1))
            regime_signals[regime_names[0]][sig_key].append(
                {"index": i, "benchmark": "mock", sig_key: round(prev_val, 4)}
            )
            for r_idx in range(1, len(regime_names)):
                noise = rng.normal(0.5, 0.2)
                cur_val = float(np.clip(0.6 * prev_val + 0.4 * noise, 0, 1))
                regime_signals[regime_names[r_idx]][sig_key].append(
                    {"index": i, "benchmark": "mock", sig_key: round(cur_val, 4)}
                )
                prev_val = cur_val

    return regime_signals, labels


def main():
    parser = argparse.ArgumentParser(
        description="exp-008: Signal Survival Analysis — N-regime comparison"
    )
    parser.add_argument(
        "--regime-dirs", nargs="+", metavar="NAME=PATH",
        help="Regime directories as name=path pairs (order defines adjacency)",
    )
    parser.add_argument("--sft-signals-dir", type=str, help="(Legacy) SFT signals directory")
    parser.add_argument("--rl-signals-dir", type=str, help="(Legacy) RL signals directory")
    parser.add_argument("--labels-file", type=str,
                        help="JSON file with contamination labels {index: 0/1}")
    parser.add_argument("--output-dir", type=str, default="./exp008_output")
    parser.add_argument("--dry-run", action="store_true",
                        help="Use synthetic mock data for validation")
    parser.add_argument("--max-items", type=int, default=None,
                        help="Limit number of items (for dry-run or debugging)")
    parser.add_argument("--regime-names", nargs="+", default=None,
                        help="Regime names for dry-run (default: SFT RL)")
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
    )

    if args.dry_run:
        max_items = args.max_items or 100
        regime_names = args.regime_names or ["SFT", "RL"]
        logger.info(
            "DRY-RUN: generating mock data with %d items, %d regimes: %s",
            max_items, len(regime_names), regime_names,
        )
        regime_signals, labels = generate_mock_data(
            n_items=max_items, regime_names=regime_names,
        )
    else:
        if args.regime_dirs:
            regime_dirs = parse_regime_dirs(args.regime_dirs)
        elif args.sft_signals_dir and args.rl_signals_dir:
            regime_dirs = OrderedDict([
                ("SFT", Path(args.sft_signals_dir)),
                ("RL", Path(args.rl_signals_dir)),
            ])
        else:
            parser.error(
                "Provide --regime-dirs or legacy --sft-signals-dir/--rl-signals-dir"
            )
            return

        if not args.labels_file:
            parser.error("--labels-file is required")

        regime_signals = OrderedDict()
        for name, dirpath in regime_dirs.items():
            if not dirpath.is_dir():
                sys.exit(f"Regime '{name}' dir not found: {dirpath}")
            logger.info("Loading signals for regime '%s' from %s", name, dirpath)
            regime_signals[name] = load_signals_from_dir(dirpath)

        labels = load_labels(Path(args.labels_file))

    if args.max_items and not args.dry_run:
        for regime_name in regime_signals:
            for sig_key in list(regime_signals[regime_name].keys()):
                regime_signals[regime_name][sig_key] = (
                    regime_signals[regime_name][sig_key][: args.max_items]
                )

    logger.info("Running survival analysis...")
    report = run_survival_analysis(regime_signals, labels)

    save_report(report, args.output_dir)
    print_summary_table(report)

    logger.info("Done. Output in %s", args.output_dir)


if __name__ == "__main__":
    main()
