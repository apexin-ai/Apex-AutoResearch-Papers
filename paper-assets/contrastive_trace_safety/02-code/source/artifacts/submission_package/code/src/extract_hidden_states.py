"""Extract hidden states from DeepSeek-R1-Distill-Llama-8B for each sentence in traces.

Input: List of trace dicts (from data_loader.prepare_dataset)
Output: Per-trace .pt files with tensor [num_sentences, 13, 4096] + metadata
"""

import os
from pathlib import Path
from typing import List, Dict

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from tqdm import tqdm

from .config import (
    MODEL_PATH, LAYERS, HIDDEN_DIM, NUM_LAYERS,
    HIDDEN_STATES_DIR, EXTRACT_BATCH_SIZE, DEVICE
)


def load_model(model_path: str = MODEL_PATH, device: str = DEVICE):
    """Load model and tokenizer."""
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


def find_sentence_boundaries(tokenizer, sentences: List[str]) -> List[int]:
    """Find each sentence's last token position via char-to-token offset mapping.

    Tokenizes the full joined text once, then maps each sentence's char span
    to token positions. This avoids BPE context mismatch from per-sentence tokenization.
    """
    full_text = " ".join(sentences)
    encoding = tokenizer(
        full_text,
        return_offsets_mapping=True,
        return_tensors="pt",
        truncation=True,
        max_length=8192,
    )
    offsets = encoding["offset_mapping"][0]  # (num_tokens, 2)

    boundaries = []
    char_pos = 0
    for sent in sentences:
        char_end = char_pos + len(sent)
        last_token_idx = 0
        for tok_idx, (start, end) in enumerate(offsets):
            if start < char_end:
                last_token_idx = tok_idx
        boundaries.append(last_token_idx)
        char_pos = char_end + 1  # +1 for the joining space

    return boundaries


def extract_trace_hidden_states(
    model, tokenizer, sentences: List[str], device: str = DEVICE
) -> torch.Tensor:
    """Extract hidden states for a single trace.

    Concatenates all sentences, does one forward pass, extracts hidden states
    at sentence boundary positions for specified layers.

    Returns: tensor of shape [num_sentences, num_layers, hidden_dim]
    """
    # Find sentence boundaries
    boundary_positions = find_sentence_boundaries(tokenizer, sentences)

    # Tokenize full text
    full_text = " ".join(sentences)
    inputs = tokenizer(
        full_text,
        return_tensors="pt",
        truncation=True,
        max_length=8192,
    ).to(device)

    num_tokens = inputs["input_ids"].shape[1]

    # Clamp boundary positions to valid range
    boundary_positions = [min(p, num_tokens - 1) for p in boundary_positions]

    with torch.no_grad():
        outputs = model(**inputs, output_hidden_states=True)

    # outputs.hidden_states is tuple of (num_layers+1) tensors, each [1, seq_len, hidden_dim]
    # Index 0 is embedding layer, so layer i is at index i+1... but model layers are 0-indexed
    # For LlamaForCausalLM, hidden_states[0] = embeddings, hidden_states[i] = layer i output
    hidden_states = outputs.hidden_states

    # Extract specified layers at boundary positions
    num_sentences = len(sentences)
    result = torch.zeros(num_sentences, NUM_LAYERS, HIDDEN_DIM, dtype=torch.float16)

    for sent_idx, pos in enumerate(boundary_positions):
        for layer_idx, layer_num in enumerate(LAYERS):
            # hidden_states[layer_num + 1] because index 0 is the embedding
            hs = hidden_states[layer_num + 1][0, pos, :]
            result[sent_idx, layer_idx, :] = hs.cpu()

    return result


def extract_all_hidden_states(
    traces: List[Dict],
    model_path: str = MODEL_PATH,
    output_dir: str = None,
    device: str = DEVICE,
    batch_size: int = EXTRACT_BATCH_SIZE,
):
    """Extract hidden states for all traces with checkpoint resumption.

    Saves per-trace .pt files containing:
    - hidden_states: tensor [num_sentences, 13, 4096]
    - trace_id: str
    - num_sentences: int
    - commitment_point: int or None
    """
    if output_dir is None:
        output_dir = str(HIDDEN_STATES_DIR)

    os.makedirs(output_dir, exist_ok=True)

    # Check which traces already have extracted states
    existing = set()
    for f in Path(output_dir).glob("*.pt"):
        existing.add(f.stem)

    remaining = [t for t in traces if t["trace_id"] not in existing]

    if not remaining:
        print(f"All {len(traces)} traces already extracted. Skipping.")
        return

    print(f"Extracting {len(remaining)}/{len(traces)} traces (skipping {len(existing)} existing)")

    model, tokenizer = load_model(model_path, device)

    for trace in tqdm(remaining, desc="Extracting hidden states"):
        trace_id = trace["trace_id"]
        sentences = trace["sentences"]

        hidden_states = extract_trace_hidden_states(model, tokenizer, sentences, device)

        save_dict = {
            "hidden_states": hidden_states,
            "trace_id": trace_id,
            "num_sentences": len(sentences),
            "commitment_point": trace.get("commitment_point"),
            "step_labels": trace.get("step_labels"),
        }

        save_path = Path(output_dir) / f"{trace_id}.pt"
        torch.save(save_dict, save_path)

    print(f"Extraction complete. Files saved to {output_dir}")


def load_hidden_states(trace_id: str, hidden_states_dir: str = None) -> Dict:
    """Load extracted hidden states for a single trace."""
    if hidden_states_dir is None:
        hidden_states_dir = str(HIDDEN_STATES_DIR)
    path = Path(hidden_states_dir) / f"{trace_id}.pt"
    return torch.load(path, map_location="cpu", weights_only=False)
