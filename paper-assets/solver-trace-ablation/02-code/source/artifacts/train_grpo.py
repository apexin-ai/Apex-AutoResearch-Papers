"""Phase 1 GRPO training: execution-only vs execution+STA reward.

Usage:
  # execution-only (GPU 0)
  CUDA_VISIBLE_DEVICES=0 python scripts/train_grpo.py \
    --model_path /root/autodl-tmp/models/Qwen3-4B \
    --data_path data/proofwriter_fol_500.jsonl \
    --reward_mode execution_only --output_dir outputs/grpo_exec_only \
    --num_steps 100 --wandb_project solver-trace-ablation

  # execution+STA (GPU 1)
  CUDA_VISIBLE_DEVICES=1 python scripts/train_grpo.py \
    --model_path /root/autodl-tmp/models/Qwen3-4B \
    --data_path data/proofwriter_fol_500.jsonl \
    --reward_mode execution_sta --output_dir outputs/grpo_exec_sta \
    --num_steps 100 --wandb_project solver-trace-ablation
"""

from __future__ import annotations

import argparse
import json
import logging
import os
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import torch
from datasets import Dataset
from transformers import AutoModelForCausalLM, AutoTokenizer, TrainerCallback
from trl import GRPOConfig, GRPOTrainer

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.solvers.factory import get_solver
from src.sta.reward import _parse_formalization, fast_sta_reward

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)


SYSTEM_PROMPT = (
    "You are a first-order logic (FOL) expert. "
    "Given natural language premises and a conclusion, formalize them into FOL.\n\n"
    "Output format:\n"
    "Premises:\n"
    "1. <FOL formula>\n"
    "2. <FOL formula>\n"
    "...\n"
    "Conclusion: <FOL formula>\n\n"
    "Use standard FOL notation with predicate-argument syntax: "
    "all x (P(x) -> Q(x)), exists x P(x), P(a) & Q(a), -P(a), P(a) | Q(a), P(a) -> Q(a)."
)

USER_TEMPLATE = (
    "Formalize the following in first-order logic.\n\n"
    "Context:\n{context}\n\n"
    "Statement to formalize:\n{question}"
)


def load_jsonl(path: str) -> list[dict]:
    data = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                data.append(json.loads(line))
    return data


def build_dataset(data: list[dict]) -> Dataset:
    records = []
    for item in data:
        prompt = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": USER_TEMPLATE.format(
                context=item["context"], question=item["question"]
            )},
        ]
        records.append({
            "prompt": prompt,
            "id": item.get("id", ""),
            "answer": item.get("answer", ""),
            "fol_premises": json.dumps(item.get("fol_premises", [])),
            "fol_conclusion": item.get("fol_conclusion", ""),
        })
    return Dataset.from_list(records)


def strip_thinking(text: str) -> str:
    return re.sub(r"<think>.*?</think>\s*", "", text, flags=re.DOTALL).strip()


def extract_completion_text(completion) -> str:
    """Extract text from a completion (handles both string and conversational formats)."""
    if isinstance(completion, list):
        return completion[-1]["content"] if completion else ""
    return completion


def make_reward_fn(reward_mode: str, solver, exec_weight: float = 0.5, sta_weight: float = 0.5):
    stats = {"total": 0, "parsed": 0, "proved": 0, "isr_sum": 0.0}
    step_buf = {"total": 0, "parsed": 0, "proved": 0, "isr_sum": 0.0, "reward_sum": 0.0}

    def reward_fn(prompts, completions, **kwargs):
        rewards = []
        for completion in completions:
            text = extract_completion_text(completion)
            cleaned = strip_thinking(text)
            stats["total"] += 1
            step_buf["total"] += 1

            if reward_mode == "execution_only":
                result = fast_sta_reward(
                    {}, cleaned, solver,
                    execution_weight=1.0, sta_weight=0.0, timeout=5,
                )
                reward_val = result["execution_reward"]
            else:
                result = fast_sta_reward(
                    {}, cleaned, solver,
                    execution_weight=exec_weight, sta_weight=sta_weight, timeout=5,
                )
                reward_val = result["combined_reward"]

            parsed = "error" not in result.get("details", {})
            proved = result["execution_reward"] > 0
            isr = result.get("sta_reward", 0.0)

            if parsed:
                stats["parsed"] += 1
                step_buf["parsed"] += 1
            if proved:
                stats["proved"] += 1
                step_buf["proved"] += 1
            stats["isr_sum"] += isr
            step_buf["isr_sum"] += isr
            step_buf["reward_sum"] += reward_val

            rewards.append(reward_val)
        return rewards

    def get_stats():
        n = stats["total"]
        if n == 0:
            return {}
        return {
            "parse_rate": stats["parsed"] / n,
            "prove_rate": stats["proved"] / n,
            "mean_isr": stats["isr_sum"] / n,
        }

    def get_step_stats():
        n = step_buf["total"]
        if n == 0:
            return {}
        result = {
            "parse_rate": step_buf["parsed"] / n,
            "prove_rate": step_buf["proved"] / n,
            "mean_isr": step_buf["isr_sum"] / n,
            "reward_mean": step_buf["reward_sum"] / n,
            "reward_std": 0.0,
        }
        step_buf["total"] = 0
        step_buf["parsed"] = 0
        step_buf["proved"] = 0
        step_buf["isr_sum"] = 0.0
        step_buf["reward_sum"] = 0.0
        return result

    def reset_stats():
        stats["total"] = 0
        stats["parsed"] = 0
        stats["proved"] = 0
        stats["isr_sum"] = 0.0

    reward_fn.get_stats = get_stats
    reward_fn.get_step_stats = get_step_stats
    reward_fn.reset_stats = reset_stats
    return reward_fn


class LocalLogCallback(TrainerCallback):
    def __init__(self, output_dir, reward_fn):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.log_path = self.output_dir / "reward_log.jsonl"
        self.reward_fn = reward_fn
        self.last_step = 0

    def on_log(self, args, state, control, logs=None, **kwargs):
        if logs is None or state.global_step == 0:
            return
        if state.global_step == self.last_step:
            return
        self.last_step = state.global_step
        step_stats = self.reward_fn.get_step_stats()
        entry = {
            "step": state.global_step,
            "reward_mean": logs.get("reward", step_stats.get("reward_mean", 0.0)),
            "reward_std": logs.get("reward_std", step_stats.get("reward_std", 0.0)),
            "prove_rate": step_stats.get("prove_rate", 0.0),
            "isr_mean": step_stats.get("mean_isr", 0.0),
            "parse_rate": step_stats.get("parse_rate", 0.0),
            "loss": logs.get("loss", 0.0),
            "lr": logs.get("learning_rate", 0.0),
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }
        with open(self.log_path, "a") as f:
            f.write(json.dumps(entry) + "\n")
            f.flush()
        print(
            f"[REWARD_LOG] step={entry['step']} reward={entry['reward_mean']:.4f} "
            f"prove_rate={entry['prove_rate']:.3f} isr={entry['isr_mean']:.3f} "
            f"parse_rate={entry['parse_rate']:.3f}",
            flush=True,
        )


def parse_args():
    parser = argparse.ArgumentParser(description="Phase 1 GRPO Training")
    parser.add_argument("--model_path", type=str, default=None)
    parser.add_argument("--data_path", type=str, default=None)
    parser.add_argument("--reward_mode", type=str, default=None,
                        choices=["execution_only", "execution_sta"])
    parser.add_argument("--output_dir", type=str, default=None)
    parser.add_argument("--num_steps", type=int, default=None)
    parser.add_argument("--per_device_batch_size", type=int, default=None)
    parser.add_argument("--gradient_accumulation_steps", type=int, default=None)
    parser.add_argument("--num_generations", type=int, default=None)
    parser.add_argument("--max_completion_length", type=int, default=None)
    parser.add_argument("--learning_rate", type=float, default=None)
    parser.add_argument("--exec_weight", type=float, default=None)
    parser.add_argument("--sta_weight", type=float, default=None)
    parser.add_argument("--seed", type=int, default=None)
    parser.add_argument("--solver", type=str, default=None)
    parser.add_argument("--wandb_project", type=str, default=None)
    parser.add_argument("--wandb_run", type=str, default=None)
    parser.add_argument("--no_wandb", action="store_true")
    parser.add_argument("--config", type=str, default=None,
                        help="YAML config file (overrides CLI args)")
    args = parser.parse_args()

    if args.config:
        cfg = load_yaml_config(args.config)
        for k, v in cfg.items():
            if hasattr(args, k):
                current = getattr(args, k)
                if current is None:
                    setattr(args, k, v)
            else:
                setattr(args, k, v)

    _fallbacks = {
        "num_steps": 100, "per_device_batch_size": 4,
        "gradient_accumulation_steps": 2, "num_generations": 4,
        "max_completion_length": 512, "learning_rate": 1e-6,
        "exec_weight": 0.5, "sta_weight": 0.5, "seed": 42, "solver": "prover9",
    }
    for k, v in _fallbacks.items():
        if getattr(args, k, None) is None:
            setattr(args, k, v)

    missing = [f for f in ("model_path", "data_path", "reward_mode", "output_dir")
               if getattr(args, f, None) is None]
    if missing:
        parser.error(f"the following arguments are required: {', '.join('--' + f for f in missing)}")

    return args


def load_yaml_config(path: str) -> dict:
    import yaml
    with open(path) as f:
        return yaml.safe_load(f)


def main():
    args = parse_args()

    if args.no_wandb:
        os.environ["WANDB_MODE"] = "disabled"

    report_to = "none" if args.no_wandb else "wandb"
    if args.wandb_project and not args.no_wandb:
        import wandb
        run_name = args.wandb_run or f"grpo_{args.reward_mode}"
        wandb.init(project=args.wandb_project, name=run_name, config=vars(args))

    logger.info(f"Loading data from {args.data_path}")
    raw_data = load_jsonl(args.data_path)
    dataset = build_dataset(raw_data)
    logger.info(f"Dataset: {len(dataset)} examples")

    logger.info(f"Initializing solver: {args.solver}")
    solver = get_solver(args.solver)
    logger.info(f"Solver ready: {type(solver).__name__}")

    reward_fn = make_reward_fn(
        args.reward_mode, solver,
        exec_weight=args.exec_weight, sta_weight=args.sta_weight,
    )

    grpo_config = GRPOConfig(
        output_dir=args.output_dir,
        max_steps=args.num_steps,
        per_device_train_batch_size=args.per_device_batch_size,
        gradient_accumulation_steps=args.gradient_accumulation_steps,
        learning_rate=args.learning_rate,
        num_generations=args.num_generations,
        max_completion_length=args.max_completion_length,
        logging_steps=1,
        save_steps=50,
        save_total_limit=2,
        save_only_model=True,
        report_to=report_to,
        bf16=True,
        seed=args.seed,
        log_completions=True,
        num_completions_to_print=2,
        chat_template_kwargs={"enable_thinking": False},
    )

    logger.info(f"Loading model from {args.model_path}")
    trainer = GRPOTrainer(
        model=args.model_path,
        reward_funcs=reward_fn,
        args=grpo_config,
        train_dataset=dataset,
        callbacks=[LocalLogCallback(args.output_dir, reward_fn)],
    )

    logger.info(f"Starting GRPO training: mode={args.reward_mode}, steps={args.num_steps}")
    trainer.train()

    logger.info("Saving final model")
    trainer.save_model(args.output_dir)

    final_stats = reward_fn.get_stats()
    logger.info(f"Final reward stats: {final_stats}")

    if not args.no_wandb and args.wandb_project:
        import wandb
        wandb.log({"final/" + k: v for k, v in final_stats.items()})
        wandb.finish()

    logger.info("Done.")


if __name__ == "__main__":
    main()
