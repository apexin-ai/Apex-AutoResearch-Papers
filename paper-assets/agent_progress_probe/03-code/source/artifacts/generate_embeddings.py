#!/usr/bin/env python3
"""Generate step embeddings for labeled windows using Qwen3-Embedding-0.6B.

Expected windows_labeled.jsonl format (one JSON per line):
    {"trajectory_id": str, "window_idx": int, "step_indices": [int, ...],
     "majority_label": int (0=stagnation, 1=progress, -1=abstain),
     "confidence": int, "labels": {...}, "short_trajectory": bool}

trajectory_id format: "instance_id__model_name__r{row_index}"

Requires the original trajectories JSONL to retrieve step texts.

Output: embeddings.pt containing per-window embedding tensors + metadata.
"""

import argparse
import json
from collections import defaultdict
from pathlib import Path

import torch
import torch.nn.functional as F
from tqdm import tqdm
from transformers import AutoModel, AutoTokenizer


def last_token_pool(last_hidden_states: torch.Tensor, attention_mask: torch.Tensor) -> torch.Tensor:
    left_padding = attention_mask[:, -1].sum() == attention_mask.shape[0]
    if left_padding:
        return last_hidden_states[:, -1]
    seq_lengths = attention_mask.sum(dim=1) - 1
    batch_idx = torch.arange(last_hidden_states.shape[0], device=last_hidden_states.device)
    return last_hidden_states[batch_idx, seq_lengths]


def parse_row_index(trajectory_id: str) -> int:
    """Extract row_index from trajectory_id 'instance_id__model_name__r{idx}'."""
    return int(trajectory_id.rsplit("__r", 1)[1])


def build_trajectory_index(traj_path: str) -> tuple[dict, dict]:
    """Build trajectory index from raw JSONL.

    Returns:
        steps_index: row_index (int) -> list of step dicts
        meta_index: row_index (int) -> {"instance_id": str, "model_name": str}
    """
    steps_index = {}
    meta_index = {}
    with open(traj_path) as f:
        for row_idx, line in enumerate(f):
            line = line.strip()
            if not line:
                continue
            raw = json.loads(line)
            steps = []
            for s in raw.get("trajectory") or []:
                steps.append({
                    "role": s.get("role", "unknown"),
                    "text": s.get("text") or s.get("system_prompt") or "",
                })
            steps_index[row_idx] = steps
            meta_index[row_idx] = {
                "instance_id": raw.get("instance_id", ""),
                "model_name": raw.get("model_name", ""),
            }
    return steps_index, meta_index


def load_windows(path: str) -> list[dict]:
    windows = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                windows.append(json.loads(line))
    return windows


@torch.no_grad()
def encode_texts(
    texts: list[str], model, tokenizer, batch_size: int, max_length: int, device: str
) -> torch.Tensor:
    all_embeds = []
    for i in range(0, len(texts), batch_size):
        batch = texts[i : i + batch_size]
        encoded = tokenizer(
            batch, max_length=max_length, padding=True, truncation=True, return_tensors="pt"
        ).to(device)
        outputs = model(**encoded)
        embeds = last_token_pool(outputs.last_hidden_state, encoded["attention_mask"])
        embeds = F.normalize(embeds, p=2, dim=1)
        all_embeds.append(embeds.cpu())
    return torch.cat(all_embeds, dim=0)


def main():
    parser = argparse.ArgumentParser(description="Generate step embeddings using Qwen3-Embedding-0.6B")
    parser.add_argument("--windows", required=True, help="Path to windows_labeled.jsonl")
    parser.add_argument("--trajectories", required=True, help="Path to original trajectories JSONL")
    parser.add_argument("--output", required=True, help="Output .pt file path")
    parser.add_argument("--model_name", default="Qwen/Qwen3-Embedding-0.6B")
    parser.add_argument("--batch_size", type=int, default=64, help="Texts per encoding batch")
    parser.add_argument("--max_length", type=int, default=512, help="Max tokens per step text")
    parser.add_argument("--device", default=None, help="Device (auto-detect if unset)")
    parser.add_argument("--chunk_size", type=int, default=500, help="Windows per checkpoint chunk")
    args = parser.parse_args()

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    checkpoint_path = output_path.with_suffix(".ckpt.pt")
    device = args.device or ("cuda" if torch.cuda.is_available() else "cpu")

    # Resume
    start_idx = 0
    results = {"embeddings": [], "labels": [], "trajectory_ids": [], "instance_ids": [], "step_indices_list": [], "confidences": []}
    if checkpoint_path.exists():
        ckpt = torch.load(checkpoint_path, weights_only=False)
        results = ckpt["results"]
        start_idx = ckpt["next_idx"]
        print(f"Resumed from checkpoint: {start_idx} windows done")

    # Load model
    print(f"Loading {args.model_name} ...")
    tokenizer = AutoTokenizer.from_pretrained(args.model_name, trust_remote_code=True)
    tokenizer.padding_side = "right"
    model = (
        AutoModel.from_pretrained(args.model_name, trust_remote_code=True, torch_dtype=torch.float16)
        .to(device)
        .eval()
    )
    embed_dim = model.config.hidden_size
    print(f"embed_dim={embed_dim}, device={device}")

    # Load data
    print("Building trajectory index ...")
    traj_index, meta_index = build_trajectory_index(args.trajectories)
    print(f"Indexed {len(traj_index)} trajectories")

    all_windows = load_windows(args.windows)
    windows = [w for w in all_windows if w.get("majority_label", -1) != -1]
    print(f"Total windows: {len(all_windows)}, usable (non-ABSTAIN): {len(windows)}, pending: {len(windows) - start_idx}")

    if start_idx >= len(windows):
        print("All windows already processed.")
        return

    pbar = tqdm(total=len(windows), initial=start_idx, desc="Embedding")

    for chunk_start in range(start_idx, len(windows), args.chunk_size):
        chunk_end = min(chunk_start + args.chunk_size, len(windows))
        chunk = windows[chunk_start:chunk_end]

        # Collect all step texts in this chunk
        all_texts = []
        text_map = []  # (window_idx_in_chunk, step_position)
        for ci, w in enumerate(chunk):
            row_index = w.get("row_index") or parse_row_index(w["trajectory_id"])
            steps = traj_index.get(row_index, [])
            for si, step_idx in enumerate(w["step_indices"]):
                text = steps[step_idx]["text"] if step_idx < len(steps) else ""
                all_texts.append(text if text else "[empty]")
                text_map.append((ci, si))

        # Batch encode
        if all_texts:
            all_embeds = encode_texts(all_texts, model, tokenizer, args.batch_size, args.max_length, device)
        else:
            all_embeds = torch.zeros(0, embed_dim)

        # Reassemble per window
        window_positions = defaultdict(list)
        for pos, (ci, si) in enumerate(text_map):
            window_positions[ci].append((si, pos))

        for ci, w in enumerate(chunk):
            positions = sorted(window_positions.get(ci, []), key=lambda x: x[0])
            if positions:
                window_tensor = torch.stack([all_embeds[pos] for _, pos in positions])
            else:
                window_tensor = torch.zeros(1, embed_dim)

            ri = w.get("row_index") or parse_row_index(w["trajectory_id"])
            instance_id = w.get("instance_id", meta_index[ri]["instance_id"])
            results["embeddings"].append(window_tensor)
            results["labels"].append(w["majority_label"])
            results["trajectory_ids"].append(w["trajectory_id"])
            results["instance_ids"].append(instance_id)
            results["step_indices_list"].append(w["step_indices"])
            results["confidences"].append(w["confidence"])

        pbar.update(len(chunk))

        # Checkpoint
        torch.save({"results": results, "next_idx": chunk_end}, checkpoint_path)

    pbar.close()

    # Save final output
    torch.save(
        {
            "embeddings": results["embeddings"],
            "labels": results["labels"],
            "trajectory_ids": results["trajectory_ids"],
            "instance_ids": results["instance_ids"],
            "step_indices_list": results["step_indices_list"],
            "confidences": results["confidences"],
            "embed_dim": embed_dim,
        },
        output_path,
    )
    print(f"Saved {len(results['embeddings'])} window embeddings to {output_path}")

    if checkpoint_path.exists():
        checkpoint_path.unlink()


if __name__ == "__main__":
    main()
