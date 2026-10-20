"""Spectral metric comparison across checkpoints for collapse detection.

Computes 4 spectral indicators (effective rank, condition number, trace norm,
spectral gap) + perplexity on each checkpoint found under an output directory,
then ranks which metric first detects collapse (leading indicator analysis).

Input:  --output-dir with G0/G1/G2 subdirectories containing training checkpoints
Output: stdout table + spectral_comparison.json in output-dir

Dependencies: torch, transformers, datasets, tqdm
"""

import argparse
import glob
import json
import logging
import math
import os
import re
import sys
from dataclasses import dataclass
from itertools import chain
from typing import Dict, List, Optional, Tuple

import torch
import torch.nn.functional as F
from torch.utils.data import DataLoader, Dataset as TorchDataset
from tqdm import tqdm
from transformers import AutoModelForCausalLM, AutoTokenizer

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Data
# ---------------------------------------------------------------------------

class PackedDataset(TorchDataset):
    def __init__(self, input_ids: List[List[int]]):
        self.input_ids = input_ids

    def __len__(self):
        return len(self.input_ids)

    def __getitem__(self, idx):
        ids = torch.tensor(self.input_ids[idx], dtype=torch.long)
        return {"input_ids": ids, "attention_mask": torch.ones_like(ids), "labels": ids.clone()}


def make_dataloader(dataset: PackedDataset, batch_size: int, shuffle: bool = False) -> DataLoader:
    return DataLoader(dataset, batch_size=batch_size, shuffle=shuffle, num_workers=2, pin_memory=True)


def prepare_holdout(tokenizer, max_seq_length: int = 2048) -> PackedDataset:
    from datasets import load_dataset

    raw = load_dataset("wikitext", "wikitext-103-raw-v1", split="test")
    tokenized = raw.map(
        lambda ex: tokenizer(ex["text"], truncation=False, add_special_tokens=False),
        batched=True,
        remove_columns=raw.column_names,
        num_proc=4,
        desc="Tokenizing holdout",
    )
    flat = list(chain(*tokenized["input_ids"]))
    n = (len(flat) // max_seq_length) * max_seq_length
    sequences = [flat[i : i + max_seq_length] for i in range(0, n, max_seq_length)]
    logger.info("Holdout: %d sequences (%d tokens)", len(sequences), n)
    return PackedDataset(sequences)


# ---------------------------------------------------------------------------
# Core spectral functions
# ---------------------------------------------------------------------------

def collect_hidden_states(
    model: torch.nn.Module,
    dataloader: DataLoader,
    num_samples: int,
    device: str = "cuda",
) -> torch.Tensor:
    """Collect mean-pooled final-layer hidden states E (N, D).

    Same logic as metrics.py compute_spectral_effective_rank but returns
    the raw matrix instead of computed metrics.
    """
    model.eval()
    hidden_list = []
    collected = 0

    with torch.no_grad():
        for batch in tqdm(dataloader, desc="collecting hidden states", leave=False):
            if collected >= num_samples:
                break
            input_ids = batch["input_ids"].to(device)
            attn_mask = batch["attention_mask"].to(device)

            out = model(input_ids=input_ids, attention_mask=attn_mask, output_hidden_states=True)
            h = out.hidden_states[-1].float()  # (B, L, D)

            mask = attn_mask.unsqueeze(-1).float()
            pooled = (h * mask).sum(1) / mask.sum(1).clamp(min=1)  # (B, D)
            hidden_list.append(pooled.cpu())
            collected += pooled.shape[0]

    return torch.cat(hidden_list, dim=0)[:num_samples]


def compute_all_spectral_metrics(E: torch.Tensor) -> dict:
    """Compute 4 spectral indicators from hidden states matrix.

    Given E of shape (N, D), computes SVD and derives:
      - eff_rank: exp(H(p)) where p_i = sigma_i / sum(sigma), Shannon entropy-based
      - condition_number: sigma_max / sigma_min
      - trace_norm: sum(sigma), i.e. nuclear norm
      - spectral_gap: sigma_1 - sigma_2

    Returns dict with all metrics plus auxiliary values.
    """
    sigma = torch.linalg.svdvals(E)  # descending
    sigma_pos = sigma[sigma > 0]

    # Effective rank
    p = sigma_pos / sigma_pos.sum()
    entropy = -(p * p.log()).sum().item()
    eff_rank = math.exp(entropy)

    # Condition number
    condition_number = (sigma_pos[0] / sigma_pos[-1]).item()

    # Trace norm (nuclear norm)
    trace_norm = sigma_pos.sum().item()

    # Spectral gap
    spectral_gap = (sigma_pos[0] - sigma_pos[1]).item() if len(sigma_pos) >= 2 else 0.0

    return {
        "eff_rank": eff_rank,
        "condition_number": condition_number,
        "trace_norm": trace_norm,
        "spectral_gap": spectral_gap,
        "top_singular_value": sigma_pos[0].item(),
        "num_singular_values": int(len(sigma_pos)),
    }


def compute_perplexity(
    model: torch.nn.Module,
    dataloader: DataLoader,
    num_samples: int = 5000,
    device: str = "cuda",
) -> float:
    model.eval()
    total_loss = 0.0
    total_tokens = 0
    seen = 0

    with torch.no_grad():
        for batch in tqdm(dataloader, desc="perplexity", leave=False):
            if seen >= num_samples:
                break
            input_ids = batch["input_ids"].to(device)
            attn_mask = batch["attention_mask"].to(device)
            labels = input_ids.clone()
            labels[attn_mask == 0] = -100

            loss = model(input_ids=input_ids, attention_mask=attn_mask, labels=labels).loss
            n_tok = (labels[:, 1:] != -100).sum().item()
            total_loss += loss.item() * n_tok
            total_tokens += n_tok
            seen += input_ids.shape[0]

    avg_loss = total_loss / max(total_tokens, 1)
    return math.exp(avg_loss)


# ---------------------------------------------------------------------------
# Checkpoint evaluation
# ---------------------------------------------------------------------------

def evaluate_checkpoint(
    checkpoint_path: str,
    holdout_data: PackedDataset,
    num_samples: int = 50_000,
    spectral_batch_size: int = 64,
    ppl_batch_size: int = 16,
    device: str = "cuda",
) -> dict:
    """Load a checkpoint, compute all spectral metrics + PPL."""
    logger.info("Evaluating %s", checkpoint_path)

    model = AutoModelForCausalLM.from_pretrained(
        checkpoint_path, torch_dtype=torch.bfloat16
    ).to(device)
    model.eval()

    spectral_loader = make_dataloader(holdout_data, batch_size=spectral_batch_size)
    E = collect_hidden_states(model, spectral_loader, num_samples=num_samples, device=device)
    metrics = compute_all_spectral_metrics(E)

    ppl_loader = make_dataloader(holdout_data, batch_size=ppl_batch_size)
    metrics["ppl"] = compute_perplexity(model, ppl_loader, num_samples=5000, device=device)

    del model
    torch.cuda.empty_cache()

    return metrics


# ---------------------------------------------------------------------------
# Leading indicator analysis
# ---------------------------------------------------------------------------

def compute_leading_indicator_ranking(
    results: List[dict],
    baseline: dict,
    g0_results: Optional[List[dict]] = None,
) -> dict:
    """Rank which spectral metric first detects collapse.

    For each metric, estimates sigma from G0 checkpoint variance and finds the
    earliest post-G0 checkpoint where the metric deviates by more than 2 sigma
    from the baseline (G0-final) value.

    Args:
        results: post-G0 checkpoint dicts, ordered chronologically.
        baseline: G0-final checkpoint dict (reference point).
        g0_results: all G0 checkpoint dicts, used to compute empirical sigma.

    Returns:
        dict with 'ranking' (sorted list) and 'details' per metric.
    """
    import numpy as np

    metric_keys = ["eff_rank", "condition_number", "trace_norm", "spectral_gap"]
    baseline_vals = {k: baseline[k] for k in metric_keys}

    details = {}
    for key in metric_keys:
        bv = baseline_vals[key]
        # Empirical sigma from G0 checkpoints; fallback to 1% of baseline if < 2 points
        if g0_results and len(g0_results) >= 2:
            g0_values = [r[key] for r in g0_results]
            sigma_est = float(np.std(g0_values, ddof=1))
            if sigma_est < 1e-8:
                sigma_est = max(abs(bv) * 0.01, 1e-8)
        else:
            sigma_est = max(abs(bv) * 0.01, 1e-8)

        first_idx = None
        first_delta = None
        first_sigma_multiple = None

        for i, r in enumerate(results):
            delta = r[key] - bv
            n_sigma = abs(delta) / sigma_est
            if n_sigma >= 2.0:
                first_idx = i
                first_delta = delta
                first_sigma_multiple = n_sigma
                break

        details[key] = {
            "baseline_value": bv,
            "sigma_estimate": sigma_est,
            "first_deviation_idx": first_idx,
            "first_deviation_delta": first_delta,
            "first_deviation_sigma": first_sigma_multiple,
        }

    # Sort: earliest deviation first; ties broken by larger sigma multiple
    ranking = sorted(
        details.items(),
        key=lambda kv: (
            kv[1]["first_deviation_idx"] if kv[1]["first_deviation_idx"] is not None else len(results) + 1,
            -(kv[1]["first_deviation_sigma"] or 0),
        ),
    )

    return {
        "ranking": [
            {"metric": k, **v, "rank": i + 1}
            for i, (k, v) in enumerate(ranking)
        ],
        "details": details,
    }


# ---------------------------------------------------------------------------
# Checkpoint discovery
# ---------------------------------------------------------------------------

def discover_checkpoints(output_dir: str) -> List[Tuple[str, str]]:
    """Scan output_dir for G*/training/checkpoint-* and G*/final_model/.

    Returns list of (label, path) sorted by generation then step.
    """
    entries = []

    for gen_dir in sorted(glob.glob(os.path.join(output_dir, "G*"))):
        gen_name = os.path.basename(gen_dir)

        # training checkpoints
        ckpt_pattern = os.path.join(gen_dir, "training", "checkpoint-*")
        ckpts = sorted(glob.glob(ckpt_pattern), key=lambda p: int(re.search(r"checkpoint-(\d+)", p).group(1)))
        for i, cp in enumerate(ckpts, 1):
            step = re.search(r"checkpoint-(\d+)", cp).group(1)
            entries.append((f"{gen_name}-ckpt{i}(s{step})", cp))

        # final model
        final = os.path.join(gen_dir, "final_model")
        if os.path.isdir(final):
            entries.append((f"{gen_name}-final", final))

    return entries


# ---------------------------------------------------------------------------
# Display
# ---------------------------------------------------------------------------

def print_table(labels: List[str], results: List[dict]):
    metric_rows = [
        ("eff_rank", "eff_rank"),
        ("cond_num", "condition_number"),
        ("trace_nm", "trace_norm"),
        ("spec_gap", "spectral_gap"),
        ("ppl", "ppl"),
    ]

    col_width = max(10, max(len(l) for l in labels) + 2)
    header = "         | " + " | ".join(l.center(col_width) for l in labels)
    sep = "=" * len(header)

    print("\nMetric Comparison Across Checkpoints")
    print(sep)
    print(header)
    print(sep)

    for display_name, key in metric_rows:
        vals = []
        for r in results:
            v = r.get(key)
            if v is None:
                vals.append("N/A".center(col_width))
            elif abs(v) >= 1000:
                vals.append(f"{v:.1f}".center(col_width))
            elif abs(v) >= 10:
                vals.append(f"{v:.1f}".center(col_width))
            else:
                vals.append(f"{v:.3f}".center(col_width))
        print(f"{display_name:>8s} | " + " | ".join(vals))

    print(sep)


def print_ranking(ranking_info: dict, labels: List[str]):
    print("\nLeading Indicator Ranking:")
    for entry in ranking_info["ranking"]:
        idx = entry["first_deviation_idx"]
        if idx is not None:
            delta = entry["first_deviation_delta"]
            sigma = entry["first_deviation_sigma"]
            sign = "+" if delta > 0 else ""
            label = labels[idx] if idx < len(labels) else f"idx={idx}"
            print(f"  {entry['rank']}. {entry['metric']:<18s} — first deviation at {label} "
                  f"(Δ={sign}{delta:.2f}, {sigma:.1f}σ)")
        else:
            print(f"  {entry['rank']}. {entry['metric']:<18s} — no significant deviation detected")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Spectral metric comparison for collapse detection")
    parser.add_argument("--output-dir", required=True, help="Root output dir with G0/G1/G2 subdirs")
    parser.add_argument("--model-name", default="EleutherAI/pythia-1b", help="Base model name for tokenizer")
    parser.add_argument("--num-samples", type=int, default=50_000, help="Hidden state samples for spectral metrics")
    parser.add_argument("--spectral-batch-size", type=int, default=64)
    parser.add_argument("--ppl-batch-size", type=int, default=16)
    parser.add_argument("--max-seq-length", type=int, default=2048)
    parser.add_argument("--device", default="cuda")
    parser.add_argument("--json-output", default=None, help="JSON output path (default: output-dir/spectral_comparison.json)")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

    checkpoints = discover_checkpoints(args.output_dir)
    if not checkpoints:
        print(f"No checkpoints found under {args.output_dir}/G*/", file=sys.stderr)
        sys.exit(1)

    labels = [label for label, _ in checkpoints]
    paths = [path for _, path in checkpoints]
    logger.info("Found %d checkpoints: %s", len(checkpoints), ", ".join(labels))

    # Prepare holdout data
    logger.info("Preparing holdout data from wikitext-103-raw-v1 test split...")
    tokenizer = AutoTokenizer.from_pretrained(args.model_name)
    holdout = prepare_holdout(tokenizer, max_seq_length=args.max_seq_length)

    # Evaluate each checkpoint
    all_results = []
    for label, path in checkpoints:
        logger.info("--- %s ---", label)
        metrics = evaluate_checkpoint(
            path, holdout,
            num_samples=args.num_samples,
            spectral_batch_size=args.spectral_batch_size,
            ppl_batch_size=args.ppl_batch_size,
            device=args.device,
        )
        metrics["label"] = label
        metrics["path"] = path
        all_results.append(metrics)
        logger.info("  eff_rank=%.1f  cond=%.1f  trace=%.1f  gap=%.2f  ppl=%.2f",
                     metrics["eff_rank"], metrics["condition_number"],
                     metrics["trace_norm"], metrics["spectral_gap"], metrics["ppl"])

    # Baseline = G0 final checkpoint; leading indicator analysis on G1/G2 only
    g0_results = [r for r in all_results if r["label"].startswith("G0")]
    post_g0_results = [r for r in all_results if not r["label"].startswith("G0")]
    baseline = g0_results[-1]  # G0 final

    ranking_info = compute_leading_indicator_ranking(post_g0_results, baseline, g0_results)

    # Display
    print_table(labels, all_results)
    post_g0_labels = [r["label"] for r in post_g0_results]
    print_ranking(ranking_info, post_g0_labels)

    # Save JSON
    json_path = args.json_output or os.path.join(args.output_dir, "spectral_comparison.json")
    report = {
        "checkpoints": [
            {**r, "path": str(r["path"])} for r in all_results
        ],
        "baseline_label": baseline["label"],
        "leading_indicator_ranking": ranking_info,
    }
    os.makedirs(os.path.dirname(json_path) or ".", exist_ok=True)
    with open(json_path, "w") as f:
        json.dump(report, f, indent=2)
    print(f"\nJSON report saved to {json_path}")


if __name__ == "__main__":
    main()
