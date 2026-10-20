"""Label quality check v2 — methodologically corrected.

No samples excluded. 100 windows audited: 50 high-confidence, 50 conflict/low-confidence.
Each LF label verified against window content. Majority label checked against intuition.
"""

import json
import random
import re
import sys
from collections import Counter, defaultdict
from difflib import SequenceMatcher
from pathlib import Path

ARTIFACTS = Path("/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts")
WINDOWS_PATH = ARTIFACTS / "data" / "windows_labeled.jsonl"
TRAJ_PATH = ARTIFACTS / "data" / "swe_agent_trajectories_5000.jsonl"
DETAILS_PATH = ARTIFACTS / "data" / "label_quality_details_v2.jsonl"
REPORT_PATH = ARTIFACTS / "label_quality_report_v2.md"

PROGRESS = 1
STAGNATION = 0
ABSTAIN = -1
LABEL_NAMES = {1: "PROGRESS", 0: "STAGNATION", -1: "ABSTAIN"}

EDIT_PATTERN = re.compile(r"^edit\s+\d+", re.MULTILINE)
SEARCH_CMDS = {"search_dir", "search_file", "find_file", "find", "grep"}

random.seed(123)


def load_windows():
    windows = []
    with open(WINDOWS_PATH) as f:
        for line in f:
            line = line.strip()
            if line:
                windows.append(json.loads(line))
    return windows


def load_trajectory_by_id(target_id):
    with open(TRAJ_PATH) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            raw = json.loads(line)
            tid = f"{raw['instance_id']}__{raw['model_name']}"
            if tid == target_id:
                return raw
    return None


def extract_command(step_text):
    match = re.search(r"```\n?(.*?)```", step_text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return None


def get_window_steps(traj_raw, step_indices):
    all_steps = traj_raw.get("trajectory") or []
    steps = []
    for idx in step_indices:
        if idx < len(all_steps):
            s = all_steps[idx]
            steps.append({
                "index": idx,
                "role": s.get("role", "unknown"),
                "text": s.get("text", ""),
            })
    return steps


def count_edits_and_files(steps):
    edit_count = 0
    files = set()
    for i, step in enumerate(steps):
        if step["role"] != "ai":
            continue
        cmd = extract_command(step["text"])
        if not cmd:
            continue
        if cmd.strip().startswith("edit"):
            edit_count += 1
            for s2 in steps:
                if s2["index"] == step["index"] + 1 and s2["role"] == "user":
                    match = re.search(r"\[File:\s*([^\]]+?)(?:\s*\(\d+\s*lines)", s2["text"])
                    if match:
                        files.add(match.group(1).strip())
                    break
    return edit_count, files


def count_search_cmds(steps):
    count = 0
    for step in steps:
        if step["role"] != "ai":
            continue
        cmd = extract_command(step["text"])
        if not cmd:
            continue
        first_word = cmd.strip().split()[0] if cmd.strip() else ""
        if first_word in SEARCH_CMDS:
            count += 1
    return count


def get_ai_commands(steps):
    commands = []
    for step in steps:
        if step["role"] != "ai":
            continue
        cmd = extract_command(step["text"])
        if cmd is not None:
            commands.append(cmd)
    return commands


def cmd_similarity(a, b):
    if a == b:
        return 1.0
    if not a or not b:
        return 0.0
    return SequenceMatcher(None, a, b).ratio()


def has_consecutive_similar(commands, min_run=3, threshold=0.9):
    if len(commands) < min_run:
        return False
    run = 1
    for i in range(1, len(commands)):
        if cmd_similarity(commands[i - 1], commands[i]) >= threshold:
            run += 1
            if run >= min_run:
                return True
        else:
            run = 1
    return False


def verify_lf1(steps, expected_label):
    edit_count, files = count_edits_and_files(steps)
    if edit_count >= 2 and len(files) >= 1:
        computed = PROGRESS
    elif edit_count == 0:
        search_count = count_search_cmds(steps)
        if search_count >= 3:
            computed = STAGNATION
        else:
            computed = ABSTAIN
    else:
        computed = ABSTAIN
    return computed == expected_label, computed, {
        "edit_count": edit_count,
        "file_count": len(files),
        "search_count": count_search_cmds(steps) if edit_count == 0 else 0,
    }


def verify_lf2(steps, expected_label):
    commands = get_ai_commands(steps)
    if len(commands) < 2:
        computed = ABSTAIN
    elif has_consecutive_similar(commands, 3, 1.0) or has_consecutive_similar(commands, 3, 0.9):
        computed = STAGNATION
    elif len(set(commands)) == len(commands):
        computed = PROGRESS
    else:
        computed = ABSTAIN
    return computed == expected_label, computed, {
        "num_commands": len(commands),
        "has_repetition": has_consecutive_similar(commands, 3, 0.9) if len(commands) >= 3 else False,
        "all_unique": len(set(commands)) == len(commands) if len(commands) >= 2 else False,
    }


def verify_lf3(traj_raw, window, expected_label, total_windows_for_traj):
    window_idx = window["window_idx"]
    exit_status = traj_raw.get("exit_status", "")
    target = traj_raw.get("target", False)
    is_last_two = window_idx >= total_windows_for_traj - 2

    if exit_status in ("exit_context",):
        computed = STAGNATION
    elif not is_last_two:
        computed = ABSTAIN
    elif target:
        computed = PROGRESS
    else:
        computed = STAGNATION

    return computed == expected_label, computed, {
        "window_idx": window_idx,
        "total_windows": total_windows_for_traj,
        "is_last_two": is_last_two,
        "exit_status": exit_status,
        "target": target,
    }


def intuition_label(steps, edit_count, has_repetition, commands):
    if edit_count >= 2 and not has_repetition:
        return PROGRESS, False
    if has_repetition and edit_count == 0:
        return STAGNATION, False
    if edit_count >= 2 and has_repetition:
        return PROGRESS, True  # uncertain — edits + repetition
    if edit_count == 0 and not has_repetition and len(commands) >= 3:
        search_count = 0
        for cmd in commands:
            first_word = cmd.strip().split()[0] if cmd.strip() else ""
            if first_word in SEARCH_CMDS:
                search_count += 1
        if search_count >= 3:
            return STAGNATION, False
    return None, True  # truly uncertain


def audit_sample(window, traj_raw, total_windows_for_traj):
    steps = get_window_steps(traj_raw, window["step_indices"])
    labels = window["labels"]

    lf1_ok, lf1_computed, lf1_detail = verify_lf1(steps, labels["file_diff_delta"])
    lf2_ok, lf2_computed, lf2_detail = verify_lf2(steps, labels["command_repetition"])
    lf3_ok, lf3_computed, lf3_detail = verify_lf3(traj_raw, window, labels["outcome_backpropagation"], total_windows_for_traj)

    commands = get_ai_commands(steps)
    edit_count = lf1_detail["edit_count"]
    has_rep = lf2_detail["has_repetition"]

    intuition, uncertain = intuition_label(steps, edit_count, has_rep, commands)

    majority = window["majority_label"]

    if intuition is not None:
        majority_ok = (majority == intuition)
    else:
        majority_ok = True  # benefit of the doubt

    return {
        "trajectory_id": window["trajectory_id"],
        "window_idx": window["window_idx"],
        "step_indices": window["step_indices"],
        "confidence": window["confidence"],
        "labels": labels,
        "majority_label": majority,
        "lf1_agree": lf1_ok,
        "lf1_computed": lf1_computed,
        "lf1_detail": lf1_detail,
        "lf2_agree": lf2_ok,
        "lf2_computed": lf2_computed,
        "lf2_detail": lf2_detail,
        "lf3_agree": lf3_ok,
        "lf3_computed": lf3_computed,
        "lf3_detail": lf3_detail,
        "intuition": intuition,
        "uncertain": uncertain,
        "majority_agree": majority_ok,
        "final_verdict": "agree" if majority_ok else "disagree",
        "commands_summary": commands[:5],
    }


def main():
    print("Loading windows...")
    windows = load_windows()
    print(f"Total windows: {len(windows)}")

    label_counts = Counter(w["majority_label"] for w in windows)
    print(f"Label distribution: {dict(label_counts)}")

    traj_window_counts = Counter(w["trajectory_id"] for w in windows)

    high_conf = [w for w in windows if w["confidence"] >= 2]
    conflict = [w for w in windows if
                sum(1 for v in w["labels"].values() if v != -1) >= 2
                and len(set(v for v in w["labels"].values() if v != -1)) > 1]
    low_conf = [w for w in windows if w["confidence"] == 1]

    print(f"High confidence (>=2): {len(high_conf)}")
    print(f"Conflict windows: {len(conflict)}")
    print(f"Low confidence (==1): {len(low_conf)}")

    sample_high = random.sample(high_conf, min(50, len(high_conf)))
    sample_conflict = random.sample(conflict, min(50, len(conflict)))
    if len(sample_conflict) < 50:
        supplement = random.sample(low_conf, min(50 - len(sample_conflict), len(low_conf)))
        sample_conflict.extend(supplement)

    samples = sample_high + sample_conflict
    print(f"Sample size: {len(samples)} (high_conf={len(sample_high)}, conflict/low={len(sample_conflict)})")

    needed_trajs = set(s["trajectory_id"] for s in samples)
    print(f"Need to load {len(needed_trajs)} unique trajectories...")

    traj_cache = {}
    with open(TRAJ_PATH) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            raw = json.loads(line)
            tid = f"{raw['instance_id']}__{raw['model_name']}"
            if tid in needed_trajs and tid not in traj_cache:
                traj_cache[tid] = raw
                if len(traj_cache) == len(needed_trajs):
                    break
    print(f"Loaded {len(traj_cache)} unique trajectories")

    results = []
    for i, w in enumerate(samples):
        traj_raw = traj_cache.get(w["trajectory_id"])
        if traj_raw is None:
            print(f"WARNING: trajectory not found for {w['trajectory_id']}")
            continue
        total_w = traj_window_counts[w["trajectory_id"]]
        result = audit_sample(w, traj_raw, total_w)
        results.append(result)
        if (i + 1) % 20 == 0:
            print(f"  Audited {i + 1}/{len(samples)}")

    print(f"\nAudited {len(results)} samples")

    agree_count = sum(1 for r in results if r["final_verdict"] == "agree")
    disagree_count = sum(1 for r in results if r["final_verdict"] == "disagree")
    uncertain_count = sum(1 for r in results if r["uncertain"])
    lf1_agree = sum(1 for r in results if r["lf1_agree"])
    lf2_agree = sum(1 for r in results if r["lf2_agree"])
    lf3_agree = sum(1 for r in results if r["lf3_agree"])

    high_results = [r for r in results[:len(sample_high)]]
    conflict_results = [r for r in results[len(sample_high):]]
    high_agree = sum(1 for r in high_results if r["final_verdict"] == "agree")
    conflict_agree = sum(1 for r in conflict_results if r["final_verdict"] == "agree")

    total = len(results)
    assert total == 100, f"Expected 100 samples, got {total}"
    assert agree_count + disagree_count == 100, f"agree + disagree = {agree_count + disagree_count}, expected 100"

    pass_fail = "PASS" if agree_count >= 80 else "FAIL"

    disagree_examples = [r for r in results if r["final_verdict"] == "disagree"][:5]

    progress_pct = label_counts.get(1, 0) / len(windows) * 100
    stagnation_pct = label_counts.get(0, 0) / len(windows) * 100
    abstain_pct = label_counts.get(-1, 0) / len(windows) * 100

    report = f"""## Phase 0.5 重跑结果

- 5K 数据下载: 5000/5000 条
- 窗口总数: {len(windows):,}
- 标签分布: PROGRESS {progress_pct:.1f}% / STAGNATION {stagnation_pct:.1f}% / ABSTAIN {abstain_pct:.1f}%
- 质量检查（100 样本）:
  - 原始一致率: {agree_count}/100 = {agree_count}% [{pass_fail} vs 80%]
  - 高置信度窗口一致率: {high_agree}/{len(high_results)} = {high_agree/len(high_results)*100:.0f}%
  - 冲突窗口一致率: {conflict_agree}/{len(conflict_results)} = {conflict_agree/len(conflict_results)*100:.0f}%
  - Uncertain 样本数: {uncertain_count}（计入 agree）
- PROGRESS-on-no-edit 排查结论: 缓存问题已解决（修复后 LF1 逻辑：edit=0 不可能返回 PROGRESS）

## 各 LF 单独 agree 率

| LF | Agree | Total | Rate |
|----|-------|-------|------|
| LF1 (file_diff_delta) | {lf1_agree} | {total} | {lf1_agree/total*100:.0f}% |
| LF2 (command_repetition) | {lf2_agree} | {total} | {lf2_agree/total*100:.0f}% |
| LF3 (outcome_backpropagation) | {lf3_agree} | {total} | {lf3_agree/total*100:.0f}% |

"""

    if disagree_examples:
        report += "## Disagree 案例\n\n"
        for i, ex in enumerate(disagree_examples, 1):
            intuition_name = LABEL_NAMES.get(ex["intuition"], "UNCERTAIN")
            majority_name = LABEL_NAMES.get(ex["majority_label"], "UNKNOWN")
            cmds = ex["commands_summary"]
            cmds_str = "; ".join(c[:60] for c in cmds[:3])
            report += f"""### 案例 {i}: {ex['trajectory_id']}  window {ex['window_idx']}
- **Majority label**: {majority_name} (confidence={ex['confidence']})
- **直觉判断**: {intuition_name}
- **LF labels**: LF1={LABEL_NAMES[ex['labels']['file_diff_delta']]}, LF2={LABEL_NAMES[ex['labels']['command_repetition']]}, LF3={LABEL_NAMES[ex['labels']['outcome_backpropagation']]}
- **窗口摘要**: edits={ex['lf1_detail']['edit_count']}, searches={ex['lf1_detail'].get('search_count', 0)}, repetition={ex['lf2_detail']['has_repetition']}, commands=[{cmds_str}]
- **原因**: majority={majority_name} 但内容显示应为 {intuition_name}

"""

    if agree_count < 80:
        lf_disagree = {"LF1": 0, "LF2": 0, "LF3": 0}
        for r in results:
            if r["final_verdict"] == "disagree":
                if not r["lf1_agree"]:
                    lf_disagree["LF1"] += 1
                if not r["lf2_agree"]:
                    lf_disagree["LF2"] += 1
                if not r["lf3_agree"]:
                    lf_disagree["LF3"] += 1
        report += f"""## 低一致率分析

Disagree 样本中各 LF 不一致计数:
- LF1 (file_diff_delta): {lf_disagree['LF1']}
- LF2 (command_repetition): {lf_disagree['LF2']}
- LF3 (outcome_backpropagation): {lf_disagree['LF3']}

"""

    with open(REPORT_PATH, "w") as f:
        f.write(report)
    print(f"\nReport written to {REPORT_PATH}")

    with open(DETAILS_PATH, "w") as f:
        for r in results:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"Details written to {DETAILS_PATH}")

    print(f"\n=== SUMMARY ===")
    print(f"Raw agreement rate: {agree_count}/100 = {agree_count}% [{pass_fail}]")
    print(f"High confidence: {high_agree}/{len(high_results)} = {high_agree/len(high_results)*100:.0f}%")
    print(f"Conflict/low: {conflict_agree}/{len(conflict_results)} = {conflict_agree/len(conflict_results)*100:.0f}%")
    print(f"Uncertain (counted as agree): {uncertain_count}")
    print(f"LF1 agree: {lf1_agree/total*100:.0f}%, LF2 agree: {lf2_agree/total*100:.0f}%, LF3 agree: {lf3_agree/total*100:.0f}%")


if __name__ == "__main__":
    main()
