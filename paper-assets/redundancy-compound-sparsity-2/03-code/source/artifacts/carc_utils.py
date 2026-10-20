"""
CARC shared utilities: EMA anchors (per-head and concatenated), Welford variance,
TEAL sparsify, data loading (C4/wikitext/alpaca + MATH-500), statistical helpers.

Used by carc_calibrate.py and carc_mvp.py.
Dependencies: torch, datasets, numpy
"""

import math
from typing import Dict, List, Optional

import numpy as np
import torch
import torch.nn.functional as F


# ---------------------------------------------------------------------------
# Welford online variance
# ---------------------------------------------------------------------------

class WelfordVariance:
    """Online running variance via Welford's algorithm."""

    def __init__(self):
        self.count = 0
        self.mean = 0.0
        self.M2 = 0.0

    def update(self, value: float):
        self.count += 1
        delta = value - self.mean
        self.mean += delta / self.count
        delta2 = value - self.mean
        self.M2 += delta * delta2

    @property
    def variance(self) -> float:
        # Return 1.0 when insufficient data to avoid division-by-zero;
        # yields alpha=0.5 (equal K/V weighting) at sequence start.
        if self.count < 2:
            return 1.0
        return self.M2 / (self.count - 1)


# ---------------------------------------------------------------------------
# EMA anchor manager
# ---------------------------------------------------------------------------

class EMAAnchorManager:
    """
    Per-layer EMA anchors for K/V with variance-aware weighting.

    Supports two modes:
      - per_head=True:  per-head cosine similarity with variance-aware head weighting (GQA)
      - per_head=False: concatenated K/V vectors (legacy)

    Must be reset between sequences.
    """

    def __init__(self, gamma: float = 0.9, num_kv_heads: Optional[int] = None,
                 per_head: bool = True, enable_reset: bool = False,
                 window_size: int = 16, tau_reset: float = 0.3,
                 n_reset: int = 5):
        self.gamma = gamma
        self.num_kv_heads = num_kv_heads
        self.per_head = per_head and num_kv_heads is not None
        self.enable_reset = enable_reset
        self.window_size = window_size
        self.tau_reset = tau_reset
        self.n_reset = n_reset
        self.state: Dict[int, dict] = {}

    def reset(self):
        """Clear all layer states. Call at the start of each new sequence."""
        self.state.clear()

    def compute_scores(
        self, layer_idx: int, k: torch.Tensor, v: torch.Tensor
    ) -> torch.Tensor:
        if self.per_head:
            return self._compute_scores_per_head(layer_idx, k, v)
        return self._compute_scores_concat(layer_idx, k, v)

    def _init_reset_state_concat(self, st: dict, batch: int, dim: int, device):
        """Initialize windowed reset buffers for concatenated mode."""
        W = self.window_size
        st["k_buffer"] = torch.zeros(W, batch, dim, device=device, dtype=torch.float32)
        st["v_buffer"] = torch.zeros(W, batch, dim, device=device, dtype=torch.float32)
        st["buffer_ptr"] = 0
        st["buffer_count"] = 0
        st["low_score_streak"] = 0

    def _compute_scores_concat(
        self, layer_idx: int, k: torch.Tensor, v: torch.Tensor
    ) -> torch.Tensor:
        """Original concatenated-vector implementation."""
        batch, seq_len, dim = k.shape
        scores = torch.zeros(batch, seq_len, device=k.device, dtype=torch.float32)

        if layer_idx not in self.state:
            self.state[layer_idx] = {
                "anchor_k": k[:, 0, :].float().clone(),
                "anchor_v": v[:, 0, :].float().clone(),
                "welf_k": WelfordVariance(),
                "welf_v": WelfordVariance(),
            }
            if self.enable_reset:
                self._init_reset_state_concat(
                    self.state[layer_idx], batch, dim, k.device
                )

        st = self.state[layer_idx]

        for t in range(seq_len):
            kt = k[:, t, :].float()
            vt = v[:, t, :].float()

            cos_k = F.cosine_similarity(kt, st["anchor_k"], dim=-1)
            cos_v = F.cosine_similarity(vt, st["anchor_v"], dim=-1)

            st["welf_k"].update(cos_k.mean().item())
            st["welf_v"].update(cos_v.mean().item())

            var_k = st["welf_k"].variance
            var_v = st["welf_v"].variance
            inv_k = 1.0 / max(var_k, 1e-8)
            inv_v = 1.0 / max(var_v, 1e-8)
            alpha = inv_v / (inv_k + inv_v)

            score_t = alpha * cos_k + (1.0 - alpha) * cos_v
            scores[:, t] = score_t

            st["anchor_k"] = self.gamma * st["anchor_k"] + (1.0 - self.gamma) * kt
            st["anchor_v"] = self.gamma * st["anchor_v"] + (1.0 - self.gamma) * vt

            if self.enable_reset:
                # Write to circular buffer
                ptr = st["buffer_ptr"]
                st["k_buffer"][ptr] = kt
                st["v_buffer"][ptr] = vt
                st["buffer_ptr"] = (ptr + 1) % self.window_size
                st["buffer_count"] = min(st["buffer_count"] + 1, self.window_size)

                # Track consecutive low-score tokens
                mean_score = score_t.mean().item()
                if mean_score < self.tau_reset:
                    st["low_score_streak"] += 1
                else:
                    st["low_score_streak"] = 0

                # Reset anchor from sliding window when dilution detected
                if (st["low_score_streak"] >= self.n_reset
                        and st["buffer_count"] >= self.window_size):
                    n_valid = st["buffer_count"]
                    st["anchor_k"] = st["k_buffer"][:n_valid].mean(dim=0)
                    st["anchor_v"] = st["v_buffer"][:n_valid].mean(dim=0)
                    st["low_score_streak"] = 0
                    st["welf_k"] = WelfordVariance()
                    st["welf_v"] = WelfordVariance()

        return scores

    def _init_reset_state_per_head(self, st: dict, batch: int, H: int,
                                   head_dim: int, device):
        """Initialize windowed reset buffers for per-head mode."""
        W = self.window_size
        st["k_buffer"] = torch.zeros(W, batch, H, head_dim, device=device,
                                     dtype=torch.float32)
        st["v_buffer"] = torch.zeros(W, batch, H, head_dim, device=device,
                                     dtype=torch.float32)
        st["buffer_ptr"] = 0
        st["buffer_count"] = 0
        st["low_score_streak"] = 0

    def _compute_scores_per_head(
        self, layer_idx: int, k: torch.Tensor, v: torch.Tensor
    ) -> torch.Tensor:
        """Per-head cosine similarity with variance-aware head weighting."""
        batch, seq_len, dim = k.shape
        H = self.num_kv_heads
        head_dim = dim // H
        k_h = k.view(batch, seq_len, H, head_dim)
        v_h = v.view(batch, seq_len, H, head_dim)

        scores = torch.zeros(batch, seq_len, device=k.device, dtype=torch.float32)

        if layer_idx not in self.state:
            self.state[layer_idx] = {
                "anchor_k": k_h[:, 0, :, :].float().clone(),  # (batch, H, head_dim)
                "anchor_v": v_h[:, 0, :, :].float().clone(),
                "welf_k": [WelfordVariance() for _ in range(H)],
                "welf_v": [WelfordVariance() for _ in range(H)],
            }
            if self.enable_reset:
                self._init_reset_state_per_head(
                    self.state[layer_idx], batch, H, head_dim, k.device
                )

        st = self.state[layer_idx]

        for t in range(seq_len):
            kt = k_h[:, t, :, :].float()  # (batch, H, head_dim)
            vt = v_h[:, t, :, :].float()

            cos_k = F.cosine_similarity(kt, st["anchor_k"], dim=-1)  # (batch, H)
            cos_v = F.cosine_similarity(vt, st["anchor_v"], dim=-1)

            head_scores = torch.zeros(batch, H, device=k.device)
            head_weights = torch.zeros(H, device=k.device)

            for h in range(H):
                st["welf_k"][h].update(cos_k[:, h].mean().item())
                st["welf_v"][h].update(cos_v[:, h].mean().item())

                var_k = st["welf_k"][h].variance
                var_v = st["welf_v"][h].variance
                inv_k = 1.0 / max(var_k, 1e-8)
                inv_v = 1.0 / max(var_v, 1e-8)
                alpha_h = inv_v / (inv_k + inv_v)

                head_scores[:, h] = alpha_h * cos_k[:, h] + (1.0 - alpha_h) * cos_v[:, h]
                total_var = var_k + var_v
                head_weights[h] = 1.0 / max(total_var, 1e-8)

            head_weights = head_weights / head_weights.sum()
            score_t = (head_scores * head_weights.unsqueeze(0)).sum(dim=-1)
            scores[:, t] = score_t

            st["anchor_k"] = self.gamma * st["anchor_k"] + (1.0 - self.gamma) * kt
            st["anchor_v"] = self.gamma * st["anchor_v"] + (1.0 - self.gamma) * vt

            if self.enable_reset:
                ptr = st["buffer_ptr"]
                st["k_buffer"][ptr] = kt
                st["v_buffer"][ptr] = vt
                st["buffer_ptr"] = (ptr + 1) % self.window_size
                st["buffer_count"] = min(st["buffer_count"] + 1, self.window_size)

                mean_score = score_t.mean().item()
                if mean_score < self.tau_reset:
                    st["low_score_streak"] += 1
                else:
                    st["low_score_streak"] = 0

                # Reset anchor from sliding window when dilution detected
                if (st["low_score_streak"] >= self.n_reset
                        and st["buffer_count"] >= self.window_size):
                    n_valid = st["buffer_count"]
                    st["anchor_k"] = st["k_buffer"][:n_valid].mean(dim=0)
                    st["anchor_v"] = st["v_buffer"][:n_valid].mean(dim=0)
                    st["low_score_streak"] = 0
                    st["welf_k"] = [WelfordVariance() for _ in range(H)]
                    st["welf_v"] = [WelfordVariance() for _ in range(H)]

        return scores


# ---------------------------------------------------------------------------
# TEAL sparsify
# ---------------------------------------------------------------------------

def sparsify(x: torch.Tensor, threshold: float) -> torch.Tensor:
    """TEAL magnitude-based activation pruning: zero out elements where |x| <= threshold."""
    return x.abs().gt(threshold) * x


# ---------------------------------------------------------------------------
# Perturbation
# ---------------------------------------------------------------------------

def compute_perturbation(
    output_sparse: torch.Tensor, output_base: torch.Tensor, eps: float = 1e-8
) -> torch.Tensor:
    """
    Per-token relative perturbation: ||O_sparse - O_base||_2 / ||O_base||_2.

    Args:
        output_sparse: (batch, seq_len, dim)
        output_base:   (batch, seq_len, dim)

    Returns:
        (batch, seq_len) perturbation fractions.
    """
    diff_norm = (output_sparse - output_base).float().norm(dim=-1)
    base_norm = output_base.float().norm(dim=-1).clamp(min=eps)
    return diff_norm / base_norm


# ---------------------------------------------------------------------------
# Histogram → threshold
# ---------------------------------------------------------------------------

def threshold_from_histogram(
    counts: torch.Tensor, bin_edges: torch.Tensor, sparsity: float
) -> float:
    """
    Compute activation magnitude threshold from an absolute-value histogram.

    Finds t such that `sparsity` fraction of |activations| <= t
    (the sparsity-th percentile of the |x| distribution).
    Uses linear interpolation within the target bin.
    """
    cdf = counts.cumsum(0).double()
    total = cdf[-1].item()
    if total == 0:
        return 0.0
    cdf = cdf / total

    idx = torch.searchsorted(cdf, sparsity).item()
    idx = min(idx, len(bin_edges) - 2)

    cdf_lo = cdf[idx - 1].item() if idx > 0 else 0.0
    cdf_hi = cdf[idx].item()
    edge_lo = bin_edges[idx].item()
    edge_hi = bin_edges[idx + 1].item()

    if cdf_hi - cdf_lo < 1e-10:
        return edge_hi
    frac = (sparsity - cdf_lo) / (cdf_hi - cdf_lo)
    return edge_lo + frac * (edge_hi - edge_lo)


# ---------------------------------------------------------------------------
# Statistical helpers
# ---------------------------------------------------------------------------

def residualize(x: np.ndarray, z: np.ndarray) -> np.ndarray:
    """Regress x on z (with intercept), return residuals."""
    z_aug = np.column_stack([z, np.ones(len(z))])
    beta = np.linalg.lstsq(z_aug, x, rcond=None)[0]
    return x - z_aug @ beta


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------

def load_math_data(num_problems: int = 60, seed: int = 42) -> List[str]:
    """
    Load MATH competition problems and format as CoT prompts.

    Returns list of prompt strings (not tokenized).
    """
    from datasets import load_dataset

    ds = load_dataset("hendrycks/competition_math", split="test", trust_remote_code=True)
    rng = np.random.RandomState(seed)
    indices = rng.choice(len(ds), size=min(num_problems, len(ds)), replace=False)

    prompts = []
    for idx in indices:
        item = ds[int(idx)]
        problem = item["problem"]
        prompt = (
            f"Solve the following math problem step by step. "
            f"Show your complete reasoning.\n\n"
            f"Problem: {problem}\n\n"
            f"Solution: Let me think through this carefully.\n"
        )
        prompts.append(prompt)
    return prompts


def load_eval_data(
    dataset_name: str = "c4",
    num_samples: int = 100,
    seq_len: int = 2048,
    tokenizer=None,
    split: str = "validation",
    seed: int = 42,
) -> List[torch.Tensor]:
    """
    Load and tokenize evaluation data into fixed-length token sequences.

    Supports: c4, wikitext, alpaca.
    Returns list of (seq_len,) token ID tensors.
    """
    from datasets import load_dataset

    if dataset_name == "c4":
        ds = load_dataset("allenai/c4", "en", split=split, streaming=True, trust_remote_code=True)
    elif dataset_name == "wikitext":
        ds = load_dataset("wikitext", "wikitext-2-raw-v1", split=split, trust_remote_code=True)
    elif dataset_name == "alpaca":
        ds = load_dataset("tatsu-lab/alpaca", split="train", trust_remote_code=True)
    else:
        raise ValueError(f"Unknown dataset: {dataset_name}. Choose from: c4, wikitext, alpaca")

    buffer: List[str] = []
    for item in ds:
        if dataset_name == "alpaca":
            text = f"{item.get('instruction', '')} {item.get('input', '')} {item.get('output', '')}"
        else:
            text = item.get("text", "")
        if text and len(text.strip()) >= 50:
            buffer.append(text)
        if len(buffer) >= num_samples * 5:
            break

    samples: List[torch.Tensor] = []
    for text in buffer:
        ids = tokenizer(text, return_tensors="pt", add_special_tokens=False).input_ids[0]
        if len(ids) >= seq_len:
            samples.append(ids[:seq_len])
        if len(samples) >= num_samples:
            break

    # Concatenate short texts if needed
    if len(samples) < num_samples:
        all_ids = torch.cat(
            [tokenizer(t, return_tensors="pt", add_special_tokens=False).input_ids[0] for t in buffer]
        )
        for i in range(0, len(all_ids) - seq_len + 1, seq_len):
            if len(samples) >= num_samples:
                break
            samples.append(all_ids[i : i + seq_len])

    return samples[:num_samples]
