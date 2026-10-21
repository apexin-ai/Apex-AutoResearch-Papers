"""Graduated cross-type dose-response: accuracy vs cumulative message-type pruning.

Uses offline traces + per-message function annotations to simulate progressive
removal of message types, from least to most information-bearing. Validated
against 10-seed online oracle data for the ack-only level.

Inputs:
  - outputs/full_scale/{qwen,llama}_round_robin/traces/traces.jsonl
  - outputs/full_scale/{qwen,llama}_round_robin/annotations/annotations.jsonl
  - outputs/oracle_{qwen,llama}_10run/seed_*.json  (for online validation)

Outputs:
  - artifacts/dose_response_data.csv
  - artifacts/paper/figures/dose_response_curve.pdf
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "artifacts" / "paper" / "figures"))
import paper_style

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

BASE_DIR = Path(__file__).resolve().parent.parent

PRUNING_LEVELS = [
    {"level": 0, "label": "None", "remove": set()},
    {"level": 1, "label": "ACK", "remove": {"acknowledgment"}},
    {"level": 2, "label": "+COORD", "remove": {"acknowledgment", "coordination"}},
    {"level": 3, "label": "+INFO", "remove": {"acknowledgment", "coordination", "information_provision"}},
    {"level": 4, "label": "All−RG", "remove": {"acknowledgment", "coordination", "information_provision", "verification"}},
]

EXPERIMENTS = {
    "Qwen-7B": {
        "traces": "outputs/full_scale/qwen_round_robin/traces/traces.jsonl",
        "annotations": "outputs/full_scale/qwen_round_robin/annotations/annotations.jsonl",
        "oracle_dir": "outputs/oracle_qwen_10run",
    },
    "Llama-7B": {
        "traces": "outputs/full_scale/llama_round_robin/traces/traces.jsonl",
        "annotations": "outputs/full_scale/llama_round_robin/annotations/annotations.jsonl",
        "oracle_dir": "outputs/oracle_llama_10run",
    },
}

SEEDS = [42, 123, 456, 789, 1024, 2048, 3072, 4096, 5120, 6144]


def extract_gsm8k_answer(text: str) -> str | None:
    """Strict extraction: only 'The answer is X', boxed, or #### patterns.
    No last-number fallback — avoids picking up stray numbers from coordination msgs."""
    patterns = [
        r'[Tt]he answer is\s*\$?\\?boxed\{([^}]+)\}',
        r'[Tt]he answer is\s*\$?\s*([+-]?\d[\d,]*\.?\d*)',
        r'####\s*([+-]?\d[\d,]*\.?\d*)',
        r'\$?\s*\\?boxed\{([^}]+)\}',
    ]
    for pat in patterns:
        m = re.findall(pat, text)
        if m:
            return m[-1].replace(",", "").strip().rstrip(".")
    return None


def check_answer(pred, truth) -> bool:
    if pred is None:
        return False
    try:
        return abs(float(pred) - float(str(truth).replace(",", ""))) < 1e-3
    except (ValueError, TypeError):
        return str(pred).strip() == str(truth).strip()


def load_annotations(ann_path: str) -> dict[str, str]:
    labels = {}
    with open(ann_path) as f:
        for line in f:
            if not line.strip():
                continue
            rec = json.loads(line)
            task_id = rec["task_id"]
            msg_idx = rec["message_index"]
            rnd = msg_idx + 1
            key = f"{task_id}_r{rnd}"
            ann_a = rec.get("annotation_a", {})
            ann_single = rec.get("annotation", {})
            fn_type = ann_a.get("type") or ann_single.get("type") or "unknown"
            labels[key] = fn_type
    return labels


def offline_graduated_pruning(traces_path: str, annotations: dict[str, str],
                              remove_types: set[str], num_tasks: int = 300):
    """Remove all messages of given types from offline traces, re-extract answers."""
    results = []
    with open(traces_path) as f:
        for i, line in enumerate(f):
            if i >= num_tasks:
                break
            if not line.strip():
                continue
            rec = json.loads(line)
            task_id = rec["task_id"]
            ground_truth = rec["ground_truth"]

            remaining = []
            total_agent = 0
            pruned_count = 0

            for msg in rec.get("messages", []):
                rnd = msg.get("round", 0)
                if rnd == 0:
                    remaining.append(msg)
                    continue
                total_agent += 1
                key = f"{task_id}_r{rnd}"
                fn_type = annotations.get(key, "unknown")
                if fn_type in remove_types:
                    pruned_count += 1
                else:
                    remaining.append(msg)

            final_answer = None
            for msg in reversed(remaining):
                final_answer = extract_gsm8k_answer(msg.get("content", ""))
                if final_answer is not None:
                    break

            results.append({
                "task_id": task_id,
                "correct": check_answer(final_answer, ground_truth),
                "pruned": pruned_count,
                "total_agent": total_agent,
            })
    return results


def compute_suppression_rate_from_annotations(
    annotations: dict[str, str], remove_types: set[str]
) -> float:
    if not annotations:
        return 0.0
    total = len(annotations)
    removed = sum(1 for v in annotations.values() if v in remove_types)
    return removed / total


def load_oracle_10seed(oracle_dir: str):
    """Load all 10 seeds of oracle data. Returns per-seed stats."""
    results = []
    for seed in SEEDS:
        fpath = Path(oracle_dir) / f"seed_{seed}.json"
        if not fpath.exists():
            continue
        with open(fpath) as f:
            d = json.load(f)
        base_acc = sum(1 for t in d["per_task"] if t["baseline_correct"]) / len(d["per_task"])
        pruned_acc = sum(1 for t in d["per_task"] if t["oracle_pruned_correct"]) / len(d["per_task"])
        type_counts = Counter()
        for task in d["per_task"]:
            for dec in task["oracle_decisions"]:
                type_counts[dec["function_type"]] += 1
        total_msgs = sum(type_counts.values())
        ack_rate = type_counts["acknowledgment"] / total_msgs if total_msgs else 0
        results.append({
            "seed": seed,
            "baseline_acc": base_acc,
            "pruned_acc": pruned_acc,
            "delta_pp": (pruned_acc - base_acc) * 100,
            "ack_suppression_rate": ack_rate,
            "type_counts": dict(type_counts),
            "total_msgs": total_msgs,
        })
    return results


def compute_oracle_suppression_rates(oracle_seeds: list[dict]) -> dict[int, dict]:
    """Compute mean suppression rate for each pruning level from oracle data."""
    level_rates = defaultdict(list)
    for seed_data in oracle_seeds:
        tc = seed_data["type_counts"]
        total = seed_data["total_msgs"]
        for lvl in PRUNING_LEVELS:
            removed = sum(tc.get(t, 0) for t in lvl["remove"])
            level_rates[lvl["level"]].append(removed / total if total else 0)
    return {
        lvl: {"mean": np.mean(rates), "std": np.std(rates)}
        for lvl, rates in level_rates.items()
    }


def run_analysis(model_name: str, exp_cfg: dict, num_tasks: int = 300):
    """Run full graduated pruning analysis for one model."""
    traces_path = str(BASE_DIR / exp_cfg["traces"])
    ann_path = str(BASE_DIR / exp_cfg["annotations"])
    oracle_dir = str(BASE_DIR / exp_cfg["oracle_dir"])

    print(f"\n{'='*70}")
    print(f"  {model_name}")
    print(f"{'='*70}")

    annotations = load_annotations(ann_path)
    print(f"Loaded {len(annotations)} annotations")

    type_dist = Counter(annotations.values())
    print(f"Type distribution: {dict(type_dist.most_common())}")

    oracle_seeds = load_oracle_10seed(oracle_dir)
    print(f"Loaded {len(oracle_seeds)} oracle seeds")

    oracle_sup_rates = compute_oracle_suppression_rates(oracle_seeds)

    baseline_results = offline_graduated_pruning(
        traces_path, annotations, set(), num_tasks
    )
    baseline_acc = sum(1 for r in baseline_results if r["correct"]) / len(baseline_results)
    print(f"Offline baseline: {baseline_acc*100:.1f}% (N={len(baseline_results)})")

    level_results = []
    print(f"\n{'Level':<8} {'Types removed':<40} {'Supp%':>6} {'Acc%':>6} {'Δ(pp)':>7}")
    print("-" * 70)

    for lvl in PRUNING_LEVELS:
        remove_types = lvl["remove"]

        if len(remove_types) == 0:
            acc = baseline_acc
            pruned_results = baseline_results
        else:
            pruned_results = offline_graduated_pruning(
                traces_path, annotations, remove_types, num_tasks
            )
            acc = sum(1 for r in pruned_results if r["correct"]) / len(pruned_results)

        sup_rate_offline = compute_suppression_rate_from_annotations(
            annotations, remove_types
        )

        oracle_sup = oracle_sup_rates.get(lvl["level"], {})
        oracle_sup_mean = oracle_sup.get("mean", sup_rate_offline)

        delta_pp = (acc - baseline_acc) * 100

        types_str = ", ".join(sorted(remove_types)) if remove_types else "(none)"
        print(f"L{lvl['level']:<6} {types_str:<40} {sup_rate_offline*100:>5.1f}% {acc*100:>5.1f}% {delta_pp:>+6.1f}")

        oracle_validation = None
        if lvl["level"] == 1 and oracle_seeds:
            oracle_deltas = [s["delta_pp"] for s in oracle_seeds]
            oracle_validation = {
                "online_mean_delta_pp": round(np.mean(oracle_deltas), 2),
                "online_sd_delta_pp": round(np.std(oracle_deltas), 2),
                "online_mean_acc": round(np.mean([s["pruned_acc"] for s in oracle_seeds]) * 100, 2),
                "n_seeds": len(oracle_seeds),
            }
            print(f"         └─ Online oracle validation: Δ={oracle_validation['online_mean_delta_pp']:+.1f}±{oracle_validation['online_sd_delta_pp']:.1f}pp ({oracle_validation['n_seeds']} seeds)")

        # McNemar-style discordance
        b_count = sum(1 for bl, pr in zip(baseline_results, pruned_results)
                      if bl["correct"] and not pr["correct"])
        c_count = sum(1 for bl, pr in zip(baseline_results, pruned_results)
                      if not bl["correct"] and pr["correct"])

        level_results.append({
            "model": model_name,
            "level": lvl["level"],
            "level_label": lvl["label"],
            "types_removed": types_str,
            "suppression_rate": round(sup_rate_offline * 100, 2),
            "suppression_rate_oracle": round(oracle_sup_mean * 100, 2) if oracle_seeds else None,
            "accuracy": round(acc * 100, 2),
            "baseline_accuracy": round(baseline_acc * 100, 2),
            "delta_pp": round(delta_pp, 2),
            "n_tasks": len(pruned_results),
            "discordant_b": b_count,
            "discordant_c": c_count,
            "source": "offline_trace_removal",
            "oracle_validation": oracle_validation,
        })

    return level_results


def write_csv(all_results: list[dict], out_path: Path):
    import csv as csv_mod
    out_path.parent.mkdir(parents=True, exist_ok=True)
    cols = [
        "model", "level", "level_label", "types_removed",
        "suppression_rate", "accuracy", "baseline_accuracy",
        "delta_pp", "n_tasks", "discordant_b", "discordant_c",
        "source",
    ]
    with open(out_path, "w", newline="") as f:
        writer = csv_mod.writer(f)
        writer.writerow(cols)
        for r in all_results:
            writer.writerow([str(r.get(c, "")) for c in cols])
    print(f"\nCSV saved to {out_path}")


def plot_dose_response(all_results: list[dict], out_path: Path):
    out_path.parent.mkdir(parents=True, exist_ok=True)

    paper_style.apply_style()

    fig, ax = plt.subplots(figsize=(paper_style.TEXTWIDTH + 1.5, 4.2))

    models = sorted(set(r["model"] for r in all_results))
    markers = {"Qwen-7B": "o", "Llama-7B": "s"}
    colors = {"Qwen-7B": "#2176AE", "Llama-7B": "#D64933"}

    level_labels = {
        "None": "No pruning",
        "ACK": "ACK",
        "+COORD": "+COORD",
        "+INFO": "+INFO",
        "All−RG": "All except\nreasoning",
    }

    for model in models:
        data = [r for r in all_results if r["model"] == model]
        data.sort(key=lambda x: x["level"])
        x = [d["suppression_rate"] for d in data]
        y = [d["delta_pp"] for d in data]

        ax.plot(x, y,
                marker=markers.get(model, "^"),
                color=colors.get(model, "#555"),
                linewidth=1.8, markersize=7, label=model,
                zorder=3)

        for d in data:
            if d["oracle_validation"]:
                ov = d["oracle_validation"]
                ax.errorbar(
                    d["suppression_rate"], ov["online_mean_delta_pp"],
                    yerr=ov["online_sd_delta_pp"],
                    fmt="*", color=colors.get(model, "#555"),
                    markersize=10, capsize=3, capthick=1.2,
                    alpha=0.7, zorder=4,
                )

    # Level annotations with collision avoidance
    levels_seen = sorted(set(r["level"] for r in all_results))
    prev_x = -999
    for lvl_id in levels_seen:
        lvl_data = [r for r in all_results if r["level"] == lvl_id]
        avg_x = np.mean([d["suppression_rate"] for d in lvl_data])
        max_y = max(d["delta_pp"] for d in lvl_data)
        label_raw = lvl_data[0]["level_label"]
        label = level_labels.get(label_raw, label_raw)
        # Merge ACK and +COORD if their x positions are within 5pp
        if avg_x - prev_x < 5 and lvl_id > 0:
            continue
        if lvl_id == 1:
            # Check if next level overlaps
            next_data = [r for r in all_results if r["level"] == 2]
            if next_data:
                next_x = np.mean([d["suppression_rate"] for d in next_data])
                if next_x - avg_x < 5:
                    label = "ACK\n+COORD"
        ax.annotate(
            label,
            xy=(avg_x, max_y + 0.8),
            fontsize=7.5, ha="center", va="bottom", color="#444",
            bbox=dict(boxstyle="round,pad=0.15", facecolor="white",
                      edgecolor="#ccc", alpha=0.8),
        )
        prev_x = avg_x

    ax.axhline(0, color="gray", linewidth=0.8, linestyle="--", alpha=0.5)

    y_vals = [r["delta_pp"] for r in all_results]
    all_ov = [r["oracle_validation"] for r in all_results if r["oracle_validation"]]
    if all_ov:
        for ov in all_ov:
            y_vals.append(ov["online_mean_delta_pp"] + ov["online_sd_delta_pp"])
            y_vals.append(ov["online_mean_delta_pp"] - ov["online_sd_delta_pp"])

    # Shade the ±1pp safe zone
    ax.axhspan(-1, 1, color="#e8f5e9", alpha=0.3, zorder=0, label="$\\pm$1pp safe zone")

    ax.set_xlabel("Suppression rate (%)")
    ax.set_ylabel("$\\Delta$ Accuracy (pp)")
    ax.legend(loc="lower left", framealpha=0.9)

    ax.annotate(
        "$\\bigstar$ = online oracle (10-seed ± SD)",
        xy=(0.98, 0.02), xycoords="axes fraction",
        fontsize=7.5, ha="right", va="bottom", color="#666",
    )

    ax.set_xlim(-3, max(r["suppression_rate"] for r in all_results) + 5)
    y_margin = max(3, (max(y_vals) - min(y_vals)) * 0.2 + 1)
    ax.set_ylim(min(y_vals) - y_margin, max(y_vals) + y_margin + 2.5)

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.tight_layout()
    plt.savefig(out_path, bbox_inches="tight")
    plt.savefig(out_path.with_suffix(".png"), bbox_inches="tight", dpi=300)
    plt.close()
    print(f"Figure saved to {out_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Graduated cross-type dose-response reanalysis"
    )
    parser.add_argument("--num-tasks", type=int, default=300,
                        help="Max tasks per experiment (default: 300)")
    parser.add_argument("--csv-out", default="artifacts/dose_response_data.csv")
    parser.add_argument("--fig-out", default="artifacts/paper/figures/dose_response_curve.pdf")
    args = parser.parse_args()

    all_results = []
    for model_name, exp_cfg in EXPERIMENTS.items():
        traces_file = BASE_DIR / exp_cfg["traces"]
        ann_file = BASE_DIR / exp_cfg["annotations"]
        if not traces_file.exists():
            print(f"SKIP {model_name}: traces not found at {traces_file}")
            continue
        if not ann_file.exists():
            print(f"SKIP {model_name}: annotations not found at {ann_file}")
            continue
        results = run_analysis(model_name, exp_cfg, args.num_tasks)
        all_results.extend(results)

    if not all_results:
        print("No results generated — check data paths.")
        sys.exit(1)

    csv_path = BASE_DIR / args.csv_out
    write_csv(all_results, csv_path)

    fig_path = BASE_DIR / args.fig_out
    plot_dose_response(all_results, fig_path)

    # Summary
    print(f"\n{'='*70}")
    print("DOSE-RESPONSE SUMMARY")
    print(f"{'='*70}")
    for model in sorted(set(r["model"] for r in all_results)):
        data = [r for r in all_results if r["model"] == model]
        data.sort(key=lambda x: x["level"])
        print(f"\n{model}:")
        max_sup = max(d["suppression_rate"] for d in data)
        deltas = [d["delta_pp"] for d in data]
        print(f"  Max suppression: {max_sup:.1f}%")
        print(f"  Delta range: [{min(deltas):+.1f}, {max(deltas):+.1f}] pp")
        if max(abs(d) for d in deltas) <= 1.5:
            print(f"  Pattern: PLATEAU (all |Δ| ≤ 1.5pp)")
        elif any(abs(d) > 3 for d in deltas[-2:]):
            print(f"  Pattern: PLATEAU→DROP at high suppression")
        else:
            print(f"  Pattern: GRADUAL decline")


if __name__ == "__main__":
    main()
