"""IMM — Importance Margin Maximization for VLA visual token compression."""

from .soft_topk import SoftTopK
from .losses import MarginMaximizationLoss, IMMTotalLoss
from .token_selection import MarginAwareTokenSelector
from .acis import ACIS
from .smolvla_wrapper import IMMSmolVLAWrapper
from .metrics import (
    compute_margin,
    topk_preservation_rate,
    kendall_tau_distance,
    certified_bound,
    margin_statistics,
    compute_empirical_lipschitz,
    l_eps_delta_ratio,
)

__all__ = [
    "SoftTopK",
    "MarginMaximizationLoss",
    "IMMTotalLoss",
    "MarginAwareTokenSelector",
    "ACIS",
    "IMMSmolVLAWrapper",
    "compute_margin",
    "topk_preservation_rate",
    "kendall_tau_distance",
    "certified_bound",
    "margin_statistics",
    "compute_empirical_lipschitz",
    "l_eps_delta_ratio",
]
