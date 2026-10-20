"""Unified LoRA fine-tuning for CWM (Code World Model) generation — supports multiple model families.

Supported model families:
  - Qwen3 (e.g. Qwen/Qwen3-4B, Qwen/Qwen3-8B)
  - DeepSeek-Coder (e.g. deepseek-ai/deepseek-coder-6.7b-instruct)

Usage:
  # Qwen3-8B
  python train_unified.py --data_dir data/ --model_name_or_path Qwen/Qwen3-8B \
      --output_dir checkpoints_cwm_qwen3_8b/ --run_name cwm-qwen3-8b-lora

  # DeepSeek-Coder-6.7B-Instruct
  python train_unified.py --data_dir data/ --model_name_or_path deepseek-ai/deepseek-coder-6.7b-instruct \
      --output_dir checkpoints_cwm_deepseek/ --run_name cwm-deepseek-6.7b-lora

Hyperparams are identical across families: LoRA rank=16, alpha=32, 3 epochs, bf16.
"""

import argparse
import json
import logging
import os

import torch
from datasets import Dataset
from peft import LoraConfig, TaskType, get_peft_model
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    DataCollatorForSeq2Seq,
    Trainer,
    TrainingArguments,
)

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger(__name__)

SYSTEM_PROMPTS = {
    "cwm": (
        "You are a code execution simulator. Given a code snippet and a test case, "
        "predict the execution result."
    ),
    "cls": (
        "You are a code verifier. Given a code patch and a test name, "
        "predict whether the test will pass or fail when run against the patched code."
    ),
}

USER_TEMPLATES = {
    "cwm": "## Code\n{code}\n\n## Test\n{test}\n\nWhat is the execution result?",
    "cls": "## Patch (git diff)\n{code}\n\n## Test\n{test}\n\nWill this test pass or fail?",
}

# ---------------------------------------------------------------------------
# Model family detection & configuration
# ---------------------------------------------------------------------------

FAMILY_CONFIG = {
    "qwen": {
        # Qwen3 uses ChatML-style template; needs enable_thinking=False to suppress <think> tags
        "lora_target_modules": ["q_proj", "k_proj", "v_proj", "o_proj"],
    },
    "deepseek": {
        # DeepSeek-Coder-Instruct uses "### Instruction / ### Response" template
        # No special chat template kwargs needed
        "lora_target_modules": ["q_proj", "k_proj", "v_proj", "o_proj"],
    },
}


def detect_model_family(model_name: str) -> str:
    name_lower = model_name.lower()
    if "qwen" in name_lower:
        return "qwen"
    if "deepseek" in name_lower:
        return "deepseek"
    return "auto"


def get_chat_template_kwargs(family: str, tokenizer) -> dict:
    """Return extra kwargs for tokenizer.apply_chat_template(), per model family."""
    if family == "qwen":
        # Qwen3 tokenizers accept enable_thinking; older Qwen2 ones don't
        try:
            tokenizer.apply_chat_template(
                [{"role": "user", "content": "hi"}],
                tokenize=False,
                enable_thinking=False,
            )
            return {"enable_thinking": False}
        except TypeError:
            return {}
    # DeepSeek and auto: no special kwargs
    return {}


def setup_tokenizer(tokenizer, family: str):
    """Ensure pad_token is set; handle family-specific token quirks."""
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
        log.info(f"Set pad_token = eos_token ({tokenizer.eos_token!r})")

    if family == "deepseek" and tokenizer.pad_token_id == tokenizer.eos_token_id:
        # DeepSeek-Coder uses <|EOT|> as eos. Using it as pad is fine for training
        # with DataCollatorForSeq2Seq (labels are masked), but log it for awareness.
        log.info(
            f"DeepSeek: pad_token_id == eos_token_id == {tokenizer.eos_token_id} "
            f"({tokenizer.eos_token!r})"
        )


def get_lora_target_modules(family: str) -> list[str]:
    cfg = FAMILY_CONFIG.get(family, FAMILY_CONFIG["qwen"])
    return cfg["lora_target_modules"]


# ---------------------------------------------------------------------------
# Prompt / tokenization (family-agnostic via apply_chat_template)
# ---------------------------------------------------------------------------

def build_messages(code, test, target=None, task="cwm"):
    user_msg = USER_TEMPLATES[task].format(code=code, test=test)
    msgs = [
        {"role": "system", "content": SYSTEM_PROMPTS[task]},
        {"role": "user", "content": user_msg},
    ]
    if target is not None:
        msgs.append({"role": "assistant", "content": target})
    return msgs


def get_target(example, task):
    if task == "cls":
        return "pass" if example["label"] == 1 else "fail"
    if "target" in example:
        return example["target"]
    if "execution_output" in example:
        return example["execution_output"]
    return None


def _try_apply_chat_template(tokenizer, messages, tmpl_kw, **kwargs):
    """apply_chat_template with graceful fallback if system role is unsupported."""
    try:
        return tokenizer.apply_chat_template(messages, **tmpl_kw, **kwargs)
    except Exception:
        # Some models don't support system role — merge system into first user message
        merged = []
        sys_content = ""
        for m in messages:
            if m["role"] == "system":
                sys_content = m["content"]
            elif m["role"] == "user" and sys_content:
                merged.append({"role": "user", "content": sys_content + "\n\n" + m["content"]})
                sys_content = ""
            else:
                merged.append(m)
        return tokenizer.apply_chat_template(merged, **tmpl_kw, **kwargs)


def tokenize_example(tokenizer, code, test, target, max_len, tmpl_kw, task="cwm"):
    prompt_ids = _try_apply_chat_template(
        tokenizer,
        build_messages(code, test, task=task),
        tmpl_kw,
        tokenize=True,
        add_generation_prompt=True,
    )
    full_ids = _try_apply_chat_template(
        tokenizer,
        build_messages(code, test, target, task=task),
        tmpl_kw,
        tokenize=True,
        add_generation_prompt=False,
    )

    truncated = len(full_ids) > max_len
    if truncated:
        full_ids = full_ids[:max_len]

    prompt_len = min(len(prompt_ids), len(full_ids))
    labels = [-100] * prompt_len + full_ids[prompt_len:]

    return {
        "input_ids": full_ids,
        "labels": labels,
        "attention_mask": [1] * len(full_ids),
    }, truncated


def load_jsonl(path):
    with open(path) as f:
        return [json.loads(line) for line in f]


def preprocess_split(tokenizer, data, max_len, name, tmpl_kw, task="cwm"):
    out = {"input_ids": [], "labels": [], "attention_mask": []}
    n_trunc = 0
    n_skip = 0
    for ex in data:
        target = get_target(ex, task)
        if target is None:
            n_skip += 1
            continue
        tok, trunc = tokenize_example(
            tokenizer, ex["code"], ex["test"], target, max_len, tmpl_kw, task=task,
        )
        for k in out:
            out[k].append(tok[k])
        n_trunc += int(trunc)
    if n_skip:
        log.warning(f"{name}: skipped {n_skip}/{len(data)} examples with no target or execution_output")
    pct = n_trunc / len(data) * 100 if data else 0
    log.info(f"{name}: {n_trunc}/{len(data)} truncated ({pct:.1f}%)")
    return Dataset.from_dict(out)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    p = argparse.ArgumentParser(description="Unified LoRA training (Qwen / DeepSeek / auto)")
    p.add_argument("--data_dir", required=True)
    p.add_argument("--model_name_or_path", required=True, help="HF model id or local path")
    p.add_argument("--task", choices=["cls", "cwm"], default="cwm",
                   help="Task: cls (pass/fail classification) or cwm (execution simulation)")
    p.add_argument("--train_file", default=None, help="Override train JSONL filename")
    p.add_argument("--val_file", default=None, help="Override val JSONL filename")
    p.add_argument("--output_dir", default="checkpoints_cwm/")
    p.add_argument("--wandb_project", default="exec-sim-repair-verifier")
    p.add_argument("--run_name", default=None, help="W&B run name (auto-generated if omitted)")
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--max_seq_length", type=int, default=2048)
    p.add_argument("--batch_size", type=int, default=2)
    p.add_argument("--grad_accumulation", type=int, default=16)
    p.add_argument("--lr", type=float, default=2e-4)
    p.add_argument("--epochs", type=int, default=3)
    p.add_argument("--warmup_ratio", type=float, default=0.1)
    p.add_argument("--lora_rank", type=int, default=16)
    p.add_argument("--lora_alpha", type=int, default=32)
    p.add_argument("--lora_dropout", type=float, default=0.05)
    p.add_argument("--max_steps", type=int, default=-1)
    p.add_argument("--no_wandb", action="store_true")
    p.add_argument("--resume_from_checkpoint", default=None,
                   help="Path to checkpoint dir to resume training from")
    args = p.parse_args()

    family = detect_model_family(args.model_name_or_path)
    log.info(f"Model: {args.model_name_or_path} → family={family}")

    if args.run_name is None:
        short = args.model_name_or_path.split("/")[-1].lower().replace("_", "-")
        args.run_name = f"{args.task}-{short}-lora"
    log.info(f"Task: {args.task}, Run name: {args.run_name}")

    if args.no_wandb:
        os.environ["WANDB_DISABLED"] = "true"
    else:
        os.environ["WANDB_PROJECT"] = args.wandb_project

    # ── Tokenizer ──
    log.info(f"Loading tokenizer: {args.model_name_or_path}")
    tokenizer = AutoTokenizer.from_pretrained(
        args.model_name_or_path, trust_remote_code=True, padding_side="right",
    )
    setup_tokenizer(tokenizer, family)
    tmpl_kw = get_chat_template_kwargs(family, tokenizer)
    log.info(f"Chat template kwargs: {tmpl_kw}")

    # Sanity check: render one example to verify template works
    sample_target = "pass" if args.task == "cls" else "PASS: test completed successfully"
    sample_text = _try_apply_chat_template(
        tokenizer,
        build_messages("def f(): return 1", "assert f() == 1", sample_target, task=args.task),
        tmpl_kw,
        tokenize=False,
        add_generation_prompt=False,
    )
    log.info(f"Sample formatted prompt (first 300 chars):\n{sample_text[:300]}")

    # ── Data ──
    if args.train_file:
        train_path = os.path.join(args.data_dir, args.train_file)
    elif args.task == "cls":
        # Prefer repo-level swebench data if available
        repo_path = os.path.join(args.data_dir, "swebench_full", "swebench_train.jsonl")
        func_path = os.path.join(args.data_dir, "train.jsonl")
        train_path = repo_path if os.path.exists(repo_path) else func_path
    else:
        train_path = os.path.join(args.data_dir, "cwm_train.jsonl")

    if args.val_file:
        val_path = os.path.join(args.data_dir, args.val_file)
    elif args.task == "cls":
        repo_path = os.path.join(args.data_dir, "swebench_full", "swebench_val.jsonl")
        func_path = os.path.join(args.data_dir, "val.jsonl")
        val_path = repo_path if os.path.exists(repo_path) else func_path
    else:
        val_path = os.path.join(args.data_dir, "cwm_val.jsonl")

    log.info(f"Train file: {train_path}")
    log.info(f"Val file: {val_path}")
    train_raw = load_jsonl(train_path)
    val_raw = load_jsonl(val_path)
    log.info(f"Loaded train={len(train_raw)}, val={len(val_raw)}")

    train_ds = preprocess_split(tokenizer, train_raw, args.max_seq_length, "train", tmpl_kw, task=args.task)
    val_ds = preprocess_split(tokenizer, val_raw, args.max_seq_length, "val", tmpl_kw, task=args.task)

    # ── Model ──
    log.info(f"Loading model: {args.model_name_or_path}")
    try:
        import flash_attn  # noqa: F401
        attn_impl = "flash_attention_2"
    except ImportError:
        attn_impl = "sdpa"
    log.info(f"Attention: {attn_impl}")

    model = AutoModelForCausalLM.from_pretrained(
        args.model_name_or_path,
        torch_dtype=torch.bfloat16,
        trust_remote_code=True,
        attn_implementation=attn_impl,
    )
    model.config.use_cache = False

    # ── LoRA ──
    target_modules = get_lora_target_modules(family)
    log.info(f"LoRA target modules: {target_modules}")

    lora_cfg = LoraConfig(
        task_type=TaskType.CAUSAL_LM,
        r=args.lora_rank,
        lora_alpha=args.lora_alpha,
        lora_dropout=args.lora_dropout,
        target_modules=target_modules,
    )
    model = get_peft_model(model, lora_cfg)
    model.enable_input_require_grads()
    model.print_trainable_parameters()

    # ── Training ──
    collator = DataCollatorForSeq2Seq(tokenizer=tokenizer, padding=True)

    is_dryrun = args.max_steps > 0
    ta = {
        "output_dir": args.output_dir,
        "num_train_epochs": args.epochs,
        "max_steps": args.max_steps,
        "per_device_train_batch_size": args.batch_size,
        "per_device_eval_batch_size": args.batch_size,
        "gradient_accumulation_steps": args.grad_accumulation,
        "learning_rate": args.lr,
        "warmup_ratio": args.warmup_ratio,
        "bf16": True,
        "logging_steps": 1 if is_dryrun else 50,
        "eval_strategy": "no" if is_dryrun else "epoch",
        "save_strategy": "no" if is_dryrun else "epoch",
        "load_best_model_at_end": not is_dryrun,
        "save_total_limit": 2,
        "seed": args.seed,
        "run_name": args.run_name,
        "report_to": "none" if args.no_wandb else "wandb",
        "gradient_checkpointing": True,
        "dataloader_num_workers": 4,
    }
    if not is_dryrun:
        ta["metric_for_best_model"] = "eval_loss"
        ta["greater_is_better"] = False
    training_args = TrainingArguments(**ta)

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_ds,
        eval_dataset=val_ds,
        data_collator=collator,
    )

    log.info("Starting training...")
    trainer.train(resume_from_checkpoint=args.resume_from_checkpoint)

    if not is_dryrun:
        best_dir = os.path.join(args.output_dir, "best")
        trainer.save_model(best_dir)
        tokenizer.save_pretrained(best_dir)
        log.info(f"Best model saved to {best_dir}")
    else:
        log.info("Dry-run complete.")


if __name__ == "__main__":
    main()
