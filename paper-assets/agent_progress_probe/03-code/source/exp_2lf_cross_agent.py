#!/usr/bin/env python3
"""E1: 2-LF (file_diff + cmd_rep) Cross-Agent Transfer

Train GB/RF on SWE 2-LF silver labels (drop outcome_backpropagation),
evaluate cross-agent transfer to OpenHands.
"""

import json
import re
from collections import Counter
from difflib import SequenceMatcher
from pathlib import Path

import numpy as np
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split

PROJECT = Path("/root/autodl-tmp/agent_progress_probe")
OH_DIR = Path("/root/autodl-tmp/openhands_data")

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
        return np.zeros(30)
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
        1 for _, t in observations
        if re.search(r"exit code [1-9]|returned non-zero|command not found", t)
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


def build_trajectory_index(path):
    """row_index -> list of step dicts [{role, text}, ...]"""
    index = {}
    with open(path) as f:
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


def extract_features_batch(windows, traj_index):
    X = np.zeros((len(windows), 30), dtype=np.float32)
    y = np.zeros(len(windows), dtype=int)
    missing = 0
    for i, w in enumerate(windows):
        row_idx = w.get("row_index", -1)
        traj_steps = traj_index.get(row_idx)
        if traj_steps is None:
            missing += 1
            continue
        si = w["step_indices"]
        steps = [traj_steps[j] for j in si if j < len(traj_steps)]
        X[i] = extract_features(steps, w.get("short_trajectory", False))
        y[i] = w["majority_label"]
    if missing > 0:
        print(f"  WARNING: {missing}/{len(windows)} windows had missing trajectories")
    return X, y


def recompute_2lf(window):
    """Recompute MV using only file_diff_delta and command_repetition.

    conf=2: both LFs voted and agree
    conf=1: exactly one LF voted
    conf=0: both abstained or disagreed (no usable label)
    """
    labels = window.get("labels", {})
    fd = labels.get("file_diff_delta", -1)
    cr = labels.get("command_repetition", -1)

    votes = [v for v in [fd, cr] if v != -1]

    if len(votes) == 0:
        return -1, 0
    elif len(votes) == 1:
        return votes[0], 1
    else:
        if fd == cr:
            return fd, 2
        else:
            return -1, 0


def main():
    print("=" * 70)
    print("E1: 2-LF (file_diff + cmd_rep) Cross-Agent Transfer")
    print("=" * 70)

    # ============================================================
    # 1. Load SWE data and recompute 2-LF labels
    # ============================================================
    print("\n--- Loading SWE windows ---")
    swe_windows = []
    with open(PROJECT / "data" / "windows_labeled.jsonl") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            w = json.loads(line)
            if "openhands" not in w["trajectory_id"]:
                swe_windows.append(w)
    print(f"Total SWE windows (excl. openhands): {len(swe_windows)}")

    non_abstain_3lf = [w for w in swe_windows if w.get("majority_label", -1) != -1]
    conf2_3lf = [w for w in non_abstain_3lf if w.get("confidence", 0) >= 2]
    conf3_3lf = [w for w in non_abstain_3lf if w.get("confidence", 0) >= 3]
    print(f"3-LF non-abstain: {len(non_abstain_3lf)}")
    print(f"3-LF conf>=2: {len(conf2_3lf)}")
    print(f"3-LF conf=3:  {len(conf3_3lf)}")

    for w in swe_windows:
        mv_2lf, conf_2lf = recompute_2lf(w)
        w["mv_2lf"] = mv_2lf
        w["conf_2lf"] = conf_2lf

    conf2_2lf = [w for w in swe_windows if w["conf_2lf"] >= 2 and w["mv_2lf"] != -1]
    conf1_2lf = [w for w in swe_windows if w["conf_2lf"] == 1]
    non_abstain_2lf = [w for w in swe_windows if w["mv_2lf"] != -1]

    n_conflicts = sum(
        1 for w in swe_windows
        if w.get("labels", {}).get("file_diff_delta", -1) != -1
        and w.get("labels", {}).get("command_repetition", -1) != -1
        and w.get("labels", {}).get("file_diff_delta", -1)
        != w.get("labels", {}).get("command_repetition", -1)
    )
    n_both_abstain = len(swe_windows) - len(conf2_2lf) - len(conf1_2lf) - n_conflicts

    stag_2lf = sum(1 for w in conf2_2lf if w["mv_2lf"] == 0)
    prog_2lf = sum(1 for w in conf2_2lf if w["mv_2lf"] == 1)

    print(f"\n2-LF label statistics:")
    print(f"  conf=2 (both agree):  {len(conf2_2lf)}")
    print(f"  conf=1 (one voted):   {len(conf1_2lf)}")
    print(f"  conflicts (disagree): {n_conflicts}")
    print(f"  both abstain:         {n_both_abstain}")
    print(f"  conf>=2 dist: stag={stag_2lf} ({stag_2lf / len(conf2_2lf) * 100:.1f}%), "
          f"prog={prog_2lf} ({prog_2lf / len(conf2_2lf) * 100:.1f}%)")

    # ============================================================
    # 2. Label agreement analysis (2-LF vs 3-LF)
    # ============================================================
    print("\n--- 2-LF vs 3-LF Label Agreement ---")

    overlap = [w for w in swe_windows
               if w.get("majority_label", -1) != -1 and w["mv_2lf"] != -1]
    agree = sum(1 for w in overlap if w["majority_label"] == w["mv_2lf"])
    print(f"Overlap (both non-abstain): {len(overlap)}")
    print(f"Agreement: {agree}/{len(overlap)} = {agree / len(overlap) * 100:.2f}%")

    for c in [1, 2, 3]:
        sub = [w for w in overlap if w.get("confidence", 0) == c]
        if sub:
            ag = sum(1 for w in sub if w["majority_label"] == w["mv_2lf"])
            print(f"  3-LF conf={c}: {ag}/{len(sub)} = {ag / len(sub) * 100:.2f}%")

    for c in [1, 2]:
        sub = [w for w in overlap if w["conf_2lf"] == c]
        if sub:
            ag = sum(1 for w in sub if w["majority_label"] == w["mv_2lf"])
            print(f"  2-LF conf={c}: {ag}/{len(sub)} = {ag / len(sub) * 100:.2f}%")

    # ============================================================
    # 3. Load trajectories
    # ============================================================
    print("\n--- Loading trajectories ---")
    swe_traj = build_trajectory_index(PROJECT / "data" / "swe_agent_trajectories_5000.jsonl")
    print(f"SWE trajectories: {len(swe_traj)}")

    oh_traj = build_trajectory_index(OH_DIR / "openhands_trajectories.jsonl")
    print(f"OH trajectories: {len(oh_traj)}")

    # ============================================================
    # 4. Prepare SWE 2-LF conf>=2 training data
    # ============================================================
    print("\n--- Preparing SWE 2-LF conf>=2 features ---")
    train_windows = []
    for w in conf2_2lf:
        tw = dict(w)
        tw["majority_label"] = tw["mv_2lf"]
        train_windows.append(tw)

    X_swe_raw, y_swe_raw = extract_features_batch(train_windows, swe_traj)
    valid_mask = np.any(X_swe_raw != 0, axis=1)
    X_swe_all = X_swe_raw[valid_mask]
    y_swe_all = y_swe_raw[valid_mask]
    print(f"  Total 2-LF conf>=2: {len(train_windows)}, valid (with trajectory): {valid_mask.sum()}")
    print(f"  X shape: {X_swe_all.shape}")

    # ============================================================
    # 5. In-domain sanity check (80/20 split)
    # ============================================================
    print("\n--- In-domain Sanity Check (stratified 80/20, seed=42) ---")
    idx_train, idx_test = train_test_split(
        np.arange(len(X_swe_all)), test_size=0.2, random_state=42, stratify=y_swe_all
    )
    X_tr, y_tr = X_swe_all[idx_train], y_swe_all[idx_train]
    X_te, y_te = X_swe_all[idx_test], y_swe_all[idx_test]

    gb_s = GradientBoostingClassifier(
        n_estimators=200, learning_rate=0.05, max_depth=5, random_state=42
    )
    gb_s.fit(X_tr, y_tr)
    gb_sp = gb_s.predict(X_te)

    rf_s = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42, n_jobs=-1)
    rf_s.fit(X_tr, y_tr)
    rf_sp = rf_s.predict(X_te)

    print(f"  Train: {len(idx_train)}, Test: {len(idx_test)}")
    print(f"  GB: macro_f1={f1_score(y_te, gb_sp, average='macro'):.4f}, "
          f"f1_stag={f1_score(y_te, gb_sp, pos_label=0):.4f}, "
          f"f1_prog={f1_score(y_te, gb_sp, pos_label=1):.4f}")
    print(f"  RF: macro_f1={f1_score(y_te, rf_sp, average='macro'):.4f}, "
          f"f1_stag={f1_score(y_te, rf_sp, pos_label=0):.4f}, "
          f"f1_prog={f1_score(y_te, rf_sp, pos_label=1):.4f}")
    print(f"  (Canonical 3-LF in-domain: GB~0.9951, RF~0.9951)")

    gb_in_f1 = f1_score(y_te, gb_sp, average="macro")
    rf_in_f1 = f1_score(y_te, rf_sp, average="macro")

    # ============================================================
    # 6. Train on ALL 2-LF conf>=2 for cross-agent
    # ============================================================
    print("\n--- Training on ALL SWE 2-LF conf>=2 ---")
    gb = GradientBoostingClassifier(
        n_estimators=200, learning_rate=0.05, max_depth=5, random_state=42
    )
    gb.fit(X_swe_all, y_swe_all)

    rf = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42, n_jobs=-1)
    rf.fit(X_swe_all, y_swe_all)
    print(f"  GB and RF trained on {len(X_swe_all)} 2-LF conf>=2 windows")

    # ============================================================
    # 7. Load OH evaluation data (separate OH file)
    # ============================================================
    print("\n--- Loading OH evaluation data ---")
    oh_windows = []
    with open(OH_DIR / "windows_labeled.jsonl") as f:
        for line in f:
            line = line.strip()
            if line:
                oh_windows.append(json.loads(line))

    oh_non_abstain = [w for w in oh_windows if w.get("majority_label", -1) != -1]
    oh_conf2 = [w for w in oh_non_abstain if w.get("confidence", 0) >= 2]
    oh_stag_all = sum(1 for w in oh_non_abstain if w["majority_label"] == 0)
    oh_stag_c2 = sum(1 for w in oh_conf2 if w["majority_label"] == 0)

    print(f"  OH total: {len(oh_windows)}")
    print(f"  OH non-abstain (all): {len(oh_non_abstain)} "
          f"(stag={oh_stag_all}, {oh_stag_all / len(oh_non_abstain) * 100:.1f}%)")
    print(f"  OH conf>=2: {len(oh_conf2)} "
          f"(stag={oh_stag_c2}, {oh_stag_c2 / len(oh_conf2) * 100:.1f}%)")

    print("\nExtracting OH features (all non-abstain)...")
    X_oh_all, y_oh_all = extract_features_batch(oh_non_abstain, oh_traj)

    print("Extracting OH features (conf>=2)...")
    X_oh_c2, y_oh_c2 = extract_features_batch(oh_conf2, oh_traj)

    # ============================================================
    # 8. Cross-agent evaluation
    # ============================================================
    print("\n" + "=" * 70)
    print("CROSS-AGENT RESULTS (SWE 2-LF -> OH)")
    print("=" * 70)

    results = {}
    for name, model in [("GB", gb), ("RF", rf)]:
        for scope, X_eval, y_eval, label in [
            ("OH all", X_oh_all, y_oh_all, "all"),
            ("OH conf>=2", X_oh_c2, y_oh_c2, "conf2"),
        ]:
            preds = model.predict(X_eval)
            mf1 = f1_score(y_eval, preds, average="macro")
            f1s = f1_score(y_eval, preds, pos_label=0)
            f1p = f1_score(y_eval, preds, pos_label=1)
            results[f"{name}_{label}"] = {
                "macro_f1": mf1, "f1_stag": f1s, "f1_prog": f1p, "N": len(y_eval)
            }

    print(f"\n{'Model':<6} {'Scope':<14} {'macro_F1':>9} {'f1_stag':>9} {'f1_prog':>9} {'N':>8}")
    print("-" * 58)
    for key in ["GB_all", "GB_conf2", "RF_all", "RF_conf2"]:
        r = results[key]
        name, scope = key.split("_", 1)
        scope_label = "OH all" if scope == "all" else "OH conf>=2"
        print(f"{name:<6} {scope_label:<14} {r['macro_f1']:>9.4f} {r['f1_stag']:>9.4f} "
              f"{r['f1_prog']:>9.4f} {r['N']:>8}")

    # Canonical 3-LF reference values
    ref = {
        "GB_all": 0.9674, "GB_conf2": 0.9919,
        "RF_all": 0.9123, "RF_conf2": 0.9959,
    }

    print(f"\n--- Delta vs canonical 3-LF ---")
    print(f"{'Model':<6} {'Scope':<14} {'3-LF':>9} {'2-LF':>9} {'delta':>9}")
    print("-" * 50)
    for key in ["GB_all", "GB_conf2", "RF_all", "RF_conf2"]:
        r = results[key]
        name, scope = key.split("_", 1)
        scope_label = "OH all" if scope == "all" else "OH conf>=2"
        d = (r["macro_f1"] - ref[key]) * 100
        print(f"{name:<6} {scope_label:<14} {ref[key]:>9.4f} {r['macro_f1']:>9.4f} {d:>+8.2f}pp")

    # ============================================================
    # 9. Full summary
    # ============================================================
    print("\n" + "=" * 70)
    print("FULL SUMMARY")
    print("=" * 70)

    print(f"\n(a) Training set sizes:")
    print(f"    2-LF conf>=2: {len(conf2_2lf)} windows")
    print(f"    3-LF conf>=2: {len(conf2_3lf)} windows")
    diff = len(conf2_2lf) - len(conf2_3lf)
    pct = (len(conf2_2lf) / len(conf2_3lf) - 1) * 100
    print(f"    Difference: {diff:+d} ({pct:+.1f}%)")

    print(f"\n(b) 2-LF vs 3-LF label agreement:")
    print(f"    Overall: {agree}/{len(overlap)} = {agree / len(overlap) * 100:.2f}%")

    print(f"\n(c) In-domain sanity (2-LF trained, 80/20 split):")
    print(f"    GB: {gb_in_f1:.4f}  (canonical 3-LF: ~0.9951)")
    print(f"    RF: {rf_in_f1:.4f}  (canonical 3-LF: ~0.9951)")

    print(f"\n(d) Cross-agent transfer (SWE->OH):")
    print(f"    GB OH all:     {results['GB_all']['macro_f1']:.4f}  (canonical: 0.9674)")
    print(f"    GB OH conf>=2: {results['GB_conf2']['macro_f1']:.4f}  (canonical: 0.9919)")
    print(f"    RF OH all:     {results['RF_all']['macro_f1']:.4f}  (canonical: 0.9123)")
    print(f"    RF OH conf>=2: {results['RF_conf2']['macro_f1']:.4f}  (canonical: 0.9959)")


if __name__ == "__main__":
    main()
