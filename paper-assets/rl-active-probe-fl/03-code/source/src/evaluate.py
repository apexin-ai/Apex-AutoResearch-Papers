"""Evaluation script for probe generation models.

Evaluates base/SFT/GRPO models on debugging accuracy, probe quality,
probe execution rate, and probe dependence.

Input: data/eval.jsonl + model checkpoint
Output: JSON results file with metrics and bootstrap CIs
Dependencies: transformers, peft, torch, numpy
"""

import argparse
import json
import logging
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import numpy as np
import torch
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer

from src.prompts import (
    PROBE_GENERATION_PROMPT,
    PROBE_GENERATION_SYSTEM,
    PROBE_GENERATION_WITH_OUTPUT_PROMPT,
)
from src.sandbox import ExecutionResult, execute_probe, run_tests

logger = logging.getLogger(__name__)


def extract_probe(text: str) -> str | None:
    match = re.search(r"```probe\s*\n(.*?)```", text, re.DOTALL)
    return match.group(1).strip() if match else None


def extract_code(text: str) -> str | None:
    match = re.search(r"```python\s*\n(.*?)```", text, re.DOTALL)
    return match.group(1).strip() if match else None


def bootstrap_ci(
    values: list[float], n_bootstrap: int = 1000, ci: float = 0.90, seed: int = 42
) -> tuple[float, float, float]:
    """Compute point estimate and bootstrap confidence interval."""
    rng = np.random.RandomState(seed)
    arr = np.array(values)
    point = float(arr.mean())
    boot_means = []
    for _ in range(n_bootstrap):
        sample = rng.choice(arr, size=len(arr), replace=True)
        boot_means.append(sample.mean())
    boot_means = sorted(boot_means)
    alpha = (1 - ci) / 2
    lo = float(boot_means[int(alpha * n_bootstrap)])
    hi = float(boot_means[int((1 - alpha) * n_bootstrap)])
    return point, lo, hi


def load_model(
    mode: str,
    model_name: str,
    checkpoint_path: str | None,
    bf16: bool,
) -> tuple:
    """Load model and tokenizer based on evaluation mode."""
    if mode == "base":
        logger.info(f"Loading base model: {model_name}")
        tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
        model = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype=torch.bfloat16 if bf16 else torch.float32,
            trust_remote_code=True,
            device_map="auto",
        )
    else:
        if not checkpoint_path:
            raise ValueError(f"--checkpoint-path required for mode={mode}")
        ckpt = Path(checkpoint_path)
        if not ckpt.exists():
            raise FileNotFoundError(f"Checkpoint not found: {ckpt}")

        logger.info(f"Loading checkpoint: {ckpt}")
        # Check if this is a LoRA adapter or full model
        adapter_config = ckpt / "adapter_config.json"
        if adapter_config.exists():
            tokenizer = AutoTokenizer.from_pretrained(str(ckpt), trust_remote_code=True)
            base_model = AutoModelForCausalLM.from_pretrained(
                model_name,
                torch_dtype=torch.bfloat16 if bf16 else torch.float32,
                trust_remote_code=True,
                device_map="auto",
            )
            model = PeftModel.from_pretrained(base_model, str(ckpt))
            model = model.merge_and_unload()
        else:
            tokenizer = AutoTokenizer.from_pretrained(str(ckpt), trust_remote_code=True)
            model = AutoModelForCausalLM.from_pretrained(
                str(ckpt),
                torch_dtype=torch.bfloat16 if bf16 else torch.float32,
                trust_remote_code=True,
                device_map="auto",
            )

    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    # Disable Qwen3 thinking mode
    if hasattr(tokenizer, 'chat_template') and tokenizer.chat_template and '<think>' in tokenizer.chat_template:
        tokenizer.chat_template = tokenizer.chat_template.replace(
            'enable_thinking is not defined or enable_thinking is true',
            'enable_thinking is defined and enable_thinking is true'
        )

    model.eval()
    return model, tokenizer


@torch.no_grad()
def generate_text(
    model, tokenizer, messages: list[dict], max_new_tokens: int = 1024, temperature: float = 0.0
) -> str:
    text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True, enable_thinking=False)
    inputs = tokenizer(text, return_tensors="pt").to(model.device)
    gen_kwargs = dict(
        max_new_tokens=max_new_tokens,
        do_sample=temperature > 0,
        pad_token_id=tokenizer.pad_token_id,
    )
    if temperature > 0:
        gen_kwargs["temperature"] = temperature
    output_ids = model.generate(**inputs, **gen_kwargs)
    new_ids = output_ids[0][inputs["input_ids"].shape[1]:]
    return tokenizer.decode(new_ids, skip_special_tokens=True)


def evaluate_sample(
    model, tokenizer, sample: dict, temperature: float = 0.0
) -> dict:
    """Evaluate a single sample: generate probe, execute, attempt fix."""
    # Generate probe
    prompt_text = PROBE_GENERATION_PROMPT.format(
        question=sample["question"], buggy_code=sample["buggy_code"]
    )
    messages = [
        {"role": "system", "content": PROBE_GENERATION_SYSTEM},
        {"role": "user", "content": prompt_text},
    ]
    probe_response = generate_text(model, tokenizer, messages, temperature=temperature)
    probe_code = extract_probe(probe_response)

    result = {
        "probe_generated": probe_code is not None,
        "probe_executed": False,
        "probe_diagnostic": False,
        "debug_accuracy": False,
        "probe_dependent": False,
        "probe_response": probe_response,
    }

    if probe_code is None:
        return result

    # Execute probe on buggy code (test_code drives method calls)
    test_code = sample.get("test_code")
    exec_result = execute_probe(sample["buggy_code"], probe_code, test_code=test_code, timeout=5)
    result["probe_executed"] = exec_result.success or bool(exec_result.stdout.strip())
    probe_output = exec_result.stdout if exec_result.stdout.strip() else exec_result.stderr

    # Check diagnostic value: different output on buggy vs solution
    solution_result = execute_probe(sample["solution"], probe_code, test_code=test_code, timeout=5)
    if exec_result.stdout.strip() or solution_result.stdout.strip():
        result["probe_diagnostic"] = (
            exec_result.stdout != solution_result.stdout
            or exec_result.stderr != solution_result.stderr
        )

    # Generate fix using probe output
    fix_prompt = PROBE_GENERATION_WITH_OUTPUT_PROMPT.format(
        question=sample["question"],
        buggy_code=sample["buggy_code"],
        probe_output=probe_output[:1000],
    )
    fix_messages = [
        {"role": "system", "content": PROBE_GENERATION_SYSTEM},
        {"role": "user", "content": fix_prompt},
    ]
    fix_response = generate_text(model, tokenizer, fix_messages, temperature=temperature)
    fixed_code = extract_code(fix_response)

    if fixed_code and "test_code" in sample:
        test_result = run_tests(fixed_code, sample["test_code"], timeout=10)
        result["debug_accuracy"] = test_result.passed

    # Probe dependence: fix with null output
    null_fix_prompt = PROBE_GENERATION_WITH_OUTPUT_PROMPT.format(
        question=sample["question"],
        buggy_code=sample["buggy_code"],
        probe_output="No output available",
    )
    null_messages = [
        {"role": "system", "content": PROBE_GENERATION_SYSTEM},
        {"role": "user", "content": null_fix_prompt},
    ]
    null_response = generate_text(model, tokenizer, null_messages, temperature=temperature)
    null_code = extract_code(null_response)

    null_passed = False
    if null_code and "test_code" in sample:
        null_test = run_tests(null_code, sample["test_code"], timeout=10)
        null_passed = null_test.passed

    result["probe_dependent"] = result["debug_accuracy"] != null_passed

    return result


def main():
    parser = argparse.ArgumentParser(description="Evaluate probe generation model")
    parser.add_argument("--mode", type=str, required=True, choices=["base", "sft", "grpo"])
    parser.add_argument("--model-name", type=str, default="Qwen/Qwen3-8B")
    parser.add_argument("--checkpoint-path", type=str, default=None)
    parser.add_argument("--data-path", type=str, default="data/eval.jsonl")
    parser.add_argument("--output-path", type=str, default=None)
    parser.add_argument("--temperature", type=float, default=0.0)
    parser.add_argument("--gpu", type=int, default=0)
    parser.add_argument("--bf16", action="store_true", default=True)
    parser.add_argument("--n-bootstrap", type=int, default=1000)
    parser.add_argument("--wandb-project", type=str, default="rl-active-probe-fl")
    parser.add_argument("--wandb-run-name", type=str, default=None)
    parser.add_argument("--max-samples", type=int, default=None)
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
    )

    os.environ["CUDA_VISIBLE_DEVICES"] = str(args.gpu)

    if args.output_path is None:
        args.output_path = f"results/eval_{args.mode}.json"
    Path(args.output_path).parent.mkdir(parents=True, exist_ok=True)

    # Load data
    samples = []
    with open(args.data_path) as f:
        for line in f:
            samples.append(json.loads(line))
    if args.max_samples:
        samples = samples[:args.max_samples]
    logger.info(f"Evaluating {len(samples)} samples in mode={args.mode}")

    # Load model
    model, tokenizer = load_model(args.mode, args.model_name, args.checkpoint_path, args.bf16)

    # Evaluate
    all_results = []
    for i, sample in enumerate(samples):
        logger.info(f"[{i+1}/{len(samples)}] Evaluating...")
        result = evaluate_sample(model, tokenizer, sample, temperature=args.temperature)
        all_results.append(result)

    # Aggregate metrics
    metrics = {}
    for key in ["debug_accuracy", "probe_executed", "probe_diagnostic", "probe_dependent"]:
        values = [float(r[key]) for r in all_results]
        point, lo, hi = bootstrap_ci(values, n_bootstrap=args.n_bootstrap)
        metrics[key] = {"mean": point, "ci_90_lo": lo, "ci_90_hi": hi}

    probe_gen_rate = sum(1 for r in all_results if r["probe_generated"]) / len(all_results)
    metrics["probe_generation_rate"] = probe_gen_rate

    # Print results
    print(f"\n{'='*60}")
    print(f"  Evaluation Results: {args.mode}")
    print(f"{'='*60}")
    print(f"  {'Metric':<25} {'Mean':>8} {'90% CI':>18}")
    print(f"  {'-'*25} {'-'*8} {'-'*18}")
    for key in ["debug_accuracy", "probe_executed", "probe_diagnostic", "probe_dependent"]:
        m = metrics[key]
        print(f"  {key:<25} {m['mean']:>8.3f} [{m['ci_90_lo']:.3f}, {m['ci_90_hi']:.3f}]")
    print(f"  {'probe_generation_rate':<25} {probe_gen_rate:>8.3f}")
    print(f"{'='*60}\n")

    # Save results
    output = {
        "mode": args.mode,
        "model_name": args.model_name,
        "checkpoint_path": args.checkpoint_path,
        "num_samples": len(samples),
        "metrics": metrics,
        "per_sample": all_results,
    }
    with open(args.output_path, "w") as f:
        json.dump(output, f, indent=2)
    logger.info(f"Results saved to {args.output_path}")

    # W&B logging
    if args.wandb_run_name:
        try:
            import wandb
            wandb.init(project=args.wandb_project, name=args.wandb_run_name)
            wandb.log({f"eval/{k}": v["mean"] for k, v in metrics.items() if isinstance(v, dict)})
            wandb.finish()
        except ImportError:
            logger.warning("wandb not installed, skipping logging")


if __name__ == "__main__":
    main()
