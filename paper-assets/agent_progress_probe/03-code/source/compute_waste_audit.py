#!/usr/bin/env python3
"""Compute waste audit: analyse stagnation tail waste in agent trajectories.

Input:
  - SWE-Agent windows: {data_dir}/windows_labeled.jsonl
  - OH windows: {oh_dir}/windows_labeled.jsonl
  - SWE trajectories: {data_dir}/swe_agent_trajectories_5000.jsonl
  - OH trajectories: {oh_dir}/openhands_trajectories.jsonl

Output:
  - artifacts/d072/compute_waste_audit.json
    Per-trajectory stagnation tail analysis, grouped by agent type.

Logic:
  For each trajectory, considering only conf>=2 windows:
    1. Sort windows by window_idx
    2. Find the stagnation onset: the earliest window such that all subsequent
       conf>=2 windows (from that point to the end) are stagnation.
    3. Compute tail_ratio = (total_steps - onset_step) / total_steps
"""

import argparse
import json
import os
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np


def load_windows(path):
    """Load windows from JSONL file."""
    windows = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                windows.append(json.loads(line))
    return windows


def build_traj_step_counts(traj_path):
    """Build mapping from trajectory_id -> total number of steps."""
    counts = {}
    with open(traj_path) as f:
        for row_idx, line in enumerate(f):
            line = line.strip()
            if not line:
                continue
            rec = json.loads(line)
            instance_id = rec.get("instance_id", "unknown")
            model_name = rec.get("model_name", "unknown")
            tid = f"{instance_id}__{model_name}__r{row_idx}"
            steps = rec.get("trajectory") or []
            counts[tid] = len(steps)
    return counts


def find_stagnation_onset(windows_sorted):
    """Find the onset of stagnation tail among conf>=2 windows.

    The onset is the earliest window such that ALL subsequent conf>=2
    windows (from that point onward) are stagnation (label=0).

    Returns (onset_window_idx, onset_step) or (None, None) if no tail.
    """
    conf2 = [(w["window_idx"], w["majority_label"], w["step_indices"])
             for w in windows_sorted
             if w.get("confidence", 0) >= 2 and w.get("majority_label", -1) != -1]

    if not conf2:
        return None, None

    # Scan from the end to find the longest trailing stagnation run
    # that extends to the last conf>=2 window.
    last_idx = len(conf2) - 1

    if conf2[last_idx][1] != 0:
        # Last conf>=2 window is progress — no stagnation tail
        return None, None

    onset_pos = last_idx
    for i in range(last_idx - 1, -1, -1):
        if conf2[i][1] == 0:
            onset_pos = i
        else:
            break

    onset_window_idx = conf2[onset_pos][0]
    onset_step = min(conf2[onset_pos][2])
    return onset_window_idx, onset_step


def classify_agent(trajectory_id):
    """Classify trajectory as swe_agent or openhands."""
    if "openhands" in trajectory_id.lower():
        return "openhands"
    return "swe_agent"


def main():
    parser = argparse.ArgumentParser(description="Compute stagnation tail waste audit")
    parser.add_argument("--data_dir", type=str, default="data",
                        help="SWE-Agent data directory")
    parser.add_argument("--oh_dir", type=str, default="/root/autodl-tmp/openhands_data",
                        help="OpenHands data directory")
    parser.add_argument("--output", type=str, default="artifacts/d072/compute_waste_audit.json",
                        help="Output JSON path")
    args = parser.parse_args()

    base_dir = Path(__file__).parent
    data_dir = base_dir / args.data_dir
    oh_dir = Path(args.oh_dir)
    output_path = base_dir / args.output

    # ------------------------------------------------------------------
    # 1. Load windows
    # ------------------------------------------------------------------
    swe_windows_path = data_dir / "windows_labeled.jsonl"
    oh_windows_path = oh_dir / "windows_labeled.jsonl"

    all_windows = []

    if swe_windows_path.exists():
        print(f"Loading SWE windows: {swe_windows_path}")
        swe_wins = load_windows(swe_windows_path)
        print(f"  {len(swe_wins)} windows")
        all_windows.extend(swe_wins)
    else:
        print(f"WARNING: SWE windows not found: {swe_windows_path}")

    if oh_windows_path.exists():
        print(f"Loading OH windows: {oh_windows_path}")
        oh_wins = load_windows(oh_windows_path)
        print(f"  {len(oh_wins)} windows")
        all_windows.extend(oh_wins)
    else:
        print(f"WARNING: OH windows not found: {oh_windows_path}")

    if not all_windows:
        print("ERROR: No windows loaded")
        sys.exit(1)

    # ------------------------------------------------------------------
    # 2. Load trajectory step counts
    # ------------------------------------------------------------------
    traj_step_counts = {}

    swe_traj_path = data_dir / "swe_agent_trajectories_5000.jsonl"
    if swe_traj_path.exists():
        print(f"Loading SWE trajectory step counts: {swe_traj_path}")
        swe_counts = build_traj_step_counts(swe_traj_path)
        traj_step_counts.update(swe_counts)
        print(f"  {len(swe_counts)} trajectories")

    oh_traj_path = oh_dir / "openhands_trajectories.jsonl"
    if oh_traj_path.exists():
        print(f"Loading OH trajectory step counts: {oh_traj_path}")
        oh_counts = build_traj_step_counts(oh_traj_path)
        traj_step_counts.update(oh_counts)
        print(f"  {len(oh_counts)} trajectories")

    # ------------------------------------------------------------------
    # 3. Group windows by trajectory
    # ------------------------------------------------------------------
    traj_windows = defaultdict(list)
    for w in all_windows:
        traj_windows[w["trajectory_id"]].append(w)

    for tid in traj_windows:
        traj_windows[tid].sort(key=lambda w: w["window_idx"])

    print(f"\nTotal trajectories with windows: {len(traj_windows)}")

    # ------------------------------------------------------------------
    # 4. Compute per-trajectory stagnation tail
    # ------------------------------------------------------------------
    per_trajectory = []
    for tid, windows in traj_windows.items():
        agent = classify_agent(tid)
        total_steps = traj_step_counts.get(tid)

        # Fallback: estimate total steps from window data
        if total_steps is None:
            max_step = 0
            for w in windows:
                if w["step_indices"]:
                    max_step = max(max_step, max(w["step_indices"]))
            total_steps = max_step + 1

        onset_window_idx, onset_step = find_stagnation_onset(windows)

        if onset_step is not None:
            tail_steps = total_steps - onset_step
            tail_ratio = tail_steps / total_steps if total_steps > 0 else 0.0
        else:
            tail_steps = 0
            tail_ratio = 0.0

        per_trajectory.append({
            "traj_id": tid,
            "agent": agent,
            "total_steps": total_steps,
            "onset_step": onset_step,
            "tail_steps": tail_steps,
            "tail_ratio": round(tail_ratio, 4),
        })

    # ------------------------------------------------------------------
    # 5. Aggregate statistics
    # ------------------------------------------------------------------
    total = len(per_trajectory)
    with_stag = [t for t in per_trajectory if t["onset_step"] is not None]
    tail_ratios_all = [t["tail_ratio"] for t in with_stag]

    summary = {
        "total_trajectories": total,
        "trajectories_with_stagnation": len(with_stag),
        "mean_tail_ratio": round(float(np.mean(tail_ratios_all)), 4) if tail_ratios_all else 0.0,
        "median_tail_ratio": round(float(np.median(tail_ratios_all)), 4) if tail_ratios_all else 0.0,
    }

    # Per-agent stats
    per_agent = {}
    for agent_name in ["swe_agent", "openhands"]:
        agent_trajs = [t for t in per_trajectory if t["agent"] == agent_name]
        agent_stag = [t for t in agent_trajs if t["onset_step"] is not None]
        agent_ratios = [t["tail_ratio"] for t in agent_stag]
        per_agent[agent_name] = {
            "total": len(agent_trajs),
            "with_stag": len(agent_stag),
            "mean_tail_ratio": round(float(np.mean(agent_ratios)), 4) if agent_ratios else 0.0,
            "median_tail_ratio": round(float(np.median(agent_ratios)), 4) if agent_ratios else 0.0,
        }

    # Tail distribution histogram
    if tail_ratios_all:
        bins = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
        counts, _ = np.histogram(tail_ratios_all, bins=bins)
        tail_distribution = {
            "bins": bins,
            "counts": counts.tolist(),
        }
    else:
        tail_distribution = {"bins": [], "counts": []}

    # ------------------------------------------------------------------
    # 6. Output
    # ------------------------------------------------------------------
    output = {
        "summary": summary,
        "per_agent": per_agent,
        "tail_distribution": tail_distribution,
        "per_trajectory": per_trajectory,
    }

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(output, f, indent=2)

    print(f"\nResults saved to {output_path}")
    print(f"\n=== Summary ===")
    print(f"Total trajectories: {summary['total_trajectories']}")
    print(f"With stagnation tail: {summary['trajectories_with_stagnation']}")
    print(f"Mean tail ratio: {summary['mean_tail_ratio']}")
    print(f"Median tail ratio: {summary['median_tail_ratio']}")
    for agent_name, stats in per_agent.items():
        if stats["total"] > 0:
            print(f"\n  {agent_name}: {stats['total']} trajectories, "
                  f"{stats['with_stag']} with stagnation, "
                  f"mean_tail={stats['mean_tail_ratio']}, "
                  f"median_tail={stats['median_tail_ratio']}")


if __name__ == "__main__":
    main()
