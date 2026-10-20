#!/usr/bin/env python3
"""E5 + E8 server-side computation.

E5: Paired bootstrap 11-feat vs 30-feat GB on OH cross-agent windows.
E8: GB per-class breakdown on Set A (stag vs prog, unanimous vs majority).

Run on server: python3 run_e5_e8_server.py
"""

import csv
import json
import re
import sys
import warnings
from collections import Counter
from difflib import SequenceMatcher
from pathlib import Path

import numpy as np
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import f1_score, accuracy_score, precision_score, recall_score

warnings.filterwarnings("ignore")

PROJECT = Path("/root/autodl-tmp/agent_progress_probe")
OH_DIR = Path("/root/autodl-tmp/openhands_data")

EDIT_CMDS = {"edit", "str_replace", "create", "insert"}
SEARCH_CMDS = {"search_dir", "search_file", "find_file", "find", "grep", "view"}
NAV_CMDS = {"open", "goto", "scroll_down", "scroll_up", "cd", "ls", "cat"}

LF_OVERLAP_INDICES = [14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]


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
        max_run, cur_run = 1, 1
        for s in sims:
            if s >= 0.9:
                cur_run += 1
                max_run = max(max_run, cur_run)
            else:
                cur_run = 1
    else:
        avg_adj_sim = max_adj_sim = 0.0
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


def load_jsonl(path):
    windows = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                windows.append(json.loads(line))
    return windows


def build_traj_index(path):
    index = {}
    with open(path) as f:
        for i, line in enumerate(f):
            line = line.strip()
            if not line:
                continue
            raw = json.loads(line)
            steps = []
            for s in raw.get("trajectory") or []:
                steps.append({"role": s.get("role", "unknown"),
                              "text": s.get("text") or s.get("system_prompt") or ""})
            index[i] = steps
    return index


def wid(w):
    return f"{w['trajectory_id']}__w{w['window_idx']}"


def macro_f1(y_true, y_pred):
    return f1_score(y_true, y_pred, average="macro", zero_division=0)


def paired_bootstrap(y_true, preds_a, preds_b, n_boot=10000, seed=42):
    rng = np.random.RandomState(seed)
    n = len(y_true)
    obs_delta = macro_f1(y_true, preds_a) - macro_f1(y_true, preds_b)
    deltas = []
    for _ in range(n_boot):
        idx = rng.choice(n, n, replace=True)
        d = macro_f1(y_true[idx], preds_a[idx]) - macro_f1(y_true[idx], preds_b[idx])
        deltas.append(d)
    deltas = np.array(deltas)
    ci_lo, ci_hi = np.percentile(deltas, [2.5, 97.5])
    p = float(np.mean(deltas <= 0) if obs_delta > 0 else np.mean(deltas >= 0))
    return obs_delta, ci_lo, ci_hi, p


# ====================================================================
# E5: 11 vs 30 features paired bootstrap
# ====================================================================

def run_e5():
    print("=" * 60)
    print("E5: 11 vs 30 Features Paired Bootstrap (Cross-Agent)")
    print("=" * 60)

    # Load SWE training data
    swe_windows = load_jsonl(PROJECT / "data" / "windows_labeled.jsonl")
    swe_non_abstain = [w for w in swe_windows if w.get("majority_label", -1) != -1]
    print(f"SWE non-abstain windows: {len(swe_non_abstain)}")

    split_info = json.loads((PROJECT / "checkpoints" / "split_info.json").read_text())

    # Build SWE trajectory index
    print("Building SWE trajectory index...")
    swe_traj = build_traj_index(PROJECT / "data" / "swe_agent_trajectories_5000.jsonl")
    print(f"  SWE trajectories: {len(swe_traj)}")

    # Build SWE features
    print("Extracting SWE features...")
    swe_features = []
    swe_labels = []
    for w in swe_non_abstain:
        row_idx = w.get("row_index", 0)
        si = w["step_indices"]
        ts = swe_traj.get(row_idx, [])
        ws = [ts[j] if j < len(ts) else {"role": "unknown", "text": ""} for j in si]
        swe_features.append(extract_features(ws, w.get("short_trajectory", False)))
        swe_labels.append(w["majority_label"])
    swe_features = np.stack(swe_features)
    swe_labels = np.array(swe_labels)
    print(f"  SWE feature matrix: {swe_features.shape}")

    # Get training indices
    keep = split_info.get("keep_indices")
    train_idx = split_info["train_indices"]
    if keep:
        X_train = swe_features[keep][train_idx]
        y_train = swe_labels[keep][train_idx]
    else:
        X_train = swe_features[train_idx]
        y_train = swe_labels[train_idx]
    print(f"  Training set: {len(X_train)}")

    # Load OH cross-agent data
    oh_windows_path = OH_DIR / "windows_labeled.jsonl"
    if not oh_windows_path.exists():
        oh_windows_path = PROJECT / "data_openhands" / "windows_labeled.jsonl"
    if not oh_windows_path.exists():
        # Try alternative paths
        for p in [OH_DIR / "oh_windows_labeled.jsonl",
                  PROJECT / "data" / "oh_windows_labeled.jsonl"]:
            if p.exists():
                oh_windows_path = p
                break

    print(f"Loading OH windows from: {oh_windows_path}")
    oh_windows = load_jsonl(oh_windows_path)
    oh_non_abstain = [w for w in oh_windows if w.get("majority_label", -1) != -1]
    oh_conf2 = [w for w in oh_non_abstain if w.get("confidence", 0) >= 2]
    print(f"  OH non-abstain: {len(oh_non_abstain)}, conf≥2: {len(oh_conf2)}")

    # Build OH trajectory index
    oh_traj_path = OH_DIR / "openhands_trajectories.jsonl"
    if not oh_traj_path.exists():
        oh_traj_path = OH_DIR / "trajectories.jsonl"
    if not oh_traj_path.exists():
        for p in [PROJECT / "data_openhands" / "openhands_trajectories.jsonl",
                  PROJECT / "data" / "openhands_trajectories.jsonl"]:
            if p.exists():
                oh_traj_path = p
                break

    print(f"Building OH trajectory index from: {oh_traj_path}")
    oh_traj = build_traj_index(oh_traj_path)
    print(f"  OH trajectories: {len(oh_traj)}")

    # Build OH features
    print("Extracting OH features...")
    oh_features = []
    oh_labels = []
    oh_wids = []
    for w in oh_conf2:
        row_idx = w.get("row_index", 0)
        si = w["step_indices"]
        ts = oh_traj.get(row_idx, [])
        ws = [ts[j] if j < len(ts) else {"role": "unknown", "text": ""} for j in si]
        oh_features.append(extract_features(ws, w.get("short_trajectory", False)))
        oh_labels.append(w["majority_label"])
        oh_wids.append(wid(w))
    oh_features = np.stack(oh_features)
    oh_labels = np.array(oh_labels)
    print(f"  OH feature matrix: {oh_features.shape}")

    # Train GB with ALL 30 features
    print("\nTraining GB (30 features)...")
    gb_30 = GradientBoostingClassifier(
        n_estimators=200, learning_rate=0.05, max_depth=5, random_state=42)
    gb_30.fit(X_train, y_train)
    preds_30 = gb_30.predict(oh_features)
    f1_30 = macro_f1(oh_labels, preds_30)
    print(f"  GB-30 cross-agent F1: {f1_30:.4f}")

    # Train GB with 11 LF-overlap features only
    print("Training GB (11 LF-overlap features)...")
    X_train_11 = X_train[:, LF_OVERLAP_INDICES]
    oh_features_11 = oh_features[:, LF_OVERLAP_INDICES]
    gb_11 = GradientBoostingClassifier(
        n_estimators=200, learning_rate=0.05, max_depth=5, random_state=42)
    gb_11.fit(X_train_11, y_train)
    preds_11 = gb_11.predict(oh_features_11)
    f1_11 = macro_f1(oh_labels, preds_11)
    print(f"  GB-11 cross-agent F1: {f1_11:.4f}")

    # Paired bootstrap
    print(f"\nPaired bootstrap (B=10000, seed=42)...")
    delta, ci_lo, ci_hi, p = paired_bootstrap(oh_labels, preds_11, preds_30, n_boot=10000, seed=42)
    sig = "YES" if p < 0.05 else "NO"
    print(f"  Observed Δ (11-feat − 30-feat): {delta:+.4f}")
    print(f"  95% CI: [{ci_lo:+.4f}, {ci_hi:+.4f}]")
    print(f"  p-value: {p:.4f}  (significant at α=0.05: {sig})")

    results = {
        "n_oh_windows": len(oh_conf2),
        "gb_30_f1": round(f1_30, 4),
        "gb_11_f1": round(f1_11, 4),
        "delta_11_minus_30": round(delta, 4),
        "ci_95_lo": round(ci_lo, 4),
        "ci_95_hi": round(ci_hi, 4),
        "p_value": round(p, 4),
        "significant_005": p < 0.05,
        "n_bootstrap": 10000,
        "seed": 42,
    }
    return results


# ====================================================================
# E8: GB on Set A per-class breakdown
# ====================================================================

def run_e8():
    print("\n" + "=" * 60)
    print("E8: GB on Set A — Per-Class & Unanimous Breakdown")
    print("=" * 60)

    # Load Set A gold labels
    gold_a = {}
    with open(PROJECT / "artifacts" / "gold_set" / "gold_3annotator_A.csv") as f:
        reader = csv.DictReader(f)
        for row in reader:
            gold_a[row["window_id"]] = int(row["gold_label"])
    print(f"Set A: {len(gold_a)} windows")

    # Load 3-annotator annotations to identify unanimous
    def read_batch(path):
        rows = {}
        with open(path) as f:
            reader = csv.DictReader(f)
            for row in reader:
                tid = row["trajectory_id"].strip('"')
                widx = int(row["window_idx"])
                key = f"{tid}__w{widx}"
                label = 1 if row["annotator_label"] == "progress" else 0
                rows[key] = label
        return rows

    b1 = read_batch(PROJECT / "artifacts" / "gold_set" / "annotation_unknown_2026-05-15.csv")
    b2 = read_batch(PROJECT / "artifacts" / "gold_set" / "annotation_unknown_2026-05-15_batch2.csv")
    b3a = read_batch(PROJECT / "artifacts" / "gold_set" / "annotation_unknown_2026-05-15_batch3a.csv")
    b3b = read_batch(PROJECT / "artifacts" / "gold_set" / "annotation_unknown_2026-05-15_batch3b.csv")
    b3 = {**b3a, **b3b}

    three_keys = set(b1) & set(b2) & set(b3)
    unanimous = {k for k in three_keys if b1[k] == b2[k] == b3[k]}

    # Load SWE data and build model
    swe_windows = load_jsonl(PROJECT / "data" / "windows_labeled.jsonl")
    swe_non_abstain = [w for w in swe_windows if w.get("majority_label", -1) != -1]
    wid_to_idx = {wid(w): i for i, w in enumerate(swe_non_abstain)}

    split_info = json.loads((PROJECT / "checkpoints" / "split_info.json").read_text())

    print("Building trajectory index...")
    swe_traj = build_traj_index(PROJECT / "data" / "swe_agent_trajectories_5000.jsonl")

    # Also try OH trajectories if gold windows include OH
    oh_traj = {}
    for p in [OH_DIR / "openhands_trajectories.jsonl", OH_DIR / "trajectories.jsonl"]:
        if p.exists():
            oh_traj = build_traj_index(p)
            print(f"  OH trajectories: {len(oh_traj)}")
            break

    # Build features for ALL windows
    print("Extracting features for all windows...")
    all_features = []
    all_labels = []
    for w in swe_non_abstain:
        row_idx = w.get("row_index", 0)
        si = w["step_indices"]
        is_oh = "openhands" in w.get("trajectory_id", "")
        if is_oh and oh_traj:
            ts = oh_traj.get(row_idx, [])
        else:
            ts = swe_traj.get(row_idx, [])
        ws = [ts[j] if j < len(ts) else {"role": "unknown", "text": ""} for j in si]
        all_features.append(extract_features(ws, w.get("short_trajectory", False)))
        all_labels.append(w["majority_label"])
    all_features = np.stack(all_features)
    all_labels = np.array(all_labels)

    # Also load OH windows if separate
    oh_wid_to_feat = {}
    oh_windows_path = OH_DIR / "windows_labeled.jsonl"
    if oh_windows_path.exists():
        oh_windows = load_jsonl(oh_windows_path)
        oh_na = [w for w in oh_windows if w.get("majority_label", -1) != -1]
        for w in oh_na:
            row_idx = w.get("row_index", 0)
            si = w["step_indices"]
            ts = oh_traj.get(row_idx, [])
            ws = [ts[j] if j < len(ts) else {"role": "unknown", "text": ""} for j in si]
            oh_wid_to_feat[wid(w)] = extract_features(ws, w.get("short_trajectory", False))

    # Train GB excluding gold windows
    keep = split_info.get("keep_indices")
    train_idx = split_info["train_indices"]
    gold_noabs = {wid_to_idx[k] for k in gold_a if k in wid_to_idx}

    if keep:
        feat_sub = all_features[keep]
        lab_sub = all_labels[keep]
        clean_train = [i for i in train_idx if keep[i] not in gold_noabs]
    else:
        feat_sub = all_features
        lab_sub = all_labels
        clean_train = [i for i in train_idx if i not in gold_noabs]

    X_train = feat_sub[clean_train]
    y_train = lab_sub[clean_train]
    print(f"Training GB (excl gold): {len(X_train)} samples")

    gb = GradientBoostingClassifier(
        n_estimators=200, learning_rate=0.05, max_depth=5, random_state=42)
    gb.fit(X_train, y_train)

    # Predict on Set A windows
    golds, preds, is_unan, gold_classes = [], [], [], []
    missing = 0
    for k, gl in gold_a.items():
        feat = None
        if k in wid_to_idx:
            feat = all_features[wid_to_idx[k]]
        elif k in oh_wid_to_feat:
            feat = oh_wid_to_feat[k]

        if feat is None:
            missing += 1
            continue

        pred = gb.predict(feat.reshape(1, -1))[0]
        golds.append(gl)
        preds.append(pred)
        is_unan.append(k in unanimous)
        gold_classes.append(gl)

    golds = np.array(golds)
    preds = np.array(preds)
    is_unan = np.array(is_unan)

    print(f"\nSet A evaluated: {len(golds)} (missing: {missing})")

    def report_metrics(name, y_true, y_pred):
        n = len(y_true)
        if n == 0:
            print(f"  {name}: N=0 (skipped)")
            return None
        mf1 = macro_f1(y_true, y_pred)
        acc = accuracy_score(y_true, y_pred)
        f1_s = f1_score(y_true, y_pred, pos_label=0, zero_division=0)
        f1_p = f1_score(y_true, y_pred, pos_label=1, zero_division=0)
        prec_s = precision_score(y_true, y_pred, pos_label=0, zero_division=0)
        rec_s = recall_score(y_true, y_pred, pos_label=0, zero_division=0)
        print(f"  {name}: N={n}, macro-F1={mf1:.4f}, acc={acc:.4f}, "
              f"F1(stag)={f1_s:.4f}, F1(prog)={f1_p:.4f}, "
              f"prec(stag)={prec_s:.4f}, rec(stag)={rec_s:.4f}")
        return {
            "n": n, "macro_f1": round(mf1, 4), "accuracy": round(acc, 4),
            "f1_stag": round(f1_s, 4), "f1_prog": round(f1_p, 4),
            "prec_stag": round(prec_s, 4), "rec_stag": round(rec_s, 4),
        }

    results = {}
    print("\n--- All Set A ---")
    results["all"] = report_metrics("All", golds, preds)

    # Stagnation-only
    stag_mask = golds == 0
    prog_mask = golds == 1
    print("\n--- By gold class ---")
    n_stag = stag_mask.sum()
    n_prog = prog_mask.sum()
    stag_correct = (preds[stag_mask] == 0).sum()
    prog_correct = (preds[prog_mask] == 1).sum()
    print(f"  Stagnation: {stag_correct}/{n_stag} correct ({100*stag_correct/max(n_stag,1):.1f}%)")
    print(f"  Progress:   {prog_correct}/{n_prog} correct ({100*prog_correct/max(n_prog,1):.1f}%)")
    results["stag_correct"] = int(stag_correct)
    results["stag_total"] = int(n_stag)
    results["prog_correct"] = int(prog_correct)
    results["prog_total"] = int(n_prog)

    # Unanimous subset
    print("\n--- Unanimous (conf=3) ---")
    results["unanimous"] = report_metrics("Unanimous", golds[is_unan], preds[is_unan])
    unan_stag = (golds[is_unan] == 0)
    unan_prog = (golds[is_unan] == 1)
    if unan_stag.sum() > 0:
        us_correct = (preds[is_unan][unan_stag] == 0).sum()
        print(f"  Unanimous stag: {us_correct}/{unan_stag.sum()} correct")
        results["unanimous_stag_correct"] = int(us_correct)
        results["unanimous_stag_total"] = int(unan_stag.sum())
    if unan_prog.sum() > 0:
        up_correct = (preds[is_unan][unan_prog] == 1).sum()
        print(f"  Unanimous prog: {up_correct}/{unan_prog.sum()} correct")
        results["unanimous_prog_correct"] = int(up_correct)
        results["unanimous_prog_total"] = int(unan_prog.sum())

    # Majority 2:1 subset
    maj_mask = ~is_unan
    print("\n--- Majority 2:1 (conf=2) ---")
    results["majority"] = report_metrics("Majority", golds[maj_mask], preds[maj_mask])

    return results


if __name__ == "__main__":
    all_results = {}

    try:
        all_results["E5"] = run_e5()
    except Exception as e:
        print(f"\nE5 FAILED: {e}")
        import traceback; traceback.print_exc()
        all_results["E5"] = {"error": str(e)}

    try:
        all_results["E8"] = run_e8()
    except Exception as e:
        print(f"\nE8 FAILED: {e}")
        import traceback; traceback.print_exc()
        all_results["E8"] = {"error": str(e)}

    out = PROJECT / "artifacts" / "e5_e8_server_results.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    with open(out, "w") as f:
        json.dump(all_results, f, indent=2)
    print(f"\nResults saved: {out}")
