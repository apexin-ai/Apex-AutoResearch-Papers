"""
GRPO RLVR Recovery Training for pruned models — v4.

Changes from v3:
- Fix: ref_model loaded via load_pruned_model (monkey-patch create_model_from_path)
  to handle non-uniform MLP/attention dimensions. beta=0.01 KL penalty now works.
- Fix: temperature 0.7 -> 0.4 (mitigate sampling degradation from v2)
- Fix: repetition_penalty=1.15 added to reduce repetitive outputs
- Kept: gradient_checkpointing=True, format_reward, max_completion_length=2048
"""

import argparse
import logging
import os
import random
import re

import numpy as np
import torch
from datasets import load_dataset
from transformers import AutoConfig, AutoTokenizer, TrainerCallback
from model_utils import load_pruned_model
from trl import GRPOConfig, GRPOTrainer
import trl.trainer.grpo_trainer as _grpo_module

try:
    import wandb
except ImportError:
    wandb = None

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger(__name__)

# --- Monkey-patch: make GRPOTrainer load pruned ref_model correctly ---
_original_create_model = _grpo_module.create_model_from_path


def _create_pruned_ref_model(model_id, architecture=None, **kwargs):
    config = AutoConfig.from_pretrained(model_id, trust_remote_code=True)
    if hasattr(config, "per_layer_intermediate_size") or hasattr(config, "per_layer_num_heads"):
        logger.info(f"Loading pruned ref_model from {model_id}")
        torch_dtype = kwargs.get("dtype", torch.bfloat16)
        if isinstance(torch_dtype, str):
            torch_dtype = getattr(torch, torch_dtype, torch.bfloat16)
        device_map = kwargs.get("device_map", "auto")
        ref_model = load_pruned_model(model_id, device_map=device_map, torch_dtype=torch_dtype)
        ref_model.eval()
        for p in ref_model.parameters():
            p.requires_grad = False
        return ref_model
    return _original_create_model(model_id, architecture=architecture, **kwargs)


_grpo_module.create_model_from_path = _create_pruned_ref_model
# --- End monkey-patch ---


def set_seed(seed: int):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)


class RewardDesertCallback(TrainerCallback):
    def __init__(self, patience: int = 50):
        self.patience = patience
        self.zero_reward_count = 0
        self.last_logged_step = -1

    def on_log(self, args, state, control, logs=None, **kwargs):
        if logs is None:
            return
        reward_mean = logs.get("reward", logs.get("rewards/mean", None))
        if reward_mean is None:
            return
        if state.global_step == self.last_logged_step:
            return
        self.last_logged_step = state.global_step

        if reward_mean == 0.0:
            self.zero_reward_count += 1
            if self.zero_reward_count >= self.patience:
                logger.warning(
                    f"REWARD DESERT: reward=0 for {self.zero_reward_count} consecutive "
                    f"log events (~{self.zero_reward_count * args.logging_steps} steps). "
                    f"Pruned model may be too weak for GRPO. Stopping."
                )
                control.should_training_stop = True
        else:
            self.zero_reward_count = 0


def extract_answer(text: str) -> str | None:
    boxed = re.findall(r"\\boxed\{([^}]+)\}", text)
    if boxed:
        return boxed[-1].strip().replace(",", "")
    hash_match = re.findall(r"####\s*(.+)", text)
    if hash_match:
        return hash_match[-1].strip().replace(",", "")
    numbers = re.findall(r"-?\d+(?:,\d{3})*(?:\.\d+)?", text)
    if numbers:
        return numbers[-1].replace(",", "")
    return None


def normalize_answer(ans: str) -> str:
    ans = ans.strip().replace(",", "").replace(" ", "")
    try:
        val = float(ans)
        if val == int(val):
            return str(int(val))
        return str(val)
    except (ValueError, OverflowError):
        return ans


def extract_gold_answer(answer_text: str) -> str:
    match = re.search(r"####\s*(.+)", answer_text)
    if match:
        return normalize_answer(match.group(1))
    return answer_text.strip()


def has_boxed_format(text: str) -> bool:
    return bool(re.search(r"\\boxed\{[^}]+\}", text))


def build_reward_fn(tokenizer, format_reward_weight: float = 0.1):
    def reward_fn(completions, **kwargs):
        gold_answers = kwargs.get("answer", None)
        rewards = []
        for i, completion in enumerate(completions):
            if isinstance(completion, list):
                text = completion[-1]["content"] if completion else ""
            else:
                text = completion

            pred = extract_answer(text)

            if gold_answers is not None and i < len(gold_answers):
                gold = normalize_answer(str(gold_answers[i]))
            else:
                gold = None

            if pred is not None and gold is not None:
                pred_norm = normalize_answer(pred)
                accuracy_reward = 1.0 if pred_norm == gold else 0.0
            else:
                accuracy_reward = 0.0

            fmt_reward = format_reward_weight if has_boxed_format(text) else 0.0
            rewards.append(accuracy_reward + fmt_reward)

        return rewards

    return reward_fn


def prepare_dataset(tokenizer, max_samples: int = None, seed: int = 42):
    ds = load_dataset("openai/gsm8k", "main", split="train")
    if max_samples is not None:
        ds = ds.shuffle(seed=seed).select(range(min(max_samples, len(ds))))

    is_qwen = "qwen" in tokenizer.name_or_path.lower() or "qwen" in getattr(tokenizer, "vocab_file", "").lower()

    def format_prompt(example):
        if is_qwen:
            messages = [
                {"role": "system", "content": "Please reason step by step, and put your final answer within \\boxed{}."},
                {"role": "user", "content": example["question"]},
            ]
            example["prompt"] = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        else:
            example["prompt"] = (
                f"Solve the following math problem step by step. "
                f"Put your final answer in \\boxed{{}}.\n\n"
                f"Question: {example['question']}\n\nAnswer:"
            )
        example["answer"] = extract_gold_answer(example["answer"])
        return example

    ds = ds.map(format_prompt)
    return ds


def main():
    parser = argparse.ArgumentParser(description="GRPO RLVR recovery training v4")
    parser.add_argument("--model_path", type=str, required=True)
    parser.add_argument("--output_dir", type=str, default=None)
    parser.add_argument("--gpu", type=int, default=0)
    parser.add_argument("--learning_rate", type=float, default=1e-6)
    parser.add_argument("--num_train_epochs", type=int, default=3)
    parser.add_argument("--per_device_train_batch_size", type=int, default=2)
    parser.add_argument("--gradient_accumulation_steps", type=int, default=8)
    parser.add_argument("--max_completion_length", type=int, default=512)
    parser.add_argument("--temperature", type=float, default=0.4)
    parser.add_argument("--repetition_penalty", type=float, default=1.15)
    parser.add_argument("--num_generations", type=int, default=4)
    parser.add_argument("--max_samples", type=int, default=None)
    parser.add_argument("--logging_steps", type=int, default=10)
    parser.add_argument("--save_steps", type=int, default=100)
    parser.add_argument("--save_total_limit", type=int, default=3)
    parser.add_argument("--reward_desert_patience", type=int, default=50)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--dtype", type=str, default="bfloat16", choices=["float16", "bfloat16", "float32"])
    parser.add_argument("--report_to", type=str, default="wandb")
    parser.add_argument("--run_name", type=str, default=None)
    parser.add_argument("--wandb_project", type=str, default="recovery_aware_struct_prune")
    parser.add_argument("--beta", type=float, default=0.01)
    parser.add_argument("--loss_type", type=str, default="dapo")
    parser.add_argument("--format_reward_weight", type=float, default=0.1)
    parser.add_argument("--gradient_checkpointing", type=str, default="true")
    parser.add_argument("--optim", type=str, default="adamw_8bit", help="optimizer type, e.g. adamw_torch or adamw_8bit")
    parser.add_argument("--max_steps", type=int, default=-1, help="max training steps (-1 = use num_train_epochs)")
    args = parser.parse_args()

    if args.output_dir is None:
        model_name = os.path.basename(args.model_path.rstrip("/"))
        args.output_dir = f"/root/autodl-tmp/recovered_{model_name}"

    set_seed(args.seed)
    os.environ["WANDB_PROJECT"] = args.wandb_project

    log_dir = "/root/autodl-tmp/recovery_aware_struct_prune/logs/"
    os.makedirs(log_dir, exist_ok=True)
    os.makedirs(args.output_dir, exist_ok=True)

    logger.info(f"Loading pruned model from {args.model_path}")
    tokenizer = AutoTokenizer.from_pretrained(args.model_path, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    dtype_map = {"float16": torch.float16, "bfloat16": torch.bfloat16, "float32": torch.float32}
    torch_dtype = dtype_map[args.dtype]

    model = load_pruned_model(args.model_path, device_map="auto", torch_dtype=torch_dtype)

    logger.info("Preparing GSM8K training dataset...")
    dataset = prepare_dataset(tokenizer, max_samples=args.max_samples, seed=args.seed)
    logger.info(f"Training on {len(dataset)} samples")

    reward_fn = build_reward_fn(tokenizer, format_reward_weight=args.format_reward_weight)

    use_gc = args.gradient_checkpointing.lower() in ("true", "1", "yes")

    grpo_config = GRPOConfig(
        output_dir=args.output_dir,
        learning_rate=args.learning_rate,
        num_train_epochs=args.num_train_epochs,
        per_device_train_batch_size=args.per_device_train_batch_size,
        gradient_accumulation_steps=args.gradient_accumulation_steps,
        max_completion_length=args.max_completion_length,
        temperature=args.temperature,
        repetition_penalty=args.repetition_penalty,
        num_generations=args.num_generations,
        beta=args.beta,
        loss_type=args.loss_type,
        run_name=args.run_name or f"grpo_{os.path.basename(args.model_path.rstrip('/'))}",
        logging_steps=args.logging_steps,
        save_steps=args.save_steps,
        save_total_limit=args.save_total_limit,
        seed=args.seed,
        bf16=(args.dtype == "bfloat16"),
        fp16=(args.dtype == "float16"),
        remove_unused_columns=False,
        log_completions=True,
        report_to=args.report_to,
        logging_dir=log_dir,
        save_strategy="steps",
        gradient_checkpointing=use_gc,
        optim=args.optim,
        max_steps=args.max_steps,
    )

    desert_cb = RewardDesertCallback(patience=args.reward_desert_patience)

    trainer = GRPOTrainer(
        model=model,
        args=grpo_config,
        train_dataset=dataset,
        reward_funcs=reward_fn,
        processing_class=tokenizer,
        callbacks=[desert_cb],
    )

    logger.info(f"Starting GRPO v4 training (GPU {args.gpu})...")
    logger.info(f"Output: {args.output_dir}")
    logger.info(f"beta={args.beta}, loss_type={args.loss_type}, format_reward={args.format_reward_weight}")
    logger.info(f"temperature={args.temperature}, repetition_penalty={args.repetition_penalty}")
    logger.info(f"Reward desert patience: {args.reward_desert_patience} log events")
    logger.info(f"ref_model loaded via monkey-patched create_model_from_path (pruned-model aware)")
    logger.info(f"optimizer: {args.optim}")
    trainer.train()

    if desert_cb.zero_reward_count >= desert_cb.patience:
        logger.warning("Training stopped due to reward desert. Saving checkpoint anyway.")

    logger.info(f"Saving recovered model to {args.output_dir}")
    trainer.save_model(args.output_dir)
    tokenizer.save_pretrained(args.output_dir)
    logger.info("GRPO v4 recovery training complete.")


if __name__ == "__main__":
    main()
