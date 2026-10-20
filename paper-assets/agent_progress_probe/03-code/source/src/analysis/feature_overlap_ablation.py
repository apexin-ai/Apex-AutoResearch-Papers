#!/usr/bin/env python3
"""Feature overlap ablation: remove LF-overlapping structural features and measure residual F1.

Addresses the concern that structural features' high F1 is due to circular
evaluation — features that directly encode the same signals as the LFs used
to generate training labels.
"""

import json
import re
from collections import Counter
from difflib import SequenceMatcher
from pathlib import Path

import numpy as np
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score

# ── All 30 features (indices match extract_features output) ──────────────────

FEATURE_NAMES = [
    "num_steps",                    # 0
    "num_actions",                  # 1
    "num_observations",             # 2
    "action_ratio",                 # 3
    "mean_text_len",                # 4
    "std_text_len",                 # 5
    "max_text_len",                 # 6
    "min_text_len",                 # 7
    "mean_action_len",              # 8
    "mean_obs_len",                 # 9
    "text_len_trend",               # 10
    "num_commands",                 # 11
    "mean_cmd_len",                 # 12
    "max_cmd_len",                  # 13
    "unique_cmd_ratio",             # 14
    "max_repeat_ratio",             # 15
    "num_edit_cmds",                # 16
    "num_search_cmds",              # 17
    "num_nav_cmds",                 # 18
    "num_submit_cmds",              # 19
    "edit_ratio",                   # 20
    "search_ratio",                 # 21
    "avg_adjacent_cmd_sim",         # 22
    "max_adjacent_cmd_sim",         # 23
    "max_consecutive_similar",      # 24
    "num_errors",                   # 25
    "num_test_outputs",             # 26
    "num_file_displays",            # 27
    "num_nonzero_exits",            # 28
    "is_short_trajectory",          # 29
]

# ── Feature overlap classification ───────────────────────────────────────────
# Conservative: if a feature *could* indirectly reflect a LF signal, it's overlapping.

CMD_REP_OVERLAP = {14, 15, 22, 23, 24}
# unique_cmd_ratio, max_repeat_ratio: direct repetition counts
# avg/max_adjacent_cmd_sim: SequenceMatcher similarity (same function as LF)
# max_consecutive_similar: consecutive run with sim>=0.9 (same logic as LF)

FILE_DIFF_OVERLAP = {16, 17, 20, 21, 27}
# num_edit_cmds, edit_ratio: count edit/str_replace/create/insert (same as LF)
# num_search_cmds, search_ratio: LF uses search-only count for stagnation
# num_file_displays: "[File:" patterns appear in edit outputs

OUTCOME_BP_OVERLAP = {29}
# is_short_trajectory: short trajs correlate with exit_context/timeout/stuck,
# which outcome_bp uses to label ALL windows as stagnation

ALL_LF_OVERLAP = CMD_REP_OVERLAP | FILE_DIFF_OVERLAP | OUTCOME_BP_OVERLAP

NO_OVERLAP = set(range(30)) - ALL_LF_OVERLAP

# ── Ablation settings ───────────────────────────────────────────────────────

ABLATION_SETTINGS = {
    "full_30": {
        "desc": "All 30 features (baseline)",
        "keep": set(range(30)),
    },
    "no_cmd_rep": {
        "desc": "Remove cmd_rep-overlapping features (5 removed)",
        "keep": set(range(30)) - CMD_REP_OVERLAP,
    },
    "no_file_diff": {
        "desc": "Remove file_diff-overlapping features (5 removed)",
        "keep": set(range(30)) - FILE_DIFF_OVERLAP,
    },
    "no_outcome_bp": {
        "desc": "Remove outcome_bp-overlapping features (1 removed)",
        "keep": set(range(30)) - OUTCOME_BP_OVERLAP,
    },
    "no_all_lf": {
        "desc": "Remove ALL LF-overlapping features (11 removed, 19 remain)",
        "keep": NO_OVERLAP,
    },
}


# ── Feature extraction (copied from cross_agent_structural_baseline.py) ─────

EDIT_CMDS = {"edit", "str_replace", "create", "insert"}
SEARCH_CMDS = {"search_dir", "search_file", "find_file", "find", "grep", "view"}
NAV_CMDS = {"open", "goto", "scroll_down", "scroll_up", "cd", "ls", "cat"}


def extract_command(text):
    match = re.search(r"```\n?(.*?)```", text, re.DOTALL)
    return match.group(1).strip() if match else None


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
        slope = (n * np.dot(x, y) - x.sum() * y.sum()) / (n * np.dot(x, x) - x.sum()**2 + 1e-9)
    else:
        slope = 0.0

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

    n_edit = n_search = n_nav = n_submit = 0
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

    if n_cmds >= 2:
        sims = [cmd_similarity(commands[i], commands[i+1]) for i in range(n_cmds - 1)]
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


# ── Data loading ─────────────────────────────────────────────────────────────

def build_trajectory_index(traj_path, normalize_roles=False):
    index = {}
    with open(traj_path) as f:
        for row_idx, line in enumerate(f):
            line = line.strip()
            if not line:
                continue
            raw = json.loads(line)
            steps = []
            for s in raw.get("trajectory") or []:
                role = s.get("role", "unknown")
                if normalize_roles and role == "assistant":
                    role = "ai"
                steps.append({
                    "role": role,
                    "text": s.get("text") or s.get("system_prompt") or "",
                })
            index[row_idx] = steps
    return index


def load_windows(path):
    windows = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            windows.append(json.loads(line))
    return windows


def extract_all_features(windows, traj_index):
    features = []
    labels = []
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
        feat = extract_features(window_steps, w.get("short_trajectory", False))
        features.append(feat)
        labels.append(w["majority_label"])
    X = np.stack(features)
    y = np.array(labels)
    X[~np.isfinite(X)] = 0.0
    return X, y


def compute_metrics(labels, preds):
    return {
        "macro_f1": f1_score(labels, preds, average="macro", zero_division=0),
        "accuracy": accuracy_score(labels, preds),
        "f1_stagnation": f1_score(labels, preds, pos_label=0, zero_division=0),
        "f1_progress": f1_score(labels, preds, pos_label=1, zero_division=0),
    }


# ── Training + evaluation ───────────────────────────────────────────────────

def train_and_eval(X_train, y_train, X_val, y_val, X_test, y_test,
                   X_oh_all=None, y_oh_all=None):
    results = {}

    # RF
    best_n, best_f1 = 100, -1
    for n in [50, 100, 200, 500]:
        rf = RandomForestClassifier(n_estimators=n, max_depth=10, random_state=42, n_jobs=-1)
        rf.fit(X_train, y_train)
        preds = rf.predict(X_val)
        f1 = f1_score(y_val, preds, average="macro", zero_division=0)
        if f1 > best_f1:
            best_f1 = f1
            best_n = n

    rf = RandomForestClassifier(n_estimators=best_n, max_depth=10, random_state=42, n_jobs=-1)
    rf.fit(X_train, y_train)
    results["RF"] = {
        "in_domain": compute_metrics(y_test.tolist(), rf.predict(X_test).tolist()),
        "hp": {"n_estimators": best_n},
    }
    if X_oh_all is not None:
        results["RF"]["cross_agent_all"] = compute_metrics(y_oh_all.tolist(), rf.predict(X_oh_all).tolist())

    # GB
    best_lr, best_f1 = 0.05, -1
    for lr_val in [0.01, 0.05, 0.1, 0.2]:
        gb = GradientBoostingClassifier(n_estimators=200, learning_rate=lr_val, max_depth=5, random_state=42)
        gb.fit(X_train, y_train)
        preds = gb.predict(X_val)
        f1 = f1_score(y_val, preds, average="macro", zero_division=0)
        if f1 > best_f1:
            best_f1 = f1
            best_lr = lr_val

    gb = GradientBoostingClassifier(n_estimators=200, learning_rate=best_lr, max_depth=5, random_state=42)
    gb.fit(X_train, y_train)
    results["GB"] = {
        "in_domain": compute_metrics(y_test.tolist(), gb.predict(X_test).tolist()),
        "hp": {"learning_rate": best_lr},
    }
    if X_oh_all is not None:
        results["GB"]["cross_agent_all"] = compute_metrics(y_oh_all.tolist(), gb.predict(X_oh_all).tolist())

    return results


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    base = Path("/root/autodl-tmp/agent_progress_probe")
    data_dir = base / "data"
    oh_dir = Path("/root/autodl-tmp/openhands_data")
    out_dir = base / "artifacts" / "feature-overlap-ablation"
    out_dir.mkdir(parents=True, exist_ok=True)

    # Load split info
    with open(base / "checkpoints" / "split_info.json") as f:
        split_info = json.load(f)
    keep_indices = split_info.get("keep_indices")
    train_idx = split_info["train_indices"]
    val_idx = split_info["val_indices"]
    test_idx = split_info["test_indices"]

    # Load SWE-Agent data
    print("Loading SWE-Agent trajectories...")
    swa_traj = build_trajectory_index(data_dir / "swe_agent_trajectories_5000.jsonl")
    all_windows = load_windows(data_dir / "windows_labeled.jsonl")
    non_abstain = [w for w in all_windows if w.get("majority_label", -1) != -1]
    if keep_indices is not None:
        windows = [non_abstain[i] for i in keep_indices]
    else:
        windows = non_abstain
    print(f"  SWE-Agent: {len(windows)} windows (conf>=2)")

    print("Extracting SWE-Agent features (all 30)...")
    X_swa, y_swa = extract_all_features(windows, swa_traj)
    print(f"  Shape: {X_swa.shape}")

    X_train_full, y_train = X_swa[train_idx], y_swa[train_idx]
    X_val_full, y_val = X_swa[val_idx], y_swa[val_idx]
    X_test_full, y_test = X_swa[test_idx], y_swa[test_idx]
    print(f"  Train={len(y_train)}, Val={len(y_val)}, Test={len(y_test)}")

    # Load OpenHands data
    print("Loading OH trajectories...")
    oh_traj = build_trajectory_index(oh_dir / "openhands_trajectories.jsonl", normalize_roles=True)
    oh_all_windows = load_windows(oh_dir / "windows_labeled.jsonl")
    oh_nonabstain = [w for w in oh_all_windows if w.get("majority_label", -1) != -1]
    print(f"  OH: {len(oh_nonabstain)} non-abstain windows")

    print("Extracting OH features (all 30)...")
    X_oh_full, y_oh = extract_all_features(oh_nonabstain, oh_traj)
    print(f"  Shape: {X_oh_full.shape}")

    # ── Run ablations ────────────────────────────────────────────────────────
    all_results = {}

    for setting_name, setting in ABLATION_SETTINGS.items():
        keep = sorted(setting["keep"])
        n_keep = len(keep)
        removed = sorted(set(range(30)) - setting["keep"])
        removed_names = [FEATURE_NAMES[i] for i in removed]

        print(f"\n{'='*70}")
        print(f"Ablation: {setting_name} — {setting['desc']}")
        print(f"  Keeping {n_keep} features, removed: {removed_names}")
        print(f"  Kept features: {[FEATURE_NAMES[i] for i in keep]}")

        X_train = X_train_full[:, keep]
        X_val = X_val_full[:, keep]
        X_test = X_test_full[:, keep]
        X_oh = X_oh_full[:, keep]

        results = train_and_eval(X_train, y_train, X_val, y_val, X_test, y_test,
                                 X_oh, y_oh)

        for model_name, m in results.items():
            print(f"\n  {model_name}:")
            print(f"    In-domain:    macro_f1={m['in_domain']['macro_f1']:.4f}")
            if "cross_agent_all" in m:
                print(f"    Cross-agent:  macro_f1={m['cross_agent_all']['macro_f1']:.4f}")

        all_results[setting_name] = {
            "description": setting["desc"],
            "n_features": n_keep,
            "removed_features": removed_names,
            "kept_features": [FEATURE_NAMES[i] for i in keep],
            "models": {k: {kk: vv for kk, vv in v.items() if kk != "hp"}
                       for k, v in results.items()},
            "hyperparams": {k: v.get("hp", {}) for k, v in results.items()},
        }

    # ── Comparison table ─────────────────────────────────────────────────────
    print(f"\n\n{'='*80}")
    print("COMPARISON TABLE")
    print(f"{'='*80}")

    baseline_rf_id = all_results["full_30"]["models"]["RF"]["in_domain"]["macro_f1"]
    baseline_gb_id = all_results["full_30"]["models"]["GB"]["in_domain"]["macro_f1"]
    baseline_rf_ca = all_results["full_30"]["models"]["RF"]["cross_agent_all"]["macro_f1"]
    baseline_gb_ca = all_results["full_30"]["models"]["GB"]["cross_agent_all"]["macro_f1"]

    header = f"{'Setting':<20s} {'#Feat':>5s}  {'RF_ID':>7s} {'Δ':>6s}  {'GB_ID':>7s} {'Δ':>6s}  {'RF_CA':>7s} {'Δ':>6s}  {'GB_CA':>7s} {'Δ':>6s}"
    print(header)
    print("-" * len(header))

    for sname in ["full_30", "no_cmd_rep", "no_file_diff", "no_outcome_bp", "no_all_lf"]:
        r = all_results[sname]
        nf = r["n_features"]
        rf_id = r["models"]["RF"]["in_domain"]["macro_f1"]
        gb_id = r["models"]["GB"]["in_domain"]["macro_f1"]
        rf_ca = r["models"]["RF"]["cross_agent_all"]["macro_f1"]
        gb_ca = r["models"]["GB"]["cross_agent_all"]["macro_f1"]

        d_rf_id = (rf_id - baseline_rf_id) * 100
        d_gb_id = (gb_id - baseline_gb_id) * 100
        d_rf_ca = (rf_ca - baseline_rf_ca) * 100
        d_gb_ca = (gb_ca - baseline_gb_ca) * 100

        print(f"{sname:<20s} {nf:>5d}  {rf_id:>7.4f} {d_rf_id:>+5.1f}pp  "
              f"{gb_id:>7.4f} {d_gb_id:>+5.1f}pp  "
              f"{rf_ca:>7.4f} {d_rf_ca:>+5.1f}pp  "
              f"{gb_ca:>7.4f} {d_gb_ca:>+5.1f}pp")

    # ── Feature classification summary ───────────────────────────────────────
    print(f"\n\nFEATURE CLASSIFICATION")
    print(f"{'='*60}")
    for i, name in enumerate(FEATURE_NAMES):
        tags = []
        if i in CMD_REP_OVERLAP:
            tags.append("cmd_rep")
        if i in FILE_DIFF_OVERLAP:
            tags.append("file_diff")
        if i in OUTCOME_BP_OVERLAP:
            tags.append("outcome_bp")
        if not tags:
            tags.append("NO_OVERLAP")
        print(f"  [{i:2d}] {name:<30s}  overlap: {', '.join(tags)}")

    print(f"\n  cmd_rep overlap:    {len(CMD_REP_OVERLAP)} features")
    print(f"  file_diff overlap:  {len(FILE_DIFF_OVERLAP)} features")
    print(f"  outcome_bp overlap: {len(OUTCOME_BP_OVERLAP)} features")
    print(f"  ALL LF overlap:     {len(ALL_LF_OVERLAP)} features")
    print(f"  No overlap:         {len(NO_OVERLAP)} features")

    # ── Save results ─────────────────────────────────────────────────────────
    # Round floats for readability
    def round_dict(d, decimals=4):
        if isinstance(d, dict):
            return {k: round_dict(v, decimals) for k, v in d.items()}
        elif isinstance(d, float):
            return round(d, decimals)
        elif isinstance(d, list):
            return [round_dict(x, decimals) for x in d]
        return d

    output = {
        "feature_classification": {
            "cmd_rep_overlap": [FEATURE_NAMES[i] for i in sorted(CMD_REP_OVERLAP)],
            "file_diff_overlap": [FEATURE_NAMES[i] for i in sorted(FILE_DIFF_OVERLAP)],
            "outcome_bp_overlap": [FEATURE_NAMES[i] for i in sorted(OUTCOME_BP_OVERLAP)],
            "no_overlap": [FEATURE_NAMES[i] for i in sorted(NO_OVERLAP)],
        },
        "ablation_results": round_dict(all_results),
        "baselines": {
            "full_30_RF_in_domain": round(baseline_rf_id, 4),
            "full_30_GB_in_domain": round(baseline_gb_id, 4),
            "full_30_RF_cross_agent": round(baseline_rf_ca, 4),
            "full_30_GB_cross_agent": round(baseline_gb_ca, 4),
        },
        "data_stats": {
            "swe_agent_train": len(y_train),
            "swe_agent_val": len(y_val),
            "swe_agent_test": len(y_test),
            "oh_all_nonabstain": len(y_oh),
        },
    }

    out_path = out_dir / "ablation_results.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nResults saved to {out_path}")


if __name__ == "__main__":
    main()
