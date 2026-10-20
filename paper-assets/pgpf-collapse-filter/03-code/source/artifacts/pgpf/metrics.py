"""Evaluation metrics for tracking model collapse across generations.

All functions return a single float.
"""

import random
from itertools import combinations

import numpy as np

try:
    import torch
except ImportError:
    torch = None


def corpus_self_bleu(samples: list[str], n: int = 4, num_pairs: int = 1000) -> float:
    """Average BLEU-4 between random pairs of samples (higher = more repetitive).

    Uses sacrebleu sentence-level BLEU. Subsamples pairs for efficiency.
    """
    import sacrebleu

    if len(samples) < 2:
        return 0.0

    if len(samples) <= 50:
        pairs = list(combinations(range(len(samples)), 2))
    else:
        pairs = [
            (random.randint(0, len(samples) - 1), random.randint(0, len(samples) - 1))
            for _ in range(num_pairs)
        ]
        pairs = [(i, j) for i, j in pairs if i != j]

    scores = []
    for i, j in pairs:
        bleu = sacrebleu.sentence_bleu(samples[i], [samples[j]])
        scores.append(bleu.score / 100.0)

    return float(np.mean(scores))


def vocab_coverage(samples: list[str], reference_vocab: set[str]) -> float:
    """Fraction of reference vocabulary present in samples.

    |vocab(samples) ∩ reference_vocab| / |reference_vocab|
    """
    if not reference_vocab:
        return 0.0
    sample_vocab = set()
    for s in samples:
        sample_vocab.update(s.split())
    return len(sample_vocab & reference_vocab) / len(reference_vocab)


def embedding_diversity(embeddings: np.ndarray, num_pairs: int = 5000) -> float:
    """Average pairwise cosine distance (higher = more diverse)."""
    n = len(embeddings)
    if n < 2:
        return 0.0

    norms = embeddings / (np.linalg.norm(embeddings, axis=1, keepdims=True) + 1e-8)

    if n <= 100:
        sim_matrix = norms @ norms.T
        mask = np.triu(np.ones((n, n), dtype=bool), k=1)
        avg_sim = sim_matrix[mask].mean()
    else:
        indices = np.random.randint(0, n, size=(num_pairs, 2))
        indices = indices[indices[:, 0] != indices[:, 1]]
        sims = np.sum(norms[indices[:, 0]] * norms[indices[:, 1]], axis=1)
        avg_sim = sims.mean()

    return float(1.0 - avg_sim)


def held_out_perplexity(
    model,
    tokenizer,
    eval_texts: list[str],
    max_length: int = 2048,
    batch_size: int = 4,
) -> float:
    """Average perplexity on held-out evaluation texts."""
    model.eval()
    total_loss = 0.0
    total_tokens = 0

    with torch.no_grad():
        for i in range(0, len(eval_texts), batch_size):
            batch_texts = eval_texts[i : i + batch_size]
            encodings = tokenizer(
                batch_texts,
                return_tensors="pt",
                truncation=True,
                max_length=max_length,
                padding=True,
            )
            input_ids = encodings.input_ids.to(model.device)
            attention_mask = encodings.attention_mask.to(model.device)

            labels = input_ids.clone()
            labels[attention_mask == 0] = -100
            outputs = model(input_ids, attention_mask=attention_mask, labels=labels)
            num_tokens = attention_mask.sum().item()
            total_loss += outputs.loss.item() * num_tokens
            total_tokens += num_tokens

    avg_loss = total_loss / max(total_tokens, 1)
    return float(np.exp(avg_loss))
