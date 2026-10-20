#!/usr/bin/env python3
"""Extract per-entity hidden states for binary probe (in-gold vs not-in-gold).

Purpose: Test whether entity quality information exists in model's hidden
representations but is inaccessible via prompting. Compares with:
  - MV agreement AUROC = 0.87 (signal exists in multi-sample outputs)
  - ESJ (prompt-based) AUROC = 0.51 (prompting fails to read it)

Input:
  - samples.jsonl per dataset (SciERC, FewNERD, CoNLL) with gold + 8 samples
  - Fine-tuned Qwen3-8B checkpoints (LoRA adapters)

Output:
  - entity_hidden_states_{dataset}.pt  — (N_entities, 4096)
  - entity_labels_{dataset}.pt         — (N_entities,) binary {0, 1}
  - entity_metadata_{dataset}.json     — per-entity info

Usage:
  CUDA_VISIBLE_DEVICES=0 python extract_entity_hidden_states.py --dataset scierc
  CUDA_VISIBLE_DEVICES=0 python extract_entity_hidden_states.py --dataset fewnerd
  CUDA_VISIBLE_DEVICES=0 python extract_entity_hidden_states.py --dataset conll
"""

import argparse
import json
import os
import random
import re
import time

import numpy as np
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

BASE_DIR = "/root/autodl-tmp/struct_self_consist_ie"
OUTPUT_DIR = os.path.join(BASE_DIR, "output/entity_probe_auroc")

DATASET_CONFIG = {
    "scierc": {
        "data_path": os.path.join(BASE_DIR, "output/exp_012_rerun_1024/samples.jsonl"),
        "model_candidates": [
            os.path.join(BASE_DIR, "checkpoints/qwen3-8b-scierc-merged-v2"),
            os.path.join(BASE_DIR, "checkpoints/qwen3-8b-scierc-lora-v2"),
        ],
        "base_model": "Qwen/Qwen3-8B",
        "schema_hint": (
            "Entity types: Generic, Material, Method, Metric, OtherScientificTerm, Task\n"
            "Relation types: COMPARE, CONJUNCTION, EVALUATE-FOR, FEATURE-OF, HYPONYM-OF, PART-OF, USED-FOR"
        ),
        "max_instances": 551,
        "n_samples": 8,
    },
    "fewnerd": {
        "data_path": os.path.join(BASE_DIR, "output/exp_021_inference/samples.jsonl"),
        "model_candidates": [
            os.path.join(BASE_DIR, "checkpoints/qwen3-8b-fewnerd-exp021-merged"),
            os.path.join(BASE_DIR, "checkpoints/qwen3-8b-fewnerd-5epoch-lora"),
        ],
        "base_model": "Qwen/Qwen3-8B",
        "schema_hint": "Entity types: person, organization, location, building, art, product, event, other",
        "max_instances": 2000,
        "n_samples": 8,
    },
    "conll": {
        "data_path": os.path.join(BASE_DIR, "output/exp_002_conll_n16/samples.jsonl"),
        "model_candidates": [
            os.path.join(BASE_DIR, "checkpoints/qwen3-8b-conll2003-merged"),
            os.path.join(BASE_DIR, "checkpoints/qwen3-8b-conll2003-lora"),
        ],
        "base_model": "Qwen/Qwen3-8B",
        "schema_hint": "Entity types: PER, LOC, ORG, MISC",
        "max_instances": 1000,
        "n_samples": 8,  # use first 8 of 16
    },
}

PROMPT_TEMPLATE = (
    "Extract all structured information (entities and relations) from the following text. "
    "Output a JSON object.\n\n"
    "Text: {text}\n"
    "{schema_line}"
    "\nOutput format: "
    '{{"entities": [{{"text": "...", "type": "...", "start": <int>, "end": <int>}}], '
    '"relations": [{{"head": "...", "tail": "...", "type": "...", '
    '"head_start": <int>, "head_end": <int>, "tail_start": <int>, "tail_end": <int>}}], '
    '"events": []}}'
)


def build_prompt(text, schema_hint):
    schema_line = f"{schema_hint}\n"
    return PROMPT_TEMPLATE.format(text=text, schema_line=schema_line)


def format_chat_prompt(tokenizer, prompt):
    messages = [{"role": "user", "content": prompt}]
    try:
        return tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True,
            enable_thinking=False,
        )
    except TypeError:
        return tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True,
        )


def reconstruct_output_json(sample):
    return json.dumps({
        "entities": sample.get("entities", []),
        "relations": sample.get("relations", []),
        "events": sample.get("events", []),
    }, ensure_ascii=False)


def find_entity_char_ranges(output_json, entities):
    """Find character ranges of each entity's text value in the JSON string.

    For each entity, finds the position of its "text" value in the JSON.
    Returns list of (start_char, end_char) relative to output_json start.
    """
    ranges = []
    search_start = 0
    for ent in entities:
        ent_text = ent["text"]
        # Find the pattern "text": "entity_text" in the JSON
        # Need to account for JSON escaping
        escaped_text = json.dumps(ent_text)[1:-1]  # remove outer quotes
        pattern = f'"text": "{escaped_text}"'
        idx = output_json.find(pattern, search_start)
        if idx == -1:
            # Fallback: try without escaping
            pattern = f'"text": "{ent_text}"'
            idx = output_json.find(pattern, search_start)
        if idx == -1:
            ranges.append(None)
            continue
        # The entity text starts after '"text": "'
        text_start = idx + len('"text": "')
        text_end = text_start + len(escaped_text)
        ranges.append((text_start, text_end))
        search_start = idx + len(pattern)
    return ranges


def char_to_token_range(token_offsets, char_start, char_end):
    """Map character range to token indices using offset mapping."""
    start_tok = None
    end_tok = None
    for i, (cs, ce) in enumerate(token_offsets):
        if cs == ce == 0:
            continue
        if start_tok is None and ce > char_start:
            start_tok = i
        if cs < char_end:
            end_tok = i + 1
    if start_tok is None or end_tok is None:
        return None
    return (start_tok, end_tok)


def extract_entity_hidden_states_for_instance(
    model, tokenizer, text, sample, gold_entities_set, schema_hint,
    instance_idx, sample_idx, device
):
    """Extract hidden state for each entity in a sample.

    Returns list of (hidden_vector, binary_label, metadata_dict).
    """
    prompt = build_prompt(text, schema_hint)
    chat_prompt = format_chat_prompt(tokenizer, prompt)
    output_json = reconstruct_output_json(sample)
    full_text = chat_prompt + output_json

    entities = sample.get("entities", [])
    if not entities:
        return []

    # Tokenize with offset mapping
    prompt_ids = tokenizer.encode(chat_prompt, add_special_tokens=False)
    prompt_len = len(prompt_ids)

    full_ids = tokenizer.encode(full_text, add_special_tokens=False)
    output_ids = full_ids[prompt_len:]
    output_len = len(output_ids)

    if output_len <= 0:
        return []

    # Decode output tokens one by one to build char offset mapping
    output_text_reconstructed = tokenizer.decode(output_ids, skip_special_tokens=False)

    # Find entity text ranges in the output JSON
    entity_char_ranges = find_entity_char_ranges(output_json, entities)

    # Build token-to-char mapping for the output portion
    # We decode each token to get its contribution to the string
    token_char_offsets = []
    cumulative = 0
    for tid in output_ids:
        tok_str = tokenizer.decode([tid], skip_special_tokens=False)
        token_char_offsets.append((cumulative, cumulative + len(tok_str)))
        cumulative += len(tok_str)

    # Run model to get hidden states
    input_tensor = torch.tensor([full_ids], device=device)
    with torch.no_grad():
        outputs = model(input_tensor, output_hidden_states=True)
    last_hidden = outputs.hidden_states[-1][0]  # (seq_len, hidden_dim)
    output_hidden = last_hidden[prompt_len:prompt_len + output_len]  # (output_len, hidden_dim)

    results = []
    for ent_idx, ent in enumerate(entities):
        char_range = entity_char_ranges[ent_idx]
        if char_range is None:
            # Can't find entity in JSON, skip
            continue

        char_start, char_end = char_range
        # Map to token range
        tok_range = char_to_token_range(token_char_offsets, char_start, char_end)
        if tok_range is None or tok_range[0] >= tok_range[1]:
            continue

        tok_start, tok_end = tok_range
        if tok_end > output_len:
            tok_end = output_len
        if tok_start >= output_len:
            continue

        ent_hidden = output_hidden[tok_start:tok_end].float().mean(dim=0).cpu()

        # Binary label: is this entity in gold?
        ent_key = (ent["text"], ent["type"])
        in_gold = 1 if ent_key in gold_entities_set else 0

        meta = {
            "instance_idx": instance_idx,
            "sample_idx": sample_idx,
            "entity_idx": ent_idx,
            "entity_text": ent["text"],
            "entity_type": ent["type"],
            "in_gold": in_gold,
            "tok_span": [tok_start, tok_end],
        }
        results.append((ent_hidden, in_gold, meta))

    return results


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", required=True, choices=["scierc", "fewnerd", "conll"])
    parser.add_argument("--data-path", type=str, default=None,
                        help="Override data_path (samples.jsonl location)")
    parser.add_argument("--max-instances", type=int, default=None)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    config = DATASET_CONFIG[args.dataset]
    max_instances = args.max_instances or config["max_instances"]
    n_samples_use = config["n_samples"]

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    device = "cuda:0" if torch.cuda.is_available() else "cpu"
    print(f"Device: {device}")
    print(f"Dataset: {args.dataset}")

    # Load data
    data_path = args.data_path or config["data_path"]
    print(f"Loading data from: {data_path}")
    with open(data_path) as f:
        all_instances = [json.loads(line) for line in f if line.strip()]
    print(f"  Total instances: {len(all_instances)}")

    # Filter to non-empty gold
    instances = [inst for inst in all_instances if len(inst["gold"].get("entities", [])) > 0]
    print(f"  Gold-filtered: {len(instances)}")

    # Subsample if needed
    if len(instances) > max_instances:
        random.seed(args.seed)
        instances = random.sample(instances, max_instances)
        print(f"  Subsampled to: {len(instances)}")

    # Find available model checkpoint (try merged first, then LoRA)
    print("Loading tokenizer and model...")
    base_model_path = config["base_model"]
    model_path = None
    for candidate in config["model_candidates"]:
        if os.path.exists(candidate):
            model_path = candidate
            break
    if model_path is None:
        raise FileNotFoundError(
            f"No checkpoint found. Tried: {config['model_candidates']}"
        )
    print(f"  Using checkpoint: {model_path}")

    is_lora = os.path.exists(os.path.join(model_path, "adapter_config.json"))

    if is_lora:
        from peft import PeftModel
        tokenizer = AutoTokenizer.from_pretrained(base_model_path, trust_remote_code=True)
        base_model = AutoModelForCausalLM.from_pretrained(
            base_model_path, torch_dtype=torch.bfloat16,
            device_map=device, trust_remote_code=True
        )
        model = PeftModel.from_pretrained(base_model, model_path)
        model = model.merge_and_unload()
    else:
        tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
        model = AutoModelForCausalLM.from_pretrained(
            model_path, torch_dtype=torch.bfloat16,
            device_map=device, trust_remote_code=True
        )

    model.eval()
    print(f"  Model loaded, hidden_dim={model.config.hidden_size}")

    # Extract entity hidden states
    all_hidden = []
    all_labels = []
    all_meta = []

    t0 = time.time()
    n_skipped = 0

    for i, inst in enumerate(instances):
        text = inst["text"]
        gold = inst["gold"]
        gold_entities_set = {(e["text"], e["type"]) for e in gold.get("entities", [])}

        samples = inst["samples"][:n_samples_use]
        for j, sample in enumerate(samples):
            results = extract_entity_hidden_states_for_instance(
                model, tokenizer, text, sample, gold_entities_set,
                config["schema_hint"], i, j, device
            )
            for hidden_vec, label, meta in results:
                all_hidden.append(hidden_vec)
                all_labels.append(label)
                meta["dataset"] = args.dataset
                all_meta.append(meta)

        if (i + 1) % 50 == 0:
            elapsed = time.time() - t0
            rate = (i + 1) / elapsed
            eta = (len(instances) - i - 1) / rate
            n_ent = len(all_hidden)
            pos_rate = sum(all_labels) / max(len(all_labels), 1)
            print(f"  [{i+1}/{len(instances)}] {elapsed:.0f}s, ETA {eta:.0f}s | "
                  f"{n_ent} entities, pos_rate={pos_rate:.3f}")

    elapsed = time.time() - t0
    print(f"\nDone in {elapsed:.1f}s")
    print(f"  Total entities: {len(all_hidden)}")
    print(f"  Positive (in-gold): {sum(all_labels)} ({sum(all_labels)/len(all_labels)*100:.1f}%)")
    print(f"  Negative (not-in-gold): {len(all_labels)-sum(all_labels)}")

    # Save
    hidden_states = torch.stack(all_hidden)
    labels = torch.tensor(all_labels, dtype=torch.long)

    torch.save(hidden_states, os.path.join(OUTPUT_DIR, f"entity_hidden_states_{args.dataset}.pt"))
    torch.save(labels, os.path.join(OUTPUT_DIR, f"entity_labels_{args.dataset}.pt"))
    with open(os.path.join(OUTPUT_DIR, f"entity_metadata_{args.dataset}.json"), "w") as f:
        json.dump({
            "dataset": args.dataset,
            "n_instances": len(instances),
            "n_samples_used": n_samples_use,
            "n_entities": len(all_hidden),
            "n_positive": int(sum(all_labels)),
            "n_negative": len(all_labels) - int(sum(all_labels)),
            "positive_rate": sum(all_labels) / len(all_labels),
            "hidden_dim": model.config.hidden_size,
            "model_path": model_path,
            "extraction_time_seconds": elapsed,
            "per_entity": all_meta,
        }, f, indent=2)

    print(f"Saved to {OUTPUT_DIR}/entity_*_{args.dataset}.*")


if __name__ == "__main__":
    main()
