"""Per-layer spectral effective rank analysis across checkpoints.

Computes eff_rank at every transformer layer (not just the last),
producing a (layers x checkpoints) matrix. Tests whether collapse
signal appears in intermediate layers before the final layer.

Usage:
    python analyze_layer_eff_rank.py \
        --checkpoint-dir /root/autodl-tmp/output_v7/ \
        --model-name EleutherAI/pythia-1b \
        --output-dir /root/autodl-tmp/output_v7/pivot_analysis/

Input:
    Checkpoint directory with G0/G1/G2 subdirs containing checkpoints.

Output:
    - layer_eff_rank_matrix.json: full layer x checkpoint matrix
    - Printed heatmap-style summary
"""

import argparse
import json
import math
import os
import sys
from pathlib import Path

import torch
from tqdm import tqdm
from transformers import AutoModelForCausalLM, AutoTokenizer


def find_checkpoints(base_dir: str) -> list[dict]:
    base = Path(base_dir)
    checkpoints = []
    for gen_dir in sorted(base.glob("G*")):
        gen_idx = int(gen_dir.name[1:])
        for ckpt in sorted(gen_dir.glob("training/checkpoint-*")):
            step = int(ckpt.name.split("-")[-1])
            checkpoints.append({"gen": gen_idx, "step": step, "path": str(ckpt)})
        final = gen_dir / "final_model"
        if final.exists():
            checkpoints.append({"gen": gen_idx, "step": 999999, "path": str(final), "is_final": True})
    return checkpoints


def compute_layer_eff_ranks(
    model, tokenizer, texts: list[str],
    num_samples: int, device: str,
) -> list[float]:
    """Compute eff_rank for every hidden layer. Returns list of length num_layers+1."""
    model.eval()
    layer_hiddens: dict[int, list[torch.Tensor]] = {}
    collected = 0
    batch_size = 8

    for i in range(0, len(texts), batch_size):
        if collected >= num_samples:
            break
        batch = texts[i:i + batch_size]
        enc = tokenizer(batch, return_tensors="pt", padding=True,
                        truncation=True, max_length=2048).to(device)

        with torch.no_grad():
            out = model(**enc, output_hidden_states=True)

        mask = enc["attention_mask"].unsqueeze(-1).float()

        for layer_idx, h in enumerate(out.hidden_states):
            h_float = h.float()
            pooled = (h_float * mask).sum(1) / mask.sum(1).clamp(min=1)
            if layer_idx not in layer_hiddens:
                layer_hiddens[layer_idx] = []
            layer_hiddens[layer_idx].append(pooled.cpu())

        collected += enc["input_ids"].shape[0]

    eff_ranks = []
    for layer_idx in sorted(layer_hiddens.keys()):
        E = torch.cat(layer_hiddens[layer_idx], dim=0)[:num_samples]
        sigma = torch.linalg.svdvals(E)
        sigma_pos = sigma[sigma > 0]
        p = sigma_pos / sigma_pos.sum()
        entropy = -(p * p.log()).sum().item()
        eff_ranks.append(round(math.exp(entropy), 2))

    return eff_ranks


def main():
    parser = argparse.ArgumentParser(description="Per-layer eff_rank analysis")
    parser.add_argument("--checkpoint-dir", required=True)
    parser.add_argument("--model-name", default="EleutherAI/pythia-1b")
    parser.add_argument("--num-samples", type=int, default=1000)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--holdout-texts", default=None)
    parser.add_argument("--only-final", action="store_true",
                        help="Only evaluate final_model checkpoints")
    args = parser.parse_args()

    device = "cuda" if torch.cuda.is_available() else "cpu"
    os.makedirs(args.output_dir, exist_ok=True)

    tokenizer = AutoTokenizer.from_pretrained(args.model_name)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    if args.holdout_texts:
        with open(args.holdout_texts) as f:
            holdout_texts = [line.strip() for line in f if line.strip()]
    else:
        from datasets import load_dataset
        ds = load_dataset("wikitext", "wikitext-103-raw-v1", split="validation")
        holdout_texts = [t for t in ds["text"] if len(t.strip()) > 100][:5000]

    checkpoints = find_checkpoints(args.checkpoint_dir)
    if args.only_final:
        checkpoints = [c for c in checkpoints if c.get("is_final")]
    if not checkpoints:
        print("ERROR: No checkpoints found", file=sys.stderr)
        sys.exit(1)

    all_results = []
    num_layers = None

    for ckpt in tqdm(checkpoints, desc="checkpoints"):
        print(f"\n=== G{ckpt['gen']} step={ckpt['step']} ===")
        model = AutoModelForCausalLM.from_pretrained(
            ckpt["path"], torch_dtype=torch.bfloat16,
        ).to(device)

        layer_ranks = compute_layer_eff_ranks(
            model, tokenizer, holdout_texts, args.num_samples, device)

        if num_layers is None:
            num_layers = len(layer_ranks)

        entry = {
            "generation": ckpt["gen"],
            "step": ckpt["step"],
            "checkpoint": ckpt["path"],
            "layer_eff_ranks": layer_ranks,
            "last_layer_rank": layer_ranks[-1],
            "min_layer_rank": min(layer_ranks),
            "min_layer_idx": layer_ranks.index(min(layer_ranks)),
        }
        all_results.append(entry)
        print(f"  layers={len(layer_ranks)}  last={layer_ranks[-1]:.1f}  "
              f"min={min(layer_ranks):.1f} (layer {entry['min_layer_idx']})")

        del model
        torch.cuda.empty_cache()

    # Print matrix summary
    if num_layers and all_results:
        g0_final = None
        for r in all_results:
            if r["generation"] == 0 and r.get("step") == 999999:
                g0_final = r["layer_eff_ranks"]
                break
        if g0_final is None and all_results:
            g0_final = all_results[0]["layer_eff_ranks"]

        print(f"\n{'Checkpoint':<20}", end="")
        layer_sample = list(range(0, num_layers, max(1, num_layers // 8))) + [num_layers - 1]
        layer_sample = sorted(set(layer_sample))
        for li in layer_sample:
            print(f"{'L' + str(li):<8}", end="")
        print()
        print("-" * (20 + 8 * len(layer_sample)))

        for r in all_results:
            label = f"G{r['generation']}"
            if r.get("step") == 999999:
                label += " final"
            else:
                label += f" s{r['step']}"
            print(f"{label:<20}", end="")
            for li in layer_sample:
                val = r["layer_eff_ranks"][li]
                delta = val - g0_final[li] if g0_final else 0
                sign = "+" if delta >= 0 else ""
                print(f"{val:.0f}({sign}{delta:.0f})", end=" ")
            print()

    out_path = os.path.join(args.output_dir, "layer_eff_rank_matrix.json")
    with open(out_path, "w") as f:
        json.dump({
            "num_layers": num_layers,
            "checkpoints": all_results,
            "g0_baseline": g0_final,
        }, f, indent=2)
    print(f"\nSaved to {out_path}")


if __name__ == "__main__":
    main()
