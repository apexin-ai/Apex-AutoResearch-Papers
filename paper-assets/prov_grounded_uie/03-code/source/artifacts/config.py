"""ProvUIE training configuration.

All hyperparameters as dataclasses. Supports CLI override via HfArgumentParser.
Used by: train_sft.py, train_grpo.py, evaluate.py.
"""

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class ModelArgs:
    """Base model and LoRA configuration."""
    model_name_or_path: str = field(
        default="Qwen/Qwen3-8B",
        metadata={"help": "HuggingFace model ID or local path"},
    )
    lora_rank: int = field(default=32, metadata={"help": "LoRA rank"})
    lora_alpha: int = field(default=64, metadata={"help": "LoRA alpha"})
    lora_dropout: float = field(default=0.05, metadata={"help": "LoRA dropout"})
    lora_target_modules: str = field(
        default="q_proj,k_proj,v_proj,o_proj,gate_proj,up_proj,down_proj",
        metadata={"help": "Comma-separated LoRA target modules"},
    )
    use_flash_attention: bool = field(default=False, metadata={"help": "Use Flash Attention 2"})
    load_in_4bit: bool = field(default=False, metadata={"help": "4-bit quantization (QLoRA)"})

    def get_target_modules(self) -> list[str]:
        return [m.strip() for m in self.lora_target_modules.split(",")]


@dataclass
class SFTArgs:
    """SFT training hyperparameters."""
    output_dir: str = field(default="./outputs/sft", metadata={"help": "Output directory"})
    learning_rate: float = field(default=2e-4, metadata={"help": "Learning rate"})
    num_train_epochs: int = field(default=3, metadata={"help": "Training epochs"})
    per_device_train_batch_size: int = field(default=4, metadata={"help": "Batch size per device"})
    gradient_accumulation_steps: int = field(default=4, metadata={"help": "Gradient accumulation"})
    max_seq_length: int = field(default=4096, metadata={"help": "Max sequence length"})
    logging_steps: int = field(default=10, metadata={"help": "Logging interval"})
    save_steps: int = field(default=500, metadata={"help": "Checkpoint interval"})
    save_total_limit: int = field(default=3, metadata={"help": "Max checkpoints to keep"})
    bf16: bool = field(default=True, metadata={"help": "Use bfloat16"})
    warmup_ratio: float = field(default=0.03, metadata={"help": "Warmup ratio"})
    lr_scheduler_type: str = field(default="cosine", metadata={"help": "LR scheduler"})
    report_to: str = field(default="none", metadata={"help": "Logging backend (wandb/none)"})
    run_name: str = field(default="provuie-sft", metadata={"help": "W&B run name"})
    eval_strategy: str = field(default="steps", metadata={"help": "Evaluation strategy"})
    eval_steps: int = field(default=500, metadata={"help": "Evaluation interval"})
    gradient_checkpointing: bool = field(default=True, metadata={"help": "Gradient checkpointing"})


@dataclass
class GRPOArgs:
    """GRPO training hyperparameters."""
    output_dir: str = field(default="./outputs/grpo", metadata={"help": "Output directory"})
    sft_checkpoint: str = field(
        default="./outputs/sft/merged",
        metadata={"help": "Path to merged SFT checkpoint"},
    )
    num_generations: int = field(default=4, metadata={"help": "Completions per prompt"})
    temperature: float = field(default=0.7, metadata={"help": "Sampling temperature"})
    top_k: int = field(default=20, metadata={"help": "Top-k sampling (0=disabled, Qwen3 default=20)"})
    top_p: float = field(default=0.95, metadata={"help": "Nucleus sampling threshold (Qwen3 default=0.95)"})
    beta: float = field(default=0.05, metadata={"help": "KL penalty coefficient"})
    learning_rate: float = field(default=5e-6, metadata={"help": "Learning rate"})
    num_train_epochs: int = field(default=1, metadata={"help": "Training epochs"})
    max_steps: int = field(default=-1, metadata={"help": "Max training steps (-1 = use epochs)"})
    per_device_train_batch_size: int = field(default=2, metadata={"help": "Batch size per device"})
    gradient_accumulation_steps: int = field(default=8, metadata={"help": "Gradient accumulation"})
    max_completion_length: int = field(default=2048, metadata={"help": "Max generation tokens"})
    max_prompt_length: int = field(default=2048, metadata={"help": "Max prompt tokens"})
    logging_steps: int = field(default=10, metadata={"help": "Logging interval"})
    save_steps: int = field(default=200, metadata={"help": "Checkpoint interval"})
    save_total_limit: int = field(default=3, metadata={"help": "Max checkpoints to keep"})
    bf16: bool = field(default=True, metadata={"help": "Use bfloat16"})
    report_to: str = field(default="none", metadata={"help": "Logging backend"})
    run_name: str = field(default="provuie-grpo", metadata={"help": "W&B run name"})
    gradient_checkpointing: bool = field(default=True, metadata={"help": "Gradient checkpointing"})


@dataclass
class RewardArgs:
    """Reward function weights and parameters."""
    w_provenance: float = field(default=0.4, metadata={"help": "Provenance fidelity weight"})
    w_structural: float = field(default=0.4, metadata={"help": "Structural F1 weight"})
    w_format: float = field(default=0.2, metadata={"help": "Format compliance weight"})
    nli_model_name: str = field(
        default="/root/autodl-tmp/.hf_cache/ms_deberta/cross-encoder/nli-deberta-v3-large",
        metadata={"help": "NLI model for entailment scoring"},
    )
    nli_device: str = field(
        default="cpu",
        metadata={"help": "Device for NLI model (cpu/cuda/cuda:1)"},
    )
    nli_batch_size: int = field(default=32, metadata={"help": "NLI batch size"})
    length_penalty_factor: float = field(
        default=3.0,
        metadata={"help": "Evidence length penalty: penalty = max(0, 1 - pred_len/doc_len * factor)"},
    )
    iou_weight: float = field(default=0.5, metadata={"help": "IoU sub-weight in provenance reward"})
    nli_weight: float = field(default=0.3, metadata={"help": "NLI sub-weight in provenance reward"})
    length_weight: float = field(default=0.2, metadata={"help": "Length penalty sub-weight"})


@dataclass
class DataArgs:
    """Data paths and preprocessing options."""
    train_file: str = field(default="./data/docred_train.jsonl", metadata={"help": "Training JSONL"})
    dev_file: str = field(default="./data/docred_dev.jsonl", metadata={"help": "Dev JSONL"})
    max_train_samples: Optional[int] = field(default=None, metadata={"help": "Max train samples (debug)"})
    max_eval_samples: Optional[int] = field(default=None, metadata={"help": "Max eval samples (debug)"})


@dataclass
class EvalArgs:
    """Evaluation configuration."""
    model_path: str = field(default="./outputs/grpo/final", metadata={"help": "Checkpoint to evaluate"})
    eval_file: str = field(default="./data/docred_dev.jsonl", metadata={"help": "Evaluation JSONL"})
    output_file: str = field(default="./outputs/eval_results.json", metadata={"help": "Results output"})
    batch_size: int = field(default=8, metadata={"help": "Inference batch size"})
    max_prompt_length: int = field(default=4096, metadata={"help": "Max prompt tokens (must match SFT training)"})
    max_new_tokens: int = field(default=2048, metadata={"help": "Max generation tokens"})
    temperature: float = field(default=0.0, metadata={"help": "Generation temperature (0=greedy)"})
