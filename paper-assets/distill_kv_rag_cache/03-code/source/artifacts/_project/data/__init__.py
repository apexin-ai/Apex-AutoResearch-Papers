"""CompressLink: Joint compression-restoration optimization for RAG KV cache."""

from .rope_utils import (
    rotate_half,
    apply_rope_query_only,
    apply_rope_key_only,
    remove_rope,
    get_rope_embeddings,
)
from .budget_manager import RecomputationBudgetManager
from .boundary_recomp import BoundaryRecomputer
from .raba import (
    compute_restoration_weighted_eigenvalues,
    get_position_prior_probs,
    raba_bit_allocation,
    dp_bit_allocation,
    greedy_bit_allocation,
)
from .cegr import CEGRSelector
from .query_probe import QueryRelevanceProbe
from .nope_attention import patch_model_for_nope, unpatch_model
from .pipeline import CompressLinkPipeline

__all__ = [
    "rotate_half",
    "apply_rope_query_only",
    "apply_rope_key_only",
    "remove_rope",
    "get_rope_embeddings",
    "RecomputationBudgetManager",
    "BoundaryRecomputer",
    "compute_restoration_weighted_eigenvalues",
    "get_position_prior_probs",
    "raba_bit_allocation",
    "dp_bit_allocation",
    "greedy_bit_allocation",
    "CEGRSelector",
    "QueryRelevanceProbe",
    "patch_model_for_nope",
    "unpatch_model",
    "CompressLinkPipeline",
]
