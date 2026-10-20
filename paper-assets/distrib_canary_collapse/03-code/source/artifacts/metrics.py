"""Canary and downstream metrics for model collapse detection.

Computes per-generation metrics on held-out data and generated samples.
All compute_* functions share the signature:
    (model, tokenizer, eval_dataset, gen_dataset=None, **kwargs) -> float | dict

Dependencies: torch, transformers, mauve-text, nltk
"""

import math
from collections import Counter
from itertools import combinations

import numpy as np
import torch
from nltk.translate.bleu_score import SmoothingFunction, sentence_bleu


# ---------------------------------------------------------------------------
# Text-surface metrics
# ---------------------------------------------------------------------------

def compute_token_entropy(model, tokenizer, eval_dataset, gen_dataset=None,
                          max_samples=512, max_length=256, batch_size=8):
    """Mean next-token entropy of `model` on `eval_dataset` (held-out real text).

    Lower entropy over generations signals the model is becoming overly
    confident / less diverse — a collapse canary.
    """
    model.eval()
    device = next(model.parameters()).device
    total_entropy = 0.0
    total_tokens = 0

    texts = eval_dataset["text"][:max_samples]
    for i in range(0, len(texts), batch_size):
        batch_texts = texts[i:i + batch_size]
        enc = tokenizer(batch_texts, return_tensors="pt", truncation=True,
                        max_length=max_length, padding=True)
        input_ids = enc["input_ids"].to(device)
        attention_mask = enc["attention_mask"].to(device)

        with torch.no_grad():
            logits = model(input_ids=input_ids, attention_mask=attention_mask).logits

        # shift: predict token t+1 from position t
        shift_logits = logits[:, :-1, :]
        shift_mask = attention_mask[:, 1:]

        log_probs = torch.log_softmax(shift_logits, dim=-1)
        probs = torch.exp(log_probs)
        token_entropy = -(probs * log_probs).sum(dim=-1)  # (B, T-1)

        masked_entropy = (token_entropy * shift_mask).sum()
        total_entropy += masked_entropy.item()
        total_tokens += shift_mask.sum().item()

    return total_entropy / max(total_tokens, 1)


def compute_self_bleu(model, tokenizer, eval_dataset, gen_dataset=None,
                      max_samples=200, sample_pairs=500):
    """Self-BLEU among generated samples — higher means less diversity.

    Uses `gen_dataset["text"]`. Falls back to `eval_dataset` if gen_dataset
    is None (useful for baseline measurement on real data).
    """
    src = gen_dataset if gen_dataset is not None else eval_dataset
    texts = src["text"][:max_samples]
    tokenized = [tokenizer.tokenize(t)[:128] for t in texts if len(t.strip()) > 0]

    if len(tokenized) < 2:
        return 0.0

    smoother = SmoothingFunction().method1
    n_pairs = min(sample_pairs, len(tokenized) * (len(tokenized) - 1) // 2)

    rng = np.random.RandomState(0)
    indices = list(range(len(tokenized)))
    scores = []
    for _ in range(n_pairs):
        i, j = rng.choice(indices, size=2, replace=False)
        score = sentence_bleu([tokenized[i]], tokenized[j],
                              weights=(0.25, 0.25, 0.25, 0.25),
                              smoothing_function=smoother)
        scores.append(score)

    return float(np.mean(scores))


def compute_distinct_n(model, tokenizer, eval_dataset, gen_dataset=None,
                       max_samples=500, ns=(1, 2, 3)):
    """Distinct-n: ratio of unique n-grams to total n-grams in generated text.

    Returns dict {"distinct_1": ..., "distinct_2": ..., "distinct_3": ...}.
    """
    src = gen_dataset if gen_dataset is not None else eval_dataset
    texts = src["text"][:max_samples]
    all_tokens = []
    for t in texts:
        all_tokens.extend(tokenizer.tokenize(t)[:256])

    result = {}
    for n in ns:
        ngrams = [tuple(all_tokens[i:i + n]) for i in range(len(all_tokens) - n + 1)]
        if len(ngrams) == 0:
            result[f"distinct_{n}"] = 0.0
        else:
            result[f"distinct_{n}"] = len(set(ngrams)) / len(ngrams)
    return result


# ---------------------------------------------------------------------------
# Calibration metrics
# ---------------------------------------------------------------------------

def compute_ece(model, tokenizer, eval_dataset, gen_dataset=None,
                max_samples=512, max_length=256, n_bins=10, batch_size=8):
    """Expected Calibration Error on held-out eval_dataset.

    Measures whether the model's confidence matches its accuracy at the
    token level. Rising ECE is a collapse canary (overconfidence).
    """
    model.eval()
    device = next(model.parameters()).device

    confidences = []
    accuracies = []

    texts = eval_dataset["text"][:max_samples]
    for i in range(0, len(texts), batch_size):
        batch_texts = texts[i:i + batch_size]
        enc = tokenizer(batch_texts, return_tensors="pt", truncation=True,
                        max_length=max_length, padding=True)
        input_ids = enc["input_ids"].to(device)
        attention_mask = enc["attention_mask"].to(device)

        with torch.no_grad():
            logits = model(input_ids=input_ids, attention_mask=attention_mask).logits

        shift_logits = logits[:, :-1, :]
        shift_labels = input_ids[:, 1:]
        shift_mask = attention_mask[:, 1:]

        probs = torch.softmax(shift_logits, dim=-1)
        max_probs, preds = probs.max(dim=-1)

        mask_flat = shift_mask.bool().flatten()
        confidences.append(max_probs.flatten()[mask_flat].cpu())
        accuracies.append((preds == shift_labels).flatten()[mask_flat].cpu().float())

    confidences = torch.cat(confidences)
    accuracies = torch.cat(accuracies)

    bin_boundaries = torch.linspace(0, 1, n_bins + 1)
    ece = 0.0
    for b in range(n_bins):
        mask = (confidences > bin_boundaries[b]) & (confidences <= bin_boundaries[b + 1])
        if mask.sum() == 0:
            continue
        bin_acc = accuracies[mask].mean()
        bin_conf = confidences[mask].mean()
        ece += mask.sum().item() / len(confidences) * abs(bin_acc - bin_conf).item()

    return ece


# ---------------------------------------------------------------------------
# Spectral metrics
# ---------------------------------------------------------------------------

def compute_effective_rank(model, tokenizer, eval_dataset, gen_dataset=None,
                           max_samples=256, max_length=256, batch_size=8):
    """Effective rank of last-layer hidden state covariance matrix.

    effective_rank = exp(entropy of normalized eigenvalues)
    Declining effective rank signals representation collapse.
    """
    model.eval()
    device = next(model.parameters()).device
    all_hidden = []

    texts = eval_dataset["text"][:max_samples]
    for i in range(0, len(texts), batch_size):
        batch_texts = texts[i:i + batch_size]
        enc = tokenizer(batch_texts, return_tensors="pt", truncation=True,
                        max_length=max_length, padding=True)
        input_ids = enc["input_ids"].to(device)
        attention_mask = enc["attention_mask"].to(device)

        with torch.no_grad():
            outputs = model(input_ids=input_ids, attention_mask=attention_mask,
                            output_hidden_states=True)
        last_hidden = outputs.hidden_states[-1]  # (B, T, D)

        # take mean-pooled representation per sample
        mask_expanded = attention_mask.unsqueeze(-1).float()
        pooled = (last_hidden * mask_expanded).sum(dim=1) / mask_expanded.sum(dim=1)
        all_hidden.append(pooled.cpu().float())

    H = torch.cat(all_hidden, dim=0).numpy()  # (N, D)
    if np.isnan(H).any() or np.isinf(H).any():
        return float('nan')
    H = H - H.mean(axis=0, keepdims=True)
    cov = np.cov(H, rowvar=False)
    try:
        eigenvalues = np.linalg.eigvalsh(cov)
    except np.linalg.LinAlgError:
        _, s, _ = np.linalg.svd(cov, full_matrices=False)
        eigenvalues = s
    eigenvalues = eigenvalues[eigenvalues > 1e-12]
    if len(eigenvalues) == 0:
        return float('nan')

    # normalized eigenvalue distribution
    p = eigenvalues / eigenvalues.sum()
    entropy = -np.sum(p * np.log(p))
    return float(np.exp(entropy))


# ---------------------------------------------------------------------------
# Downstream metrics
# ---------------------------------------------------------------------------

def compute_perplexity(model, tokenizer, eval_dataset, gen_dataset=None,
                       max_samples=512, max_length=256, batch_size=8):
    """Perplexity on held-out real data. The primary collapse indicator."""
    model.eval()
    device = next(model.parameters()).device
    total_loss = 0.0
    total_tokens = 0

    texts = eval_dataset["text"][:max_samples]
    for i in range(0, len(texts), batch_size):
        batch_texts = texts[i:i + batch_size]
        enc = tokenizer(batch_texts, return_tensors="pt", truncation=True,
                        max_length=max_length, padding=True)
        input_ids = enc["input_ids"].to(device)
        attention_mask = enc["attention_mask"].to(device)

        labels = input_ids.clone()
        labels[attention_mask == 0] = -100

        with torch.no_grad():
            outputs = model(input_ids=input_ids, attention_mask=attention_mask,
                            labels=labels)

        shift_mask = attention_mask[:, 1:]
        n_tokens = shift_mask.sum().item()

        # outputs.loss is mean over all non-ignored tokens
        total_loss += outputs.loss.item() * n_tokens
        total_tokens += n_tokens

    return float(math.exp(total_loss / max(total_tokens, 1)))


def compute_mauve(model, tokenizer, eval_dataset, gen_dataset=None,
                  max_samples=2000, max_length=256):
    """MAUVE score between real (eval_dataset) and generated (gen_dataset) text.

    MAUVE ∈ [0, 1]; higher = generated distribution closer to real.
    Declining MAUVE is a downstream collapse signal.
    """
    import mauve as mauve_pkg

    real_texts = eval_dataset["text"][:max_samples]
    real_texts = [t[:max_length * 4] for t in real_texts if len(t.strip()) > 0]

    if gen_dataset is None:
        return 1.0  # no generated data to compare

    gen_texts = gen_dataset["text"][:max_samples]
    gen_texts = [t[:max_length * 4] for t in gen_texts if len(t.strip()) > 0]

    if len(gen_texts) == 0:
        return 0.0

    # use the same number of samples for fair comparison
    n = min(len(real_texts), len(gen_texts))
    result = mauve_pkg.compute_mauve(
        p_text=real_texts[:n],
        q_text=gen_texts[:n],
        device_id=torch.cuda.current_device() if torch.cuda.is_available() else -1,
        max_text_length=max_length,
        verbose=False,
    )
    return float(result.mauve)


# ---------------------------------------------------------------------------
# Convenience: compute all metrics at once
# ---------------------------------------------------------------------------

def compute_all_metrics(model, tokenizer, eval_dataset, gen_dataset=None,
                        **kwargs):
    """Compute every metric and return a flat dict.

    Args:
        model: HuggingFace causal LM.
        tokenizer: Corresponding tokenizer.
        eval_dataset: Held-out real data split (must have "text" column).
        gen_dataset: Generated/synthetic data (must have "text" column).
        **kwargs: Forwarded to individual metric functions.

    Returns:
        dict with keys: token_entropy, self_bleu, distinct_1/2/3, ece,
        effective_rank, perplexity, mauve.
    """
    results = {}

    results["token_entropy"] = compute_token_entropy(
        model, tokenizer, eval_dataset, gen_dataset, **kwargs)

    results["self_bleu"] = compute_self_bleu(
        model, tokenizer, eval_dataset, gen_dataset, **kwargs)

    distinct = compute_distinct_n(
        model, tokenizer, eval_dataset, gen_dataset, **kwargs)
    results.update(distinct)

    results["ece"] = compute_ece(
        model, tokenizer, eval_dataset, gen_dataset, **kwargs)

    results["effective_rank"] = compute_effective_rank(
        model, tokenizer, eval_dataset, gen_dataset, **kwargs)

    results["perplexity"] = compute_perplexity(
        model, tokenizer, eval_dataset, gen_dataset, **kwargs)

    try:
        results["mauve"] = compute_mauve(
            model, tokenizer, eval_dataset, gen_dataset, **kwargs)
    except Exception as e:
        print(f"  [WARN] MAUVE skipped: {e}")
        results["mauve"] = float("nan")

    return results
