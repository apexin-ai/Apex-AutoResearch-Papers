"""Sliding window extraction and labeling pipeline for agent_progress_probe."""

from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from data_loader import Step, Trajectory, load_trajectories_streaming
from labeling_functions import ALL_LFS, ABSTAIN

WINDOW_SIZE_PAIRS = 5  # 5 action-observation pairs = 10 steps
STRIDE_PAIRS = 2       # slide by 2 pairs = 4 steps
WINDOW_SIZE_STEPS = WINDOW_SIZE_PAIRS * 2  # 10
STRIDE_STEPS = STRIDE_PAIRS * 2            # 4
MIN_STEPS_FOR_WINDOW = 12  # system + issue + at least 10 interaction steps


def extract_windows(trajectory: Trajectory) -> list[dict]:
    """Extract sliding windows from a trajectory.

    Skips step 0 (system) and step 1 (issue description).
    Returns list of window dicts with steps and metadata.
    """
    # Start from step 2 (first ai action after issue)
    interaction_steps = [s for s in trajectory.steps if s.index >= 2]

    if not interaction_steps:
        return []

    trajectory_id = f"{trajectory.instance_id}__{trajectory.model_name}__r{trajectory.row_index}"
    common = {
        "trajectory_id": trajectory_id,
        "instance_id": trajectory.instance_id,
        "row_index": trajectory.row_index,
    }
    windows = []

    if len(interaction_steps) < WINDOW_SIZE_STEPS:
        # Short trajectory: single window with all available steps
        windows.append({
            **common,
            "window_idx": 0,
            "steps": interaction_steps,
            "step_indices": [s.index for s in interaction_steps],
            "short_trajectory": True,
        })
    else:
        idx = 0
        while idx + WINDOW_SIZE_STEPS <= len(interaction_steps):
            w_steps = interaction_steps[idx:idx + WINDOW_SIZE_STEPS]
            windows.append({
                **common,
                "window_idx": len(windows),
                "steps": w_steps,
                "step_indices": [s.index for s in w_steps],
                "short_trajectory": False,
            })
            idx += STRIDE_STEPS

        # If there are remaining steps that form a partial window at the end,
        # include them only if we haven't already covered them
        if idx < len(interaction_steps) and idx != 0:
            remaining = interaction_steps[idx:]
            if len(remaining) >= 4:  # at least 2 pairs
                windows.append({
                    **common,
                    "window_idx": len(windows),
                    "steps": remaining,
                    "step_indices": [s.index for s in remaining],
                    "short_trajectory": False,
                })

    return windows


def label_windows(windows: list[dict], trajectory: Trajectory) -> list[dict]:
    """Apply all labeling functions to extracted windows."""
    total_windows = len(windows)

    for i, w in enumerate(windows):
        position = {
            "window_idx": i,
            "total_windows": total_windows,
            "is_last": i == total_windows - 1,
        }
        labels = {}
        for lf_name, lf_fn in ALL_LFS:
            labels[lf_name] = lf_fn(w["steps"], trajectory, position)

        w["labels"] = labels

        # Majority vote (excluding abstains)
        non_abstain = [v for v in labels.values() if v != ABSTAIN]
        if non_abstain:
            counts = Counter(non_abstain)
            w["majority_label"] = counts.most_common(1)[0][0]
            w["confidence"] = counts.most_common(1)[0][1]
        else:
            w["majority_label"] = ABSTAIN
            w["confidence"] = 0

    return windows


def process_trajectory(trajectory: Trajectory) -> list[dict]:
    """Full pipeline: extract windows and apply labels."""
    windows = extract_windows(trajectory)
    if not windows:
        return []
    return label_windows(windows, trajectory)


def window_to_serializable(w: dict) -> dict:
    """Convert a window dict to JSON-serializable format (no Step objects)."""
    return {
        "trajectory_id": w["trajectory_id"],
        "instance_id": w["instance_id"],
        "row_index": w["row_index"],
        "window_idx": w["window_idx"],
        "step_indices": w["step_indices"],
        "short_trajectory": w.get("short_trajectory", False),
        "labels": w["labels"],
        "majority_label": w["majority_label"],
        "confidence": w["confidence"],
    }


def run_pipeline(data_path: str | Path, output_path: str | Path, limit: int | None = None):
    """Run the full pipeline on all trajectories and save results."""
    data_path = Path(data_path)
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Statistics counters
    total_windows = 0
    total_trajectories = 0
    short_trajectories = 0
    resolved_windows = 0
    unresolved_windows = 0

    lf_counts = {name: Counter() for name, _ in ALL_LFS}
    majority_counts = Counter()
    high_conf_counts = Counter()  # confidence >= 2
    agreement_total = 0
    agreement_agree = 0

    resolved_label_counts = Counter()
    unresolved_label_counts = Counter()

    with open(output_path, "w") as fout:
        for traj in load_trajectories_streaming(data_path, limit=limit):
            total_trajectories += 1
            windows = process_trajectory(traj)

            if not windows:
                continue

            if windows[0].get("short_trajectory"):
                short_trajectories += 1

            for w in windows:
                total_windows += 1

                if traj.target:
                    resolved_windows += 1
                else:
                    unresolved_windows += 1

                # Per-LF stats
                for lf_name, _ in ALL_LFS:
                    label = w["labels"][lf_name]
                    lf_counts[lf_name][label] += 1

                # Majority vote stats
                majority_counts[w["majority_label"]] += 1
                if w["confidence"] >= 2:
                    high_conf_counts[w["majority_label"]] += 1

                # Agreement: when >=2 LFs are non-abstain
                non_abstain_labels = [v for v in w["labels"].values() if v != ABSTAIN]
                if len(non_abstain_labels) >= 2:
                    agreement_total += 1
                    if len(set(non_abstain_labels)) == 1:
                        agreement_agree += 1

                # By resolved/unresolved
                if traj.target:
                    resolved_label_counts[w["majority_label"]] += 1
                else:
                    unresolved_label_counts[w["majority_label"]] += 1

                # Write serialized window
                fout.write(json.dumps(window_to_serializable(w)) + "\n")

            if total_trajectories % 100 == 0:
                print(f"  Processed {total_trajectories} trajectories, {total_windows} windows...")

    # Generate report
    stats = {
        "total_windows": total_windows,
        "total_trajectories": total_trajectories,
        "short_trajectories": short_trajectories,
        "resolved_windows": resolved_windows,
        "unresolved_windows": unresolved_windows,
        "lf_counts": {k: dict(v) for k, v in lf_counts.items()},
        "majority_counts": dict(majority_counts),
        "high_conf_counts": dict(high_conf_counts),
        "agreement_total": agreement_total,
        "agreement_agree": agreement_agree,
        "resolved_label_counts": dict(resolved_label_counts),
        "unresolved_label_counts": dict(unresolved_label_counts),
    }

    return stats


def generate_report(stats: dict, report_path: str | Path):
    """Generate markdown statistics report."""
    report_path = Path(report_path)

    total = stats["total_windows"]
    lines = []
    lines.append("# Label Statistics Report")
    lines.append("")
    lines.append("## 1. 窗口总数")
    lines.append("")
    lines.append(f"| 指标 | 值 |")
    lines.append(f"|------|-----|")
    lines.append(f"| 总窗口数 | {total:,} |")
    lines.append(f"| 总轨迹数 | {stats['total_trajectories']:,} |")
    lines.append(f"| 短轨迹数 (<12 steps) | {stats['short_trajectories']:,} |")
    lines.append(f"| Resolved 轨迹窗口 | {stats['resolved_windows']:,} |")
    lines.append(f"| Unresolved 轨迹窗口 | {stats['unresolved_windows']:,} |")
    lines.append("")

    lines.append("## 2. 每个 LF 的覆盖率")
    lines.append("")
    lines.append("| LF | 非 Abstain 数 | 覆盖率 |")
    lines.append("|-----|--------------|--------|")
    for lf_name, _ in ALL_LFS:
        counts = stats["lf_counts"][lf_name]
        non_abstain = sum(v for k, v in counts.items() if k != ABSTAIN)
        coverage = non_abstain / total * 100 if total > 0 else 0
        lines.append(f"| {lf_name} | {non_abstain:,} | {coverage:.1f}% |")
    lines.append("")

    lines.append("## 3. 每个 LF 的标签分布")
    lines.append("")
    label_names = {1: "progress", 0: "stagnation", -1: "abstain"}
    for lf_name, _ in ALL_LFS:
        counts = stats["lf_counts"][lf_name]
        lines.append(f"### {lf_name}")
        lines.append("")
        lines.append("| 标签 | 数量 | 占比 |")
        lines.append("|------|------|------|")
        for label_val in [1, 0, -1]:
            c = counts.get(label_val, 0)
            pct = c / total * 100 if total > 0 else 0
            lines.append(f"| {label_names[label_val]} | {c:,} | {pct:.1f}% |")
        lines.append("")

    lines.append("## 4. LF 一致性")
    lines.append("")
    agree_total = stats["agreement_total"]
    agree_agree = stats["agreement_agree"]
    agree_rate = agree_agree / agree_total * 100 if agree_total > 0 else 0
    lines.append(f"- ≥2 个 LF 都非 abstain 的窗口数：{agree_total:,}")
    lines.append(f"- 其中标签一致的窗口数：{agree_agree:,}")
    lines.append(f"- **一致率：{agree_rate:.1f}%**")
    lines.append("")

    lines.append("## 5. 多数投票标签分布（高置信度，confidence ≥ 2）")
    lines.append("")
    high_conf = stats["high_conf_counts"]
    high_total = sum(high_conf.values())
    lines.append(f"高置信度窗口总数：{high_total:,}")
    lines.append("")
    lines.append("| 标签 | 数量 | 占比 |")
    lines.append("|------|------|------|")
    for label_val in [1, 0]:
        c = high_conf.get(label_val, 0)
        pct = c / high_total * 100 if high_total > 0 else 0
        lines.append(f"| {label_names[label_val]} | {c:,} | {pct:.1f}% |")
    lines.append("")

    lines.append("## 6. 按 Resolved/Unresolved 分组的标签分布")
    lines.append("")
    lines.append("### Resolved 轨迹")
    lines.append("")
    lines.append("| Majority Label | 数量 | 占比 |")
    lines.append("|----------------|------|------|")
    res_total = sum(stats["resolved_label_counts"].values())
    for label_val in [1, 0, -1]:
        c = stats["resolved_label_counts"].get(label_val, 0)
        pct = c / res_total * 100 if res_total > 0 else 0
        lines.append(f"| {label_names[label_val]} | {c:,} | {pct:.1f}% |")
    lines.append("")

    lines.append("### Unresolved 轨迹")
    lines.append("")
    lines.append("| Majority Label | 数量 | 占比 |")
    lines.append("|----------------|------|------|")
    unres_total = sum(stats["unresolved_label_counts"].values())
    for label_val in [1, 0, -1]:
        c = stats["unresolved_label_counts"].get(label_val, 0)
        pct = c / unres_total * 100 if unres_total > 0 else 0
        lines.append(f"| {label_names[label_val]} | {c:,} | {pct:.1f}% |")
    lines.append("")

    lines.append("## 7. 类别平衡评估")
    lines.append("")
    prog_high = high_conf.get(1, 0)
    stag_high = high_conf.get(0, 0)
    if high_total > 0:
        ratio = max(prog_high, stag_high) / max(min(prog_high, stag_high), 1)
        lines.append(f"- Progress (高置信): {prog_high:,}")
        lines.append(f"- Stagnation (高置信): {stag_high:,}")
        lines.append(f"- 比例 (多/少): {ratio:.1f}:1")
        lines.append("")
        if ratio > 3:
            lines.append("**严重不平衡。** 建议：")
            lines.append("1. 对少数类进行过采样 (SMOTE 或重复采样)")
            lines.append("2. 使用 class weights 在训练时补偿")
            lines.append("3. 考虑调整 LF 阈值以增加少数类覆盖")
            lines.append("4. 使用 focal loss 代替 cross-entropy")
        elif ratio > 1.5:
            lines.append("**中度不平衡。** 建议使用 class weights 或在评估时关注 F1 而非 accuracy。")
        else:
            lines.append("**类别相对平衡。** 标准训练流程即可。")
    else:
        lines.append("无高置信度窗口，无法评估类别平衡。")
    lines.append("")

    report_path.write_text("\n".join(lines))
    print(f"Report saved to {report_path}")


if __name__ == "__main__":
    DATA_PATH = (
        "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/"
        "agent_progress_probe/artifacts/data/swe_agent_trajectories_1000.jsonl"
    )
    OUTPUT_PATH = (
        "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/"
        "agent_progress_probe/artifacts/data/windows_labeled.jsonl"
    )
    REPORT_PATH = (
        "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/"
        "agent_progress_probe/artifacts/label_statistics_report.md"
    )

    # First test with 10 trajectories
    print("=" * 60)
    print("VALIDATION: Testing with 10 trajectories")
    print("=" * 60)

    test_stats = run_pipeline(DATA_PATH, OUTPUT_PATH + ".test", limit=10)
    print(f"\nTest results: {test_stats['total_windows']} windows from {test_stats['total_trajectories']} trajectories")
    print(f"LF coverage:")
    for lf_name, _ in ALL_LFS:
        counts = test_stats["lf_counts"][lf_name]
        non_abstain = sum(v for k, v in counts.items() if k != -1)
        print(f"  {lf_name}: {non_abstain}/{test_stats['total_windows']} non-abstain")
    print(f"Majority vote: {test_stats['majority_counts']}")

    # Spot check: print a few windows with labels
    print("\n" + "=" * 60)
    print("SPOT CHECK: First 3 windows from first trajectory")
    print("=" * 60)

    from data_loader import load_trajectories_streaming
    traj = next(load_trajectories_streaming(DATA_PATH, limit=1))
    windows = process_trajectory(traj)
    for w in windows[:3]:
        print(f"\nWindow {w['window_idx']}: steps {w['step_indices'][0]}-{w['step_indices'][-1]}")
        print(f"  Labels: {w['labels']}")
        print(f"  Majority: {w['majority_label']} (confidence={w['confidence']})")
        # Show commands in window
        for s in w["steps"]:
            if s.is_action and s.command:
                cmd_preview = s.command[:80].replace('\n', ' ')
                print(f"    Step {s.index} cmd: {cmd_preview}")

    # Full run
    print("\n" + "=" * 60)
    print("FULL RUN: Processing all 1000 trajectories")
    print("=" * 60)

    stats = run_pipeline(DATA_PATH, OUTPUT_PATH)
    generate_report(stats, REPORT_PATH)

    print(f"\nDone. {stats['total_windows']:,} windows labeled.")
    print(f"Output: {OUTPUT_PATH}")
    print(f"Report: {REPORT_PATH}")

    # Clean up test file
    Path(OUTPUT_PATH + ".test").unlink(missing_ok=True)
