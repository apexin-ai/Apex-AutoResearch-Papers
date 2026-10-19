#!/usr/bin/env python3
"""exp-012: Extract sycophancy direction (d_syc) from Llama-3-8B-Instruct and evaluate via AUROC.

Replicates exp-001 (Qwen3-8B, AUROC=0.827) on Llama-3-8B-Instruct for cross-model validation.

Input:  calibration_v2_1_expanded.jsonl  (181 contrastive pairs, 362 samples)
        Each sample: {pair_id, condition, domain, evidence_strength, turns}
        condition ∈ {valid_correction, invalid_pressure}

Output: results/exp012_llama_direction/
        ├── directions.pt          — d_syc per layer (L16-L31), L2-normalized
        ├── activations.pt         — hidden states at last-token position
        └── evaluation_report.json — 5-fold CV AUROC, style-controlled AUROC, per-layer breakdown

Usage:
    python run_exp012_llama_direction.py --model-path /path/to/Llama-3-8B-Instruct
    python run_exp012_llama_direction.py --help
"""

import argparse
import json
import logging
import sys
import time
from collections import defaultdict
from pathlib import Path

import numpy as np
import torch
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import StratifiedKFold
from tqdm import tqdm
from transformers import AutoModelForCausalLM, AutoTokenizer

logger = logging.getLogger(__name__)

LAYER_START = 16
LAYER_END = 32  # exclusive; layers 16-31
DEFAULT_MODEL_PATH = "/root/autodl-tmp/models/Meta-Llama-3-8B-Instruct"
DEFAULT_DATA_PATH = "/root/mvp_v2_1_expanded/data/calibration_v2_1_expanded.jsonl"
DEFAULT_OUTPUT_DIR = "/root/contrastive_entrain_calib/results/exp012_llama_direction"


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------

def load_samples(path: str) -> list[dict]:
    samples = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                samples.append(json.loads(line))
    return samples


def group_pairs(samples: list[dict]) -> dict[str, dict[str, dict]]:
    """Group samples by pair_id → {condition: sample}. Keep only complete pairs."""
    grouped: dict[str, dict[str, dict]] = defaultdict(dict)
    for s in samples:
        grouped[s["pair_id"]][s["condition"]] = s

    complete = {}
    for pid, conds in grouped.items():
        if "valid_correction" in conds and "invalid_pressure" in conds:
            complete[pid] = conds
        else:
            logger.warning("Incomplete pair '%s': %s", pid, list(conds.keys()))
    return complete


# ---------------------------------------------------------------------------
# Activation extraction
# ---------------------------------------------------------------------------

def extract_activations(
    model,
    tokenizer,
    samples: list[dict],
    device: torch.device,
    layer_start: int,
    layer_end: int,
) -> list[dict]:
    """Forward pass each sample, extract hidden states at last-token position.

    Returns list of {pair_id, condition, domain, evidence_strength, activation}
    where activation is a Tensor of shape (num_selected_layers, hidden_dim).
    """
    results = []

    for sample in tqdm(samples, desc="Extracting activations"):
        messages = [{"role": t["role"], "content": t["content"]} for t in sample["turns"]]
        input_ids = tokenizer.apply_chat_template(
            messages, add_generation_prompt=True, tokenize=True, return_tensors="pt"
        ).to(device)

        with torch.no_grad():
            outputs = model(input_ids, output_hidden_states=True)

        # hidden_states: tuple of (num_layers+1) tensors, each (1, seq_len, hidden_dim)
        # hidden_states[0] = embedding, hidden_states[k+1] = layer k output
        last_pos = input_ids.shape[1] - 1
        layer_acts = []
        for layer_idx in range(layer_start, layer_end):
            h = outputs.hidden_states[layer_idx + 1][0, last_pos, :]
            layer_acts.append(h.cpu().float())

        activation = torch.stack(layer_acts)  # (num_selected_layers, hidden_dim)

        results.append({
            "pair_id": sample["pair_id"],
            "condition": sample["condition"],
            "domain": sample["domain"],
            "evidence_strength": sample["evidence_strength"],
            "activation": activation,
        })

    return results


# ---------------------------------------------------------------------------
# Direction computation
# ---------------------------------------------------------------------------

def compute_direction(
    act_records: list[dict],
    pair_ids: list[str],
) -> torch.Tensor:
    """Compute d_syc = mean(invalid_pressure) - mean(valid_correction), L2-normalized.

    Returns (num_layers, hidden_dim).
    """
    pid_set = set(pair_ids)
    pos_acts, neg_acts = [], []
    for rec in act_records:
        if rec["pair_id"] not in pid_set:
            continue
        if rec["condition"] == "invalid_pressure":
            pos_acts.append(rec["activation"])
        else:
            neg_acts.append(rec["activation"])

    pos_mean = torch.stack(pos_acts).mean(dim=0)
    neg_mean = torch.stack(neg_acts).mean(dim=0)
    direction = pos_mean - neg_mean
    norms = direction.norm(dim=-1, keepdim=True).clamp(min=1e-8)
    return direction / norms


# ---------------------------------------------------------------------------
# AUROC evaluation
# ---------------------------------------------------------------------------

def compute_auroc_per_layer(
    act_records: list[dict],
    d_syc: torch.Tensor,
    pair_ids: list[str],
) -> dict[int, float]:
    """Project test activations onto d_syc, compute AUROC per layer.

    Returns {layer_offset: auroc} where layer_offset 0 = LAYER_START.
    """
    pid_set = set(pair_ids)
    num_layers = d_syc.shape[0]

    labels = []
    scores: dict[int, list[float]] = {l: [] for l in range(num_layers)}

    for rec in act_records:
        if rec["pair_id"] not in pid_set:
            continue
        label = 1 if rec["condition"] == "invalid_pressure" else 0
        labels.append(label)
        for l in range(num_layers):
            s = torch.dot(rec["activation"][l], d_syc[l]).item()
            scores[l].append(s)

    labels_arr = np.array(labels)
    results = {}
    for l in range(num_layers):
        if len(np.unique(labels_arr)) < 2:
            results[l] = float("nan")
        else:
            results[l] = roc_auc_score(labels_arr, np.array(scores[l]))
    return results


def compute_paired_auroc(
    act_records: list[dict],
    d_syc: torch.Tensor,
    pair_ids: list[str],
    layer_idx: int,
) -> float:
    """Style-controlled AUROC: fraction of pairs where invalid_pressure scores higher.

    Controls for question content by comparing within each pair.
    """
    pid_set = set(pair_ids)
    by_pair: dict[str, dict[str, torch.Tensor]] = defaultdict(dict)
    for rec in act_records:
        if rec["pair_id"] in pid_set:
            by_pair[rec["pair_id"]][rec["condition"]] = rec["activation"]

    concordant = 0
    total = 0
    for pid in pair_ids:
        if pid not in by_pair:
            continue
        if "invalid_pressure" not in by_pair[pid] or "valid_correction" not in by_pair[pid]:
            continue
        s_pos = torch.dot(by_pair[pid]["invalid_pressure"][layer_idx], d_syc[layer_idx]).item()
        s_neg = torch.dot(by_pair[pid]["valid_correction"][layer_idx], d_syc[layer_idx]).item()
        if s_pos > s_neg:
            concordant += 1
        elif s_pos == s_neg:
            concordant += 0.5
        total += 1

    return concordant / total if total > 0 else float("nan")


def kfold_cv_auroc(
    act_records: list[dict],
    pairs: dict[str, dict[str, dict]],
    n_folds: int = 5,
    seed: int = 42,
) -> dict:
    """5-fold stratified cross-validation AUROC.

    Stratification by domain. Returns per-fold and aggregated results.
    """
    pair_ids = sorted(pairs.keys())
    domains = np.array([pairs[pid]["valid_correction"]["domain"] for pid in pair_ids])

    skf = StratifiedKFold(n_splits=n_folds, shuffle=True, random_state=seed)

    fold_results = []
    all_aurocs_per_layer: dict[int, list[float]] = defaultdict(list)

    for fold_i, (train_idx, test_idx) in enumerate(skf.split(pair_ids, domains)):
        train_pids = [pair_ids[i] for i in train_idx]
        test_pids = [pair_ids[i] for i in test_idx]

        d_syc = compute_direction(act_records, train_pids)
        aurocs = compute_auroc_per_layer(act_records, d_syc, test_pids)

        best_layer = max(aurocs, key=aurocs.get)
        best_auroc = aurocs[best_layer]

        paired_auroc = compute_paired_auroc(act_records, d_syc, test_pids, best_layer)

        fold_results.append({
            "fold": fold_i,
            "n_train": len(train_pids),
            "n_test": len(test_pids),
            "best_layer_offset": best_layer,
            "best_layer_absolute": best_layer + LAYER_START,
            "best_auroc": best_auroc,
            "style_controlled_auroc": paired_auroc,
            "per_layer_auroc": {str(LAYER_START + l): v for l, v in aurocs.items()},
        })

        for l, v in aurocs.items():
            all_aurocs_per_layer[l].append(v)

        logger.info(
            "Fold %d: best AUROC=%.4f (layer %d), style-controlled=%.4f",
            fold_i, best_auroc, best_layer + LAYER_START, paired_auroc,
        )

    mean_aurocs = {l: np.mean(vs) for l, vs in all_aurocs_per_layer.items()}
    std_aurocs = {l: np.std(vs) for l, vs in all_aurocs_per_layer.items()}
    best_layer = max(mean_aurocs, key=mean_aurocs.get)

    return {
        "folds": fold_results,
        "mean_auroc_per_layer": {str(LAYER_START + l): v for l, v in mean_aurocs.items()},
        "std_auroc_per_layer": {str(LAYER_START + l): v for l, v in std_aurocs.items()},
        "best_layer_absolute": best_layer + LAYER_START,
        "best_mean_auroc": mean_aurocs[best_layer],
        "best_std_auroc": std_aurocs[best_layer],
        "mean_style_controlled_auroc": np.mean([f["style_controlled_auroc"] for f in fold_results]),
    }


def stratified_breakdown(
    act_records: list[dict],
    d_syc: torch.Tensor,
    pair_ids: list[str],
    best_layer: int,
    group_key: str,
) -> dict[str, float]:
    """AUROC broken down by a metadata field (domain, evidence_strength)."""
    pid_set = set(pair_ids)
    groups: dict[str, list[dict]] = defaultdict(list)
    for rec in act_records:
        if rec["pair_id"] in pid_set:
            groups[str(rec[group_key])].append(rec)

    results = {}
    for group_val, group_recs in sorted(groups.items()):
        labels = []
        scores = []
        for rec in group_recs:
            labels.append(1 if rec["condition"] == "invalid_pressure" else 0)
            scores.append(torch.dot(rec["activation"][best_layer], d_syc[best_layer]).item())

        labels_arr = np.array(labels)
        if len(np.unique(labels_arr)) < 2:
            results[group_val] = float("nan")
        else:
            results[group_val] = roc_auc_score(labels_arr, np.array(scores))

    return results


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="exp-012: d_syc extraction + AUROC for Llama-3-8B-Instruct"
    )
    parser.add_argument(
        "--model-path", default=DEFAULT_MODEL_PATH,
        help=f"Model path (default: {DEFAULT_MODEL_PATH})",
    )
    parser.add_argument(
        "--data-path", default=DEFAULT_DATA_PATH,
        help=f"Calibration JSONL path (default: {DEFAULT_DATA_PATH})",
    )
    parser.add_argument(
        "--output-dir", default=DEFAULT_OUTPUT_DIR,
        help=f"Output directory (default: {DEFAULT_OUTPUT_DIR})",
    )
    parser.add_argument("--device", default="cuda:0", help="Torch device (default: cuda:0)")
    parser.add_argument("--n-folds", type=int, default=5, help="CV folds (default: 5)")
    parser.add_argument("--seed", type=int, default=42, help="Random seed (default: 42)")
    parser.add_argument(
        "--max-samples", type=int, default=None,
        help="Limit samples for debugging",
    )
    parser.add_argument(
        "--skip-extraction", action="store_true",
        help="Skip extraction, load existing activations.pt",
    )
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )

    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    act_path = out_dir / "activations.pt"

    # --- Load data ---
    logger.info("Loading data from %s", args.data_path)
    samples = load_samples(args.data_path)
    if args.max_samples:
        samples = samples[:args.max_samples]
    pairs = group_pairs(samples)
    logger.info("Loaded %d samples, %d complete pairs", len(samples), len(pairs))

    # --- Extract activations ---
    if args.skip_extraction and act_path.exists():
        logger.info("Loading cached activations from %s", act_path)
        act_records = torch.load(act_path, map_location="cpu", weights_only=False)
    else:
        device = torch.device(args.device)
        logger.info("Loading tokenizer from %s", args.model_path)
        tokenizer = AutoTokenizer.from_pretrained(args.model_path)
        if tokenizer.pad_token_id is None:
            tokenizer.pad_token_id = tokenizer.eos_token_id

        logger.info("Loading model from %s", args.model_path)
        model = AutoModelForCausalLM.from_pretrained(
            args.model_path,
            torch_dtype=torch.bfloat16,
            device_map=args.device,
        )
        model.eval()

        t0 = time.time()
        act_records = extract_activations(
            model, tokenizer, samples, device, LAYER_START, LAYER_END
        )
        elapsed = time.time() - t0
        logger.info("Extraction done in %.1fs (%.2fs/sample)", elapsed, elapsed / len(samples))

        logger.info("Saving activations to %s", act_path)
        torch.save(act_records, act_path)

        del model
        torch.cuda.empty_cache()

    # --- 5-fold CV AUROC ---
    logger.info("Running %d-fold stratified CV AUROC", args.n_folds)
    cv_results = kfold_cv_auroc(act_records, pairs, args.n_folds, args.seed)

    # --- Full-data direction + stratified breakdown ---
    all_pair_ids = sorted(pairs.keys())
    d_syc_full = compute_direction(act_records, all_pair_ids)
    best_layer_offset = cv_results["best_layer_absolute"] - LAYER_START

    breakdown_domain = stratified_breakdown(
        act_records, d_syc_full, all_pair_ids, best_layer_offset, "domain"
    )
    breakdown_evidence = stratified_breakdown(
        act_records, d_syc_full, all_pair_ids, best_layer_offset, "evidence_strength"
    )
    full_aurocs = compute_auroc_per_layer(act_records, d_syc_full, all_pair_ids)
    full_paired = compute_paired_auroc(act_records, d_syc_full, all_pair_ids, best_layer_offset)

    # --- Save directions ---
    directions_path = out_dir / "directions.pt"
    torch.save({
        "d_syc": d_syc_full,
        "layer_range": (LAYER_START, LAYER_END),
        "pair_ids": all_pair_ids,
        "metadata": {
            "model": args.model_path,
            "num_pairs": len(pairs),
            "num_layers": LAYER_END - LAYER_START,
            "hidden_dim": d_syc_full.shape[-1],
            "seed": args.seed,
        },
    }, directions_path)
    logger.info("Saved directions to %s", directions_path)

    # --- Build report ---
    report = {
        "experiment": "exp-012",
        "model": args.model_path,
        "data": args.data_path,
        "num_samples": len(samples),
        "num_pairs": len(pairs),
        "layer_range": [LAYER_START, LAYER_END - 1],
        "cv": cv_results,
        "full_data": {
            "best_layer": cv_results["best_layer_absolute"],
            "per_layer_auroc": {str(LAYER_START + l): v for l, v in full_aurocs.items()},
            "style_controlled_auroc": full_paired,
            "breakdown_by_domain": breakdown_domain,
            "breakdown_by_evidence_strength": breakdown_evidence,
        },
    }

    report_path = out_dir / "evaluation_report.json"
    with open(report_path, "w") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    logger.info("Saved report to %s", report_path)

    # --- Print summary ---
    print("\n" + "=" * 60)
    print("EXP-012: Llama-3-8B-Instruct d_syc DIRECTION EVALUATION")
    print("=" * 60)
    print(f"Pairs: {len(pairs)}  |  Samples: {len(samples)}")
    print(f"Layers: {LAYER_START}-{LAYER_END - 1}  |  Hidden dim: {d_syc_full.shape[-1]}")
    print()
    print(f"5-fold CV best layer: {cv_results['best_layer_absolute']}")
    print(f"5-fold CV AUROC:      {cv_results['best_mean_auroc']:.4f} ± {cv_results['best_std_auroc']:.4f}")
    print(f"Style-controlled:     {cv_results['mean_style_controlled_auroc']:.4f}")
    print()

    print("Per-layer mean AUROC (CV):")
    sorted_layers = sorted(cv_results["mean_auroc_per_layer"].items(), key=lambda x: x[1], reverse=True)
    for layer_str, auroc in sorted_layers[:5]:
        std = cv_results["std_auroc_per_layer"][layer_str]
        print(f"  Layer {layer_str:>2s}: {auroc:.4f} ± {std:.4f}")
    print()

    print("AUROC by domain (full data, best layer):")
    for domain, auroc in sorted(breakdown_domain.items()):
        print(f"  {domain:15s}: {auroc:.4f}")
    print()

    print("AUROC by evidence_strength (full data, best layer):")
    for es, auroc in sorted(breakdown_evidence.items()):
        print(f"  {es:15s}: {auroc:.4f}")
    print("=" * 60)


if __name__ == "__main__":
    main()
