"""Phase 0.5: Label quality spot-check with rule-based AI review."""

from __future__ import annotations

import json
import random
import re
from collections import Counter, defaultdict
from pathlib import Path

ARTIFACTS = Path("/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts")
WINDOWS_PATH = ARTIFACTS / "data" / "windows_labeled.jsonl"
TRAJ_PATH = ARTIFACTS / "data" / "swe_agent_trajectories_1000.jsonl"
DETAILS_PATH = ARTIFACTS / "data" / "label_quality_details.jsonl"
REPORT_PATH = ARTIFACTS / "label_quality_report.md"

PROGRESS = 1
STAGNATION = 0
ABSTAIN = -1

random.seed(42)


def load_windows() -> list[dict]:
    windows = []
    with open(WINDOWS_PATH) as f:
        for line in f:
            line = line.strip()
            if line:
                windows.append(json.loads(line))
    return windows


def build_trajectory_index() -> dict[str, dict]:
    """Build {trajectory_id: raw_record} index."""
    index = {}
    with open(TRAJ_PATH) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            raw = json.loads(line)
            tid = f"{raw['instance_id']}__{raw['model_name']}"
            index[tid] = raw
    return index


def classify_windows(windows: list[dict]) -> dict:
    high_conf_progress = []
    high_conf_stagnation = []
    conflict = []
    low_conf = []

    for w in windows:
        labels = w["labels"]
        non_abstain = {k: v for k, v in labels.items() if v != ABSTAIN}

        if len(non_abstain) >= 2:
            vals = set(non_abstain.values())
            if len(vals) > 1:
                conflict.append(w)
                continue

        if w["confidence"] >= 2:
            if w["majority_label"] == PROGRESS:
                high_conf_progress.append(w)
            elif w["majority_label"] == STAGNATION:
                high_conf_stagnation.append(w)
        elif w["confidence"] == 1:
            low_conf.append(w)

    return {
        "high_conf_progress": high_conf_progress,
        "high_conf_stagnation": high_conf_stagnation,
        "conflict": conflict,
        "low_conf": low_conf,
    }


def sample_windows(classified: dict) -> list[dict]:
    samples = []

    hc_prog = classified["high_conf_progress"]
    hc_stag = classified["high_conf_stagnation"]

    n_prog = min(25, len(hc_prog))
    n_stag = 50 - n_prog
    n_stag = min(n_stag, len(hc_stag))

    samples.extend(random.sample(hc_prog, n_prog))
    samples.extend(random.sample(hc_stag, n_stag))

    for s in samples:
        s["_sample_group"] = "high_confidence"

    conflict = classified["conflict"]
    low_conf = classified["low_conf"]

    n_conflict = min(50, len(conflict))
    conflict_samples = random.sample(conflict, n_conflict)
    for s in conflict_samples:
        s["_sample_group"] = "conflict"

    remaining = 50 - n_conflict
    if remaining > 0 and low_conf:
        low_samples = random.sample(low_conf, min(remaining, len(low_conf)))
        for s in low_samples:
            s["_sample_group"] = "low_confidence"
        conflict_samples.extend(low_samples)

    samples.extend(conflict_samples)
    return samples


def get_window_steps(window: dict, traj_index: dict) -> list[dict]:
    tid = window["trajectory_id"]
    raw = traj_index.get(tid)
    if not raw:
        return []
    traj_steps = raw.get("trajectory", [])
    result = []
    for idx in window["step_indices"]:
        if idx < len(traj_steps):
            step = traj_steps[idx]
            result.append({
                "index": idx,
                "role": step.get("role", "unknown"),
                "text": step.get("text", "")[:2000],
            })
    return result


def extract_command(text: str) -> str | None:
    match = re.search(r"```\n?(.*?)```", text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return None


def review_window(window: dict, steps: list[dict]) -> dict:
    """Rule-based review of a labeled window."""
    label = window["majority_label"]
    labels = window["labels"]

    has_edit = False
    commands = []
    error_counts = []
    search_no_edit = True

    for step in steps:
        text = step["text"]
        role = step["role"]

        if role == "ai":
            cmd = extract_command(text)
            if cmd:
                first_word = cmd.strip().split()[0] if cmd.strip() else ""
                commands.append(first_word)
                if first_word == "edit":
                    has_edit = True
                    search_no_edit = False

        if role == "user" and step["index"] > 0:
            err_count = text.count("Traceback") + text.count("Error")
            error_counts.append(err_count)

    cmd_counter = Counter(commands)
    has_repeated_cmd = any(c >= 3 for c in cmd_counter.values())
    errors_decreasing = (
        len(error_counts) >= 2
        and error_counts[-1] < error_counts[0]
        and error_counts[0] > 0
    )

    search_cmds = {"search_dir", "search_file", "find_file", "find", "grep"}
    only_search = all(c in search_cmds for c in commands if c) and len(commands) > 0

    verdict = "needs_human_review"
    reason = "no clear signal matched"

    if has_edit and label == PROGRESS:
        verdict = "agree"
        reason = "edit commands present, consistent with progress label"
    elif has_edit and label == STAGNATION:
        if has_repeated_cmd:
            verdict = "agree"
            reason = "repeated commands despite edits, consistent with stagnation"
        else:
            verdict = "disagree"
            reason = "edit commands present but labeled stagnation"
    elif has_repeated_cmd and label == STAGNATION:
        verdict = "agree"
        reason = "repeated commands (≥3 same), consistent with stagnation"
    elif has_repeated_cmd and label == PROGRESS:
        verdict = "disagree"
        reason = "repeated commands but labeled progress"
    elif errors_decreasing and label == PROGRESS:
        verdict = "agree"
        reason = "errors decreasing, consistent with progress"
    elif only_search and not has_edit and label == STAGNATION:
        verdict = "agree"
        reason = "search/find only without edit, consistent with stagnation"
    elif only_search and not has_edit and label == PROGRESS:
        verdict = "disagree"
        reason = "search/find only but labeled progress"
    elif not has_edit and not has_repeated_cmd and label == STAGNATION:
        verdict = "agree"
        reason = "no edits, likely exploration/stagnation"

    sole_voter = None
    non_abstain = {k: v for k, v in labels.items() if v != ABSTAIN}
    if len(non_abstain) == 1:
        sole_voter = list(non_abstain.keys())[0]

    return {
        "trajectory_id": window["trajectory_id"],
        "window_idx": window["window_idx"],
        "sample_group": window.get("_sample_group", "unknown"),
        "lf_labels": labels,
        "majority_label": label,
        "confidence": window["confidence"],
        "verdict": verdict,
        "reason": reason,
        "sole_voter": sole_voter,
        "features": {
            "has_edit": has_edit,
            "has_repeated_cmd": has_repeated_cmd,
            "errors_decreasing": errors_decreasing,
            "only_search": only_search,
            "commands": commands,
        },
        "step_summary": [
            f"[{s['index']}] {s['role']}: {s['text'][:150].replace(chr(10), ' ')}"
            for s in steps[:5]
        ],
    }


def compute_lf_accuracy(results: list[dict]) -> dict[str, dict]:
    """Per-LF accuracy when it's the sole voter."""
    lf_stats = defaultdict(lambda: {"agree": 0, "disagree": 0, "needs_human_review": 0, "total": 0})
    for r in results:
        if r["sole_voter"]:
            lf = r["sole_voter"]
            lf_stats[lf][r["verdict"]] += 1
            lf_stats[lf]["total"] += 1
    return dict(lf_stats)


def generate_report(results: list[dict], classified: dict) -> str:
    total = len(results)
    agree = sum(1 for r in results if r["verdict"] == "agree")
    disagree = sum(1 for r in results if r["verdict"] == "disagree")
    needs_review = sum(1 for r in results if r["verdict"] == "needs_human_review")

    hc_results = [r for r in results if r["sample_group"] == "high_confidence"]
    cf_results = [r for r in results if r["sample_group"] in ("conflict", "low_confidence")]

    hc_agree = sum(1 for r in hc_results if r["verdict"] == "agree")
    cf_agree = sum(1 for r in cf_results if r["verdict"] == "agree")

    overall_rate = agree / total * 100 if total else 0
    hc_rate = hc_agree / len(hc_results) * 100 if hc_results else 0
    cf_rate = cf_agree / len(cf_results) * 100 if cf_results else 0

    # Effective agreement: agree / (agree + disagree), excluding needs_human_review
    decided = agree + disagree
    effective_rate = agree / decided * 100 if decided else 0

    lf_acc = compute_lf_accuracy(results)

    disagree_cases = [r for r in results if r["verdict"] == "disagree"][:5]
    review_cases = [r for r in results if r["verdict"] == "needs_human_review"][:5]

    lines = [
        "# Label Quality Report — Phase 0.5",
        "",
        "## 1. 总体一致率",
        "",
        f"| 指标 | 值 |",
        f"|------|-----|",
        f"| 抽样总数 | {total} |",
        f"| Agree (审核与 LF 一致) | {agree} ({agree/total*100:.1f}%) |",
        f"| Disagree (审核与 LF 不一致) | {disagree} ({disagree/total*100:.1f}%) |",
        f"| Needs Human Review | {needs_review} ({needs_review/total*100:.1f}%) |",
        f"| **有效一致率 (agree / (agree+disagree))** | **{effective_rate:.1f}%** |",
        "",
        "## 2. 分组一致率",
        "",
        f"| 组别 | 样本数 | Agree | Agree 率 |",
        f"|------|--------|-------|----------|",
        f"| 高置信度 (conf≥2) | {len(hc_results)} | {hc_agree} | {hc_rate:.1f}% |",
        f"| 冲突/低置信度 | {len(cf_results)} | {cf_agree} | {cf_rate:.1f}% |",
        "",
        "## 3. 各 LF 单独投票时的准确率",
        "",
        "| LF 名称 | 单独投票样本数 | Agree | Disagree | Needs Review | Agree/(Agree+Disagree) |",
        "|---------|---------------|-------|----------|-------------|----------------------|",
    ]

    for lf_name, stats in sorted(lf_acc.items()):
        t = stats["total"]
        a = stats["agree"]
        d = stats["disagree"]
        nr = stats["needs_human_review"]
        ad = a + d
        rate = f"{a/ad*100:.1f}%" if ad > 0 else "N/A"
        lines.append(f"| {lf_name} | {t} | {a} | {d} | {nr} | {rate} |")

    lines.extend([
        "",
        "## 4. 典型 Disagree 案例",
        "",
    ])

    for i, case in enumerate(disagree_cases, 1):
        label_str = "progress" if case["majority_label"] == 1 else "stagnation"
        lines.append(f"### Case {i}: {case['trajectory_id']} window {case['window_idx']}")
        lines.append(f"- **LF 标签**: {label_str} (conf={case['confidence']})")
        lines.append(f"- **LF 投票**: {case['lf_labels']}")
        lines.append(f"- **审核意见**: {case['reason']}")
        lines.append(f"- **特征**: edit={case['features']['has_edit']}, "
                      f"repeated_cmd={case['features']['has_repeated_cmd']}, "
                      f"search_only={case['features']['only_search']}")
        lines.append(f"- **窗口摘要**:")
        for s in case["step_summary"]:
            lines.append(f"  - `{s}`")
        lines.append("")

    lines.extend([
        "## 5. 典型 Needs Human Review 案例",
        "",
    ])

    for i, case in enumerate(review_cases, 1):
        label_str = "progress" if case["majority_label"] == 1 else "stagnation"
        lines.append(f"### Case {i}: {case['trajectory_id']} window {case['window_idx']}")
        lines.append(f"- **LF 标签**: {label_str} (conf={case['confidence']})")
        lines.append(f"- **LF 投票**: {case['lf_labels']}")
        lines.append(f"- **特征**: edit={case['features']['has_edit']}, "
                      f"repeated_cmd={case['features']['has_repeated_cmd']}, "
                      f"commands={case['features']['commands'][:5]}")
        lines.append(f"- **窗口摘要**:")
        for s in case["step_summary"]:
            lines.append(f"  - `{s}`")
        lines.append("")

    lines.extend([
        "## 6. 结论",
        "",
    ])

    target_met = effective_rate >= 80.0
    if target_met:
        lines.append(f"**有效一致率 {effective_rate:.1f}% ≥ 80% 目标，标签质量达标。**")
    else:
        lines.append(f"**有效一致率 {effective_rate:.1f}% < 80% 目标，标签质量未达标。**")

    lines.append("")
    lines.append("### 分析")
    lines.append("")
    lines.append(f"- 高置信度窗口一致率 ({hc_rate:.1f}%) vs 冲突窗口 ({cf_rate:.1f}%)，"
                 f"差异 {abs(hc_rate - cf_rate):.1f}pp")

    if lf_acc:
        worst_lf = min(lf_acc.items(),
                       key=lambda x: x[1]["agree"] / max(x[1]["agree"] + x[1]["disagree"], 1))
        wl_name = worst_lf[0]
        wl_a = worst_lf[1]["agree"]
        wl_d = worst_lf[1]["disagree"]
        wl_rate = wl_a / max(wl_a + wl_d, 1) * 100
        lines.append(f"- 准确率最低的 LF: **{wl_name}** ({wl_rate:.1f}%)")
        if not target_met:
            lines.append(f"- 建议优先修正 {wl_name}，其 disagree 案例多为: "
                         + (f"有 edit 但标为 stagnation" if wl_name == "file_diff_delta" else
                            f"规则过于宽松/严格"))

    lines.append("")
    lines.append("### 数据分布参考")
    lines.append("")
    lines.append(f"| 类别 | 数量 |")
    lines.append(f"|------|------|")
    lines.append(f"| 高置信度 progress | {len(classified['high_conf_progress'])} |")
    lines.append(f"| 高置信度 stagnation | {len(classified['high_conf_stagnation'])} |")
    lines.append(f"| 冲突窗口 | {len(classified['conflict'])} |")
    lines.append(f"| 低置信度 (conf=1) | {len(classified['low_conf'])} |")
    lines.append("")

    return "\n".join(lines)


def main():
    print("Loading windows...")
    windows = load_windows()
    print(f"  Total: {len(windows)}")

    print("Classifying windows...")
    classified = classify_windows(windows)
    for k, v in classified.items():
        print(f"  {k}: {len(v)}")

    print("Sampling 100 windows...")
    samples = sample_windows(classified)
    group_counts = Counter(s.get("_sample_group") for s in samples)
    print(f"  Sampled: {len(samples)} — {dict(group_counts)}")

    print("Loading trajectory index...")
    traj_index = build_trajectory_index()
    print(f"  Trajectories: {len(traj_index)}")

    print("Running rule-based review...")
    results = []
    for w in samples:
        steps = get_window_steps(w, traj_index)
        result = review_window(w, steps)
        results.append(result)

    verdict_counts = Counter(r["verdict"] for r in results)
    print(f"  Verdicts: {dict(verdict_counts)}")

    print(f"Saving details to {DETAILS_PATH}...")
    with open(DETAILS_PATH, "w") as f:
        for r in results:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

    print("Generating report...")
    report = generate_report(results, classified)
    with open(REPORT_PATH, "w") as f:
        f.write(report)
    print(f"Report saved to {REPORT_PATH}")

    # Print a few sample cases for verification
    print("\n" + "=" * 60)
    print("SAMPLE CASES FOR VERIFICATION")
    print("=" * 60)

    for verdict_type in ["agree", "disagree", "needs_human_review"]:
        cases = [r for r in results if r["verdict"] == verdict_type]
        if cases:
            c = cases[0]
            label_str = "progress" if c["majority_label"] == 1 else "stagnation"
            print(f"\n--- {verdict_type.upper()} example ---")
            print(f"  Trajectory: {c['trajectory_id']}, window {c['window_idx']}")
            print(f"  Group: {c['sample_group']}, Label: {label_str}, Conf: {c['confidence']}")
            print(f"  LF votes: {c['lf_labels']}")
            print(f"  Reason: {c['reason']}")
            print(f"  Features: edit={c['features']['has_edit']}, "
                  f"repeat={c['features']['has_repeated_cmd']}, "
                  f"search_only={c['features']['only_search']}")
            for s in c["step_summary"][:3]:
                print(f"    {s}")


if __name__ == "__main__":
    main()
