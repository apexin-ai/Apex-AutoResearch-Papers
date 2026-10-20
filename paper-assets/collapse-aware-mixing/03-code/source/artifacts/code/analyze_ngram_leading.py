"""Analyze which metric first signals collapse across checkpoints.

Reads metrics.jsonl from each generation, identifies the first checkpoint
where each metric significantly deviates from G0 final baseline, and
ranks metrics by leading time.

Usage:
    python analyze_ngram_leading.py \
        --data-dir /root/autodl-tmp/output_v7/ \
        --output leading_indicator_ranking.json

Input:
    Data directory with G0/, G1/, G2/ subdirs, each containing
    metrics/metrics.jsonl (one JSON object per checkpoint).

Output:
    - Ranking table: which metric signals collapse first
    - JSON report with per-metric detection details
"""

import argparse
import json
import os
import sys
from pathlib import Path


METRICS_CONFIG = {
    "spectral_effective_rank": {
        "label": "eff_rank",
        "direction": "decrease",
        "abs_threshold": 3.0,
        "rel_threshold": 0.005,
    },
    "perplexity": {
        "label": "ppl",
        "direction": "increase",
        "abs_threshold": 2.0,
        "rel_threshold": 0.05,
    },
    "unigram_entropy": {
        "label": "unigram_ent",
        "direction": "decrease",
        "abs_threshold": 0.5,
        "rel_threshold": 0.10,
    },
    "bigram_entropy": {
        "label": "bigram_ent",
        "direction": "decrease",
        "abs_threshold": 0.5,
        "rel_threshold": 0.10,
    },
    "trigram_entropy": {
        "label": "trigram_ent",
        "direction": "decrease",
        "abs_threshold": 0.5,
        "rel_threshold": 0.10,
    },
    "vocab_coverage": {
        "label": "vocab_cov",
        "direction": "decrease",
        "abs_threshold": 0.05,
        "rel_threshold": 0.10,
    },
    "token_entropy_mean": {
        "label": "tok_ent_mean",
        "direction": "decrease",
        "abs_threshold": 0.3,
        "rel_threshold": 0.05,
    },
    "spectral_entropy": {
        "label": "spec_entropy",
        "direction": "decrease",
        "abs_threshold": 0.02,
        "rel_threshold": 0.005,
    },
}


def read_metrics_jsonl(path: str) -> list[dict]:
    entries = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                entries.append(json.loads(line))
    return entries


def get_metric_value(entry: dict, metric_name: str) -> float | None:
    if metric_name in entry:
        return entry[metric_name]
    short_names = {
        "spectral_effective_rank": ["eff_rank", "effective_rank"],
        "perplexity": ["ppl"],
        "vocab_coverage": ["coverage"],
    }
    for alias in short_names.get(metric_name, []):
        if alias in entry:
            return entry[alias]
    return None


def detect_first_signal(
    checkpoints: list[dict],
    metric_name: str,
    baseline_value: float,
    config: dict,
) -> dict | None:
    """Find first checkpoint where metric significantly deviates from baseline."""
    direction = config["direction"]
    abs_thresh = config["abs_threshold"]
    rel_thresh = config["rel_threshold"]

    for ckpt in checkpoints:
        val = get_metric_value(ckpt, metric_name)
        if val is None:
            continue

        abs_change = val - baseline_value
        rel_change = abs_change / abs(baseline_value) if baseline_value != 0 else 0

        triggered = False
        if direction == "decrease":
            triggered = (abs_change <= -abs_thresh) or (rel_change <= -rel_thresh)
        elif direction == "increase":
            triggered = (abs_change >= abs_thresh) or (rel_change >= rel_thresh)

        if triggered:
            return {
                "checkpoint_idx": checkpoints.index(ckpt),
                "generation": ckpt.get("generation", ckpt.get("gen")),
                "step": ckpt.get("global_step", ckpt.get("step")),
                "tokens_seen": ckpt.get("tokens_seen"),
                "baseline": baseline_value,
                "value": val,
                "abs_change": round(abs_change, 4),
                "rel_change": round(rel_change, 4),
            }

    return None


def main():
    parser = argparse.ArgumentParser(description="Rank metrics by collapse leading time")
    parser.add_argument("--data-dir", required=True, help="Directory with G0/G1/G2 subdirs")
    parser.add_argument("--output", default="leading_indicator_ranking.json")
    args = parser.parse_args()

    data_dir = Path(args.data_dir)

    # Collect all checkpoints across generations
    all_checkpoints = []
    g0_final = None

    for gen_dir in sorted(data_dir.glob("G*")):
        gen_idx = int(gen_dir.name[1:])
        metrics_file = gen_dir / "metrics" / "metrics.jsonl"
        if not metrics_file.exists():
            metrics_file = gen_dir / "metrics.jsonl"
        if not metrics_file.exists():
            print(f"WARN: no metrics for {gen_dir.name}", file=sys.stderr)
            continue

        entries = read_metrics_jsonl(str(metrics_file))
        for e in entries:
            if "generation" not in e and "gen" not in e:
                e["generation"] = gen_idx
            all_checkpoints.append(e)

        if gen_idx == 0 and entries:
            g0_final = entries[-1]

    if g0_final is None:
        print("ERROR: No G0 metrics found", file=sys.stderr)
        sys.exit(1)

    # Only look at G1+ checkpoints for detection
    post_g0 = [c for c in all_checkpoints
                if (c.get("generation", c.get("gen", 0))) > 0]

    if not post_g0:
        print("ERROR: No post-G0 checkpoints found", file=sys.stderr)
        sys.exit(1)

    # Detect first signal for each metric
    results = []
    for metric_name, config in METRICS_CONFIG.items():
        baseline = get_metric_value(g0_final, metric_name)
        if baseline is None:
            results.append({
                "metric": config["label"],
                "metric_key": metric_name,
                "detected": False,
                "reason": "no baseline value",
            })
            continue

        detection = detect_first_signal(post_g0, metric_name, baseline, config)
        if detection:
            results.append({
                "metric": config["label"],
                "metric_key": metric_name,
                "detected": True,
                "detection_checkpoint_idx": detection["checkpoint_idx"],
                "detection_gen": detection["generation"],
                "detection_step": detection["step"],
                "detection_tokens": detection["tokens_seen"],
                "baseline": detection["baseline"],
                "trigger_value": detection["value"],
                "abs_change": detection["abs_change"],
                "rel_change": detection["rel_change"],
                "direction": config["direction"],
                "abs_threshold": config["abs_threshold"],
                "rel_threshold": config["rel_threshold"],
            })
        else:
            results.append({
                "metric": config["label"],
                "metric_key": metric_name,
                "detected": False,
                "reason": "no significant change detected",
                "baseline": baseline,
                "final_value": get_metric_value(post_g0[-1], metric_name),
            })

    # Sort: detected first (by checkpoint_idx), then non-detected
    detected = [r for r in results if r["detected"]]
    not_detected = [r for r in results if not r["detected"]]
    detected.sort(key=lambda r: r["detection_checkpoint_idx"])
    ranked = detected + not_detected

    # Print ranking
    print(f"\nLeading Indicator Ranking ({len(post_g0)} post-G0 checkpoints)")
    print("=" * 90)
    print(f"{'Rank':<6} {'Metric':<15} {'Detected':<10} {'Gen':<5} {'Step':<8} "
          f"{'Baseline':<10} {'Value':<10} {'Change':<10}")
    print("-" * 90)
    for i, r in enumerate(ranked):
        rank = i + 1 if r["detected"] else "—"
        gen = f"G{r.get('detection_gen', '')}" if r["detected"] else "—"
        step = r.get("detection_step", "—")
        baseline = f"{r.get('baseline', 0):.3f}" if r.get("baseline") is not None else "—"
        value = f"{r.get('trigger_value', 0):.3f}" if r["detected"] else "—"
        change = f"{r.get('rel_change', 0):+.1%}" if r["detected"] else r.get("reason", "—")
        print(f"{str(rank):<6} {r['metric']:<15} {'YES' if r['detected'] else 'NO':<10} "
              f"{gen:<5} {str(step):<8} {baseline:<10} {value:<10} {change:<10}")

    # Check if multiple metrics triggered at the same checkpoint
    same_ckpt = (
        len(detected) > 1
        and len(set(r["detection_checkpoint_idx"] for r in detected)) == 1
    )
    if same_ckpt:
        print(f"\nNOTE: All {len(detected)} detected metrics triggered at the same "
              "checkpoint. Rank ordering reflects dictionary definition order, "
              "not true temporal precedence. Finer checkpoint granularity is "
              "needed to distinguish leading times.")

    # Summarize
    if detected:
        fastest = detected[0]
        print(f"\nFastest signal: {fastest['metric']} at G{fastest['detection_gen']} "
              f"step {fastest['detection_step']} ({fastest['rel_change']:+.1%})")
        eff_rank_result = next((r for r in ranked if r["metric_key"] == "spectral_effective_rank"), None)
        if eff_rank_result and not eff_rank_result["detected"]:
            print("eff_rank: NOT detected — does not lead other metrics")
        elif eff_rank_result and eff_rank_result["detected"]:
            eff_idx = detected.index(eff_rank_result)
            print(f"eff_rank: rank #{eff_idx + 1} out of {len(detected)} detected metrics")

    report = {
        "g0_baseline_checkpoint": str(g0_final.get("checkpoint", "last G0 entry")),
        "num_post_g0_checkpoints": len(post_g0),
        "ranking": ranked,
        "summary": {
            "total_metrics": len(ranked),
            "detected": len(detected),
            "not_detected": len(not_detected),
            "fastest_metric": detected[0]["metric"] if detected else None,
            "same_checkpoint_tie": same_ckpt,
        },
        "note": (
            "When multiple metrics trigger at the same checkpoint, rank ordering "
            "reflects METRICS_CONFIG dictionary definition order, not true temporal "
            "precedence. Finer checkpoint granularity is needed to distinguish "
            "leading times among co-detected metrics."
        ),
    }

    with open(args.output, "w") as f:
        json.dump(report, f, indent=2, default=str)
    print(f"\nReport saved to {args.output}")


if __name__ == "__main__":
    main()
