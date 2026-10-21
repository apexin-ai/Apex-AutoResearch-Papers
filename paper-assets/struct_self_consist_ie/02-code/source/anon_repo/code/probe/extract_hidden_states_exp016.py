#!/usr/bin/env python3
"""Extract hidden states from Qwen3-8B SciERC model using exp_012_rerun_1024 data.

Same as extract_hidden_states.py but pointing to rerun_1024 data.
Output: hidden_state_probe_exp016/{hidden_states.pt, labels.pt, logprobs.pt, metadata.json}
"""

import json
import os
import sys
import time

import numpy as np
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL_PATH = "/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-merged-v2"
DATA_PATH = "/root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/samples_with_logprobs.jsonl"
OUTPUT_DIR = "/root/autodl-tmp/struct_self_consist_ie/output/hidden_state_probe_exp016"

SCIERC_SCHEMA_HINT = (
    "Entity types: Generic, Material, Method, Metric, OtherScientificTerm, Task\n"
    "Relation types: COMPARE, CONJUNCTION, EVALUATE-FOR, FEATURE-OF, HYPONYM-OF, PART-OF, USED-FOR"
)

TRAIN_ALIGNED_TEMPLATE = (
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


def build_prompt(text):
    schema_line = f"{SCIERC_SCHEMA_HINT}\n"
    return TRAIN_ALIGNED_TEMPLATE.format(text=text, schema_line=schema_line)


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
    output = {
        "entities": sample.get("entities", []),
        "relations": sample.get("relations", []),
        "events": sample.get("events", []),
    }
    return json.dumps(output, ensure_ascii=False)


def entity_set(ext):
    return {(e["text"], e["type"]) for e in ext.get("entities", [])}


def compute_ner_f1(pred, gold):
    pred_set = entity_set(pred)
    gold_set = entity_set(gold)
    tp = len(pred_set & gold_set)
    if tp == 0:
        return 0.0
    p = tp / (tp + len(pred_set - gold_set))
    r = tp / (tp + len(gold_set - pred_set))
    return 2 * p * r / (p + r)


def main():
    gpu_id = int(os.environ.get("CUDA_VISIBLE_DEVICES", "0").split(",")[0])
    device = f"cuda:{gpu_id}" if torch.cuda.is_available() else "cpu"
    print(f"Using device: {device}")

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print("Loading data...")
    with open(DATA_PATH) as f:
        instances = [json.loads(line) for line in f if line.strip()]
    print(f"  {len(instances)} instances, {len(instances[0]['samples'])} samples each")

    # Verify greedy F1 (text-based, gold-filtered)
    greedy_f1s = []
    for inst in instances:
        gold = inst["gold"]
        if len(gold.get("entities", [])) == 0:
            continue
        greedy = inst.get("greedy", inst["samples"][0])
        greedy_f1s.append(compute_ner_f1(greedy, gold))
    print(f"  Gold-filtered: {len(greedy_f1s)} instances")
    print(f"  Text-based greedy F1: {np.mean(greedy_f1s):.4f}")

    total_pairs = sum(len(inst["samples"]) for inst in instances)
    print(f"  Total (instance, sample) pairs: {total_pairs}")

    print("Loading tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH, trust_remote_code=True)

    print("Loading model...")
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_PATH,
        torch_dtype=torch.bfloat16,
        device_map=device,
        trust_remote_code=True,
    )
    model.eval()
    print(f"  Model loaded on {device}")

    all_hidden_states = []
    all_labels = []
    all_logprobs = []
    all_meta = []

    t0 = time.time()
    for i, inst in enumerate(instances):
        text = inst["text"]
        gold = inst["gold"]
        prompt = build_prompt(text)
        chat_prompt = format_chat_prompt(tokenizer, prompt)

        prompt_ids = tokenizer.encode(chat_prompt, add_special_tokens=False)
        prompt_len = len(prompt_ids)

        for j, sample in enumerate(inst["samples"]):
            output_json = reconstruct_output_json(sample)
            full_text = chat_prompt + output_json
            input_ids = tokenizer.encode(full_text, add_special_tokens=False)
            output_start = prompt_len
            output_len = len(input_ids) - prompt_len

            if output_len <= 0:
                hs_vec = torch.zeros(model.config.hidden_size, dtype=torch.float32)
            else:
                input_tensor = torch.tensor([input_ids], device=model.device)
                with torch.no_grad():
                    outputs = model(input_tensor, output_hidden_states=True)
                last_hidden = outputs.hidden_states[-1][0]
                output_hidden = last_hidden[output_start:output_start + output_len]
                hs_vec = output_hidden.float().mean(dim=0).cpu()

            f1 = compute_ner_f1(sample, gold)
            lp = sample.get("mean_logprob")
            if lp is None:
                lp = sample.get("cumulative_logprob", -999) / max(sample.get("n_tokens", 1), 1)

            all_hidden_states.append(hs_vec)
            all_labels.append(f1)
            all_logprobs.append(lp)
            all_meta.append({
                "instance_idx": i,
                "sample_idx": j,
                "instance_id": inst.get("id", ""),
                "f1": f1,
                "mean_logprob": lp,
                "n_tokens": sample.get("n_tokens", 0),
            })

        if (i + 1) % 50 == 0:
            elapsed = time.time() - t0
            rate = (i + 1) / elapsed
            eta = (len(instances) - i - 1) / rate
            print(f"  [{i+1}/{len(instances)}] {elapsed:.0f}s elapsed, ETA {eta:.0f}s")

    elapsed = time.time() - t0
    print(f"Done extracting hidden states in {elapsed:.1f}s")

    hidden_states = torch.stack(all_hidden_states)
    labels = torch.tensor(all_labels, dtype=torch.float32)
    logprobs = torch.tensor(all_logprobs, dtype=torch.float32)

    print(f"  hidden_states shape: {hidden_states.shape}")
    print(f"  labels shape: {labels.shape}, range [{labels.min():.3f}, {labels.max():.3f}]")

    torch.save(hidden_states, os.path.join(OUTPUT_DIR, "hidden_states.pt"))
    torch.save(labels, os.path.join(OUTPUT_DIR, "labels.pt"))
    torch.save(logprobs, os.path.join(OUTPUT_DIR, "logprobs.pt"))

    with open(os.path.join(OUTPUT_DIR, "metadata.json"), "w") as f:
        json.dump({
            "n_instances": len(instances),
            "n_samples_per_instance": len(instances[0]["samples"]),
            "total_pairs": len(all_meta),
            "hidden_dim": model.config.hidden_size,
            "model_path": MODEL_PATH,
            "data_path": DATA_PATH,
            "extraction_time_seconds": elapsed,
            "per_sample_meta": all_meta,
        }, f, indent=2)

    print(f"Saved to {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
