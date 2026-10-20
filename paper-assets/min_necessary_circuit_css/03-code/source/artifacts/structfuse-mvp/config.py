"""StructFuse MVP configuration.
Defines model/task/method settings, CSS thresholds, and CIRCUS config-bagging params.
"""

from dataclasses import dataclass, field
from typing import List


@dataclass
class MVPConfig:
    model_name: str = "gpt2-small"
    task: str = "ioi"
    num_samples: int = 100

    # K=3 methods
    methods: List[str] = field(default_factory=lambda: ["eap_ig", "edge_pruning", "acdc"])
    K: int = 3

    # CSS thresholds: {0, 1/3, 2/3, 1}
    css_thresholds: List[float] = field(default_factory=lambda: [0.0, 0.33, 0.67, 1.0])
    css_default_threshold: float = 0.67  # >= 2/3 methods agree

    # CIRCUS config-bagging for EAP-IG
    circus_B: int = 10  # number of threshold bins
    circus_core_threshold: float = 1.0
    circus_contingent_threshold: float = 0.5

    # Method-specific
    eap_ig_steps: int = 5
    eap_ig_topn: int = 100
    acdc_threshold: float = 0.05
    edge_pruning_target_sparsity: float = 0.05

    # Evaluation
    faithfulness_metrics: List[str] = field(default_factory=lambda: ["cpr", "cmd"])


MVP_CONFIG = MVPConfig()


@dataclass
class LargeModelConfig(MVPConfig):
    """Config for large models (0.5B-8B) where ACDC is replaced by IFR."""
    model_name: str = "Qwen/Qwen2.5-0.5B"
    methods: List[str] = field(default_factory=lambda: ["eap_ig", "edge_pruning", "ifr"])
    num_samples: int = 50

    eap_ig_topn: int = 200
    ifr_topn: int = 200
