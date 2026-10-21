"""
RASP Scoring: combine importance I(h) and functional overlap F(h).

S(h) = I(h) * (1 - F(h))^alpha

Structures with lower S(h) are pruned first.
Standard baseline uses only I(h) for ranking.
"""

import argparse
import logging
import os

import torch

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger(__name__)


def compute_rasp_scores(importance: dict, overlap: dict, alpha: float = 1.0) -> dict:
    """Compute S(h) = I(h) * (1 - F(h))^alpha for each structure.

    Args:
        importance: dict[layer_idx -> tensor of I(h)]
        overlap: dict[layer_idx -> tensor of F(h)]
        alpha: recoverability penalty exponent

    Returns:
        dict[layer_idx -> tensor of S(h)]
    """
    scores = {}
    for layer_idx in importance:
        ih = importance[layer_idx].float()
        fh = overlap[layer_idx].float()
        sh = ih * (1.0 - fh).pow(alpha)
        scores[layer_idx] = sh
    return scores


def rank_structures(scores: dict) -> list:
    """Flatten and rank all structures globally by score (ascending = prune first).

    Returns list of (score, layer_idx, struct_idx) sorted ascending.
    """
    entries = []
    for layer_idx, layer_scores in scores.items():
        for struct_idx in range(layer_scores.shape[0]):
            entries.append((layer_scores[struct_idx].item(), layer_idx, struct_idx))
    entries.sort(key=lambda x: x[0])
    return entries


def main():
    parser = argparse.ArgumentParser(description="Compute RASP pruning scores")
    parser.add_argument("--importance_path", type=str, required=True, help="Path to importance scores .pt")
    parser.add_argument("--cka_path", type=str, default=None, help="Path to CKA overlap scores .pt (None for standard mode)")
    parser.add_argument("--mode", type=str, choices=["standard", "rasp"], default="rasp")
    parser.add_argument("--alpha", type=float, default=1.0, help="Recoverability penalty exponent")
    parser.add_argument("--output_path", type=str, required=True, help="Output .pt file for pruning scores")
    args = parser.parse_args()

    importance_data = torch.load(args.importance_path, map_location="cpu", weights_only=True)
    attn_importance = importance_data["attn_importance"]
    mlp_importance = importance_data["mlp_importance"]

    if args.mode == "rasp":
        if args.cka_path is None:
            raise ValueError("--cka_path required for rasp mode")
        cka_data = torch.load(args.cka_path, map_location="cpu", weights_only=True)
        attn_overlap = cka_data["attn_overlap"]
        mlp_overlap = cka_data["mlp_overlap"]

        attn_scores = compute_rasp_scores(attn_importance, attn_overlap, args.alpha)
        mlp_scores = compute_rasp_scores(mlp_importance, mlp_overlap, args.alpha)
        logger.info(f"Computed RASP scores with alpha={args.alpha}")
    else:
        # Standard: score = importance only
        attn_scores = {k: v.float() for k, v in attn_importance.items()}
        mlp_scores = {k: v.float() for k, v in mlp_importance.items()}
        logger.info("Computed standard importance-only scores")

    attn_ranking = rank_structures(attn_scores)
    mlp_ranking = rank_structures(mlp_scores)

    logger.info(f"Attention heads total: {len(attn_ranking)}, lowest 5 scores: "
                f"{[f'L{e[1]}H{e[2]}={e[0]:.6f}' for e in attn_ranking[:5]]}")
    logger.info(f"MLP groups total: {len(mlp_ranking)}, lowest 5 scores: "
                f"{[f'L{e[1]}G{e[2]}={e[0]:.6f}' for e in mlp_ranking[:5]]}")

    os.makedirs(os.path.dirname(args.output_path) or ".", exist_ok=True)
    result = {
        "attn_scores": attn_scores,
        "mlp_scores": mlp_scores,
        "attn_ranking": attn_ranking,
        "mlp_ranking": mlp_ranking,
        "mode": args.mode,
        "alpha": args.alpha,
    }
    torch.save(result, args.output_path)
    logger.info(f"Saved pruning scores to {args.output_path}")


if __name__ == "__main__":
    main()
