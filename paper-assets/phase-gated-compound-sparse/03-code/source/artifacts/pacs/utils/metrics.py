# General-purpose metrics for PACS profiling: perplexity, accuracy, etc.

from typing import List, Optional

import torch
import torch.nn.functional as F


def compute_perplexity(
    logits: torch.Tensor,
    labels: torch.Tensor,
    token_indices: Optional[List[int]] = None,
) -> float:
    """Compute mean per-token perplexity, optionally restricted to specific positions.

    Args:
        logits: (seq_len, vocab_size) – unnormalized logits.
        labels: (seq_len,) – ground-truth token ids.  Positions with label == -100
                are ignored (standard HF convention).
        token_indices: If given, only these positions contribute to the result.
                       None means all valid positions.

    Returns:
        Scalar perplexity (exp of mean cross-entropy over selected positions).
    """
    # Shift: logits[t] predicts labels[t+1]
    shift_logits = logits[:-1]  # (S-1, V)
    shift_labels = labels[1:]   # (S-1,)

    # float32 for numerical stability with fp16 logits
    per_token_ce = F.cross_entropy(
        shift_logits.float(), shift_labels, reduction="none"
    )  # (S-1,)

    if token_indices is not None:
        # token_indices refer to *label* positions; after shift they map to index-1
        idx = torch.tensor(
            [i - 1 for i in token_indices if 0 < i < len(labels)],
            device=per_token_ce.device,
        )
        if idx.numel() == 0:
            return float("nan")
        per_token_ce = per_token_ce[idx]

    # Ignore positions where label == -100
    valid = shift_labels[: per_token_ce.size(0)] != -100 if token_indices is None else torch.ones_like(per_token_ce, dtype=torch.bool)
    if token_indices is None:
        per_token_ce = per_token_ce[valid]

    if per_token_ce.numel() == 0:
        return float("nan")

    return torch.exp(per_token_ce.mean()).item()


def ppl_from_cached_losses(
    ce_losses: torch.Tensor,
    token_indices: Optional[List[int]] = None,
    seq_len: int = 0,
) -> float:
    """Compute perplexity from pre-computed shifted CE losses.

    Args:
        ce_losses: (seq_len-1,) per-token cross-entropy losses (already shifted).
        token_indices: Label positions to evaluate. Same convention as compute_perplexity.
        seq_len: Original sequence length (for bounds checking).
    """
    if token_indices is not None:
        idx = torch.tensor(
            [i - 1 for i in token_indices if 0 < i < seq_len],
            device=ce_losses.device,
        )
        if idx.numel() == 0:
            return float("nan")
        selected = ce_losses[idx]
    else:
        selected = ce_losses
    if selected.numel() == 0:
        return float("nan")
    return torch.exp(selected.mean()).item()


def compute_accuracy(predictions: List[str], references: List[str]) -> float:
    """Exact-match accuracy between prediction and reference string lists."""
    if len(predictions) == 0:
        return 0.0
    matches = sum(p == r for p, r in zip(predictions, references))
    return matches / len(predictions)
