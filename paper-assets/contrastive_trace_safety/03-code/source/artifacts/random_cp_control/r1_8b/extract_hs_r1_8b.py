"""Extract ALL 25 layers (L0-L24) of hidden states from DeepSeek-R1-Distill-Llama-8B.

Standalone script for westd server. Saves per-trace .pt files.
"""
import argparse
import os
import time
from pathlib import Path
from collections import defaultdict

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from datasets import load_dataset

MODEL_NAME = "deepseek-ai/DeepSeek-R1-Distill-Llama-8B"
EXTRACT_LAYERS = list(range(25))
NUM_EXTRACT_LAYERS = 25
HIDDEN_DIM = 4096
HF_DATASET = "ishitakakkar-10/HarmThoughts"
TARGET_MODEL = "r1-8b"
SAFETY_LABELS = {"RA", "AL", "CC", "ED", "IA"}
MAX_LENGTH = 8192


def ts():
    return time.strftime("[%H:%M:%S]")


def load_traces(model_name=TARGET_MODEL):
    ds = load_dataset(HF_DATASET, split="train")
    traces_raw = defaultdict(list)
    for row in ds:
        if row["model_name"] != model_name:
            continue
        sid = row["sentence_id"]
        parts = sid.rsplit("-", 1)
        trace_id = parts[0]
        step_idx = int(parts[1]) - 1
        traces_raw[trace_id].append({
            "step_idx": step_idx,
            "sentence": row["sentence"],
            "label": row["llm_annotation"],
            "query": row["query"],
            "final_judgment": row["final_judgment"],
        })

    traces = []
    for trace_id, steps in traces_raw.items():
        steps.sort(key=lambda x: x["step_idx"])
        labels = [s["label"] for s in steps]
        sentences = [s["sentence"] for s in steps]
        is_jailbreak = steps[0]["final_judgment"] == 1.0

        last_safety_idx = None
        for i, label in enumerate(labels):
            if label in SAFETY_LABELS:
                last_safety_idx = i
        cp = None
        if last_safety_idx is not None and last_safety_idx < len(labels) - 1:
            cp = last_safety_idx + 1

        step_labels = None
        if cp is not None:
            step_labels = [0 if i < cp else 1 for i in range(len(steps))]

        traces.append({
            "trace_id": trace_id,
            "sentences": sentences,
            "labels": labels,
            "is_jailbreak": is_jailbreak,
            "num_steps": len(steps),
            "commitment_point": cp,
            "step_labels": step_labels,
        })
    return traces


def find_sentence_boundaries(tokenizer, sentences):
    full_text = " ".join(sentences)
    encoding = tokenizer(
        full_text,
        return_offsets_mapping=True,
        return_tensors="pt",
        truncation=True,
        max_length=MAX_LENGTH,
    )
    offsets = encoding["offset_mapping"][0]

    boundaries = []
    char_pos = 0
    for sent in sentences:
        char_end = char_pos + len(sent)
        last_token_idx = 0
        for tok_idx, (start, end) in enumerate(offsets):
            if start < char_end:
                last_token_idx = tok_idx
        boundaries.append(last_token_idx)
        char_pos = char_end + 1
    return boundaries


def extract_trace_hidden_states(model, tokenizer, sentences, device="cuda:0"):
    boundary_positions = find_sentence_boundaries(tokenizer, sentences)
    full_text = " ".join(sentences)
    inputs = tokenizer(
        full_text, return_tensors="pt", truncation=True, max_length=MAX_LENGTH,
    ).to(device)

    num_tokens = inputs["input_ids"].shape[1]
    boundary_positions = [min(p, num_tokens - 1) for p in boundary_positions]

    with torch.no_grad():
        outputs = model(**inputs, output_hidden_states=True)

    hidden_states = outputs.hidden_states
    num_sentences = len(sentences)
    result = torch.zeros(num_sentences, NUM_EXTRACT_LAYERS, HIDDEN_DIM, dtype=torch.float16)

    for sent_idx, pos in enumerate(boundary_positions):
        for layer_idx, layer_num in enumerate(EXTRACT_LAYERS):
            hs = hidden_states[layer_num][0, pos, :]
            result[sent_idx, layer_idx, :] = hs.cpu()

    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model-path", default=None,
                        help="Local model path. If not given, downloads from HF.")
    parser.add_argument("--output-dir", default="/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states_r1_8b_full")
    parser.add_argument("--device", default="cuda:0")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    model_path = args.model_path or MODEL_NAME

    print(f"{ts()} Loading traces from HarmThoughts...")
    traces = load_traces()
    jb_with_cp = [t for t in traces if t["is_jailbreak"] and t["commitment_point"] is not None]
    print(f"  Total traces: {len(traces)}, jailbreak with CP: {len(jb_with_cp)}")

    if args.dry_run:
        jb_with_cp = jb_with_cp[:2]
        print(f"  Dry-run: {len(jb_with_cp)} traces")

    os.makedirs(args.output_dir, exist_ok=True)
    existing = {f.stem for f in Path(args.output_dir).glob("*.pt")}
    remaining = [t for t in jb_with_cp if t["trace_id"] not in existing]

    if not remaining:
        print(f"All {len(jb_with_cp)} traces already extracted.")
        return

    print(f"{ts()} Extracting {len(remaining)}/{len(jb_with_cp)} traces "
          f"(skipping {len(jb_with_cp) - len(remaining)} existing)")

    print(f"{ts()} Loading model: {model_path}")
    tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    model = AutoModelForCausalLM.from_pretrained(
        model_path, torch_dtype=torch.float16, device_map=args.device,
        trust_remote_code=True,
    )
    model.eval()

    hs_count = len(model(
        tokenizer("test", return_tensors="pt").input_ids.to(args.device),
        output_hidden_states=True,
    ).hidden_states)
    print(f"  Model returns {hs_count} hidden state layers, extracting L0-L24 ({NUM_EXTRACT_LAYERS})")
    assert hs_count >= NUM_EXTRACT_LAYERS

    for i, trace in enumerate(remaining):
        t0 = time.time()
        hidden_states = extract_trace_hidden_states(
            model, tokenizer, trace["sentences"], args.device
        )
        save_dict = {
            "hidden_states": hidden_states,
            "trace_id": trace["trace_id"],
            "num_sentences": trace["num_steps"],
            "commitment_point": trace["commitment_point"],
            "step_labels": trace["step_labels"],
        }
        save_path = Path(args.output_dir) / f"{trace['trace_id']}.pt"
        torch.save(save_dict, save_path)
        elapsed = time.time() - t0
        if (i + 1) % 10 == 0 or args.dry_run:
            print(f"  [{i+1}/{len(remaining)}] {trace['trace_id']}: "
                  f"shape={hidden_states.shape} ({elapsed:.1f}s)")

    print(f"{ts()} Extraction complete. Files saved to {args.output_dir}")


if __name__ == "__main__":
    main()
