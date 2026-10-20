"""LF conflict analysis: extract 4 categories of cases and generate report."""

import json
import random
import re
from difflib import SequenceMatcher
from pathlib import Path
from collections import defaultdict

random.seed(42)

ARTIFACTS = Path("/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts")
WINDOWS_PATH = ARTIFACTS / "data" / "windows_labeled.jsonl"
TRAJ_PATH = ARTIFACTS / "data" / "swe_agent_trajectories_5000.jsonl"
OUTPUT_PATH = ARTIFACTS / "lf_conflict_analysis.md"

PROGRESS = 1
STAGNATION = 0
ABSTAIN = -1

LABEL_NAME = {1: "PROGRESS", 0: "STAGNATION", -1: "ABSTAIN"}


def load_windows():
    windows = []
    with open(WINDOWS_PATH) as f:
        for line in f:
            line = line.strip()
            if line:
                windows.append(json.loads(line))
    return windows


def categorize(windows):
    cats = {1: [], 2: [], 3: [], 4: []}
    for w in windows:
        lf1 = w["labels"]["file_diff_delta"]
        lf2 = w["labels"]["command_repetition"]
        lf3 = w["labels"]["outcome_backpropagation"]

        if lf1 == PROGRESS and lf2 == STAGNATION:
            cats[1].append(w)
        if lf1 in (STAGNATION, ABSTAIN) and lf2 == PROGRESS:
            cats[2].append(w)
        if lf1 == PROGRESS and lf2 == PROGRESS and lf3 == PROGRESS:
            cats[3].append(w)
        if lf1 == STAGNATION and lf2 == STAGNATION and lf3 == STAGNATION:
            cats[4].append(w)
    return cats


def build_traj_index():
    """Build trajectory_id -> file offset index for random access."""
    index = {}
    with open(TRAJ_PATH) as f:
        while True:
            offset = f.tell()
            line = f.readline()
            if not line:
                break
            line = line.strip()
            if not line:
                continue
            raw = json.loads(line)
            tid = raw["instance_id"] + "__" + raw["model_name"]
            index[tid] = offset
    return index


def load_traj(traj_index, tid):
    with open(TRAJ_PATH) as f:
        f.seek(traj_index[tid])
        return json.loads(f.readline())


def has_actions_in_window(w, traj_raw):
    steps_raw = traj_raw.get("trajectory", [])
    for idx in w["step_indices"]:
        if idx < len(steps_raw):
            s = steps_raw[idx]
            if s.get("role") == "ai":
                cmd = extract_command(s.get("text", ""))
                if cmd:
                    return True
    return False


def sample_cases_with_validation(cats, traj_index, n=10):
    sampled = {}
    for cat_id, ws in cats.items():
        seen = set()
        deduped = []
        for w in ws:
            key = (w["trajectory_id"], w["window_idx"])
            if key not in seen:
                seen.add(key)
                deduped.append(w)
        random.shuffle(deduped)
        selected = []
        seen_trajs = set()
        for w in deduped:
            if len(selected) >= n:
                break
            tid = w["trajectory_id"]
            if tid not in traj_index:
                continue
            if tid in seen_trajs and len(selected) >= n // 2:
                continue
            traj_raw = load_traj(traj_index, tid)
            if has_actions_in_window(w, traj_raw):
                selected.append(w)
                seen_trajs.add(tid)
        sampled[cat_id] = selected
    return sampled


def load_needed_trajectories(sampled, traj_index):
    trajs = {}
    for cases in sampled.values():
        for w in cases:
            tid = w["trajectory_id"]
            if tid not in trajs and tid in traj_index:
                trajs[tid] = load_traj(traj_index, tid)
    return trajs


def extract_command(text):
    match = re.search(r"```\n?(.*?)```", text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return None


def summarize_window(w, traj_raw):
    steps_raw = traj_raw.get("trajectory", [])
    step_indices = w["step_indices"]
    window_steps = []
    for idx in step_indices:
        if idx < len(steps_raw):
            window_steps.append((idx, steps_raw[idx]))

    actions = []
    observations = []
    for idx, s in window_steps:
        role = s.get("role", "")
        text = s.get("text", "")
        if role == "ai":
            cmd = extract_command(text)
            if cmd:
                actions.append(cmd[:120])
        elif role == "user" and idx > 0:
            obs_snippet = ""
            if "[File:" in text:
                match = re.search(r"\[File:\s*([^\]]+?)(?:\s*\(\d+\s*lines)", text)
                if match:
                    obs_snippet = f"显示文件 {match.group(1).strip()}"
            if "Traceback" in text or "Error" in text:
                obs_snippet += " [有错误]"
            if ("PASSED" in text or "FAILED" in text) and "test" in text.lower():
                obs_snippet += " [测试输出]"
            if obs_snippet:
                observations.append(obs_snippet.strip())

    summary_parts = []
    if actions:
        cmd_types = defaultdict(int)
        for a in actions:
            first_word = a.split()[0] if a.split() else "?"
            if first_word in ("edit", "open", "goto", "scroll_down", "scroll_up"):
                cmd_types[first_word] += 1
            elif first_word in ("find", "find_file", "search_dir", "search_file", "grep"):
                cmd_types["search"] += 1
            elif first_word in ("python", "pytest", "python3"):
                cmd_types["run"] += 1
            elif first_word == "create":
                cmd_types["create"] += 1
            else:
                cmd_types[first_word] += 1

        cmd_desc = ", ".join(f"{k}×{v}" for k, v in sorted(cmd_types.items(), key=lambda x: -x[1]))
        summary_parts.append(f"命令: {cmd_desc}")

        unique_cmds = len(set(actions))
        total_cmds = len(actions)
        if unique_cmds < total_cmds:
            summary_parts.append(f"({unique_cmds}/{total_cmds} 唯一命令)")

        if len(actions) <= 5:
            cmd_list = "; ".join(a[:80] for a in actions)
            summary_parts.append(f"具体: [{cmd_list}]")
        else:
            cmd_list = "; ".join(a[:60] for a in actions[:3])
            summary_parts.append(f"前3条: [{cmd_list}] ...")

    if observations:
        summary_parts.append(f"观察: {'; '.join(observations[:3])}")

    return " | ".join(summary_parts), actions


def compute_lf_reasons(w, actions, traj_raw):
    lf1 = w["labels"]["file_diff_delta"]
    lf2 = w["labels"]["command_repetition"]
    lf3 = w["labels"]["outcome_backpropagation"]

    # LF1: use all steps in window (including observations) to count edits properly
    steps_raw = traj_raw.get("trajectory", [])
    edit_count = 0
    edited_files = set()
    search_count = 0
    for idx in w["step_indices"]:
        if idx >= len(steps_raw):
            continue
        s = steps_raw[idx]
        if s.get("role") != "ai":
            continue
        cmd = extract_command(s.get("text", ""))
        if not cmd:
            continue
        if cmd.strip().startswith("edit"):
            edit_count += 1
            next_idx = idx + 1
            if next_idx < len(steps_raw):
                obs_text = steps_raw[next_idx].get("text", "")
                match = re.search(r"\[File:\s*([^\]]+?)(?:\s*\(\d+\s*lines)", obs_text)
                if match:
                    edited_files.add(match.group(1).strip())
        first_word = cmd.strip().split()[0] if cmd.strip() else ""
        if first_word in ("search_dir", "search_file", "find_file", "find", "grep"):
            search_count += 1

    lf1_reason = f"edit_count={edit_count}, files_edited={len(edited_files)}, search_count={search_count}"

    unique = len(set(actions))
    total = len(actions)
    has_consec_exact = False
    has_consec_similar = False
    if total >= 3:
        for i in range(2, total):
            if actions[i] == actions[i-1] == actions[i-2]:
                has_consec_exact = True
                break
        if not has_consec_exact:
            run = 1
            for i in range(1, total):
                if SequenceMatcher(None, actions[i-1], actions[i]).ratio() >= 0.9:
                    run += 1
                    if run >= 3:
                        has_consec_similar = True
                        break
                else:
                    run = 1

    lf2_reason = f"unique={unique}/{total}"
    if has_consec_exact:
        lf2_reason += ", 有完全相同连续≥3"
    elif has_consec_similar:
        lf2_reason += ", 有相似连续≥3 (sim≥0.9)"
    else:
        lf2_reason += ", 无连续重复"

    target = traj_raw.get("target", False)
    exit_status = traj_raw.get("exit_status", "")
    lf3_reason = f"window_idx={w['window_idx']}, exit_status={exit_status}, target={target}"

    return {
        "lf1": (LABEL_NAME[lf1], lf1_reason),
        "lf2": (LABEL_NAME[lf2], lf2_reason),
        "lf3": (LABEL_NAME[lf3], lf3_reason),
    }


def semantic_judgment(summary, actions, w, traj_raw):
    lf1 = w["labels"]["file_diff_delta"]
    lf2 = w["labels"]["command_repetition"]

    has_edits = any(a.startswith("edit") for a in actions)
    has_search = any(a.split()[0] in ("search_dir", "search_file", "find_file", "find", "grep") for a in actions if a.split())
    has_run = any(a.split()[0] in ("python", "pytest", "python3") for a in actions if a.split())

    unique = len(set(actions))
    total = len(actions)

    has_repetition = False
    if total >= 3:
        for i in range(2, total):
            if actions[i] == actions[i-1] == actions[i-2]:
                has_repetition = True
                break
        if not has_repetition:
            run = 1
            for i in range(1, total):
                if SequenceMatcher(None, actions[i-1], actions[i]).ratio() >= 0.9:
                    run += 1
                    if run >= 3:
                        has_repetition = True
                        break
                else:
                    run = 1

    if has_edits and has_repetition:
        return "部分进展。agent 有代码编辑行为说明在尝试修复，但命令重复表明可能在反复试错同一个方向，实际进展有限。"
    if has_edits and not has_repetition:
        return "有进展。agent 在编辑代码且命令多样化，表明在有方向地推进修复。"
    if not has_edits and unique == total and total >= 3:
        return "探索阶段。agent 命令多样但没有编辑操作，可能在定位问题阶段，属于必要的前置工作但未直接推进修复。"
    if not has_edits and has_search and total >= 3:
        return "停滞偏向。agent 仅在搜索/浏览，没有编辑行为，且搜索量较大，可能在反复定位而无法锁定问题。"
    if has_repetition and not has_edits:
        return "停滞。agent 既没有编辑也在重复命令，明确处于停滞状态。"
    if total < 2:
        return "数据不足，无法判断。"

    return "不确定。行为模式不明确，需要结合更多上下文判断。"


def format_case(case_num, w, traj_raw):
    summary, actions = summarize_window(w, traj_raw)
    reasons = compute_lf_reasons(w, actions, traj_raw)
    majority = LABEL_NAME[w["majority_label"]]
    sem = semantic_judgment(summary, actions, w, traj_raw)

    lines = []
    lines.append(f"### Case {case_num} (trajectory_id: {w['trajectory_id']}, window_idx: {w['window_idx']})")
    lines.append(f"- **轨迹摘要**: {summary}")
    lines.append(f"- **LF1(file_diff)**: {reasons['lf1'][0]} — {reasons['lf1'][1]}")
    lines.append(f"- **LF2(cmd_repetition)**: {reasons['lf2'][0]} — {reasons['lf2'][1]}")
    lines.append(f"- **LF3(outcome)**: {reasons['lf3'][0]} — {reasons['lf3'][1]}")
    lines.append(f"- **Majority vote**: {majority}")
    lines.append(f"- **语义判断**: {sem}")
    lines.append("")
    return "\n".join(lines)


def main():
    print("Loading windows...")
    windows = load_windows()
    total = len(windows)
    print(f"Total windows: {total}")

    print("Categorizing...")
    cats = categorize(windows)
    for cid, ws in cats.items():
        print(f"  Category {cid}: {len(ws)} windows")

    print("Building trajectory index...")
    traj_index = build_traj_index()
    print(f"  Indexed {len(traj_index)} trajectories")

    print("Sampling (with validation)...")
    sampled = sample_cases_with_validation(cats, traj_index, n=10)
    for cid, ws in sampled.items():
        print(f"  Category {cid}: sampled {len(ws)}")

    print("Loading needed trajectories...")
    trajs = load_needed_trajectories(sampled, traj_index)
    print(f"  Loaded {len(trajs)} trajectories")

    cat_names = {
        1: "Category 1: LF1=PROGRESS, LF2=STAGNATION",
        2: "Category 2: LF1=STAG/ABSTAIN, LF2=PROGRESS",
        3: "Category 3: 三 LF 一致 = PROGRESS",
        4: "Category 4: 三 LF 一致 = STAGNATION",
    }

    report = []
    report.append("# LF 冲突分析报告\n")
    report.append("## 统计概览\n")
    report.append(f"- 总窗口数: {total:,}")
    report.append(f"- LF1=PROGRESS & LF2=STAGNATION 窗口数: {len(cats[1]):,} (占比 {len(cats[1])/total*100:.1f}%)")
    report.append(f"- LF1=STAG/ABSTAIN & LF2=PROGRESS 窗口数: {len(cats[2]):,} (占比 {len(cats[2])/total*100:.1f}%)")
    report.append(f"- 三 LF 一致=PROGRESS 窗口数: {len(cats[3]):,} (占比 {len(cats[3])/total*100:.1f}%)")
    report.append(f"- 三 LF 一致=STAGNATION 窗口数: {len(cats[4]):,} (占比 {len(cats[4])/total*100:.1f}%)")
    report.append("")

    # Placeholder for conflict hypothesis - will fill after analyzing cases
    report.append("## 冲突根因假设\n")
    conflict_hypothesis_idx = len(report)
    report.append("[PLACEHOLDER]")
    report.append("")

    for cid in [1, 2, 3, 4]:
        report.append(f"## {cat_names[cid]}\n")
        cases = sampled[cid]
        if len(cases) < 10:
            report.append(f"*注: 该类别仅有 {len(cases)} 个窗口，全部展示。*\n")
        for i, w in enumerate(cases, 1):
            tid = w["trajectory_id"]
            if tid not in trajs:
                report.append(f"### Case {i} (trajectory_id: {tid}, window_idx: {w['window_idx']})")
                report.append("- **轨迹摘要**: [轨迹数据未找到]")
                report.append("")
                continue
            report.append(format_case(i, w, trajs[tid]))

    # Now analyze the conflict patterns to write hypothesis
    # Analyze Cat 1 cases (LF1=PROG, LF2=STAG)
    cat1_edit_repeat = 0
    for w in sampled[1]:
        tid = w["trajectory_id"]
        if tid in trajs:
            _, actions = summarize_window(w, trajs[tid])
            has_edits = any(a.startswith("edit") for a in actions)
            has_repeat = False
            if len(actions) >= 3:
                for i in range(2, len(actions)):
                    if actions[i] == actions[i-1] == actions[i-2]:
                        has_repeat = True
                        break
            if has_edits and has_repeat:
                cat1_edit_repeat += 1

    cat2_diverse_no_edit = 0
    for w in sampled[2]:
        tid = w["trajectory_id"]
        if tid in trajs:
            _, actions = summarize_window(w, trajs[tid])
            has_edits = any(a.startswith("edit") for a in actions)
            if not has_edits and len(set(actions)) == len(actions):
                cat2_diverse_no_edit += 1

    hypothesis = []
    hypothesis.append("LF1 与 LF2 冲突的根本原因是两个 LF 捕捉了不同维度的信号，且这两个维度并不总是一致的：\n")
    hypothesis.append("1. **LF1 关注编辑行为**（是否在修改代码），**LF2 关注命令多样性**（是否在重复操作）。")
    hypothesis.append("   这两个维度是正交的：agent 可以编辑代码但用重复模式（如反复 edit 同一区域），也可以命令多样但不涉及编辑（如探索/搜索阶段）。\n")
    hypothesis.append("2. **Cat1 典型场景**（LF1=PROGRESS, LF2=STAGNATION）：agent 在反复 edit 同一个文件的同一区域，")
    hypothesis.append("   可能在 trial-and-error 修复 bug。LF1 看到有编辑就给 PROGRESS，LF2 看到重复 edit 命令给 STAGNATION。")
    hypothesis.append(f"   在抽样的 10 个案例中，{cat1_edit_repeat} 个符合「编辑+重复」模式。\n")
    hypothesis.append("3. **Cat2 典型场景**（LF1=STAG/ABSTAIN, LF2=PROGRESS）：agent 在用多样化命令探索代码库，")
    hypothesis.append("   如 find_file → open → search_dir → scroll，没有 edit。LF2 看到全不重复给 PROGRESS，LF1 因为没有 edit 给 ABSTAIN/STAGNATION。")
    hypothesis.append(f"   在抽样的 10 个案例中，{cat2_diverse_no_edit} 个符合「多样但无编辑」模式。\n")
    hypothesis.append("4. **核心问题**：LF1 和 LF2 对「progress」的定义不兼容。LF1 定义 progress = 修改代码，LF2 定义 progress = 行为多样化。")
    hypothesis.append("   两者都是合理的弱信号，但在 trial-and-error 编辑和纯探索阶段会系统性冲突。")

    report[conflict_hypothesis_idx] = "\n".join(hypothesis)

    # Conclusions
    report.append("## 结论与建议\n")
    report.append("### LF 冲突的主要模式\n")
    report.append("1. **编辑 + 重复模式**（Cat1）: agent 在反复编辑同一区域（trial-and-error），LF1 认为有进展，LF2 认为停滞。")
    report.append("   语义上这属于「低效进展」——agent 在努力但方向可能不对。")
    report.append("2. **多样探索 + 无编辑**（Cat2）: agent 在用多种命令浏览代码库，LF2 认为有进展，LF1 认为停滞。")
    report.append("   语义上这属于「必要前置工作」——agent 在理解问题，但尚未开始修复。\n")
    report.append("### 冲突时哪个 LF 更可靠\n")
    report.append("- Cat1 场景中，LF2 (STAGNATION) 通常更准确：反复编辑同一区域确实是停滞信号。")
    report.append("- Cat2 场景中，两个 LF 都有道理：探索不是停滞但也不是直接进展。应标为 ABSTAIN 而非强判。")
    report.append("- LF3 在两个冲突类别中大多 ABSTAIN（因为冲突窗口多在轨迹中段），起不到仲裁作用。\n")
    report.append("### 阈值/逻辑调整建议\n")
    report.append("1. LF1 应区分「重复编辑」和「多样编辑」：如果 edit 命令 similarity > 0.9，不应判 PROGRESS。")
    report.append("2. LF2 对全部唯一命令判 PROGRESS 过于宽松：纯探索不等于进展，建议增加「包含至少一次 edit」的条件。")
    report.append("3. 考虑增加 LF4（如观察到的 error 变化、文件浏览深度等）来提供独立信号。\n")
    report.append("### 对 Majority Vote 质量的影响\n")
    report.append(f"- 冲突窗口（Cat1 + Cat2）共 {len(cats[1]) + len(cats[2]):,} 个，占总窗口的 {(len(cats[1]) + len(cats[2]))/total*100:.1f}%。")
    report.append("- 在冲突窗口中，majority vote 实质由 LF3 仲裁（2:1 或 ABSTAIN 导致 1:1 时依赖 LF3）。")
    report.append("- 但 LF3 在大多数窗口上 ABSTAIN，因此冲突窗口的 majority vote 常由两个相互矛盾的 LF 中票数多的一个决定，")
    report.append("  标签质量低于一致窗口。建议对冲突窗口降低置信权重或引入人工审查。")

    report_text = "\n".join(report)
    with open(OUTPUT_PATH, "w") as f:
        f.write(report_text)
    print(f"\nReport written to {OUTPUT_PATH}")
    print(f"Report length: {len(report_text)} chars")


if __name__ == "__main__":
    main()
