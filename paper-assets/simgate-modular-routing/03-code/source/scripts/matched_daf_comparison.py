"""Matched 7B vs 72B DAF comparison across shared tasks."""
import json
import math
import os
from collections import defaultdict

DEATH_THRESHOLD = -100
BASE = "/root/autodl-tmp/simgate-modular-routing/results"
DIR_7B = os.path.join(BASE, "plan_c")
DIR_72B = os.path.join(BASE, "backbone_72b")


def load_episodes(data_dir):
    tasks = {}
    if not os.path.isdir(data_dir):
        return tasks
    for task_name in sorted(os.listdir(data_dir)):
        ep_file = os.path.join(data_dir, task_name, "episodes.jsonl")
        if not os.path.isfile(ep_file):
            continue
        episodes = []
        with open(ep_file) as f:
            for line in f:
                ep = json.loads(line)
                if "always_internal" not in ep or "always_deterministic" not in ep:
                    continue
                int_score = ep["always_internal"]["final_score"]
                det_score = ep["always_deterministic"]["final_score"]
                episodes.append((int_score, det_score))
        if episodes:
            tasks[task_name] = episodes
    return tasks


def classify(int_score, det_score):
    int_died = int_score <= DEATH_THRESHOLD
    det_died = det_score <= DEATH_THRESHOLD
    if int_died and not det_died:
        return "det-preferred", "death_asymmetry"
    if det_died and not int_died:
        return "internal-preferred", "death_asymmetry"
    if int_died and det_died:
        return "no-preference", "both_dead"
    if det_score > int_score:
        return "det-preferred", "score_comparison"
    if int_score > det_score:
        return "internal-preferred", "score_comparison"
    return "no-preference", "tied_alive"


def analyze_task(task_name, episodes):
    n = len(episodes)
    int_deaths = sum(1 for s_int, s_det in episodes if s_int <= DEATH_THRESHOLD)
    det_deaths = sum(1 for s_int, s_det in episodes if s_det <= DEATH_THRESHOLD)

    label_counts = defaultdict(int)
    source_counts = defaultdict(int)
    for s_int, s_det in episodes:
        label, source = classify(s_int, s_det)
        label_counts[label] += 1
        source_counts[source] += 1

    int_dr = int_deaths / n if n else 0
    det_dr = det_deaths / n if n else 0

    death_driven = source_counts.get("death_asymmetry", 0)
    score_driven = source_counts.get("score_comparison", 0)
    decisive = death_driven + score_driven
    daf = death_driven / decisive if decisive > 0 else float("nan")

    int_mean = sum(s[0] for s in episodes) / n
    det_mean = sum(s[1] for s in episodes) / n
    delta_full = det_mean - int_mean

    alive_eps = [(s_int, s_det) for s_int, s_det in episodes
                 if s_int > DEATH_THRESHOLD and s_det > DEATH_THRESHOLD]
    if alive_eps:
        delta_nd = (sum(s[1] for s in alive_eps) / len(alive_eps)
                    - sum(s[0] for s in alive_eps) / len(alive_eps))
    else:
        delta_nd = 0

    return {
        "task": task_name,
        "n": n,
        "int_death_rate": int_dr,
        "det_death_rate": det_dr,
        "death_driven": death_driven,
        "score_driven": score_driven,
        "tied_or_both_dead": label_counts.get("no-preference", 0),
        "daf": daf,
        "delta_full": delta_full,
        "delta_nd": delta_nd,
        "int_mean": int_mean,
        "det_mean": det_mean,
        "label_dist": dict(label_counts),
        "source_dist": dict(source_counts),
    }


def main():
    tasks_7b = load_episodes(DIR_7B)
    tasks_72b = load_episodes(DIR_72B)

    matched = sorted(set(tasks_7b.keys()) & set(tasks_72b.keys()))
    print(f"7B tasks ({len(tasks_7b)}): {sorted(tasks_7b.keys())}")
    print(f"72B tasks ({len(tasks_72b)}): {sorted(tasks_72b.keys())}")
    print(f"Matched tasks ({len(matched)}): {matched}")
    print(f"7B-only: {sorted(set(tasks_7b.keys()) - set(tasks_72b.keys()))}")
    print(f"72B-only: {sorted(set(tasks_72b.keys()) - set(tasks_7b.keys()))}")
    print()

    results_7b = []
    results_72b = []
    for task in matched:
        r7b = analyze_task(task, tasks_7b[task])
        r72b = analyze_task(task, tasks_72b[task])
        results_7b.append(r7b)
        results_72b.append(r72b)

    hdr = (f"{'Task':<45} | {'7B DR(int)':>10} | {'7B DR(det)':>10} | {'7B DAF':>8} "
           f"| {'72B DR(int)':>11} | {'72B DR(det)':>11} | {'72B DAF':>8} | {'dDAF':>8}")
    sep = "-" * len(hdr)
    print(hdr)
    print(sep)

    agg_7b_death = 0
    agg_7b_score = 0
    agg_72b_death = 0
    agg_72b_score = 0
    agg_7b_n = 0
    agg_72b_n = 0

    for r7, r72 in zip(results_7b, results_72b):
        d_daf = r72["daf"] - r7["daf"]
        agg_7b_death += r7["death_driven"]
        agg_7b_score += r7["score_driven"]
        agg_72b_death += r72["death_driven"]
        agg_72b_score += r72["score_driven"]
        agg_7b_n += r7["n"]
        agg_72b_n += r72["n"]

        print(f"{r7['task']:<45} | {r7['int_death_rate']:>9.1%} | {r7['det_death_rate']:>9.1%} "
              f"| {r7['daf']:>7.1%} | {r72['int_death_rate']:>10.1%} | {r72['det_death_rate']:>10.1%} "
              f"| {r72['daf']:>7.1%} | {d_daf:>+7.1%}")

    print(sep)
    agg_7b_daf = agg_7b_death / (agg_7b_death + agg_7b_score) if (agg_7b_death + agg_7b_score) > 0 else 0
    agg_72b_daf = agg_72b_death / (agg_72b_death + agg_72b_score) if (agg_72b_death + agg_72b_score) > 0 else 0

    valid_7b_dafs = [r["daf"] for r in results_7b if not math.isnan(r["daf"])]
    valid_72b_dafs = [r["daf"] for r in results_72b if not math.isnan(r["daf"])]
    tw_7b = sum(valid_7b_dafs) / len(valid_7b_dafs) if valid_7b_dafs else 0
    tw_72b = sum(valid_72b_dafs) / len(valid_72b_dafs) if valid_72b_dafs else 0

    agg_7b_idr = sum(r["int_death_rate"] * r["n"] for r in results_7b) / agg_7b_n
    agg_7b_ddr = sum(r["det_death_rate"] * r["n"] for r in results_7b) / agg_7b_n
    agg_72b_idr = sum(r["int_death_rate"] * r["n"] for r in results_72b) / agg_72b_n
    agg_72b_ddr = sum(r["det_death_rate"] * r["n"] for r in results_72b) / agg_72b_n

    print(f"{'Ep-weighted agg':<45} | {agg_7b_idr:>9.1%} | {agg_7b_ddr:>9.1%} "
          f"| {agg_7b_daf:>7.1%} | {agg_72b_idr:>10.1%} | {agg_72b_ddr:>10.1%} "
          f"| {agg_72b_daf:>7.1%} | {agg_72b_daf - agg_7b_daf:>+7.1%}")
    print(f"{'Task-weighted agg':<45} |           |           "
          f"| {tw_7b:>7.1%} |            |            "
          f"| {tw_72b:>7.1%} | {tw_72b - tw_7b:>+7.1%}")

    print("\n\n=== DETAILED PER-TASK BREAKDOWN ===\n")
    for r7, r72 in zip(results_7b, results_72b):
        print(f"--- {r7['task']} ---")
        print(f"  7B:  n={r7['n']}, int_DR={r7['int_death_rate']:.1%}, det_DR={r7['det_death_rate']:.1%}, "
              f"death={r7['death_driven']}, score={r7['score_driven']}, DAF={r7['daf']:.1%}")
        print(f"       labels: {r7['label_dist']}")
        print(f"       sources: {r7['source_dist']}")
        print(f"  72B: n={r72['n']}, int_DR={r72['int_death_rate']:.1%}, det_DR={r72['det_death_rate']:.1%}, "
              f"death={r72['death_driven']}, score={r72['score_driven']}, DAF={r72['daf']:.1%}")
        print(f"       labels: {r72['label_dist']}")
        print(f"       sources: {r72['source_dist']}")
        print()

    print("\n=== DOMINANCE SHIFT ANALYSIS ===\n")
    shifts_found = False
    for r7, r72 in zip(results_7b, results_72b):
        if math.isnan(r7["daf"]) or math.isnan(r72["daf"]):
            continue
        was_death = r7["daf"] > 0.5
        is_death = r72["daf"] > 0.5
        if was_death != is_death:
            direction = "death->perf" if was_death else "perf->death"
            print(f"  SHIFT: {r7['task']}: {direction} "
                  f"(7B DAF={r7['daf']:.1%} -> 72B DAF={r72['daf']:.1%})")
            shifts_found = True
    if not shifts_found:
        print("  No dominance shifts detected (all tasks maintain same category)")

    output = {
        "matched_tasks": matched,
        "n_matched": len(matched),
        "per_task": [
            {
                "task": r7["task"],
                "7b": {k: v for k, v in r7.items() if k != "task"},
                "72b": {k: v for k, v in r72.items() if k != "task"},
                "delta_daf": r72["daf"] - r7["daf"],
            }
            for r7, r72 in zip(results_7b, results_72b)
        ],
        "aggregate": {
            "episode_weighted": {
                "7b_daf": agg_7b_daf, "72b_daf": agg_72b_daf,
                "delta": agg_72b_daf - agg_7b_daf,
                "7b_int_dr": agg_7b_idr, "72b_int_dr": agg_72b_idr,
            },
            "task_weighted": {
                "7b_daf": tw_7b, "72b_daf": tw_72b,
                "delta": tw_72b - tw_7b,
            },
        },
    }
    out_path = os.path.join(BASE, "..", "artifacts", "72b_matched_daf_comparison.json")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\n[Saved JSON to {out_path}]")


if __name__ == "__main__":
    main()
