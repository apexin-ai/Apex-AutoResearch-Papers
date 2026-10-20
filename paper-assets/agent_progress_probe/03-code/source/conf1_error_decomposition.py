#!/usr/bin/env python3
"""D073-A1: Conf=1 Gold Error Decomposition — GB vs MV."""

import csv
import json
import re
from collections import Counter
from difflib import SequenceMatcher
from pathlib import Path

import numpy as np
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import f1_score, accuracy_score, confusion_matrix

BASE = Path(__file__).parent
DATA_DIR = BASE / "artifacts" / "data"
GOLD_DIR = BASE / "artifacts" / "gold_set"

EDIT_CMDS = {"edit", "str_replace", "create", "insert"}
SEARCH_CMDS = {"search_dir", "search_file", "find_file", "find", "grep", "view"}
NAV_CMDS = {"open", "goto", "scroll_down", "scroll_up", "cd", "ls", "cat"}


def extract_command(text):
    m = re.search(r"```\n?(.*?)```", text, re.DOTALL)
    return m.group(1).strip() if m else None


def cmd_similarity(a, b):
    if a == b:
        return 1.0
    if not a or not b:
        return 0.0
    return SequenceMatcher(None, a, b).ratio()


def extract_features(steps, is_short):
    n = len(steps)
    if n == 0:
        return np.zeros(30, dtype=np.float32)
    texts = [s["text"] for s in steps]
    text_lens = [len(t) for t in texts]
    actions = [(s, t) for s, t in zip(steps, texts) if s["role"] == "ai"]
    observations = [(s, t) for s, t in zip(steps, texts) if s["role"] == "user"]
    n_actions = len(actions)
    n_obs = len(observations)
    mean_tlen = np.mean(text_lens)
    std_tlen = np.std(text_lens) if n > 1 else 0.0
    max_tlen = max(text_lens)
    min_tlen = min(text_lens)
    action_lens = [len(t) for _, t in actions] if actions else [0]
    obs_lens = [len(t) for _, t in observations] if observations else [0]
    mean_action_len = np.mean(action_lens)
    mean_obs_len = np.mean(obs_lens)
    if n > 1:
        x = np.arange(n, dtype=float)
        y = np.array(text_lens, dtype=float)
        slope = (n * np.dot(x, y) - x.sum() * y.sum()) / (n * np.dot(x, x) - x.sum() ** 2 + 1e-9)
    else:
        slope = 0.0
    commands = []
    for _, t in actions:
        cmd = extract_command(t)
        if cmd:
            commands.append(cmd)
    n_cmds = len(commands)
    cmd_lens = [len(c) for c in commands] if commands else [0]
    mean_cmd_len = np.mean(cmd_lens)
    max_cmd_len = max(cmd_lens) if cmd_lens else 0
    if n_cmds > 0:
        unique_cmds = len(set(commands))
        unique_cmd_ratio = unique_cmds / n_cmds
        cmd_counter = Counter(commands)
        repeat_ratio = cmd_counter.most_common(1)[0][1] / n_cmds
    else:
        unique_cmd_ratio = 1.0
        repeat_ratio = 0.0
    n_edit = n_search = n_nav = n_submit = 0
    for cmd in commands:
        fw = cmd.strip().split()[0] if cmd.strip() else ""
        if fw in EDIT_CMDS:
            n_edit += 1
        elif fw in SEARCH_CMDS:
            n_search += 1
        elif fw in NAV_CMDS:
            n_nav += 1
        elif fw == "submit":
            n_submit += 1
    edit_ratio = n_edit / max(n_cmds, 1)
    search_ratio = n_search / max(n_cmds, 1)
    if n_cmds >= 2:
        sims = [cmd_similarity(commands[i], commands[i + 1]) for i in range(n_cmds - 1)]
        avg_adj_sim = np.mean(sims)
        max_adj_sim = max(sims)
        max_run = 1
        cur_run = 1
        for s in sims:
            if s >= 0.9:
                cur_run += 1
                max_run = max(max_run, cur_run)
            else:
                cur_run = 1
    else:
        avg_adj_sim = 0.0
        max_adj_sim = 0.0
        max_run = 0
    n_errors = sum(1 for t in texts if "Traceback" in t or "Error" in t)
    n_test_output = sum(1 for t in texts if ("PASSED" in t or "FAILED" in t) and "test" in t.lower())
    n_file_display = sum(1 for t in texts if "[File:" in t)
    n_nonzero_exit = sum(
        1 for _, t in observations if re.search(r"exit code [1-9]|returned non-zero|command not found", t)
    )
    return np.array([
        n, n_actions, n_obs, n_actions / max(n, 1),
        mean_tlen, std_tlen, max_tlen, min_tlen,
        mean_action_len, mean_obs_len, slope,
        n_cmds, mean_cmd_len, max_cmd_len,
        unique_cmd_ratio, repeat_ratio,
        n_edit, n_search, n_nav, n_submit,
        edit_ratio, search_ratio,
        avg_adj_sim, max_adj_sim, max_run,
        n_errors, n_test_output, n_file_display, n_nonzero_exit,
        float(is_short),
    ], dtype=np.float32)


def window_id(w):
    return f"{w['trajectory_id']}__w{w['window_idx']}"


def main():
    # 1. Gold Set B
    gold_wids, gold_labels = [], []
    with open(GOLD_DIR / "gold_2plus_agreed_B.csv") as f:
        for row in csv.DictReader(f):
            gold_wids.append(row["window_id"])
            gold_labels.append(int(row["gold_label"]))
    gold_map = dict(zip(gold_wids, gold_labels))
    print(f"Gold Set B: N={len(gold_wids)}")

    # 2. Silver conf from annotation CSVs
    wid_to_silver_conf = {}
    for fname in ["annotation_unknown_2026-05-15.csv", "annotation_unknown_2026-05-15_batch2.csv",
                   "annotation_unknown_2026-05-15_batch3a.csv", "annotation_unknown_2026-05-15_batch3b.csv"]:
        p = GOLD_DIR / fname
        if not p.exists():
            continue
        with open(p) as f:
            for r in csv.DictReader(f):
                wid_to_silver_conf[f"{r['trajectory_id']}__w{r['window_idx']}"] = int(r['confidence'])

    # 3. Load windows
    print("Loading windows_labeled.jsonl ...")
    all_windows = []
    with open(DATA_DIR / "windows_labeled.jsonl") as f:
        for line in f:
            if line.strip():
                all_windows.append(json.loads(line))
    non_abstain = [w for w in all_windows if w.get("majority_label", -1) != -1]
    wid_to_mv = {window_id(w): w["majority_label"] for w in non_abstain}
    wid_to_noabs_idx = {window_id(w): i for i, w in enumerate(non_abstain)}

    # 4. Build trajectory index & features
    print("Building trajectory index ...")
    traj_index = {}
    with open(DATA_DIR / "swe_agent_trajectories_5000.jsonl") as f:
        for line in f:
            raw = json.loads(line.strip())
            steps = [{"role": s.get("role", "unknown"), "text": s.get("text") or s.get("system_prompt") or ""}
                     for s in (raw.get("trajectory") or [])]
            traj_index[len(traj_index)] = steps
    print(f"  {len(traj_index)} trajectories")

    print("Extracting features ...")
    all_features = np.zeros((len(non_abstain), 30), dtype=np.float32)
    all_mv_labels = np.zeros(len(non_abstain), dtype=int)
    for i, w in enumerate(non_abstain):
        row_idx = w.get("row_index", 0)
        traj_steps = traj_index.get(row_idx, [])
        window_steps = [traj_steps[si] if si < len(traj_steps) else {"role": "unknown", "text": ""}
                        for si in w["step_indices"]]
        all_features[i] = extract_features(window_steps, w.get("short_trajectory", False))
        all_mv_labels[i] = w["majority_label"]

    # 5. Train GB on conf>=2 SWE, excluding gold
    gold_set = set(gold_wids)
    conf2_mask = np.array([w.get("confidence", 0) >= 2 for w in non_abstain])
    not_gold_mask = np.array([window_id(w) not in gold_set for w in non_abstain])
    train_mask = conf2_mask & not_gold_mask
    X_train = all_features[train_mask]
    y_train = all_mv_labels[train_mask]
    print(f"  GB train: {len(X_train)} (conf>=2, gold excluded)")

    gb = GradientBoostingClassifier(n_estimators=200, learning_rate=0.05, max_depth=5, random_state=42)
    gb.fit(X_train, y_train)

    # 6. Conf=1 windows: get GB preds and MV labels
    conf1_wids = [wid for wid in gold_wids if wid_to_silver_conf.get(wid) == 1]
    print(f"\nConf=1 gold windows: {len(conf1_wids)}")

    # Filter to those with both GB predictions (SWE features) and MV labels
    eval_data = []
    for wid in conf1_wids:
        idx = wid_to_noabs_idx.get(wid)
        mv = wid_to_mv.get(wid)
        gl = gold_map[wid]
        if idx is not None and mv is not None and mv != -1:
            gb_pred = gb.predict(all_features[idx:idx+1])[0]
            eval_data.append({
                "window_id": wid,
                "gold_label": gl,
                "gb_pred": int(gb_pred),
                "mv_label": int(mv),
            })

    n_eval = len(eval_data)
    print(f"Conf=1 with GB+MV+gold: {n_eval}")

    # 7. Build confusion matrix
    gb_correct = [d["gb_pred"] == d["gold_label"] for d in eval_data]
    mv_correct = [d["mv_label"] == d["gold_label"] for d in eval_data]

    both_correct = sum(g and m for g, m in zip(gb_correct, mv_correct))
    gb_right_mv_wrong = sum(g and not m for g, m in zip(gb_correct, mv_correct))
    gb_wrong_mv_right = sum(not g and m for g, m in zip(gb_correct, mv_correct))
    both_wrong = sum(not g and not m for g, m in zip(gb_correct, mv_correct))

    assert both_correct + gb_right_mv_wrong + gb_wrong_mv_right + both_wrong == n_eval

    # 8. Per-class breakdown
    by_class = {}
    for cls_name, cls_val in [("stagnation", 0), ("progress", 1)]:
        cls_data = [d for d in eval_data if d["gold_label"] == cls_val]
        gb_c = [d["gb_pred"] == d["gold_label"] for d in cls_data]
        mv_c = [d["mv_label"] == d["gold_label"] for d in cls_data]
        by_class[cls_name] = {
            "n": len(cls_data),
            "gb_correct_mv_wrong": sum(g and not m for g, m in zip(gb_c, mv_c)),
            "gb_wrong_mv_correct": sum(not g and m for g, m in zip(gb_c, mv_c)),
            "both_correct": sum(g and m for g, m in zip(gb_c, mv_c)),
            "both_wrong": sum(not g and not m for g, m in zip(gb_c, mv_c)),
        }

    # 9. Verify GB F1 on conf=1
    gb_golds = [d["gold_label"] for d in eval_data]
    gb_preds = [d["gb_pred"] for d in eval_data]
    mv_labels = [d["mv_label"] for d in eval_data]
    gb_f1 = f1_score(gb_golds, gb_preds, average="macro")
    gb_acc = accuracy_score(gb_golds, gb_preds)
    mv_agree = sum(m == g for m, g in zip(mv_labels, gb_golds))
    mv_rate = mv_agree / n_eval

    print(f"\n--- Verification ---")
    print(f"GB F1 (conf=1): {gb_f1:.4f} (expected ~0.784)")
    print(f"GB accuracy: {gb_acc:.4f}")
    print(f"MV-gold agreement: {mv_agree}/{n_eval} = {mv_rate:.4f} (expected ~0.738)")

    # Per-class F1
    gb_f1_stag = f1_score(gb_golds, gb_preds, average="binary", pos_label=0)
    gb_f1_prog = f1_score(gb_golds, gb_preds, average="binary", pos_label=1)
    print(f"GB F1 stagnation: {gb_f1_stag:.4f}")
    print(f"GB F1 progress: {gb_f1_prog:.4f}")

    # 10. Print confusion matrix
    print(f"\n--- GB vs MV Confusion (conf=1, N={n_eval}) ---")
    print(f"  Both correct:        {both_correct:>4} ({both_correct/n_eval:.1%})")
    print(f"  GB correct, MV wrong:{gb_right_mv_wrong:>4} ({gb_right_mv_wrong/n_eval:.1%})")
    print(f"  GB wrong, MV correct:{gb_wrong_mv_right:>4} ({gb_wrong_mv_right/n_eval:.1%})")
    print(f"  Both wrong:          {both_wrong:>4} ({both_wrong/n_eval:.1%})")

    for cls_name in ["progress", "stagnation"]:
        c = by_class[cls_name]
        print(f"\n  {cls_name.upper()} (n={c['n']}):")
        print(f"    Both correct:         {c['both_correct']:>3}")
        print(f"    GB correct, MV wrong: {c['gb_correct_mv_wrong']:>3}")
        print(f"    GB wrong, MV correct: {c['gb_wrong_mv_correct']:>3}")
        print(f"    Both wrong:           {c['both_wrong']:>3}")

    # 11. Interpretation
    gb_advantage = gb_right_mv_wrong - gb_wrong_mv_right
    if gb_advantage > 0:
        interp = (
            f"GB corrects {gb_right_mv_wrong} MV errors while introducing {gb_wrong_mv_right} new errors "
            f"(net advantage: +{gb_advantage} windows). "
            f"On conf=1 (LF-disagreement) windows, GB learns patterns beyond simple LF voting."
        )
    elif gb_advantage < 0:
        interp = (
            f"MV corrects {gb_wrong_mv_right} GB errors while GB corrects {gb_right_mv_wrong} MV errors "
            f"(net MV advantage: {-gb_advantage} windows). "
            f"On conf=1 windows, MV is more reliable than GB."
        )
    else:
        interp = (
            f"GB and MV correct the same number of each other's errors ({gb_right_mv_wrong} each). "
            f"Neither method has a clear advantage on conf=1 windows."
        )

    # 12. Save output
    output = {
        "task": "D073-A1",
        "description": "Conf=1 Gold Error Decomposition: GB vs MV",
        "n_conf1_total": len(conf1_wids),
        "n_conf1_with_gold_and_features": n_eval,
        "n_conf1_oh_excluded": len(conf1_wids) - n_eval,
        "gb_f1_conf1": round(gb_f1, 4),
        "gb_accuracy_conf1": round(gb_acc, 4),
        "gb_f1_stagnation": round(gb_f1_stag, 4),
        "gb_f1_progress": round(gb_f1_prog, 4),
        "mv_gold_agreement": round(mv_rate, 4),
        "confusion_matrix": {
            "gb_correct_mv_wrong": gb_right_mv_wrong,
            "gb_wrong_mv_correct": gb_wrong_mv_right,
            "both_correct": both_correct,
            "both_wrong": both_wrong,
        },
        "by_class": by_class,
        "interpretation": interp,
        "per_window": eval_data,
    }
    out_path = BASE / "artifacts" / "d073" / "conf1_error_decomposition.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nSaved: {out_path}")


if __name__ == "__main__":
    main()
