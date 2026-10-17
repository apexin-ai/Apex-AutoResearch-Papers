"""Confusability matrix computation and adaptive thresholding.

Input: Type embeddings (.pt dict {name: tensor}) or precomputed sim_matrix (.pt)
Output: Cosine similarity matrix, adaptive threshold value
Dependencies: torch

"""
import logging
from typing import List, Optional, Tuple

import torch
import torch.nn.functional as F

logger = logging.getLogger(__name__)


def load_type_embeddings(path: str) -> Tuple[torch.Tensor, List[str]]:
    """Load type embeddings from .pt file.

    Returns:
        (embeddings [N, D], type_names sorted alphabetically)
    """
    data = torch.load(path, map_location="cpu", weights_only=True)
    if isinstance(data, dict) and ("sim_matrix" in data or "similarity_matrix" in data):
        raise ValueError(f"{path} is a sim_matrix file, not embeddings. Use load_sim_matrix().")
    type_names = sorted(data.keys())
    embeddings = torch.stack([data[name] for name in type_names]).float()
    logger.info("Loaded embeddings: %d types, dim=%d", len(type_names), embeddings.shape[1])
    return embeddings, type_names


def load_sim_matrix(path: str) -> Tuple[torch.Tensor, List[str]]:
    """Load precomputed similarity matrix from .pt file.

    Returns:
        (sim_matrix [N, N], type_names)
    """
    data = torch.load(path, map_location="cpu", weights_only=True)
    if isinstance(data, dict):
        if "sim_matrix" in data:
            matrix = data["sim_matrix"]
        elif "similarity_matrix" in data:
            matrix = data["similarity_matrix"]
        else:
            raise ValueError(f"Unknown keys in matrix file: {list(data.keys())}")
        type_names = data.get("type_names", [f"type_{i}" for i in range(matrix.shape[0])])
        return matrix, type_names
    elif isinstance(data, torch.Tensor):
        return data, [f"type_{i}" for i in range(data.shape[0])]
    raise ValueError(f"{path} does not contain a sim_matrix dict.")


def cosine_similarity_matrix(embeddings: torch.Tensor) -> torch.Tensor:
    """Compute pairwise cosine similarity matrix.

    Args:
        embeddings: [N, D] tensor

    Returns:
        [N, N] symmetric cosine similarity matrix
    """
    normed = F.normalize(embeddings, dim=1)
    sim = normed @ normed.T
    return sim


def normalize_confusion_matrix(C: torch.Tensor) -> torch.Tensor:
    """Symmetrize and normalize an empirical confusion matrix to [0, 1]."""
    sym = (C + C.T) / 2.0
    diag_mask = ~torch.eye(sym.shape[0], dtype=torch.bool)
    off_diag = sym[diag_mask]
    if off_diag.max() == off_diag.min():
        return torch.zeros_like(sym)
    normalized = (sym - off_diag.min()) / (off_diag.max() - off_diag.min())
    normalized.fill_diagonal_(1.0)
    return normalized


def adaptive_threshold(sim_matrix: torch.Tensor, k: float = 1.0) -> float:
    """Compute adaptive threshold: mean + k * std of upper triangle values.

    Args:
        sim_matrix: [N, N] similarity matrix
        k: number of standard deviations above the mean (default 1.0)

    Returns:
        Threshold value tau
    """
    mask = torch.triu(torch.ones_like(sim_matrix, dtype=torch.bool), diagonal=1)
    upper_vals = sim_matrix[mask]
    tau = upper_vals.mean().item() + k * upper_vals.std().item()
    logger.info("Adaptive threshold: mean=%.4f, std=%.4f, k=%.1f -> tau=%.4f",
                upper_vals.mean().item(), upper_vals.std().item(), k, tau)
    return tau
