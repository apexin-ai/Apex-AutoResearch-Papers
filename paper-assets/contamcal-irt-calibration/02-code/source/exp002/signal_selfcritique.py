"""
Signal 4: Self-Critique entropy collapse.

Lets the model evaluate whether its own answer to a benchmark item is correct.
Computes entropy of the YES/NO log-prob distribution. Low entropy (high
certainty) indicates possible memorization.

Input:  Target model, benchmark items + model's answers
Output: JSON with per-item negative entropy scores
"""

import argparse
import json
import logging
import math
import os
from pathlib import Path

import numpy as np
import torch
from tqdm import tqdm
from transformers import AutoModelForCausalLM, AutoTokenizer

logger = logging.getLogger(__name__)

HF_HOME = os.environ.get("HF_HOME", "/root/autodl-tmp/.hf_cache")
os.environ["HF_HOME"] = HF_HOME

CRITIQUE_TEMPLATE = (
    "Is the following answer correct? "
    "Answer: {answer}. "
    "Question: {question}. "
    "Explain briefly then conclude with YES or NO."
)


def _resolve_adapter_path(adapter_path: str) -> str:
    """Resolve adapter path: check for lora_adapter/ subdirectory."""
    if adapter_path is None:
        return None
    p = Path(adapter_path)
    if (p / "adapter_config.json").exists():
        return str(p)
    lora_sub = p / "lora_adapter"
    if (lora_sub / "adapter_config.json").exists():
        return str(lora_sub)
    return str(p)


def load_model_and_tokenizer(model_path: str, cache_dir: str, adapter_path: str = None):
    adapter_path = _resolve_adapter_path(adapter_path)

    logger.info("Loading model: %s", model_path)
    tokenizer = AutoTokenizer.from_pretrained(
        model_path, cache_dir=cache_dir, trust_remote_code=True
    )
    model = AutoModelForCausalLM.from_pretrained(
        model_path, cache_dir=cache_dir,
        torch_dtype=torch.bfloat16, trust_remote_code=True,
        device_map="auto",
    )
    if adapter_path:
        from peft import PeftModel
        logger.info("Loading LoRA adapter from %s", adapter_path)
        model = PeftModel.from_pretrained(model, adapter_path)
        model = model.merge_and_unload()
        logger.info("LoRA adapter merged into base model")
    model.eval()
    return model, tokenizer


def get_model_answer(model, tokenizer, prompt: str, max_new_tokens: int = 256) -> str:
    """Generate model's answer to a benchmark item."""
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=2048)
    inputs = {k: v.to(model.device) for k, v in inputs.items()}

    with torch.no_grad():
        output_ids = model.generate(
            **inputs, max_new_tokens=max_new_tokens, do_sample=False,
            pad_token_id=tokenizer.pad_token_id or tokenizer.eos_token_id,
        )
    generated = tokenizer.decode(output_ids[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True)
    return generated.strip()


def compute_yes_no_entropy(model, tokenizer, critique_prompt: str) -> dict:
    """Compute entropy of YES/NO log-prob distribution for the critique prompt."""
    inputs = tokenizer(critique_prompt, return_tensors="pt", truncation=True, max_length=2048)
    inputs = {k: v.to(model.device) for k, v in inputs.items()}

    with torch.no_grad():
        outputs = model(**inputs)
    logits = outputs.logits[0, -1, :]
    log_probs = torch.log_softmax(logits, dim=-1)

    # Get log-probs for YES and NO tokens (try multiple tokenizations)
    yes_variants = ["YES", "Yes", "yes", " YES", " Yes", " yes"]
    no_variants = ["NO", "No", "no", " NO", " No", " no"]

    def best_logprob(variants):
        best = float("-inf")
        for v in variants:
            ids = tokenizer.encode(v, add_special_tokens=False)
            if ids:
                lp = log_probs[ids[0]].item()
                best = max(best, lp)
        return best

    yes_lp = best_logprob(yes_variants)
    no_lp = best_logprob(no_variants)

    # Normalize to binary distribution
    max_lp = max(yes_lp, no_lp)
    yes_p = math.exp(yes_lp - max_lp)
    no_p = math.exp(no_lp - max_lp)
    total = yes_p + no_p

    if total < 1e-10:
        return {"entropy": 0.0, "yes_prob": 0.5, "no_prob": 0.5}

    yes_p /= total
    no_p /= total

    # Binary entropy
    entropy = 0.0
    if yes_p > 1e-10:
        entropy -= yes_p * math.log2(yes_p)
    if no_p > 1e-10:
        entropy -= no_p * math.log2(no_p)

    return {"entropy": entropy, "yes_prob": yes_p, "no_prob": no_p}


def format_question_prompt(row: dict, benchmark: str) -> str:
    """Format benchmark item as a question prompt for model answer generation."""
    if benchmark == "mmlu":
        choices = "\n".join(f"{chr(65+i)}) {c}" for i, c in enumerate(row["choices"]))
        return f"Question: {row['question']}\n{choices}\nAnswer:"
    elif benchmark == "gsm8k":
        return f"Question: {row['question']}\nAnswer:"
    elif benchmark == "arc_challenge":
        choices = "\n".join(f"{l}) {t}" for l, t in zip(row["choices"]["label"], row["choices"]["text"]))
        return f"Question: {row['question']}\n{choices}\nAnswer:"
    elif benchmark == "humaneval":
        return row["prompt"]
    else:
        raise ValueError(f"Unknown benchmark: {benchmark}")


def format_question_text(row: dict, benchmark: str) -> str:
    """Extract question text for the critique prompt."""
    if benchmark == "mmlu":
        return row["question"]
    elif benchmark == "gsm8k":
        return row["question"]
    elif benchmark == "arc_challenge":
        return row["question"]
    elif benchmark == "humaneval":
        return row["prompt"][:200]
    else:
        raise ValueError(f"Unknown benchmark: {benchmark}")


def compute_selfcritique_signal(
    benchmark: str,
    model_path: str,
    cache_dir: str,
    adapter_path: str = None,
    max_answer_tokens: int = 256,
    max_items: int = None,
) -> list[dict]:
    """Compute self-critique entropy for all items in a benchmark."""
    from datasets import load_dataset

    if benchmark == "mmlu":
        ds = load_dataset("cais/mmlu", "all", split="test", cache_dir=cache_dir)
    elif benchmark == "gsm8k":
        ds = load_dataset("openai/gsm8k", "main", split="test", cache_dir=cache_dir)
    elif benchmark == "arc_challenge":
        ds = load_dataset("allenai/ai2_arc", "ARC-Challenge", split="test", cache_dir=cache_dir)
    elif benchmark == "humaneval":
        ds = load_dataset("openai/openai_humaneval", "openai_humaneval", split="test", cache_dir=cache_dir)
    else:
        raise ValueError(f"Unknown benchmark: {benchmark}")

    if max_items:
        ds = ds.select(range(min(max_items, len(ds))))

    model, tokenizer = load_model_and_tokenizer(model_path, cache_dir, adapter_path=adapter_path)

    results = []
    for i, row in enumerate(tqdm(ds, desc=f"Self-critique {benchmark}")):
        # Step 1: Get model's answer
        q_prompt = format_question_prompt(row, benchmark)
        answer = get_model_answer(model, tokenizer, q_prompt, max_answer_tokens)

        # Step 2: Build critique prompt
        question_text = format_question_text(row, benchmark)
        critique_prompt = CRITIQUE_TEMPLATE.format(
            answer=answer[:500], question=question_text[:500]
        )

        # Step 3: Compute YES/NO entropy
        ent_data = compute_yes_no_entropy(model, tokenizer, critique_prompt)

        # Negative entropy: higher = more certain = more suspicious
        results.append({
            "index": i,
            "benchmark": benchmark,
            "s4_selfcritique": -ent_data["entropy"],
            "s4_entropy": ent_data["entropy"],
            "s4_yes_prob": ent_data["yes_prob"],
            "s4_no_prob": ent_data["no_prob"],
        })

    return results


def main():
    parser = argparse.ArgumentParser(description="Signal 4: Self-Critique entropy collapse")
    parser.add_argument("--benchmark", type=str, required=True,
                        choices=["mmlu", "gsm8k", "arc_challenge", "humaneval"])
    parser.add_argument("--model-path", type=str, required=True,
                        help="Target model path")
    parser.add_argument("--adapter-path", type=str, default=None,
                        help="Path to LoRA adapter directory for target model")
    parser.add_argument("--output-dir", type=str, required=True)
    parser.add_argument("--max-answer-tokens", type=int, default=256)
    parser.add_argument("--gpu", type=str, default=None)
    parser.add_argument("--cache-dir", type=str, default="/root/autodl-tmp/.hf_cache")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    results = compute_selfcritique_signal(
        benchmark=args.benchmark,
        model_path=args.model_path,
        cache_dir=args.cache_dir,
        adapter_path=args.adapter_path,
        max_answer_tokens=args.max_answer_tokens,
    )

    out_file = output_dir / f"signal_selfcritique_{args.benchmark}.json"
    with open(out_file, "w") as f:
        json.dump(results, f, indent=2)
    logger.info("Saved %d items to %s", len(results), out_file)


if __name__ == "__main__":
    main()
