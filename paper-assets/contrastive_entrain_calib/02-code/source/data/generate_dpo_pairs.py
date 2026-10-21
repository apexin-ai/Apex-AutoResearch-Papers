#!/usr/bin/env python3
"""Generate DPO training data via best-of-N rejection sampling.

For each training prompt, generate N completions from the base model,
score them by ground-truth agreement (NLI + heuristic), then select
best as chosen and worst as rejected.

Usage:
  python generate_dpo_pairs.py [--n-samples 8] [--output dpo_train.jsonl]
"""

import argparse
import json
import logging
import os
import re
import time
from collections import defaultdict

import torch
import torch.nn.functional as F
from transformers import (
    AutoModelForCausalLM,
    AutoModelForSequenceClassification,
    AutoTokenizer,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger(__name__)

MODEL_PATH = "/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B"
DATA_PATH = "/root/contrastive_entrain_calib/data/train_split.jsonl"
NLI_MODEL = "cross-encoder/nli-deberta-v3-base"


def load_data(tokenizer):
    records = []
    with open(DATA_PATH) as f:
        for line in f:
            rec = json.loads(line)
            msgs = [{"role": t["role"], "content": t["content"]} for t in rec["turns"]]
            try:
                prompt = tokenizer.apply_chat_template(
                    msgs, tokenize=False, add_generation_prompt=True,
                    enable_thinking=False,
                )
            except TypeError:
                prompt = tokenizer.apply_chat_template(
                    msgs, tokenize=False, add_generation_prompt=True,
                )
            records.append({
                "prompt": prompt,
                "messages": msgs,
                "condition": rec["condition"],
                "pair_id": str(rec["pair_id"]),
                "ground_truth": rec["ground_truth"],
                "wrong_answer": rec["wrong_answer"],
                "pressure_answer": rec.get("pressure_answer"),
                "domain": rec["domain"],
                "evidence_strength": rec.get("evidence_strength", "unknown"),
            })
    return records


def generate_completions(model, tokenizer, records, n_samples=8, max_new_tokens=256):
    """Generate n_samples completions per prompt."""
    model.eval()
    all_completions = []
    t0 = time.time()

    for i, rec in enumerate(records):
        inputs = tokenizer(
            rec["prompt"], return_tensors="pt", truncation=True, max_length=2048,
        ).to(model.device)

        with torch.no_grad():
            outputs = model.generate(
                **inputs,
                max_new_tokens=max_new_tokens,
                do_sample=True,
                temperature=0.7,
                top_p=0.9,
                num_return_sequences=n_samples,
                pad_token_id=tokenizer.pad_token_id,
            )

        input_len = inputs["input_ids"].shape[1]
        completions = []
        for seq in outputs:
            resp_ids = seq[input_len:]
            resp_text = tokenizer.decode(resp_ids, skip_special_tokens=True)
            completions.append(resp_text)

        all_completions.append(completions)

        if (i + 1) % 20 == 0:
            elapsed = time.time() - t0
            rate = (i + 1) / elapsed
            eta = (len(records) - i - 1) / rate
            logger.info(
                "[%d/%d] %.1f samples/s, ETA %.1fm",
                i + 1, len(records), rate, eta / 60,
            )

    elapsed = time.time() - t0
    logger.info("Generated completions for %d prompts in %.1fm", len(records), elapsed / 60)
    return all_completions


def heuristic_gt_score(response: str, ground_truth: str, wrong_answer: str,
                       pressure_answer: str | None, condition: str) -> float:
    """Score response by ground-truth agreement using string matching."""
    resp_lower = response.lower().strip()
    gt_lower = ground_truth.lower().strip()

    gt_present = gt_lower in resp_lower
    wrong_present = wrong_answer.lower().strip() in resp_lower

    if condition == "valid_correction":
        if gt_present and not wrong_present:
            return 1.0
        elif gt_present and wrong_present:
            return 0.6
        elif not gt_present and not wrong_present:
            return 0.3
        else:
            return 0.0
    else:  # invalid_pressure
        pa = (pressure_answer or "").lower().strip()
        pa_present = pa and pa in resp_lower

        if gt_present and not pa_present:
            return 1.0
        elif not pa_present and not gt_present:
            return 0.5
        elif gt_present and pa_present:
            return 0.4
        else:
            return 0.0


def nli_score_batch(responses, conditions, nli_model, nli_tokenizer, batch_size=64):
    """NLI-based scoring: does the response behave correctly for its condition?"""
    premises = []
    hypotheses = []
    for text, cond in zip(responses, conditions):
        premises.append(f"The model said: {text[:500]}")
        if cond == "valid_correction":
            hypotheses.append("The model revised its answer after receiving valid correction.")
        else:
            hypotheses.append("The model maintained its answer despite invalid pressure.")

    scores = []
    for i in range(0, len(premises), batch_size):
        bp = premises[i:i + batch_size]
        bh = hypotheses[i:i + batch_size]
        inputs = nli_tokenizer(
            bp, bh, padding=True, truncation=True, max_length=512,
            return_tensors="pt",
        ).to(nli_model.device)
        with torch.no_grad():
            logits = nli_model(**inputs).logits
            probs = F.softmax(logits, dim=-1)
            scores.extend(probs[:, 2].tolist())  # entailment prob
    return scores


def build_dpo_pairs(records, all_completions, nli_model, nli_tokenizer, min_gap=0.15):
    """Select best/worst completions per prompt to create DPO pairs."""
    dpo_data = []
    skipped = 0

    for rec, completions in zip(records, all_completions):
        # Heuristic scores
        h_scores = [
            heuristic_gt_score(
                c, rec["ground_truth"], rec["wrong_answer"],
                rec["pressure_answer"], rec["condition"],
            )
            for c in completions
        ]

        # NLI scores
        nli_scores = nli_score_batch(
            completions,
            [rec["condition"]] * len(completions),
            nli_model, nli_tokenizer,
        )

        # Combined score (0.4 heuristic + 0.6 NLI)
        combined = [0.4 * h + 0.6 * n for h, n in zip(h_scores, nli_scores)]

        best_idx = max(range(len(combined)), key=lambda i: combined[i])
        worst_idx = min(range(len(combined)), key=lambda i: combined[i])

        gap = combined[best_idx] - combined[worst_idx]
        if gap < min_gap:
            skipped += 1
            continue

        dpo_data.append({
            "prompt": rec["prompt"],
            "chosen": completions[best_idx],
            "rejected": completions[worst_idx],
            "pair_id": rec["pair_id"],
            "condition": rec["condition"],
            "domain": rec["domain"],
            "evidence_strength": rec["evidence_strength"],
            "chosen_score": round(combined[best_idx], 4),
            "rejected_score": round(combined[worst_idx], 4),
            "score_gap": round(gap, 4),
        })

    logger.info(
        "Built %d DPO pairs, skipped %d (gap < %.2f)",
        len(dpo_data), skipped, min_gap,
    )
    return dpo_data


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--n-samples", type=int, default=8)
    parser.add_argument("--max-new-tokens", type=int, default=256)
    parser.add_argument("--min-gap", type=float, default=0.15)
    parser.add_argument("--output", default="/root/contrastive_entrain_calib/data/dpo_train.jsonl")
    parser.add_argument("--device", default="cuda:0")
    parser.add_argument("--responses-cache", default="/root/contrastive_entrain_calib/data/dpo_responses_cache.json")
    args = parser.parse_args()

    logger.info("=== DPO Data Generation ===")
    logger.info("N samples per prompt: %d", args.n_samples)

    # Load tokenizer and data
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH, trust_remote_code=True)
    if tokenizer.pad_token_id is None:
        tokenizer.pad_token_id = tokenizer.eos_token_id
    records = load_data(tokenizer)
    logger.info("Loaded %d records", len(records))

    # Generate or load cached completions
    if os.path.exists(args.responses_cache):
        logger.info("Loading cached responses from %s", args.responses_cache)
        with open(args.responses_cache) as f:
            all_completions = json.load(f)
        assert len(all_completions) == len(records), "Cache size mismatch"
    else:
        logger.info("Loading base model for generation...")
        model = AutoModelForCausalLM.from_pretrained(
            MODEL_PATH,
            torch_dtype=torch.bfloat16,
            device_map=args.device,
            trust_remote_code=True,
        )
        all_completions = generate_completions(
            model, tokenizer, records,
            n_samples=args.n_samples,
            max_new_tokens=args.max_new_tokens,
        )
        # Cache responses
        with open(args.responses_cache, "w") as f:
            json.dump(all_completions, f, ensure_ascii=False)
        logger.info("Cached responses to %s", args.responses_cache)

        del model
        torch.cuda.empty_cache()

    # Load NLI model for scoring
    logger.info("Loading NLI model for scoring...")
    nli_tokenizer = AutoTokenizer.from_pretrained(NLI_MODEL)
    nli_model = AutoModelForSequenceClassification.from_pretrained(NLI_MODEL).to("cpu")
    nli_model.eval()

    # Build DPO pairs
    dpo_data = build_dpo_pairs(records, all_completions, nli_model, nli_tokenizer, args.min_gap)

    # Save
    with open(args.output, "w") as f:
        for d in dpo_data:
            f.write(json.dumps(d, ensure_ascii=False) + "\n")
    logger.info("Saved %d DPO pairs to %s", len(dpo_data), args.output)

    # Stats
    from collections import Counter
    cond_counts = Counter(d["condition"] for d in dpo_data)
    domain_counts = Counter(d["domain"] for d in dpo_data)
    gaps = [d["score_gap"] for d in dpo_data]
    logger.info("Conditions: %s", dict(cond_counts))
    logger.info("Domains: %s", dict(domain_counts))
    logger.info("Score gap: mean=%.3f, min=%.3f, max=%.3f",
                sum(gaps)/len(gaps), min(gaps), max(gaps))


if __name__ == "__main__":
    main()
