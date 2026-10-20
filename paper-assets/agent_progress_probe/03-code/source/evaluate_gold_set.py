#!/usr/bin/env python3
"""Gold Set Evaluation Pipeline.

Evaluates multiple models/label sources against human-annotated gold labels.

Input:
  --gold_csv PATH   : CSV with columns (window_id, gold_label)
                      window_id format: {trajectory_id}__w{window_idx}
  --output_dir PATH : Output directory for results JSON + markdown report

Evaluated models:
  1. MV labels        — majority vote from labeling functions
  2. probe_001        — GRU probe (checkpoints/best_model.pt)
  3. Structural RF    — RandomForest on hand-crafted features (trained on-the-fly)
  4. Structural GB    — GradientBoosting on hand-crafted features (trained on-the-fly)
  5. TWV labels       — Temporally-Weighted Vote σ=2 labels (data/windows_tlm_labels.jsonl)

Output:
  - results.json     : Per-model metrics + gold distribution + deltas
  - report.md        : Human-readable markdown comparison report

Dependencies: torch, scikit-learn, numpy

Dry-run mode (--dry_run):
  Generates pseudo gold labels from conf>=2 MV labels, runs full pipeline.
"""

import argparse
import csv
import json
import os
import re
import sys
import time
import warnings
from collections import Counter
from difflib import SequenceMatcher
from pathlib import Path

import numpy as np
import torch
import torch.nn as nn
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from sklearn.preprocessing import StandardScaler
from torch.utils.data import DataLoader

warnings.filterwarnings("ignore", category=UserWarning)

# ---------------------------------------------------------------------------
# Import probe model from project
# ---------------------------------------------------------------------------
sys.path.insert(0, str(Path(__file__).parent))
from probe_model import ProgressProbe, WindowDataset, collate_fn


# ===========================================================================
# Metrics
# ===========================================================================

def compute_metrics(y_true, y_pred):
    return {
        "macro_f1": f1_score(y_true, y_pred, average="macro", zero_division=0),
        "f1_stag": f1_score(y_true, y_pred, pos_label=0, zero_division=0),
        "f1_prog": f1_score(y_true, y_pred, pos_label=1, zero_division=0),
        "precision_stag": precision_score(y_true, y_pred, pos_label=0, zero_division=0),
        "recall_stag": recall_score(y_true, y_pred, pos_label=0, zero_division=0),
        "accuracy": accuracy_score(y_true, y_pred),
    }


# ===========================================================================
# Structural feature extraction (from non_nlp_baseline.py)
# ===========================================================================

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


# ===========================================================================
# Data loading helpers
# ===========================================================================

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


def parse_row_index(trajectory_id):
    return int(trajectory_id.rsplit("__r", 1)[1])


# ===========================================================================
# Evaluators
# ===========================================================================

def evaluate_mv(gold_wids, gold_labels, wid_to_window):
    preds = []
    valid_gold = []
    for wid, gl in zip(gold_wids, gold_labels):
        w = wid_to_window.get(wid)
        if w is None:
            continue
        preds.append(w["majority_label"])
        valid_gold.append(gl)
    if not preds:
        return None, 0
    return compute_metrics(valid_gold, preds), len(preds)


def evaluate_twv(gold_wids, gold_labels, wid_to_twv):
    preds = []
    valid_gold = []
    for wid, gl in zip(gold_wids, gold_labels):
        twv = wid_to_twv.get(wid)
        if twv is None:
            continue
        preds.append(twv["twv_label"])
        valid_gold.append(gl)
    if not preds:
        return None, 0
    return compute_metrics(valid_gold, preds), len(preds)


@torch.no_grad()
def evaluate_probe_model(gold_wids, gold_labels, wid_to_emb_idx, embeddings, ckpt_path, device):
    if not os.path.exists(ckpt_path):
        return None, 0

    ckpt = torch.load(ckpt_path, map_location=device, weights_only=False)
    model = ProgressProbe(
        embed_dim=ckpt["embed_dim"],
        hidden_size=ckpt["hidden_size"],
        num_layers=ckpt["num_layers"],
    ).to(device)
    model.load_state_dict(ckpt["model_state_dict"])
    model.eval()

    gold_embs = []
    valid_gold = []
    for wid, gl in zip(gold_wids, gold_labels):
        idx = wid_to_emb_idx.get(wid)
        if idx is None:
            continue
        gold_embs.append(embeddings[idx])
        valid_gold.append(gl)

    if not gold_embs:
        return None, 0

    ds = WindowDataset(gold_embs, valid_gold)
    loader = DataLoader(ds, batch_size=64, collate_fn=collate_fn)

    all_preds = []
    all_labels = []
    for padded, labels, lengths in loader:
        logits = model(padded.to(device), lengths)
        preds = (torch.sigmoid(logits) >= 0.5).long().cpu()
        all_preds.extend(preds.tolist())
        all_labels.extend(labels.long().tolist())

    return compute_metrics(all_labels, all_preds), len(all_preds)


def evaluate_structural(
    gold_wids, gold_labels, wid_to_noabs_idx,
    all_features, all_mv_labels, split_info, model_cls, model_kwargs, use_scaler=False,
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

    scaler = None
    if use_scaler:
        scaler = StandardScaler()
        X_train = scaler.fit_transform(X_train)

    clf = model_cls(**model_kwargs)
    clf.fit(X_train, y_train)

    gold_feats = []
    valid_gold = []
    for wid, gl in zip(gold_wids, gold_labels):
        idx = wid_to_noabs_idx.get(wid)
        if idx is None:
            continue
        gold_feats.append(all_features[idx])
        valid_gold.append(gl)

    if not gold_feats:
        return None, 0

    X_gold = np.stack(gold_feats)
    if scaler is not None:
        X_gold = scaler.transform(X_gold)
    preds = clf.predict(X_gold).tolist()

    return compute_metrics(valid_gold, preds), len(preds)


# ===========================================================================
# Dry-run: generate pseudo gold CSV
# ===========================================================================

def generate_pseudo_gold(windows, min_confidence=2):
    rows = []
    for w in windows:
        if w.get("majority_label", -1) == -1:
            continue
        if w.get("confidence", 0) >= min_confidence:
            rows.append((window_id(w), w["majority_label"]))
    return rows


# ===========================================================================
# Report generation
# ===========================================================================

def generate_report(results, gold_dist, mv_gold_agreement, output_dir):
    lines = ["# Gold Set Evaluation Report\n"]
    lines.append(f"**Date**: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")

    lines.append("## Gold Label Distribution\n")
    total = gold_dist.get("total", 0)
    n_stag = gold_dist.get("stagnation", 0)
    n_prog = gold_dist.get("progress", 0)
    lines.append(f"- Total gold windows: **{total}**")
    lines.append(f"- Stagnation (0): **{n_stag}** ({100*n_stag/max(total,1):.1f}%)")
    lines.append(f"- Progress (1): **{n_prog}** ({100*n_prog/max(total,1):.1f}%)\n")

    lines.append("## Per-Model Results vs Gold\n")
    header = "| Model | N | Macro-F1 | F1(stag) | F1(prog) | Prec(stag) | Rec(stag) | Accuracy |"
    sep = "|---|---|---|---|---|---|---|---|"
    lines.append(header)
    lines.append(sep)
    for name, metrics, n in results:
        if metrics is None:
            lines.append(f"| {name} | — | SKIPPED | | | | | |")
            continue
        lines.append(
            f"| {name} | {n} "
            f"| {metrics['macro_f1']:.4f} "
            f"| {metrics['f1_stag']:.4f} "
            f"| {metrics['f1_prog']:.4f} "
            f"| {metrics['precision_stag']:.4f} "
            f"| {metrics['recall_stag']:.4f} "
            f"| {metrics['accuracy']:.4f} |"
        )
    lines.append("")

    if mv_gold_agreement is not None:
        lines.append("## MV vs Gold Agreement (Circular Eval Indicator)\n")
        lines.append(f"- MV-Gold agreement rate: **{mv_gold_agreement['agreement_rate']:.4f}**")
        lines.append(f"- MV-Gold disagreement count: **{mv_gold_agreement['n_disagree']}** / {mv_gold_agreement['n_total']}")
        lines.append(f"- Implication: models trained on MV labels have a ceiling of ~{mv_gold_agreement['agreement_rate']:.1%} accuracy when evaluated against gold.\n")

    mv_metrics = None
    for name, m, _ in results:
        if name == "MV Labels" and m is not None:
            mv_metrics = m
            break

    if mv_metrics is not None:
        lines.append("## MV-derived vs Gold-derived Metric Deltas\n")
        lines.append("Shows how much each model's gold-eval metrics differ from its MV-eval metrics.")
        lines.append("Positive delta = gold metric higher than MV metric.\n")
        lines.append("| Model | Δ Macro-F1 | Δ F1(stag) | Δ Accuracy |")
        lines.append("|---|---|---|---|")
        for name, metrics, _ in results:
            if metrics is None or name == "MV Labels":
                continue
            lines.append(
                f"| {name} "
                f"| — | — | — |"
            )
        lines.append("")
        lines.append("*(Full MV-derived metrics will be computed when original test-set results are available.)*\n")

    report_text = "\n".join(lines)
    report_path = Path(output_dir) / "report.md"
    report_path.write_text(report_text)
    return report_path


# ===========================================================================
# Main
# ===========================================================================

def main():
    parser = argparse.ArgumentParser(description="Evaluate models against gold labels")
    parser.add_argument("--gold_csv", type=str, default=None, help="Gold labels CSV (window_id, gold_label)")
    parser.add_argument("--output_dir", type=str, required=True, help="Output directory")
    parser.add_argument("--data_dir", type=str, default="data", help="Data directory")
    parser.add_argument("--checkpoint", type=str, default="checkpoints/best_model.pt", help="GRU probe checkpoint")
    parser.add_argument("--twv_checkpoint", type=str, default="checkpoints_tlm_twv/best_model.pt", help="TWV probe checkpoint")
    parser.add_argument("--split_info", type=str, default="checkpoints/split_info.json", help="Split info JSON")
    parser.add_argument("--trajectories", type=str, default="data/swe_agent_trajectories_5000.jsonl", help="Raw trajectories")
    parser.add_argument("--device", type=str, default=None, help="Device (e.g. cuda:1)")
    parser.add_argument("--dry_run", action="store_true", help="Generate pseudo gold from conf>=2 MV labels")
    parser.add_argument("--dry_run_min_conf", type=int, default=2, help="Min confidence for dry-run pseudo gold")
    args = parser.parse_args()

    t_start = time.time()
    base_dir = Path(__file__).parent
    data_dir = base_dir / args.data_dir
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    device = args.device or ("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Device: {device}")

    # ------------------------------------------------------------------
    # 1. Load windows
    # ------------------------------------------------------------------
    print("Loading windows_labeled.jsonl ...")
    all_windows = load_windows_jsonl(data_dir / "windows_labeled.jsonl")
    non_abstain = [w for w in all_windows if w.get("majority_label", -1) != -1]
    print(f"  Total windows: {len(all_windows)}, non-abstain: {len(non_abstain)}")

    wid_to_window = {window_id(w): w for w in non_abstain}
    wid_to_noabs_idx = {window_id(w): i for i, w in enumerate(non_abstain)}

    # ------------------------------------------------------------------
    # 2. Load or generate gold labels
    # ------------------------------------------------------------------
    if args.dry_run:
        print(f"DRY RUN: generating pseudo gold from conf>={args.dry_run_min_conf} MV labels ...")
        pseudo_gold = generate_pseudo_gold(all_windows, min_confidence=args.dry_run_min_conf)
        gold_wids = [wid for wid, _ in pseudo_gold]
        gold_labels = [label for _, label in pseudo_gold]
        print(f"  Pseudo gold windows: {len(gold_wids)}")

        csv_path = output_dir / "pseudo_gold.csv"
        with open(csv_path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["window_id", "gold_label"])
            for wid, label in pseudo_gold:
                writer.writerow([wid, label])
        print(f"  Saved pseudo gold CSV: {csv_path}")
    else:
        if args.gold_csv is None:
            print("ERROR: --gold_csv required when not in --dry_run mode")
            sys.exit(1)
        print(f"Loading gold CSV: {args.gold_csv}")
        gold_wids = []
        gold_labels = []
        with open(args.gold_csv) as f:
            reader = csv.DictReader(f)
            for row in reader:
                gold_wids.append(row["window_id"])
                gold_labels.append(int(row["gold_label"]))
        print(f"  Gold windows: {len(gold_wids)}")

    gold_dist = {
        "total": len(gold_labels),
        "stagnation": sum(1 for l in gold_labels if l == 0),
        "progress": sum(1 for l in gold_labels if l == 1),
    }
    print(f"  Distribution: stag={gold_dist['stagnation']}, prog={gold_dist['progress']}")

    # ------------------------------------------------------------------
    # 3. Load embeddings
    # ------------------------------------------------------------------
    print("Loading embeddings.pt ...")
    emb_data = torch.load(data_dir / "embeddings.pt", map_location="cpu", weights_only=False)
    embeddings = emb_data["embeddings"]
    emb_trajectory_ids = emb_data.get("trajectory_ids", [])
    print(f"  Embeddings loaded: {len(embeddings)}")

    wid_to_emb_idx = {}
    if len(emb_trajectory_ids) == len(non_abstain):
        for i, w in enumerate(non_abstain):
            wid_to_emb_idx[window_id(w)] = i
    else:
        print(f"  WARNING: embedding count ({len(embeddings)}) != non_abstain ({len(non_abstain)}), building fallback index")
        for i in range(len(embeddings)):
            if i < len(non_abstain):
                wid_to_emb_idx[window_id(non_abstain[i])] = i

    # ------------------------------------------------------------------
    # 4. Load split info
    # ------------------------------------------------------------------
    split_info_path = base_dir / args.split_info
    print(f"Loading split info: {split_info_path}")
    with open(split_info_path) as f:
        split_info = json.load(f)

    # ------------------------------------------------------------------
    # 5. Evaluate each model
    # ------------------------------------------------------------------
    results = []

    # --- 5a. MV Labels ---
    print("\n[1/5] Evaluating MV Labels vs Gold ...")
    mv_metrics, mv_n = evaluate_mv(gold_wids, gold_labels, wid_to_window)
    if mv_metrics:
        print(f"  macro_f1={mv_metrics['macro_f1']:.4f}, accuracy={mv_metrics['accuracy']:.4f}, n={mv_n}")
    else:
        print("  SKIPPED: no matching windows")
    results.append(("MV Labels", mv_metrics, mv_n))

    # --- 5b. GRU Probe ---
    probe_ckpt = base_dir / args.checkpoint
    print(f"\n[2/5] Evaluating GRU Probe vs Gold ...")
    if probe_ckpt.exists():
        probe_metrics, probe_n = evaluate_probe_model(
            gold_wids, gold_labels, wid_to_emb_idx, embeddings, str(probe_ckpt), device
        )
        if probe_metrics:
            print(f"  macro_f1={probe_metrics['macro_f1']:.4f}, accuracy={probe_metrics['accuracy']:.4f}, n={probe_n}")
        else:
            print("  SKIPPED: no matching gold windows in embeddings")
    else:
        print(f"  SKIPPED: checkpoint not found at {probe_ckpt}")
        probe_metrics, probe_n = None, 0
    results.append(("GRU Probe", probe_metrics, probe_n))

    # --- 5c/5d. Structural RF & GB ---
    traj_path = base_dir / args.trajectories
    struct_available = traj_path.exists()
    if struct_available:
        print(f"\n[3-4/5] Building structural features ...")
        traj_index = build_trajectory_index(str(traj_path))
        print(f"  Indexed {len(traj_index)} trajectories")

        all_features = []
        all_mv_labels = []
        for w in non_abstain:
            row_idx = w.get("row_index", 0)
            step_indices = w["step_indices"]
            traj_steps = traj_index.get(row_idx, [])
            window_steps = []
            for si in step_indices:
                if si < len(traj_steps):
                    window_steps.append(traj_steps[si])
                else:
                    window_steps.append({"role": "unknown", "text": ""})
            feat = extract_structural_features(window_steps, w.get("short_trajectory", False))
            all_features.append(feat)
            all_mv_labels.append(w["majority_label"])

        all_features = np.stack(all_features)
        print(f"  Feature matrix: {all_features.shape}")

        # RF
        print("  Evaluating Structural RF ...")
        rf_metrics, rf_n = evaluate_structural(
            gold_wids, gold_labels, wid_to_noabs_idx,
            all_features, all_mv_labels, split_info,
            RandomForestClassifier,
            {"n_estimators": 100, "max_depth": 10, "random_state": 42, "n_jobs": -1},
        )
        if rf_metrics:
            print(f"  RF: macro_f1={rf_metrics['macro_f1']:.4f}, accuracy={rf_metrics['accuracy']:.4f}, n={rf_n}")
        else:
            print("  RF: SKIPPED")
        results.append(("Structural RF", rf_metrics, rf_n))

        # GB
        print("  Evaluating Structural GB ...")
        gb_metrics, gb_n = evaluate_structural(
            gold_wids, gold_labels, wid_to_noabs_idx,
            all_features, all_mv_labels, split_info,
            GradientBoostingClassifier,
            {"n_estimators": 200, "learning_rate": 0.05, "max_depth": 5, "random_state": 42},
        )
        if gb_metrics:
            print(f"  GB: macro_f1={gb_metrics['macro_f1']:.4f}, accuracy={gb_metrics['accuracy']:.4f}, n={gb_n}")
        else:
            print("  GB: SKIPPED")
        results.append(("Structural GB", gb_metrics, gb_n))
    else:
        print(f"\n[3-4/5] SKIPPED structural baselines: {traj_path} not found")
        results.append(("Structural RF", None, 0))
        results.append(("Structural GB", None, 0))

    # --- 5e. TWV Labels ---
    twv_labels_path = data_dir / "windows_tlm_labels.jsonl"
    print(f"\n[5/5] Evaluating TWV Labels vs Gold ...")
    if twv_labels_path.exists():
        twv_windows = load_windows_jsonl(str(twv_labels_path))
        wid_to_twv = {}
        for w in twv_windows:
            wid = f"{w['trajectory_id']}__w{w['window_idx']}"
            wid_to_twv[wid] = w
        twv_metrics, twv_n = evaluate_twv(gold_wids, gold_labels, wid_to_twv)
        if twv_metrics:
            print(f"  macro_f1={twv_metrics['macro_f1']:.4f}, accuracy={twv_metrics['accuracy']:.4f}, n={twv_n}")
        else:
            print("  SKIPPED: no matching windows")
    else:
        print(f"  SKIPPED: {twv_labels_path} not found")
        twv_metrics, twv_n = None, 0
    results.append(("TWV Labels", twv_metrics, twv_n))

    # --- 5f. TWV Probe (bonus) ---
    twv_ckpt = base_dir / args.twv_checkpoint
    if twv_ckpt.exists():
        twv_emb_path = base_dir / "data_tlm_twv" / "embeddings.pt"
        if twv_emb_path.exists():
            print("\n[bonus] Evaluating TWV Probe vs Gold ...")
            twv_emb_data = torch.load(twv_emb_path, map_location="cpu", weights_only=False)
            twv_embeddings = twv_emb_data["embeddings"]

            twv_wid_to_emb_idx = {}
            twv_all_windows = load_windows_jsonl(str(twv_labels_path)) if twv_labels_path.exists() else []
            twv_non_abstain = [w for w in twv_all_windows if w.get("mv_label", -1) != -1]
            if len(twv_embeddings) == len(twv_non_abstain):
                for i, w in enumerate(twv_non_abstain):
                    wid = f"{w['trajectory_id']}__w{w['window_idx']}"
                    twv_wid_to_emb_idx[wid] = i
            else:
                for i, w in enumerate(non_abstain):
                    if i < len(twv_embeddings):
                        twv_wid_to_emb_idx[window_id(w)] = i

            twv_probe_metrics, twv_probe_n = evaluate_probe_model(
                gold_wids, gold_labels, twv_wid_to_emb_idx, twv_embeddings, str(twv_ckpt), device
            )
            if twv_probe_metrics:
                print(f"  macro_f1={twv_probe_metrics['macro_f1']:.4f}, accuracy={twv_probe_metrics['accuracy']:.4f}, n={twv_probe_n}")
                results.append(("TWV Probe", twv_probe_metrics, twv_probe_n))
            else:
                print("  SKIPPED: no matching windows")

    # ------------------------------------------------------------------
    # 6. MV-Gold agreement
    # ------------------------------------------------------------------
    n_agree = 0
    n_total = 0
    for wid, gl in zip(gold_wids, gold_labels):
        w = wid_to_window.get(wid)
        if w is None:
            continue
        n_total += 1
        if w["majority_label"] == gl:
            n_agree += 1
    mv_gold_agreement = {
        "agreement_rate": n_agree / max(n_total, 1),
        "n_agree": n_agree,
        "n_disagree": n_total - n_agree,
        "n_total": n_total,
    }
    print(f"\nMV-Gold agreement: {n_agree}/{n_total} = {mv_gold_agreement['agreement_rate']:.4f}")

    # ------------------------------------------------------------------
    # 7. Output
    # ------------------------------------------------------------------
    elapsed = time.time() - t_start

    output = {
        "gold_distribution": gold_dist,
        "mv_gold_agreement": mv_gold_agreement,
        "models": {},
        "elapsed_seconds": round(elapsed, 2),
        "dry_run": args.dry_run,
    }
    for name, metrics, n in results:
        output["models"][name] = {
            "n_evaluated": n,
            "metrics": {k: round(v, 6) for k, v in metrics.items()} if metrics else None,
        }

    json_path = output_dir / "results.json"
    with open(json_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nResults JSON: {json_path}")

    report_path = generate_report(results, gold_dist, mv_gold_agreement, output_dir)
    print(f"Report: {report_path}")
    print(f"\nTotal elapsed: {elapsed:.1f}s")


if __name__ == "__main__":
    main()
