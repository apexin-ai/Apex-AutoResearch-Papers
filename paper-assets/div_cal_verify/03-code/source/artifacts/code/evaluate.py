# Evaluation metrics: held-out perplexity, rare n-gram survival, RankMe, k-NN probe, rank correlation.
# Usage: python evaluate.py --model ./checkpoints/gen_0 --data_dir ./data --output ./results/gen_0/metrics.json

import argparse
import json
import os
from pathlib import Path

import numpy as np
import torch
from scipy.stats import spearmanr
from transformers import AutoTokenizer, AutoModelForCausalLM
from collections import Counter

from representation_monitor import (
    compute_rankme,
    compute_knn_probe,
    compute_diversity_scores,
    load_contriever,
)


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--model", type=str, required=True,
                   help="Path to student checkpoint or model name")
    p.add_argument("--tokenizer", type=str, default="Qwen/Qwen3-1.7B")
    p.add_argument("--data_dir", type=str, default="./data")
    p.add_argument("--synthetic_data", type=str, default=None,
                   help="Path to synthetic data .pt (for n-gram survival)")
    p.add_argument("--output", type=str, required=True)
    p.add_argument("--device", type=str, default="cuda:0")
    p.add_argument("--batch_size", type=int, default=32)
    return p.parse_args()


@torch.no_grad()
def compute_held_out_perplexity(model, test_chunks, device, batch_size=32):
    """Compute average perplexity on held-out test set."""
    model.eval()
    total_loss = 0.0
    total_tokens = 0

    for i in range(0, len(test_chunks), batch_size):
        batch = test_chunks[i:i + batch_size]
        max_len = max(len(ids) for ids in batch)
        padded = torch.zeros(len(batch), max_len, dtype=torch.long, device=device)
        mask = torch.zeros(len(batch), max_len, dtype=torch.long, device=device)
        for j, ids in enumerate(batch):
            padded[j, :len(ids)] = torch.tensor(ids, dtype=torch.long)
            mask[j, :len(ids)] = 1

        outputs = model(input_ids=padded, attention_mask=mask, labels=padded)
        shift_mask = mask[:, 1:]
        num_tokens = shift_mask.sum().item()
        total_loss += outputs.loss.item() * num_tokens
        total_tokens += num_tokens

    avg_loss = total_loss / max(total_tokens, 1)
    return float(np.exp(avg_loss))


def compute_rare_ngram_survival(reference_texts, synthetic_texts, n=3, rare_percentile=10):
    """Rare n-gram survival rate: what fraction of rare n-grams from reference appear in synthetic.

    Measures whether generative iteration preserves tail-distribution diversity.
    """
    ref_counter = Counter()
    for text in reference_texts:
        tokens = text.split()
        for i in range(len(tokens) - n + 1):
            ref_counter[tuple(tokens[i:i + n])] += 1

    if not ref_counter:
        return 0.0

    counts = sorted(ref_counter.values())
    threshold = counts[max(0, len(counts) * rare_percentile // 100)]
    rare_ngrams = {ng for ng, c in ref_counter.items() if c <= threshold}

    if not rare_ngrams:
        return 0.0

    synth_ngrams = set()
    for text in synthetic_texts:
        tokens = text.split()
        for i in range(len(tokens) - n + 1):
            synth_ngrams.add(tuple(tokens[i:i + n]))

    survived = rare_ngrams & synth_ngrams
    return len(survived) / len(rare_ngrams)


def compute_rank_correlation(model, tokenizer, candidates, device, contriever_model, batch_size=32):
    """Spearman rank correlation between model-internal and Contriever diversity scores.

    Uses L2 distance to centroid as a simple per-sample diversity proxy.
    """
    internal_emb = compute_diversity_scores(
        model, candidates, device, method="internal", batch_size=batch_size
    )
    contriever_emb = compute_diversity_scores(
        model, candidates, device, method="contriever",
        tokenizer=tokenizer, contriever_model=contriever_model, batch_size=batch_size
    )

    # per-sample diversity = L2 distance to centroid
    int_centroid = internal_emb.mean(dim=0, keepdim=True)
    int_dists = torch.norm(internal_emb - int_centroid, dim=1).numpy()

    con_centroid = contriever_emb.mean(dim=0, keepdim=True)
    con_dists = torch.norm(contriever_emb - con_centroid, dim=1).numpy()

    corr, pvalue = spearmanr(int_dists, con_dists)
    return float(corr), float(pvalue)


def main():
    args = parse_args()
    os.makedirs(os.path.dirname(args.output), exist_ok=True)

    print(f"Loading model: {args.model}")
    tokenizer = AutoTokenizer.from_pretrained(args.tokenizer, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    model = AutoModelForCausalLM.from_pretrained(
        args.model, torch_dtype=torch.bfloat16, trust_remote_code=True
    ).to(args.device).eval()

    ref_chunks = torch.load(Path(args.data_dir) / "ref_chunks.pt", weights_only=True)
    rare_labels = torch.load(Path(args.data_dir) / "ref_rare_labels.pt", weights_only=True)
    test_chunks = torch.load(Path(args.data_dir) / "test_chunks.pt", weights_only=True)

    metrics = {}

    # 1. Held-out perplexity
    print("Computing held-out perplexity...")
    metrics["held_out_perplexity"] = compute_held_out_perplexity(
        model, test_chunks, args.device, args.batch_size
    )
    print(f"  Perplexity: {metrics['held_out_perplexity']:.2f}")

    # 2. RankMe
    print("Computing RankMe...")
    metrics["rankme"] = compute_rankme(model, ref_chunks, args.device, args.batch_size)
    print(f"  RankMe: {metrics['rankme']:.2f}")

    # 3. k-NN probe
    print("Computing k-NN probe...")
    metrics["knn_probe_accuracy"] = compute_knn_probe(
        model, ref_chunks, rare_labels, args.device, batch_size=args.batch_size
    )
    print(f"  k-NN accuracy: {metrics['knn_probe_accuracy']:.4f}")

    # 4. Rare n-gram survival (if synthetic data provided)
    if args.synthetic_data and os.path.exists(args.synthetic_data):
        print("Computing rare n-gram survival...")
        ref_texts = [tokenizer.decode(c, skip_special_tokens=True) for c in ref_chunks]
        synth_ids = torch.load(args.synthetic_data, weights_only=True)
        synth_texts = [tokenizer.decode(ids, skip_special_tokens=True) for ids in synth_ids]
        metrics["rare_ngram_survival"] = compute_rare_ngram_survival(ref_texts, synth_texts)
        print(f"  Rare n-gram survival: {metrics['rare_ngram_survival']:.4f}")

    # 5. Rank correlation (internal vs Contriever)
    print("Computing rank correlation (internal vs Contriever)...")
    contriever = load_contriever(device="cpu")
    # use a subset of ref_chunks for efficiency
    subset = ref_chunks[:500]
    corr, pval = compute_rank_correlation(
        model, tokenizer, subset, args.device, contriever, args.batch_size
    )
    metrics["rank_correlation"] = corr
    metrics["rank_correlation_pvalue"] = pval
    print(f"  Rank correlation: {corr:.4f} (p={pval:.4e})")

    # Save
    with open(args.output, "w") as f:
        json.dump(metrics, f, indent=2)
    print(f"\nMetrics saved to {args.output}")


if __name__ == "__main__":
    main()
