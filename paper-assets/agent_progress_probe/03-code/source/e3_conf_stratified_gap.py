#!/usr/bin/env python3
"""E3: Conf-stratified Silver-Gold Gap Decomposition.

Gold Set B (N=505, ≥2 annotators agreed) stratified by silver LF confidence.
Per-stratum metrics: MV-gold agreement, GB gold F1, silver-gold gap, stagnation prevalence.
"""

import csv
import json
import re
import sys
from collections import Counter
from difflib import SequenceMatcher
from pathlib import Path

import numpy as np
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import f1_score, accuracy_score
from sklearn.model_selection import StratifiedKFold

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
    # ================================================================
    # 1. Gold Set B
    # ================================================================
    gold_wids, gold_labels = [], []
    with open(GOLD_DIR / "gold_2plus_agreed_B.csv") as f:
        for row in csv.DictReader(f):
            gold_wids.append(row["window_id"])
            gold_labels.append(int(row["gold_label"]))
    n_gold = len(gold_wids)
    print(f"Gold Set B: N={n_gold} (stag={sum(1 for l in gold_labels if l==0)}, prog={sum(1 for l in gold_labels if l==1)})")

    # ================================================================
    # 2. Silver conf from annotation CSVs
    # ================================================================
    wid_to_silver_conf = {}
    for fname in ["annotation_unknown_2026-05-15.csv", "annotation_unknown_2026-05-15_batch2.csv",
                   "annotation_unknown_2026-05-15_batch3a.csv", "annotation_unknown_2026-05-15_batch3b.csv"]:
        p = GOLD_DIR / fname
        if not p.exists():
            continue
        with open(p) as f:
            for r in csv.DictReader(f):
                wid_to_silver_conf[f"{r['trajectory_id']}__w{r['window_idx']}"] = int(r['confidence'])
    print(f"Silver conf matched: {sum(1 for w in gold_wids if w in wid_to_silver_conf)}/{n_gold}")

    # ================================================================
    # 3. Silver MV labels from windows_labeled.jsonl
    # ================================================================
    print("Loading windows_labeled.jsonl ...")
    all_windows = []
    with open(DATA_DIR / "windows_labeled.jsonl") as f:
        for line in f:
            if line.strip():
                all_windows.append(json.loads(line))
    non_abstain = [w for w in all_windows if w.get("majority_label", -1) != -1]
    wid_to_mv = {window_id(w): w["majority_label"] for w in non_abstain}
    wid_to_conf = {window_id(w): w.get("confidence", 0) for w in non_abstain}
    wid_to_noabs_idx = {window_id(w): i for i, w in enumerate(non_abstain)}
    print(f"  Non-abstain: {len(non_abstain)}")

    # Add abstain windows
    for w in all_windows:
        wid = window_id(w)
        if wid not in wid_to_mv:
            wid_to_mv[wid] = w.get("majority_label", -1)

    n_swe_matched = sum(1 for w in gold_wids if w in wid_to_noabs_idx)
    n_oh = sum(1 for w in gold_wids if "openhands" in w)
    print(f"  SWE gold matched: {n_swe_matched}, OH gold (no local data): {n_oh}")

    # ================================================================
    # 4. Structural features & GB model
    # ================================================================
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
    print(f"  Features: {all_features.shape}")

    # Train GB on conf>=2 SWE windows, excluding gold
    conf2_mask = np.array([w.get("confidence", 0) >= 2 for w in non_abstain])
    gold_set = set(gold_wids)
    not_gold_mask = np.array([window_id(w) not in gold_set for w in non_abstain])
    train_mask = conf2_mask & not_gold_mask
    X_train = all_features[train_mask]
    y_train = all_mv_labels[train_mask]
    print(f"  GB train: {len(X_train)} (conf>=2, gold excluded)")

    gb = GradientBoostingClassifier(n_estimators=200, learning_rate=0.05, max_depth=5, random_state=42)
    gb.fit(X_train, y_train)

    # GB predictions for gold SWE windows
    gold_gb_preds = {}
    for wid in gold_wids:
        idx = wid_to_noabs_idx.get(wid)
        if idx is not None:
            gold_gb_preds[wid] = gb.predict(all_features[idx:idx+1])[0]
    print(f"  GB gold predictions: {len(gold_gb_preds)}/{n_gold}")

    # GB silver F1 via 5-fold CV on conf>=2 (excluding gold)
    print("  Computing GB silver F1 (5-fold CV on conf>=2) ...")
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    cv_preds = np.zeros(len(y_train), dtype=int)
    for fold_train, fold_test in cv.split(X_train, y_train):
        clf = GradientBoostingClassifier(n_estimators=200, learning_rate=0.05, max_depth=5, random_state=42)
        clf.fit(X_train[fold_train], y_train[fold_train])
        cv_preds[fold_test] = clf.predict(X_train[fold_test])
    gb_silver_f1 = f1_score(y_train, cv_preds, average="macro")
    print(f"  GB silver F1 (5-fold CV): {gb_silver_f1:.4f}")

    # Per-conf silver F1 via CV
    train_conf_levels = np.array([non_abstain[i].get("confidence", 0)
                                  for i, m in enumerate(train_mask) if m])
    gb_silver_f1_by_conf = {}
    for c in [2, 3]:
        mask_c = train_conf_levels == c
        if mask_c.sum() > 10 and len(set(y_train[mask_c])) > 1:
            gb_silver_f1_by_conf[c] = f1_score(y_train[mask_c], cv_preds[mask_c], average="macro")
            print(f"    conf={c}: {gb_silver_f1_by_conf[c]:.4f} (n={mask_c.sum()})")

    # Silver stagnation rates by conf (from all SWE non-abstain)
    silver_stag_by_conf = {}
    for w in non_abstain:
        c = w.get("confidence", 0)
        silver_stag_by_conf.setdefault(c, [0, 0])
        silver_stag_by_conf[c][1] += 1
        if w["majority_label"] == 0:
            silver_stag_by_conf[c][0] += 1
    overall_silver_stag = sum(v[0] for v in silver_stag_by_conf.values()) / sum(v[1] for v in silver_stag_by_conf.values())

    # ================================================================
    # 5. Stratified analysis
    # ================================================================
    print("\n" + "=" * 90)
    print("E3: CONF-STRATIFIED SILVER-GOLD GAP — Gold Set B (N=505)")
    print("=" * 90)

    conf_groups = {0: [], 1: [], 2: [], 3: []}
    for wid, gl in zip(gold_wids, gold_labels):
        conf = wid_to_silver_conf.get(wid, -1)
        if conf in conf_groups:
            conf_groups[conf].append((wid, gl))

    hdr = f"{'Conf':>4} | {'N':>4} | {'MV-Gold Agree':>14} | {'GB Gold F1':>10} | {'GB Silv F1':>10} | {'Gap':>7} | {'Gold Stag%':>10} | {'Silv Stag%':>10}"
    print(hdr)
    print("-" * len(hdr))

    results = {}
    for conf in [0, 1, 2, 3]:
        group = conf_groups[conf]
        n = len(group)
        if n == 0:
            continue

        # MV-gold agreement
        mv_a = mv_t = 0
        for wid, gl in group:
            mv = wid_to_mv.get(wid)
            if mv is not None and mv != -1:
                mv_t += 1
                if mv == gl:
                    mv_a += 1
        mv_rate = mv_a / mv_t if mv_t > 0 else None

        # GB gold F1
        gb_g, gb_p = [], []
        for wid, gl in group:
            if wid in gold_gb_preds:
                gb_g.append(gl)
                gb_p.append(gold_gb_preds[wid])
        if len(gb_g) > 1 and len(set(gb_g)) > 1:
            gb_f1 = f1_score(gb_g, gb_p, average="macro")
        elif len(gb_g) > 0:
            gb_f1 = accuracy_score(gb_g, gb_p)
        else:
            gb_f1 = None

        # Silver F1 reference
        sf1 = gb_silver_f1_by_conf.get(conf, gb_silver_f1)
        gap = (sf1 - gb_f1) if gb_f1 is not None and sf1 is not None else None

        # Stagnation
        gold_stag = sum(1 for _, gl in group if gl == 0)
        ss = silver_stag_by_conf.get(conf, [0, 1])
        silver_sr = ss[0] / max(ss[1], 1)

        mv_str = f"{mv_a}/{mv_t}={mv_rate:.1%}" if mv_rate is not None else "N/A"
        gb_str = f"{gb_f1:.4f}" if gb_f1 is not None else "—"
        sf_str = f"{sf1:.4f}" if sf1 is not None else "—"
        gap_str = f"{gap:+.4f}" if gap is not None else "—"

        print(f"{conf:>4} | {n:>4} | {mv_str:>14} | {gb_str:>10} | {sf_str:>10} | {gap_str:>7} | {gold_stag/n:>9.1%} | {silver_sr:>9.1%}")

        results[f"conf_{conf}"] = {
            "n": n,
            "mv_gold": {"agree": mv_a, "total": mv_t, "rate": round(mv_rate, 4) if mv_rate is not None else None},
            "gb_gold_f1": round(gb_f1, 4) if gb_f1 is not None else None,
            "gb_gold_n": len(gb_g),
            "gb_silver_f1": round(sf1, 4) if sf1 is not None else None,
            "gap": round(gap, 4) if gap is not None else None,
            "gold_stag_rate": round(gold_stag / n, 4),
            "silver_stag_rate": round(silver_sr, 4),
        }

    # Aggregates
    print("-" * len(hdr))
    for label, confs in [("≥2", [2, 3]), ("≥1", [1, 2, 3]), ("All", [0, 1, 2, 3])]:
        combined = []
        for c in confs:
            combined.extend(conf_groups.get(c, []))
        if not combined:
            continue
        n = len(combined)
        mv_a = mv_t = 0
        gb_g, gb_p = [], []
        for wid, gl in combined:
            mv = wid_to_mv.get(wid)
            if mv is not None and mv != -1:
                mv_t += 1
                if mv == gl:
                    mv_a += 1
            if wid in gold_gb_preds:
                gb_g.append(gl)
                gb_p.append(gold_gb_preds[wid])
        mv_r = mv_a / mv_t if mv_t > 0 else None
        gb_f1 = f1_score(gb_g, gb_p, average="macro") if len(gb_g) > 1 and len(set(gb_g)) > 1 else None
        stag = sum(1 for _, gl in combined if gl == 0)

        mv_str = f"{mv_a}/{mv_t}={mv_r:.1%}" if mv_r is not None else "N/A"
        gb_str = f"{gb_f1:.4f}" if gb_f1 is not None else "—"
        print(f"{label:>4} | {n:>4} | {mv_str:>14} | {gb_str:>10} | {'':>10} | {'':>7} | {stag/n:>9.1%} |")

        rkey = f"conf_{label.replace('≥','ge')}"
        results[rkey] = {
            "n": n,
            "mv_gold": {"agree": mv_a, "total": mv_t, "rate": round(mv_r, 4) if mv_r else None},
            "gb_gold_f1": round(gb_f1, 4) if gb_f1 is not None else None,
            "gb_gold_n": len(gb_g),
            "gold_stag_rate": round(stag / n, 4),
        }

    # ================================================================
    # 6. Key findings
    # ================================================================
    print("\n" + "=" * 90)
    print("KEY FINDINGS")
    print("=" * 90)

    rge2 = results.get("conf_ge2", {})
    r2 = results.get("conf_2", {})
    r3 = results.get("conf_3", {})
    r1 = results.get("conf_1", {})

    rate_ge2 = rge2.get("mv_gold", {}).get("rate")
    if rate_ge2 is not None:
        verdict = "CONFIRMED" if rate_ge2 > 0.90 else "NOT MET"
        print(f"\n  conf≥2 MV-gold agreement: {rate_ge2:.1%} → {verdict} >90% target")
    if r3.get("mv_gold", {}).get("rate") is not None:
        print(f"  conf=3 MV-gold agreement: {r3['mv_gold']['rate']:.1%}")
    if r2.get("mv_gold", {}).get("rate") is not None:
        print(f"  conf=2 MV-gold agreement: {r2['mv_gold']['rate']:.1%}")
    if r1.get("mv_gold", {}).get("rate") is not None:
        print(f"  conf=1 MV-gold agreement: {r1['mv_gold']['rate']:.1%}")

    print(f"\n  Stagnation prevalence:")
    print(f"    Silver overall (SWE): {overall_silver_stag:.1%}")
    print(f"    Gold Set B overall: {sum(1 for l in gold_labels if l==0)/n_gold:.1%}")
    for c in [1, 2, 3]:
        rc = results.get(f"conf_{c}", {})
        if rc:
            print(f"    conf={c}: gold={rc['gold_stag_rate']:.1%}, silver={rc['silver_stag_rate']:.1%}")

    if rge2.get("gb_gold_f1") is not None:
        print(f"\n  GB gold F1 (conf≥2): {rge2['gb_gold_f1']:.4f} (n={rge2['gb_gold_n']})")
        print(f"  GB silver F1 (5-fold CV): {gb_silver_f1:.4f}")
        print(f"  Silver-gold gap overall: {gb_silver_f1 - rge2['gb_gold_f1']:+.4f}")

    print(f"\n  NOTE: {n_oh} OH gold windows lack local trajectory data → GB/MV analysis is SWE-only.")
    print(f"  Existing full-set eval (consensus_601): GB gold F1 = 0.7237 (N=584)")

    # ================================================================
    # 7. Save
    # ================================================================
    output = {
        "experiment": "E3_conf_stratified_gap",
        "gold_set": "B_2plus_agreed",
        "n_gold": n_gold,
        "n_swe_matched_gb": len(gold_gb_preds),
        "n_oh_no_local_data": n_oh,
        "gb_silver_f1_cv": round(gb_silver_f1, 4),
        "gb_silver_f1_by_conf": {str(k): round(v, 4) for k, v in gb_silver_f1_by_conf.items()},
        "silver_stag_rate_overall": round(overall_silver_stag, 4),
        "strata": results,
    }
    out_path = GOLD_DIR / "e3_conf_stratified_gap.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nSaved: {out_path}")


if __name__ == "__main__":
    main()
