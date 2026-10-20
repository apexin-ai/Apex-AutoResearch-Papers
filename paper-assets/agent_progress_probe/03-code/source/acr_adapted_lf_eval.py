#!/usr/bin/env python3
"""ACR adapted-LF relabeling + cross-agent transfer evaluation.

Replaces file_diff_delta and outcome_backpropagation (which misfire on ACR)
with action_entropy and output_stagnation. Evaluates whether LF portability
determines cross-agent transfer ceiling.
"""

import json
import math
import re
import sys
from collections import Counter
from dataclasses import dataclass
from difflib import SequenceMatcher
from pathlib import Path
from typing import Optional

import numpy as np
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score

# ── Constants ──
PROGRESS = 1
STAGNATION = 0
ABSTAIN = -1

ACR_TRAJ_PATH = Path("/root/autodl-tmp/agent3_data/autocoderover_trajectories.jsonl")
ACR_WIN_PATH = Path("/root/autodl-tmp/agent3_data/acr_windows_labeled.jsonl")
SWE_TRAJ_PATH = Path("/root/autodl-tmp/agent_progress_probe/data/swe_agent_trajectories_5000.jsonl")
SWE_WIN_PATH = Path("/root/autodl-tmp/agent_progress_probe/data/windows_labeled.jsonl")
OUT_PATH = Path("/root/autodl-tmp/agent3_data/acr_adapted_lf_results.json")


# ── Step wrapper ──
@dataclass
class Step:
    index: int
    role: str
    text: str
    mask: bool = False

    @property
    def is_action(self):
        return self.role == "ai"

    @property
    def is_observation(self):
        return self.role == "user" and self.index > 0

    @property
    def command(self) -> Optional[str]:
        if self.role != "ai":
            return None
        match = re.search(r"```\n?(.*?)```", self.text, re.DOTALL)
        return match.group(1).strip() if match else None


# ── Adapted LFs ──

def _cmd_similarity(a, b):
    if a == b: return 1.0
    if not a or not b: return 0.0
    return SequenceMatcher(None, a, b).ratio()


def _has_consecutive_similar(commands, min_run=3, threshold=0.9):
    if len(commands) < min_run:
        return False
    run = 1
    for i in range(1, len(commands)):
        if _cmd_similarity(commands[i-1], commands[i]) >= threshold:
            run += 1
            if run >= min_run:
                return True
        else:
            run = 1
    return False


def lf_command_repetition(steps):
    commands = [s.command for s in steps if s.is_action and s.command]
    if len(commands) < 2:
        return ABSTAIN
    if _has_consecutive_similar(commands, min_run=3, threshold=1.0):
        return STAGNATION
    if _has_consecutive_similar(commands, min_run=3, threshold=0.9):
        return STAGNATION
    if len(set(commands)) == len(commands):
        return PROGRESS
    return ABSTAIN


def _action_type_category(cmd):
    fw = cmd.strip().split()[0] if cmd.strip() else ""
    if fw in {"edit", "str_replace", "create", "insert"}: return "edit"
    if fw in {"search_dir", "search_file", "find_file", "find", "grep"}: return "search"
    if fw in {"open", "goto", "scroll_down", "scroll_up", "cd", "ls", "cat", "view"}: return "nav"
    if fw in {"python", "pytest", "python3"}: return "test"
    if fw == "submit": return "submit"
    return "other"


def lf_action_entropy(steps, threshold=0.3):
    commands = [s.command for s in steps if s.is_action and s.command]
    if len(commands) < 3:
        return ABSTAIN
    counter = Counter(_action_type_category(c) for c in commands)
    total = sum(counter.values())
    entropy = -sum((c/total) * math.log2(c/total) for c in counter.values() if c > 0)
    max_ent = math.log2(len(counter)) if len(counter) > 1 else 1.0
    norm = entropy / max_ent if max_ent > 0 else 0.0
    if norm < threshold:
        return STAGNATION
    return ABSTAIN


def lf_output_stagnation(steps, sim_threshold=0.8, min_run=3):
    obs = [s.text[:500] for s in steps if s.is_observation]
    if len(obs) < min_run:
        return ABSTAIN
    run = 1
    for i in range(1, len(obs)):
        if SequenceMatcher(None, obs[i-1], obs[i]).ratio() >= sim_threshold:
            run += 1
            if run >= min_run:
                return STAGNATION
        else:
            run = 1
    return ABSTAIN


def lf_error_repetition(steps, threshold=4):
    error_sigs = []
    for step in steps:
        if not step.is_observation:
            continue
        if "Traceback" not in step.text and "Error" not in step.text:
            continue
        for line in reversed(step.text.strip().splitlines()):
            line = line.strip()
            if line and ("Error" in line or "Exception" in line):
                error_sigs.append(line[:200])
                break
        else:
            error_sigs.append("_generic_error_")
    if len(error_sigs) < 2:
        return ABSTAIN
    if Counter(error_sigs).most_common(1)[0][1] >= threshold:
        return STAGNATION
    return ABSTAIN


ADAPTED_LFS = [
    ("command_repetition", lf_command_repetition),
    ("action_entropy", lf_action_entropy),
    ("output_stagnation", lf_output_stagnation),
]

ADAPTED_LFS_4 = ADAPTED_LFS + [("error_repetition", lf_error_repetition)]


def majority_vote(votes):
    non_abstain = [v for v in votes if v != ABSTAIN]
    if not non_abstain:
        return ABSTAIN, 0
    c = Counter(non_abstain)
    label, count = c.most_common(1)[0]
    confidence = count
    return label, confidence


# ── Structural features (from cross_agent_structural_baseline.py) ──

EDIT_CMDS = {"edit", "str_replace", "create", "insert"}
SEARCH_CMDS_F = {"search_dir", "search_file", "find_file", "find", "grep", "view"}
NAV_CMDS = {"open", "goto", "scroll_down", "scroll_up", "cd", "ls", "cat"}


def extract_command_from_text(text):
    match = re.search(r"```\n?(.*?)```", text, re.DOTALL)
    return match.group(1).strip() if match else None


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
        cmd = extract_command_from_text(t)
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
        elif first_word in SEARCH_CMDS_F:
            n_search += 1
        elif first_word in NAV_CMDS:
            n_nav += 1
        elif first_word == "submit":
            n_submit += 1

    edit_ratio = n_edit / max(n_cmds, 1)
    search_ratio = n_search / max(n_cmds, 1)

    if n_cmds >= 2:
        sims = [_cmd_similarity(commands[i], commands[i+1]) for i in range(n_cmds - 1)]
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
        max_similar_run = max_run
    else:
        avg_adj_sim = 0.0
        max_adj_sim = 0.0
        max_similar_run = 0

    n_errors = sum(1 for s, t in observations if "Traceback" in t or "Error" in t)
    error_ratio = n_errors / max(n_obs, 1)

    if n_obs >= 2:
        obs_texts = [t[:500] for _, t in observations]
        obs_sims = [SequenceMatcher(None, obs_texts[i], obs_texts[i+1]).ratio()
                     for i in range(len(obs_texts) - 1)]
        avg_obs_sim = np.mean(obs_sims)
        max_obs_sim = max(obs_sims)
    else:
        avg_obs_sim = 0.0
        max_obs_sim = 0.0

    return np.array([
        n, n_actions, n_obs,
        mean_tlen, std_tlen, max_tlen, min_tlen,
        mean_action_len, mean_obs_len, slope,
        n_cmds, mean_cmd_len, max_cmd_len,
        unique_cmd_ratio, repeat_ratio,
        n_edit, n_search, n_nav, n_submit,
        edit_ratio, search_ratio,
        avg_adj_sim, max_adj_sim, max_similar_run,
        n_errors, error_ratio,
        avg_obs_sim, max_obs_sim,
        float(is_short),
        float(n_cmds > 0 and commands[-1].strip().split()[0] == "submit" if n_cmds > 0 else False),
    ])


def compute_metrics(labels, preds):
    return {
        "macro_f1": f1_score(labels, preds, average="macro", zero_division=0),
        "accuracy": accuracy_score(labels, preds),
        "precision_macro": precision_score(labels, preds, average="macro", zero_division=0),
        "recall_macro": recall_score(labels, preds, average="macro", zero_division=0),
        "f1_stagnation": f1_score(labels, preds, pos_label=0, zero_division=0),
        "f1_progress": f1_score(labels, preds, pos_label=1, zero_division=0),
    }


# ══════════════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════════════

def main():
    # ── Phase 1: ACR relabeling ──
    print("=" * 70)
    print("PHASE 1: ACR RELABELING WITH ADAPTED LFs")
    print("=" * 70)

    print("\nLoading ACR trajectories...", flush=True)
    acr_traj = {}
    with open(ACR_TRAJ_PATH) as f:
        for i, line in enumerate(f):
            d = json.loads(line)
            tid = f"{d['instance_id']}__{d['model_name']}__r{i}"
            acr_traj[tid] = d["trajectory"]
    print(f"  Loaded {len(acr_traj)} ACR trajectories")

    print("Loading ACR windows...", flush=True)
    acr_windows = []
    with open(ACR_WIN_PATH) as f:
        for line in f:
            acr_windows.append(json.loads(line))
    print(f"  Loaded {len(acr_windows)} ACR windows")

    # Apply adapted LFs to each ACR window
    print("\nApplying adapted LFs to ACR windows...", flush=True)
    lf_stats = {name: {"stag": 0, "prog": 0, "abstain": 0} for name, _ in ADAPTED_LFS_4}
    adapted_labels = []
    adapted_labels_4lf = []

    for w in acr_windows:
        tid = w["trajectory_id"]
        if tid not in acr_traj:
            adapted_labels.append({"label": ABSTAIN, "confidence": 0, "votes": {}})
            adapted_labels_4lf.append({"label": ABSTAIN, "confidence": 0, "votes": {}})
            continue

        traj = acr_traj[tid]
        step_indices = w["step_indices"]
        raw_steps = [traj[i] for i in step_indices if i < len(traj)]
        steps = [Step(index=idx, role=s["role"], text=s["text"]) for idx, s in zip(step_indices, raw_steps)]

        # Apply all 4 LFs
        votes_all = {}
        for name, fn in ADAPTED_LFS_4:
            v = fn(steps)
            votes_all[name] = v
            if v == STAGNATION:
                lf_stats[name]["stag"] += 1
            elif v == PROGRESS:
                lf_stats[name]["prog"] += 1
            else:
                lf_stats[name]["abstain"] += 1

        # 3-LF adapted MV
        votes_3 = [votes_all[n] for n in ["command_repetition", "action_entropy", "output_stagnation"]]
        label_3, conf_3 = majority_vote(votes_3)
        adapted_labels.append({"label": label_3, "confidence": conf_3, "votes": {k: votes_all[k] for k in ["command_repetition", "action_entropy", "output_stagnation"]}})

        # 4-LF adapted MV
        votes_4 = list(votes_all.values())
        label_4, conf_4 = majority_vote(votes_4)
        adapted_labels_4lf.append({"label": label_4, "confidence": conf_4, "votes": votes_all})

    total = len(acr_windows)
    print(f"\n  Per-LF statistics on ACR ({total} windows):")
    print(f"  {'LF':<25s} {'Stag':>6s} {'Prog':>6s} {'Abstain':>8s} {'Coverage':>10s} {'TrigRate':>10s}")
    for name, _ in ADAPTED_LFS_4:
        s = lf_stats[name]
        cov = (s["stag"] + s["prog"]) / total
        trig = s["stag"] / total
        print(f"  {name:<25s} {s['stag']:>6d} {s['prog']:>6d} {s['abstain']:>8d} {cov:>10.3f} {trig:>10.3f}")

    # Compare original vs adapted labels
    orig_labels = [w["majority_label"] for w in acr_windows]
    adapt3_labels = [a["label"] for a in adapted_labels]
    adapt4_labels = [a["label"] for a in adapted_labels_4lf]

    # Non-abstain counts
    orig_nonabstain = sum(1 for l in orig_labels if l != ABSTAIN)
    adapt3_nonabstain = sum(1 for l in adapt3_labels if l != ABSTAIN)
    adapt4_nonabstain = sum(1 for l in adapt4_labels if l != ABSTAIN)

    orig_stag = sum(1 for l in orig_labels if l == STAGNATION)
    adapt3_stag = sum(1 for l in adapt3_labels if l == STAGNATION)
    adapt4_stag = sum(1 for l in adapt4_labels if l == STAGNATION)

    print(f"\n  Label comparison:")
    print(f"  {'Config':<20s} {'NonAbstain':>12s} {'Stag':>6s} {'Prog':>6s} {'StagRate':>10s}")
    print(f"  {'Original 3-LF':<20s} {orig_nonabstain:>12d} {orig_stag:>6d} {orig_nonabstain - orig_stag:>6d} {orig_stag/max(orig_nonabstain,1):>10.3f}")
    print(f"  {'Adapted 3-LF':<20s} {adapt3_nonabstain:>12d} {adapt3_stag:>6d} {adapt3_nonabstain - adapt3_stag:>6d} {adapt3_stag/max(adapt3_nonabstain,1):>10.3f}")
    print(f"  {'Adapted 4-LF':<20s} {adapt4_nonabstain:>12d} {adapt4_stag:>6d} {adapt4_nonabstain - adapt4_stag:>6d} {adapt4_stag/max(adapt4_nonabstain,1):>10.3f}")

    # Label change analysis
    changed_3 = sum(1 for o, a in zip(orig_labels, adapt3_labels) if o != a and o != ABSTAIN and a != ABSTAIN)
    both_nonabstain_3 = sum(1 for o, a in zip(orig_labels, adapt3_labels) if o != ABSTAIN and a != ABSTAIN)
    print(f"\n  Label changes (orig→adapted 3-LF, among {both_nonabstain_3} both-nonabstain): {changed_3} ({changed_3/max(both_nonabstain_3,1):.3f})")

    # Confidence distribution for adapted 3-LF
    conf_dist = Counter(a["confidence"] for a in adapted_labels if a["label"] != ABSTAIN)
    print(f"  Adapted 3-LF confidence distribution: {dict(sorted(conf_dist.items()))}")

    # ── Phase 2: Train structural models on SWE ──
    print("\n" + "=" * 70)
    print("PHASE 2: STRUCTURAL MODEL TRAINING (SWE-Agent)")
    print("=" * 70)

    print("\nLoading SWE trajectories...", flush=True)
    swe_traj = {}
    with open(SWE_TRAJ_PATH) as f:
        for i, line in enumerate(f):
            d = json.loads(line)
            tid = f"{d['instance_id']}__{d['model_name']}__r{i}"
            swe_traj[tid] = d["trajectory"]
    print(f"  Loaded {len(swe_traj)} SWE trajectories")

    print("Loading SWE windows (conf≥2)...", flush=True)
    swe_windows = []
    with open(SWE_WIN_PATH) as f:
        for line in f:
            w = json.loads(line)
            if w["majority_label"] != ABSTAIN and w["confidence"] >= 2:
                swe_windows.append(w)
    print(f"  Loaded {len(swe_windows)} SWE conf≥2 windows")

    X_swe, y_swe = [], []
    for w in swe_windows:
        if w["trajectory_id"] not in swe_traj:
            continue
        traj = swe_traj[w["trajectory_id"]]
        steps = [traj[i] for i in w["step_indices"] if i < len(traj)]
        if not steps:
            continue
        X_swe.append(extract_features(steps, w.get("short_trajectory", False)))
        y_swe.append(w["majority_label"])
    X_swe, y_swe = np.array(X_swe), np.array(y_swe)
    print(f"  SWE features: {X_swe.shape}, stag={sum(y_swe==0)}, prog={sum(y_swe==1)}")

    scaler = StandardScaler()
    X_swe_s = scaler.fit_transform(X_swe)

    gb = GradientBoostingClassifier(n_estimators=200, learning_rate=0.05, max_depth=4, random_state=42)
    rf = RandomForestClassifier(n_estimators=100, random_state=42)
    lr = LogisticRegression(C=1.0, max_iter=1000, random_state=42)
    gb.fit(X_swe, y_swe)
    rf.fit(X_swe, y_swe)
    lr.fit(X_swe_s, y_swe)
    print("  Models trained (GB, RF, LR)")

    # ── Phase 3: Cross-agent evaluation ──
    print("\n" + "=" * 70)
    print("PHASE 3: CROSS-AGENT EVALUATION (SWE → ACR)")
    print("=" * 70)

    # Extract ACR features
    def get_acr_features(windows, traj_dict):
        X, y_orig, y_adapt3, y_adapt4, indices = [], [], [], [], []
        for idx, w in enumerate(windows):
            if w["trajectory_id"] not in traj_dict:
                continue
            traj = traj_dict[w["trajectory_id"]]
            steps = [traj[i] for i in w["step_indices"] if i < len(traj)]
            if not steps:
                continue
            X.append(extract_features(steps, w.get("short_trajectory", False)))
            y_orig.append(w["majority_label"])
            y_adapt3.append(adapted_labels[idx]["label"])
            y_adapt4.append(adapted_labels_4lf[idx]["label"])
            indices.append(idx)
        return np.array(X), np.array(y_orig), np.array(y_adapt3), np.array(y_adapt4), indices

    X_acr, y_orig_all, y_a3_all, y_a4_all, idx_all = get_acr_features(acr_windows, acr_traj)
    print(f"\n  ACR features: {X_acr.shape}")

    # Filter subsets
    def filter_subset(X, y_orig, y_adapt, label_type="orig"):
        y_ref = y_orig if label_type == "orig" else y_adapt
        mask = y_ref != ABSTAIN
        return X[mask], y_orig[mask], y_adapt[mask]

    results = {}

    for label_config, y_eval_all in [("original_3lf", y_orig_all), ("adapted_3lf", y_a3_all), ("adapted_4lf", y_a4_all)]:
        results[label_config] = {}
        # All non-abstain
        mask_all = y_eval_all != ABSTAIN
        X_sub = X_acr[mask_all]
        y_sub = y_eval_all[mask_all]

        if len(y_sub) == 0:
            continue

        # Conf>=2 for adapted labels
        if label_config.startswith("adapted"):
            labels_list = adapted_labels if "3lf" in label_config else adapted_labels_4lf
            conf_mask = np.array([labels_list[idx_all[i]]["confidence"] >= 2
                                  for i in range(len(idx_all))])[mask_all]
        else:
            conf_mask = np.array([acr_windows[idx_all[i]]["confidence"] >= 2
                                  for i in range(len(idx_all))])[mask_all]

        for subset_name, s_mask in [("all", np.ones(len(y_sub), dtype=bool)), ("conf2", conf_mask)]:
            if s_mask.sum() == 0:
                continue
            Xs = X_sub[s_mask]
            ys = y_sub[s_mask]

            results[label_config][subset_name] = {"n": int(len(ys)), "stag": int(sum(ys == 0)), "prog": int(sum(ys == 1))}

            for model_name, model, scaled in [("GB", gb, False), ("RF", rf, False), ("LR", lr, True)]:
                Xi = scaler.transform(Xs) if scaled else Xs
                preds = model.predict(Xi)
                m = compute_metrics(ys.tolist(), preds.tolist())
                results[label_config][subset_name][model_name] = {k: round(v, 4) for k, v in m.items()}

    # ── Print comparison table ──
    print("\n" + "=" * 70)
    print("COMPARISON TABLE: Cross-Agent Transfer (SWE → ACR)")
    print("=" * 70)

    for label_config in ["original_3lf", "adapted_3lf", "adapted_4lf"]:
        if label_config not in results:
            continue
        print(f"\n  --- {label_config} ---")
        for subset in ["all", "conf2"]:
            if subset not in results[label_config]:
                continue
            r = results[label_config][subset]
            print(f"  [{subset}] n={r['n']}, stag={r['stag']}, prog={r['prog']}")
            for mn in ["GB", "RF", "LR"]:
                if mn not in r:
                    continue
                m = r[mn]
                print(f"    {mn:3s}: macro_f1={m['macro_f1']:.4f}  f1_stag={m['f1_stagnation']:.4f}  f1_prog={m['f1_progress']:.4f}  acc={m['accuracy']:.4f}")

    # ── Summary delta table ──
    print("\n" + "=" * 70)
    print("DELTA TABLE: Adapted 3-LF vs Original 3-LF")
    print("=" * 70)
    print(f"\n  {'Model':<6s} {'Orig macro_f1':>14s} {'Adapt macro_f1':>15s} {'Delta':>8s} {'Orig f1_stag':>13s} {'Adapt f1_stag':>14s} {'Delta':>8s}")

    for mn in ["GB", "RF", "LR"]:
        orig_m = results.get("original_3lf", {}).get("all", {}).get(mn, {})
        adapt_m = results.get("adapted_3lf", {}).get("all", {}).get(mn, {})
        if orig_m and adapt_m:
            d_macro = adapt_m["macro_f1"] - orig_m["macro_f1"]
            d_stag = adapt_m["f1_stagnation"] - orig_m["f1_stagnation"]
            print(f"  {mn:<6s} {orig_m['macro_f1']:>14.4f} {adapt_m['macro_f1']:>15.4f} {d_macro:>+8.4f} {orig_m['f1_stagnation']:>13.4f} {adapt_m['f1_stagnation']:>14.4f} {d_stag:>+8.4f}")

    # ── Phase 4: LF contribution analysis ──
    print("\n" + "=" * 70)
    print("PHASE 4: ADAPTED LF CONTRIBUTION ANALYSIS")
    print("=" * 70)

    # Which adapted LF fires most on stagnation windows?
    adapt3_stag_windows = [i for i, a in enumerate(adapted_labels) if a["label"] == STAGNATION]
    if adapt3_stag_windows:
        print(f"\n  Among {len(adapt3_stag_windows)} adapted-3LF stagnation windows:")
        for lf_name in ["command_repetition", "action_entropy", "output_stagnation"]:
            fired = sum(1 for i in adapt3_stag_windows if adapted_labels[i]["votes"].get(lf_name) == STAGNATION)
            print(f"    {lf_name}: fired on {fired}/{len(adapt3_stag_windows)} ({fired/len(adapt3_stag_windows):.3f})")

    # Unique contributions: windows where only one adapted LF fires stag
    for lf_name in ["command_repetition", "action_entropy", "output_stagnation"]:
        unique = 0
        for a in adapted_labels:
            if a["label"] == STAGNATION and a["votes"].get(lf_name) == STAGNATION:
                others = [a["votes"][n] for n in ["command_repetition", "action_entropy", "output_stagnation"] if n != lf_name]
                if all(v != STAGNATION for v in others):
                    unique += 1
        print(f"    {lf_name} sole stag trigger: {unique}")

    # ── Save results ──
    output = {
        "experiment": "d073-s1b-acr-adapted",
        "description": "ACR adapted LF relabeling + cross-agent transfer evaluation",
        "acr_lf_stats": {
            name: {
                "stag": lf_stats[name]["stag"],
                "prog": lf_stats[name]["prog"],
                "abstain": lf_stats[name]["abstain"],
                "coverage": round((lf_stats[name]["stag"] + lf_stats[name]["prog"]) / total, 4),
                "trigger_rate": round(lf_stats[name]["stag"] / total, 4),
            }
            for name, _ in ADAPTED_LFS_4
        },
        "label_comparison": {
            "original_3lf": {"nonabstain": orig_nonabstain, "stag": orig_stag, "stag_rate": round(orig_stag / max(orig_nonabstain, 1), 4)},
            "adapted_3lf": {"nonabstain": adapt3_nonabstain, "stag": adapt3_stag, "stag_rate": round(adapt3_stag / max(adapt3_nonabstain, 1), 4)},
            "adapted_4lf": {"nonabstain": adapt4_nonabstain, "stag": adapt4_stag, "stag_rate": round(adapt4_stag / max(adapt4_nonabstain, 1), 4)},
        },
        "cross_agent_results": results,
        "swe_train": {"n": int(len(y_swe)), "stag_rate": round(float(sum(y_swe == 0) / len(y_swe)), 4)},
    }

    with open(OUT_PATH, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nResults saved to {OUT_PATH}")


if __name__ == "__main__":
    main()
