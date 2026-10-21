import logging
import math

import numpy as np
import torch
from tqdm import tqdm

logger = logging.getLogger(__name__)

CRITIQUE_TEMPLATE = (
    "Is the following answer correct? "
    "Answer: {answer}. "
    "Question: {question}. "
    "Explain briefly then conclude with YES or NO."
)

BATCH_SIZE = 32


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


def _batch_generate_answers(model, tokenizer, prompts, max_new_tokens=64):
    inputs = tokenizer(prompts, return_tensors="pt", padding=True, truncation=True, max_length=2048)
    inputs = {k: v.to(model.device) for k, v in inputs.items()}

    with torch.no_grad():
        output_ids = model.generate(
            **inputs, max_new_tokens=max_new_tokens, do_sample=False,
            pad_token_id=tokenizer.pad_token_id,
        )

    input_len = inputs["input_ids"].shape[1]
    answers = []
    for i in range(len(prompts)):
        generated = tokenizer.decode(output_ids[i][input_len:], skip_special_tokens=True)
        answers.append(generated.strip())
    return answers


def _batch_compute_yes_no_entropy(model, tokenizer, critique_prompts, yes_ids, no_ids):
    inputs = tokenizer(critique_prompts, return_tensors="pt", padding=True, truncation=True, max_length=2048)
    inputs = {k: v.to(model.device) for k, v in inputs.items()}

    with torch.no_grad():
        outputs = model(**inputs)

    logits = outputs.logits[:, -1, :]
    log_probs = torch.log_softmax(logits.float(), dim=-1)

    results = []
    for i in range(len(critique_prompts)):
        item_lp = log_probs[i]

        yes_lp = max(item_lp[tid].item() for tid in yes_ids) if yes_ids else -100.0
        no_lp = max(item_lp[tid].item() for tid in no_ids) if no_ids else -100.0

        max_lp = max(yes_lp, no_lp)
        yes_p = math.exp(yes_lp - max_lp)
        no_p = math.exp(no_lp - max_lp)
        total = yes_p + no_p
        yes_p /= total
        no_p /= total

        entropy = 0.0
        if yes_p > 0:
            entropy -= yes_p * math.log2(yes_p)
        if no_p > 0:
            entropy -= no_p * math.log2(no_p)

        results.append({
            "entropy": entropy,
            "yes_prob": yes_p,
            "no_prob": no_p,
        })

    return results


def compute(
    benchmark: str,
    model_path: str,
    adapter_path: str = None,
    output_dir: str = None,
    cache_dir: str = None,
    batch_size: int = 32,
    **kwargs,
) -> list[dict]:
    from utils import (
        load_model_and_tokenizer, load_benchmark_dataset,
        format_question_text, make_item_id,
    )

    cache_dir = cache_dir or "/root/autodl-tmp/.hf_cache"

    ds = load_benchmark_dataset(benchmark, cache_dir)
    model, tokenizer = load_model_and_tokenizer(model_path, adapter_path, cache_dir)

    tokenizer.pad_token = tokenizer.eos_token
    tokenizer.padding_side = "left"

    yes_ids, no_ids = _get_yes_no_token_ids(tokenizer)

    items = list(ds)
    results = []
    # mmlu has 14k items; generate() + forward pass OOMs 3B models at bs>=8
    if len(items) > 5000:
        bs = min(batch_size, 2)
    elif len(items) > 2000:
        bs = min(batch_size, 8)
    else:
        bs = min(batch_size, BATCH_SIZE)
    logger.info("Self-critique %s: %d items, batch_size=%d", benchmark, len(items), bs)

    for batch_start in tqdm(range(0, len(items), bs), desc=f"Self-critique {benchmark}"):
        batch_items = items[batch_start:batch_start + bs]

        q_prompts = [format_question_text(row, benchmark) for row in batch_items]
        answers = _batch_generate_answers(model, tokenizer, q_prompts)

        critique_prompts = []
        for row, answer in zip(batch_items, answers):
            question_text = format_question_text(row, benchmark)
            critique_prompts.append(CRITIQUE_TEMPLATE.format(
                answer=answer[:500], question=question_text[:500]
            ))

        ent_datas = _batch_compute_yes_no_entropy(model, tokenizer, critique_prompts, yes_ids, no_ids)

        for j, ent_data in enumerate(ent_datas):
            results.append({
                "item_id": make_item_id(benchmark, batch_start + j),
                "signal": "s4_selfcritique",
                "score": -ent_data["entropy"],  # negate: low entropy -> high contamination suspicion
                "metadata": {
                    "entropy": ent_data["entropy"],
                    "yes_prob": ent_data["yes_prob"],
                    "no_prob": ent_data["no_prob"],
                },
            })

    return results
