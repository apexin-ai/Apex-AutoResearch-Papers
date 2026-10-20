# train_cwm_baseline.py — Qwen3 LoRA fine-tuning for CWM (Code World Model) generation baseline
# Input: data_dir/ with {cwm_train,cwm_val}.jsonl (fields: code, test, target)
# Output: LoRA adapter in output_dir/best/
# Key difference from train_verifier.py (classification):
#   - Prompt asks for execution result instead of pass/fail
#   - Target is execution output string (e.g. "PASS: ..." or "FAIL: AssertionError: ...")
#   - Standard causal LM loss on target tokens (no classification head)
#   - Loss masked on system+user tokens, only computed on assistant response
# Same: LoRA config, batch_size, grad_accumulation, lr, epochs, seed, max_seq_len

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

SYSTEM_PROMPT = (
    "You are a code execution simulator. Given a code snippet and a test case, "
    "predict the execution result."
)


def load_jsonl(path):
    with open(path) as f:
        return [json.loads(line) for line in f]


def detect_thinking_support(tokenizer):
    """Qwen3 tokenizers support enable_thinking; older ones don't."""
    try:
        tokenizer.apply_chat_template(
            [{"role": "user", "content": "hi"}],
            tokenize=False,
            enable_thinking=False,
        )
        return {"enable_thinking": False}
    except TypeError:
        return {}


def build_messages(code, test, target=None):
    user_msg = f"## Code\n{code}\n\n## Test\n{test}\n\nWhat is the execution result?"
    msgs = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_msg},
    ]
    if target is not None:
        msgs.append({"role": "assistant", "content": target})
    return msgs


def tokenize_example(tokenizer, code, test, target, max_len, tmpl_kw):
    prompt_ids = tokenizer.apply_chat_template(
        build_messages(code, test),
        tokenize=True, add_generation_prompt=True, **tmpl_kw,
    )
    full_ids = tokenizer.apply_chat_template(
        build_messages(code, test, target),
        tokenize=True, add_generation_prompt=False, **tmpl_kw,
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


def preprocess_split(tokenizer, data, max_len, name, tmpl_kw):
    out = {"input_ids": [], "labels": [], "attention_mask": []}
    n_trunc = 0
    for ex in data:
        tok, trunc = tokenize_example(
            tokenizer, ex["code"], ex["test"], ex["target"], max_len, tmpl_kw,
        )
        for k in out:
            out[k].append(tok[k])
        n_trunc += int(trunc)
    pct = n_trunc / len(data) * 100 if data else 0
    log.info(f"{name}: {n_trunc}/{len(data)} truncated ({pct:.1f}%)")
    return Dataset.from_dict(out)


def main():
    p = argparse.ArgumentParser(description="Train Qwen3 LoRA CWM generation baseline")
    p.add_argument("--data_dir", required=True)
    p.add_argument("--model_name", default="Qwen/Qwen3-4B")
    p.add_argument("--output_dir", default="checkpoints_cwm/")
    p.add_argument("--wandb_project", default="exec-sim-repair-verifier")
    p.add_argument("--run_name", default="cwm-qwen3-4b-lora")
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
    args = p.parse_args()

    if args.no_wandb:
        os.environ["WANDB_DISABLED"] = "true"
    else:
        os.environ["WANDB_PROJECT"] = args.wandb_project

    log.info(f"Loading tokenizer: {args.model_name}")
    tokenizer = AutoTokenizer.from_pretrained(
        args.model_name, trust_remote_code=True, padding_side="right",
    )
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    tmpl_kw = detect_thinking_support(tokenizer)
    log.info(f"Chat template kwargs: {tmpl_kw}")

    train_raw = load_jsonl(os.path.join(args.data_dir, "cwm_train.jsonl"))
    val_raw = load_jsonl(os.path.join(args.data_dir, "cwm_val.jsonl"))
    log.info(f"Loaded train={len(train_raw)}, val={len(val_raw)}")

    train_ds = preprocess_split(tokenizer, train_raw, args.max_seq_length, "train", tmpl_kw)
    val_ds = preprocess_split(tokenizer, val_raw, args.max_seq_length, "val", tmpl_kw)

    log.info(f"Loading model: {args.model_name}")
    try:
        import flash_attn  # noqa: F401
        attn_impl = "flash_attention_2"
    except ImportError:
        attn_impl = "sdpa"
    log.info(f"Attention: {attn_impl}")

    model = AutoModelForCausalLM.from_pretrained(
        args.model_name,
        torch_dtype=torch.bfloat16,
        trust_remote_code=True,
        attn_implementation=attn_impl,
    )
    model.config.use_cache = False

    lora_cfg = LoraConfig(
        task_type=TaskType.CAUSAL_LM,
        r=args.lora_rank,
        lora_alpha=args.lora_alpha,
        lora_dropout=args.lora_dropout,
        target_modules=["q_proj", "k_proj", "v_proj", "o_proj"],
    )
    model = get_peft_model(model, lora_cfg)
    model.enable_input_require_grads()
    model.print_trainable_parameters()

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
    trainer.train()

    if not is_dryrun:
        best_dir = os.path.join(args.output_dir, "best")
        trainer.save_model(best_dir)
        tokenizer.save_pretrained(best_dir)
        log.info(f"Best model saved to {best_dir}")
    else:
        log.info("Dry-run complete.")


if __name__ == "__main__":
    main()
