#!/usr/bin/env python3
"""Divergence point analysis for ALFWorld failure trajectories.

Computes divergence statistics, early/mid/late grouping, and γ(d) distribution.
Outputs structured JSON, LaTeX tables for paper, and human-readable summary.
"""

import argparse
import json
import math
import os
import sys
from collections import defaultdict
from pathlib import Path

try:
    import numpy as np
except ImportError:
    np = None


# ---------------------------------------------------------------------------
# Game file normalization (same as build_dpo_pairs.py)
# ---------------------------------------------------------------------------

def normalize_game_file(game_file: str) -> str:
    gf = game_file.rstrip("/")
    if gf.endswith("/game.tw-pddl"):
        gf = gf[: -len("/game.tw-pddl")]
    parts = gf.split("/")
    return "/".join(parts[-2:]) if len(parts) >= 2 else gf


# ---------------------------------------------------------------------------
# Message helpers (handle both {role,content} and {from,value} formats)
# ---------------------------------------------------------------------------

def _role(msg: dict) -> str:
    return msg.get("role") or {"human": "user", "gpt": "assistant"}.get(msg.get("from", ""), "")


def _content(msg: dict) -> str:
    return msg.get("content") or msg.get("value", "")


# ---------------------------------------------------------------------------
# Task type detection
# ---------------------------------------------------------------------------

TASK_TYPE_KEYS = [
    "pick_and_place",
    "pick_clean_then_place",
    "pick_heat_then_place",
    "pick_cool_then_place",
    "look_at_obj",
    "pick_two_obj",
]

TASK_TYPE_SHORT = {
    "pick_and_place": "put",
    "pick_clean_then_place": "clean",
    "pick_heat_then_place": "heat",
    "pick_cool_then_place": "cool",
    "look_at_obj": "examine",
    "pick_two_obj": "puttwo",
}


def get_task_type(game_file: str) -> str:
    for k in TASK_TYPE_KEYS:
        if f"/{k}" in game_file or game_file.startswith(k):
            return k
    return "unknown"


# ---------------------------------------------------------------------------
# Step extraction & divergence (mirrors build_dpo_pairs.py logic)
# ---------------------------------------------------------------------------

def find_task_start(conversations: list) -> int:
    task_desc_idx = -1
    for i, msg in enumerate(conversations):
        if _role(msg) in ("user", "human") and "Your task is to:" in _content(msg):
            task_desc_idx = i
    search_from = task_desc_idx + 1 if task_desc_idx >= 0 else 0
    for i in range(search_from, len(conversations)):
        if _role(conversations[i]) in ("assistant", "gpt") and "Action:" in _content(conversations[i]):
            return i
    return len(conversations)


def extract_action_sequence(conversations: list, start_idx: int) -> list[str]:
    actions = []
    for i in range(start_idx, len(conversations)):
        if _role(conversations[i]) in ("assistant", "gpt"):
            content = _content(conversations[i])
            if "Action:" in content:
                actions.append(_extract_action_text(content))
    return actions


def _extract_action_text(content: str) -> str:
    for line in content.split("\n"):
        stripped = line.strip()
        if stripped.lower().startswith("action:"):
            return " ".join(stripped[len("action:"):].split()).lower()
    return " ".join(content.split()).lower()


def find_divergence_point(expert_actions: list[str], fail_actions: list[str]) -> int:
    min_len = min(len(expert_actions), len(fail_actions))
    for i in range(min_len):
        if expert_actions[i] != fail_actions[i]:
            return i
    return min_len


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------

def load_trajectories(dirs: list[str]) -> list[dict]:
    records = []
    for d in dirs:
        for p in sorted(Path(d).glob("*.jsonl")):
            with open(p) as f:
                for line in f:
                    if line.strip():
                        records.append(json.loads(line))
    return records


def load_expert_index(path: str) -> dict[str, dict]:
    with open(path) as f:
        experts = json.load(f)
    index = {}
    for ex in experts:
        key = normalize_game_file(ex["game_file"])
        index[key] = ex
    return index


# ---------------------------------------------------------------------------
# Analysis
# ---------------------------------------------------------------------------

def analyze(trajectories: list[dict], expert_index: dict, gamma_min: float, gamma_max: float) -> dict:
    total = len(trajectories)
    successes = [t for t in trajectories if t.get("reward")]
    failures = [t for t in trajectories if not t.get("reward")]

    # Per-task-type counts
    type_total = defaultdict(int)
    type_success = defaultdict(int)
    for t in trajectories:
        tt = t.get("task_type") or get_task_type(t.get("game_file", ""))
        type_total[tt] += 1
        if t.get("reward"):
            type_success[tt] += 1

    per_type_sr = {}
    for tt in sorted(set(list(type_total.keys()))):
        n = type_total[tt]
        s = type_success[tt]
        per_type_sr[tt] = {"total": n, "success": s, "rate": s / n if n > 0 else 0.0}

    # Divergence analysis on failures
    d_values = []
    correction_spans = []
    unmatched = 0
    matched = 0
    per_type_d = defaultdict(list)

    for t in failures:
        gf = t.get("game_file", "")
        key = normalize_game_file(gf)
        expert = expert_index.get(key)
        if expert is None:
            unmatched += 1
            continue
        matched += 1

        fail_convs = t.get("conversations", [])
        expert_convs = expert.get("conversations", [])

        fail_start = find_task_start(fail_convs)
        expert_start = find_task_start(expert_convs)

        fail_actions = extract_action_sequence(fail_convs, fail_start)
        expert_actions = extract_action_sequence(expert_convs, expert_start)

        if not expert_actions:
            continue

        div_point = find_divergence_point(expert_actions, fail_actions)
        d = div_point / len(expert_actions)
        correction_span = len(expert_actions) - div_point

        d_values.append(d)
        correction_spans.append(correction_span)

        tt = t.get("task_type") or get_task_type(gf)
        per_type_d[tt].append(d)

    # d statistics
    d_stats = _compute_stats(d_values)

    # Histogram (10 bins)
    histogram = [0] * 10
    for d in d_values:
        b = min(int(d * 10), 9)
        histogram[b] += 1

    # Per-type d mean
    per_type_d_mean = {}
    for tt in sorted(per_type_d.keys()):
        vals = per_type_d[tt]
        per_type_d_mean[tt] = {"mean": _mean(vals), "count": len(vals)}

    # Early/Mid/Late grouping
    early = [(d, cs) for d, cs in zip(d_values, correction_spans) if d < 0.33]
    mid = [(d, cs) for d, cs in zip(d_values, correction_spans) if 0.33 <= d < 0.67]
    late = [(d, cs) for d, cs in zip(d_values, correction_spans) if d >= 0.67]

    n_div = len(d_values)
    groups = {}
    for name, subset in [("early", early), ("mid", mid), ("late", late)]:
        groups[name] = {
            "count": len(subset),
            "proportion": len(subset) / n_div if n_div > 0 else 0.0,
            "avg_correction_span": _mean([cs for _, cs in subset]),
            "avg_d": _mean([d for d, _ in subset]),
        }

    # γ(d) mapping
    gamma_values = [gamma_min + (gamma_max - gamma_min) * d for d in d_values]
    gamma_stats = _compute_stats(gamma_values)

    return {
        "basic": {
            "total_episodes": total,
            "success": len(successes),
            "failure": len(failures),
            "success_rate": len(successes) / total if total > 0 else 0.0,
        },
        "per_task_type_sr": per_type_sr,
        "divergence": {
            "matched_failures": matched,
            "unmatched_failures": unmatched,
            "d_stats": d_stats,
            "histogram_bins": ["[0.0,0.1)", "[0.1,0.2)", "[0.2,0.3)", "[0.3,0.4)",
                               "[0.4,0.5)", "[0.5,0.6)", "[0.6,0.7)", "[0.7,0.8)",
                               "[0.8,0.9)", "[0.9,1.0]"],
            "histogram_counts": histogram,
            "per_type_d_mean": per_type_d_mean,
        },
        "groups": groups,
        "gamma": {
            "gamma_min": gamma_min,
            "gamma_max": gamma_max,
            "stats": gamma_stats,
        },
        "expert_match": {
            "exact_match": matched,
            "unmatched": unmatched,
            "match_rate": matched / (matched + unmatched) if (matched + unmatched) > 0 else 0.0,
        },
    }


def _mean(vals):
    return sum(vals) / len(vals) if vals else 0.0


def _std(vals):
    if len(vals) < 2:
        return 0.0
    m = _mean(vals)
    return math.sqrt(sum((v - m) ** 2 for v in vals) / (len(vals) - 1))


def _percentile(vals, p):
    if not vals:
        return 0.0
    s = sorted(vals)
    k = (len(s) - 1) * p / 100.0
    f = int(k)
    c = min(f + 1, len(s) - 1)
    d = k - f
    return s[f] + d * (s[c] - s[f])


def _compute_stats(vals):
    if not vals:
        return {"count": 0, "mean": 0, "median": 0, "std": 0, "min": 0, "max": 0,
                "q25": 0, "q75": 0}
    return {
        "count": len(vals),
        "mean": _mean(vals),
        "median": _percentile(vals, 50),
        "std": _std(vals),
        "min": min(vals),
        "max": max(vals),
        "q25": _percentile(vals, 25),
        "q75": _percentile(vals, 75),
    }


# ---------------------------------------------------------------------------
# LaTeX output
# ---------------------------------------------------------------------------

def generate_latex(results: dict) -> str:
    lines = []

    # Table 1: Per-task-type success rate
    lines.append("% Table 1: Per-task-type success rate")
    lines.append(r"\begin{table}[t]")
    lines.append(r"\centering")
    lines.append(r"\caption{Per-task-type success rate.}")
    lines.append(r"\label{tab:task_type_sr}")
    lines.append(r"\begin{tabular}{lrrr}")
    lines.append(r"\toprule")
    lines.append(r"Task Type & Total & Success & Rate (\%) \\")
    lines.append(r"\midrule")
    sr = results["per_task_type_sr"]
    for tt in sorted(sr.keys()):
        v = sr[tt]
        short = TASK_TYPE_SHORT.get(tt, tt)
        lines.append(f"{short} & {v['total']} & {v['success']} & {v['rate']*100:.1f} \\\\")
    b = results["basic"]
    lines.append(r"\midrule")
    lines.append(f"Overall & {b['total_episodes']} & {b['success']} & {b['success_rate']*100:.1f} \\\\")
    lines.append(r"\bottomrule")
    lines.append(r"\end{tabular}")
    lines.append(r"\end{table}")
    lines.append("")

    # Table 2: Divergence point distribution (early/mid/late)
    lines.append("% Table 2: Divergence point distribution")
    lines.append(r"\begin{table}[t]")
    lines.append(r"\centering")
    lines.append(r"\caption{Divergence point distribution by failure stage.}")
    lines.append(r"\label{tab:divergence_groups}")
    lines.append(r"\begin{tabular}{lcrrr}")
    lines.append(r"\toprule")
    lines.append(r"Stage & $d$ range & Count & Prop. (\%) & Avg.\ $C_{\text{span}}$ \\")
    lines.append(r"\midrule")
    g = results["groups"]
    stage_labels = [
        ("Early", "$[0, 0.33)$", "early"),
        ("Mid", "$[0.33, 0.67)$", "mid"),
        ("Late", "$[0.67, 1.0]$", "late"),
    ]
    for label, drange, key in stage_labels:
        v = g[key]
        lines.append(
            f"{label} & {drange} & {v['count']} & {v['proportion']*100:.1f} & {v['avg_correction_span']:.1f} \\\\"
        )
    lines.append(r"\bottomrule")
    lines.append(r"\end{tabular}")
    lines.append(r"\end{table}")
    lines.append("")

    # Table 3: γ(d) distribution statistics
    lines.append("% Table 3: Gamma distribution statistics")
    lines.append(r"\begin{table}[t]")
    lines.append(r"\centering")
    gmin = results["gamma"]["gamma_min"]
    gmax = results["gamma"]["gamma_max"]
    lines.append(r"\caption{$\gamma(d)$ distribution ($\gamma_{\min}=" + f"{gmin}" + r", \gamma_{\max}=" + f"{gmax}" + r"$).}")
    lines.append(r"\label{tab:gamma_dist}")
    lines.append(r"\begin{tabular}{lr}")
    lines.append(r"\toprule")
    lines.append(r"Statistic & Value \\")
    lines.append(r"\midrule")
    gs = results["gamma"]["stats"]
    for k, label in [("mean", "Mean"), ("median", "Median"), ("std", "Std"),
                     ("min", "Min"), ("max", "Max"), ("q25", "Q25"), ("q75", "Q75")]:
        lines.append(f"{label} & {gs[k]:.4f} \\\\")
    lines.append(r"\bottomrule")
    lines.append(r"\end{tabular}")
    lines.append(r"\end{table}")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Human-readable summary
# ---------------------------------------------------------------------------

def print_summary(results: dict):
    b = results["basic"]
    print(f"\n{'='*60}")
    print("DIVERGENCE ANALYSIS SUMMARY")
    print(f"{'='*60}")
    print(f"Episodes: {b['total_episodes']}  Success: {b['success']}  Failure: {b['failure']}  SR: {b['success_rate']*100:.1f}%")

    print(f"\n--- Per-task-type success rate ---")
    print(f"{'Type':<25} {'Total':>6} {'Succ':>6} {'Rate':>8}")
    print("-" * 50)
    for tt in sorted(results["per_task_type_sr"].keys()):
        v = results["per_task_type_sr"][tt]
        print(f"{tt:<25} {v['total']:>6} {v['success']:>6} {v['rate']*100:>7.1f}%")

    div = results["divergence"]
    ds = div["d_stats"]
    print(f"\n--- Divergence point (d = div_point / expert_len) ---")
    print(f"Matched failures: {div['matched_failures']}  Unmatched: {div['unmatched_failures']}")
    if ds["count"] > 0:
        print(f"Mean: {ds['mean']:.3f}  Median: {ds['median']:.3f}  Std: {ds['std']:.3f}")
        print(f"Min: {ds['min']:.3f}  Max: {ds['max']:.3f}  Q25: {ds['q25']:.3f}  Q75: {ds['q75']:.3f}")

        print(f"\nHistogram:")
        for label, count in zip(div["histogram_bins"], div["histogram_counts"]):
            bar = "#" * count
            print(f"  {label:>12}: {count:>4} {bar}")

    print(f"\n--- Early / Mid / Late ---")
    g = results["groups"]
    print(f"{'Stage':<8} {'Count':>6} {'Prop':>8} {'Avg CSpan':>10} {'Avg d':>8}")
    print("-" * 45)
    for key in ["early", "mid", "late"]:
        v = g[key]
        print(f"{key:<8} {v['count']:>6} {v['proportion']*100:>7.1f}% {v['avg_correction_span']:>10.1f} {v['avg_d']:>8.3f}")

    gs = results["gamma"]["stats"]
    print(f"\n--- γ(d) distribution (γ_min={results['gamma']['gamma_min']}, γ_max={results['gamma']['gamma_max']}) ---")
    if gs["count"] > 0:
        print(f"Mean: {gs['mean']:.4f}  Median: {gs['median']:.4f}  Std: {gs['std']:.4f}")
        print(f"Min: {gs['min']:.4f}  Max: {gs['max']:.4f}")

    em = results["expert_match"]
    print(f"\n--- Expert matching ---")
    print(f"Matched: {em['exact_match']}  Unmatched: {em['unmatched']}  Match rate: {em['match_rate']*100:.1f}%")
    print(f"{'='*60}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Analyze divergence points in ALFWorld failure trajectories")
    parser.add_argument("--trajectory_dirs", nargs="+", required=True,
                        help="One or more trajectory directories")
    parser.add_argument("--expert_file", type=str, required=True,
                        help="Path to alfworld_sft.json")
    parser.add_argument("--output_dir", type=str, default="outputs/divergence_analysis",
                        help="Output directory")
    parser.add_argument("--gamma_min", type=float, default=0.85)
    parser.add_argument("--gamma_max", type=float, default=0.97)
    args = parser.parse_args()

    trajectories = load_trajectories(args.trajectory_dirs)
    if not trajectories:
        print("ERROR: No trajectories loaded.", file=sys.stderr)
        sys.exit(1)

    expert_index = load_expert_index(args.expert_file)
    results = analyze(trajectories, expert_index, args.gamma_min, args.gamma_max)

    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    json_path = out_dir / "divergence_summary.json"
    with open(json_path, "w") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    tex_path = out_dir / "divergence_tables.tex"
    with open(tex_path, "w") as f:
        f.write(generate_latex(results))

    print_summary(results)
    print(f"\nJSON: {json_path}")
    print(f"LaTeX: {tex_path}")


if __name__ == "__main__":
    main()
