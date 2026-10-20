#!/usr/bin/env python3
"""Non-NLP baseline: structural/numerical features only.

Extracts hand-crafted features from raw trajectory steps (no embeddings),
trains LogisticRegression, RandomForest, GradientBoosting.
Uses the same train/val/test split as probe_001.
"""

import json
import re
import sys
import argparse
from collections import Counter
from difflib import SequenceMatcher
from pathlib import Path

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score


def compute_metrics(labels, preds):
    return {
        "macro_f1": f1_score(labels, preds, average="macro", zero_division=0),
        "accuracy": accuracy_score(labels, preds),
        "precision_macro": precision_score(labels, preds, average="macro", zero_division=0),
        "recall_macro": recall_score(labels, preds, average="macro", zero_division=0),
        "f1_stagnation": f1_score(labels, preds, pos_label=0, zero_division=0),
        "f1_progress": f1_score(labels, preds, pos_label=1, zero_division=0),
    }


def extract_command(text):
    match = re.search(r"```\n?(.*?)```", text, re.DOTALL)
    return match.group(1).strip() if match else None


EDIT_CMDS = {"edit", "str_replace", "create", "insert"}
SEARCH_CMDS = {"search_dir", "search_file", "find_file", "find", "grep", "view"}
NAV_CMDS = {"open", "goto", "scroll_down", "scroll_up", "cd", "ls", "cat"}


def cmd_similarity(a, b):
    if a == b:
        return 1.0
    if not a or not b:
        return 0.0
    return SequenceMatcher(None, a, b).ratio()


def extract_features(steps, is_short):
    """Extract structural features from a list of step dicts.

    Each step dict has: role, text
    """
    n = len(steps)
    if n == 0:
        return np.zeros(30)

    roles = [s["role"] for s in steps]
    texts = [s["text"] for s in steps]
    text_lens = [len(t) for t in texts]

    actions = [(s, t) for s, t in zip(steps, texts) if s["role"] == "ai"]
    observations = [(s, t) for s, t in zip(steps, texts) if s["role"] == "user"]

    n_actions = len(actions)
    n_obs = len(observations)

    # --- text length features ---
    mean_tlen = np.mean(text_lens)
    std_tlen = np.std(text_lens) if n > 1 else 0.0
    max_tlen = max(text_lens)
    min_tlen = min(text_lens)

    action_lens = [len(t) for _, t in actions] if actions else [0]
    obs_lens = [len(t) for _, t in observations] if observations else [0]
    mean_action_len = np.mean(action_lens)
    mean_obs_len = np.mean(obs_lens)

    # text length trend (slope via simple linear regression)
    if n > 1:
        x = np.arange(n, dtype=float)
        y = np.array(text_lens, dtype=float)
        slope = (n * np.dot(x, y) - x.sum() * y.sum()) / (n * np.dot(x, x) - x.sum()**2 + 1e-9)
    else:
        slope = 0.0

    # --- command features ---
    commands = []
    for s, t in actions:
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
        max_repeat = cmd_counter.most_common(1)[0][1]
        repeat_ratio = max_repeat / n_cmds
    else:
        unique_cmd_ratio = 1.0
        repeat_ratio = 0.0

    # command type counts
    n_edit = 0
    n_search = 0
    n_nav = 0
    n_submit = 0
    for cmd in commands:
        first_word = cmd.strip().split()[0] if cmd.strip() else ""
        if first_word in EDIT_CMDS:
            n_edit += 1
        elif first_word in SEARCH_CMDS:
            n_search += 1
        elif first_word in NAV_CMDS:
            n_nav += 1
        elif first_word == "submit":
            n_submit += 1

    edit_ratio = n_edit / max(n_cmds, 1)
    search_ratio = n_search / max(n_cmds, 1)

    # adjacent command similarity
    if n_cmds >= 2:
        sims = [cmd_similarity(commands[i], commands[i+1]) for i in range(n_cmds - 1)]
        avg_adj_sim = np.mean(sims)
        max_adj_sim = max(sims)
        # max consecutive run with sim >= 0.9
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

    # --- content pattern features ---
    n_errors = sum(1 for t in texts if "Traceback" in t or "Error" in t)
    n_test_output = sum(1 for t in texts if ("PASSED" in t or "FAILED" in t) and "test" in t.lower())
    n_file_display = sum(1 for t in texts if "[File:" in t)

    # exit code patterns in observations (look for "exit code" or "$?" patterns)
    n_nonzero_exit = sum(1 for _, t in observations if re.search(r"exit code [1-9]|returned non-zero|command not found", t))

    feature_vec = np.array([
        n,                    # 0: num_steps
        n_actions,            # 1: num_actions
        n_obs,                # 2: num_observations
        n_actions / max(n, 1),# 3: action_ratio
        mean_tlen,            # 4: mean_text_len
        std_tlen,             # 5: std_text_len
        max_tlen,             # 6: max_text_len
        min_tlen,             # 7: min_text_len
        mean_action_len,      # 8: mean_action_len
        mean_obs_len,         # 9: mean_obs_len
        slope,                # 10: text_len_trend
        n_cmds,               # 11: num_commands
        mean_cmd_len,         # 12: mean_cmd_len
        max_cmd_len,          # 13: max_cmd_len
        unique_cmd_ratio,     # 14: unique_cmd_ratio
        repeat_ratio,         # 15: max_repeat_ratio
        n_edit,               # 16: num_edit_cmds
        n_search,             # 17: num_search_cmds
        n_nav,                # 18: num_nav_cmds
        n_submit,             # 19: num_submit_cmds
        edit_ratio,           # 20: edit_ratio
        search_ratio,         # 21: search_ratio
        avg_adj_sim,          # 22: avg_adjacent_cmd_similarity
        max_adj_sim,          # 23: max_adjacent_cmd_similarity
        max_run,              # 24: max_consecutive_similar_cmds
        n_errors,             # 25: num_errors
        n_test_output,        # 26: num_test_outputs
        n_file_display,       # 27: num_file_displays
        n_nonzero_exit,       # 28: num_nonzero_exits
        float(is_short),      # 29: is_short_trajectory
    ], dtype=np.float32)

    return feature_vec


FEATURE_NAMES = [
    "num_steps", "num_actions", "num_observations", "action_ratio",
    "mean_text_len", "std_text_len", "max_text_len", "min_text_len",
    "mean_action_len", "mean_obs_len", "text_len_trend",
    "num_commands", "mean_cmd_len", "max_cmd_len",
    "unique_cmd_ratio", "max_repeat_ratio",
    "num_edit_cmds", "num_search_cmds", "num_nav_cmds", "num_submit_cmds",
    "edit_ratio", "search_ratio",
    "avg_adjacent_cmd_sim", "max_adjacent_cmd_sim", "max_consecutive_similar",
    "num_errors", "num_test_outputs", "num_file_displays", "num_nonzero_exits",
    "is_short_trajectory",
]


def build_trajectory_index(traj_path):
    """row_index -> list of step dicts [{role, text}, ...]"""
    index = {}
    with open(traj_path) as f:
        for row_idx, line in enumerate(f):
            line = line.strip()
            if not line:
                continue
            raw = json.loads(line)
            steps = []
            for s in raw.get("trajectory") or []:
                steps.append({
                    "role": s.get("role", "unknown"),
                    "text": s.get("text") or s.get("system_prompt") or "",
                })
            index[row_idx] = steps
    return index


def load_windows(path):
    windows = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                windows.append(json.loads(line))
    return windows


def print_table(results):
    header = "| Method                      | Macro-F1 | Accuracy | F1(stag) | F1(prog) |"
    sep = "|" + "|".join(["-" * 30] + ["-" * 10] * 4) + "|"
    print(header)
    print(sep)
    for name, m in results:
        row = f"| {name:28s} |"
        for key in ["macro_f1", "accuracy", "f1_stagnation", "f1_progress"]:
            v = m.get(key)
            if v is None:
                row += "    —     |"
            else:
                row += f" {v:.4f}   |"
        print(row)


def main():
    parser = argparse.ArgumentParser(description="Non-NLP structural baseline")
    parser.add_argument("--data_dir", required=True)
    parser.add_argument("--split_info", required=True)
    parser.add_argument("--trajectories", required=True)
    args = parser.parse_args()

    data_dir = Path(args.data_dir)

    # Load split info
    with open(args.split_info) as f:
        split_info = json.load(f)

    # Build trajectory index
    print("Building trajectory index ...")
    traj_index = build_trajectory_index(args.trajectories)
    print(f"Indexed {len(traj_index)} trajectories")

    # Load windows
    print("Loading windows ...")
    all_windows = load_windows(data_dir / "windows_labeled.jsonl")
    print(f"Total windows: {len(all_windows)}")

    # Step 1: filter out ABSTAIN (mirrors generate_embeddings.py)
    non_abstain = [w for w in all_windows if w.get("majority_label", -1) != -1]
    print(f"Non-abstain: {len(non_abstain)}")

    # Step 2: apply keep_indices (confidence filter, indexes into non_abstain array)
    keep_indices = split_info.get("keep_indices")
    if keep_indices is not None:
        min_conf = split_info.get("min_confidence", 0)
        print(f"Confidence filter (min_confidence={min_conf}): {len(keep_indices)}/{len(non_abstain)}")
        windows = [non_abstain[i] for i in keep_indices]
    else:
        windows = non_abstain

    print(f"Usable windows: {len(windows)}")

    # Extract features for all usable windows
    print("Extracting features ...")
    features = []
    labels = []
    n_missing = 0
    for w in windows:
        row_idx = w.get("row_index", 0)
        step_indices = w["step_indices"]
        traj_steps = traj_index.get(row_idx, [])

        window_steps = []
        for si in step_indices:
            if si < len(traj_steps):
                window_steps.append(traj_steps[si])
            else:
                window_steps.append({"role": "unknown", "text": ""})
                n_missing += 1

        feat = extract_features(window_steps, w.get("short_trajectory", False))
        features.append(feat)
        labels.append(w["majority_label"])

    X = np.stack(features)
    y = np.array(labels)
    print(f"Feature matrix: {X.shape}, missing steps: {n_missing}")

    # Split
    train_idx = split_info["train_indices"]
    val_idx = split_info["val_indices"]
    test_idx = split_info["test_indices"]
    print(f"Split — train: {len(train_idx)}, val: {len(val_idx)}, test: {len(test_idx)}")

    X_train, y_train = X[train_idx], y[train_idx]
    X_val, y_val = X[val_idx], y[val_idx]
    X_test, y_test = X[test_idx], y[test_idx]

    print(f"Train label dist: stag={sum(y_train==0)}, prog={sum(y_train==1)}")
    print(f"Test label dist:  stag={sum(y_test==0)}, prog={sum(y_test==1)}")
    print()

    # Standardize
    scaler = StandardScaler()
    X_train_s = scaler.fit_transform(X_train)
    X_val_s = scaler.transform(X_val)
    X_test_s = scaler.transform(X_test)

    results = []
    results.append(("GRU Probe (ref)", {"macro_f1": 0.9055}))
    results.append(("MeanPool+LR (ref)", {"macro_f1": 0.8435}))

    # --- LogisticRegression ---
    print("=== Logistic Regression (C tuning) ===")
    best_c, best_val_f1 = None, -1
    for c in [0.001, 0.01, 0.1, 1.0, 10.0, 100.0]:
        lr = LogisticRegression(max_iter=2000, C=c, solver="lbfgs")
        lr.fit(X_train_s, y_train)
        val_preds = lr.predict(X_val_s)
        m = compute_metrics(y_val.tolist(), val_preds.tolist())
        print(f"  C={c:7.3f} → val Macro-F1={m['macro_f1']:.4f}")
        if m["macro_f1"] > best_val_f1:
            best_val_f1 = m["macro_f1"]
            best_c = c

    print(f"  Best C={best_c}")
    lr_final = LogisticRegression(max_iter=2000, C=best_c, solver="lbfgs")
    lr_final.fit(X_train_s, y_train)
    test_preds_lr = lr_final.predict(X_test_s)
    m_lr = compute_metrics(y_test.tolist(), test_preds_lr.tolist())
    results.append(("Struct + LR", m_lr))
    print(f"  Test: {m_lr}")

    # Feature importance (LR coefficients)
    print("\n  Top features (LR coef magnitude):")
    coefs = np.abs(lr_final.coef_[0])
    top_idx = np.argsort(coefs)[::-1][:10]
    for i in top_idx:
        print(f"    {FEATURE_NAMES[i]:30s} = {lr_final.coef_[0][i]:+.4f}")
    print()

    # --- RandomForest ---
    print("=== Random Forest (n_estimators tuning) ===")
    best_n, best_val_f1_rf = None, -1
    for n in [50, 100, 200, 500]:
        rf = RandomForestClassifier(n_estimators=n, max_depth=10, random_state=42, n_jobs=-1)
        rf.fit(X_train, y_train)
        val_preds = rf.predict(X_val)
        m = compute_metrics(y_val.tolist(), val_preds.tolist())
        print(f"  n={n:4d} → val Macro-F1={m['macro_f1']:.4f}")
        if m["macro_f1"] > best_val_f1_rf:
            best_val_f1_rf = m["macro_f1"]
            best_n = n

    print(f"  Best n_estimators={best_n}")
    rf_final = RandomForestClassifier(n_estimators=best_n, max_depth=10, random_state=42, n_jobs=-1)
    rf_final.fit(X_train, y_train)
    test_preds_rf = rf_final.predict(X_test)
    m_rf = compute_metrics(y_test.tolist(), test_preds_rf.tolist())
    results.append(("Struct + RF", m_rf))
    print(f"  Test: {m_rf}")

    print("\n  Top features (RF importance):")
    imp = rf_final.feature_importances_
    top_idx = np.argsort(imp)[::-1][:10]
    for i in top_idx:
        print(f"    {FEATURE_NAMES[i]:30s} = {imp[i]:.4f}")
    print()

    # --- GradientBoosting ---
    print("=== Gradient Boosting ===")
    best_lr_gb, best_val_f1_gb = None, -1
    for lr_val in [0.01, 0.05, 0.1, 0.2]:
        gb = GradientBoostingClassifier(
            n_estimators=200, learning_rate=lr_val, max_depth=5, random_state=42
        )
        gb.fit(X_train, y_train)
        val_preds = gb.predict(X_val)
        m = compute_metrics(y_val.tolist(), val_preds.tolist())
        print(f"  lr={lr_val:.2f} → val Macro-F1={m['macro_f1']:.4f}")
        if m["macro_f1"] > best_val_f1_gb:
            best_val_f1_gb = m["macro_f1"]
            best_lr_gb = lr_val

    print(f"  Best lr={best_lr_gb}")
    gb_final = GradientBoostingClassifier(
        n_estimators=200, learning_rate=best_lr_gb, max_depth=5, random_state=42
    )
    gb_final.fit(X_train, y_train)
    test_preds_gb = gb_final.predict(X_test)
    m_gb = compute_metrics(y_test.tolist(), test_preds_gb.tolist())
    results.append(("Struct + GB", m_gb))
    print(f"  Test: {m_gb}")
    print()

    # --- Summary ---
    print("=" * 80)
    print("RESULTS SUMMARY")
    print("=" * 80)
    print_table(results)

    # Best non-NLP
    best_name = max(results[2:], key=lambda x: x[1].get("macro_f1", 0))
    print(f"\nBest structural baseline: {best_name[0]} (Macro-F1={best_name[1]['macro_f1']:.4f})")
    print(f"vs GRU Probe:      {0.9055 - best_name[1]['macro_f1']:+.4f}")
    print(f"vs MeanPool+LR:    {0.8435 - best_name[1]['macro_f1']:+.4f}")

    # Save results
    output = {
        "Struct + LR": {f"test_{k}": round(v, 4) for k, v in m_lr.items()},
        "Struct + RF": {f"test_{k}": round(v, 4) for k, v in m_rf.items()},
        "Struct + GB": {f"test_{k}": round(v, 4) for k, v in m_gb.items()},
        "best_model": best_name[0],
        "best_macro_f1": round(best_name[1]["macro_f1"], 4),
        "probe_ref_macro_f1": 0.9055,
        "meanpool_lr_ref_macro_f1": 0.8435,
        "num_features": len(FEATURE_NAMES),
        "feature_names": FEATURE_NAMES,
        "hyperparams": {
            "LR_best_C": best_c,
            "RF_best_n_estimators": best_n,
            "GB_best_lr": best_lr_gb,
        },
    }
    out_path = data_dir / "non_nlp_baseline_results.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nResults saved to {out_path}")


if __name__ == "__main__":
    main()
