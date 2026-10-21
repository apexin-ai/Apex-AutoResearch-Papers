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

import gc

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

BATCH_SIZE = 32


def load_model_and_tokenizer(model_path: str, cache_dir: str):
    import os, json
    adapter_config_path = os.path.join(model_path, "adapter_config.json")
    if os.path.exists(adapter_config_path):
        with open(adapter_config_path) as f:
            adapter_cfg = json.load(f)
        base_model_path = adapter_cfg["base_model_name_or_path"]
        logger.info("Loading base model: %s + LoRA adapter: %s", base_model_path, model_path)
        tokenizer = AutoTokenizer.from_pretrained(
            base_model_path, cache_dir=cache_dir, trust_remote_code=True
        )
        base_model = AutoModelForCausalLM.from_pretrained(
            base_model_path, cache_dir=cache_dir,
            torch_dtype=torch.bfloat16, trust_remote_code=True,
            device_map="auto",
        )
        from peft import PeftModel
        model = PeftModel.from_pretrained(base_model, model_path)
        model = model.merge_and_unload()
    else:
        logger.info("Loading model: %s", model_path)
        tokenizer = AutoTokenizer.from_pretrained(
            model_path, cache_dir=cache_dir, trust_remote_code=True
        )
        model = AutoModelForCausalLM.from_pretrained(
            model_path, cache_dir=cache_dir,
            torch_dtype=torch.bfloat16, trust_remote_code=True,
            device_map="auto",
        )
    model.eval()
    return model, tokenizer


def _get_yes_no_token_ids(tokenizer):
    yes_variants = ["YES", "Yes", "yes", " YES", " Yes", " yes"]
    no_variants = ["NO", "No", "no", " NO", " No", " no"]
    yes_ids = set()
    for v in yes_variants:
        ids = tokenizer.encode(v, add_special_tokens=False)
        if ids:
            yes_ids.add(ids[0])
    no_ids = set()
    for v in no_variants:
        ids = tokenizer.encode(v, add_special_tokens=False)
        if ids:
            no_ids.add(ids[0])
    return list(yes_ids), list(no_ids)


def batch_generate_answers(model, tokenizer, prompts, max_new_tokens=64):
    inputs = tokenizer(prompts, return_tensors='pt', padding=True, truncation=True, max_length=2048)
    inputs = {k: v.to(model.device) for k, v in inputs.items()}

    with torch.no_grad():
        output_ids = model.generate(
            **inputs, max_new_tokens=max_new_tokens, do_sample=False,
            pad_token_id=tokenizer.pad_token_id,
        )

    input_len = inputs['input_ids'].shape[1]
    answers = []
    for i in range(len(prompts)):
        generated = tokenizer.decode(output_ids[i][input_len:], skip_special_tokens=True)
        answers.append(generated.strip())
    return answers


def batch_compute_yes_no_entropy(model, tokenizer, critique_prompts, yes_ids, no_ids):
    inputs = tokenizer(critique_prompts, return_tensors='pt', padding=True, truncation=True, max_length=2048)
    inputs = {k: v.to(model.device) for k, v in inputs.items()}

    with torch.no_grad():
        outputs = model(**inputs)

    logits = outputs.logits[:, -1, :]
    log_probs = torch.log_softmax(logits.float(), dim=-1)

    results = []
    for i in range(len(critique_prompts)):
        item_lp = log_probs[i]

        yes_lp = max(item_lp[tid].item() for tid in yes_ids) if yes_ids else float("-inf")
        no_lp = max(item_lp[tid].item() for tid in no_ids) if no_ids else float("-inf")

        max_lp = max(yes_lp, no_lp)
        yes_p = math.exp(yes_lp - max_lp)
        no_p = math.exp(no_lp - max_lp)
        total = yes_p + no_p

        if total < 1e-10:
            results.append({"entropy": 0.0, "yes_prob": 0.5, "no_prob": 0.5})
            continue

        yes_p /= total
        no_p /= total

        entropy = 0.0
        if yes_p > 1e-10:
            entropy -= yes_p * math.log2(yes_p)
        if no_p > 1e-10:
            entropy -= no_p * math.log2(no_p)

        results.append({"entropy": entropy, "yes_prob": yes_p, "no_prob": no_p})

    return results


def format_question_prompt(row: dict, benchmark: str) -> str:
    """Format benchmark item as a question prompt for model answer generation."""
    if benchmark == "mmlu":
        choices = "\n".join(f"{chr(65+i)}) {c}" for i, c in enumerate(row["choices"]))
        return f"Question: {row['question']}\n{choices}\nAnswer:"
    elif benchmark == "gsm8k":
        return f"Question: {row['question']}\nAnswer: Let's think step by step.\n"
    elif benchmark == "arc_challenge":
        choices = "\n".join(f"{l}) {t}" for l, t in zip(row["choices"]["label"], row["choices"]["text"]))
        return f"Question: {row['question']}\n{choices}\nAnswer:"
    elif benchmark == "humaneval":
        return row["prompt"]
    else:
        raise ValueError(f"Unknown benchmark: {benchmark}")


def format_question_text(row: dict, benchmark: str) -> str:
    """Short text version of the question for the critique prompt."""
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
    max_answer_tokens: int = 64,
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

    model, tokenizer = load_model_and_tokenizer(model_path, cache_dir)

    tokenizer.pad_token = tokenizer.eos_token
    tokenizer.padding_side = 'left'

    yes_ids, no_ids = _get_yes_no_token_ids(tokenizer)

    items = list(ds)
    results = []
    for batch_start in tqdm(range(0, len(items), BATCH_SIZE), desc=f"Self-critique {benchmark}"):
        batch_items = items[batch_start:batch_start + BATCH_SIZE]

        q_prompts = [format_question_prompt(row, benchmark) for row in batch_items]
        answers = batch_generate_answers(model, tokenizer, q_prompts, max_answer_tokens)

        critique_prompts = []
        for row, answer in zip(batch_items, answers):
            question_text = format_question_text(row, benchmark)
            critique_prompt = CRITIQUE_TEMPLATE.format(
                answer=answer[:500], question=question_text[:500]
            )
            critique_prompts.append(critique_prompt)

        ent_datas = batch_compute_yes_no_entropy(model, tokenizer, critique_prompts, yes_ids, no_ids)

        for j, ent_data in enumerate(ent_datas):
            results.append({
                "index": batch_start + j,
                "benchmark": benchmark,
                "s4_selfcritique": -ent_data["entropy"],
                "s4_entropy": ent_data["entropy"],
                "s4_yes_prob": ent_data["yes_prob"],
                "s4_no_prob": ent_data["no_prob"],
            })

    del model, tokenizer
    gc.collect()
    torch.cuda.empty_cache()
    logger.info("Freed self-critique model GPU memory")

    return results


def main():
    parser = argparse.ArgumentParser(description="Signal 4: Self-Critique entropy collapse")
    parser.add_argument("--benchmark", type=str, required=True,
                        choices=["mmlu", "gsm8k", "arc_challenge", "humaneval"])
    parser.add_argument("--model-path", type=str, required=True,
                        help="Target model path")
    parser.add_argument("--output-dir", type=str, required=True)
    parser.add_argument("--max-answer-tokens", type=int, default=64)
    parser.add_argument("--gpu", type=str, default=None)
    parser.add_argument("--cache-dir", type=str, default="/root/autodl-tmp/.hf_cache")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

    if args.gpu:
        os.environ["CUDA_VISIBLE_DEVICES"] = args.gpu

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    results = compute_selfcritique_signal(
        benchmark=args.benchmark,
        model_path=args.model_path,
        cache_dir=args.cache_dir,
        max_answer_tokens=args.max_answer_tokens,
    )

    out_file = output_dir / f"signal_selfcritique_{args.benchmark}.json"
    with open(out_file, "w") as f:
        json.dump(results, f, indent=2)
    logger.info("Saved %d items to %s", len(results), out_file)


if __name__ == "__main__":
    main()
