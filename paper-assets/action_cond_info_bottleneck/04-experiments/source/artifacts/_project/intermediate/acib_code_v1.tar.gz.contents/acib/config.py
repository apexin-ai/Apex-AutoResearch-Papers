# ACIB hyperparameter configuration.
# Defines scorer architecture, loss weights, and mode (soft/hard).

from dataclasses import dataclass, field
from typing import Literal


@dataclass
class ACIBConfig:
    # --- Scorer architecture ---
    visual_dim: int = 960           # SmolVLA hidden_size (PixelShuffle output dim)
    condition_dim: int = 960        # conditioning signal dim (language embedding pooled)
    hidden_dim: int = 64            # scorer MLP hidden; use 64 or 128
    num_visual_tokens: int = 64     # tokens per frame after PixelShuffle(factor=4)

    # --- Mode ---
    mode: Literal["soft", "hard"] = "soft"
    top_k_ratio: float = 0.8       # hard mode: fraction of tokens to keep

    # --- Loss weights ---
    alpha: float = 1.0              # consistency loss weight (clean vs perturbed scores)
    beta: float = 0.01              # IB loss weight (sparsity regularization)

    # --- Training ---
    freeze_vlm: bool = True         # freeze VLM backbone (default SmolVLA behavior)
    freeze_action_expert: bool = False  # train action expert alongside scorer
    train_scorer_only: bool = False     # if True, freeze everything except scorer

    # --- Conditioning source ---
    # "language": pool language token embeddings as condition
    # "state": use robot state projection as condition
    # "both": concatenate language + state
    condition_source: Literal["language", "state", "both"] = "language"
