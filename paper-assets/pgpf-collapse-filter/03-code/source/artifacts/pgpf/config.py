"""Default configuration for PGPF recursive training pipeline."""

from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional


@dataclass
class LoRAConfig:
    r: int = 16
    lora_alpha: int = 16
    lora_dropout: float = 0.05
    target_modules: list[str] = field(default_factory=lambda: ["q_proj", "v_proj", "k_proj", "o_proj"])
    task_type: str = "CAUSAL_LM"


@dataclass
class TrainingConfig:
    per_device_train_batch_size: int = 16
    gradient_accumulation_steps: int = 1
    learning_rate: float = 2e-4
    lr_scheduler_type: str = "linear"
    warmup_steps: int = 5
    num_train_epochs: int = 3
    max_seq_length: int = 2048
    bf16: bool = True
    logging_steps: int = 10
    save_strategy: str = "epoch"


@dataclass
class GenerationConfig:
    max_new_tokens: int = 512
    temperature: float = 0.7
    top_p: float = 0.9
    do_sample: bool = True
    num_return_sequences: int = 1


@dataclass
class PGPFConfig:
    model_name: str = "Qwen/Qwen2.5-1.5B"
    dataset_name: str = "teknium/OpenHermes-2.5"
    num_generations: int = 3
    filter_method: str = "pgpf_static"  # no_filter | random | confidence | pgpf_static | lexical_only
    retention_rate: float = 0.5
    num_synthetic_per_gen: int = 8000
    real_data_mix_ratio: float = 0.5  # fraction of real data mixed each generation

    # PGPF thresholds (percentile-based, applied to gen-0 distribution)
    lexical_conformity_percentile: float = 50.0
    semantic_novelty_percentile: float = 50.0
    quality_percentile: float = 50.0

    # Embedding model for semantic novelty
    embedding_model: str = "dunzhang/stella_en_1.5B_v5"
    bleu_corpus_k: int = 50

    # Paths
    output_dir: str = "outputs"
    data_dir: str = "data"
    seed: int = 42

    lora: LoRAConfig = field(default_factory=LoRAConfig)
    training: TrainingConfig = field(default_factory=TrainingConfig)
    generation: GenerationConfig = field(default_factory=GenerationConfig)

    def checkpoint_dir(self, generation: int) -> Path:
        return Path(self.output_dir) / f"gen_{generation}" / "checkpoint"

    def metrics_path(self, generation: int) -> Path:
        return Path(self.output_dir) / f"gen_{generation}" / "metrics.json"

    def synthetic_data_path(self, generation: int) -> Path:
        return Path(self.output_dir) / f"gen_{generation}" / "synthetic.jsonl"

    def scored_data_path(self, generation: int) -> Path:
        return Path(self.output_dir) / f"gen_{generation}" / "scored.jsonl"
