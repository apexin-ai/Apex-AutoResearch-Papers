"""
MATH-500 Evaluation.

Evaluates model accuracy on the HuggingFaceH4/MATH-500 subset (500 problems)
by generating reasoning traces and comparing extracted answers against gold.
"""

import argparse
import json
import logging
import math
import os
import random
import re

import numpy as np
import torch
from datasets import load_dataset
from transformers import AutoTokenizer
from model_utils import load_pruned_model
from tqdm import tqdm

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger(__name__)


def set_seed(seed: int):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)


def _extract_boxed(text: str) -> str | None:
    idx = text.rfind("\\boxed{")
    if idx == -1:
        return None
    depth = 0
    start = idx + len("\\boxed{")
    for i in range(start, len(text)):
        if text[i] == "{":
            depth += 1
        elif text[i] == "}":
            if depth == 0:
                return text[start:i]
            depth -= 1
    return None


def normalize_answer(ans: str) -> str:
    if ans is None:
        return ""
    ans = ans.strip()
    ans = ans.rstrip(".")
    ans = re.sub(r"\\text\{([^}]*)\}", r"\1", ans)
    ans = re.sub(r"\\(mathrm|mathbf|textbf|operatorname)\{([^}]*)\}", r"\2", ans)
    ans = re.sub(r"\\(left|right|displaystyle)", "", ans)
    ans = ans.replace("\\!", "").replace("\\,", "").replace("\\;", "").replace("\\ ", "")
    ans = ans.replace("\\$", "").replace("$", "")
    ans = ans.replace("\\%", "%")
    ans = re.sub(r"\\dfrac", r"\\frac", ans)
    ans = re.sub(r"\\tfrac", r"\\frac", ans)
    ans = ans.replace("{", "").replace("}", "")
    ans = re.sub(r"\\(sin|cos|tan|cot|sec|csc|log|ln|exp|sqrt)", r"\1", ans)
    ans = re.sub(r",\s+", ",", ans)
    ans = re.sub(r"\(\s+", "(", ans)
    ans = re.sub(r"\s+\)", ")", ans)
    ans = re.sub(r"(\w)\s*([+-])\s*(\w)", r"\1\2\3", ans)
    ans = re.sub(r"\s+", " ", ans).strip()
    ans = ans.lower()
    if re.match(r'^\([a-zA-Z0-9]\)$', ans):
        ans = ans[1:-1]
    return ans


def extract_model_answer(text: str) -> str | None:
    clean = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL)
    if not clean.strip():
        clean = text

    boxed = _extract_boxed(clean)
    if boxed is not None:
        return boxed

    patterns = [
        r"[Tt]he (?:\w+ )?answer is[:\s]*\$?(.+?)\$?\s*(?:\.|$)",
        r"\b[Aa]nswer\s*(?:is|:)\s*\$?(.+?)\$?\s*(?:\.|$)",
        r"\$\\boxed\{(.+?)\}\$",
    ]
    for pat in patterns:
        m = re.search(pat, clean, re.MULTILINE)
        if m:
            return m.group(1).strip()

    if clean != text:
        boxed_full = _extract_boxed(text)
        if boxed_full is not None:
            return boxed_full
        for pat in patterns:
            matches = re.findall(pat, text, re.MULTILINE)
            if matches:
                return matches[-1].strip()

    numbers = re.findall(r"-?\d+(?:,\d{3})*(?:\.\d+)?(?:/\d+)?", clean)
    if numbers:
        return numbers[-1].replace(",", "")
    return None


def answers_match(pred: str | None, gold: str) -> bool:
    if pred is None:
        return False
    pred_n = normalize_answer(pred)
    gold_n = normalize_answer(gold)
    if not pred_n:
        return False
    if pred_n == gold_n:
        return True
    try:
        def eval_numeric(s):
            s = s.replace("\\frac", "").replace("\\pi", str(math.pi))
            s = re.sub(r"(\d+)\s*(\d+)/(\d+)", lambda m: str(int(m.group(1)) + int(m.group(2))/int(m.group(3))), s)
            s = re.sub(r"(\d+)/(\d+)", lambda m: str(int(m.group(1))/int(m.group(2))), s)
            s = s.replace(",", "").strip()
            return float(s)
        pv = eval_numeric(pred_n)
        gv = eval_numeric(gold_n)
        return abs(pv - gv) < 1e-5
    except (ValueError, OverflowError, ZeroDivisionError):
        pass
    return False


def binomial_stderr(p: float, n: int) -> float:
    if n == 0:
        return 0.0
    return math.sqrt(p * (1 - p) / n)


def evaluate(model, tokenizer, dataset, max_new_tokens: int = 4096):
    model.eval()
    device = next(model.parameters()).device
    correct = 0
    total = 0
    results = []
    n_natural_eos = 0
    n_truncated = 0
    response_lengths = []

    for item in tqdm(dataset, desc="MATH-500 eval"):
        problem = item["problem"]
        gold_answer = item["answer"]

        messages = [{"role": "user", "content": problem}]
        prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        inputs = tokenizer(prompt, return_tensors="pt").to(device)

        with torch.no_grad():
            outputs = model.generate(
                **inputs,
                max_new_tokens=max_new_tokens,
                do_sample=False,
                pad_token_id=tokenizer.pad_token_id or tokenizer.eos_token_id,
            )

        response_ids = outputs[0][inputs["input_ids"].shape[1]:]
        response = tokenizer.decode(response_ids, skip_special_tokens=True)
        response_lengths.append(len(response_ids))

        if len(response_ids) > 0 and response_ids[-1].item() == tokenizer.eos_token_id:
            n_natural_eos += 1
        else:
            n_truncated += 1

        pred_answer = extract_model_answer(response)
        is_correct = answers_match(pred_answer, gold_answer)
        if is_correct:
            correct += 1
        total += 1

        results.append({
            "problem": problem[:200],
            "gold_answer": gold_answer,
            "pred_answer": pred_answer,
            "correct": is_correct,
            "response_length": len(response_ids),
        })

    accuracy = correct / total if total > 0 else 0.0
    stderr = binomial_stderr(accuracy, total)
    eos_stats = {
        "natural_eos": n_natural_eos,
        "truncated": n_truncated,
        "avg_response_length": float(np.mean(response_lengths)) if response_lengths else 0,
    }
    return accuracy, correct, total, results, eos_stats, stderr


def main():
    parser = argparse.ArgumentParser(description="MATH-500 Evaluation")
    parser.add_argument("--model_path", type=str, required=True)
    parser.add_argument("--output_path", type=str, default=None)
    parser.add_argument("--max_new_tokens", type=int, default=4096)
    parser.add_argument("--max_samples", type=int, default=None)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--dtype", type=str, default="bfloat16", choices=["float16", "bfloat16", "float32"])
    parser.add_argument("--device_map", type=str, default="auto")
    args = parser.parse_args()

    set_seed(args.seed)

    logger.info(f"Loading model from {args.model_path}")
    tokenizer = AutoTokenizer.from_pretrained(args.model_path, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    dtype_map = {"float16": torch.float16, "bfloat16": torch.bfloat16, "float32": torch.float32}
    torch_dtype = dtype_map[args.dtype]
    model = load_pruned_model(args.model_path, device_map=args.device_map, torch_dtype=torch_dtype)

    logger.info("Loading MATH-500 dataset...")
    dataset = load_dataset("HuggingFaceH4/MATH-500", split="test")
    logger.info(f"Loaded {len(dataset)} problems")

    if args.max_samples is not None:
        dataset = dataset.shuffle(seed=args.seed).select(range(min(args.max_samples, len(dataset))))
    logger.info(f"Evaluating on {len(dataset)} problems")

    accuracy, n_correct, n_total, results, eos_stats, stderr = evaluate(
        model, tokenizer, dataset, max_new_tokens=args.max_new_tokens
    )

    logger.info(f"MATH-500 Accuracy: {accuracy:.4f} +/- {stderr:.4f} ({n_correct}/{n_total})")
    logger.info(f"EOS Stats: {json.dumps(eos_stats, indent=2)}")

    if args.output_path is None:
        model_name = os.path.basename(args.model_path.rstrip("/"))
        args.output_path = f"results/eval_math500_{model_name}.json"

    os.makedirs(os.path.dirname(args.output_path) or ".", exist_ok=True)
    output = {
        "model_path": args.model_path,
        "benchmark": "MATH-500",
        "accuracy": accuracy,
        "stderr": stderr,
        "n_correct": n_correct,
        "n_total": n_total,
        "eos_stats": eos_stats,
        "examples": results,
    }
    with open(args.output_path, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    logger.info(f"Results saved to {args.output_path}")


if __name__ == "__main__":
    main()
