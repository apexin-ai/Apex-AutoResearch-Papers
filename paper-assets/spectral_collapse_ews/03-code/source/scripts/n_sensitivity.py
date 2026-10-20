"""
SLV sensitivity to sample size n.

Computes SLV on the same model checkpoint with varying numbers of held-out
samples (n ∈ {250, 500, 1000, 2000, 5000}). For each n, draws multiple
random subsamples from a pool of 5000 embeddings to estimate mean and
standard deviation. Outputs a table of n vs SLV with relative change.

Usage:
    python scripts/n_sensitivity.py --gpu 0
    python scripts/n_sensitivity.py --checkpoint_path /path/to/checkpoint --gpu 1
    python scripts/n_sensitivity.py --gen 0 --condition pure_collapse --seed 42 --gpu 0
"""
import os
import sys
import json
import time
import argparse

import torch
import numpy as np

os.environ["TOKENIZERS_PARALLELISM"] = "false"
os.environ["HF_HOME"] = "/root/autodl-tmp/.hf_cache"

EPSILON = 1e-10
BASE_MODEL = "EleutherAI/pythia-410m-deduped"
MAX_LENGTH = 512
BATCH_SIZE = 16
POOL_SIZE = 5000
DEFAULT_N_VALUES = [250, 500, 1000, 2000, 5000]
DEFAULT_N_REPEATS = 10


def parse_args():
    p = argparse.ArgumentParser(description="SLV sensitivity to sample size n")
    p.add_argument("--checkpoint_path", type=str, default=None,
                   help="Path to model checkpoint. Default: pretrained Pythia-410M.")
    p.add_argument("--condition", type=str, default=None,
                   help="Condition name (e.g. pure_collapse, fixed_mix_0.3). "
                        "Used with --gen and --seed to resolve checkpoint path.")
    p.add_argument("--gen", type=int, default=None,
                   help="Generation number. Used with --condition and --seed.")
    p.add_argument("--seed", type=int, default=42,
                   help="Random seed for checkpoint resolution and subsampling.")
    p.add_argument("--gpu", type=int, default=0, help="GPU device index.")
    p.add_argument("--n_values", type=int, nargs="+", default=DEFAULT_N_VALUES,
                   help="Sample sizes to evaluate.")
    p.add_argument("--n_repeats", type=int, default=DEFAULT_N_REPEATS,
                   help="Number of random subsamples per n value.")
    p.add_argument("--output", type=str,
                   default="/root/spectral_collapse_ews/results/n_sensitivity.json",
                   help="Output path for results JSON.")
    return p.parse_args()


def resolve_checkpoint(args):
    """Resolve checkpoint path from args."""
    if args.checkpoint_path:
        return args.checkpoint_path
    if args.condition is not None and args.gen is not None:
        base = "/root/autodl-tmp/spectral_collapse_ews/checkpoints_phase1"
        path = os.path.join(base, f"{args.condition}_{args.seed}", f"gen_{args.gen}")
        if os.path.isdir(path):
            return path
        path_alt = os.path.join(base, f"{args.condition}_seed{args.seed}", f"gen_{args.gen}")
        if os.path.isdir(path_alt):
            return path_alt
        print(f"WARNING: checkpoint dir not found at {path}, falling back to base model")
    return BASE_MODEL


def load_texts(n_samples):
    """Load held-out text samples for embedding extraction."""
    from datasets import load_dataset
    try:
        ds = load_dataset("monology/pile-uncopyrighted", split="train", streaming=True)
        texts = []
        for ex in ds:
            t = ex.get("text", "")
            if len(t.strip()) > 50:
                texts.append(t[:2000])
            if len(texts) >= n_samples:
                break
        if len(texts) >= n_samples:
            return texts
    except Exception as e:
        print(f"  pile-uncopyrighted failed: {e}")

    try:
        ds = load_dataset("wikitext", "wikitext-103-raw-v1", split="test")
        texts = [t for t in ds["text"] if len(t.strip()) > 50][:n_samples]
        if len(texts) >= n_samples:
            return texts
    except Exception as e:
        print(f"  wikitext failed: {e}")

    print("  FATAL: cannot load enough held-out texts")
    sys.exit(1)


def extract_embeddings(model, tokenizer, texts, device):
    """Extract last-layer mean-pooled embeddings for all texts."""
    model.eval()
    all_emb = []
    with torch.no_grad():
        for i in range(0, len(texts), BATCH_SIZE):
            batch = texts[i:i + BATCH_SIZE]
            inputs = tokenizer(
                batch, return_tensors="pt", padding=True,
                truncation=True, max_length=MAX_LENGTH
            ).to(device)
            outputs = model(**inputs, output_hidden_states=True)
            last_hidden = outputs.hidden_states[-1]
            mask = inputs["attention_mask"].unsqueeze(-1)
            mean_emb = (last_hidden * mask).sum(dim=1) / mask.sum(dim=1)
            all_emb.append(mean_emb.cpu())
    return torch.cat(all_emb, dim=0).float()


def compute_slv(E):
    """Compute SLV = sum of log(σ_i) for σ_i > ε."""
    sv = torch.linalg.svdvals(E)
    return torch.sum(torch.log(sv[sv > EPSILON])).item()


def compute_effective_rank(E):
    """Compute effective rank from singular values."""
    sv = torch.linalg.svdvals(E)
    sv = sv[sv > EPSILON]
    p = sv / sv.sum()
    entropy = -torch.sum(p * torch.log(p)).item()
    return np.exp(entropy)


def run_sensitivity(E_pool, n_values, n_repeats, rng):
    """Run SLV computation across sample sizes with random subsampling."""
    pool_n = E_pool.shape[0]
    d = E_pool.shape[1]
    results = []

    for n in n_values:
        if n > pool_n:
            print(f"  WARNING: n={n} > pool_size={pool_n}, using full pool")
            n = pool_n

        slv_vals = []
        reff_vals = []
        n_sv_vals = []

        for rep in range(n_repeats):
            indices = rng.choice(pool_n, size=n, replace=False)
            E_sub = E_pool[indices]
            slv = compute_slv(E_sub)
            reff = compute_effective_rank(E_sub)
            n_sv = min(n, d)
            slv_vals.append(slv)
            reff_vals.append(reff)
            n_sv_vals.append(n_sv)

        results.append({
            "n": n,
            "n_singular_values": n_sv_vals[0],
            "slv_mean": float(np.mean(slv_vals)),
            "slv_std": float(np.std(slv_vals)),
            "slv_values": [float(v) for v in slv_vals],
            "reff_mean": float(np.mean(reff_vals)),
            "reff_std": float(np.std(reff_vals)),
        })
        print(f"  n={n:5d}: SLV = {np.mean(slv_vals):.2f} ± {np.std(slv_vals):.2f}  "
              f"(r_eff = {np.mean(reff_vals):.1f} ± {np.std(reff_vals):.1f}, "
              f"k={n_sv_vals[0]} SVs)")

    return results


def print_table(results, reference_n=1000):
    """Print formatted results table with relative changes."""
    ref = next((r for r in results if r["n"] == reference_n), results[0])
    ref_slv = ref["slv_mean"]

    print("\n" + "=" * 75)
    print(f"{'n':>6s}  {'k (SVs)':>7s}  {'SLV mean':>10s}  {'SLV std':>9s}  "
          f"{'Rel Δ vs n={reference_n}':>18s}  {'CV (%)':>7s}")
    print("-" * 75)
    for r in results:
        rel_delta = (r["slv_mean"] - ref_slv) / abs(ref_slv) * 100
        cv = r["slv_std"] / abs(r["slv_mean"]) * 100 if r["slv_mean"] != 0 else 0
        print(f"{r['n']:6d}  {r['n_singular_values']:7d}  {r['slv_mean']:10.2f}  "
              f"{r['slv_std']:9.2f}  {rel_delta:+17.2f}%  {cv:7.3f}")
    print("=" * 75)


def main():
    args = parse_args()
    device = f"cuda:{args.gpu}" if torch.cuda.is_available() else "cpu"
    rng = np.random.default_rng(args.seed)

    checkpoint = resolve_checkpoint(args)
    print(f"Checkpoint: {checkpoint}")
    print(f"Device: {device}")
    print(f"n values: {args.n_values}")
    print(f"Repeats per n: {args.n_repeats}")

    from transformers import AutoModelForCausalLM, AutoTokenizer

    print(f"\n--- Loading model ---")
    tokenizer = AutoTokenizer.from_pretrained(checkpoint)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    model = AutoModelForCausalLM.from_pretrained(checkpoint).to(device)
    d = model.config.hidden_size
    print(f"  hidden_size (d) = {d}")

    max_n = max(args.n_values)
    pool_size = max(max_n, POOL_SIZE)
    print(f"\n--- Loading {pool_size} text samples ---")
    texts = load_texts(pool_size)
    print(f"  Got {len(texts)} texts")

    print(f"\n--- Extracting {len(texts)} embeddings ---")
    t0 = time.time()
    E_pool = extract_embeddings(model, tokenizer, texts, device)
    t1 = time.time()
    print(f"  Embedding pool shape: {E_pool.shape} (took {t1-t0:.1f}s)")

    del model
    if device.startswith("cuda"):
        torch.cuda.empty_cache()

    print(f"\n--- Running sensitivity analysis ---")
    results = run_sensitivity(E_pool, sorted(args.n_values), args.n_repeats, rng)

    print_table(results)

    output = {
        "checkpoint": checkpoint,
        "device": device,
        "seed": args.seed,
        "n_repeats": args.n_repeats,
        "pool_size": int(E_pool.shape[0]),
        "hidden_size": d,
        "epsilon": EPSILON,
        "results": results,
    }
    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    with open(args.output, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nResults saved to {args.output}")


if __name__ == "__main__":
    main()
