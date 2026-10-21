"""Death decomposition analysis for plan-012.

Reads plan-001b episode data (episodes.jsonl) and quantifies how much of the
deterministic vs internal score gap (Delta) comes from death avoidance.

Input:  --data_dir pointing to a directory tree containing */episodes.jsonl
        (or **/episodes.jsonl at any nesting depth).
Output: Terminal summary + per-task CSV to --output.

Dependencies: numpy, scipy, pandas (+ stdlib json/argparse/pathlib).
"""

import argparse
import json
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Tuple

import numpy as np
import pandas as pd
from scipy.stats import pearsonr

DEATH_SCORE = -100.0


def find_episode_files(data_dir: Path) -> Dict[str, Path]:
    """Discover all episodes.jsonl files, keyed by task name (parent dir name)."""
    tasks = {}
    for ep_file in sorted(data_dir.rglob("episodes.jsonl")):
        task_name = ep_file.parent.name
        if task_name not in tasks:
            tasks[task_name] = ep_file
    return tasks


def load_episodes(ep_file: Path) -> List[dict]:
    episodes = []
    with open(ep_file) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            ep = json.loads(line)
            if "always_internal" in ep and "always_deterministic" in ep:
                episodes.append(ep)
    return episodes


def extract_scores(episodes: List[dict]) -> Tuple[np.ndarray, np.ndarray]:
    int_scores = np.array([ep["always_internal"]["final_score"] for ep in episodes])
    det_scores = np.array([ep["always_deterministic"]["final_score"] for ep in episodes])
    return int_scores, det_scores


def analyze_task(task_name: str, episodes: List[dict]) -> dict:
    int_s, det_s = extract_scores(episodes)
    n = len(int_s)

    int_dead = int_s <= DEATH_SCORE
    det_dead = det_s <= DEATH_SCORE
    either_dead = int_dead | det_dead
    neither_dead = ~either_dead

    death_rate_int = int_dead.sum() / n
    death_rate_det = det_dead.sum() / n

    delta_full = det_s.mean() - int_s.mean()

    # No-death subset
    n_nd = neither_dead.sum()
    if n_nd > 0:
        delta_nd = det_s[neither_dead].mean() - int_s[neither_dead].mean()
    else:
        delta_nd = np.nan

    # Penalty replaced: -100 -> 0
    int_pr = np.where(int_dead, 0.0, int_s)
    det_pr = np.where(det_dead, 0.0, det_s)
    delta_penalty_replaced = det_pr.mean() - int_pr.mean()

    # Label distribution
    det_pref = int(((det_s > int_s) & ~(int_dead & det_dead)).sum()
                   + 0)  # det wins when: det>int and not both dead
    # More precise: classify each episode
    det_pref_count = 0
    int_pref_count = 0
    no_pref_count = 0
    for i_s, d_s, i_d, d_d in zip(int_s, det_s, int_dead, det_dead):
        if i_d and not d_d:
            det_pref_count += 1
        elif d_d and not i_d:
            int_pref_count += 1
        elif i_d and d_d:
            no_pref_count += 1
        elif d_s > i_s:
            det_pref_count += 1
        elif i_s > d_s:
            int_pref_count += 1
        else:
            no_pref_count += 1

    return {
        "task_name": task_name,
        "n_episodes": n,
        "death_rate_int": round(death_rate_int, 4),
        "death_rate_det": round(death_rate_det, 4),
        "delta_full": round(delta_full, 2),
        "delta_nd": round(delta_nd, 2) if not np.isnan(delta_nd) else np.nan,
        "delta_penalty_replaced": round(delta_penalty_replaced, 2),
        "det_pref": det_pref_count,
        "int_pref": int_pref_count,
        "no_pref": no_pref_count,
        "_int_scores": int_s,
        "_det_scores": det_s,
    }


def print_summary(task_results: List[dict], df: pd.DataFrame):
    all_int = np.concatenate([r["_int_scores"] for r in task_results])
    all_det = np.concatenate([r["_det_scores"] for r in task_results])

    int_dead = all_int <= DEATH_SCORE
    det_dead = all_det <= DEATH_SCORE
    neither_dead = ~(int_dead | det_dead)

    delta_full = all_det.mean() - all_int.mean()
    delta_nd = (all_det[neither_dead].mean() - all_int[neither_dead].mean()
                if neither_dead.any() else np.nan)
    fraction = (delta_full - delta_nd) / delta_full if delta_full != 0 and not np.isnan(delta_nd) else np.nan

    # Penalty replaced
    int_pr = np.where(int_dead, 0.0, all_int)
    det_pr = np.where(det_dead, 0.0, all_det)
    delta_pr = det_pr.mean() - int_pr.mean()

    # Pearson correlation: per-task (death_rate_int - death_rate_det) vs delta_full
    valid = df.dropna(subset=["delta_full"])
    death_rate_diff = valid["death_rate_int"] - valid["death_rate_det"]
    if len(valid) >= 3:
        r, p = pearsonr(death_rate_diff.values, valid["delta_full"].values)
    else:
        r, p = np.nan, np.nan

    # Label totals
    det_pref_total = df["det_pref"].sum()
    int_pref_total = df["int_pref"].sum()
    no_pref_total = df["no_pref"].sum()
    n_total = df["n_episodes"].sum()

    print("=" * 60)
    print("Death Decomposition Summary")
    print("=" * 60)
    print(f"Tasks: {len(df)}, Episodes: {n_total}")
    print(f"Death rate: internal={int_dead.mean():.1%}, det={det_dead.mean():.1%}")
    print(f"Delta_full (det-int):  {delta_full:+.2f}")
    print(f"Delta_nd (no-death):   {delta_nd:+.2f}" if not np.isnan(delta_nd) else "Delta_nd: N/A")
    print(f"Delta_pr (penalty->0): {delta_pr:+.2f}")
    print(f"Death avoidance fraction: {fraction:.4f}" if not np.isnan(fraction) else "Death avoidance fraction: N/A")
    print(f"Pearson r(death_rate_diff, delta): r={r:.4f}, p={p:.2e}" if not np.isnan(r) else "Pearson r: N/A")
    print(f"Labels: det-preferred={det_pref_total}, internal-preferred={int_pref_total}, no-preference={no_pref_total}")
    print("=" * 60)


def main():
    parser = argparse.ArgumentParser(description="Plan-012 death decomposition analysis")
    parser.add_argument("--data_dir", required=True,
                        help="Root directory containing task subdirs with episodes.jsonl")
    parser.add_argument("--output", default="death_decomposition_summary.csv",
                        help="Output CSV path (default: death_decomposition_summary.csv)")
    args = parser.parse_args()

    data_dir = Path(args.data_dir)
    if not data_dir.is_dir():
        print(f"ERROR: {data_dir} is not a directory")
        return

    task_files = find_episode_files(data_dir)
    if not task_files:
        print(f"ERROR: No episodes.jsonl found under {data_dir}")
        return

    print(f"Found {len(task_files)} tasks under {data_dir}")

    task_results = []
    for task_name, ep_file in sorted(task_files.items()):
        episodes = load_episodes(ep_file)
        if not episodes:
            continue
        result = analyze_task(task_name, episodes)
        task_results.append(result)

    if not task_results:
        print("ERROR: No valid episodes loaded")
        return

    csv_columns = [
        "task_name", "n_episodes", "death_rate_int", "death_rate_det",
        "delta_full", "delta_nd", "delta_penalty_replaced",
        "det_pref", "int_pref", "no_pref",
    ]
    df = pd.DataFrame([{k: r[k] for k in csv_columns} for r in task_results])

    print_summary(task_results, df)

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"\nCSV saved to {output_path}")


if __name__ == "__main__":
    main()
