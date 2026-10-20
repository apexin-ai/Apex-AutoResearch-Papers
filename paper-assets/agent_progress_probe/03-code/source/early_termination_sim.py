#!/usr/bin/env python3
"""D072: Early Termination Simulation.

Simulate early termination based on stagnation prediction.
Train on SWE conf>=2, evaluate cross-agent on OH.
Policy: k consecutive stagnation predictions -> terminate.
Supports multi-seed runs for mean+-std confidence intervals.
"""

import argparse
import json
import re
from collections import Counter, defaultdict
from difflib import SequenceMatcher
from pathlib import Path

import numpy as np
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier

PROJECT = Path("/root/autodl-tmp/agent_progress_probe")
OH_DIR = Path("/root/autodl-tmp/openhands_data")

EDIT_CMDS = {"edit", "str_replace", "create", "insert"}
SEARCH_CMDS = {"search_dir", "search_file", "find_file", "find", "grep", "view"}
NAV_CMDS = {"open", "goto", "scroll_down", "scroll_up", "cd", "ls", "cat"}

K_VALUES = [1, 2, 3, 5, 7, 10]


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
        slope = (n * np.dot(x, y) - x.sum() * y.sum()) / (
            n * np.dot(x, x) - x.sum() ** 2 + 1e-9
        )
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
    n_test_output = sum(
        1 for t in texts if ("PASSED" in t or "FAILED" in t) and "test" in t.lower()
    )
    n_file_display = sum(1 for t in texts if "[File:" in t)
    n_nonzero_exit = sum(
        1
        for _, t in observations
        if re.search(r"exit code [1-9]|returned non-zero|command not found", t)
    )
    return np.array(
        [
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
        ],
        dtype=np.float32,
    )


def build_trajectory_index(path):
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


def simulate_early_termination(traj_windows, preds, labels, k, traj_total_steps):
    """Simulate k-consecutive-stagnation early termination policy.

    Args:
        traj_windows: dict[traj_id] -> list of (global_idx, window_dict) sorted by window_idx
        preds: np.array of predictions for all OH windows (0=stag, 1=prog)
        labels: np.array of MV labels for all OH windows
        k: consecutive stagnation threshold
        traj_total_steps: dict[traj_id] -> total trajectory step count

    Returns: dict with metrics
    """
    n_terminated = 0
    n_correct_termination = 0
    n_stag_tail = 0
    n_stag_tail_terminated = 0
    total_steps = 0
    saved_steps = 0
    n_false_termination = 0

    for traj_id, windows in traj_windows.items():
        if not windows:
            continue

        t_steps = traj_total_steps.get(traj_id, 0)
        if t_steps == 0:
            continue
        total_steps += t_steps

        last_global_idx = windows[-1][0]
        has_stag_tail = labels[last_global_idx] == 0
        if has_stag_tail:
            n_stag_tail += 1

        consec = 0
        terminated = False
        term_global_idx = None
        term_window = None

        for global_idx, w in windows:
            if preds[global_idx] == 0:
                consec += 1
            else:
                consec = 0

            if consec >= k:
                terminated = True
                term_global_idx = global_idx
                term_window = w
                break

        if terminated:
            n_terminated += 1
            if labels[term_global_idx] == 0:
                n_correct_termination += 1
            if has_stag_tail:
                n_stag_tail_terminated += 1
            else:
                n_false_termination += 1
            term_step = max(term_window["step_indices"])
            saved_steps += max(0, t_steps - term_step - 1)

    precision = n_correct_termination / max(n_terminated, 1)
    recall = n_stag_tail_terminated / max(n_stag_tail, 1)
    compute_saved = saved_steps / max(total_steps, 1)
    false_term_rate = n_false_termination / max(n_terminated, 1)

    return {
        "precision": round(precision, 4),
        "recall": round(recall, 4),
        "compute_saved": round(compute_saved, 4),
        "false_termination_rate": round(false_term_rate, 4),
        "n_terminated": int(n_terminated),
        "n_stag_tail": int(n_stag_tail),
        "n_stag_tail_terminated": int(n_stag_tail_terminated),
        "n_false_termination": int(n_false_termination),
        "total_steps": int(total_steps),
        "saved_steps": int(saved_steps),
    }


def main():
    parser = argparse.ArgumentParser(description="D072: Early Termination Simulation")
    parser.add_argument("--dry-run", action="store_true", help="Load data and print stats only")
    parser.add_argument("--seeds", type=int, nargs="+", default=[42, 123, 456],
                        help="Random seeds for multi-run aggregation (default: 42 123 456)")
    args = parser.parse_args()

    # ==================================================================
    # 1. Load SWE windows
    # ==================================================================
    print("Loading SWE windows...")
    swe_windows = []
    with open(PROJECT / "data" / "windows_labeled.jsonl") as f:
        for line in f:
            line = line.strip()
            if line:
                w = json.loads(line)
                if "openhands" not in w.get("trajectory_id", ""):
                    swe_windows.append(w)
    print(f"  SWE total: {len(swe_windows)}")

    swe_3lf_conf2 = [
        w for w in swe_windows
        if w.get("majority_label", -1) != -1 and w.get("confidence", 0) >= 2
    ]
    print(f"  3-LF conf>=2: {len(swe_3lf_conf2)}")

    for w in swe_windows:
        mv, conf = recompute_2lf(w)
        w["mv_2lf"] = mv
        w["conf_2lf"] = conf

    swe_2lf_conf2 = [w for w in swe_windows if w["conf_2lf"] >= 2 and w["mv_2lf"] != -1]
    print(f"  2-LF conf>=2: {len(swe_2lf_conf2)}")

    # ==================================================================
    # 2. Load trajectories
    # ==================================================================
    print("Loading SWE trajectories...")
    swe_traj = build_trajectory_index(PROJECT / "data" / "swe_agent_trajectories_5000.jsonl")
    print(f"  {len(swe_traj)} trajectories")

    print("Loading OH trajectories...")
    oh_traj = build_trajectory_index(OH_DIR / "openhands_trajectories.jsonl")
    print(f"  {len(oh_traj)} trajectories")

    # ==================================================================
    # 3. Extract SWE features (seed-independent)
    # ==================================================================
    print("Extracting SWE 3-LF features...")
    X_3lf, y_3lf = extract_features_batch(swe_3lf_conf2, swe_traj)
    valid_3lf = np.any(X_3lf != 0, axis=1)
    X_3lf, y_3lf = X_3lf[valid_3lf], y_3lf[valid_3lf]
    print(f"  3-LF valid: {len(X_3lf)}")

    print("Extracting SWE 2-LF features...")
    train_2lf = [dict(w, majority_label=w["mv_2lf"]) for w in swe_2lf_conf2]
    X_2lf, y_2lf = extract_features_batch(train_2lf, swe_traj)
    valid_2lf = np.any(X_2lf != 0, axis=1)
    X_2lf, y_2lf = X_2lf[valid_2lf], y_2lf[valid_2lf]
    print(f"  2-LF valid: {len(X_2lf)}")

    # ==================================================================
    # 4. Load OH evaluation data (conf>=2)
    # ==================================================================
    print("\nLoading OH windows...")
    oh_windows_all = []
    with open(OH_DIR / "windows_labeled.jsonl") as f:
        for line in f:
            line = line.strip()
            if line:
                oh_windows_all.append(json.loads(line))

    oh_conf2 = [
        w for w in oh_windows_all
        if w.get("majority_label", -1) != -1 and w.get("confidence", 0) >= 2
    ]
    n_oh_stag = sum(1 for w in oh_conf2 if w["majority_label"] == 0)
    n_oh_prog = sum(1 for w in oh_conf2 if w["majority_label"] == 1)
    stag_prevalence = n_oh_stag / len(oh_conf2)
    print(f"  OH conf>=2: {len(oh_conf2)} (stag={n_oh_stag}, prog={n_oh_prog}, prev={stag_prevalence:.3f})")

    # ==================================================================
    # 5. Extract OH features (seed-independent)
    # ==================================================================
    print("Extracting OH features...")
    X_oh, y_oh = extract_features_batch(oh_conf2, oh_traj)

    # ==================================================================
    # 6. Group OH windows by trajectory (seed-independent)
    # ==================================================================
    print("Grouping OH windows by trajectory...")
    traj_groups = defaultdict(list)
    for i, w in enumerate(oh_conf2):
        tid = w["trajectory_id"]
        traj_groups[tid].append((i, w))

    for tid in traj_groups:
        traj_groups[tid].sort(key=lambda x: x[1]["window_idx"])

    traj_total_steps = {}
    for i, w in enumerate(oh_conf2):
        tid = w["trajectory_id"]
        if tid in traj_total_steps:
            continue
        row_idx = w.get("row_index", -1)
        traj_steps = oh_traj.get(row_idx)
        if traj_steps is not None:
            traj_total_steps[tid] = len(traj_steps)

    n_traj = len(traj_groups)
    n_traj_with_steps = len(traj_total_steps)
    print(f"  {n_traj} trajectories, {n_traj_with_steps} with step data")

    if args.dry_run:
        print("\n[dry-run] Data loaded successfully. Exiting.")
        return

    # ==================================================================
    # 7. Multi-seed simulation loop
    # ==================================================================
    seeds = args.seeds
    print(f"\nRunning simulation with {len(seeds)} seed(s): {seeds}")

    all_seed_results = {}

    for seed in seeds:
        print(f"\n--- Seed {seed} ---")
        rng = np.random.RandomState(seed)

        print(f"  Training 3-LF GB (seed={seed})...")
        gb = GradientBoostingClassifier(
            n_estimators=200, learning_rate=0.05, max_depth=5, random_state=seed
        )
        gb.fit(X_3lf, y_3lf)

        print(f"  Training 2-LF RF (seed={seed})...")
        rf = RandomForestClassifier(
            n_estimators=100, max_depth=10, random_state=seed, n_jobs=-1
        )
        rf.fit(X_2lf, y_2lf)

        gb_preds = gb.predict(X_oh)
        rf_preds = rf.predict(X_oh)
        oracle_preds = y_oh.copy()
        random_preds = (rng.random(len(y_oh)) >= stag_prevalence).astype(int)

        model_preds = {
            "3lf_gb": gb_preds,
            "2lf_rf": rf_preds,
            "oracle": oracle_preds,
            "random": random_preds,
        }

        seed_results = {}
        for model_name, preds in model_preds.items():
            seed_results[model_name] = {}
            for k in K_VALUES:
                res = simulate_early_termination(
                    traj_groups, preds, y_oh, k, traj_total_steps
                )
                seed_results[model_name][str(k)] = res
                print(
                    f"  {model_name:>8} k={k:<2}: "
                    f"prec={res['precision']:.3f} rec={res['recall']:.3f} "
                    f"saved={res['compute_saved']:.3f} ftr={res['false_termination_rate']:.3f} "
                    f"(term={res['n_terminated']}/{n_traj})"
                )
            print()

        all_seed_results[seed] = seed_results

    # ==================================================================
    # 8. Aggregate mean +- std across seeds
    # ==================================================================
    print("Aggregating across seeds...")
    METRIC_KEYS = ["precision", "recall", "compute_saved", "false_termination_rate"]

    aggregated = {}
    for model_name in ["3lf_gb", "2lf_rf", "oracle", "random"]:
        aggregated[model_name] = {}
        for k_str in [str(k) for k in K_VALUES]:
            vals = {mk: [] for mk in METRIC_KEYS}
            for seed in seeds:
                entry = all_seed_results[seed][model_name][k_str]
                for mk in METRIC_KEYS:
                    vals[mk].append(entry[mk])

            agg_entry = {}
            for mk in METRIC_KEYS:
                arr = np.array(vals[mk])
                agg_entry[mk] = round(float(np.mean(arr)), 4)
                agg_entry[f"{mk}_std"] = round(float(np.std(arr)), 4)
            aggregated[model_name][k_str] = agg_entry

    # ==================================================================
    # 9. Save output
    # ==================================================================
    out_dir = PROJECT / "artifacts" / "d072"
    out_dir.mkdir(parents=True, exist_ok=True)

    per_seed_output = {}
    for seed in seeds:
        per_seed_output[str(seed)] = {
            model: {k: {
                "precision": v["precision"],
                "recall": v["recall"],
                "compute_saved": v["compute_saved"],
                "false_termination_rate": v["false_termination_rate"],
            } for k, v in kv.items()}
            for model, kv in all_seed_results[seed].items()
        }

    output = {
        "models": ["3lf_gb", "2lf_rf", "oracle", "random"],
        "k_values": K_VALUES,
        "results": aggregated,
        "per_seed": per_seed_output,
        "details": {str(seed): all_seed_results[seed] for seed in seeds},
        "metadata": {
            "oh_trajectories": n_traj,
            "oh_trajectories_with_steps": n_traj_with_steps,
            "oh_windows": len(oh_conf2),
            "stag_prevalence": round(stag_prevalence, 4),
            "swe_3lf_train": int(len(X_3lf)),
            "swe_2lf_train": int(len(X_2lf)),
            "seeds": seeds,
            "gb_hp": {"n_estimators": 200, "learning_rate": 0.05, "max_depth": 5},
            "rf_hp": {"n_estimators": 100, "max_depth": 10},
        },
    }

    out_path = out_dir / "early_termination_sim.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nSaved: {out_path}")

    # ==================================================================
    # 10. Summary table (aggregated)
    # ==================================================================
    print("\n" + "=" * 100)
    print(f"EARLY TERMINATION SIMULATION SUMMARY (mean +- std across {len(seeds)} seeds)")
    print("=" * 100)
    print(f"OH trajectories: {n_traj} | OH windows (conf>=2): {len(oh_conf2)} | Stag prevalence: {stag_prevalence:.1%}")
    print()

    header = f"{'Model':<10} {'k':>3} | {'Precision':>14} {'Recall':>14} {'Saved':>14} {'FalseTermR':>14}"
    print(header)
    print("-" * len(header))
    for model_name in ["3lf_gb", "2lf_rf", "oracle", "random"]:
        for k in K_VALUES:
            r = aggregated[model_name][str(k)]
            print(
                f"{model_name:<10} {k:>3} | "
                f"{r['precision']:.3f}+-{r['precision_std']:.3f} "
                f"{r['recall']:.3f}+-{r['recall_std']:.3f} "
                f"{r['compute_saved']:.3f}+-{r['compute_saved_std']:.3f} "
                f"{r['false_termination_rate']:.3f}+-{r['false_termination_rate_std']:.3f}"
            )
        print("-" * len(header))


if __name__ == "__main__":
    main()
