"""EASS (Expected-Attention Segment Scoring) — aggregates per-token EA scores
to segment-level budgets using structural priors and EASS-calibrated modulation."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Dict, List, Sequence, Tuple

if TYPE_CHECKING:
    import torch

# ---------------------------------------------------------------------------
# Segment data structure (interface contract with role_extractor.py)
# ---------------------------------------------------------------------------

@dataclass
class Segment:
    role: str          # SYSTEM_PROMPT | USER_MESSAGE | ASSISTANT_MESSAGE | TOOL_CALL | TOOL_RESULT | THINKING_TRACE
    start_idx: int     # inclusive
    end_idx: int       # exclusive
    turn_index: int    # 0-based conversation turn


# ---------------------------------------------------------------------------
# Structural prior table
# ---------------------------------------------------------------------------

# B_prior values per (role, recency_bucket).
# "recent" = within 2 turns of the latest turn.
_B_PRIOR: Dict[Tuple[str, str], float] = {
    ("SYSTEM_PROMPT",    "any"):    1.0,
    ("TOOL_RESULT",      "recent"): 0.8,
    ("TOOL_RESULT",      "older"):  0.5,
    ("USER_MESSAGE",     "any"):    0.6,
    ("ASSISTANT_MESSAGE","any"):    0.6,
    ("TOOL_CALL",        "any"):    0.5,
    ("THINKING_TRACE",   "recent"): 0.4,
    ("THINKING_TRACE",   "older"):  0.15,
}

_RECENT_TURN_THRESHOLD = 2  # turns within this distance count as "recent"


def _recency_bucket(role: str, turn_index: int, max_turn: int) -> str:
    if role == "SYSTEM_PROMPT":
        return "any"
    distance = max_turn - turn_index
    if role in ("TOOL_RESULT", "THINKING_TRACE"):
        return "recent" if distance <= _RECENT_TURN_THRESHOLD else "older"
    return "any"


def _get_b_prior(role: str, turn_index: int, max_turn: int) -> float:
    bucket = _recency_bucket(role, turn_index, max_turn)
    key = (role, bucket)
    if key in _B_PRIOR:
        return _B_PRIOR[key]
    # Fallback: try "any" bucket, then default 0.5
    return _B_PRIOR.get((role, "any"), 0.5)


# ---------------------------------------------------------------------------
# Core functions
# ---------------------------------------------------------------------------

def compute_eass(
    ea_scores: "torch.Tensor",
    segments: Sequence[Segment],
) -> "torch.Tensor":
    """Aggregate per-token EA scores to per-segment EASS.

    Args:
        ea_scores: shape (batch, num_kv_heads, seq_len)
        segments: ordered, non-overlapping segments covering the sequence

    Returns:
        Tensor of shape (batch, num_kv_heads, num_segments) with mean EA per segment.
    """
    import torch

    B, H, _S = ea_scores.shape
    N = len(segments)
    eass = torch.zeros(B, H, N, dtype=ea_scores.dtype, device=ea_scores.device)

    for i, seg in enumerate(segments):
        length = seg.end_idx - seg.start_idx
        if length <= 0:
            continue
        eass[:, :, i] = ea_scores[:, :, seg.start_idx : seg.end_idx].mean(dim=-1)

    return eass


def compute_budget(
    segments: Sequence[Segment],
    eass_scores: "torch.Tensor",
    *,
    beta: float = 0.5,
    b_min: float = 0.1,
    b_max: float = 1.0,
    max_turn: int | None = None,
) -> "torch.Tensor":
    """Compute per-segment retention budget B_final.

    B_final(s) = clip(B_prior(s) * (1 + β * z_eass(s)), B_min, B_max)

    where z_eass is the z-scored EASS (per batch×head). Recency is encoded
    solely through B_prior's recent/older bucket selection — no additional
    continuous decay factor.

    Args:
        segments: segment list
        eass_scores: shape (batch, num_kv_heads, num_segments)
        beta: sensitivity of budget to EASS deviation
        b_min / b_max: clipping bounds
        max_turn: latest turn index; inferred from segments if None

    Returns:
        Tensor of shape (batch, num_kv_heads, num_segments) with budget in [b_min, b_max].
    """
    import torch

    if max_turn is None:
        max_turn = max(s.turn_index for s in segments) if segments else 0

    B, H, N = eass_scores.shape

    # --- structural prior (recency encoded via bucket, not continuous decay) ---
    b_prior = torch.zeros(N, dtype=eass_scores.dtype, device=eass_scores.device)

    for i, seg in enumerate(segments):
        b_prior[i] = _get_b_prior(seg.role, seg.turn_index, max_turn)

    # broadcast to (1, 1, N) for element-wise ops
    b_prior = b_prior.unsqueeze(0).unsqueeze(0)

    # --- z-score EASS per (batch, head) ---
    mean = eass_scores.mean(dim=-1, keepdim=True)
    std = eass_scores.std(dim=-1, keepdim=True).clamp(min=1e-8)
    z = (eass_scores - mean) / std

    b_final = b_prior * (1.0 + beta * z)
    b_final = b_final.clamp(min=b_min, max=b_max)

    return b_final


def map_budget_to_scores(
    ea_scores: "torch.Tensor",
    segments: Sequence[Segment],
    budgets: "torch.Tensor",
) -> "torch.Tensor":
    """Modulate per-token EA scores by their segment's normalized budget.

    Budgets are normalized so the token-weighted mean equals 1.0,
    turning them from suppression factors into redistribution factors:
    high-budget segments get multiplier > 1.0, low-budget segments get < 1.0,
    but overall scoring power is preserved.

    Args:
        ea_scores: shape (batch, num_kv_heads, seq_len)
        segments: segment list
        budgets: shape (batch, num_kv_heads, num_segments)

    Returns:
        Modulated scores, same shape as ea_scores.
    """
    import torch

    # Token-weighted mean budget for normalization
    total_tokens = 0
    weighted_sum = budgets[:, :, :1] * 0.0
    for i, seg in enumerate(segments):
        length = seg.end_idx - seg.start_idx
        if length > 0:
            weighted_sum = weighted_sum + budgets[:, :, i : i + 1] * length
            total_tokens += length

    if total_tokens > 0:
        budget_mean = (weighted_sum / total_tokens).clamp(min=1e-8)
    else:
        budget_mean = weighted_sum + 1.0
    normalized = budgets / budget_mean

    out = ea_scores.clone()
    for i, seg in enumerate(segments):
        if seg.end_idx <= seg.start_idx:
            continue
        out[:, :, seg.start_idx : seg.end_idx] *= normalized[:, :, i : i + 1]
    return out
