"""Formal Bound Verification (plan_005).

Validates Claim 1 (stability criterion): top-k selection is stable under
epsilon-bounded perturbation when Delta_k > 2*L*epsilon.

Measures:
  1. Lipschitz constant L (spectral norm product + empirical)
  2. Empirical top-k stability across epsilon levels (perturbation on visual tokens)
  3. Theoretical vs empirical stability rate comparison
  4. Margin distribution statistics

Usage:
    python eval_formal_bound.py \
        --checkpoint checkpoints/imm_two_stage/final/checkpoint.pt \
        --config configs/imm_anchor.yaml \
        --gpu 0 --max_batches 500 --seed 42
"""

from __future__ import annotations

import argparse
import json
import logging
import sys
from pathlib import Path

import numpy as np
import torch

ARTIFACTS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(ARTIFACTS_DIR))

from imm.metrics import compute_empirical_lipschitz, compute_margin

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger(__name__)


def parse_args():
    parser = argparse.ArgumentParser(description="Formal bound verification (plan_005)")
    parser.add_argument("--checkpoint", type=str, required=True)
    parser.add_argument("--config", type=str, required=True)
    parser.add_argument("--gpu", type=int, default=0)
    parser.add_argument("--max_batches", type=int, default=500)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--output", type=str, default="results/formal_bound_plan005.json")
    return parser.parse_args()


@torch.no_grad()
def extract_vis_tokens_and_query(model, batch):
    """Extract visual tokens and action query for direct ACIS input.

    Returns vis_tokens (B, N, D), suffix_embs (B, Q, D_action), k (int).
    """
    bm = model.base_model
    images, _ = model.policy.prepare_images(batch)
    vis_tokens, _ = model._get_visual_tokens(images)

    actions = model.policy.prepare_action(batch)
    noise = bm.sample_noise(actions.shape, actions.device)
    time = bm.sample_time(actions.shape[0], actions.device)
    time_expanded = time[:, None, None]
    x_t = time_expanded * noise + (1 - time_expanded) * actions
    suffix_embs, _, _ = bm.embed_suffix(x_t, time)

    N_vis = vis_tokens.shape[1]
    k = max(1, int(N_vis * model.k_ratio))
    return vis_tokens, suffix_embs, k


@torch.no_grad()
def measure_topk_stability(acis, vis_tokens, suffix_embs, k, epsilon):
    """Measure exact top-k set stability under epsilon perturbation of visual tokens.

    Perturbation model: Gaussian noise with per-element std = epsilon.

    Returns:
        stable: (B,) bool — True if top-k set identical after perturbation
        margins: (B,) Delta_k values from clean scores
        jaccard: (B,) Jaccard similarity of top-k sets
    """
    scores_clean = acis(suffix_embs, vis_tokens)
    _, idx_clean = torch.topk(scores_clean, k, dim=-1)

    delta = epsilon * torch.randn_like(vis_tokens)
    scores_perturbed = acis(suffix_embs, vis_tokens + delta)
    _, idx_perturbed = torch.topk(scores_perturbed, k, dim=-1)

    B, N = scores_clean.shape
    mask_clean = torch.zeros(B, N, device=scores_clean.device)
    mask_pert = torch.zeros(B, N, device=scores_clean.device)
    mask_clean.scatter_(1, idx_clean, 1.0)
    mask_pert.scatter_(1, idx_perturbed, 1.0)

    stable = (mask_clean == mask_pert).all(dim=-1)

    intersection = (mask_clean * mask_pert).sum(-1)
    union = (mask_clean + mask_pert).clamp(max=1.0).sum(-1)
    jaccard = intersection / union.clamp(min=1.0)

    margins = compute_margin(scores_clean, k)
    return stable, margins, jaccard


def main():
    args = parse_args()

    import random

    random.seed(args.seed)
    np.random.seed(args.seed)
    torch.manual_seed(args.seed)

    device = torch.device(f"cuda:{args.gpu}" if torch.cuda.is_available() else "cpu")

    from evaluate import load_config, load_model_and_checkpoint
    from train import (
        get_tokenizer_from_policy,
        load_dataset,
        make_dataloader,
        preprocess_batch,
    )

    config = load_config(args.config)
    model, imm_enabled = load_model_and_checkpoint(config, args.checkpoint, device)

    if not imm_enabled or not hasattr(model, "acis"):
        log.error("Checkpoint must be an IMM model with ACIS module")
        sys.exit(1)

    model.eval()
    tokenizer = get_tokenizer_from_policy(model)

    dataset = load_dataset(config)
    dataloader = make_dataloader(dataset, {
        **config,
        "training": {
            **config.get("training", {}),
            "batch_size": config.get("training", {}).get("eval_batch_size", 4),
        },
    })

    # === Lipschitz estimation ===
    log.info("Estimating Lipschitz constant (spectral norm)...")
    L_spectral = model.acis.get_lipschitz_estimate()
    log.info("  L_spectral = %.6f", L_spectral)

    log.info("Estimating Lipschitz constant (empirical, 10 batches x 100 samples)...")
    L_empirical = 0.0
    lip_batches = 0
    for batch in dataloader:
        if lip_batches >= 10:
            break
        batch = {k: v.to(device) if isinstance(v, torch.Tensor) else v for k, v in batch.items()}
        batch = preprocess_batch(batch, tokenizer, device=device)
        vis_tokens, suffix_embs, _ = extract_vis_tokens_and_query(model, batch)
        L = compute_empirical_lipschitz(
            model.acis, vis_tokens, suffix_embs, num_samples=100, epsilon=0.001
        )
        L_empirical = max(L_empirical, L)
        lip_batches += 1
    log.info("  L_empirical = %.6f", L_empirical)

    # === Pre-load evaluation batches ===
    log.info("Pre-loading %d batches...", args.max_batches)
    batches = []
    for batch_idx, batch in enumerate(dataloader):
        if batch_idx >= args.max_batches:
            break
        batch = {k: v.to(device) if isinstance(v, torch.Tensor) else v for k, v in batch.items()}
        batch = preprocess_batch(batch, tokenizer, device=device)
        batches.append(batch)
    log.info("Loaded %d batches", len(batches))

    # === Stability measurement ===
    epsilons = [0.005, 0.01, 0.02, 0.05, 0.1]
    k_value = None
    all_clean_margins = []
    results_per_eps = {}

    for eps in epsilons:
        log.info("Evaluating eps = %.3f ...", eps)
        torch.manual_seed(args.seed + int(eps * 10000))

        stable_count = 0
        total_count = 0
        eps_margins = []
        eps_jaccards = []

        for batch in batches:
            vis_tokens, suffix_embs, k = extract_vis_tokens_and_query(model, batch)
            if k_value is None:
                k_value = k

            stable, margins, jaccard = measure_topk_stability(
                model.acis, vis_tokens, suffix_embs, k, eps
            )

            stable_count += stable.sum().item()
            total_count += stable.shape[0]
            eps_margins.append(margins.cpu())
            eps_jaccards.append(jaccard.cpu())

        margins_cat = torch.cat(eps_margins)
        jaccards_cat = torch.cat(eps_jaccards)
        empirical_stability = stable_count / total_count
        mean_jaccard = jaccards_cat.mean().item()

        # Theoretical bound: stability >= P(Delta_k > 2*L*eps)
        # Use empirical L for tighter bound
        threshold = 2 * L_empirical * eps
        theoretical_stable = (margins_cat > threshold).float().mean().item()

        # Also compute with spectral L
        threshold_spectral = 2 * L_spectral * eps
        theoretical_stable_spectral = (margins_cat > threshold_spectral).float().mean().item()

        results_per_eps[eps] = {
            "empirical_stability": empirical_stability,
            "mean_jaccard": mean_jaccard,
            "theoretical_bound_empirical_L": theoretical_stable,
            "theoretical_bound_spectral_L": theoretical_stable_spectral,
            "margin_over_bound": empirical_stability - theoretical_stable,
            "threshold_2Le_empirical": threshold,
            "threshold_2Le_spectral": threshold_spectral,
            "n_samples": total_count,
        }

        if eps == epsilons[0]:
            all_clean_margins = margins_cat

        log.info(
            "  eps=%.3f: stability=%.4f, jaccard=%.4f, "
            "theo(emp_L)>=%.4f, theo(spec_L)>=%.4f",
            eps, empirical_stability, mean_jaccard,
            theoretical_stable, theoretical_stable_spectral,
        )

    # === Margin distribution (from smallest epsilon run for cleanest margins) ===
    m_np = all_clean_margins.numpy()
    margin_dist = {
        "mean": float(m_np.mean()),
        "median": float(np.median(m_np)),
        "std": float(m_np.std()),
        "min": float(m_np.min()),
        "max": float(m_np.max()),
        "p5": float(np.percentile(m_np, 5)),
        "p25": float(np.percentile(m_np, 25)),
        "p75": float(np.percentile(m_np, 75)),
        "p95": float(np.percentile(m_np, 95)),
    }

    # === Print summary ===
    print()
    print("=" * 70)
    print("=== Formal Bound Verification (plan_005) ===")
    print("=" * 70)
    print(f"Lipschitz constant L = {L_empirical:.6f} (empirical)")
    print(f"Lipschitz constant L = {L_spectral:.6f} (spectral norm product)")
    print(f"k_ratio = {model.k_ratio}, k = {k_value} tokens")
    print(f"Total samples per eps = {results_per_eps[epsilons[0]]['n_samples']}")
    print()
    header = (
        f"| {'eps':>7} | {'Emp. Stability':>14} | {'Jaccard':>8} "
        f"| {'Theo(emp_L)':>11} | {'Theo(spec_L)':>12} | {'Margin':>8} |"
    )
    print(header)
    print(f"|{'-' * 9}|{'-' * 16}|{'-' * 10}|{'-' * 13}|{'-' * 14}|{'-' * 10}|")
    for eps in epsilons:
        r = results_per_eps[eps]
        print(
            f"| {eps:>7.3f} | {r['empirical_stability']:>14.4f} | {r['mean_jaccard']:>8.4f} "
            f"| {r['theoretical_bound_empirical_L']:>11.4f} | {r['theoretical_bound_spectral_L']:>12.4f} "
            f"| +{r['margin_over_bound']:>6.4f} |"
        )
    print()
    print("Margin Delta_k distribution:")
    print(
        f"  mean={margin_dist['mean']:.4f}, median={margin_dist['median']:.4f}, "
        f"std={margin_dist['std']:.4f}"
    )
    print(
        f"  [min={margin_dist['min']:.4f}, p5={margin_dist['p5']:.4f}, "
        f"p25={margin_dist['p25']:.4f}, p75={margin_dist['p75']:.4f}, "
        f"p95={margin_dist['p95']:.4f}, max={margin_dist['max']:.4f}]"
    )
    print()

    # Tightness ratio
    for eps in epsilons:
        r = results_per_eps[eps]
        if r["theoretical_bound_empirical_L"] > 0:
            tightness = r["empirical_stability"] / r["theoretical_bound_empirical_L"]
            print(f"  eps={eps:.3f}: tightness ratio = {tightness:.2f}x "
                  f"(empirical/theoretical)")

    # === Save JSON ===
    output_data = {
        "lipschitz_L_empirical": L_empirical,
        "lipschitz_L_spectral": L_spectral,
        "k": k_value,
        "k_ratio": model.k_ratio,
        "epsilon_values": epsilons,
        "empirical_stability": [results_per_eps[e]["empirical_stability"] for e in epsilons],
        "mean_jaccard": [results_per_eps[e]["mean_jaccard"] for e in epsilons],
        "theoretical_bound_empirical_L": [
            results_per_eps[e]["theoretical_bound_empirical_L"] for e in epsilons
        ],
        "theoretical_bound_spectral_L": [
            results_per_eps[e]["theoretical_bound_spectral_L"] for e in epsilons
        ],
        "margin_distribution": margin_dist,
        "per_epsilon": {str(e): results_per_eps[e] for e in epsilons},
        "_meta": {
            "checkpoint": args.checkpoint,
            "config": args.config,
            "max_batches": args.max_batches,
            "seed": args.seed,
            "n_batches_loaded": len(batches),
        },
    }

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(output_data, f, indent=2, default=str)
    log.info("Results saved to %s", output_path)


if __name__ == "__main__":
    main()
