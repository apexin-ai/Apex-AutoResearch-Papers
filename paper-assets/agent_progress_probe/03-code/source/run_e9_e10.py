#!/usr/bin/env python3
"""E9: Multi-seed Paired t-tests + E10: Conf=1 Subset Evaluation."""

import json
import re
import sys
from collections import Counter
from difflib import SequenceMatcher
from pathlib import Path

import numpy as np
from scipy import stats
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.metrics import f1_score, accuracy_score, precision_score, recall_score
from sklearn.model_selection import train_test_split

BASE = Path(__file__).parent
DATA_DIR = BASE / "artifacts" / "data"

# ============================================================
# Feature extraction (from e3_conf_stratified_gap.py)
# ============================================================
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


def compute_metrics(y_true, y_pred):
    return {
        "macro_f1": f1_score(y_true, y_pred, average="macro", zero_division=0),
        "accuracy": accuracy_score(y_true, y_pred),
        "f1_stag": f1_score(y_true, y_pred, pos_label=0, zero_division=0),
        "f1_prog": f1_score(y_true, y_pred, pos_label=1, zero_division=0),
    }


def cohens_d(a, b):
    na, nb = len(a), len(b)
    pooled_std = np.sqrt(((na - 1) * np.var(a, ddof=1) + (nb - 1) * np.var(b, ddof=1)) / (na + nb - 2))
    if pooled_std == 0:
        return float("inf") if np.mean(a) != np.mean(b) else 0.0
    return (np.mean(a) - np.mean(b)) / pooled_std


def paired_cohens_d(a, b):
    diffs = np.array(a) - np.array(b)
    if np.std(diffs, ddof=1) == 0:
        return float("inf") if np.mean(diffs) != 0 else 0.0
    return np.mean(diffs) / np.std(diffs, ddof=1)


def permutation_test(a, b, n_perms=10000, paired=True, seed=42):
    rng = np.random.RandomState(seed)
    a, b = np.array(a), np.array(b)
    if paired:
        assert len(a) == len(b)
        obs_diff = np.mean(a - b)
        diffs = a - b
        count = 0
        for _ in range(n_perms):
            signs = rng.choice([-1, 1], size=len(diffs))
            perm_diff = np.mean(diffs * signs)
            if abs(perm_diff) >= abs(obs_diff):
                count += 1
        return count / n_perms
    else:
        obs_diff = np.mean(a) - np.mean(b)
        combined = np.concatenate([a, b])
        na = len(a)
        count = 0
        for _ in range(n_perms):
            rng.shuffle(combined)
            perm_diff = np.mean(combined[:na]) - np.mean(combined[na:])
            if abs(perm_diff) >= abs(obs_diff):
                count += 1
        return count / n_perms


def run_e9():
    print("=" * 90)
    print("E9: MULTI-SEED PAIRED STATISTICAL TESTS")
    print("=" * 90)

    # ----------------------------------------------------------------
    # Per-seed data
    # ----------------------------------------------------------------
    probe_gru = {"seeds": [42, 123, 456], "macro_f1": [0.9055, 0.9265, 0.9234],
                 "f1_stag": [None, 0.9022, 0.9024], "f1_prog": [None, 0.9508, 0.9444]}
    probe_e5 = {"seeds": [42, 123, 456], "macro_f1": [0.9363, 0.9403, 0.9378],
                "f1_stag": [0.9067, 0.9272, 0.9179], "f1_prog": [0.9660, 0.9534, 0.9577]}
    probe_bgem3 = {"seeds": [42, 123, 456], "macro_f1": [0.9413, 0.8474, 0.9364],
                   "f1_stag": [0.9147, 0.8173, 0.9183], "f1_prog": [0.9679, 0.8775, 0.9545]}
    struct_gb_indomain = {"seeds": [42, 123, 456], "macro_f1": [0.9951, 0.9951, 0.9951]}
    struct_rf_indomain = {"seeds": [42, 123, 456], "macro_f1": [0.9951, 0.9951, 0.9951]}
    gb_cross_oh_all = {"seeds": [42, 123, 456, 789, 1024],
                       "macro_f1": [0.9674, 0.9662, 0.9699, 0.9615, 0.9656]}
    gb_cross_oh_conf2 = {"seeds": [42, 123, 456, 789, 1024],
                         "macro_f1": [0.9919, 0.9920, 0.9930, 0.9908, 0.9915]}
    probe_zero_shot_cross = 0.5984

    results = {}

    def report_test(name, a, b, a_name, b_name, paired=True):
        a_arr, b_arr = np.array(a), np.array(b)
        print(f"\n--- {name} ---")
        print(f"  {a_name}: {a_arr.mean():.4f} ± {a_arr.std(ddof=1):.4f} (n={len(a)})")
        print(f"  {b_name}: {b_arr.mean():.4f} ± {b_arr.std(ddof=1):.4f} (n={len(b)})")
        print(f"  Δ = {a_arr.mean() - b_arr.mean():+.4f}")

        if paired and len(a) == len(b):
            if np.std(a_arr - b_arr, ddof=1) == 0:
                print(f"  Paired t-test: N/A (zero variance in differences)")
                t_stat, p_val = 0.0, 1.0
            else:
                t_stat, p_val = stats.ttest_rel(a, b)
                print(f"  Paired t-test: t={t_stat:.4f}, p={p_val:.4f}, df={len(a)-1}")
            d = paired_cohens_d(a, b)
            perm_p = permutation_test(a, b, paired=True)
            print(f"  Permutation test (10k): p={perm_p:.4f}")
        else:
            t_stat, p_val = stats.ttest_ind(a, b, equal_var=False)
            print(f"  Welch's t-test: t={t_stat:.4f}, p={p_val:.4f}")
            d = cohens_d(a, b)
            perm_p = permutation_test(a, b, paired=False)
            print(f"  Permutation test (10k): p={perm_p:.4f}")

        print(f"  Cohen's d = {d:.4f}")
        sig = "***" if p_val < 0.001 else "**" if p_val < 0.01 else "*" if p_val < 0.05 else "ns"
        print(f"  Significance: {sig} (p={p_val:.4f})")

        results[name] = {
            "a_name": a_name, "b_name": b_name,
            "a_mean": round(float(a_arr.mean()), 4), "b_mean": round(float(b_arr.mean()), 4),
            "delta": round(float(a_arr.mean() - b_arr.mean()), 4),
            "t_stat": round(float(t_stat), 4), "p_value": round(float(p_val), 4),
            "perm_p": round(float(perm_p), 4),
            "cohens_d": round(float(d), 4) if not np.isinf(d) else "inf",
            "n_a": len(a), "n_b": len(b),
            "paired": paired and len(a) == len(b),
            "significant": p_val < 0.05,
        }

    # ================================================================
    # Comparison 1: Structural GB vs GRU Probe (in-domain, conf≥2)
    # ================================================================
    report_test(
        "Structural GB vs GRU Probe (in-domain)",
        struct_gb_indomain["macro_f1"], probe_gru["macro_f1"],
        "Struct GB", "GRU Probe", paired=True)

    # ================================================================
    # Comparison 2: E5-large Probe vs GRU Probe
    # ================================================================
    report_test(
        "E5-large Probe vs GRU Probe",
        probe_e5["macro_f1"], probe_gru["macro_f1"],
        "E5-large", "GRU (nomic)", paired=True)

    # ================================================================
    # Comparison 3: BGE-M3 Probe vs GRU Probe
    # ================================================================
    report_test(
        "BGE-M3 Probe vs GRU Probe",
        probe_bgem3["macro_f1"], probe_gru["macro_f1"],
        "BGE-M3", "GRU (nomic)", paired=True)

    # ================================================================
    # Comparison 4: E5-large vs BGE-M3
    # ================================================================
    report_test(
        "E5-large Probe vs BGE-M3 Probe",
        probe_e5["macro_f1"], probe_bgem3["macro_f1"],
        "E5-large", "BGE-M3", paired=True)

    # ================================================================
    # Comparison 5: Cross-agent GB (5 seeds) vs Probe zero-shot
    # ================================================================
    gb_vals = gb_cross_oh_all["macro_f1"]
    t_stat, p_val = stats.ttest_1samp(gb_vals, probe_zero_shot_cross)
    d = (np.mean(gb_vals) - probe_zero_shot_cross) / np.std(gb_vals, ddof=1)
    print(f"\n--- Cross-agent GB vs Probe zero-shot ---")
    print(f"  GB cross-agent: {np.mean(gb_vals):.4f} ± {np.std(gb_vals, ddof=1):.4f} (n=5)")
    print(f"  Probe zero-shot: {probe_zero_shot_cross:.4f} (n=1)")
    print(f"  Δ = {np.mean(gb_vals) - probe_zero_shot_cross:+.4f}")
    print(f"  One-sample t-test (GB vs probe point): t={t_stat:.4f}, p={p_val:.6f}")
    print(f"  Cohen's d = {d:.4f}")
    print(f"  Significance: *** (p={p_val:.6f})")
    results["Cross-agent GB vs Probe zero-shot"] = {
        "a_name": "GB cross-agent", "b_name": "Probe zero-shot",
        "a_mean": round(float(np.mean(gb_vals)), 4), "b_mean": probe_zero_shot_cross,
        "delta": round(float(np.mean(gb_vals) - probe_zero_shot_cross), 4),
        "t_stat": round(float(t_stat), 4), "p_value": round(float(p_val), 6),
        "cohens_d": round(float(d), 4),
        "n_a": 5, "n_b": 1, "paired": False,
        "test": "one-sample t", "significant": p_val < 0.05,
    }

    # ================================================================
    # Comparison 6: Cross-agent GB OH all (5 seeds) variance analysis
    # ================================================================
    print(f"\n--- Cross-agent GB stability (OH all) ---")
    print(f"  Seeds: {gb_cross_oh_all['seeds']}")
    print(f"  Values: {gb_cross_oh_all['macro_f1']}")
    print(f"  Mean: {np.mean(gb_cross_oh_all['macro_f1']):.4f}")
    print(f"  Std: {np.std(gb_cross_oh_all['macro_f1'], ddof=1):.4f}")
    print(f"  Range: [{min(gb_cross_oh_all['macro_f1']):.4f}, {max(gb_cross_oh_all['macro_f1']):.4f}]")
    print(f"  CV: {np.std(gb_cross_oh_all['macro_f1'], ddof=1) / np.mean(gb_cross_oh_all['macro_f1']) * 100:.3f}%")

    # ================================================================
    # Comparison 7: Cross-agent GB OH conf≥2 (5 seeds) variance
    # ================================================================
    print(f"\n--- Cross-agent GB stability (OH conf≥2) ---")
    print(f"  Seeds: {gb_cross_oh_conf2['seeds']}")
    print(f"  Values: {gb_cross_oh_conf2['macro_f1']}")
    print(f"  Mean: {np.mean(gb_cross_oh_conf2['macro_f1']):.4f}")
    print(f"  Std: {np.std(gb_cross_oh_conf2['macro_f1'], ddof=1):.4f}")
    print(f"  Range: [{min(gb_cross_oh_conf2['macro_f1']):.4f}, {max(gb_cross_oh_conf2['macro_f1']):.4f}]")

    # ================================================================
    # Bootstrap CIs from gold eval (already computed)
    # ================================================================
    print(f"\n--- Gold Set B Bootstrap Paired Tests (N=491, from gold-3annotator-eval) ---")
    gold_tests = {
        "GB vs MV": {"delta": 0.042, "p": 0.0001, "sig": True},
        "GB vs Probe": {"delta": 0.088, "p": 0.0001, "sig": True},
        "RF vs GB": {"delta": -0.029, "p": 0.0003, "sig": True},
        "TWV-Probe vs GB": {"delta": -0.023, "p": 0.056, "sig": False},
        "TWV-Probe vs Probe": {"delta": 0.064, "p": 0.0002, "sig": True},
    }
    for name, v in gold_tests.items():
        sig = "***" if v["p"] < 0.001 else "**" if v["p"] < 0.01 else "*" if v["p"] < 0.05 else "ns"
        print(f"  {name}: Δ={v['delta']:+.3f}, p={v['p']:.4f} ({sig})")
    results["gold_bootstrap_tests"] = gold_tests

    # ================================================================
    # Summary table
    # ================================================================
    print("\n" + "=" * 90)
    print("E9 SUMMARY TABLE")
    print("=" * 90)
    print(f"{'Comparison':<45} {'Δ':>7} {'t':>8} {'p':>8} {'d':>7} {'Sig':>4}")
    print("-" * 80)
    for name, r in results.items():
        if name == "gold_bootstrap_tests":
            continue
        delta = r.get("delta", 0)
        t = r.get("t_stat", 0)
        p = r.get("p_value", 1)
        d = r.get("cohens_d", 0)
        sig = "***" if p < 0.001 else "**" if p < 0.01 else "*" if p < 0.05 else "ns"
        d_str = f"{d:.2f}" if isinstance(d, float) else d
        print(f"{name:<45} {delta:>+7.4f} {t:>8.3f} {p:>8.4f} {d_str:>7} {sig:>4}")

    return results


def run_e10():
    print("\n\n" + "=" * 90)
    print("E10: CONF=1 SUBSET EVALUATION")
    print("=" * 90)

    # ================================================================
    # 1. Load windows
    # ================================================================
    print("Loading windows_labeled.jsonl ...")
    all_windows = []
    with open(DATA_DIR / "windows_labeled.jsonl") as f:
        for line in f:
            if line.strip():
                w = json.loads(line)
                w["confidence"] = int(w.get("confidence", 0))
                w["majority_label"] = int(w.get("majority_label", -1))
                w["row_index"] = int(w.get("row_index", 0))
                w["window_idx"] = int(w.get("window_idx", 0))
                si = w.get("step_indices", "[]")
                if isinstance(si, str):
                    si = json.loads(si)
                w["step_indices"] = si
                if isinstance(w.get("short_trajectory"), str):
                    w["short_trajectory"] = w["short_trajectory"].lower() == "true"
                all_windows.append(w)

    non_abstain = [w for w in all_windows if w["majority_label"] != -1]
    conf1 = [w for w in non_abstain if w["confidence"] == 1]
    conf2plus = [w for w in non_abstain if w["confidence"] >= 2]
    conf2only = [w for w in non_abstain if w["confidence"] == 2]
    conf3 = [w for w in non_abstain if w["confidence"] == 3]

    print(f"  Total: {len(all_windows)}")
    print(f"  Non-abstain: {len(non_abstain)}")
    print(f"  conf=1: {len(conf1)}")
    print(f"  conf≥2: {len(conf2plus)}")
    print(f"  conf=3: {len(conf3)}")

    conf1_stag = sum(1 for w in conf1 if w["majority_label"] == 0)
    conf2_stag = sum(1 for w in conf2plus if w["majority_label"] == 0)
    print(f"\n  conf=1 stag rate: {conf1_stag}/{len(conf1)} = {conf1_stag/len(conf1)*100:.1f}%")
    print(f"  conf≥2 stag rate: {conf2_stag}/{len(conf2plus)} = {conf2_stag/len(conf2plus)*100:.1f}%")

    # ================================================================
    # 2. Load trajectory data
    # ================================================================
    print("\nLoading trajectories ...")
    traj_file = DATA_DIR / "swe_agent_trajectories_5000.jsonl"
    traj_index = {}
    with open(traj_file) as f:
        for line in f:
            raw = json.loads(line.strip())
            steps = [{"role": s.get("role", "unknown"),
                      "text": s.get("text") or s.get("system_prompt") or ""}
                     for s in (raw.get("trajectory") or [])]
            traj_index[len(traj_index)] = steps
    print(f"  {len(traj_index)} trajectories")

    # ================================================================
    # 3. Extract features for ALL non-abstain windows
    # ================================================================
    print("Extracting features ...")
    features = np.zeros((len(non_abstain), 30), dtype=np.float32)
    labels = np.zeros(len(non_abstain), dtype=int)
    confs = np.zeros(len(non_abstain), dtype=int)

    for i, w in enumerate(non_abstain):
        row_idx = w["row_index"]
        traj_steps = traj_index.get(row_idx, [])
        window_steps = [traj_steps[si] if si < len(traj_steps) else {"role": "unknown", "text": ""}
                        for si in w["step_indices"]]
        features[i] = extract_features(window_steps, w.get("short_trajectory", False))
        labels[i] = w["majority_label"]
        confs[i] = w["confidence"]

    print(f"  Features: {features.shape}")

    # ================================================================
    # 4. Split and train on conf≥2, evaluate on conf=1
    # ================================================================
    conf2_mask = confs >= 2
    conf1_mask = confs == 1

    X_conf2 = features[conf2_mask]
    y_conf2 = labels[conf2_mask]
    X_conf1 = features[conf1_mask]
    y_conf1 = labels[conf1_mask]

    print(f"\n  Train data (conf≥2): {len(X_conf2)} windows")
    print(f"  Eval data (conf=1): {len(X_conf1)} windows")

    results = {}

    for seed in [42, 123, 456]:
        print(f"\n{'='*60}")
        print(f"  SEED = {seed}")
        print(f"{'='*60}")

        X_train, X_test_conf2, y_train, y_test_conf2 = train_test_split(
            X_conf2, y_conf2, test_size=0.2, random_state=seed, stratify=y_conf2)

        # GB canonical
        gb = GradientBoostingClassifier(n_estimators=200, learning_rate=0.05, max_depth=5, random_state=seed)
        gb.fit(X_train, y_train)

        # RF canonical
        rf = RandomForestClassifier(n_estimators=100, random_state=seed, n_jobs=-1)
        rf.fit(X_train, y_train)

        # Evaluate on conf≥2 test
        gb_pred_conf2 = gb.predict(X_test_conf2)
        rf_pred_conf2 = rf.predict(X_test_conf2)
        gb_m_conf2 = compute_metrics(y_test_conf2, gb_pred_conf2)
        rf_m_conf2 = compute_metrics(y_test_conf2, rf_pred_conf2)

        # Evaluate on conf=1
        gb_pred_conf1 = gb.predict(X_conf1)
        rf_pred_conf1 = rf.predict(X_conf1)
        gb_m_conf1 = compute_metrics(y_conf1, gb_pred_conf1)
        rf_m_conf1 = compute_metrics(y_conf1, rf_pred_conf1)

        # MV baseline on conf=1 (majority label IS the MV, so MV accuracy = 100% by definition)
        # Instead, show label distribution and how well models agree with silver labels
        mv_conf1_pred = y_conf1  # silver MV IS the label

        print(f"\n  conf≥2 test (n={len(y_test_conf2)}):")
        print(f"    GB: macro_f1={gb_m_conf2['macro_f1']:.4f}, f1_stag={gb_m_conf2['f1_stag']:.4f}, f1_prog={gb_m_conf2['f1_prog']:.4f}")
        print(f"    RF: macro_f1={rf_m_conf2['macro_f1']:.4f}, f1_stag={rf_m_conf2['f1_stag']:.4f}, f1_prog={rf_m_conf2['f1_prog']:.4f}")

        print(f"\n  conf=1 (n={len(y_conf1)}, stag={sum(y_conf1==0)}, prog={sum(y_conf1==1)}):")
        print(f"    GB: macro_f1={gb_m_conf1['macro_f1']:.4f}, f1_stag={gb_m_conf1['f1_stag']:.4f}, f1_prog={gb_m_conf1['f1_prog']:.4f}")
        print(f"    RF: macro_f1={rf_m_conf1['macro_f1']:.4f}, f1_stag={rf_m_conf1['f1_stag']:.4f}, f1_prog={rf_m_conf1['f1_prog']:.4f}")

        gb_rf_agree_conf1 = np.mean(gb_pred_conf1 == rf_pred_conf1)
        print(f"\n    GB-RF agreement on conf=1: {gb_rf_agree_conf1*100:.1f}%")
        print(f"    GB agrees with silver MV: {np.mean(gb_pred_conf1 == y_conf1)*100:.1f}%")
        print(f"    RF agrees with silver MV: {np.mean(rf_pred_conf1 == y_conf1)*100:.1f}%")

        results[seed] = {
            "conf2_test": {"n": len(y_test_conf2), "gb": gb_m_conf2, "rf": rf_m_conf2},
            "conf1": {"n": len(y_conf1), "gb": gb_m_conf1, "rf": rf_m_conf1,
                      "stag_count": int(sum(y_conf1 == 0)), "prog_count": int(sum(y_conf1 == 1)),
                      "gb_rf_agree": round(float(gb_rf_agree_conf1), 4),
                      "gb_mv_agree": round(float(np.mean(gb_pred_conf1 == y_conf1)), 4),
                      "rf_mv_agree": round(float(np.mean(rf_pred_conf1 == y_conf1)), 4)},
        }

    # ================================================================
    # 5. Aggregate multi-seed results
    # ================================================================
    print("\n" + "=" * 90)
    print("E10 MULTI-SEED AGGREGATE")
    print("=" * 90)

    for subset_key, subset_name in [("conf2_test", "conf≥2 test"), ("conf1", "conf=1")]:
        gb_f1s = [results[s][subset_key]["gb"]["macro_f1"] for s in [42, 123, 456]]
        rf_f1s = [results[s][subset_key]["rf"]["macro_f1"] for s in [42, 123, 456]]
        gb_stag_f1s = [results[s][subset_key]["gb"]["f1_stag"] for s in [42, 123, 456]]
        rf_stag_f1s = [results[s][subset_key]["rf"]["f1_stag"] for s in [42, 123, 456]]
        gb_prog_f1s = [results[s][subset_key]["gb"]["f1_prog"] for s in [42, 123, 456]]
        rf_prog_f1s = [results[s][subset_key]["rf"]["f1_prog"] for s in [42, 123, 456]]

        n = results[42][subset_key]["n"]

        print(f"\n  {subset_name} (n={n}):")
        print(f"    GB macro_f1: {np.mean(gb_f1s):.4f} ± {np.std(gb_f1s, ddof=1):.4f}")
        print(f"    RF macro_f1: {np.mean(rf_f1s):.4f} ± {np.std(rf_f1s, ddof=1):.4f}")
        print(f"    GB f1_stag:  {np.mean(gb_stag_f1s):.4f} ± {np.std(gb_stag_f1s, ddof=1):.4f}")
        print(f"    RF f1_stag:  {np.mean(rf_stag_f1s):.4f} ± {np.std(rf_stag_f1s, ddof=1):.4f}")
        print(f"    GB f1_prog:  {np.mean(gb_prog_f1s):.4f} ± {np.std(gb_prog_f1s, ddof=1):.4f}")
        print(f"    RF f1_prog:  {np.mean(rf_prog_f1s):.4f} ± {np.std(rf_prog_f1s, ddof=1):.4f}")

    # Paired t-test: GB conf=1 vs GB conf≥2
    gb_conf1 = [results[s]["conf1"]["gb"]["macro_f1"] for s in [42, 123, 456]]
    gb_conf2 = [results[s]["conf2_test"]["gb"]["macro_f1"] for s in [42, 123, 456]]
    rf_conf1 = [results[s]["conf1"]["rf"]["macro_f1"] for s in [42, 123, 456]]
    rf_conf2 = [results[s]["conf2_test"]["rf"]["macro_f1"] for s in [42, 123, 456]]

    print(f"\n  Paired tests (conf≥2 test vs conf=1):")
    for model, c2, c1 in [("GB", gb_conf2, gb_conf1), ("RF", rf_conf2, rf_conf1)]:
        delta = np.mean(c2) - np.mean(c1)
        if np.std(np.array(c2) - np.array(c1), ddof=1) > 0:
            t, p = stats.ttest_rel(c2, c1)
            perm_p = permutation_test(c2, c1, paired=True)
        else:
            t, p, perm_p = 0.0, 1.0, 1.0
        d = paired_cohens_d(c2, c1)
        sig = "***" if p < 0.001 else "**" if p < 0.01 else "*" if p < 0.05 else "ns"
        print(f"    {model}: Δ(conf≥2 - conf=1) = {delta:+.4f}, t={t:.3f}, p={p:.4f}, perm_p={perm_p:.4f}, d={d:.2f} ({sig})")

    # Paired t-test: GB vs RF on conf=1
    print(f"\n  GB vs RF on conf=1:")
    delta = np.mean(gb_conf1) - np.mean(rf_conf1)
    if np.std(np.array(gb_conf1) - np.array(rf_conf1), ddof=1) > 0:
        t, p = stats.ttest_rel(gb_conf1, rf_conf1)
        perm_p = permutation_test(gb_conf1, rf_conf1, paired=True)
    else:
        t, p, perm_p = 0.0, 1.0, 1.0
    d = paired_cohens_d(gb_conf1, rf_conf1)
    sig = "***" if p < 0.001 else "**" if p < 0.01 else "*" if p < 0.05 else "ns"
    print(f"    Δ(GB - RF) = {delta:+.4f}, t={t:.3f}, p={p:.4f}, perm_p={perm_p:.4f}, d={d:.2f} ({sig})")

    return results


if __name__ == "__main__":
    e9_results = run_e9()
    e10_results = run_e10()

    output = {"e9": e9_results, "e10": {str(k): v for k, v in e10_results.items()}}
    out_path = BASE / "artifacts" / "e9_e10_results.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2, default=str)
    print(f"\nResults saved: {out_path}")
