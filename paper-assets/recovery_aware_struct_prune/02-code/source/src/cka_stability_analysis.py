"""
CKA Scoring Stability Analysis.

Validates that CKA-based pruning scores (F(g) overlap) are robust to calibration
set size. Computes F(g) for all prunable structures using 256/512/1024 calibration
samples from GSM8K train, then measures pairwise Spearman rank correlation.
rho > 0.95 indicates stable scoring.

Input:  --model_path  Dense base model (DeepSeek-R1-Distill-Qwen-7B)
        --device      GPU device (e.g. cuda:0)
Output: --output_path JSON with Spearman correlations, top/bottom-10 structures
Deps:   cka_overlap.py (load_calibration_data, set_seed, collect_head_activations,
                        collect_mlp_activations, compute_overlap)
"""

import argparse
import json
import logging
import os
import sys

import numpy as np
import scipy.stats as stats
import torch

src_dir = os.path.dirname(os.path.abspath(__file__))
if src_dir not in sys.path:
    sys.path.insert(0, src_dir)

from cka_overlap import (
    collect_head_activations,
    collect_mlp_activations,
    compute_overlap,
    load_calibration_data,
    set_seed,
)
from transformers import AutoModelForCausalLM, AutoTokenizer

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

CALIB_SIZES = [256, 512, 1024]


def subsample_activations(activations_dict, n_samples):
    """Subsample first n_samples from activation tensors."""
    return {layer: acts[:n_samples] for layer, acts in activations_dict.items()}


def fh_to_flat_vector(overlap_dict):
    """Flatten per-layer F(g) into a single vector, ordered by (layer_idx, struct_idx)."""
    vals = []
    labels = []
    for layer_idx in sorted(overlap_dict.keys()):
        for i, s in enumerate(overlap_dict[layer_idx].tolist()):
            vals.append(s)
            labels.append((layer_idx, i))
    return np.array(vals), labels


def get_top_bottom(vals, labels, structure_type, k=10):
    """Return top-k highest and bottom-k lowest F(g) structures."""
    indices = np.argsort(vals)
    bottom = []
    for idx in indices[:k]:
        layer, struct = labels[idx]
        bottom.append({"name": f"layer{layer}_{structure_type}{struct}",
                        "score": round(float(vals[idx]), 6)})
    top = []
    for idx in indices[-k:][::-1]:
        layer, struct = labels[idx]
        top.append({"name": f"layer{layer}_{structure_type}{struct}",
                     "score": round(float(vals[idx]), 6)})
    return top, bottom


def main():
    parser = argparse.ArgumentParser(
        description="CKA scoring stability across calibration sizes")
    parser.add_argument("--model_path", type=str, required=True)
    parser.add_argument("--output_path", type=str, required=True)
    parser.add_argument("--device", type=str, default="cuda:0")
    parser.add_argument("--mlp_groups", type=int, default=28)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--dtype", type=str, default="bfloat16",
                        choices=["float16", "bfloat16", "float32"])
    args = parser.parse_args()

    set_seed(args.seed)
    device = torch.device(args.device)
    torch_dtype = {"float16": torch.float16, "bfloat16": torch.bfloat16,
                   "float32": torch.float32}[args.dtype]

    logger.info(f"Loading model from {args.model_path}")
    tokenizer = AutoTokenizer.from_pretrained(args.model_path, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(
        args.model_path, torch_dtype=torch_dtype, device_map=device, trust_remote_code=True,
    )

    max_size = max(CALIB_SIZES)
    logger.info(f"Loading {max_size} calibration samples from GSM8K train")
    calibration_data = load_calibration_data(tokenizer, max_size, seed=args.seed)
    logger.info(f"Loaded {len(calibration_data)} samples")

    logger.info("Collecting GQA group activations...")
    attn_acts = collect_head_activations(model, tokenizer, calibration_data, device)

    logger.info("Collecting MLP group activations...")
    mlp_acts = collect_mlp_activations(model, tokenizer, calibration_data, device, args.mlp_groups)

    del model
    torch.cuda.empty_cache()
    logger.info("Model freed")

    # Compute F(g) for each calibration size by subsampling activations.
    # load_calibration_data shuffles with fixed seed then takes first N,
    # so first-256 subset matches what n_samples=256 would produce.
    attn_overlap_by_size = {}
    mlp_overlap_by_size = {}
    for size in CALIB_SIZES:
        logger.info(f"Computing F(g) with N={size} ...")
        sub_attn = subsample_activations(attn_acts, size)
        sub_mlp = subsample_activations(mlp_acts, size)
        attn_overlap_by_size[size], _ = compute_overlap(sub_attn, "gqa_groups")
        mlp_overlap_by_size[size], _ = compute_overlap(sub_mlp, "mlp_groups")
        logger.info(f"  N={size} done")

    del attn_acts, mlp_acts
    torch.cuda.empty_cache()

    # Flatten scores per size, compute top/bottom structures
    results = {"calibration_sizes": CALIB_SIZES, "correlations": {}, "per_size": {}}
    attn_flat = {}
    mlp_flat = {}

    for size in CALIB_SIZES:
        attn_vals, attn_labels = fh_to_flat_vector(attn_overlap_by_size[size])
        mlp_vals, mlp_labels = fh_to_flat_vector(mlp_overlap_by_size[size])
        attn_flat[size] = (attn_vals, attn_labels)
        mlp_flat[size] = (mlp_vals, mlp_labels)

        attn_top, attn_bot = get_top_bottom(attn_vals, attn_labels, "gqa_group")
        mlp_top, mlp_bot = get_top_bottom(mlp_vals, mlp_labels, "mlp_group")
        results["per_size"][str(size)] = {
            "n_attn_structures": len(attn_vals),
            "n_mlp_structures": len(mlp_vals),
            "attn": {"top10": attn_top, "bottom10": attn_bot},
            "mlp": {"top10": mlp_top, "bottom10": mlp_bot},
        }

    # Pairwise Spearman rank correlations
    pairs = [(256, 512), (256, 1024), (512, 1024)]
    for sa, sb in pairs:
        pair_key = f"{sa}_vs_{sb}"
        rho_attn, p_attn = stats.spearmanr(attn_flat[sa][0], attn_flat[sb][0])
        rho_mlp, p_mlp = stats.spearmanr(mlp_flat[sa][0], mlp_flat[sb][0])

        combined_a = np.concatenate([attn_flat[sa][0], mlp_flat[sa][0]])
        combined_b = np.concatenate([attn_flat[sb][0], mlp_flat[sb][0]])
        rho_all, p_all = stats.spearmanr(combined_a, combined_b)

        results["correlations"][pair_key] = {
            "attn": {"rho": round(float(rho_attn), 6), "p_value": float(p_attn)},
            "mlp": {"rho": round(float(rho_mlp), 6), "p_value": float(p_mlp)},
            "combined": {"rho": round(float(rho_all), 6), "p_value": float(p_all)},
        }
        logger.info(f"{pair_key}: attn rho={rho_attn:.4f}, mlp rho={rho_mlp:.4f}, "
                     f"combined rho={rho_all:.4f}")

    all_combined_rhos = [results["correlations"][f"{a}_vs_{b}"]["combined"]["rho"]
                         for a, b in pairs]
    results["summary"] = {
        "min_combined_rho": float(min(all_combined_rhos)),
        "mean_combined_rho": float(np.mean(all_combined_rhos)),
        "stable": all(r > 0.95 for r in all_combined_rhos),
        "threshold": 0.95,
    }

    os.makedirs(os.path.dirname(args.output_path) or ".", exist_ok=True)
    with open(args.output_path, "w") as f:
        json.dump(results, f, indent=2)
    logger.info(f"Saved to {args.output_path}")

    # Print summary
    print(f"\n{'=' * 60}")
    print("CKA Scoring Stability Analysis")
    print(f"{'=' * 60}")
    for pair_key, corr in results["correlations"].items():
        print(f"\n{pair_key}:")
        print(f"  Attention heads:  rho={corr['attn']['rho']:.4f}  "
              f"(p={corr['attn']['p_value']:.2e})")
        print(f"  MLP groups:       rho={corr['mlp']['rho']:.4f}  "
              f"(p={corr['mlp']['p_value']:.2e})")
        print(f"  Combined:         rho={corr['combined']['rho']:.4f}  "
              f"(p={corr['combined']['p_value']:.2e})")

    status = "PASS" if results["summary"]["stable"] else "FAIL"
    print(f"\nOverall: {status} (threshold rho>0.95, "
          f"min rho={results['summary']['min_combined_rho']:.4f})")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
