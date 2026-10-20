"""Compare generated eff_rank vs n-gram entropy as collapse detectors.

Tests whether generated eff_rank (Pivot B) adds value over n-gram entropy:
(a) Does it detect collapse earlier?
(b) Does it provide a smoother gradual decline vs n-gram's step-function drop?

Usage:
    python compare_eff_rank_vs_ngram.py \
        --pivot-b /root/autodl-tmp/output_v7/pivot_b_analysis/generated_vs_holdout_eff_rank.json \
        --data-dir /root/autodl-tmp/output_v7/ \
        --output /root/autodl-tmp/output_v7/pivot_b_analysis/pivot_b_comparison.json

Input:
    - Pivot B output: generated_vs_holdout_eff_rank.json (from analyze_generated_eff_rank.py)
    - Data directory with G0/G1/G2 metrics.jsonl files

Output:
    - Comparison table: per-checkpoint relative changes for all signals
    - Detection timing: which signal fires first
    - Smoothness analysis: first-difference variance as proxy for gradual vs abrupt
    - Verdict: does Pivot B add value?
"""

import argparse
import json
import math
import os
import sys
from pathlib import Path


NGRAM_METRICS = ["unigram_entropy", "bigram_entropy", "trigram_entropy", "vocab_coverage"]

DETECTION_THRESHOLDS = {
    "generated_eff_rank": {"direction": "decrease", "rel": 0.005, "abs": 3.0},
    "holdout_eff_rank": {"direction": "decrease", "rel": 0.005, "abs": 3.0},
    "unigram_entropy": {"direction": "decrease", "rel": 0.10, "abs": 0.5},
    "bigram_entropy": {"direction": "decrease", "rel": 0.10, "abs": 0.5},
    "trigram_entropy": {"direction": "decrease", "rel": 0.10, "abs": 0.5},
    "vocab_coverage": {"direction": "decrease", "rel": 0.10, "abs": 0.05},
}


def read_metrics_jsonl(path: str) -> list[dict]:
    entries = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                entries.append(json.loads(line))
    return entries


def load_ngram_metrics(data_dir: str) -> list[dict]:
    """Load metrics.jsonl from each generation, return sorted checkpoint list."""
    base = Path(data_dir)
    all_ckpts = []
    for gen_dir in sorted(base.glob("G*")):
        gen_idx = int(gen_dir.name[1:])
        for metrics_path in [gen_dir / "metrics" / "metrics.jsonl", gen_dir / "metrics.jsonl"]:
            if metrics_path.exists():
                entries = read_metrics_jsonl(str(metrics_path))
                for e in entries:
                    if "generation" not in e and "gen" not in e:
                        e["generation"] = gen_idx
                    all_ckpts.append(e)
                break
    return all_ckpts


def get_val(entry: dict, key: str) -> float | None:
    if key in entry:
        return entry[key]
    aliases = {
        "unigram_entropy": ["unigram_H"],
        "spectral_effective_rank": ["eff_rank", "effective_rank"],
        "vocab_coverage": ["coverage"],
    }
    for alias in aliases.get(key, []):
        if alias in entry:
            return entry[alias]
    return None


def detect_first(values: list[tuple[dict, float]], baseline: float, config: dict) -> dict | None:
    """Find first checkpoint where metric significantly deviates from baseline."""
    for meta, val in values:
        abs_change = val - baseline
        rel_change = abs_change / abs(baseline) if baseline != 0 else 0
        if config["direction"] == "decrease":
            if abs_change <= -config["abs"] or rel_change <= -config["rel"]:
                return {"meta": meta, "value": val, "abs_change": abs_change, "rel_change": rel_change}
        else:
            if abs_change >= config["abs"] or rel_change >= config["rel"]:
                return {"meta": meta, "value": val, "abs_change": abs_change, "rel_change": rel_change}
    return None


def compute_smoothness(values: list[float]) -> dict:
    """Smoothness metrics: lower first-difference variance = smoother decline."""
    if len(values) < 2:
        return {"first_diff_var": None, "first_diff_mean": None, "monotonic": None}
    diffs = [values[i + 1] - values[i] for i in range(len(values) - 1)]
    mean_d = sum(diffs) / len(diffs)
    var_d = sum((d - mean_d) ** 2 for d in diffs) / len(diffs) if len(diffs) > 1 else 0
    monotonic = all(d <= 0 for d in diffs) or all(d >= 0 for d in diffs)
    return {
        "first_diff_var": round(var_d, 6),
        "first_diff_mean": round(mean_d, 6),
        "monotonic": monotonic,
        "num_points": len(values),
    }


def main():
    parser = argparse.ArgumentParser(description="Compare generated eff_rank vs n-gram entropy")
    parser.add_argument("--pivot-b", required=True,
                        help="Path to generated_vs_holdout_eff_rank.json")
    parser.add_argument("--data-dir", required=True,
                        help="Directory with G0/G1/G2 metrics.jsonl")
    parser.add_argument("--output", default="pivot_b_comparison.json")
    args = parser.parse_args()

    with open(args.pivot_b) as f:
        pivot_b_data = json.load(f)

    ngram_ckpts = load_ngram_metrics(args.data_dir)
    if not ngram_ckpts:
        print("ERROR: No metrics.jsonl found", file=sys.stderr)
        sys.exit(1)

    # Build G0 baselines from ngram metrics
    g0_entries = [c for c in ngram_ckpts if c.get("generation", c.get("gen", 0)) == 0]
    if not g0_entries:
        print("ERROR: No G0 metrics", file=sys.stderr)
        sys.exit(1)
    g0_final = g0_entries[-1]

    ngram_baselines = {}
    for key in NGRAM_METRICS:
        val = get_val(g0_final, key)
        if val is not None:
            ngram_baselines[key] = val

    # Build G0 baselines from pivot B
    g0_pivot = [e for e in pivot_b_data if e["generation"] == 0]
    if not g0_pivot:
        print("ERROR: No G0 entries in pivot B data", file=sys.stderr)
        sys.exit(1)
    g0_pivot_final = g0_pivot[-1]
    pivot_baselines = {
        "generated_eff_rank": g0_pivot_final["generated_eff_rank"],
        "holdout_eff_rank": g0_pivot_final["holdout_eff_rank"],
    }

    # Collect post-G0 values for each signal
    post_g0_ngram = [c for c in ngram_ckpts if c.get("generation", c.get("gen", 0)) > 0]
    post_g0_pivot = [e for e in pivot_b_data if e["generation"] > 0]

    # Build per-checkpoint comparison table
    comparison = []

    # Pivot B entries (generation, step) as anchors
    for pe in pivot_b_data:
        gen = pe["generation"]
        step = pe["step"]
        row = {
            "generation": gen,
            "step": step,
            "max_length": pe.get("max_length"),
            "holdout_eff_rank": pe["holdout_eff_rank"],
            "generated_eff_rank": pe["generated_eff_rank"],
            "gen_hold_delta": pe["delta"],
        }

        # Find matching ngram checkpoint (closest step in same generation)
        matched = None
        for nc in ngram_ckpts:
            nc_gen = nc.get("generation", nc.get("gen", 0))
            nc_step = nc.get("global_step", nc.get("step", 0))
            if nc_gen == gen and nc_step == step:
                matched = nc
                break
        if matched is None:
            best_dist = float("inf")
            for nc in ngram_ckpts:
                nc_gen = nc.get("generation", nc.get("gen", 0))
                nc_step = nc.get("global_step", nc.get("step", 0))
                if nc_gen == gen:
                    dist = abs(nc_step - step)
                    if dist < best_dist:
                        best_dist = dist
                        matched = nc

        if matched:
            for key in NGRAM_METRICS:
                val = get_val(matched, key)
                row[key] = val
                if val is not None and key in ngram_baselines:
                    bl = ngram_baselines[key]
                    row[f"{key}_rel_change"] = round((val - bl) / abs(bl), 4) if bl != 0 else None

        if gen == 0 and pivot_baselines["generated_eff_rank"]:
            row["gen_eff_rank_rel_change"] = 0.0
            row["hold_eff_rank_rel_change"] = 0.0
        elif pivot_baselines["generated_eff_rank"]:
            bl_g = pivot_baselines["generated_eff_rank"]
            bl_h = pivot_baselines["holdout_eff_rank"]
            row["gen_eff_rank_rel_change"] = round(
                (pe["generated_eff_rank"] - bl_g) / abs(bl_g), 4) if bl_g != 0 else None
            row["hold_eff_rank_rel_change"] = round(
                (pe["holdout_eff_rank"] - bl_h) / abs(bl_h), 4) if bl_h != 0 else None

        comparison.append(row)

    # --- Detection timing ---
    detections = {}

    # Pivot B signals
    for signal in ["generated_eff_rank", "holdout_eff_rank"]:
        baseline = pivot_baselines[signal]
        vals = [({"generation": e["generation"], "step": e["step"]}, e[signal])
                for e in post_g0_pivot]
        det = detect_first(vals, baseline, DETECTION_THRESHOLDS[signal])
        detections[signal] = {
            "baseline": baseline,
            "detected": det is not None,
            "first_detection": {
                "generation": det["meta"]["generation"],
                "step": det["meta"]["step"],
                "value": round(det["value"], 2),
                "rel_change": round(det["rel_change"], 4),
            } if det else None,
        }

    # N-gram signals
    for key in NGRAM_METRICS:
        if key not in ngram_baselines:
            continue
        baseline = ngram_baselines[key]
        vals = [
            ({"generation": c.get("generation", c.get("gen", 0)),
              "step": c.get("global_step", c.get("step", 0))},
             get_val(c, key))
            for c in post_g0_ngram if get_val(c, key) is not None
        ]
        det = detect_first(vals, baseline, DETECTION_THRESHOLDS[key])
        detections[key] = {
            "baseline": baseline,
            "detected": det is not None,
            "first_detection": {
                "generation": det["meta"]["generation"],
                "step": det["meta"]["step"],
                "value": round(det["value"], 4),
                "rel_change": round(det["rel_change"], 4),
            } if det else None,
        }

    # --- Smoothness analysis ---
    smoothness = {}

    gen_eff_vals = [e["generated_eff_rank"] for e in pivot_b_data]
    smoothness["generated_eff_rank"] = compute_smoothness(gen_eff_vals)

    for key in NGRAM_METRICS:
        vals = [get_val(c, key) for c in ngram_ckpts if get_val(c, key) is not None]
        smoothness[key] = compute_smoothness(vals)

    # --- Verdict ---
    gen_detected = detections.get("generated_eff_rank", {}).get("detected", False)
    ngram_detected = any(detections.get(k, {}).get("detected", False) for k in NGRAM_METRICS)

    if gen_detected and not ngram_detected:
        verdict = "PIVOT_B_WINS: generated eff_rank detects collapse before n-gram metrics"
    elif gen_detected and ngram_detected:
        gen_step = detections["generated_eff_rank"]["first_detection"]["step"]
        gen_gen = detections["generated_eff_rank"]["first_detection"]["generation"]
        earliest_ngram = None
        for k in NGRAM_METRICS:
            d = detections.get(k, {})
            if d.get("detected"):
                fd = d["first_detection"]
                if earliest_ngram is None or (fd["generation"], fd["step"]) < (earliest_ngram["generation"], earliest_ngram["step"]):
                    earliest_ngram = fd
        if earliest_ngram and (gen_gen, gen_step) < (earliest_ngram["generation"], earliest_ngram["step"]):
            verdict = "PIVOT_B_WINS: generated eff_rank leads n-gram metrics"
        elif earliest_ngram and (gen_gen, gen_step) == (earliest_ngram["generation"], earliest_ngram["step"]):
            gen_smooth = smoothness.get("generated_eff_rank", {}).get("first_diff_var")
            ngram_smooth = smoothness.get("unigram_entropy", {}).get("first_diff_var")
            if gen_smooth is not None and ngram_smooth is not None and gen_smooth < ngram_smooth:
                verdict = "PIVOT_B_MARGINAL: same detection time, but smoother signal"
            else:
                verdict = "PIVOT_B_NO_ADVANTAGE: same detection time, no smoothness advantage"
        else:
            verdict = "PIVOT_B_LOSES: n-gram metrics lead generated eff_rank"
    elif not gen_detected and ngram_detected:
        verdict = "PIVOT_B_FAILS: generated eff_rank does not detect collapse at all"
    else:
        verdict = "INCONCLUSIVE: neither signal detects collapse"

    # --- Print ---
    print(f"\n{'='*80}")
    print("Pivot B Comparison: Generated eff_rank vs N-gram Entropy")
    print(f"{'='*80}")

    print(f"\n--- Detection Timing ---")
    print(f"{'Signal':<25} {'Detected':<10} {'Gen':<5} {'Step':<8} {'Rel Change':<12}")
    print("-" * 65)
    for sig, info in detections.items():
        det = info["detected"]
        fd = info.get("first_detection") or {}
        gen_s = f"G{fd.get('generation', '')}" if det else "—"
        step_s = str(fd.get("step", "—")) if det else "—"
        rc = f"{fd.get('rel_change', 0):+.1%}" if det else "—"
        print(f"{sig:<25} {'YES' if det else 'NO':<10} {gen_s:<5} {step_s:<8} {rc:<12}")

    print(f"\n--- Smoothness (first-difference variance, lower=smoother) ---")
    print(f"{'Signal':<25} {'Var':<12} {'Mean Δ':<12} {'Monotonic':<10} {'Points':<8}")
    print("-" * 70)
    for sig, info in smoothness.items():
        var_s = f"{info['first_diff_var']:.6f}" if info["first_diff_var"] is not None else "—"
        mean_s = f"{info['first_diff_mean']:.6f}" if info["first_diff_mean"] is not None else "—"
        mono_s = str(info.get("monotonic", "—"))
        pts = str(info.get("num_points", "—"))
        print(f"{sig:<25} {var_s:<12} {mean_s:<12} {mono_s:<10} {pts:<8}")

    print(f"\n--- Verdict ---")
    print(verdict)

    # --- Save ---
    report = {
        "comparison_table": comparison,
        "detections": detections,
        "smoothness": smoothness,
        "verdict": verdict,
        "baselines": {
            "pivot_b": pivot_baselines,
            "ngram": ngram_baselines,
        },
    }
    os.makedirs(os.path.dirname(os.path.abspath(args.output)), exist_ok=True)
    with open(args.output, "w") as f:
        json.dump(report, f, indent=2, default=str)
    print(f"\nReport saved to {args.output}")


if __name__ == "__main__":
    main()
