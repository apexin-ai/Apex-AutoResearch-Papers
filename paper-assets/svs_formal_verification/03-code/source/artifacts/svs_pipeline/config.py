"""Pipeline configuration.

All tunable parameters in one place. Override via environment variables
or by modifying this file directly for experiments.
"""

import os
from dataclasses import dataclass, field


@dataclass
class APIConfig:
    """LLM API settings (OpenAI-compatible)."""
    base_url: str = os.getenv("SVS_API_BASE_URL", "https://api.deepseek.com/v1")
    api_key: [REDACTED] = os.getenv("SVS_API_KEY", "")
    model: str = os.getenv("SVS_MODEL", "deepseek-chat")
    formalization_model: str = os.getenv("SVS_FORMAL_MODEL", "deepseek-chat")
    formalization_base_url: str = os.getenv("SVS_FORMAL_API_BASE_URL", "https://api.deepseek.com/v1")
    formalization_api_key: [REDACTED] = os.getenv("SVS_FORMAL_API_KEY", "")
    max_retries: int = 3
    timeout: int = 60


@dataclass
class SamplingConfig:
    """Chain sampling parameters."""
    num_chains: int = 8          # N: chains per problem
    temperature: float = 0.7     # T: sampling temperature
    max_tokens: int = 2048       # max tokens per chain


@dataclass
class VerificationConfig:
    """Z3 verification parameters."""
    z3_timeout_ms: int = 5000    # Z3 solver timeout per check
    ic_weight: float = 0.5       # weight for internal consistency in chain score
    fc_weight: float = 0.5       # weight for formalization confidence in chain score
    cclc_lambda: float = 0.3     # weight for CCLC in group score


@dataclass
class MVPConfig:
    """MVP experiment parameters."""
    num_problems: int = 50       # number of problems for MVP
    dataset: str = "proofwriter"
    subset: str = "depth-5"
    seed: int = 42
    # P2 statistical thresholds (Reviewer-adjusted)
    cohens_d_threshold: float = 0.15
    p_value_threshold: float = 0.05
    require_ci_excludes_zero: bool = True


@dataclass
class PipelineConfig:
    api: APIConfig = field(default_factory=APIConfig)
    sampling: SamplingConfig = field(default_factory=SamplingConfig)
    verification: VerificationConfig = field(default_factory=VerificationConfig)
    mvp: MVPConfig = field(default_factory=MVPConfig)
    output_dir: str = "outputs"
    verbose: bool = True
