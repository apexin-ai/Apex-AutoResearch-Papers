"""Pilot experiment configuration for collapse-aware-mixing MVP.

Validates spectral effective rank as a leading indicator of model collapse
in iterative synthetic training (Pythia-1B, 3 generations x 500M tokens).
"""

import os
from dataclasses import dataclass


@dataclass
class PilotConfig:
    # --- Model ---
    model_name: str = "EleutherAI/pythia-1b"

    # --- Training ---
    num_generations: int = 3                    # G0 (real), G1 (synth from G0), G2 (synth from G1)
    tokens_per_generation: int = 100_000_000    # 100M tokens per generation
    checkpoint_interval_tokens: int = 10_000_000  # save + eval every 10M tokens
    max_seq_length: int = 2048
    per_device_batch_size: int = 8
    gradient_accumulation_steps: int = 4
    learning_rate: float = 2e-6
    warmup_ratio: float = 0.05
    weight_decay: float = 0.01
    seed: int = 42
    bf16: bool = True
    gradient_checkpointing: bool = True

    # --- Synthetic data generation ---
    gen_temperature: float = 1.0
    gen_top_p: float = 0.95
    gen_batch_size: int = 32
    gen_max_new_tokens: int = 2048

    # --- Metrics ---
    spectral_num_samples: int = 50_000          # sequences for spectral effective rank
    spectral_batch_size: int = 64
    metrics_gen_tokens: int = 500_000           # tokens to generate at each ckpt for n-gram/coverage
    ppl_num_samples: int = 5_000                # sequences for PPL evaluation
    ppl_batch_size: int = 16

    # --- Data ---
    real_dataset: str = "wikitext"
    real_dataset_config: str = "wikitext-103-raw-v1"
    holdout_size: int = 10_000                  # sequences reserved for evaluation
    fixed_ratio: float | None = None            # real/synth mixing ratio: None=original, 0.0=pure synth, 1.0=pure real

    # --- Paths ---
    output_dir: str = "./output"

    # --- Logging ---
    use_wandb: bool = True
    wandb_project: str = "collapse-aware-mixing"
    wandb_run_prefix: str = "pilot"

    # --- Derived properties ---

    @property
    def effective_batch_size(self) -> int:
        return self.per_device_batch_size * self.gradient_accumulation_steps

    @property
    def tokens_per_step(self) -> int:
        return self.max_seq_length * self.effective_batch_size

    @property
    def save_steps(self) -> int:
        return self.checkpoint_interval_tokens // self.tokens_per_step

    @property
    def max_steps(self) -> int:
        return self.tokens_per_generation // self.tokens_per_step

    def gen_dir(self, g: int) -> str:
        return os.path.join(self.output_dir, f"G{g}")

    def checkpoint_dir(self, g: int, step: int) -> str:
        return os.path.join(self.gen_dir(g), "training", f"checkpoint-{step}")

    def synthetic_data_path(self, g: int) -> str:
        return os.path.join(self.gen_dir(g), "synthetic_data")

    def metrics_path(self, g: int) -> str:
        return os.path.join(self.gen_dir(g), "metrics.jsonl")

    def summary_path(self) -> str:
        return os.path.join(self.output_dir, "pilot_summary.json")
