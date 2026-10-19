from dataclasses import dataclass, field
from typing import Literal


@dataclass
class ACIBConfig:
    visual_dim: int = 960
    condition_dim: int = 960
    hidden_dim: int = 64
    num_visual_tokens: int = 64

    mode: Literal["soft", "hard"] = "soft"
    top_k_ratio: float = 0.8

    alpha: float = 0.01
    beta: float = 0.1

    freeze_vlm: bool = True
    freeze_action_expert: bool = False
    train_scorer_only: bool = False

    # v7.2: unified freeze mode (overrides legacy booleans when not "legacy")
    freeze_mode: Literal["legacy", "scorer_only", "connector_scorer", "all_trainable"] = "legacy"

    condition_source: Literal["language", "visual_mean", "state", "both"] = "language"
    stop_grad_task: bool = False

    # v7: contrastive auxiliary loss
    lambda_contrastive: float = 0.0

    # v8: conditioning mode
    conditioning_mode: Literal["concat", "film"] = "concat"

    # Residual connection for eval: alpha=0 pass-through, alpha=1 pure multiplicative
    scoring_alpha: float = 1.0

    # v7.2: connector drift regularization weight
    lambda_drift: float = 0.1
