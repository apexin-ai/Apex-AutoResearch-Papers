# Global configuration: model paths, GPU mapping, dataset config, experiment params.

from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Tuple

# ── Paths ──────────────────────────────────────────────────────────────
PROJECT_ROOT = Path("/root/cert_manip_resist_eval")
ARTIFACTS_DIR = PROJECT_ROOT / "artifacts"
RESULTS_DIR = ARTIFACTS_DIR / "results"
LOGS_DIR = ARTIFACTS_DIR / "logs"

# ── Model Configuration ───────────────────────────────────────────────
# model_id -> (local_path, gpu_id, family_name)
# Paths are placeholders — update after models are downloaded.
MODEL_REGISTRY: Dict[str, Tuple[str, int, str]] = {
    "qwen2.5-72b": (
        "/root/autodl-tmp/models/Qwen2.5-72B-Instruct-AWQ",
        0,
        "qwen",
    ),
    "llama3.1-70b": (
        "/root/autodl-tmp/models/Llama-3.1-70B-Instruct-AWQ",
        1,
        "meta",
    ),
    "mistral-large": (
        "/root/autodl-tmp/models/Mistral-Large-Instruct-2407-AWQ",
        2,
        "mistral",
    ),
    "qwen2.5-32b": (
        "/root/autodl-tmp/models/Qwen2.5-32B-Instruct-AWQ",
        3,
        "qwen",
    ),
    "qwen2.5-14b": (
        "/root/autodl-tmp/models/Qwen2.5-14B-Instruct-AWQ",
        3,
        "qwen",
    ),
    "llama3.1-8b": (
        "/root/autodl-tmp/models/Llama-3.1-8B-Instruct-AWQ",
        1,
        "meta",
    ),
}

# ── Dataset Configuration ─────────────────────────────────────────────
# dataset_name -> (hf_id, config_name, split, n_samples)
DATASET_REGISTRY: Dict[str, Tuple[str, str, str, int]] = {
    "mmlu": ("cais/mmlu", "all", "test", 300),
    "arc_challenge": ("allenai/ai2_arc", "ARC-Challenge", "test", 300),
}

# ── Experiment Parameters ─────────────────────────────────────────────
RANDOM_SEED: int = 42
N_SAMPLES: int = 300
N_BOOTSTRAP: int = 1000
BOOTSTRAP_ALPHA: float = 0.05

# ── Panel Configuration ───────────────────────────────────────────────
# Heterogeneous panels: cross-family combinations
HETERO_PANELS: List[List[str]] = [
    ["qwen2.5-72b", "llama3.1-70b", "mistral-large"],
    ["qwen2.5-72b", "llama3.1-70b"],
    ["qwen2.5-72b", "mistral-large"],
    ["llama3.1-70b", "mistral-large"],
    ["qwen2.5-72b", "llama3.1-70b", "mistral-large", "qwen2.5-32b"],
]

# Homogeneous panels: same-family (Qwen), all distinct models per panel
HOMO_PANELS: List[List[str]] = [
    ["qwen2.5-72b", "qwen2.5-32b"],                      # K=2
    ["qwen2.5-72b", "qwen2.5-32b", "qwen2.5-14b"],      # K=3
]

# ── vLLM Serving ──────────────────────────────────────────────────────
VLLM_MAX_MODEL_LEN: int = 4096
VLLM_GPU_MEMORY_UTILIZATION: float = 0.90
VLLM_TEMPERATURE: float = 0.0
VLLM_MAX_TOKENS: int = 512


@dataclass
class ExperimentConfig:
    """Bundles all config for a single experiment run."""
    seed: int = RANDOM_SEED
    n_samples: int = N_SAMPLES
    n_bootstrap: int = N_BOOTSTRAP
    bootstrap_alpha: float = BOOTSTRAP_ALPHA
    model_ids: List[str] = field(default_factory=lambda: list(MODEL_REGISTRY.keys()))
    datasets: List[str] = field(default_factory=lambda: list(DATASET_REGISTRY.keys()))
    results_dir: Path = RESULTS_DIR
