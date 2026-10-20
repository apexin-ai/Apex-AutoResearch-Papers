#!/usr/bin/env python3
"""Paired bootstrap significance tests on gold set evaluation.

Recomputes per-window predictions for each model, then runs paired bootstrap
to test whether performance differences are statistically significant.
"""

import argparse
import csv
import json
import re
import sys
import warnings
from collections import Counter
from difflib import SequenceMatcher
from pathlib import Path

import numpy as np
import torch
import torch.nn as nn
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.metrics import f1_score
from sklearn.preprocessing import StandardScaler
from torch.utils.data import DataLoader

warnings.filterwarnings("ignore", category=UserWarning)

sys.path.insert(0, str(Path(__file__).parent))
from probe_model import ProgressProbe, WindowDataset, collate_fn


# ---------- structural feature extraction (from evaluate_gold_set.py) ----------

EDIT_CMDS = {"edit", "str_replace", "create", "insert"}
SEARCH_CMDS = {"search_dir", "search_file", "find_file", "find", "grep", "view"}
NAV_CMDS = {"open", "goto", "scroll_down", "scroll_up", "cd", "ls", "cat"}


def _extract_command(text):
    match = re.search(r"```\n?(.*?)```", text, re.DOTALL)
    return match.group(1).strip() if match else None


def _cmd_similarity(a, b):
    if a == b:
        return 1.0
    if not a or not b:
        return 0.0
    return SequenceMatcher(None, a, b).ratio()


def extract_structural_features(steps, is_short):
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
    for s, t in actions:
        cmd = _extract_command(t)
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
        sims = [_cmd_similarity(commands[i], commands[i + 1]) for i in range(n_cmds - 1)]
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


# ---------- data loading ----------

def load_windows_jsonl(path):
    windows = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                windows.append(json.loads(line))
    return windows


def build_trajectory_index(traj_path):
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


def window_id(w):
    return f"{w['trajectory_id']}__w{w['window_idx']}"


# ---------- per-window prediction collectors ----------

def get_mv_predictions(gold_wids, gold_labels, wid_to_window):
    wids, golds, preds = [], [], []
    for wid, gl in zip(gold_wids, gold_labels):
        w = wid_to_window.get(wid)
        if w is None:
            continue
        wids.append(wid)
        golds.append(gl)
        preds.append(w["majority_label"])
    return wids, np.array(golds), np.array(preds)


def get_structural_predictions(
    gold_wids, gold_labels, wid_to_noabs_idx,
    all_features, all_mv_labels, split_info, model_cls, model_kwargs,
):
    keep_indices = split_info.get("keep_indices")
    if keep_indices is not None:
        feat_subset = all_features[keep_indices]
        label_subset = np.array(all_mv_labels)[keep_indices]
    else:
        feat_subset = all_features
        label_subset = np.array(all_mv_labels)

    train_idx = split_info["train_indices"]

    # Exclude gold windows from training to prevent data leakage
    gold_noabs_set = {wid_to_noabs_idx[wid] for wid in gold_wids if wid in wid_to_noabs_idx}
    if keep_indices is not None:
        train_idx = [i for i in train_idx if keep_indices[i] not in gold_noabs_set]
    else:
        train_idx = [i for i in train_idx if i not in gold_noabs_set]

    X_train = feat_subset[train_idx]
    y_train = label_subset[train_idx]

    clf = model_cls(**model_kwargs)
    clf.fit(X_train, y_train)

    wids, golds, preds = [], [], []
    for wid, gl in zip(gold_wids, gold_labels):
        idx = wid_to_noabs_idx.get(wid)
        if idx is None:
            continue
        feat = all_features[idx].reshape(1, -1)
        pred = clf.predict(feat)[0]
        wids.append(wid)
        golds.append(gl)
        preds.append(pred)
    return wids, np.array(golds), np.array(preds)


@torch.no_grad()
def get_probe_predictions(gold_wids, gold_labels, wid_to_emb_idx, embeddings, ckpt_path, device):
    ckpt = torch.load(ckpt_path, map_location=device, weights_only=False)
    model = ProgressProbe(
        embed_dim=ckpt["embed_dim"],
        hidden_size=ckpt["hidden_size"],
        num_layers=ckpt["num_layers"],
    ).to(device)
    model.load_state_dict(ckpt["model_state_dict"])
    model.eval()

    ordered_wids = []
    ordered_golds = []
    ordered_embs = []
    for wid, gl in zip(gold_wids, gold_labels):
        idx = wid_to_emb_idx.get(wid)
        if idx is None:
            continue
        ordered_wids.append(wid)
        ordered_golds.append(gl)
        ordered_embs.append(embeddings[idx])

    if not ordered_embs:
        return [], np.array([]), np.array([])

    ds = WindowDataset(ordered_embs, ordered_golds)
    loader = DataLoader(ds, batch_size=64, collate_fn=collate_fn)

    all_preds = []
    for padded, labels, lengths in loader:
        logits = model(padded.to(device), lengths)
        preds = (torch.sigmoid(logits) >= 0.5).long().cpu().tolist()
        all_preds.extend(preds)

    return ordered_wids, np.array(ordered_golds), np.array(all_preds)


# ---------- bootstrap ----------

def macro_f1(y_true, y_pred):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        return f1_score(y_true, y_pred, average="macro", zero_division=0)


def paired_bootstrap(y_true, preds_a, preds_b, n_bootstrap=10000, seed=42):
    rng = np.random.RandomState(seed)
    n = len(y_true)
    observed_delta = macro_f1(y_true, preds_a) - macro_f1(y_true, preds_b)
    deltas = []
    for _ in range(n_bootstrap):
        idx = rng.choice(n, n, replace=True)
        delta = macro_f1(y_true[idx], preds_a[idx]) - macro_f1(y_true[idx], preds_b[idx])
        deltas.append(delta)
    deltas = np.array(deltas)
    ci_lo, ci_hi = np.percentile(deltas, [2.5, 97.5])
    p_value = float(np.mean(deltas <= 0) if observed_delta > 0 else np.mean(deltas >= 0))
    return observed_delta, ci_lo, ci_hi, p_value


# ---------- main ----------

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--gold_csv", type=str, required=True)
    parser.add_argument("--output", type=str, required=True)
    parser.add_argument("--data_dir", type=str, default="data")
    parser.add_argument("--checkpoint", type=str, default="checkpoints/best_model.pt")
    parser.add_argument("--twv_checkpoint", type=str, default="checkpoints_tlm_twv/best_model.pt")
    parser.add_argument("--split_info", type=str, default="checkpoints/split_info.json")
    parser.add_argument("--trajectories", type=str, default="data/swe_agent_trajectories_5000.jsonl")
    parser.add_argument("--oh_trajectories", type=str, default=None,
                        help="OpenHands trajectory JSONL for OH window features")
    parser.add_argument("--n_bootstrap", type=int, default=10000)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    base_dir = Path(__file__).parent
    data_dir = base_dir / args.data_dir
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Device: {device}")

    # --- load gold labels ---
    gold_wids, gold_labels = [], []
    with open(args.gold_csv) as f:
        reader = csv.DictReader(f)
        for row in reader:
            gold_wids.append(row["window_id"])
            gold_labels.append(int(row["gold_label"]))
    print(f"Gold labels: {len(gold_wids)}")

    # --- load windows ---
    all_windows = load_windows_jsonl(data_dir / "windows_labeled.jsonl")
    non_abstain = [w for w in all_windows if w.get("majority_label", -1) != -1]
    wid_to_window = {window_id(w): w for w in non_abstain}
    wid_to_noabs_idx = {window_id(w): i for i, w in enumerate(non_abstain)}

    # --- load embeddings ---
    emb_data = torch.load(data_dir / "embeddings.pt", map_location="cpu", weights_only=False)
    embeddings = emb_data["embeddings"]
    wid_to_emb_idx = {}
    for i, w in enumerate(non_abstain):
        if i < len(embeddings):
            wid_to_emb_idx[window_id(w)] = i

    # --- load split info ---
    with open(base_dir / args.split_info) as f:
        split_info = json.load(f)

    # --- build structural features ---
    print("Building structural features ...")
    traj_index = build_trajectory_index(str(base_dir / args.trajectories))
    print(f"  SWE trajectories: {len(traj_index)}")
    oh_traj_index = {}
    if args.oh_trajectories:
        oh_traj_index = build_trajectory_index(str(base_dir / args.oh_trajectories))
        print(f"  OH trajectories: {len(oh_traj_index)}")

    all_features, all_mv_labels = [], []
    n_swe, n_oh = 0, 0
    for w in non_abstain:
        row_idx = w.get("row_index", 0)
        step_indices = w["step_indices"]
        is_oh = "openhands" in w.get("trajectory_id", "")
        if is_oh and oh_traj_index:
            traj_steps = oh_traj_index.get(row_idx, [])
            n_oh += 1
        else:
            traj_steps = traj_index.get(row_idx, [])
            n_swe += 1
        window_steps = [
            traj_steps[si] if si < len(traj_steps) else {"role": "unknown", "text": ""}
            for si in step_indices
        ]
        all_features.append(extract_structural_features(window_steps, w.get("short_trajectory", False)))
        all_mv_labels.append(w["majority_label"])
    all_features = np.stack(all_features)
    print(f"  Feature matrix: {all_features.shape} (SWE={n_swe}, OH={n_oh})")

    # ====== collect per-window predictions ======
    print("Collecting MV predictions ...")
    mv_wids, mv_golds, mv_preds = get_mv_predictions(gold_wids, gold_labels, wid_to_window)
    print(f"  MV: N={len(mv_wids)}, macro-F1={macro_f1(mv_golds, mv_preds):.4f}")

    print("Collecting GB predictions ...")
    gb_wids, gb_golds, gb_preds = get_structural_predictions(
        gold_wids, gold_labels, wid_to_noabs_idx,
        all_features, all_mv_labels, split_info,
        GradientBoostingClassifier,
        {"n_estimators": 200, "learning_rate": 0.05, "max_depth": 5, "random_state": 42},
    )
    print(f"  GB: N={len(gb_wids)}, macro-F1={macro_f1(gb_golds, gb_preds):.4f}")

    print("Collecting RF predictions ...")
    rf_wids, rf_golds, rf_preds = get_structural_predictions(
        gold_wids, gold_labels, wid_to_noabs_idx,
        all_features, all_mv_labels, split_info,
        RandomForestClassifier,
        {"n_estimators": 100, "max_depth": 10, "random_state": 42, "n_jobs": -1},
    )
    print(f"  RF: N={len(rf_wids)}, macro-F1={macro_f1(rf_golds, rf_preds):.4f}")

    print("Collecting GRU Probe predictions ...")
    probe_wids, probe_golds, probe_preds = get_probe_predictions(
        gold_wids, gold_labels, wid_to_emb_idx, embeddings,
        str(base_dir / args.checkpoint), device,
    )
    print(f"  GRU Probe: N={len(probe_wids)}, macro-F1={macro_f1(probe_golds, probe_preds):.4f}")

    print("Collecting TWV Probe predictions ...")
    twv_emb_data = torch.load(base_dir / "data_tlm_twv" / "embeddings.pt", map_location="cpu", weights_only=False)
    twv_embeddings = twv_emb_data["embeddings"]
    twv_labels_path = data_dir / "windows_tlm_labels.jsonl"
    twv_all_windows = load_windows_jsonl(str(twv_labels_path))
    twv_non_abstain = [w for w in twv_all_windows if w.get("mv_label", -1) != -1]
    twv_wid_to_emb_idx = {}
    if len(twv_embeddings) == len(twv_non_abstain):
        for i, w in enumerate(twv_non_abstain):
            twv_wid_to_emb_idx[f"{w['trajectory_id']}__w{w['window_idx']}"] = i
    else:
        for i, w in enumerate(non_abstain):
            if i < len(twv_embeddings):
                twv_wid_to_emb_idx[window_id(w)] = i
    twv_probe_wids, twv_probe_golds, twv_probe_preds = get_probe_predictions(
        gold_wids, gold_labels, twv_wid_to_emb_idx, twv_embeddings,
        str(base_dir / args.twv_checkpoint), device,
    )
    print(f"  TWV Probe: N={len(twv_probe_wids)}, macro-F1={macro_f1(twv_probe_golds, twv_probe_preds):.4f}")

    # ====== paired bootstrap tests ======
    results = {"n_bootstrap": args.n_bootstrap, "seed": args.seed, "tests": {}}

    def run_test(name, wids_a, golds_a, preds_a, wids_b, golds_b, preds_b, label_a, label_b):
        set_a = set(wids_a)
        set_b = set(wids_b)
        shared = sorted(set_a & set_b)
        idx_a = {wid: i for i, wid in enumerate(wids_a)}
        idx_b = {wid: i for i, wid in enumerate(wids_b)}
        shared_golds = np.array([golds_a[idx_a[wid]] for wid in shared])
        shared_preds_a = np.array([preds_a[idx_a[wid]] for wid in shared])
        shared_preds_b = np.array([preds_b[idx_b[wid]] for wid in shared])

        f1_a = macro_f1(shared_golds, shared_preds_a)
        f1_b = macro_f1(shared_golds, shared_preds_b)
        print(f"\n--- {name} ---")
        print(f"  Shared windows: {len(shared)}")
        print(f"  {label_a} macro-F1 (on shared): {f1_a:.4f}")
        print(f"  {label_b} macro-F1 (on shared): {f1_b:.4f}")

        delta, ci_lo, ci_hi, p = paired_bootstrap(
            shared_golds, shared_preds_a, shared_preds_b,
            n_bootstrap=args.n_bootstrap, seed=args.seed,
        )
        sig = "YES" if p < 0.05 else "NO"
        print(f"  Observed Δ ({label_a} - {label_b}): {delta:+.4f}")
        print(f"  95% CI: [{ci_lo:+.4f}, {ci_hi:+.4f}]")
        print(f"  p-value: {p:.4f}  (significant at α=0.05: {sig})")

        results["tests"][name] = {
            "model_a": label_a,
            "model_b": label_b,
            "n_samples": len(shared),
            "n_bootstrap": args.n_bootstrap,
            "f1_a_on_shared": round(f1_a, 6),
            "f1_b_on_shared": round(f1_b, 6),
            "observed_delta": round(delta, 6),
            "ci_95_lo": round(ci_lo, 6),
            "ci_95_hi": round(ci_hi, 6),
            "p_value": round(p, 6),
            "significant_005": p < 0.05,
        }

    print(f"\n{'='*60}")
    print(f"Paired Bootstrap Tests (N_boot={args.n_bootstrap}, seed={args.seed})")
    print(f"{'='*60}")

    # Test 1: GB vs MV Labels (N=195)
    run_test("gb_vs_mv", gb_wids, gb_golds, gb_preds, mv_wids, mv_golds, mv_preds,
             "Structural GB", "MV Labels")

    # Test 2: GB vs GRU Probe (shared windows only)
    run_test("gb_vs_gru_probe", gb_wids, gb_golds, gb_preds, probe_wids, probe_golds, probe_preds,
             "Structural GB", "GRU Probe")

    # Test 3: RF vs GB (N=195)
    run_test("rf_vs_gb", rf_wids, rf_golds, rf_preds, gb_wids, gb_golds, gb_preds,
             "Structural RF", "Structural GB")

    # Test 4 (bonus): TWV Probe vs GB (shared windows)
    run_test("twv_probe_vs_gb", twv_probe_wids, twv_probe_golds, twv_probe_preds,
             gb_wids, gb_golds, gb_preds, "TWV Probe", "Structural GB")

    # Test 5 (bonus): TWV Probe vs GRU Probe (shared windows)
    run_test("twv_probe_vs_gru_probe", twv_probe_wids, twv_probe_golds, twv_probe_preds,
             probe_wids, probe_golds, probe_preds, "TWV Probe", "GRU Probe")

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved: {output_path}")


if __name__ == "__main__":
    main()
