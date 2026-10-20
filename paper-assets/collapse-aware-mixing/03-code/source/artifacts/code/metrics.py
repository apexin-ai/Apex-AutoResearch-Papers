"""Collapse-detection metrics for the pilot experiment.

Six metrics computed at each training checkpoint:
1. Spectral effective rank (core hypothesis)
2. Token-level prediction entropy variance
3. N-gram entropy (uni/bi/trigram)
4. Vocabulary coverage
5. Perplexity on held-out real data
6. Inter-generational KL divergence (unigram approximation)
"""

import math
import logging
from collections import Counter
from typing import Dict, List, Optional

import numpy as np
import torch
import torch.nn.functional as F
from torch.utils.data import DataLoader
from tqdm import tqdm

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# 1. Spectral effective rank
# ---------------------------------------------------------------------------

def compute_spectral_effective_rank(
    model: torch.nn.Module,
    dataloader: DataLoader,
    num_samples: int = 50_000,
    device: str = "cuda",
) -> Dict[str, float]:
    """RankMe-style effective rank from final-layer hidden states.

    Collects mean-pooled hidden states E (N x d), computes singular values,
    normalises to a distribution p, and returns exp(H(p)).
    """
    model.eval()
    hidden_list = []
    collected = 0

    with torch.no_grad():
        for batch in tqdm(dataloader, desc="spectral-rank", leave=False):
            if collected >= num_samples:
                break
            input_ids = batch["input_ids"].to(device)
            attn_mask = batch["attention_mask"].to(device)

            out = model(input_ids=input_ids, attention_mask=attn_mask, output_hidden_states=True)
            # final-layer hidden: (B, L, D)
            h = out.hidden_states[-1].float()

            # mean-pool over sequence (mask-aware)
            mask = attn_mask.unsqueeze(-1).float()
            pooled = (h * mask).sum(1) / mask.sum(1).clamp(min=1)  # (B, D)
            hidden_list.append(pooled.cpu())
            collected += pooled.shape[0]

    E = torch.cat(hidden_list, dim=0)[:num_samples]  # (N, D)
    sigma = torch.linalg.svdvals(E)                   # descending

    # normalise to probability distribution
    sigma_pos = sigma[sigma > 0]
    p = sigma_pos / sigma_pos.sum()
    entropy = -(p * p.log()).sum().item()
    eff_rank = math.exp(entropy)

    return {
        "spectral_effective_rank": eff_rank,
        "spectral_entropy": entropy,
        "top_singular_value": sigma[0].item(),
        "sigma_ratio_top_bottom": (sigma[0] / sigma_pos[-1]).item(),
        "spectral_num_samples": int(E.shape[0]),
    }


# ---------------------------------------------------------------------------
# 2. Token-level prediction entropy variance
# ---------------------------------------------------------------------------

def compute_token_entropy_variance(
    model: torch.nn.Module,
    dataloader: DataLoader,
    num_samples: int = 10_000,
    device: str = "cuda",
) -> Dict[str, float]:
    """Per-token next-token entropy, report mean and variance across all tokens."""
    model.eval()
    entropies = []
    seen = 0

    with torch.no_grad():
        for batch in tqdm(dataloader, desc="token-entropy", leave=False):
            if seen >= num_samples:
                break
            input_ids = batch["input_ids"].to(device)
            attn_mask = batch["attention_mask"].to(device)

            logits = model(input_ids=input_ids, attention_mask=attn_mask).logits
            # shift: predict position t+1 from position t
            logits = logits[:, :-1, :]
            mask = attn_mask[:, 1:].bool()

            log_p = F.log_softmax(logits, dim=-1)
            p = log_p.exp()
            ent = -(p * log_p).sum(dim=-1)  # (B, L-1)

            for i in range(ent.shape[0]):
                entropies.append(ent[i][mask[i]].cpu())
            seen += input_ids.shape[0]

    all_ent = torch.cat(entropies).float()
    return {
        "token_entropy_mean": all_ent.mean().item(),
        "token_entropy_var": all_ent.var().item(),
        "token_entropy_std": all_ent.std().item(),
        "token_entropy_num_tokens": int(all_ent.shape[0]),
    }


# ---------------------------------------------------------------------------
# 3. N-gram entropy
# ---------------------------------------------------------------------------

def compute_ngram_entropy(token_ids: List[int], max_n: int = 3) -> Dict[str, float]:
    """Shannon entropy of unigram / bigram / trigram distributions."""
    label = {1: "unigram", 2: "bigram", 3: "trigram"}
    results: Dict[str, float] = {}
    for n in range(1, max_n + 1):
        counter: Counter = Counter()
        for i in range(len(token_ids) - n + 1):
            counter[tuple(token_ids[i : i + n])] += 1
        total = sum(counter.values())
        entropy = -sum((c / total) * math.log(c / total) for c in counter.values())
        results[f"{label[n]}_entropy"] = entropy
        results[f"{label[n]}_unique"] = len(counter)
    return results


# ---------------------------------------------------------------------------
# 4. Vocabulary coverage
# ---------------------------------------------------------------------------

def compute_vocab_coverage(token_ids: List[int], vocab_size: int) -> Dict[str, float]:
    unique = len(set(token_ids))
    return {
        "vocab_coverage": unique / vocab_size,
        "unique_tokens": unique,
        "total_tokens": len(token_ids),
    }


# ---------------------------------------------------------------------------
# 5. Perplexity
# ---------------------------------------------------------------------------

def compute_perplexity(
    model: torch.nn.Module,
    dataloader: DataLoader,
    num_samples: int = 5_000,
    device: str = "cuda",
) -> Dict[str, float]:
    """Standard perplexity on held-out data."""
    model.eval()
    total_loss = 0.0
    total_tokens = 0
    seen = 0

    with torch.no_grad():
        for batch in tqdm(dataloader, desc="perplexity", leave=False):
            if seen >= num_samples:
                break
            input_ids = batch["input_ids"].to(device)
            attn_mask = batch["attention_mask"].to(device)
            labels = input_ids.clone()
            labels[attn_mask == 0] = -100

            loss = model(input_ids=input_ids, attention_mask=attn_mask, labels=labels).loss
            n_tok = (labels[:, 1:] != -100).sum().item()
            total_loss += loss.item() * n_tok
            total_tokens += n_tok
            seen += input_ids.shape[0]

    avg_loss = total_loss / max(total_tokens, 1)
    return {
        "perplexity": math.exp(avg_loss),
        "avg_loss": avg_loss,
        "ppl_num_tokens": total_tokens,
    }


# ---------------------------------------------------------------------------
# 6. Inter-generational KL divergence (full distribution report)
# ---------------------------------------------------------------------------

def _unigram_dist(ids: np.ndarray, vocab_size: int, smoothing: float = 1e-8) -> np.ndarray:
    c = np.bincount(ids, minlength=vocab_size).astype(np.float64)
    c += smoothing
    return c / c.sum()


def _bigram_kl(ids_a: List[int], ids_b: List[int], smoothing: float = 1e-8) -> float:
    """KL(P_a || P_b) over bigram distributions (sparse, observed-support only)."""
    ca: Counter = Counter(zip(ids_a[:-1], ids_a[1:]))
    cb: Counter = Counter(zip(ids_b[:-1], ids_b[1:]))
    all_bg = set(ca) | set(cb)
    n_bg = len(all_bg)
    total_a = sum(ca.values()) + smoothing * n_bg
    total_b = sum(cb.values()) + smoothing * n_bg
    kl = 0.0
    for bg in all_bg:
        pa = (ca.get(bg, 0) + smoothing) / total_a
        pb = (cb.get(bg, 0) + smoothing) / total_b
        kl += pa * math.log(pa / pb)
    return kl


def compute_kl_divergence(
    ids_a: List[int],
    ids_b: List[int],
    vocab_size: int,
    smoothing: float = 1e-8,
    n_bootstrap: int = 1000,
    ci_level: float = 0.95,
) -> Dict[str, float]:
    """Full KL divergence report.

    Returns unigram KL, bigram KL, frequency-binned KL contributions
    (high/mid/low-freq tokens), and bootstrap 95% CI on unigram KL.
    """
    arr_a = np.array(ids_a, dtype=np.int64)
    arr_b = np.array(ids_b, dtype=np.int64)

    # Token IDs from generation may exceed tokenizer vocab_size (added tokens).
    effective_vocab = max(vocab_size, int(arr_a.max()) + 1, int(arr_b.max()) + 1)

    # --- Unigram KL ---
    p = _unigram_dist(arr_a, effective_vocab, smoothing)
    q = _unigram_dist(arr_b, effective_vocab, smoothing)
    per_token_kl = p * np.log(p / q)
    kl_unigram = float(per_token_kl.sum())
    kl_reverse = float((q * np.log(q / p)).sum())
    js = 0.5 * (kl_unigram + kl_reverse)

    # --- Bigram KL ---
    kl_bigram = _bigram_kl(ids_a, ids_b, smoothing)

    # --- Frequency-binned KL (based on reference corpus ids_a) ---
    counts_a = np.bincount(arr_a, minlength=effective_vocab)
    ranked = np.argsort(-counts_a)
    n_nonzero = int((counts_a[ranked] > 0).sum())
    cut_high = max(1, n_nonzero // 100)         # top 1% of token types
    cut_mid = max(cut_high + 1, n_nonzero // 5)  # top 20%

    kl_freq_high = float(per_token_kl[ranked[:cut_high]].sum())
    kl_freq_mid = float(per_token_kl[ranked[cut_high:cut_mid]].sum())
    kl_freq_low = float(per_token_kl[ranked[cut_mid:]].sum())

    # --- Bootstrap CI on unigram KL ---
    rng = np.random.default_rng(42)
    sub_n = min(1_000_000, len(arr_a), len(arr_b))
    boot_kls = np.empty(n_bootstrap)
    for i in range(n_bootstrap):
        sa = rng.choice(arr_a, size=sub_n, replace=True)
        sb = rng.choice(arr_b, size=sub_n, replace=True)
        bp = np.bincount(sa, minlength=effective_vocab).astype(np.float64) + smoothing
        bq = np.bincount(sb, minlength=effective_vocab).astype(np.float64) + smoothing
        bp /= bp.sum()
        bq /= bq.sum()
        boot_kls[i] = (bp * np.log(bp / bq)).sum()

    alpha = (1 - ci_level) / 2
    ci_lo = float(np.percentile(boot_kls, alpha * 100))
    ci_hi = float(np.percentile(boot_kls, (1 - alpha) * 100))

    return {
        "kl_unigram": kl_unigram,
        "kl_unigram_reverse": kl_reverse,
        "js_divergence": js,
        "kl_bigram": kl_bigram,
        "kl_freq_high": kl_freq_high,
        "kl_freq_mid": kl_freq_mid,
        "kl_freq_low": kl_freq_low,
        "kl_ci_lower_95": ci_lo,
        "kl_ci_upper_95": ci_hi,
        "kl_bootstrap_mean": float(boot_kls.mean()),
        "kl_bootstrap_std": float(boot_kls.std()),
        "kl_freq_high_ntypes": int(cut_high),
        "kl_freq_mid_ntypes": int(cut_mid - cut_high),
        "kl_freq_low_ntypes": int(max(0, n_nonzero - cut_mid)),
        "kl_ci_note": "token-level i.i.d. bootstrap; CI may be anti-conservative due to sequential dependence",
    }


# ---------------------------------------------------------------------------
# Orchestrator: all metrics for one checkpoint
# ---------------------------------------------------------------------------

def compute_checkpoint_metrics(
    model: torch.nn.Module,
    holdout_loader: DataLoader,
    gen_token_ids: List[int],
    prev_gen_token_ids: Optional[List[int]],
    vocab_size: int,
    config,
    device: str = "cuda",
) -> Dict[str, float]:
    """Compute all six metric groups for a single checkpoint."""
    results: Dict[str, float] = {}

    logger.info("Computing spectral effective rank ...")
    results.update(compute_spectral_effective_rank(
        model, holdout_loader, num_samples=config.spectral_num_samples, device=device
    ))

    logger.info("Computing token entropy variance ...")
    results.update(compute_token_entropy_variance(
        model, holdout_loader, num_samples=config.ppl_num_samples, device=device
    ))

    logger.info("Computing perplexity ...")
    results.update(compute_perplexity(
        model, holdout_loader, num_samples=config.ppl_num_samples, device=device
    ))

    logger.info("Computing n-gram entropy & vocab coverage ...")
    results.update(compute_ngram_entropy(gen_token_ids))
    results.update(compute_vocab_coverage(gen_token_ids, vocab_size))

    if prev_gen_token_ids is not None:
        logger.info("Computing KL divergence (full report) ...")
        results.update(compute_kl_divergence(prev_gen_token_ids, gen_token_ids, vocab_size))

    return results
