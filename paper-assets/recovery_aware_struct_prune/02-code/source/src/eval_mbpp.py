"""MBPP (Mostly Basic Python Problems) Evaluation.

Evaluates code generation models on MBPP sanitized subset (374 tasks).
Uses sandbox execution to verify generated code against test cases.
"""

import argparse
from datetime import datetime
import json
import logging
import math
import os
import random
import re
import sys
import subprocess
import tempfile

import numpy as np
import torch
from datasets import load_dataset
from transformers import AutoTokenizer
from model_utils import load_pruned_model
from tqdm import tqdm

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)


def set_seed(seed):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)


def extract_code_block(text):
    """Extract Python code from model response, handling markdown fences and think tags."""
    clean = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL)
    if not clean.strip():
        clean = text
    code_blocks = re.findall(r"```python\s*\n(.*?)```", clean, re.DOTALL)
    if code_blocks:
        return code_blocks[0]
    code_blocks = re.findall(r"```\s*\n(.*?)```", clean, re.DOTALL)
    if code_blocks:
        return code_blocks[0]
    return clean


def run_test(code, test_list, test_setup_code="", timeout=10):
    """Execute generated code against MBPP test cases in a subprocess sandbox.

    Concatenates setup code, generated code, and assert statements,
    then runs in an isolated subprocess with timeout enforcement.
    """
    parts = []
    if test_setup_code:
        parts.append(test_setup_code)
    parts.append(code)
    parts.extend(test_list)
    full_code = "\n".join(parts)

    with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as f:
        f.write(full_code)
        tmp_path = f.name
    try:
        result = subprocess.run(
            [sys.executable, tmp_path],
            capture_output=True, text=True, timeout=timeout,
        )
        return result.returncode == 0, result.stderr[:500] if result.stderr else ""
    except subprocess.TimeoutExpired:
        return False, "Timeout"
    except Exception as e:
        return False, str(e)[:500]
    finally:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass


def main():
    parser = argparse.ArgumentParser(description="MBPP pass@1 evaluation")
    parser.add_argument("--model_path", type=str, required=True)
    parser.add_argument("--output_path", type=str, default=None)
    parser.add_argument("--max_new_tokens", type=int, default=2048)
    parser.add_argument("--max_samples", type=int, default=None)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--dtype", type=str, default="bfloat16")
    parser.add_argument("--timeout", type=int, default=10)
    args = parser.parse_args()

    set_seed(args.seed)

    logger.info(f"Loading model from {args.model_path}")
    tokenizer = AutoTokenizer.from_pretrained(args.model_path, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    dtype_map = {"float16": torch.float16, "bfloat16": torch.bfloat16, "float32": torch.float32}
    model = load_pruned_model(args.model_path, device_map="auto", torch_dtype=dtype_map[args.dtype])
    model.eval()
    device = next(model.parameters()).device

    logger.info("Loading MBPP dataset (sanitized, 374 tasks)...")
    dataset = load_dataset("mbpp", split="train")
    logger.info(f"Loaded {len(dataset)} problems")

    if args.max_samples is not None:
        dataset = dataset.select(range(min(args.max_samples, len(dataset))))

    correct = 0
    total = 0
    results = []
    response_lengths = []
    eos_token_id = tokenizer.eos_token_id

    for idx in tqdm(range(len(dataset)), desc="MBPP"):
        item = dataset[idx]
        task_id = item["task_id"]
        text = item["text"]
        test_list = item["test_list"]
        test_setup_code = item.get("test_setup_code", "")

        test_examples = "\n".join(test_list[:3])
        user_msg = (
            f"Write a Python function to solve the following task. "
            f"Only output the complete function, no explanation.\n\n"
            f"Task: {text}\n\n"
            f"Test cases for reference:\n{test_examples}"
        )
        messages = [{"role": "user", "content": user_msg}]
        prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=2048).to(device)

        with torch.no_grad():
            output_ids = model.generate(
                **inputs,
                max_new_tokens=args.max_new_tokens,
                do_sample=False,
                pad_token_id=tokenizer.pad_token_id or eos_token_id,
            )

        gen_ids = output_ids[0, inputs["input_ids"].shape[1]:]
        response = tokenizer.decode(gen_ids, skip_special_tokens=True)
        resp_len = len(gen_ids)
        response_lengths.append(resp_len)

        code = extract_code_block(response)

        passed, error = run_test(code, test_list, test_setup_code, timeout=args.timeout)
        if passed:
            correct += 1
        total += 1

        results.append({
            "task_id": task_id,
            "passed": passed,
            "error": error if not passed else "",
            "response_length": resp_len,
        })

        if (idx + 1) % 20 == 0:
            logger.info(f"Progress: {idx+1}/{len(dataset)}, Pass@1: {correct/total:.4f}")

    accuracy = correct / total if total > 0 else 0
    stderr = math.sqrt(accuracy * (1 - accuracy) / total) if total > 0 else 0

    logger.info(f"MBPP pass@1: {accuracy:.4f} +/- {stderr:.4f} ({correct}/{total})")

    eos_stats = {
        "avg_response_length": float(np.mean(response_lengths)) if response_lengths else 0,
        "median_response_length": float(np.median(response_lengths)) if response_lengths else 0,
    }

    if args.output_path is None:
        model_name = os.path.basename(args.model_path.rstrip("/"))
        args.output_path = f"results/eval_mbpp_{model_name}.json"

    os.makedirs(os.path.dirname(args.output_path) or ".", exist_ok=True)
    output = {
        "model_path": args.model_path,
        "benchmark": "MBPP",
        "pass_at_1": accuracy,
        "stderr": stderr,
        "n_correct": correct,
        "n_total": total,
        "eos_stats": eos_stats,
        "examples": results,
    }

    with open(args.output_path, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    logger.info(f"Results saved to {args.output_path}")

    sentinel_path = args.output_path + ".done"
    with open(sentinel_path, "w") as f:
        f.write(f"completed_at={datetime.now().isoformat()}\n")
        f.write(f"pass_at_1={accuracy:.4f}\n")
        f.write(f"n_correct={correct}\n")
        f.write(f"n_total={total}\n")
    logger.info(f"Sentinel written: {sentinel_path}")


if __name__ == "__main__":
    main()
