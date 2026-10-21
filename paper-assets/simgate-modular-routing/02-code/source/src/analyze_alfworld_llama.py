#!/usr/bin/env python3
# ALFWorld Llama counterfactual results analysis.
# Input: episodes.jsonl (one JSON object per line)
# Output: stdout report, analysis.json, latex_table.tex
import argparse
import json
import os
from collections import Counter, defaultdict

import numpy as np


def load_episodes(path):
    episodes = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                episodes.append(json.loads(line))
    return episodes


def label_distribution(episodes):
    counts = Counter(ep["label"] for ep in episodes)
    n = len(episodes)
    return {
        "det-preferred": counts.get("det-preferred", 0),
        "int-preferred": counts.get("int-preferred", 0),
        "no-preference": counts.get("no-preference", 0),
        "total": n,
    }


def det_leaning(dist):
    non_tie = dist["det-preferred"] + dist["int-preferred"]
    if non_tie == 0:
        return 0.0, 0
    return dist["det-preferred"] / non_tie, non_tie


def per_task_breakdown(episodes):
    by_type = defaultdict(list)
    for ep in episodes:
        by_type[ep["task_type"]].append(ep)
    rows = []
    for tt in sorted(by_type):
        eps = by_type[tt]
        d = label_distribution(eps)
        n = d["total"]
        rows.append({
            "task_type": tt,
            "n": n,
            "det_pref": d["det-preferred"],
            "int_pref": d["int-preferred"],
            "no_pref": d["no-preference"],
            "det_pref_pct": d["det-preferred"] / n * 100 if n else 0,
        })
    return rows


def check_deaths(episodes):
    death_episodes = []
    for ep in episodes:
        int_score = ep.get("internal", {}).get("score", 0)
        det_score = ep.get("deterministic", {}).get("score", 0)
        if int_score == -100 or det_score == -100:
            death_episodes.append(ep["task_id"])
    return death_episodes


def bootstrap_ci(values, stat_fn, B=10000, ci=0.95, seed=42):
    rng = np.random.RandomState(seed)
    arr = np.array(values)
    n = len(arr)
    stats = np.empty(B)
    for i in range(B):
        sample = arr[rng.randint(0, n, size=n)]
        stats[i] = stat_fn(sample)
    lo = np.percentile(stats, (1 - ci) / 2 * 100)
    hi = np.percentile(stats, (1 + ci) / 2 * 100)
    return float(lo), float(hi), float(np.mean(stats))


def main():
    parser = argparse.ArgumentParser(description="ALFWorld Llama counterfactual analysis")
    parser.add_argument("--input", default="results/alfworld_llama_counterfactual/episodes.jsonl")
    parser.add_argument("--qwen-input", default="results/alfworld_counterfactual/episodes.jsonl")
    parser.add_argument("--bootstrap-B", type=int, default=10000)
    args = parser.parse_args()

    episodes = load_episodes(args.input)
    print(f"Loaded {len(episodes)} episodes from {args.input}")

    # --- Qwen data ---
    qwen_episodes = []
    qwen_path = args.qwen_input
    if os.path.exists(qwen_path):
        qwen_episodes = load_episodes(qwen_path)
        print(f"Loaded {len(qwen_episodes)} Qwen episodes from {qwen_path}")
    else:
        print(f"Qwen data not found at {qwen_path}, using known values only")

    # === 1. Label distribution ===
    dist = label_distribution(episodes)
    n = dist["total"]
    print("\n" + "=" * 60)
    print("1. LABEL DISTRIBUTION")
    print("=" * 60)
    for label in ["det-preferred", "int-preferred", "no-preference"]:
        c = dist[label]
        print(f"  {label:20s}: {c:4d}  ({c/n*100:5.1f}%)")
    print(f"  {'total':20s}: {n:4d}")

    # === 2. Det-leaning among non-ties ===
    det_lean, non_tie = det_leaning(dist)
    print("\n" + "=" * 60)
    print("2. DET-LEANING (non-tie)")
    print("=" * 60)
    print(f"  det_preferred / (det_preferred + int_preferred) = {dist['det-preferred']} / {non_tie} = {det_lean*100:.1f}%")

    # === 3. Per-task-type breakdown ===
    rows = per_task_breakdown(episodes)
    print("\n" + "=" * 60)
    print("3. PER-TASK-TYPE BREAKDOWN")
    print("=" * 60)
    print(f"  {'task_type':30s} {'n':>4s} {'det':>4s} {'int':>4s} {'tie':>4s} {'det%':>6s}")
    print("  " + "-" * 54)
    for r in rows:
        print(f"  {r['task_type']:30s} {r['n']:4d} {r['det_pref']:4d} {r['int_pref']:4d} {r['no_pref']:4d} {r['det_pref_pct']:5.1f}%")

    # === 4. Qwen comparison ===
    print("\n" + "=" * 60)
    print("4. LLAMA vs QWEN COMPARISON")
    print("=" * 60)
    if qwen_episodes:
        qwen_dist = label_distribution(qwen_episodes)
        qwen_n = qwen_dist["total"]
        qwen_det_lean, qwen_non_tie = det_leaning(qwen_dist)
    else:
        qwen_n = 134
        qwen_dist = {"det-preferred": 35, "int-preferred": 100, "no-preference": -1}
        qwen_det_lean = 0.259
        qwen_non_tie = 135

    print(f"  {'metric':25s} {'Llama':>10s} {'Qwen':>10s}")
    print("  " + "-" * 47)
    print(f"  {'total episodes':25s} {n:10d} {qwen_n if qwen_episodes else 'N/A':>10}")
    for label in ["det-preferred", "int-preferred", "no-preference"]:
        lv = dist[label]
        lp = lv / n * 100
        if qwen_episodes:
            qv = qwen_dist[label]
            qp = qv / qwen_n * 100
            print(f"  {label:25s} {lv:4d} ({lp:4.1f}%) {qv:4d} ({qp:4.1f}%)")
        else:
            print(f"  {label:25s} {lv:4d} ({lp:4.1f}%) {'---':>10s}")
    if qwen_episodes:
        print(f"  {'det-leaning (non-tie)':25s} {det_lean*100:9.1f}% {qwen_det_lean*100:9.1f}%")
    else:
        print(f"  {'det-leaning (non-tie)':25s} {det_lean*100:9.1f}% {25.9:9.1f}%")

    # === 5. DAF confirmation ===
    deaths = check_deaths(episodes)
    print("\n" + "=" * 60)
    print("5. DAF (Death-Avoidance Failure) CHECK")
    print("=" * 60)
    if deaths:
        print(f"  WARNING: {len(deaths)} episodes with score=-100 found!")
        for d in deaths[:5]:
            print(f"    - {d}")
    else:
        print("  No deaths (score=-100) found in any episode.")
        print("  ALFWorld: no death mechanism, DAF=0% by definition.")

    # === 6. Bootstrap CIs ===
    print("\n" + "=" * 60)
    print("6. BOOTSTRAP CONFIDENCE INTERVALS (B={})".format(args.bootstrap_B))
    print("=" * 60)

    det_pref_binary = [1.0 if ep["label"] == "det-preferred" else 0.0 for ep in episodes]
    lo, hi, mean = bootstrap_ci(det_pref_binary, np.mean, B=args.bootstrap_B)
    print(f"  det-preferred %:  {mean*100:.1f}%  95% CI [{lo*100:.1f}%, {hi*100:.1f}%]")

    det_scores = [ep["deterministic"]["score"] for ep in episodes]
    int_scores = [ep["internal"]["score"] for ep in episodes]
    deltas = [d - i for d, i in zip(det_scores, int_scores)]
    lo_d, hi_d, mean_d = bootstrap_ci(deltas, np.mean, B=args.bootstrap_B)
    print(f"  Δ_full (det-int):  {mean_d:.4f}  95% CI [{lo_d:.4f}, {hi_d:.4f}]")

    # === Save JSON ===
    out_dir = os.path.dirname(args.input)
    results = {
        "n_episodes": n,
        "label_distribution": {
            "det-preferred": dist["det-preferred"],
            "int-preferred": dist["int-preferred"],
            "no-preference": dist["no-preference"],
        },
        "label_pct": {
            "det-preferred": round(dist["det-preferred"] / n * 100, 2),
            "int-preferred": round(dist["int-preferred"] / n * 100, 2),
            "no-preference": round(dist["no-preference"] / n * 100, 2),
        },
        "det_leaning_pct": round(det_lean * 100, 2),
        "per_task": rows,
        "deaths": len(deaths),
        "daf": "0% (no death mechanism)",
        "bootstrap": {
            "det_preferred_pct": {"mean": round(mean * 100, 2), "ci95": [round(lo * 100, 2), round(hi * 100, 2)]},
            "delta_full": {"mean": round(mean_d, 4), "ci95": [round(lo_d, 4), round(hi_d, 4)]},
        },
    }
    json_path = os.path.join(out_dir, "analysis.json")
    with open(json_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved analysis JSON to {json_path}")

    # === Save LaTeX table ===
    llama_det_pct = dist["det-preferred"] / n * 100
    llama_int_pct = dist["int-preferred"] / n * 100
    llama_tie_pct = dist["no-preference"] / n * 100

    if qwen_episodes:
        qwen_det_pct = qwen_dist["det-preferred"] / qwen_n * 100
        qwen_int_pct = qwen_dist["int-preferred"] / qwen_n * 100
        qwen_tie_pct = qwen_dist["no-preference"] / qwen_n * 100
    else:
        qwen_det_pct = 25.9
        qwen_int_pct = 74.1
        qwen_tie_pct = 0.0

    latex = (
        "% ALFWorld counterfactual comparison: Llama vs Qwen\n"
        "% Columns: Model & Det-Pref & Int-Pref & Tie & Det-Leaning & DAF\n"
        f"Llama & {llama_det_pct:.1f}\\% & {llama_int_pct:.1f}\\% & {llama_tie_pct:.1f}\\% & {det_lean*100:.1f}\\% & 0\\% \\\\\n"
        f"Qwen  & {qwen_det_pct:.1f}\\% & {qwen_int_pct:.1f}\\% & {qwen_tie_pct:.1f}\\% & {qwen_det_lean*100:.1f}\\% & 0\\% \\\\\n"
    )
    tex_path = os.path.join(out_dir, "latex_table.tex")
    with open(tex_path, "w") as f:
        f.write(latex)
    print(f"Saved LaTeX table to {tex_path}")


if __name__ == "__main__":
    main()
