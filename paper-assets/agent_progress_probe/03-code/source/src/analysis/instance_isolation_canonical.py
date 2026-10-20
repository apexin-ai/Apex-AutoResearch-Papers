#!/usr/bin/env python3
"""Instance-level isolation with canonical baseline code.

Train on SWE-Agent TRAIN SPLIT ONLY (not trainval) to match
cross_agent_structural_baseline.py exactly. Evaluate OH full vs unseen-only.
"""

import json, re, sys
from collections import Counter, defaultdict
from difflib import SequenceMatcher
from pathlib import Path

import numpy as np
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.metrics import f1_score, accuracy_score, precision_score, recall_score


EDIT_CMDS = {"edit", "str_replace", "create", "insert"}
SEARCH_CMDS = {"search_dir", "search_file", "find_file", "find", "grep", "view"}
NAV_CMDS = {"open", "goto", "scroll_down", "scroll_up", "cd", "ls", "cat"}


def extract_command(text):
    match = re.search(r"```\n?(.*?)```", text, re.DOTALL)
    return match.group(1).strip() if match else None


def cmd_similarity(a, b):
    if a == b: return 1.0
    if not a or not b: return 0.0
    return SequenceMatcher(None, a, b).ratio()


def extract_features(steps, is_short):
    n = len(steps)
    if n == 0: return np.zeros(30)
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
        slope = (n * np.dot(x, y) - x.sum() * y.sum()) / (n * np.dot(x, x) - x.sum()**2 + 1e-9)
    else:
        slope = 0.0
    commands = []
    for s, t in actions:
        cmd = extract_command(t)
        if cmd: commands.append(cmd)
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
    n_edit = n_search = n_nav = n_submit = 0
    for cmd in commands:
        first_word = cmd.strip().split()[0] if cmd.strip() else ""
        if first_word in EDIT_CMDS: n_edit += 1
        elif first_word in SEARCH_CMDS: n_search += 1
        elif first_word in NAV_CMDS: n_nav += 1
        elif first_word == "submit": n_submit += 1
    edit_ratio = n_edit / max(n_cmds, 1)
    search_ratio = n_search / max(n_cmds, 1)
    if n_cmds >= 2:
        sims = [cmd_similarity(commands[i], commands[i+1]) for i in range(n_cmds - 1)]
        avg_adj_sim = np.mean(sims)
        max_adj_sim = max(sims)
        max_run = 1; cur_run = 1
        for s in sims:
            if s >= 0.9: cur_run += 1; max_run = max(max_run, cur_run)
            else: cur_run = 1
    else:
        avg_adj_sim = 0.0; max_adj_sim = 0.0; max_run = 0
    n_errors = sum(1 for t in texts if "Traceback" in t or "Error" in t)
    n_test_output = sum(1 for t in texts if ("PASSED" in t or "FAILED" in t) and "test" in t.lower())
    n_file_display = sum(1 for t in texts if "[File:" in t)
    n_nonzero_exit = sum(1 for _, t in observations if re.search(r"exit code [1-9]|returned non-zero|command not found", t))
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


def build_trajectory_index(traj_path, normalize_roles=False):
    index = {}
    with open(traj_path) as f:
        for row_idx, line in enumerate(f):
            line = line.strip()
            if not line: continue
            raw = json.loads(line)
            steps = []
            for s in raw.get("trajectory") or []:
                role = s.get("role", "unknown")
                if normalize_roles and role == "assistant": role = "ai"
                steps.append({"role": role, "text": s.get("text") or s.get("system_prompt") or ""})
            index[row_idx] = steps
    return index


def load_windows(path):
    windows = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line: continue
            windows.append(json.loads(line))
    return windows


def extract_all_features(windows, traj_index):
    features, labels = [], []
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
    if n_missing > 0:
        print(f"  [warn] {n_missing} missing step references", flush=True)
    X = np.stack(features)
    y = np.array(labels)
    X[~np.isfinite(X)] = 0.0
    return X, y


def compute_metrics(labels, preds):
    return {
        "macro_f1": f1_score(labels, preds, average="macro", zero_division=0),
        "accuracy": accuracy_score(labels, preds),
        "precision_macro": precision_score(labels, preds, average="macro", zero_division=0),
        "recall_macro": recall_score(labels, preds, average="macro", zero_division=0),
        "f1_stagnation": f1_score(labels, preds, pos_label=0, zero_division=0),
        "f1_progress": f1_score(labels, preds, pos_label=1, zero_division=0),
    }


def main():
    base = Path("/root/autodl-tmp/agent_progress_probe")
    data_dir = base / "data"
    oh_dir = Path("/root/autodl-tmp/openhands_data")
    out_dir = base / "artifacts" / "instance-isolation-canonical"
    out_dir.mkdir(parents=True, exist_ok=True)

    # ── Load split info (same as canonical baseline) ──
    with open(base / "checkpoints" / "split_info.json") as f:
        split_info = json.load(f)
    keep_indices = split_info.get("keep_indices")
    train_idx = split_info["train_indices"]

    # ── SWE-Agent: load and filter ──
    print("Loading SWE-Agent windows...", flush=True)
    swa_all_windows = load_windows(data_dir / "windows_labeled.jsonl")
    swa_nonabstain = [w for w in swa_all_windows if w.get("majority_label", -1) != -1]
    if keep_indices is not None:
        swa_conf2 = [swa_nonabstain[i] for i in keep_indices]
    else:
        swa_conf2 = swa_nonabstain
    # CRITICAL: train split only (not trainval) to match canonical baseline
    swa_train = [swa_conf2[i] for i in train_idx]
    print(f"  all={len(swa_all_windows)}, non_abstain={len(swa_nonabstain)}, conf2={len(swa_conf2)}, train={len(swa_train)}", flush=True)

    # ── Instance IDs ──
    swa_train_instances = {w["instance_id"] for w in swa_train if "instance_id" in w}
    swa_all_instances = {w["instance_id"] for w in swa_nonabstain if "instance_id" in w}
    print(f"  SWE train instances: {len(swa_train_instances)}", flush=True)

    # ── Extract SWE-Agent features (train split only) ──
    print("Loading SWE-Agent trajectories...", flush=True)
    swa_traj = build_trajectory_index(data_dir / "swe_agent_trajectories_5000.jsonl")
    print("Extracting SWE-Agent train features...", flush=True)
    X_train, y_train = extract_all_features(swa_train, swa_traj)
    print(f"  Train features: {X_train.shape}, stag={sum(y_train==0)}, prog={sum(y_train==1)}", flush=True)
    del swa_traj

    # ── OpenHands ──
    print("Loading OpenHands...", flush=True)
    oh_all_windows = load_windows(oh_dir / "windows_labeled.jsonl")
    oh_nonabstain = [w for w in oh_all_windows if w.get("majority_label", -1) != -1]
    print(f"  total={len(oh_all_windows)}, non_abstain={len(oh_nonabstain)}", flush=True)

    oh_instances = set()
    oh_instance_windows = defaultdict(int)
    oh_instance_windows_c2 = defaultdict(int)
    for w in oh_nonabstain:
        inst = w.get("instance_id", "")
        oh_instances.add(inst)
        oh_instance_windows[inst] += 1
        if w.get("confidence", 0) >= 2:
            oh_instance_windows_c2[inst] += 1

    # ── Overlap ──
    overlap = swa_train_instances & oh_instances
    oh_unseen_inst = oh_instances - swa_train_instances
    oh_overlap_w = sum(oh_instance_windows[i] for i in overlap)
    oh_unseen_w = sum(oh_instance_windows[i] for i in oh_unseen_inst)
    oh_overlap_w_c2 = sum(oh_instance_windows_c2.get(i, 0) for i in overlap)
    oh_unseen_w_c2 = sum(oh_instance_windows_c2.get(i, 0) for i in oh_unseen_inst)

    print(f"\n=== INSTANCE OVERLAP ===", flush=True)
    print(f"SWE train instances: {len(swa_train_instances)}", flush=True)
    print(f"OH instances:        {len(oh_instances)}", flush=True)
    print(f"Overlap:             {len(overlap)} ({len(overlap)/len(oh_instances)*100:.1f}% of OH)", flush=True)
    print(f"OH windows overlap:  {oh_overlap_w} (all), {oh_overlap_w_c2} (conf>=2)", flush=True)
    print(f"OH windows unseen:   {oh_unseen_w} (all), {oh_unseen_w_c2} (conf>=2)", flush=True)

    # ── Extract OH features (once for all) ──
    print("\nLoading OH trajectories...", flush=True)
    oh_traj = build_trajectory_index(oh_dir / "openhands_trajectories.jsonl", normalize_roles=True)
    print("Extracting OH features (all non-abstain)...", flush=True)
    X_oh_all, y_oh_all = extract_all_features(oh_nonabstain, oh_traj)
    print(f"  OH features: {X_oh_all.shape}", flush=True)
    del oh_traj

    # ── Build masks ──
    unseen_mask = np.array([w.get("instance_id", "") not in swa_train_instances for w in oh_nonabstain])
    conf2_mask = np.array([w.get("confidence", 0) >= 2 for w in oh_nonabstain])
    full_mask = np.ones(len(oh_nonabstain), dtype=bool)

    masks = {
        "full_all": full_mask,
        "unseen_all": unseen_mask,
        "full_conf2": conf2_mask,
        "unseen_conf2": unseen_mask & conf2_mask,
    }

    print(f"\nMask sizes: full_all={full_mask.sum()}, unseen_all={unseen_mask.sum()}, "
          f"full_conf2={conf2_mask.sum()}, unseen_conf2={(unseen_mask & conf2_mask).sum()}", flush=True)

    # ── Train (train split only, canonical hyperparams) ──
    print("\nTraining GB (n_estimators=200, lr=0.05, max_depth=5)...", flush=True)
    gb = GradientBoostingClassifier(n_estimators=200, learning_rate=0.05, max_depth=5, random_state=42)
    gb.fit(X_train, y_train)

    print("Training RF (n_estimators=100, max_depth=10)...", flush=True)
    rf = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42, n_jobs=-1)
    rf.fit(X_train, y_train)

    # ── Evaluate ──
    print(f"\n{'Setting':<20s} {'Model':>5s} {'N':>7s} {'macro_f1':>9s} {'f1_stag':>8s} {'f1_prog':>8s}", flush=True)
    print("-" * 60, flush=True)

    eval_results = {}
    for mask_name, mask in masks.items():
        X_sub = X_oh_all[mask]
        y_sub = y_oh_all[mask]
        eval_results[mask_name] = {}
        for model_name, model in [("GB", gb), ("RF", rf)]:
            preds = model.predict(X_sub)
            m = compute_metrics(y_sub.tolist(), preds.tolist())
            eval_results[mask_name][model_name] = m
            print(f"{mask_name:<20s} {model_name:>5s} {len(y_sub):>7d} {m['macro_f1']:>9.4f} {m['f1_stagnation']:>8.4f} {m['f1_progress']:>8.4f}", flush=True)

    # ── Table 2 verification ──
    table2 = {
        "GB_all": 0.9674,
        "RF_all": 0.9123,
        "GB_conf2": 0.9919,
        "RF_conf2": 0.9959,
    }
    print(f"\n=== TABLE 2 VERIFICATION ===", flush=True)
    verification = {}
    for key, target in table2.items():
        model, subset = key.split("_", 1)
        mask_key = f"full_{subset}" if subset == "all" else "full_conf2"
        actual = round(eval_results[mask_key][model]["macro_f1"], 4)
        match = actual == target
        diff = round((actual - target) * 10000, 1)
        verification[key] = {"target": target, "actual": actual, "match": match, "diff_bps": diff}
        status = "MATCH" if match else f"MISMATCH ({diff:+.1f} bps)"
        print(f"  {key}: target={target:.4f}, actual={actual:.4f} -> {status}", flush=True)

    all_match = all(v["match"] for v in verification.values())
    print(f"\nAll Table 2 numbers match: {all_match}", flush=True)

    # ── Deltas ──
    print(f"\n=== DELTA (unseen - full) ===", flush=True)
    deltas = {}
    for conf, fk, uk in [("all", "full_all", "unseen_all"), ("conf>=2", "full_conf2", "unseen_conf2")]:
        deltas[conf] = {}
        for mn in ["GB", "RF"]:
            ff1 = eval_results[fk][mn]["macro_f1"]
            uf1 = eval_results[uk][mn]["macro_f1"]
            d = uf1 - ff1
            deltas[conf][mn] = {"full": round(ff1, 4), "unseen": round(uf1, 4), "delta_pp": round(d * 100, 2)}
            print(f"  {conf:>8s} {mn}: full={ff1:.4f}, unseen={uf1:.4f}, delta={d*100:+.2f}pp", flush=True)

    # ── Save ──
    output = {
        "instance_overlap": {
            "swe_train_instances": len(swa_train_instances),
            "swe_all_instances": len(swa_all_instances),
            "oh_instances": len(oh_instances),
            "overlap_count": len(overlap),
            "overlap_ratio_of_oh": round(len(overlap) / len(oh_instances), 4),
            "oh_windows_in_overlap": oh_overlap_w,
            "oh_windows_in_unseen": oh_unseen_w,
            "oh_conf2_in_overlap": oh_overlap_w_c2,
            "oh_conf2_in_unseen": oh_unseen_w_c2,
            "overlapping_instances": sorted(overlap),
        },
        "evaluation": {k: {mn: {mk: round(mv, 4) for mk, mv in m.items()} for mn, m in v.items()} for k, v in eval_results.items()},
        "deltas": deltas,
        "table2_verification": verification,
        "all_table2_match": all_match,
        "data_stats": {
            "swe_train": len(y_train),
            "oh_nonabstain": int(full_mask.sum()),
            "oh_unseen": int(unseen_mask.sum()),
            "oh_conf2": int(conf2_mask.sum()),
            "oh_unseen_conf2": int((unseen_mask & conf2_mask).sum()),
        },
        "hyperparams": {
            "GB": {"n_estimators": 200, "learning_rate": 0.05, "max_depth": 5},
            "RF": {"n_estimators": 100, "max_depth": 10},
        },
        "note": "Trained on TRAIN SPLIT ONLY (not trainval) to match canonical cross_agent_structural_baseline.py",
    }
    out_path = out_dir / "results.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nSaved to {out_path}", flush=True)


if __name__ == "__main__":
    main()
