"""Central configuration for contrastive_trace_safety project."""

import os
from pathlib import Path

# Paths — set DATA_DIR and MODEL_DIR environment variables before running
PROJECT_ROOT = Path(os.environ.get("DATA_DIR", "."))
ARTIFACTS_DIR = PROJECT_ROOT / "artifacts"
HIDDEN_STATES_DIR = ARTIFACTS_DIR / "hidden_states"
PROBES_DIR = ARTIFACTS_DIR / "probes"

# Model
MODEL_NAME = "deepseek-ai/DeepSeek-R1-Distill-Llama-8B"
MODEL_PATH = os.environ.get("MODEL_DIR", "models") + "/DeepSeek-R1-Distill-Llama-8B"

# Dataset
HF_DATASET = "ishitakakkar-10/HarmThoughts"
TARGET_MODEL = "r1-8b"

# Hidden state extraction
LAYERS = list(range(12, 25))  # layers 12-24, 13 layers total
NUM_LAYERS = len(LAYERS)
HIDDEN_DIM = 4096
EXTRACT_BATCH_SIZE = 4
DEVICE = "cuda:0"

# Probes
WINDOW_SIZE = 5
TEMPORAL_HIDDEN_DIM = 512
LEARNING_RATE = 1e-3
TRAIN_EPOCHS = 20
PROBE_BATCH_SIZE = 64
DEFAULT_LAYER = 20  # for static probe

# Data split
TRAIN_RATIO = 0.6
VAL_RATIO = 0.2
SEED = 42

# Evaluation
DETECTION_THRESHOLD = 0.9
DETECTION_WINDOW = 5

# Safety labels that define commitment point
SAFETY_LABELS = {"RA", "AL", "CC", "ED", "IA"}
