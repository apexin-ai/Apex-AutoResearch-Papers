"""
Phase 1 LoRA Expert Training — Configuration.

Centralized hyperparameters, paths, and perturbation taxonomy for
training per-perturbation-type LoRA adapters on pi0's PaliGemma backbone.

Dependencies: (none — pure Python dataclasses)
"""

import dataclasses
from pathlib import Path

# ---------------------------------------------------------------------------
# Perturbation taxonomy (from Phase 0)
# ---------------------------------------------------------------------------

PERTURBATION_TYPES = ["visual", "spatial", "physical", "universal"]

PERTURBATION_DESCRIPTIONS = {
    "visual": "camera viewpoints + lighting + background + sensor noise",
    "spatial": "object layout perturbations",
    "physical": "robot initial state perturbations",
    "universal": "mixed — all perturbation types",
}

# ---------------------------------------------------------------------------
# Model architecture constants
# ---------------------------------------------------------------------------

PALIGEMMA_NUM_LAYERS = 18
PALIGEMMA_HIDDEN_DIM = 2048
ACTION_EXPERT_NUM_LAYERS = 18
ACTION_EXPERT_HIDDEN_DIM = 1024

# Default pi0 config
ACTION_DIM = 32
ACTION_HORIZON = 50
MAX_TOKEN_LEN = 48

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

PI0_CHECKPOINT = "/root/autodl-tmp/checkpoints/pi0_base"
PI0_WEIGHTS = f"{PI0_CHECKPOINT}/model.safetensors"
OPENPI_ROOT = "/root/openpi"
PROJECT_ROOT = "/root/meta_brain_lora_routing"

DEFAULT_CHECKPOINT_BASE = f"{PROJECT_ROOT}/checkpoints/phase1"

# Data paths (placeholders for spatial/physical — populated by data workers)
DATA_PATHS = {
    "visual": "physical-intelligence/libero",  # HuggingFace repo for standard demos
    "spatial": f"{PROJECT_ROOT}/data/spatial_rollouts",  # placeholder
    "physical": f"{PROJECT_ROOT}/data/physical_rollouts",  # placeholder
    "universal": None,  # mixed from all above
}

# ---------------------------------------------------------------------------
# LoRA configuration
# ---------------------------------------------------------------------------

@dataclasses.dataclass
class LoRAConfig:
    rank: int = 16
    alpha: int = 32
    dropout: float = 0.05
    bias: str = "none"

    # Target: ALL PaliGemma attention Q/K/V/O projections (18 layers).
    # Action Expert layers are NOT modified.
    # Module name patterns are auto-detected at runtime (see train script).
    attn_projections: tuple = ("q_proj", "k_proj", "v_proj", "o_proj")

    @property
    def scaling(self) -> float:
        return self.alpha / self.rank


# ---------------------------------------------------------------------------
# Training configuration
# ---------------------------------------------------------------------------

@dataclasses.dataclass
class TrainConfig:
    perturbation_type: str = "visual"
    gpu: int = 0
    epochs: int = 10
    batch_size: int = 8
    lr: float = 1e-4
    weight_decay: float = 0.01
    warmup_steps: int = 100
    grad_clip_norm: float = 1.0
    seed: int = 42
    dry_run: bool = False

    # LoRA
    lora: LoRAConfig = dataclasses.field(default_factory=LoRAConfig)

    # Checkpoint
    checkpoint_dir: str = ""

    # Early stopping: halt if val MSE doesn't improve for this many evals
    patience: int = 3

    # Logging
    wandb_project: str = "meta_brain_lora_routing"
    wandb_group: str = "phase1_lora"
    log_interval: int = 10  # steps between loss prints

    # Flow-matching time sampling (pi0 default)
    time_beta_alpha: float = 1.5
    time_beta_beta: float = 1.0

    # OpenPI config name for LIBERO data pipeline
    openpi_config_name: str = "pi0_libero"

    def __post_init__(self):
        if self.perturbation_type not in PERTURBATION_TYPES:
            raise ValueError(
                f"Unknown perturbation_type '{self.perturbation_type}'. "
                f"Valid: {PERTURBATION_TYPES}"
            )
        if not self.checkpoint_dir:
            self.checkpoint_dir = (
                f"{DEFAULT_CHECKPOINT_BASE}/{self.perturbation_type}"
            )

    @property
    def wandb_name(self) -> str:
        return f"{self.perturbation_type}_seed{self.seed}"

    @property
    def device_str(self) -> str:
        return f"cuda:{self.gpu}"


# ---------------------------------------------------------------------------
# Dry-run overrides
# ---------------------------------------------------------------------------

def apply_dry_run_overrides(cfg: TrainConfig) -> TrainConfig:
    """Shrink everything for a quick pipeline validation."""
    cfg.epochs = 1
    cfg.batch_size = 2
    cfg.log_interval = 1
    cfg.warmup_steps = 2
    cfg.patience = 999  # don't early-stop in dry-run
    return cfg
