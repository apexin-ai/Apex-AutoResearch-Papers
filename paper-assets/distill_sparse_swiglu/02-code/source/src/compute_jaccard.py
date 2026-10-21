"""Cross-seed mask Jaccard distance for KL 30% uniform predictors.

For each layer L in LLaMA-3.1-8B, generate per-token binary masks
(uniform per-layer top-k, sparsity=0.30) from 3 seed predictors on the
first NUM_SEQS WikiText-2 sequences, then compute Jaccard distance
(1 - |A∩B|/|A∪B|) per pair of seeds, per layer.
"""
import argparse
import os
import sys
import time

import torch

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data_utils import get_eval_dataset
from predictor import PredictorWrapper, SparsityPredictor
from transformers import AutoModelForCausalLM, AutoTokenizer


BASE_DIR = "/root/distill_sparse_swiglu"
MODEL_PATH = "/root/autodl-tmp/models/llama-3.1-8b"
CHECKPOINTS = {
    "s42":  "checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt",
    "s123": "checkpoints/kl_sparsity30_s123/predictor_kl_normalized.pt",
    "s456": "checkpoints/kl_sparsity30_s456/predictor_kl_normalized.pt",
}
SPARSITY_TARGET = 0.30
NUM_SEQS = 100
SEQ_LEN = 2048


def _best_attn_impl():
    import importlib.util
    if importlib.util.find_spec("flash_attn"):
        return "flash_attention_2"
    return "sdpa"


def load_predictors(ckpt_path, hidden_size, intermediate_size, num_layers, device, dtype):
    """Load a ModuleList of SparsityPredictors from a checkpoint."""
    predictors = torch.nn.ModuleList([
        SparsityPredictor(hidden_size, intermediate_size, bottleneck_size=128)
        for _ in range(num_layers)
    ])
    ckpt = torch.load(ckpt_path, map_location="cpu", weights_only=True)
    predictors.load_state_dict(ckpt["predictors"])
    predictors.to(device=device, dtype=dtype)
    predictors.eval()
    return predictors


@torch.no_grad()
def per_token_topk_mask(logits, sparsity_target):
    """logits: [B, S, I]. Returns bool mask: top (1-sparsity)*I per token kept."""
    intermediate_size = logits.shape[-1]
    k = int(intermediate_size * (1.0 - sparsity_target))
    _, idx = torch.topk(logits, k, dim=-1)
    mask = torch.zeros_like(logits, dtype=torch.bool)
    mask.scatter_(-1, idx, True)
    return mask


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--gpu", type=int, default=0)
    parser.add_argument("--num_seqs", type=int, default=NUM_SEQS)
    parser.add_argument("--seq_len", type=int, default=SEQ_LEN)
    parser.add_argument("--sparsity", type=float, default=SPARSITY_TARGET)
    args = parser.parse_args()

    device = torch.device(f"cuda:{args.gpu}")
    dtype = torch.bfloat16

    print(f"[load] model: {MODEL_PATH}")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_PATH, torch_dtype=dtype, attn_implementation=_best_attn_impl()
    ).to(device).eval()
    cfg = model.config
    num_layers = cfg.num_hidden_layers
    hidden_size = cfg.hidden_size
    intermediate_size = cfg.intermediate_size
    print(f"  layers={num_layers}, hidden={hidden_size}, intermediate={intermediate_size}")

    print("[load] predictors")
    seed_predictors = {}
    for seed, rel_path in CHECKPOINTS.items():
        ckpt_path = rel_path if os.path.isabs(rel_path) else os.path.join(BASE_DIR, rel_path)
        print(f"  {seed}: {ckpt_path}")
        seed_predictors[seed] = load_predictors(
            ckpt_path, hidden_size, intermediate_size, num_layers, device, dtype
        )

    wrapper = PredictorWrapper(model, bottleneck_size=128)
    wrapper.predictors.to(device=device, dtype=dtype)

    print(f"[data] WikiText-2, num_seqs={args.num_seqs}, seq_len={args.seq_len}")
    examples = get_eval_dataset("wikitext2", tokenizer, args.seq_len, max_samples=args.num_seqs)
    print(f"  loaded {len(examples)} sequences")

    seeds = list(CHECKPOINTS.keys())
    pairs = [(seeds[i], seeds[j]) for i in range(len(seeds)) for j in range(i + 1, len(seeds))]

    # int64 accumulators on CPU to avoid overflow and free GPU memory
    inter_counts = {p: torch.zeros(num_layers, dtype=torch.int64) for p in pairs}
    union_counts = {p: torch.zeros(num_layers, dtype=torch.int64) for p in pairs}
    mask_ones = {s: torch.zeros(num_layers, dtype=torch.int64) for s in seeds}
    total_elems = torch.zeros(num_layers, dtype=torch.int64)

    t0 = time.time()
    for i, ex in enumerate(examples):
        input_ids = ex["input_ids"].unsqueeze(0).to(device)
        wrapper.forward_dense(input_ids, capture_intermediates=True)
        layer_inputs = wrapper.get_layer_inputs()

        for li in range(num_layers):
            if li not in layer_inputs:
                continue
            x = layer_inputs[li].to(device=device, dtype=dtype)
            seed_masks = {}
            for seed in seeds:
                logits = seed_predictors[seed][li](x)
                seed_masks[seed] = per_token_topk_mask(logits, args.sparsity)
            n_elems = seed_masks[seeds[0]].numel()
            total_elems[li] += n_elems
            for s in seeds:
                mask_ones[s][li] += seed_masks[s].sum().item()
            for a, b in pairs:
                inter = (seed_masks[a] & seed_masks[b]).sum().item()
                union = (seed_masks[a] | seed_masks[b]).sum().item()
                inter_counts[(a, b)][li] += inter
                union_counts[(a, b)][li] += union
            del seed_masks, x

        if (i + 1) % 10 == 0 or i == 0:
            elapsed = time.time() - t0
            print(f"  seq {i+1}/{len(examples)}  elapsed={elapsed:.1f}s")

    print(f"[done] total processing {time.time() - t0:.1f}s\n")

    # Per-seed empirical sparsity (sanity check)
    print("=" * 72)
    print("Sanity: per-seed mean sparsity (averaged over layers, tokens)")
    print("=" * 72)
    for s in seeds:
        empirical_density = mask_ones[s].sum().item() / total_elems.sum().item()
        print(f"  {s}: density={empirical_density:.4f}, sparsity={1 - empirical_density:.4f}")

    # Jaccard per pair, per layer
    print()
    print("=" * 72)
    print(f"Jaccard distance (1 - |A∩B|/|A∪B|) per layer, sparsity_target={args.sparsity}")
    print("=" * 72)
    header = f"{'Layer':>5} | " + " | ".join(f"{a}-{b}".rjust(10) for a, b in pairs)
    print(header)
    print("-" * len(header))
    layer_jd = {p: [] for p in pairs}
    for li in range(num_layers):
        row = [f"{li:5d}"]
        for p in pairs:
            inter = inter_counts[p][li].item()
            union = union_counts[p][li].item()
            jd = 1.0 - (inter / union) if union > 0 else float("nan")
            layer_jd[p].append(jd)
            row.append(f"{jd:10.4f}")
        print(" | ".join(row))

    print("-" * len(header))
    means = [f"{sum(layer_jd[p]) / num_layers:10.4f}" for p in pairs]
    print(f"{'MEAN':>5} | " + " | ".join(means))

    # Model-level aggregate (single Jaccard pooling all layers)
    print()
    print("=" * 72)
    print("Model-level Jaccard distance (pooled across all layers)")
    print("=" * 72)
    pooled = []
    for p in pairs:
        inter = inter_counts[p].sum().item()
        union = union_counts[p].sum().item()
        jd = 1.0 - (inter / union) if union > 0 else float("nan")
        pooled.append(jd)
        print(f"  {p[0]}-{p[1]}: Jaccard_distance={jd:.4f}  (IoU={1-jd:.4f})")
    print(f"  PAIR-MEAN: {sum(pooled)/len(pooled):.4f}")


if __name__ == "__main__":
    main()
