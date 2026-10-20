"""
GSM8K Test Set Evaluation.

Evaluates model accuracy on GSM8K test split by generating reasoning traces
and comparing extracted numeric answers against gold answers.

Input:  model path
Output: accuracy printed to stdout + saved to results JSON
"""

import argparse
import json
import logging
import os
import random
import re

import numpy as np
import torch
from datasets import load_dataset
from transformers import AutoModelForCausalLM, AutoTokenizer
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


def extract_answer(text: str) -> str | None:
    """Extract numeric answer from model output."""
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
    except ValueError:
        return ans


def extract_gold_answer(answer_text: str) -> str:
    match = re.search(r"####\s*(.+)", answer_text)
    if match:
        return normalize_answer(match.group(1))
    return answer_text.strip()


def evaluate(model, tokenizer, dataset, max_new_tokens: int = 512, batch_size: int = 1):
    """Run evaluation and return accuracy + per-example results."""
    model.eval()
    device = next(model.parameters()).device

    correct = 0
    total = 0
    results = []

    for i in tqdm(range(0, len(dataset), batch_size), desc="Evaluating"):
        batch = dataset[i : i + batch_size]
        questions = batch["question"] if isinstance(batch["question"], list) else [batch["question"]]
        answers = batch["answer"] if isinstance(batch["answer"], list) else [batch["answer"]]

        for q, a in zip(questions, answers):
            prompt = (
                f"Solve the following math problem step by step. "
                f"Put your final answer in \\boxed{{}}.\n\n"
                f"Question: {q}\n\nAnswer:"
            )

            inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=1024).to(device)

            with torch.no_grad():
                output_ids = model.generate(
                    **inputs,
                    max_new_tokens=max_new_tokens,
                    temperature=0.0,
                    do_sample=False,
                    pad_token_id=tokenizer.pad_token_id or tokenizer.eos_token_id,
                )

            generated = output_ids[0][inputs["input_ids"].shape[1] :]
            response = tokenizer.decode(generated, skip_special_tokens=True)

            pred = extract_answer(response)
            gold = extract_gold_answer(a)

            is_correct = False
            if pred is not None:
                is_correct = normalize_answer(pred) == gold

            if is_correct:
                correct += 1
            total += 1

            results.append({
                "question": q,
                "gold": gold,
                "prediction": pred,
                "correct": is_correct,
                "response": response[:500],  # truncate for storage
            })

            if total % 100 == 0:
                logger.info(f"Progress: {total}/{len(dataset)}, running accuracy: {correct/total:.4f}")

    accuracy = correct / total if total > 0 else 0.0
    return accuracy, results


def main():
    parser = argparse.ArgumentParser(description="Evaluate model on GSM8K test set")
    parser.add_argument("--model_path", type=str, required=True, help="Path to model")
    parser.add_argument("--output_path", type=str, default=None, help="Output JSON path for results")
    parser.add_argument("--max_new_tokens", type=int, default=512)
    parser.add_argument("--max_samples", type=int, default=None, help="Limit test samples (None=all)")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--dtype", type=str, default="bfloat16", choices=["float16", "bfloat16", "float32"])
    args = parser.parse_args()

    set_seed(args.seed)

    logger.info(f"Loading model from {args.model_path}")
    tokenizer = AutoTokenizer.from_pretrained(args.model_path, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    dtype_map = {"float16": torch.float16, "bfloat16": torch.bfloat16, "float32": torch.float32}
    torch_dtype = dtype_map[args.dtype]

    model = AutoModelForCausalLM.from_pretrained(
        args.model_path,
        torch_dtype=torch_dtype,
        device_map="auto",
        trust_remote_code=True,
    )

    logger.info("Loading GSM8K test set...")
    dataset = load_dataset("openai/gsm8k", "main", split="test")
    if args.max_samples is not None:
        dataset = dataset.shuffle(seed=args.seed).select(range(min(args.max_samples, len(dataset))))
    logger.info(f"Evaluating on {len(dataset)} test samples")

    accuracy, results = evaluate(model, tokenizer, dataset, max_new_tokens=args.max_new_tokens)

    logger.info(f"GSM8K Accuracy: {accuracy:.4f} ({int(accuracy * len(dataset))}/{len(dataset)})")

    # Determine output path
    if args.output_path is None:
        model_name = os.path.basename(args.model_path.rstrip("/"))
        args.output_path = f"results/eval_{model_name}.json"

    os.makedirs(os.path.dirname(args.output_path) or ".", exist_ok=True)
    output = {
        "model_path": args.model_path,
        "accuracy": accuracy,
        "n_correct": int(accuracy * len(dataset)),
        "n_total": len(dataset),
        "examples": results,
    }
    with open(args.output_path, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    logger.info(f"Results saved to {args.output_path}")


if __name__ == "__main__":
    main()
