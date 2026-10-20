#!/usr/bin/env python3
"""Paired bootstrap test -- Table 2 exact scope.

3 comparisons:
1. RF vs Probe in-domain (SWE conf>=2 test, N=1,824)
2. GB vs Probe zero-shot cross-agent (OH conf>=2 test, N=6,122)
3. GB vs Probe fine-tuned cross-agent (OH conf>=2 test, N=6,122)
"""

import json
import re
import sys
import datetime
from collections import Counter
from difflib import SequenceMatcher
from pathlib import Path

import numpy as np
import torch
from torch.utils.data import DataLoader
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import f1_score

sys.path.insert(0, str(Path(__file__).parent))
from probe_model import ProgressProbe, WindowDataset, collate_fn

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
        1 for _, t in observations if re.search(r"exit code [1-9]|returned non-zero|command not found", t)
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
        for line in f:
            rec = json.loads(line)
            tid = f"{rec['instance_id']}__{rec.get('model_name', 'unknown')}__r0"
            index[tid] = rec["trajectory"]
    return index


def extract_features_batch(windows, traj_index):
    X = np.zeros((len(windows), 30), dtype=np.float32)
    y = np.zeros(len(windows), dtype=int)
    for i, w in enumerate(windows):
        tid = w["trajectory_id"]
        traj = traj_index.get(tid)
        if traj is None:
            continue
        si = w["step_indices"]
        steps = [traj[j] for j in si if j < len(traj)]
        X[i] = extract_features(steps, w.get("short_trajectory", False))
        y[i] = w["majority_label"]
    return X, y


def paired_bootstrap(y_true, preds_a, preds_b, n_bootstrap=10000, seed=42):
    rng = np.random.RandomState(seed)
    n = len(y_true)

    f1_a = f1_score(y_true, preds_a, average="macro", zero_division=0)
    f1_b = f1_score(y_true, preds_b, average="macro", zero_division=0)
    observed_delta = f1_a - f1_b

    deltas = []
    for _ in range(n_bootstrap):
        idx = rng.choice(n, size=n, replace=True)
        y_b = y_true[idx]
        if len(np.unique(y_b)) < 2:
            continue
        d_a = f1_score(y_b, preds_a[idx], average="macro", zero_division=0)
        d_b = f1_score(y_b, preds_b[idx], average="macro", zero_division=0)
        deltas.append(d_a - d_b)

    deltas = np.array(deltas)
    ci_lower = float(np.percentile(deltas, 2.5))
    ci_upper = float(np.percentile(deltas, 97.5))
    p_value = float(np.mean(deltas <= 0)) if observed_delta > 0 else float(np.mean(deltas >= 0))

    return {
        "f1_a": round(f1_a, 4),
        "f1_b": round(f1_b, 4),
        "delta_pp": round(observed_delta * 100, 2),
        "ci_lower_pp": round(ci_lower * 100, 2),
        "ci_upper_pp": round(ci_upper * 100, 2),
        "p_value": p_value,
        "n_valid_bootstraps": len(deltas),
    }


@torch.no_grad()
def probe_predict(model, embeddings, labels, device="cpu", batch_size=64):
    ds = WindowDataset(embeddings, labels)
    loader = DataLoader(ds, batch_size=batch_size, collate_fn=collate_fn)
    all_preds = []
    for padded, _, lengths in loader:
        logits = model(padded.to(device), lengths)
        preds = (torch.sigmoid(logits) >= 0.5).long().cpu()
        all_preds.extend(preds.tolist())
    return np.array(all_preds)


def load_probe(ckpt_path, device="cpu"):
    ckpt = torch.load(ckpt_path, map_location="cpu", weights_only=False)
    model = ProgressProbe(
        embed_dim=ckpt["embed_dim"],
        hidden_size=ckpt["hidden_size"],
        num_layers=ckpt["num_layers"],
        dropout=ckpt.get("dropout", 0.1),
    )
    model.load_state_dict(ckpt["model_state_dict"])
    model = model.to(device)
    model.eval()
    return model


def main():
    data_dir = PROJECT / "data"

    # ==========================================================
    # STEP 1: Load SWE-Agent data
    # ==========================================================
    print("Loading SWE-Agent trajectories...")
    swa_traj = build_trajectory_index(data_dir / "swe_agent_trajectories_5000.jsonl")
    print(f"  {len(swa_traj)} trajectories")

    print("Loading SWE-Agent windows...")
    all_windows = []
    with open(data_dir / "windows_labeled.jsonl") as f:
        for line in f:
            all_windows.append(json.loads(line))
    non_abstain = [w for w in all_windows if w.get("majority_label", -1) != -1]
    print(f"  {len(all_windows)} total, {len(non_abstain)} non-abstain")

    with open(PROJECT / "checkpoints" / "split_info.json") as f:
        split = json.load(f)
    keep_indices = split.get("keep_indices")
    train_idx = split["train_indices"]
    val_idx = split["val_indices"]
    test_idx = split["test_indices"]

    windows_conf2 = [non_abstain[i] for i in keep_indices] if keep_indices else non_abstain
    print(f"  Conf>=2: {len(windows_conf2)}, Train={len(train_idx)}, Val={len(val_idx)}, Test={len(test_idx)}")

    # ==========================================================
    # STEP 2: Extract SWE structural features
    # ==========================================================
    print("Extracting SWE structural features...")
    X_swe, y_swe = extract_features_batch(windows_conf2, swa_traj)

    X_train = X_swe[train_idx]
    y_train = y_swe[train_idx]
    X_test_swe = X_swe[test_idx]
    y_test_swe = y_swe[test_idx]

    n_test_swe = len(test_idx)
    swe_stag = int(np.sum(y_test_swe == 0))
    swe_prog = int(np.sum(y_test_swe == 1))
    print(f"  Test: N={n_test_swe} (stag={swe_stag}, prog={swe_prog})")

    # ==========================================================
    # STEP 3: Comparison 1 — RF vs Probe in-domain
    # ==========================================================
    print("\n=== Comparison 1: RF vs Probe (SWE in-domain) ===")

    print("Training RF (n_estimators=100, max_depth=10)...")
    rf = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42, n_jobs=-1)
    rf.fit(X_train, y_train)
    rf_preds = rf.predict(X_test_swe)
    print(f"  RF macro-F1: {f1_score(y_test_swe, rf_preds, average='macro'):.4f}")

    print("Loading SWE embeddings...")
    swe_emb = torch.load(data_dir / "embeddings.pt", map_location="cpu", weights_only=False)
    all_embs = swe_emb["embeddings"]
    all_labs = swe_emb["labels"]
    conf2_embs = [all_embs[i] for i in keep_indices]
    conf2_labs = [all_labs[i] for i in keep_indices]
    test_embs_swe = [conf2_embs[i] for i in test_idx]
    test_labs_swe = [conf2_labs[i] for i in test_idx]

    print("Loading probe (checkpoints/best_model.pt)...")
    probe_swe = load_probe(PROJECT / "checkpoints" / "best_model.pt")
    probe_preds_swe = probe_predict(probe_swe, test_embs_swe, test_labs_swe)
    print(f"  Probe macro-F1: {f1_score(y_test_swe, probe_preds_swe, average='macro'):.4f}")
    del probe_swe, swe_emb, all_embs, all_labs, conf2_embs, conf2_labs

    print("Paired bootstrap (10K)...")
    y_swe_np = np.array(y_test_swe)
    rf_np = np.array(rf_preds)
    bs1 = paired_bootstrap(y_swe_np, rf_np, probe_preds_swe, n_bootstrap=10000, seed=42)
    print(f"  RF={bs1['f1_a']}, Probe={bs1['f1_b']}, delta={bs1['delta_pp']:+.2f}pp, "
          f"CI=[{bs1['ci_lower_pp']:.2f},{bs1['ci_upper_pp']:.2f}], p={bs1['p_value']}")

    # ==========================================================
    # STEP 4: Load OH data
    # ==========================================================
    print("\n=== Loading OH data ===")

    oh_emb_data = torch.load(OH_DIR / "embeddings_fixed_conf2.pt", map_location="cpu", weights_only=False)
    oh_embs = oh_emb_data["embeddings"]
    oh_labs = oh_emb_data["labels"]
    oh_tids = oh_emb_data["trajectory_ids"]
    oh_step_indices = oh_emb_data["step_indices_list"]
    print(f"  OH conf>=2: {len(oh_embs)} windows")

    ft_data = torch.load(PROJECT / "checkpoints_oh_fixed_ft" / "test_preds.pt", map_location="cpu", weights_only=False)
    oh_test_idx = ft_data["test_idx"]
    oh_test_labels_list = ft_data["test_labels"]
    oh_ft_preds_list = ft_data["test_preds"]
    print(f"  OH test split: N={len(oh_test_idx)}")

    print("Loading OH trajectories...")
    oh_traj = build_trajectory_index(OH_DIR / "openhands_trajectories.jsonl")
    print(f"  {len(oh_traj)} trajectories")

    # ==========================================================
    # STEP 5: Extract OH structural features for test split
    # ==========================================================
    print("Extracting OH test structural features...")
    oh_test_windows = []
    for idx in oh_test_idx:
        oh_test_windows.append({
            "trajectory_id": oh_tids[idx],
            "step_indices": oh_step_indices[idx],
            "majority_label": oh_labs[idx],
            "short_trajectory": False,
        })

    X_oh_test, y_oh_test = extract_features_batch(oh_test_windows, oh_traj)
    oh_stag = int(np.sum(y_oh_test == 0))
    oh_prog = int(np.sum(y_oh_test == 1))
    print(f"  OH test: N={len(y_oh_test)} (stag={oh_stag}, prog={oh_prog})")

    # ==========================================================
    # STEP 6: Train GB on SWE, predict on OH test
    # ==========================================================
    print("\nTraining GB (n_estimators=200, lr=0.05, max_depth=5) on SWE...")
    gb = GradientBoostingClassifier(n_estimators=200, learning_rate=0.05, max_depth=5, random_state=42)
    gb.fit(X_train, y_train)
    gb_oh_preds = gb.predict(X_oh_test)
    gb_oh_f1 = f1_score(y_oh_test, gb_oh_preds, average="macro")
    print(f"  GB on OH test split: macro-F1 = {gb_oh_f1:.4f}")
    print(f"  Note: Table 2 reports 0.9674 on all OH (N=150,652); this is conf>=2 test split (N={len(y_oh_test)})")

    # ==========================================================
    # STEP 7: Comparison 2 — GB vs Probe zero-shot (OH)
    # ==========================================================
    print("\n=== Comparison 2: GB vs Probe zero-shot (OH test) ===")

    print("Loading SWE probe (checkpoints_full/best_model.pt) for zero-shot...")
    zs_probe = load_probe(PROJECT / "checkpoints_full" / "best_model.pt")
    oh_test_embs = [oh_embs[i] for i in oh_test_idx]
    oh_test_labs_for_ds = [oh_labs[i] for i in oh_test_idx]
    zs_preds = probe_predict(zs_probe, oh_test_embs, oh_test_labs_for_ds)
    zs_f1 = f1_score(y_oh_test, zs_preds, average="macro")
    print(f"  Probe zero-shot: macro-F1 = {zs_f1:.4f}")
    del zs_probe

    print("Paired bootstrap (10K)...")
    y_oh_np = np.array(y_oh_test)
    gb_oh_np = np.array(gb_oh_preds)
    bs2 = paired_bootstrap(y_oh_np, gb_oh_np, zs_preds, n_bootstrap=10000, seed=42)
    print(f"  GB={bs2['f1_a']}, Probe-ZS={bs2['f1_b']}, delta={bs2['delta_pp']:+.2f}pp, "
          f"CI=[{bs2['ci_lower_pp']:.2f},{bs2['ci_upper_pp']:.2f}], p={bs2['p_value']}")

    # ==========================================================
    # STEP 8: Comparison 3 — GB vs Probe fine-tuned (OH)
    # ==========================================================
    print("\n=== Comparison 3: GB vs Probe fine-tuned (OH test) ===")

    ft_preds_np = np.array(oh_ft_preds_list)
    ft_f1 = f1_score(y_oh_test, ft_preds_np, average="macro")
    print(f"  Probe fine-tuned: macro-F1 = {ft_f1:.4f}")

    print("Paired bootstrap (10K)...")
    bs3 = paired_bootstrap(y_oh_np, gb_oh_np, ft_preds_np, n_bootstrap=10000, seed=42)
    print(f"  GB={bs3['f1_a']}, Probe-FT={bs3['f1_b']}, delta={bs3['delta_pp']:+.2f}pp, "
          f"CI=[{bs3['ci_lower_pp']:.2f},{bs3['ci_upper_pp']:.2f}], p={bs3['p_value']}")

    # ==========================================================
    # OUTPUT
    # ==========================================================
    results = {
        "comparison_1_rf_vs_probe_indomain": {
            "scope": "SWE-Agent conf>=2 test split",
            "N": n_test_swe,
            "class_dist": {"stagnation": swe_stag, "progress": swe_prog},
            "model_a": "Structural RF",
            "model_b": "ProgressProbe (GRU)",
            "f1_a": bs1["f1_a"],
            "f1_b": bs1["f1_b"],
            "delta_pp": bs1["delta_pp"],
            "ci_95": [bs1["ci_lower_pp"], bs1["ci_upper_pp"]],
            "p_value": bs1["p_value"],
            "table2_ref": {"f1_a": 0.9951, "f1_b": 0.9055},
        },
        "comparison_2_gb_vs_probe_zeroshot_oh": {
            "scope": "OH conf>=2 test split",
            "scope_note": "Table 2 GB=0.9674 is on all 150,652 OH windows; this bootstrap uses conf>=2 test split only. GB F1 on this subset differs from Table 2.",
            "N": len(y_oh_test),
            "class_dist": {"stagnation": oh_stag, "progress": oh_prog},
            "model_a": "Structural GB",
            "model_b": "ProgressProbe zero-shot",
            "f1_a": bs2["f1_a"],
            "f1_b": bs2["f1_b"],
            "delta_pp": bs2["delta_pp"],
            "ci_95": [bs2["ci_lower_pp"], bs2["ci_upper_pp"]],
            "p_value": bs2["p_value"],
            "table2_ref": {"f1_a_all_oh": 0.9674, "f1_b": 0.598},
        },
        "comparison_3_gb_vs_probe_finetuned_oh": {
            "scope": "OH conf>=2 test split",
            "scope_note": "Same scope as comparison 2. GB retrained on same SWE data.",
            "N": len(y_oh_test),
            "class_dist": {"stagnation": oh_stag, "progress": oh_prog},
            "model_a": "Structural GB",
            "model_b": "ProgressProbe fine-tuned",
            "f1_a": bs3["f1_a"],
            "f1_b": bs3["f1_b"],
            "delta_pp": bs3["delta_pp"],
            "ci_95": [bs3["ci_lower_pp"], bs3["ci_upper_pp"]],
            "p_value": bs3["p_value"],
            "table2_ref": {"f1_a_all_oh": 0.9674, "f1_b": 0.976},
        },
        "metadata": {
            "n_bootstrap": 10000,
            "seed": 42,
            "timestamp": datetime.datetime.now().isoformat(),
            "note": "Paired bootstrap on Table 2 exact scope",
            "rf_hp": {"n_estimators": 100, "max_depth": 10},
            "gb_hp": {"n_estimators": 200, "learning_rate": 0.05, "max_depth": 5},
        },
    }

    out_path = PROJECT / "bootstrap_table2_matched.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to {out_path}")

    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    for k, v in results.items():
        if k == "metadata":
            continue
        print(f"\n{k}:")
        print(f"  Scope: {v['scope']}, N={v['N']}")
        print(f"  {v['model_a']}: F1={v['f1_a']}")
        print(f"  {v['model_b']}: F1={v['f1_b']}")
        print(f"  Delta: {v['delta_pp']:+.2f}pp")
        print(f"  95% CI: [{v['ci_95'][0]:.2f}, {v['ci_95'][1]:.2f}]")
        print(f"  p-value: {v['p_value']}")


if __name__ == "__main__":
    main()
