"""Extract ALL 25 layers (L0-L24) of hidden states from DeepSeek-R1-Distill-Llama-8B.

Reviewer requirement: cover shallow layers to test composite metric shallow bias.
Existing pipeline only extracts L12-L24 (13 layers). This script extracts L0-L24 (25 layers).

Usage:
    # Dry-run (2 traces, verify output format)
    python -m src.advbench.extract_hidden_states --dry-run

    # Full extraction
    python -m src.advbench.extract_hidden_states

    # Shard (e.g., traces 0-99)
    python -m src.advbench.extract_hidden_states --start 0 --end 100

    # Custom output dir
    python -m src.advbench.extract_hidden_states --output-dir artifacts/hidden_states_all25
"""

import argparse
import os
from pathlib import Path

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from tqdm import tqdm

MODEL_PATH = "MODEL_DIR/DeepSeek-R1-Distill-Llama-8B"
MODEL_NAME = "deepseek-ai/DeepSeek-R1-Distill-Llama-8B"
EXTRACT_LAYERS = list(range(25))  # L0-L24 (model has 33: embedding + 32 transformer layers)
NUM_EXTRACT_LAYERS = 25
HIDDEN_DIM = 4096
DEFAULT_OUTPUT_DIR = "DATA_DIR/artifacts/hidden_states_all25"
HF_DATASET = "ishitakakkar-10/HarmThoughts"
TARGET_MODEL = "r1-8b"
SAFETY_LABELS = {"RA", "AL", "CC", "ED", "IA"}
DEVICE = "cuda:0"
MAX_LENGTH = 8192


def load_model(model_path: str = MODEL_PATH, device: str = DEVICE):
    tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    model = AutoModelForCausalLM.from_pretrained(
        model_path,
        torch_dtype=torch.float16,
        device_map=device,
        trust_remote_code=True,
    )
    model.eval()
    return model, tokenizer


def load_traces(model_name: str = TARGET_MODEL):
    from collections import defaultdict
    from datasets import load_dataset

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

        cp = _extract_commitment_point(labels)
        step_labels = None
        if cp is not None:
            step_labels = [0 if i < cp else 1 for i in range(len(steps))]

        traces.append({
            "trace_id": trace_id,
            "sentences": sentences,
            "labels": labels,
            "query": steps[0]["query"],
            "is_jailbreak": is_jailbreak,
            "num_steps": len(steps),
            "commitment_point": cp,
            "step_labels": step_labels,
        })

    return traces


def _extract_commitment_point(labels):
    last_safety_idx = None
    for i, label in enumerate(labels):
        if label in SAFETY_LABELS:
            last_safety_idx = i
    if last_safety_idx is None or last_safety_idx == len(labels) - 1:
        return None
    return last_safety_idx + 1


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


def extract_trace_hidden_states(model, tokenizer, sentences, device=DEVICE):
    """Extract hidden states for all 25 layers at sentence boundary positions.

    Returns: tensor [num_sentences, 25, 4096]
    """
    boundary_positions = find_sentence_boundaries(tokenizer, sentences)

    full_text = " ".join(sentences)
    inputs = tokenizer(
        full_text,
        return_tensors="pt",
        truncation=True,
        max_length=MAX_LENGTH,
    ).to(device)

    num_tokens = inputs["input_ids"].shape[1]
    boundary_positions = [min(p, num_tokens - 1) for p in boundary_positions]

    with torch.no_grad():
        outputs = model(**inputs, output_hidden_states=True)

    # hidden_states[0] = embedding, hidden_states[1..32] = transformer layers
    # Model has 33 entries total; we extract indices 0..24 (L0-L24)
    hidden_states = outputs.hidden_states

    num_sentences = len(sentences)
    result = torch.zeros(num_sentences, NUM_EXTRACT_LAYERS, HIDDEN_DIM, dtype=torch.float16)

    for sent_idx, pos in enumerate(boundary_positions):
        for layer_idx, layer_num in enumerate(EXTRACT_LAYERS):
            hs = hidden_states[layer_num][0, pos, :]
            result[sent_idx, layer_idx, :] = hs.cpu()

    return result


def main():
    parser = argparse.ArgumentParser(
        description="Extract all 25 layers of hidden states from R1-8B traces"
    )
    parser.add_argument("--model-path", default=MODEL_PATH)
    parser.add_argument("--output-dir", default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--device", default=DEVICE)
    parser.add_argument("--batch-size", type=int, default=1,
                        help="Traces per batch (sequential forward pass per trace)")
    parser.add_argument("--start", type=int, default=None,
                        help="Start index for trace shard (inclusive)")
    parser.add_argument("--end", type=int, default=None,
                        help="End index for trace shard (exclusive)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Process only 2 traces to verify output format")
    args = parser.parse_args()

    print("Loading traces from HarmThoughts...")
    traces = load_traces()
    print(f"Loaded {len(traces)} traces")

    if args.start is not None or args.end is not None:
        start = args.start or 0
        end = args.end or len(traces)
        traces = traces[start:end]
        print(f"Shard: traces[{start}:{end}] = {len(traces)} traces")

    if args.dry_run:
        traces = traces[:2]
        print(f"Dry-run: processing {len(traces)} traces")

    os.makedirs(args.output_dir, exist_ok=True)

    existing = {f.stem for f in Path(args.output_dir).glob("*.pt")}
    remaining = [t for t in traces if t["trace_id"] not in existing]

    if not remaining:
        print(f"All {len(traces)} traces already extracted. Done.")
        return

    print(f"Extracting {len(remaining)}/{len(traces)} traces "
          f"(skipping {len(traces) - len(remaining)} existing)")

    print(f"Loading model from {args.model_path}...")
    model, tokenizer = load_model(args.model_path, args.device)

    hs_count = len(model(
        tokenizer("test", return_tensors="pt").input_ids.to(args.device),
        output_hidden_states=True
    ).hidden_states)
    print(f"Model returns {hs_count} hidden state layers, extracting L0-L24 ({NUM_EXTRACT_LAYERS} layers)")
    assert hs_count >= NUM_EXTRACT_LAYERS, (
        f"Model has {hs_count} layers but need at least {NUM_EXTRACT_LAYERS}"
    )

    for trace in tqdm(remaining, desc="Extracting hidden states (all 25 layers)"):
        trace_id = trace["trace_id"]
        sentences = trace["sentences"]

        hidden_states = extract_trace_hidden_states(
            model, tokenizer, sentences, args.device
        )

        save_dict = {
            "hidden_states": hidden_states,
            "trace_id": trace_id,
            "num_sentences": len(sentences),
            "commitment_point": trace.get("commitment_point"),
            "step_labels": trace.get("step_labels"),
        }

        save_path = Path(args.output_dir) / f"{trace_id}.pt"
        torch.save(save_dict, save_path)

        if args.dry_run:
            print(f"  {trace_id}: hidden_states shape={hidden_states.shape} "
                  f"dtype={hidden_states.dtype}")

    print(f"Extraction complete. Files saved to {args.output_dir}")


if __name__ == "__main__":
    main()
