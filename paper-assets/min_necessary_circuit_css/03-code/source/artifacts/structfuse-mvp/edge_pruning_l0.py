"""L0 Edge Pruning: circuit discovery via differentiable mask optimization.

Optimizes continuous edge masks using Hard Concrete relaxation (Louizos et al. 2018)
with L0 regularization. Minimizes -task_metric + lambda * L0(masks) to find the
minimal circuit preserving task performance.

vs auto-circuit mask_gradient (gradient-based attribution):
  mask_gradient: one-pass importance scoring via integrated gradients over masks
  L0 pruning: multi-epoch iterative optimization producing genuinely optimized masks

Ref: Bhaskar et al. 2024 "Finding Transformer Circuits with Edge Pruning"
"""

import math
import torch
import torch.nn as nn
from typing import Dict, List, Tuple


class HardConcreteMask(nn.Module):
    """Hard Concrete distribution for differentiable L0 regularization.
    Ref: Louizos et al. 2018 "Learning Sparse Neural Networks through L0 Regularization"
    """

    def __init__(self, n_edges: int, init_value: float = 0.0,
                 beta: float = 2/3, zeta: float = 1.1, gamma: float = -0.1):
        super().__init__()
        self.log_alpha = nn.Parameter(torch.full((n_edges,), init_value))
        self.beta = beta
        self.zeta = zeta
        self.gamma = gamma

    def forward(self, training: bool = True) -> torch.Tensor:
        if training:
            u = torch.rand_like(self.log_alpha).clamp(1e-8, 1 - 1e-8)
            s = torch.sigmoid((torch.log(u / (1 - u)) + self.log_alpha) / self.beta)
            s_bar = s * (self.zeta - self.gamma) + self.gamma
            return s_bar.clamp(0, 1)
        z = torch.sigmoid(self.log_alpha) * (self.zeta - self.gamma) + self.gamma
        return z.clamp(0, 1)

    def l0_loss(self) -> torch.Tensor:
        """Expected L0 norm under the hard concrete distribution."""
        return torch.sigmoid(
            self.log_alpha - self.beta * math.log(-self.gamma / self.zeta)
        ).sum()


# --- Edge topology helpers (mirrored from ifr_discovery.py) ---

def _src_layer(name: str) -> int:
    if name == "hook_embed":
        return -1
    return int(name.split(".")[1])


def _before_attn(src: str, dst_layer: int) -> bool:
    return _src_layer(src) < dst_layer


def _before_mlp(src: str, dst_layer: int) -> bool:
    sl = _src_layer(src)
    if sl < dst_layer:
        return True
    return sl == dst_layer and "hook_result" in src


def _extract_tokens(dataset):
    if isinstance(dataset, torch.Tensor):
        return dataset
    if hasattr(dataset, "toks"):
        return dataset.toks
    if isinstance(dataset, dict) and "input_ids" in dataset:
        return dataset["input_ids"]
    return dataset


def _build_edge_index(n_layers: int, n_heads: int):
    """Build internal edge lists grouped by destination layer.

    Attention edges use per-layer granularity (shared across heads at each layer).
    MLP edges are per (source, destination_layer).
    Output is expanded to per-Q/K/V/head format for CSS compatibility.
    """
    sources: List[str] = ["hook_embed"]
    attn_edges: List[Tuple[str, int]] = []
    mlp_edges: List[Tuple[str, int]] = []

    for L in range(n_layers):
        for src in sources:
            if _before_attn(src, L):
                attn_edges.append((src, L))

        for src in sources:
            if _before_mlp(src, L):
                mlp_edges.append((src, L))
        for H in range(n_heads):
            mlp_edges.append((f"blocks.{L}.attn.hook_result[{H}]", L))

        for H in range(n_heads):
            sources.append(f"blocks.{L}.attn.hook_result[{H}]")
        sources.append(f"blocks.{L}.hook_mlp_out")

    attn_lookup: Dict[int, List[Tuple[str, int]]] = {}
    for i, (src, dst) in enumerate(attn_edges):
        attn_lookup.setdefault(dst, []).append((src, i))

    mlp_lookup: Dict[int, List[Tuple[str, int]]] = {}
    for i, (src, dst) in enumerate(mlp_edges):
        mlp_lookup.setdefault(dst, []).append((src, i))

    return attn_edges, mlp_edges, attn_lookup, mlp_lookup


def _masked_forward(model, embed, z_attn, z_mlp, attn_lookup, mlp_lookup):
    """Cascading forward pass with L0 edge masks.

    Each component's input is reconstructed as a masked weighted sum of upstream
    outputs. Later layers see masked outputs from earlier layers.
    """
    n_layers = model.cfg.n_layers
    n_heads = model.cfg.n_heads
    d_head = model.cfg.d_head
    device = embed.device
    B, S, D = embed.shape

    src_acts: Dict[str, torch.Tensor] = {"hook_embed": embed}
    # Accumulated attention output biases (b_O per layer, always included)
    bias_acc = torch.zeros(1, 1, D, device=device)

    for L in range(n_layers):
        block = model.blocks[L]

        # --- Attention: reconstruct masked residual input ---
        resid_attn = bias_acc.expand(B, S, D) + torch.zeros(B, S, D, device=device)
        for src_name, idx in attn_lookup.get(L, []):
            resid_attn = resid_attn + z_attn[idx] * src_acts[src_name]

        normed = block.ln1(resid_attn)
        q = torch.einsum('bsd,ndh->bsnh', normed, block.attn.W_Q) + block.attn.b_Q
        k = torch.einsum('bsd,ndh->bsnh', normed, block.attn.W_K) + block.attn.b_K
        v = torch.einsum('bsd,ndh->bsnh', normed, block.attn.W_V) + block.attn.b_V

        attn_scores = torch.einsum('bqnh,bknh->bnqk', q, k) / math.sqrt(d_head)
        causal = torch.triu(
            torch.ones(S, S, device=device, dtype=torch.bool), diagonal=1
        )
        attn_scores = attn_scores.masked_fill(causal[None, None], float('-inf'))
        pattern = torch.softmax(attn_scores, dim=-1)
        z_out = torch.einsum('bnqk,bknh->bqnh', pattern, v)
        result = torch.einsum('bsnh,nhd->bsnd', z_out, block.attn.W_O)

        for H in range(n_heads):
            src_acts[f"blocks.{L}.attn.hook_result[{H}]"] = result[:, :, H, :]

        bias_acc = bias_acc + block.attn.b_O

        # --- MLP: reconstruct masked residual input ---
        resid_mlp = bias_acc.expand(B, S, D) + torch.zeros(B, S, D, device=device)
        for src_name, idx in mlp_lookup.get(L, []):
            resid_mlp = resid_mlp + z_mlp[idx] * src_acts[src_name]

        mlp_out = block.mlp(block.ln2(resid_mlp))
        src_acts[f"blocks.{L}.hook_mlp_out"] = mlp_out

    # Final residual = all component outputs + accumulated biases
    final_resid = bias_acc.expand(B, S, D) + torch.zeros(B, S, D, device=device)
    for act in src_acts.values():
        final_resid = final_resid + act

    normed_final = model.ln_final(final_resid)
    logits = normed_final @ model.W_U + model.b_U
    return logits


def run_edge_pruning_l0(
    model,
    dataset,
    metric,
    target_sparsity: float = 0.05,
    n_epochs: int = 100,
    lr: float = 0.01,
    lambda_l0: float = 1e-2,
) -> Dict[str, float]:
    """Run Edge Pruning with L0 regularization.

    Args:
        model: HookedTransformer instance
        dataset: tokenized input data (tensor, .toks, or dict with input_ids)
        metric: callable(logits) -> scalar, higher = better task performance
        target_sparsity: informational; actual sparsity controlled by lambda_l0
        n_epochs: optimization epochs
        lr: learning rate for mask parameters
        lambda_l0: L0 regularization coefficient

    Returns:
        Dict mapping edge names (TransformerLens format) to mask values [0, 1].
        Mask > 0.5 indicates edge is in the circuit.
    """
    n_layers = model.cfg.n_layers
    n_heads = model.cfg.n_heads
    device = next(model.parameters()).device

    tokens = _extract_tokens(dataset).to(device)

    with torch.no_grad():
        embed = model.embed(tokens)
        if hasattr(model, 'pos_embed'):
            embed = embed + model.pos_embed(tokens)
        embed = embed.detach()

    attn_edges, mlp_edges, attn_lookup, mlp_lookup = _build_edge_index(
        n_layers, n_heads
    )
    n_attn = len(attn_edges)
    n_mlp = len(mlp_edges)

    mask = HardConcreteMask(n_attn + n_mlp).to(device)
    optimizer = torch.optim.Adam([mask.log_alpha], lr=lr)

    model.eval()
    for p in model.parameters():
        p.requires_grad_(False)

    for epoch in range(n_epochs):
        z = mask(training=True)

        logits = _masked_forward(
            model, embed, z[:n_attn], z[n_attn:], attn_lookup, mlp_lookup
        )

        task_loss = -metric(logits)
        l0_loss = mask.l0_loss()
        total_loss = task_loss + lambda_l0 * l0_loss

        optimizer.zero_grad()
        total_loss.backward()
        optimizer.step()

        if (epoch + 1) % 20 == 0:
            with torch.no_grad():
                z_eval = mask(training=False)
                n_active = (z_eval > 0.5).sum().item()
            print(
                f"  [L0] epoch {epoch+1}/{n_epochs}: "
                f"loss={total_loss.item():.4f} task={task_loss.item():.4f} "
                f"l0={l0_loss.item():.1f} active={n_active}/{n_attn+n_mlp}"
            )

    with torch.no_grad():
        z_final = mask(training=False)

    edge_scores: Dict[str, float] = {}

    for i, (src, dst_layer) in enumerate(attn_edges):
        val = z_final[i].item()
        for H in range(n_heads):
            for hook in ("hook_q", "hook_k", "hook_v"):
                edge_scores[
                    f"{src} -> blocks.{dst_layer}.attn.{hook}[{H}]"
                ] = val

    for i, (src, dst_layer) in enumerate(mlp_edges):
        edge_scores[
            f"{src} -> blocks.{dst_layer}.hook_mlp_in"
        ] = z_final[n_attn + i].item()

    return edge_scores
