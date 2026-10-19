"""
Configuration constants for Meta-Brain Phase 0 perturbation classifier.

Defines perturbation taxonomies, layer indices, model dimensions,
and hyperparameter defaults shared across collect/train/eval scripts.
"""

# ---------------------------------------------------------------------------
# Perturbation taxonomy
# ---------------------------------------------------------------------------

PERTURBATION_TYPES_6CLASS = {
    "camera_viewpoints": 0,
    "light_conditions": 1,
    "background_textures": 2,
    "sensor_noise": 3,
    "objects_layout": 4,
    "robot_initial_states": 5,
}

PERTURBATION_TYPES_3CLASS = {
    "visual": 0,   # camera + light + background + noise
    "spatial": 1,  # layout
    "physical": 2, # robot
}

CLASS_6_TO_3_MAPPING = {
    0: 0,  # camera_viewpoints   -> visual
    1: 0,  # light_conditions    -> visual
    2: 0,  # background_textures -> visual
    3: 0,  # sensor_noise        -> visual
    4: 1,  # objects_layout      -> spatial
    5: 2,  # robot_initial_states -> physical
}

CLASS_6_NAMES = [
    "camera_viewpoints",
    "light_conditions",
    "background_textures",
    "sensor_noise",
    "objects_layout",
    "robot_initial_states",
]

CLASS_3_NAMES = ["visual", "spatial", "physical"]

BINARY_NAMES = ["nominal", "perturbed"]

# ---------------------------------------------------------------------------
# π₀ architecture constants
# ---------------------------------------------------------------------------

PALIGEMMA_LAYERS = [2, 4, 6, 8, 10, 12, 14, 16]
EXPERT_LAYERS = [2, 6, 10, 14]

PALIGEMMA_HIDDEN_DIM = 2048
EXPERT_HIDDEN_DIM = 1024

PALIGEMMA_NUM_LAYERS = 18  # layers[0..17]
EXPERT_NUM_LAYERS = 18

# PyTorch module path templates
PALIGEMMA_LAYER_TEMPLATE = (
    "model.paligemma_with_expert.paligemma.language_model.layers.{i}"
)
EXPERT_LAYER_TEMPLATE = (
    "model.paligemma_with_expert.gemma_expert.model.layers.{i}"
)

# ---------------------------------------------------------------------------
# Pooling strategies
# ---------------------------------------------------------------------------

POOLING_STRATEGIES = ["mean", "first", "last", "first_last"]

def pooling_output_dim(pooling: str, hidden_dim: int) -> int:
    """Return output dimension for a given pooling strategy."""
    if pooling == "first_last":
        return hidden_dim * 2
    return hidden_dim

# ---------------------------------------------------------------------------
# Classifier defaults
# ---------------------------------------------------------------------------

CLASSIFIER_HIDDEN_DIM = 256
DEFAULT_LR = 1e-3
DEFAULT_EPOCHS = 50
DEFAULT_BATCH_SIZE = 64
NUM_FOLDS = 5

# Activation source → input dimension calculation
ACTIVATION_SOURCES = ["paligemma_only", "expert_only", "both"]

def compute_input_dim(activation_source: str, pooling: str) -> int:
    """Compute classifier input dimension from source and pooling strategy."""
    pg_dim = len(PALIGEMMA_LAYERS) * pooling_output_dim(pooling, PALIGEMMA_HIDDEN_DIM)
    ex_dim = len(EXPERT_LAYERS) * pooling_output_dim(pooling, EXPERT_HIDDEN_DIM)
    if activation_source == "paligemma_only":
        return pg_dim
    elif activation_source == "expert_only":
        return ex_dim
    elif activation_source == "both":
        return pg_dim + ex_dim
    raise ValueError(f"Unknown activation_source: {activation_source}")

# ---------------------------------------------------------------------------
# Sweep grid
# ---------------------------------------------------------------------------

SWEEP_POOLINGS = ["mean", "first", "first_last"]
SWEEP_SOURCES = ["paligemma_only", "expert_only", "both"]
SWEEP_LRS = [1e-2, 1e-3, 1e-4]

# ---------------------------------------------------------------------------
# Go / No-Go thresholds (Phase 0 success criteria)
# ---------------------------------------------------------------------------

GO_NOGO = {
    "6class_accuracy_min": 0.50,   # >50% on 6-class (chance=16.7%)
    "3class_accuracy_min": 0.65,   # >65% on 3-class (chance=33.3%)
    "binary_accuracy_min": 0.80,   # >80% on binary (chance=50%)
    "binary_roc_auc_min": 0.85,
}
