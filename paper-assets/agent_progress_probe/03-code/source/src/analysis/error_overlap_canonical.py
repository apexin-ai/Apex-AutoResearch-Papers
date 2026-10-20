#!/usr/bin/env python3
"""Canonical error overlap analysis: probe vs structural GB on OH conf>=2.

Reproduces the authoritative numbers for the paper's error-overlap claim.
All alignment uses (trajectory_id, tuple(step_indices)) keys.

Usage:
    python src/analysis/error_overlap_canonical.py \
        --checkpoint_path checkpoints_full/best_model.pt \
        --embeddings_path /root/autodl-tmp/openhands_data/embeddings_fixed.pt \
        --windows_jsonl_path /root/autodl-tmp/openhands_data/windows_labeled.jsonl \
        --oh_traj_path /root/autodl-tmp/openhands_data/openhands_trajectories.jsonl \
        --swe_windows_path data/windows_labeled.jsonl \
        --swe_traj_path data/swe_agent_trajectories_5000.jsonl \
        --conf_threshold 2 \
        --output_path results/error_overlap_canonical.json
"""

import argparse
import json
import re
from collections import Counter
from difflib import SequenceMatcher
from pathlib import Path

import numpy as np
import torch
import torch.nn as nn
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score


# ── Probe model (mirrors probe_model.py) ────────────────────────────────

class ProgressProbe(nn.Module):
    def __init__(self, embed_dim, hidden_size=256, num_layers=2, dropout=0.1):
        super().__init__()
        self.gru = nn.GRU(embed_dim, hidden_size, num_layers=num_layers,
                          batch_first=True, dropout=dropout if num_layers > 1 else 0.0)
        self.classifier = nn.Linear(hidden_size, 1)

    def forward(self, x, lengths=None):
        if lengths is not None:
            x = nn.utils.rnn.pack_padded_sequence(
                x, lengths.cpu(), batch_first=True, enforce_sorted=False)
        _, hidden = self.gru(x)
        return self.classifier(hidden[-1]).squeeze(-1)


# ── Structural feature extraction (mirrors non_nlp_baseline.py) ─────────

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
        slope = (n * np.dot(x, y) - x.sum() * y.sum()) / \
                (n * np.dot(x, x) - x.sum()**2 + 1e-9)
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

    adj_sims = []
    for i in range(len(commands) - 1):
        adj_sims.append(cmd_similarity(commands[i], commands[i + 1]))
    avg_adj_sim = np.mean(adj_sims) if adj_sims else 0.0
    max_adj_sim = max(adj_sims) if adj_sims else 0.0

    max_run = 1
    if len(commands) > 1:
        run = 1
        for i in range(1, len(commands)):
            if commands[i] == commands[i - 1]:
                run += 1
                max_run = max(max_run, run)
            else:
                run = 1

    n_errors_feat = sum(1 for t in texts
                        if "error" in t.lower() or "Error" in t or "Traceback" in t)
    n_test_output = sum(1 for t in texts
                        if ("PASSED" in t or "FAILED" in t) and "test" in t.lower())
    n_file_display = sum(1 for t in texts if "[File:" in t)
    n_nonzero_exit = sum(
        1 for _, t in observations
        if re.search(r"exit code [1-9]|returned non-zero|command not found", t))

    return np.array([
        n, n_actions, n_obs, n_actions / max(n, 1),
        mean_tlen, std_tlen, max_tlen, min_tlen,
        mean_action_len, mean_obs_len, slope,
        n_cmds, mean_cmd_len, max_cmd_len,
        unique_cmd_ratio, repeat_ratio,
        n_edit, n_search, n_nav, n_submit,
        edit_ratio, search_ratio,
        avg_adj_sim, max_adj_sim, max_run,
        n_errors_feat, n_test_output, n_file_display, n_nonzero_exit,
        float(is_short),
    ], dtype=np.float32)


def build_trajectory_index(traj_path):
    index = {}
    with open(traj_path) as f:
        for row_idx, line in enumerate(f):
            line = line.strip()
            if not line:
                continue
            raw = json.loads(line)
            steps = [{"role": s.get("role", "unknown"),
                       "text": s.get("text") or s.get("system_prompt") or ""}
                      for s in raw.get("trajectory") or []]
            index[row_idx] = steps
    return index


def extract_features_for_windows(windows, traj_index):
    features = []
    for w in windows:
        row_idx = w.get("row_index", 0)
        step_indices = w["step_indices"]
        traj_steps = traj_index.get(row_idx, [])
        window_steps = [
            traj_steps[si] if si < len(traj_steps)
            else {"role": "unknown", "text": ""}
            for si in step_indices
        ]
        features.append(extract_features(window_steps, w.get("short_trajectory", False)))
    return np.stack(features)


# ── Main ────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Canonical error overlap analysis")
    parser.add_argument("--checkpoint_path", required=True)
    parser.add_argument("--embeddings_path", required=True)
    parser.add_argument("--windows_jsonl_path", required=True)
    parser.add_argument("--oh_traj_path", required=True)
    parser.add_argument("--swe_windows_path", required=True)
    parser.add_argument("--swe_traj_path", required=True)
    parser.add_argument("--conf_threshold", type=int, default=2)
    parser.add_argument("--output_path", required=True)
    args = parser.parse_args()

    device = "cuda" if torch.cuda.is_available() else "cpu"

    # ── 1. Load probe checkpoint ────────────────────────────────────────
    print("=== Loading probe checkpoint ===")
    ckpt = torch.load(args.checkpoint_path, map_location="cpu", weights_only=False)
    embed_dim = ckpt["embed_dim"]
    hidden_size = ckpt.get("hidden_size", 256)
    num_layers = ckpt.get("num_layers", 2)
    dropout = ckpt.get("dropout", 0.1)
    print(f"Checkpoint: epoch={ckpt.get('epoch')}, "
          f"embed_dim={embed_dim}, hidden={hidden_size}, layers={num_layers}")

    model = ProgressProbe(embed_dim, hidden_size, num_layers, dropout)
    model.load_state_dict(ckpt["model_state_dict"])
    model.to(device)
    model.eval()

    # ── 2. Load OH embeddings and filter by confidence ──────────────────
    print("\n=== Loading OH embeddings ===")
    emb_data = torch.load(args.embeddings_path, map_location="cpu", weights_only=False)
    oh_embs = emb_data["embeddings"]
    oh_labels = emb_data["labels"]
    oh_confs = emb_data["confidences"]
    oh_traj_ids = emb_data["trajectory_ids"]
    oh_step_indices = emb_data["step_indices_list"]
    print(f"Total embeddings: {len(oh_embs)}")

    conf_mask = [i for i, c in enumerate(oh_confs) if c >= args.conf_threshold]
    c2_embs = [oh_embs[i] for i in conf_mask]
    c2_labels = [oh_labels[i] for i in conf_mask]
    c2_traj_ids = [oh_traj_ids[i] for i in conf_mask]
    c2_step_indices = [oh_step_indices[i] for i in conf_mask]
    n_total = len(c2_labels)
    n_stag = sum(1 for l in c2_labels if l == 0)
    n_prog = n_total - n_stag
    print(f"conf>={args.conf_threshold}: {n_total} windows "
          f"(stag={n_stag}, prog={n_prog})")

    # ── 3. Probe inference ──────────────────────────────────────────────
    print("\n=== Probe inference ===")
    probe_preds = []
    probe_probs_list = []
    batch_size = 256
    with torch.no_grad():
        for start in range(0, n_total, batch_size):
            end = min(start + batch_size, n_total)
            batch_embs = c2_embs[start:end]
            lengths = torch.tensor([e.shape[0] for e in batch_embs])
            max_len = int(lengths.max())
            padded = torch.zeros(len(batch_embs), max_len, embed_dim)
            for j, e in enumerate(batch_embs):
                padded[j, :e.shape[0]] = e
            padded = padded.to(device)
            lengths = lengths.to(device)
            logits = model(padded, lengths)
            probs = torch.sigmoid(logits).cpu()
            preds = (probs >= 0.5).long()
            probe_preds.extend(preds.tolist())
            probe_probs_list.extend(probs.tolist())

    probe_preds = np.array(probe_preds)
    gold_labels = np.array(c2_labels)
    probe_errors = probe_preds != gold_labels

    probe_cm = confusion_matrix(gold_labels, probe_preds, labels=[0, 1])
    p_tn, p_fp, p_fn, p_tp = probe_cm.ravel()
    probe_macro_f1 = f1_score(gold_labels, probe_preds, average="macro", zero_division=0)
    total_probe_errors = int(probe_errors.sum())
    print(f"Probe: macro_f1={probe_macro_f1:.4f}, errors={total_probe_errors}")
    print(f"  CM: TN={p_tn}, FP={p_fp}, FN={p_fn}, TP={p_tp}")

    # ── 4. Structural GB: train on SWE, predict on OH conf>=2 ───────────
    print("\n=== Structural GB ===")
    print("Loading SWE training data...")
    with open(args.swe_windows_path) as f:
        swe_windows = [json.loads(l) for l in f]
    swe_non_abstain = [w for w in swe_windows
                       if w.get("majority_label", -1) != -1]
    print(f"SWE non-abstain: {len(swe_non_abstain)}")

    swe_traj_index = build_trajectory_index(args.swe_traj_path)
    swe_X = extract_features_for_windows(swe_non_abstain, swe_traj_index)
    swe_y = np.array([w["majority_label"] for w in swe_non_abstain])
    print(f"SWE features: {swe_X.shape}")

    gb = GradientBoostingClassifier(
        n_estimators=200, learning_rate=0.05, max_depth=5, random_state=42)
    print("Training GB on SWE data (n_estimators=200, lr=0.05)...")
    gb.fit(swe_X, swe_y)

    print("Loading OH trajectory index...")
    oh_traj_index = build_trajectory_index(args.oh_traj_path)
    print(f"OH trajectories indexed: {len(oh_traj_index)}")

    print("Loading OH windows for structural features...")
    with open(args.windows_jsonl_path) as f:
        all_oh_windows = [json.loads(l) for l in f]
    oh_conf2_windows = [w for w in all_oh_windows
                        if w.get("confidence", 0) >= args.conf_threshold
                        and w.get("majority_label", -1) != -1]
    print(f"OH conf>={args.conf_threshold} for structural: {len(oh_conf2_windows)}")

    print("Extracting OH structural features...")
    oh_X = extract_features_for_windows(oh_conf2_windows, oh_traj_index)
    oh_y = np.array([w["majority_label"] for w in oh_conf2_windows])

    struct_preds = gb.predict(oh_X)
    struct_errors_mask = struct_preds != oh_y
    struct_cm = confusion_matrix(oh_y, struct_preds, labels=[0, 1])
    s_tn, s_fp, s_fn, s_tp = struct_cm.ravel()
    struct_macro_f1 = f1_score(oh_y, struct_preds, average="macro", zero_division=0)
    total_struct_errors = int(struct_errors_mask.sum())
    print(f"Struct GB: macro_f1={struct_macro_f1:.4f}, errors={total_struct_errors}")
    print(f"  CM: TN={s_tn}, FP={s_fp}, FN={s_fn}, TP={s_tp}")

    # ── 5. Overlap via (trajectory_id, step_indices) key alignment ──────
    print("\n=== Error overlap ===")
    probe_keys = {}
    for i in range(n_total):
        key = (c2_traj_ids[i], tuple(c2_step_indices[i]))
        probe_keys[key] = i

    struct_keys = {}
    for i, w in enumerate(oh_conf2_windows):
        key = (w["trajectory_id"], tuple(w["step_indices"]))
        struct_keys[key] = i

    common_keys = set(probe_keys) & set(struct_keys)
    print(f"Common windows: {len(common_keys)} / probe={len(probe_keys)}, "
          f"struct={len(struct_keys)}")

    probe_error_keys = set()
    struct_error_keys = set()
    for key in common_keys:
        pi = probe_keys[key]
        si = struct_keys[key]
        if probe_errors[pi]:
            probe_error_keys.add(key)
        if struct_errors_mask[si]:
            struct_error_keys.add(key)

    both_wrong = probe_error_keys & struct_error_keys
    probe_only = probe_error_keys - struct_error_keys
    struct_only = struct_error_keys - probe_error_keys

    n_probe_err = len(probe_error_keys)
    n_struct_err = len(struct_error_keys)
    n_both = len(both_wrong)
    overlap_rate = n_both / max(n_probe_err, 1)

    print(f"Probe errors:  {n_probe_err}")
    print(f"Struct errors: {n_struct_err}")
    print(f"Both wrong:    {n_both}")
    print(f"Probe-only:    {len(probe_only)}")
    print(f"Struct-only:   {len(struct_only)}")
    print(f"Overlap rate:  {n_both}/{n_probe_err} = {overlap_rate:.4f} "
          f"({overlap_rate*100:.2f}%)")

    # ── 6. Output ───────────────────────────────────────────────────────
    result = {
        "eval_subset": f"conf>={args.conf_threshold}",
        "n_windows": n_total,
        "probe": {
            "macro_f1": round(probe_macro_f1, 6),
            "errors": total_probe_errors,
            "confusion_matrix": {"TN": int(p_tn), "FP": int(p_fp),
                                 "FN": int(p_fn), "TP": int(p_tp)},
        },
        "structural_gb": {
            "macro_f1": round(struct_macro_f1, 6),
            "errors": total_struct_errors,
            "confusion_matrix": {"TN": int(s_tn), "FP": int(s_fp),
                                 "FN": int(s_fn), "TP": int(s_tp)},
            "hyperparams": {"n_estimators": 200, "learning_rate": 0.05,
                            "max_depth": 5, "random_state": 42},
        },
        "error_overlap": {
            "common_windows": len(common_keys),
            "probe_errors": n_probe_err,
            "struct_errors": n_struct_err,
            "both_wrong": n_both,
            "probe_only": len(probe_only),
            "struct_only": len(struct_only),
            "overlap_rate": round(overlap_rate, 6),
        },
        "data_paths": {
            "checkpoint": args.checkpoint_path,
            "embeddings": args.embeddings_path,
            "windows_jsonl": args.windows_jsonl_path,
            "oh_trajectories": args.oh_traj_path,
            "swe_windows": args.swe_windows_path,
            "swe_trajectories": args.swe_traj_path,
        },
    }

    output_path = Path(args.output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(result, f, indent=2)
    print(f"\nSaved to {output_path}")


if __name__ == "__main__":
    main()
