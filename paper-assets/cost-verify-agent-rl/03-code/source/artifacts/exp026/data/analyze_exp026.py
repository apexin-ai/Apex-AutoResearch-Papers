#!/usr/bin/env python3
"""exp026 step-independent GRPO training analysis."""

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    HAS_MPL = True
except ImportError:
    HAS_MPL = False


# ---------------------------------------------------------------------------
# Log parsing
# ---------------------------------------------------------------------------

# Metric key aliases → canonical names
METRIC_ALIASES = {
    "success": "success_rate",
    "success_rate": "success_rate",
    "AlfworldSG/success": "success_rate",
    "alfworldsg/success": "success_rate",
    "unknown/success": "success_rate",

    "action_is_valid": "action_is_valid",
    "AlfworldSG/action_is_valid": "action_is_valid",
    "alfworldsg/action_is_valid": "action_is_valid",
    "unknown/action_is_valid": "action_is_valid",

    "pg_loss": "pg_loss",
    "actor/pg_loss": "pg_loss",

    "entropy": "entropy",
    "actor/entropy": "entropy",

    "kl_loss": "kl_divergence",
    "kl_divergence": "kl_divergence",
    "critic/kl_loss": "kl_divergence",
    "ppo_kl": "kl_divergence",
    "actor/kl_loss": "kl_divergence",

    "reward_mean": "reward_mean",
    "reward/mean": "reward_mean",
    "unknown/reward/mean": "reward_mean",

    "grad_norm": "grad_norm",
    "actor/grad_norm": "grad_norm",

    "pass@1": "pass_at_1",
    "pass@16": "pass_at_16",
    "effective": "effective",
}

# Patterns for RAGEN console log lines
# Format 1: "step:N prefix/metric: value"
RE_STEP_METRIC = re.compile(
    r"step[:\s]+(\d+)\s+"
    r"([\w/\-@.]+)"
    r"[:\s]+\s*"
    r"([+-]?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?)"
)

# Format 2: "prefix/metric@N: value" (val-core, val-aux, train-core etc.)
RE_PREFIXED_METRIC = re.compile(
    r"((?:val|train|test)[-_]?(?:core|aux|env)?)"
    r"/([\w/\-@.]+)"
    r"[:\s]+\s*"
    r"([+-]?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?)"
)

# Format 3: key=value pairs in a single line (tqdm-style)
RE_KV_PAIRS = re.compile(
    r"([\w/\-@.]+)\s*=\s*([+-]?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?)"
)

# Step header pattern (e.g. "Step 5/150", "step 5:", "Training step 5")
RE_STEP_HEADER = re.compile(r"(?:training\s+)?step\s*[:\s]\s*(\d+)", re.IGNORECASE)


def _canonicalize(key: str) -> str | None:
    """Map a raw metric key to its canonical name."""
    k = key.strip().lower()
    # Try exact match first
    for alias, canon in METRIC_ALIASES.items():
        if k == alias.lower():
            return canon
    # Try suffix match (handles arbitrary prefixes)
    for alias, canon in METRIC_ALIASES.items():
        if k.endswith("/" + alias.lower()) or k.endswith("/" + alias.lower().replace("/", "/")):
            return canon
    # Direct partial matches
    if "success" in k and "gate" not in k:
        return "success_rate"
    if "action_is_valid" in k or "action_valid" in k:
        return "action_is_valid"
    if "pg_loss" in k:
        return "pg_loss"
    if "entropy" in k:
        return "entropy"
    if k.endswith("kl_loss") or k.endswith("kl_divergence") or k == "ppo_kl":
        return "kl_divergence"
    if "reward" in k and "mean" in k:
        return "reward_mean"
    if "grad_norm" in k:
        return "grad_norm"
    return None


def parse_log(path: str) -> dict:
    """Parse RAGEN training log, return {split: {metric: [(step, value)]}}."""
    data = {"train": defaultdict(list), "val": defaultdict(list)}
    current_step = None
    current_split = "train"

    with open(path, "r", errors="replace") as f:
        for raw_line in f:
            line = raw_line.strip()
            if not line:
                continue

            # Detect split context
            low = line.lower()
            if "val_before_train" in low or "val-core" in low or "val-env" in low or "val-aux" in low:
                current_split = "val"
            elif "train-core" in low or "train-env" in low or "training step" in low.replace("validation", ""):
                if "val" not in low:
                    current_split = "train"

            # Try Format 1: step:N metric: value
            for m in RE_STEP_METRIC.finditer(line):
                step = int(m.group(1))
                raw_key = m.group(2)
                value = float(m.group(3))
                canon = _canonicalize(raw_key)
                if canon:
                    split = "val" if "val" in raw_key.lower() else current_split
                    data[split][canon].append((step, value))
                current_step = step

            # Try Format 2: prefix/metric@N: value
            for m in RE_PREFIXED_METRIC.finditer(line):
                prefix = m.group(1).lower()
                raw_key = m.group(2)
                value = float(m.group(3))
                canon = _canonicalize(raw_key)
                if canon:
                    split = "val" if "val" in prefix else "train"
                    step = current_step if current_step is not None else 0
                    data[split][canon].append((step, value))

            # Update current step from headers
            sh = RE_STEP_HEADER.search(line)
            if sh:
                new_step = int(sh.group(1))
                if new_step != current_step:
                    current_step = new_step
                    if "val" not in low:
                        current_split = "train"

            # Try Format 3: key=value pairs (fallback for tqdm lines)
            if "=" in line and current_step is not None:
                for m in RE_KV_PAIRS.finditer(line):
                    raw_key = m.group(1)
                    value = float(m.group(2))
                    canon = _canonicalize(raw_key)
                    if canon:
                        data[current_split][canon].append((current_step, value))

    # Deduplicate: keep last value per (step, metric) pair
    for split in data:
        for metric in data[split]:
            seen = {}
            for step, val in data[split][metric]:
                seen[step] = val
            data[split][metric] = sorted(seen.items())

    return data


# ---------------------------------------------------------------------------
# Statistics
# ---------------------------------------------------------------------------

SFT_BASELINE = 0.0625


def compute_stats(data: dict) -> dict:
    val_success = data["val"].get("success_rate", [])
    train_success = data["train"].get("success_rate", [])
    all_success = val_success if val_success else train_success

    best_val_step, best_val_success = -1, 0.0
    for step, val in all_success:
        if val > best_val_success:
            best_val_success = val
            best_val_step = step

    final_val_success = all_success[-1][1] if all_success else 0.0

    # Total steps
    all_steps = set()
    for split in data.values():
        for metric_data in split.values():
            for step, _ in metric_data:
                all_steps.add(step)
    total_steps = max(all_steps) if all_steps else 0

    # Convergence: first step where success > 20%
    convergence_step = None
    for step, val in sorted(all_success):
        if val > 0.20:
            convergence_step = step
            break

    # Entropy collapse: any window where entropy drops >30%
    entropy_data = data["train"].get("entropy", [])
    collapse_detected = False
    window = 5
    for i in range(len(entropy_data) - window):
        e_start = entropy_data[i][1]
        e_end = entropy_data[i + window][1]
        if e_start > 0 and (e_start - e_end) / e_start > 0.30:
            collapse_detected = True
            break

    # KL explosion
    kl_data = data["train"].get("kl_divergence", [])
    kl_explosion = any(v > 1.0 for _, v in kl_data)

    # pg_loss zero: 3+ consecutive steps
    pg_data = data["train"].get("pg_loss", [])
    pg_zero_detected = False
    zero_run = 0
    for _, v in pg_data:
        if abs(v) < 1e-8:
            zero_run += 1
            if zero_run >= 3:
                pg_zero_detected = True
                break
        else:
            zero_run = 0

    mvp_passed = best_val_success >= 0.20
    improvement = best_val_success / SFT_BASELINE if SFT_BASELINE > 0 else 0.0

    return {
        "exp_id": "exp026_step_independent_grpo",
        "total_steps": total_steps,
        "best_val_success": round(best_val_success, 4),
        "best_val_step": best_val_step,
        "final_val_success": round(final_val_success, 4),
        "convergence_step": convergence_step,
        "collapse_detected": collapse_detected,
        "kl_explosion_detected": kl_explosion,
        "pg_loss_zero_detected": pg_zero_detected,
        "mvp_passed": mvp_passed,
        "improvement_over_sft": f"{improvement:.1f}x",
    }


# ---------------------------------------------------------------------------
# Plotting
# ---------------------------------------------------------------------------

ENTROPY_COLLAPSE_THRESHOLD = 0.19


def plot_curves(data: dict, output_path: str):
    if not HAS_MPL:
        print("WARNING: matplotlib not available, skipping plot", file=sys.stderr)
        return

    metrics = [
        ("success_rate", "Success Rate", True),
        ("pg_loss", "PG Loss", False),
        ("entropy", "Entropy", False),
        ("kl_divergence", "KL Divergence", False),
        ("reward_mean", "Reward Mean", False),
        ("action_is_valid", "Action Is Valid", False),
    ]

    fig, axes = plt.subplots(2, 3, figsize=(18, 10))
    fig.suptitle("exp026 Step-Independent GRPO Training Curves", fontsize=14, fontweight="bold")
    axes = axes.flatten()

    for idx, (metric, title, show_both_splits) in enumerate(metrics):
        ax = axes[idx]
        train_pts = data["train"].get(metric, [])
        val_pts = data["val"].get(metric, [])

        if train_pts:
            steps, vals = zip(*train_pts)
            ax.plot(steps, vals, "b.-", label="train", alpha=0.8, markersize=4)

        if show_both_splits and val_pts:
            steps, vals = zip(*val_pts)
            ax.plot(steps, vals, "ro-", label="val", markersize=6, linewidth=2)

        if not show_both_splits and val_pts and not train_pts:
            steps, vals = zip(*val_pts)
            ax.plot(steps, vals, "ro-", label="val", markersize=6, linewidth=2)

        if metric == "entropy":
            ax.axhline(y=ENTROPY_COLLAPSE_THRESHOLD, color="r", linestyle="--",
                       alpha=0.6, label=f"collapse threshold ({ENTROPY_COLLAPSE_THRESHOLD})")

        if metric == "success_rate":
            ax.axhline(y=SFT_BASELINE, color="gray", linestyle=":", alpha=0.6,
                       label=f"SFT baseline ({SFT_BASELINE})")
            ax.axhline(y=0.20, color="green", linestyle="--", alpha=0.5, label="MVP target (20%)")

        if metric == "kl_divergence":
            ax.axhline(y=1.0, color="r", linestyle="--", alpha=0.5, label="KL explosion threshold")

        ax.set_title(title)
        ax.set_xlabel("Step")
        ax.set_ylabel(title)
        ax.legend(fontsize=8)
        ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    print(f"Saved plot: {output_path}")
    plt.close()


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Analyze exp026 RAGEN training log")
    parser.add_argument("--log", required=True, help="Path to training log file")
    parser.add_argument("--output", default=".", help="Output directory for artifacts")
    args = parser.parse_args()

    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Parsing log: {args.log}")
    data = parse_log(args.log)

    # Print parsed metric counts
    for split in ("train", "val"):
        metrics_found = {k: len(v) for k, v in data[split].items() if v}
        if metrics_found:
            print(f"  {split}: {metrics_found}")

    if not any(data[s] for s in data):
        print("ERROR: No metrics found in log. Check log format.", file=sys.stderr)
        sys.exit(1)

    # Compute stats
    stats = compute_stats(data)
    summary_path = output_dir / "exp026_summary.json"
    with open(summary_path, "w") as f:
        json.dump(stats, f, indent=2)
    print(f"Saved summary: {summary_path}")

    # Print key results
    print("\n--- Key Results ---")
    print(f"  Total steps:       {stats['total_steps']}")
    print(f"  Best val success:  {stats['best_val_success']:.2%} (step {stats['best_val_step']})")
    print(f"  Final val success: {stats['final_val_success']:.2%}")
    print(f"  Convergence step:  {stats['convergence_step'] or 'N/A (never > 20%)'}")
    print(f"  MVP passed:        {stats['mvp_passed']}")
    print(f"  vs SFT baseline:   {stats['improvement_over_sft']}")
    print(f"  Collapse detected: {stats['collapse_detected']}")
    print(f"  KL explosion:      {stats['kl_explosion_detected']}")
    print(f"  PG loss zero:      {stats['pg_loss_zero_detected']}")

    # Plot
    plot_path = output_dir / "exp026_training_curves.png"
    plot_curves(data, str(plot_path))


if __name__ == "__main__":
    main()
