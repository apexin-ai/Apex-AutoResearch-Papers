#!/usr/bin/env python3
"""Gold-set evaluation pipeline for agent_progress_probe.

Evaluates multiple stagnation detectors against human-annotated gold labels:
  - Structural classifiers (RF / GB / LR) trained on 30-dim hand-crafted features
  - GRU probe (ProgressProbe) on pre-computed embeddings
  - LLM-as-judge (from cached prediction JSONL)
  - Silver labels (majority-vote from labeling functions)

Pre-evaluation checks:
  - Inter-annotator agreement (Cohen's κ for 2 raters, Fleiss' κ for 3+)
    Gate: κ ≥ 0.8 passes; < 0.8 warns but does not abort.

Post-evaluation statistics:
  - Paired bootstrap 95% CIs on macro-F1 differences (1000 resamples)
  - McNemar's test for pairwise model comparisons

Inputs:
  --gold-file       CSV or JSONL with fields: window_id, gold_label (0/1),
                    optional annotator_id, confidence
  --predictions-dir Directory with model artifacts (checkpoints, embeddings,
                    windows_labeled.jsonl, trajectories, cached LLM predictions)
  --output-dir      Where to write results JSON and reliability diagram PDF

Outputs:
  {output-dir}/gold_set_results.json   — full metrics for every model
  {output-dir}/gold_set_reliability.pdf — calibration curves

Dependencies: torch, scikit-learn, numpy, matplotlib, scipy
"""

import argparse
import csv
import json
import re
import sys
import time
import warnings
from collections import Counter, defaultdict
from difflib import SequenceMatcher
from itertools import combinations
from pathlib import Path

import numpy as np
from sklearn.calibration import calibration_curve
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    cohen_kappa_score,
    f1_score,
    precision_score,
    recall_score,
)
from sklearn.preprocessing import StandardScaler

warnings.filterwarnings("ignore", category=UserWarning)

# ---------------------------------------------------------------------------
# Optional: torch (only needed for GRU probe)
# ---------------------------------------------------------------------------
try:
    import torch
    import torch.nn as nn
    from torch.utils.data import DataLoader

    HAS_TORCH = True
except ImportError:
    HAS_TORCH = False

# ---------------------------------------------------------------------------
# Try importing probe model from project artifacts
# ---------------------------------------------------------------------------
_ARTIFACTS_DIR = Path(__file__).resolve().parent.parent.parent / "artifacts"
if _ARTIFACTS_DIR.exists():
    sys.path.insert(0, str(_ARTIFACTS_DIR))
try:
    from probe_model import ProgressProbe, WindowDataset, collate_fn
    HAS_PROBE = True
except ImportError:
    HAS_PROBE = False


# ===========================================================================
# Metrics
# ===========================================================================

def compute_metrics(y_true, y_pred):
    """Per-model metrics: macro-F1, accuracy, per-class P/R/F1, Cohen's kappa."""
    return {
        "macro_f1": f1_score(y_true, y_pred, average="macro", zero_division=0),
        "accuracy": accuracy_score(y_true, y_pred),
        "precision_stag": precision_score(y_true, y_pred, pos_label=0, zero_division=0),
        "recall_stag": recall_score(y_true, y_pred, pos_label=0, zero_division=0),
        "f1_stag": f1_score(y_true, y_pred, pos_label=0, zero_division=0),
        "precision_prog": precision_score(y_true, y_pred, pos_label=1, zero_division=0),
        "recall_prog": recall_score(y_true, y_pred, pos_label=1, zero_division=0),
        "f1_prog": f1_score(y_true, y_pred, pos_label=1, zero_division=0),
        "cohens_kappa": cohen_kappa_score(y_true, y_pred),
    }


# ===========================================================================
# Structural feature extraction (mirrors non_nlp_baseline.py)
# ===========================================================================

EDIT_CMDS = {"edit", "str_replace", "create", "insert"}
SEARCH_CMDS = {"search_dir", "search_file", "find_file", "find", "grep", "view"}
NAV_CMDS = {"open", "goto", "scroll_down", "scroll_up", "cd", "ls", "cat"}

STRUCTURAL_FEATURE_NAMES = [
    "num_steps", "num_actions", "num_observations", "action_ratio",
    "mean_text_len", "std_text_len", "max_text_len", "min_text_len",
    "mean_action_len", "mean_obs_len", "text_len_trend",
    "num_commands", "mean_cmd_len", "max_cmd_len",
    "unique_cmd_ratio", "max_repeat_ratio",
    "num_edit_cmds", "num_search_cmds", "num_nav_cmds", "num_submit_cmds",
    "edit_ratio", "search_ratio",
    "avg_adjacent_cmd_sim", "max_adjacent_cmd_sim", "max_consecutive_similar",
    "num_errors", "num_test_outputs", "num_file_displays", "num_nonzero_exits",
    "is_short_trajectory",
]
_EXPECTED_FEATURE_DIM = 30


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
    """Extract 30-dim structural feature vector from a list of step dicts."""
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
    n_test_output = sum(
        1 for t in texts if ("PASSED" in t or "FAILED" in t) and "test" in t.lower()
    )
    n_file_display = sum(1 for t in texts if "[File:" in t)
    n_nonzero_exit = sum(
        1
        for _, t in observations
        if re.search(r"exit code [1-9]|returned non-zero|command not found", t)
    )

    vec = np.array(
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
    assert vec.shape[0] == _EXPECTED_FEATURE_DIM, (
        f"Structural feature dim mismatch: got {vec.shape[0]}, expected {_EXPECTED_FEATURE_DIM}"
    )
    assert len(STRUCTURAL_FEATURE_NAMES) == _EXPECTED_FEATURE_DIM, (
        f"STRUCTURAL_FEATURE_NAMES length {len(STRUCTURAL_FEATURE_NAMES)} != {_EXPECTED_FEATURE_DIM}"
    )
    return vec


# ===========================================================================
# Inter-annotator agreement
# ===========================================================================

def _fleiss_kappa(table):
    """Fleiss' κ for multiple raters.

    Args:
        table: (N, k) array where N = items, k = categories.
               table[i, j] = number of raters who assigned category j to item i.

    Reference: Fleiss, J.L. (1971). "Measuring nominal scale agreement among
    many raters." Psychological Bulletin, 76(5), 378–382.
    """
    N, k = table.shape
    n = table[0].sum()
    if n <= 1 or N == 0:
        return 0.0

    p_j = table.sum(axis=0) / (N * n)
    P_i = (np.sum(table ** 2, axis=1) - n) / (n * (n - 1))
    P_bar = np.mean(P_i)
    P_e = np.sum(p_j ** 2)

    if abs(1.0 - P_e) < 1e-9:
        return 1.0
    return (P_bar - P_e) / (1.0 - P_e)


def compute_inter_annotator_agreement(gold_records):
    """Compute inter-annotator agreement on gold labels.

    Args:
        gold_records: list of dicts with window_id, gold_label, optional annotator_id.

    Returns:
        dict with keys: n_annotators, metric ("cohens_kappa" | "fleiss_kappa" | None),
        value (float | None), passed (bool).
    """
    annotators = set()
    for r in gold_records:
        aid = r.get("annotator_id")
        if aid is not None:
            annotators.add(aid)

    if len(annotators) <= 1:
        print("  WARNING: Only 1 annotator (or no annotator_id field); skipping IAA check.")
        return {"n_annotators": max(len(annotators), 1), "metric": None, "value": None, "passed": True}

    by_window = defaultdict(dict)
    for r in gold_records:
        aid = r.get("annotator_id")
        if aid is not None:
            by_window[r["window_id"]][aid] = r["gold_label"]

    multi_annotated = {wid: labels for wid, labels in by_window.items() if len(labels) >= 2}
    if not multi_annotated:
        print("  WARNING: No windows with multiple annotations; skipping IAA check.")
        return {"n_annotators": len(annotators), "metric": None, "value": None, "passed": True}

    n_annotators = len(annotators)

    if n_annotators == 2:
        ann_list = sorted(annotators)
        y1, y2 = [], []
        for wid, labels in multi_annotated.items():
            if ann_list[0] in labels and ann_list[1] in labels:
                y1.append(labels[ann_list[0]])
                y2.append(labels[ann_list[1]])
        if not y1:
            return {"n_annotators": 2, "metric": None, "value": None, "passed": True}
        kappa = cohen_kappa_score(y1, y2)
        metric_name = "cohens_kappa"
    else:
        categories = sorted({r["gold_label"] for r in gold_records})
        cat_idx = {c: i for i, c in enumerate(categories)}
        table = np.zeros((len(multi_annotated), len(categories)), dtype=float)
        for row_i, (wid, labels) in enumerate(multi_annotated.items()):
            for aid, lbl in labels.items():
                table[row_i, cat_idx[lbl]] += 1
        kappa = _fleiss_kappa(table)
        metric_name = "fleiss_kappa"

    passed = kappa >= 0.8
    status = "PASS" if passed else "WARNING — below 0.8 threshold"
    print(f"  Inter-annotator agreement ({metric_name}): {kappa:.4f} [{status}]")
    print(f"  Annotators: {n_annotators}, windows with ≥2 annotations: {len(multi_annotated)}")
    if not passed:
        print("  WARNING: Low agreement. Results may be unreliable. Continuing anyway.")

    return {"n_annotators": n_annotators, "metric": metric_name, "value": round(kappa, 6), "passed": passed}


# ===========================================================================
# Pairwise statistical tests
# ===========================================================================

def _paired_bootstrap_ci(y_true, preds_a, preds_b, n_bootstrap=1000, seed=42):
    """Bootstrap 95% CI for the difference in macro-F1 between two models.

    Returns (mean_diff, ci_lower, ci_upper) where diff = F1(a) - F1(b).
    """
    rng = np.random.RandomState(seed)
    y_true = np.asarray(y_true)
    preds_a = np.asarray(preds_a)
    preds_b = np.asarray(preds_b)
    n = len(y_true)
    diffs = []
    for _ in range(n_bootstrap):
        idx = rng.randint(0, n, size=n)
        f1_a = f1_score(y_true[idx], preds_a[idx], average="macro", zero_division=0)
        f1_b = f1_score(y_true[idx], preds_b[idx], average="macro", zero_division=0)
        diffs.append(f1_a - f1_b)
    diffs = np.array(diffs)
    return float(np.mean(diffs)), float(np.percentile(diffs, 2.5)), float(np.percentile(diffs, 97.5))


def _mcnemar_test(y_true, preds_a, preds_b):
    """McNemar's test (with continuity correction) comparing two models.

    Returns p-value. Uses scipy.stats.chi2 for the p-value computation.
    """
    from scipy.stats import chi2

    y_true = np.asarray(y_true)
    preds_a = np.asarray(preds_a)
    preds_b = np.asarray(preds_b)

    correct_a = (preds_a == y_true)
    correct_b = (preds_b == y_true)
    # b: A correct, B wrong; c: A wrong, B correct
    b = int(np.sum(correct_a & ~correct_b))
    c = int(np.sum(~correct_a & correct_b))

    if b + c == 0:
        return 1.0
    stat = (abs(b - c) - 1) ** 2 / (b + c)
    return float(chi2.sf(stat, df=1))


def compute_pairwise_comparisons(gold_wids, gold_labels, model_preds):
    """Compute bootstrap CIs and McNemar tests for all model pairs.

    Args:
        gold_wids: list of window IDs (gold order).
        gold_labels: list of gold labels.
        model_preds: dict {model_name: {wid: predicted_label}}.

    Returns:
        dict of pairwise results keyed as "model_a_vs_model_b".
    """
    gold_map = dict(zip(gold_wids, gold_labels))
    model_names = list(model_preds.keys())
    results = {}

    for name_a, name_b in combinations(model_names, 2):
        preds_a_map = model_preds[name_a]
        preds_b_map = model_preds[name_b]
        common_wids = set(preds_a_map.keys()) & set(preds_b_map.keys()) & set(gold_map.keys())
        if len(common_wids) < 10:
            continue

        wids = sorted(common_wids)
        y_true = [gold_map[w] for w in wids]
        pa = [preds_a_map[w] for w in wids]
        pb = [preds_b_map[w] for w in wids]

        mean_diff, ci_lo, ci_hi = _paired_bootstrap_ci(y_true, pa, pb)
        p_val = _mcnemar_test(y_true, pa, pb)

        key = f"{name_a}_vs_{name_b}"
        results[key] = {
            "n_common": len(wids),
            "bootstrap_mean_diff": round(mean_diff, 6),
            "ci_95_lower": round(ci_lo, 6),
            "ci_95_upper": round(ci_hi, 6),
            "mcnemar_p": round(p_val, 6),
        }

    return results


# ===========================================================================
# Data loading helpers
# ===========================================================================

def load_gold_labels(path):
    """Load gold labels from CSV or JSONL.

    Returns list of dicts: [{window_id, gold_label, annotator_id?, confidence?}]
    """
    path = Path(path)
    records = []
    if path.suffix == ".csv":
        with open(path) as f:
            reader = csv.DictReader(f)
            for row in reader:
                rec = {
                    "window_id": row["window_id"],
                    "gold_label": int(row["gold_label"]),
                }
                if "annotator_id" in row:
                    rec["annotator_id"] = row["annotator_id"]
                if "confidence" in row:
                    rec["confidence"] = int(row["confidence"]) if row["confidence"] else None
                records.append(rec)
    else:
        with open(path) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                obj = json.loads(line)
                rec = {
                    "window_id": obj["window_id"],
                    "gold_label": int(obj["gold_label"]),
                }
                if "annotator_id" in obj:
                    rec["annotator_id"] = obj["annotator_id"]
                if "confidence" in obj:
                    rec["confidence"] = obj.get("confidence")
                records.append(rec)
    return records


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
                steps.append(
                    {
                        "role": s.get("role", "unknown"),
                        "text": s.get("text") or s.get("system_prompt") or "",
                    }
                )
            index[row_idx] = steps
    return index


def window_id_from_window(w):
    return f"{w['trajectory_id']}__w{w['window_idx']}"


def parse_row_index(trajectory_id):
    return int(trajectory_id.rsplit("__r", 1)[1])


# ===========================================================================
# Model evaluators
# ===========================================================================

def _align(gold_wids, gold_labels, prediction_map):
    """Align gold labels with predictions by window_id.

    Returns (aligned_gold, aligned_preds, n_missing).
    """
    aligned_gold, aligned_preds = [], []
    n_missing = 0
    for wid, gl in zip(gold_wids, gold_labels):
        pred = prediction_map.get(wid)
        if pred is None:
            n_missing += 1
            continue
        aligned_gold.append(gl)
        aligned_preds.append(pred)
    return aligned_gold, aligned_preds, n_missing


def evaluate_silver(gold_wids, gold_labels, wid_to_window):
    """Silver majority-vote labels vs gold."""
    pred_map = {}
    prob_map = {}
    conf_map = {}
    for wid in gold_wids:
        w = wid_to_window.get(wid)
        if w is None:
            continue
        pred_map[wid] = w["majority_label"]
        prob_map[wid] = float(w["majority_label"])
        conf_map[wid] = w.get("confidence", 0)
    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)
    if not gold_al:
        return None, 0, {}, {}, {}, {}
    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map, conf_map, pred_map


def evaluate_structural_clf(
    gold_wids,
    gold_labels,
    wid_to_noabs_idx,
    all_features,
    all_mv_labels,
    split_info,
    model_cls,
    model_kwargs,
    use_scaler=False,
):
    """Train structural classifier on silver train split, predict on gold windows."""
    keep_indices = split_info.get("keep_indices")
    if keep_indices is not None:
        feat_subset = all_features[keep_indices]
        label_subset = np.array(all_mv_labels)[keep_indices]
    else:
        feat_subset = all_features
        label_subset = np.array(all_mv_labels)

    train_idx = split_info["train_indices"]
    X_train = feat_subset[train_idx]
    y_train = label_subset[train_idx]

    scaler = None
    if use_scaler:
        scaler = StandardScaler()
        X_train = scaler.fit_transform(X_train)

    clf = model_cls(**model_kwargs)
    clf.fit(X_train, y_train)

    pred_map = {}
    prob_map = {}
    for wid in gold_wids:
        idx = wid_to_noabs_idx.get(wid)
        if idx is None:
            continue
        feat = all_features[idx].reshape(1, -1)
        if scaler is not None:
            feat = scaler.transform(feat)
        pred_map[wid] = int(clf.predict(feat)[0])
        if hasattr(clf, "predict_proba"):
            prob_map[wid] = float(clf.predict_proba(feat)[0, 1])

    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)
    if not gold_al:
        return None, 0, n_miss, prob_map, pred_map
    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map, pred_map


def evaluate_gru_probe(gold_wids, gold_labels, wid_to_emb_idx, embeddings, ckpt_path, device):
    """GRU probe evaluation on gold windows."""
    if not HAS_TORCH or not HAS_PROBE:
        return None, 0, len(gold_wids), {}, {}

    ckpt_path = Path(ckpt_path)
    if not ckpt_path.exists():
        return None, 0, len(gold_wids), {}, {}

    ckpt = torch.load(ckpt_path, map_location=device, weights_only=False)
    model = ProgressProbe(
        embed_dim=ckpt["embed_dim"],
        hidden_size=ckpt["hidden_size"],
        num_layers=ckpt["num_layers"],
    ).to(device)
    model.load_state_dict(ckpt["model_state_dict"])
    model.eval()

    ordered_wids = []
    gold_embs = []
    valid_gold = []
    n_miss = 0
    for wid, gl in zip(gold_wids, gold_labels):
        idx = wid_to_emb_idx.get(wid)
        if idx is None:
            n_miss += 1
            continue
        ordered_wids.append(wid)
        gold_embs.append(embeddings[idx])
        valid_gold.append(gl)

    if not gold_embs:
        return None, 0, n_miss, {}, {}

    ds = WindowDataset(gold_embs, valid_gold)
    loader = DataLoader(ds, batch_size=64, collate_fn=collate_fn)

    all_preds = []
    all_probs = []
    all_labels = []
    with torch.no_grad():
        for padded, labels, lengths in loader:
            logits = model(padded.to(device), lengths)
            probs = torch.sigmoid(logits).cpu()
            preds = (probs >= 0.5).long()
            all_preds.extend(preds.tolist())
            all_probs.extend(probs.tolist())
            all_labels.extend(labels.long().tolist())

    prob_map = {wid: p for wid, p in zip(ordered_wids, all_probs)}
    pred_map_out = {wid: p for wid, p in zip(ordered_wids, all_preds)}
    return compute_metrics(all_labels, all_preds), len(all_preds), n_miss, prob_map, pred_map_out


def evaluate_llm_judge(gold_wids, gold_labels, predictions_path):
    """LLM-as-judge from cached predictions JSONL/JSON."""
    predictions_path = Path(predictions_path)
    if not predictions_path.exists():
        return None, 0, len(gold_wids), {}, {}

    pred_index = {}
    if predictions_path.suffix == ".jsonl":
        with open(predictions_path) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                obj = json.loads(line)
                wid = f"{obj['trajectory_id']}__w{obj['window_idx']}"
                if obj.get("predicted_label", -1) != -1:
                    pred_index[wid] = obj
    else:
        with open(predictions_path) as f:
            data = json.load(f)
        for obj in data.get("results", []):
            wid = f"{obj['trajectory_id']}__w{obj['window_idx']}"
            if obj.get("predicted_label", -1) != -1:
                pred_index[wid] = obj

    pred_map = {wid: obj["predicted_label"] for wid, obj in pred_index.items()}
    prob_map = {}
    for wid, obj in pred_index.items():
        conf = obj.get("llm_confidence", 3)
        label = obj["predicted_label"]
        prob_map[wid] = label * (0.5 + conf / 10.0) + (1 - label) * (0.5 - conf / 10.0)

    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)
    if not gold_al:
        return None, 0, n_miss, prob_map, pred_map
    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map, pred_map


# ===========================================================================
# Confidence stratification (silver label confidence vs gold agreement)
# ===========================================================================

def confidence_stratification(gold_wids, gold_labels, wid_to_window):
    """Agreement between silver and gold stratified by silver confidence (1/2/3)."""
    strata = {1: {"agree": 0, "total": 0}, 2: {"agree": 0, "total": 0}, 3: {"agree": 0, "total": 0}}
    for wid, gl in zip(gold_wids, gold_labels):
        w = wid_to_window.get(wid)
        if w is None:
            continue
        conf = w.get("confidence", 0)
        if conf not in strata:
            continue
        strata[conf]["total"] += 1
        if w["majority_label"] == gl:
            strata[conf]["agree"] += 1

    result = {}
    for conf in [1, 2, 3]:
        total = strata[conf]["total"]
        agree = strata[conf]["agree"]
        result[f"conf_{conf}"] = {
            "total": total,
            "agree": agree,
            "agreement_rate": agree / total if total > 0 else None,
        }
    return result


# ===========================================================================
# Reliability diagram
# ===========================================================================

def plot_reliability_diagram(model_probs, gold_wids, gold_labels, output_path, n_bins=10):
    """Plot calibration curves for all models with predicted probabilities."""
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    plt.rcParams.update(
        {
            "font.family": "serif",
            "font.size": 10,
            "axes.labelsize": 11,
            "axes.titlesize": 12,
            "legend.fontsize": 9,
            "figure.dpi": 150,
        }
    )

    gold_map = dict(zip(gold_wids, gold_labels))

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.5), gridspec_kw={"width_ratios": [2, 1]})

    ax1.plot([0, 1], [0, 1], "k--", lw=1, label="Perfect calibration")

    colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"]
    for i, (model_name, prob_map) in enumerate(model_probs.items()):
        y_true, y_prob = [], []
        for wid, prob in prob_map.items():
            gl = gold_map.get(wid)
            if gl is not None:
                y_true.append(gl)
                y_prob.append(prob)
        if len(y_true) < 10:
            continue

        y_true = np.array(y_true)
        y_prob = np.array(y_prob)

        fraction_pos, mean_predicted = calibration_curve(
            y_true, y_prob, n_bins=n_bins, strategy="uniform"
        )
        ax1.plot(
            mean_predicted, fraction_pos,
            "o-", color=colors[i % len(colors)], label=model_name, markersize=4,
        )

        ax2.hist(
            y_prob, bins=n_bins, range=(0, 1),
            alpha=0.5, color=colors[i % len(colors)], label=model_name,
        )

    ax1.set_xlabel("Mean predicted probability")
    ax1.set_ylabel("Fraction of positives (progress)")
    ax1.set_title("Reliability Diagram")
    ax1.legend(loc="lower right")
    ax1.set_xlim(-0.02, 1.02)
    ax1.set_ylim(-0.02, 1.02)
    ax1.set_aspect("equal")

    ax2.set_xlabel("Predicted probability")
    ax2.set_ylabel("Count")
    ax2.set_title("Prediction Distribution")
    ax2.legend(loc="upper right")

    fig.tight_layout()
    fig.savefig(output_path, bbox_inches="tight")
    plt.close(fig)


# ===========================================================================
# Console summary
# ===========================================================================

def print_summary_table(results):
    """Print markdown-formatted summary to console."""
    header = (
        "| Model               | N     | Macro-F1 | Accuracy | P(stag) | R(stag) "
        "| F1(stag) | P(prog) | R(prog) | F1(prog) | Cohen κ |"
    )
    sep = "|" + "|".join(["---"] * 11) + "|"
    print(header)
    print(sep)
    for name, metrics, n, n_miss in results:
        if metrics is None:
            print(f"| {name:19s} | {'—':>5s} | SKIPPED (missing={n_miss}) |{'|' * 8}")
            continue
        print(
            f"| {name:19s} "
            f"| {n:5d} "
            f"| {metrics['macro_f1']:.4f}   "
            f"| {metrics['accuracy']:.4f}   "
            f"| {metrics['precision_stag']:.4f}  "
            f"| {metrics['recall_stag']:.4f}  "
            f"| {metrics['f1_stag']:.4f}   "
            f"| {metrics['precision_prog']:.4f}  "
            f"| {metrics['recall_prog']:.4f}  "
            f"| {metrics['f1_prog']:.4f}   "
            f"| {metrics['cohens_kappa']:.4f}  |"
        )


# ===========================================================================
# Main
# ===========================================================================

ALL_MODELS = ["silver", "rf", "gb", "lr", "gru_probe", "llm_judge"]


def main():
    parser = argparse.ArgumentParser(
        description="Gold-set evaluation pipeline for agent_progress_probe",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--gold-file", required=True,
        help="Path to gold label file (CSV or JSONL). "
             "Required fields: window_id, gold_label (0=stagnation, 1=progress). "
             "Optional: annotator_id, confidence.",
    )
    parser.add_argument(
        "--predictions-dir", required=True,
        help="Directory containing model artifacts: "
             "data/windows_labeled.jsonl, data/embeddings.pt, "
             "checkpoints/best_model.pt, checkpoints/split_info.json, "
             "data/swe_agent_trajectories_5000.jsonl, "
             "results/llm_judge_results.json",
    )
    parser.add_argument(
        "--output-dir", default="artifacts",
        help="Output directory for results JSON and reliability PDF (default: artifacts)",
    )
    parser.add_argument(
        "--models", nargs="+", default=ALL_MODELS, choices=ALL_MODELS,
        help="Which models to evaluate (default: all). "
             "Choices: silver, rf, gb, lr, gru_probe, llm_judge",
    )
    parser.add_argument("--device", default=None, help="Torch device (default: auto)")
    parser.add_argument(
        "--llm-predictions", default=None,
        help="Override path to LLM-as-judge cached predictions (JSON or JSONL)",
    )
    parser.add_argument(
        "--checkpoint", default=None,
        help="Override path to GRU probe checkpoint (default: {predictions-dir}/checkpoints/best_model.pt)",
    )
    parser.add_argument(
        "--trajectories", default=None,
        help="Override path to raw trajectories JSONL",
    )
    parser.add_argument("--n-bins", type=int, default=10, help="Calibration curve bins")
    args = parser.parse_args()

    t_start = time.time()
    pdir = Path(args.predictions_dir)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    device = args.device
    if device is None and HAS_TORCH:
        device = "cuda" if torch.cuda.is_available() else "cpu"
    elif device is None:
        device = "cpu"

    selected_models = set(args.models)

    # ------------------------------------------------------------------
    # 1. Load gold labels
    # ------------------------------------------------------------------
    print(f"Loading gold labels: {args.gold_file}")
    gold_records = load_gold_labels(args.gold_file)
    gold_wids = [r["window_id"] for r in gold_records]
    gold_labels = [r["gold_label"] for r in gold_records]
    gold_dist = Counter(gold_labels)
    print(f"  Total: {len(gold_labels)}, stag={gold_dist.get(0, 0)}, prog={gold_dist.get(1, 0)}")

    # ------------------------------------------------------------------
    # 1b. Inter-annotator agreement check
    # ------------------------------------------------------------------
    print("\nInter-annotator agreement check:")
    iaa_result = compute_inter_annotator_agreement(gold_records)

    # ------------------------------------------------------------------
    # 2. Load windows_labeled.jsonl
    # ------------------------------------------------------------------
    windows_path = None
    for candidate in [
        pdir / "data" / "windows_labeled.jsonl",
        pdir / "windows_labeled.jsonl",
        pdir / "artifacts" / "data" / "windows_labeled.jsonl",
    ]:
        if candidate.exists():
            windows_path = candidate
            break
    if windows_path is None:
        print("ERROR: windows_labeled.jsonl not found under predictions-dir")
        sys.exit(1)
    print(f"Loading windows: {windows_path}")
    all_windows = load_windows_jsonl(str(windows_path))
    non_abstain = [w for w in all_windows if w.get("majority_label", -1) != -1]
    print(f"  Total: {len(all_windows)}, non-abstain: {len(non_abstain)}")

    wid_to_window = {window_id_from_window(w): w for w in non_abstain}
    wid_to_noabs_idx = {window_id_from_window(w): i for i, w in enumerate(non_abstain)}

    # ------------------------------------------------------------------
    # 3. Load split info
    # ------------------------------------------------------------------
    split_info_path = None
    for candidate in [
        pdir / "checkpoints" / "split_info.json",
        pdir / "split_info.json",
        pdir / "artifacts" / "split_info.json",
    ]:
        if candidate.exists():
            split_info_path = candidate
            break
    split_info = None
    if split_info_path is not None:
        print(f"Loading split info: {split_info_path}")
        with open(split_info_path) as f:
            split_info = json.load(f)

    # ------------------------------------------------------------------
    # 4. Evaluate models
    # ------------------------------------------------------------------
    results = []
    model_probs = {}
    model_preds = {}

    # --- Silver labels ---
    if "silver" in selected_models:
        print("\nEvaluating: Silver (MV) Labels vs Gold ...")
        m, n, n_miss, prob_map, conf_map, pred_map = evaluate_silver(
            gold_wids, gold_labels, wid_to_window
        )
        if m:
            print(f"  macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}")
        results.append(("Silver (MV)", m, n, n_miss))
        if prob_map:
            model_probs["Silver (MV)"] = prob_map
        if pred_map:
            model_preds["Silver (MV)"] = pred_map

    # --- Structural classifiers (RF, GB, LR) ---
    need_structural = selected_models & {"rf", "gb", "lr"}
    if need_structural:
        traj_path = Path(args.trajectories) if args.trajectories else None
        if traj_path is None:
            for candidate in [
                pdir / "data" / "swe_agent_trajectories_5000.jsonl",
                pdir / "swe_agent_trajectories_5000.jsonl",
                pdir / "artifacts" / "data" / "swe_agent_trajectories_5000.jsonl",
                pdir / "data" / "swe_agent_trajectories_1000.jsonl",
                pdir / "artifacts" / "data" / "swe_agent_trajectories_1000.jsonl",
            ]:
                if candidate.exists():
                    traj_path = candidate
                    break

        if traj_path is not None and traj_path.exists() and split_info is not None:
            print(f"\nBuilding structural features (trajectories: {traj_path}) ...")
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

            struct_configs = {
                "rf": (
                    "Structural RF",
                    RandomForestClassifier,
                    {"n_estimators": 200, "max_depth": 10, "random_state": 42, "n_jobs": -1},
                    False,
                ),
                "gb": (
                    "Structural GB",
                    GradientBoostingClassifier,
                    {"n_estimators": 200, "learning_rate": 0.1, "max_depth": 5, "random_state": 42},
                    False,
                ),
                "lr": (
                    "Structural LR",
                    LogisticRegression,
                    {"max_iter": 2000, "C": 1.0, "solver": "lbfgs"},
                    True,
                ),
            }
            for key in ["rf", "gb", "lr"]:
                if key not in selected_models:
                    continue
                name, cls, kwargs, scaler = struct_configs[key]
                print(f"  Evaluating {name} ...")
                m, n, n_miss, prob_map, pred_map = evaluate_structural_clf(
                    gold_wids, gold_labels, wid_to_noabs_idx,
                    all_features, all_mv_labels, split_info,
                    cls, kwargs, use_scaler=scaler,
                )
                if m:
                    print(f"    macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}")
                results.append((name, m, n, n_miss))
                if prob_map:
                    model_probs[name] = prob_map
                if pred_map:
                    model_preds[name] = pred_map
        else:
            reason = "trajectories not found" if traj_path is None else "split_info not found"
            print(f"\nSkipping structural classifiers: {reason}")
            for key in ["rf", "gb", "lr"]:
                if key in selected_models:
                    name = {"rf": "Structural RF", "gb": "Structural GB", "lr": "Structural LR"}[key]
                    results.append((name, None, 0, len(gold_wids)))

    # --- GRU Probe ---
    if "gru_probe" in selected_models:
        ckpt_path = Path(args.checkpoint) if args.checkpoint else None
        if ckpt_path is None:
            for candidate in [
                pdir / "checkpoints" / "best_model.pt",
                pdir / "best_model.pt",
                pdir / "artifacts" / "best_model.pt",
            ]:
                if candidate.exists():
                    ckpt_path = candidate
                    break

        emb_path = None
        for candidate in [
            pdir / "data" / "embeddings.pt",
            pdir / "embeddings.pt",
            pdir / "artifacts" / "data" / "embeddings.pt",
        ]:
            if candidate.exists():
                emb_path = candidate
                break

        print(f"\nEvaluating: GRU Probe ...")
        if HAS_TORCH and HAS_PROBE and emb_path is not None and ckpt_path is not None:
            emb_data = torch.load(emb_path, map_location="cpu", weights_only=False)
            embeddings = emb_data["embeddings"]

            wid_to_emb_idx = {}
            if len(embeddings) == len(non_abstain):
                for i, w in enumerate(non_abstain):
                    wid_to_emb_idx[window_id_from_window(w)] = i
            else:
                for i in range(min(len(embeddings), len(non_abstain))):
                    wid_to_emb_idx[window_id_from_window(non_abstain[i])] = i

            m, n, n_miss, prob_map, pred_map = evaluate_gru_probe(
                gold_wids, gold_labels, wid_to_emb_idx, embeddings, str(ckpt_path), device
            )
            if m:
                print(f"  macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}")
            results.append(("GRU Probe", m, n, n_miss))
            if prob_map:
                model_probs["GRU Probe"] = prob_map
            if pred_map:
                model_preds["GRU Probe"] = pred_map
        else:
            missing = []
            if not HAS_TORCH:
                missing.append("torch")
            if not HAS_PROBE:
                missing.append("probe_model")
            if emb_path is None:
                missing.append("embeddings.pt")
            if ckpt_path is None:
                missing.append("checkpoint")
            print(f"  SKIPPED: {', '.join(missing)} not available")
            results.append(("GRU Probe", None, 0, len(gold_wids)))

    # --- LLM-as-judge ---
    if "llm_judge" in selected_models:
        llm_path = Path(args.llm_predictions) if args.llm_predictions else None
        if llm_path is None:
            for candidate in [
                pdir / "results" / "llm_judge_results.json",
                pdir / "llm_judge_results.json",
                pdir / "artifacts" / "results" / "llm_judge_results.json",
                pdir / "results" / "llm_judge_results.jsonl",
            ]:
                if candidate.exists():
                    llm_path = candidate
                    break

        print(f"\nEvaluating: LLM-as-Judge ...")
        if llm_path is not None and llm_path.exists():
            m, n, n_miss, prob_map, pred_map = evaluate_llm_judge(gold_wids, gold_labels, llm_path)
            if m:
                print(f"  macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}")
            results.append(("LLM-as-Judge", m, n, n_miss))
            if prob_map:
                model_probs["LLM-as-Judge (pseudo-probability)"] = prob_map
            if pred_map:
                model_preds["LLM-as-Judge"] = pred_map
        else:
            print(f"  SKIPPED: no cached predictions found")
            results.append(("LLM-as-Judge", None, 0, len(gold_wids)))

    # ------------------------------------------------------------------
    # 5. Confidence stratification
    # ------------------------------------------------------------------
    print("\nConfidence stratification (silver conf vs gold agreement):")
    conf_strat = confidence_stratification(gold_wids, gold_labels, wid_to_window)
    for conf_key in ["conf_1", "conf_2", "conf_3"]:
        s = conf_strat[conf_key]
        rate = f"{s['agreement_rate']:.4f}" if s["agreement_rate"] is not None else "N/A"
        print(f"  {conf_key}: {s['agree']}/{s['total']} = {rate}")

    # ------------------------------------------------------------------
    # 5b. Pairwise statistical comparisons
    # ------------------------------------------------------------------
    pairwise = {}
    if len(model_preds) >= 2:
        print("\nPairwise statistical comparisons (bootstrap CI on macro-F1 diff + McNemar):")
        pairwise = compute_pairwise_comparisons(gold_wids, gold_labels, model_preds)
        for pair_key, stats in pairwise.items():
            sig = " *" if stats["mcnemar_p"] < 0.05 else ""
            print(
                f"  {pair_key}: ΔF1={stats['bootstrap_mean_diff']:+.4f} "
                f"CI=[{stats['ci_95_lower']:+.4f}, {stats['ci_95_upper']:+.4f}] "
                f"McNemar p={stats['mcnemar_p']:.4f}{sig}"
            )

    # ------------------------------------------------------------------
    # 6. Console summary
    # ------------------------------------------------------------------
    print("\n" + "=" * 120)
    print("GOLD SET EVALUATION RESULTS")
    print("=" * 120)
    print_summary_table(results)

    # ------------------------------------------------------------------
    # 7. Reliability diagram
    # ------------------------------------------------------------------
    pdf_path = output_dir / "gold_set_reliability.pdf"
    if model_probs:
        try:
            plot_reliability_diagram(
                model_probs, gold_wids, gold_labels, str(pdf_path), n_bins=args.n_bins
            )
            print(f"\nReliability diagram: {pdf_path}")
        except Exception as e:
            print(f"\nFailed to generate reliability diagram: {e}")
    else:
        print("\nNo probability estimates available; skipping reliability diagram.")

    # ------------------------------------------------------------------
    # 8. JSON output
    # ------------------------------------------------------------------
    elapsed = time.time() - t_start
    output = {
        "gold_file": str(args.gold_file),
        "gold_distribution": {"total": len(gold_labels), "stagnation": gold_dist.get(0, 0), "progress": gold_dist.get(1, 0)},
        "inter_annotator_agreement": iaa_result,
        "confidence_stratification": conf_strat,
        "pairwise_comparisons": pairwise,
        "models": {},
        "elapsed_seconds": round(elapsed, 2),
    }
    for name, metrics, n, n_miss in results:
        output["models"][name] = {
            "n_evaluated": n,
            "n_missing": n_miss,
            "metrics": {k: round(v, 6) for k, v in metrics.items()} if metrics else None,
        }

    json_path = output_dir / "gold_set_results.json"
    with open(json_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"Results JSON: {json_path}")
    print(f"Elapsed: {elapsed:.1f}s")


if __name__ == "__main__":
    main()
