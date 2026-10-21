"""Token Importance Analysis: attention weight distribution + gradient correlation.

Analyzes tokens deleted vs retained by ACIS:
  1. Attention weight distribution (how much each token group is attended to in VLM layers)
  2. Gradient correlation (ACIS scores vs action-loss gradient magnitude)
  3. Per-sample raw data for visualization

Usage:
    CUDA_VISIBLE_DEVICES=1 python eval_token_importance.py \
        --checkpoint checkpoints/imm_anchor_v8b_twostage/final/checkpoint.pt \
        --num_samples 500 \
        --output_dir results/token_importance_analysis/
"""

from __future__ import annotations

import argparse
import json
import logging
import sys
from pathlib import Path
from typing import Any, Dict, List, Tuple

import numpy as np
import torch
import torch.nn.functional as F
import yaml

ARTIFACTS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(ARTIFACTS_DIR))

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger(__name__)


def parse_args():
    parser = argparse.ArgumentParser(description="Token importance analysis")
    parser.add_argument("--checkpoint", type=str, required=True)
    parser.add_argument("--config", type=str, default=None,
                        help="Config YAML (auto-detected from checkpoint if not provided)")
    parser.add_argument("--num_samples", type=int, default=500)
    parser.add_argument("--output_dir", type=str, default="results/token_importance_analysis/")
    parser.add_argument("--batch_size", type=int, default=4)
    parser.add_argument("--seed", type=int, default=42)
    return parser.parse_args()


def find_config(checkpoint_path: str) -> str:
    ckpt_path = Path(checkpoint_path)
    for parent in ckpt_path.parents:
        for cfg in parent.glob("*.yaml"):
            return str(cfg)
    return str(ARTIFACTS_DIR / "configs" / "imm_anchor.yaml")


def collect_vlm_attention_weights(model, batch, vis_token_count):
    """Register hooks on VLM attention layers to capture attention weights
    directed at visual token positions.

    Returns: list of (B, N_vis) tensors — mean attention received by each
    visual token position, one per VLM layer.
    """
    bm = model.base_model
    vlm = bm.vlm_with_expert

    text_model = None
    if hasattr(vlm, 'text_model'):
        text_model = vlm.text_model
    elif hasattr(vlm, 'model'):
        text_model = vlm.model

    if text_model is None:
        return []

    layers = None
    if hasattr(text_model, 'layers'):
        layers = text_model.layers
    elif hasattr(text_model, 'model') and hasattr(text_model.model, 'layers'):
        layers = text_model.model.layers

    if layers is None:
        return []

    attention_maps = []
    hooks = []

    def make_hook(layer_idx):
        def hook_fn(module, args, kwargs, output):
            if isinstance(output, tuple) and len(output) >= 2 and output[1] is not None:
                attn_w = output[1]  # (B, H, seq, seq)
                attention_maps.append((layer_idx, attn_w.detach()))
        return hook_fn

    for idx, layer in enumerate(layers):
        attn_module = None
        if hasattr(layer, 'self_attn'):
            attn_module = layer.self_attn
        elif hasattr(layer, 'attention'):
            attn_module = layer.attention

        if attn_module is not None:
            h = attn_module.register_forward_hook(make_hook(idx), with_kwargs=True)
            hooks.append(h)

    return hooks, attention_maps


def compute_gradient_importance(model, batch, device):
    """Compute gradient magnitude of action loss w.r.t. each visual token.

    Returns:
        grad_magnitudes: (B, N_vis) gradient L2 norm per token
        importance_scores: (B, N_vis) ACIS scores
        action_loss: scalar
    """
    bm = model.base_model

    images, img_masks = model.policy.prepare_images(batch)
    state = model.policy.prepare_state(batch)

    from lerobot.utils.constants import OBS_LANGUAGE_TOKENS, OBS_LANGUAGE_ATTENTION_MASK
    lang_tokens = batch[OBS_LANGUAGE_TOKENS]
    lang_masks = batch[OBS_LANGUAGE_ATTENTION_MASK]
    actions = model.policy.prepare_action(batch)

    vis_tokens, tokens_per_cam = model._get_visual_tokens(images)
    vis_tokens = vis_tokens.detach().requires_grad_(True)

    noise = bm.sample_noise(actions.shape, actions.device)
    time = bm.sample_time(actions.shape[0], actions.device)
    time_expanded = time[:, None, None]
    x_t = time_expanded * noise + (1 - time_expanded) * actions
    u_t = noise - actions

    suffix_embs, suffix_pad, suffix_att = bm.embed_suffix(x_t, time)

    importance_scores = model.acis(suffix_embs, vis_tokens)

    N_vis = vis_tokens.shape[1]
    k = max(1, int(N_vis * model.k_ratio))

    selected_tokens, mask, sel_info = model.token_selector(
        importance_scores, vis_tokens, k, training=True
    )

    prefix_embs, prefix_pad, prefix_att = model._build_prefix_with_vis_tokens(
        selected_tokens, tokens_per_cam, img_masks, lang_tokens, lang_masks, state
    )

    all_pad = torch.cat([prefix_pad, suffix_pad], dim=1)
    all_att = torch.cat([prefix_att, suffix_att], dim=1)

    from imm.smolvla_wrapper import _make_att_2d_masks
    att_2d = _make_att_2d_masks(all_pad, all_att)
    position_ids = torch.cumsum(all_pad, dim=1) - 1

    (_, suffix_out), _ = bm.vlm_with_expert.forward(
        attention_mask=att_2d,
        position_ids=position_ids,
        past_key_values=None,
        inputs_embeds=[prefix_embs, suffix_embs],
        use_cache=False,
        fill_kv_cache=False,
    )

    chunk_size = bm.config.chunk_size
    suffix_out = suffix_out[:, -chunk_size:]
    suffix_out = suffix_out.to(dtype=torch.float32)
    v_t = bm.action_out_proj(suffix_out)

    action_dim = model.policy.config.action_feature.shape[0]
    action_loss = F.mse_loss(
        u_t[:, :, :action_dim],
        v_t[:, :, :action_dim],
    )

    action_loss.backward()

    grad_magnitudes = vis_tokens.grad.norm(dim=-1)  # (B, N_vis)

    return grad_magnitudes.detach(), importance_scores.detach(), action_loss.detach()


def compute_attention_stats_via_acis(model, batch):
    """Use ACIS internal attention weights as proxy for how much visual tokens are attended.

    Captures the attention weight matrix inside ACIS (action queries → visual keys).
    Returns: (B, N_vis) mean attention received per visual token.
    """
    bm = model.base_model

    images, img_masks = model.policy.prepare_images(batch)
    vis_tokens, _ = model._get_visual_tokens(images)

    actions = model.policy.prepare_action(batch)
    noise = bm.sample_noise(actions.shape, actions.device)
    time = bm.sample_time(actions.shape[0], actions.device)
    time_expanded = time[:, None, None]
    x_t = time_expanded * noise + (1 - time_expanded) * actions

    suffix_embs, _, _ = bm.embed_suffix(x_t, time)

    acis = model.acis
    B, N, _ = vis_tokens.shape
    Q = suffix_embs.shape[1]
    H, d = acis.num_heads, acis.head_dim

    q = acis.q_proj(acis.query_proj(suffix_embs))
    k = acis.k_proj(vis_tokens)

    q = q.view(B, Q, H, d).transpose(1, 2)
    k = k.view(B, N, H, d).transpose(1, 2)

    attn_weights = torch.matmul(q, k.transpose(-2, -1)) * acis.scale
    attn_weights = attn_weights.softmax(dim=-1)  # (B, H, Q, N)

    # Mean attention received by each visual token across all heads and queries
    attn_per_token = attn_weights.mean(dim=(1, 2))  # (B, N)

    return attn_per_token.detach()


def main():
    args = parse_args()
    torch.manual_seed(args.seed)
    np.random.seed(args.seed)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    log.info("Device: %s", device)

    config_path = args.config or find_config(args.checkpoint)
    log.info("Config: %s", config_path)

    from train import load_config, load_smolvla_policy, wrap_with_imm, load_dataset, make_dataloader, preprocess_batch, get_tokenizer_from_policy

    config = load_config(config_path)
    config["imm"]["enabled"] = True

    policy = load_smolvla_policy(config, device)
    model = wrap_with_imm(policy, config)
    model.to(device)

    ckpt_path = Path(args.checkpoint)
    if ckpt_path.is_dir():
        ckpt_path = ckpt_path / "checkpoint.pt"
    log.info("Loading checkpoint: %s", ckpt_path)
    state = torch.load(ckpt_path, map_location=device, weights_only=False)
    model.load_state_dict(state["model_state_dict"], strict=False)

    tokenizer = get_tokenizer_from_policy(model)

    dataset = load_dataset(config)
    dl_config = {
        **config,
        "training": {**config.get("training", {}), "batch_size": args.batch_size},
    }
    dataloader = make_dataloader(dataset, dl_config)

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Storage
    all_grad_correlations_pearson = []
    all_grad_correlations_spearman = []
    all_attn_retained = []
    all_attn_deleted = []
    all_importance_scores_list = []
    all_grad_magnitudes_list = []
    all_attn_weights_list = []

    n_samples_processed = 0
    max_batches = (args.num_samples + args.batch_size - 1) // args.batch_size

    log.info("Starting analysis: %d samples, batch_size=%d, max_batches=%d",
             args.num_samples, args.batch_size, max_batches)

    for batch_idx, batch in enumerate(dataloader):
        if batch_idx >= max_batches:
            break

        batch = {k: v.to(device) if isinstance(v, torch.Tensor) else v for k, v in batch.items()}
        batch = preprocess_batch(batch, tokenizer, device=device)
        B = next(v.shape[0] for v in batch.values() if isinstance(v, torch.Tensor))

        # --- 1. Gradient analysis (requires grad) ---
        model.train()
        model.zero_grad()

        grad_mags, importance_scores, action_loss = compute_gradient_importance(model, batch, device)
        # grad_mags: (B, N_vis), importance_scores: (B, N_vis)

        N_vis = importance_scores.shape[1]
        k = max(1, int(N_vis * model.k_ratio))

        # --- 2. Attention weight analysis (no grad needed) ---
        model.eval()
        with torch.no_grad():
            attn_per_token = compute_attention_stats_via_acis(model, batch)
            # attn_per_token: (B, N_vis)

        # --- 3. Per-sample statistics ---
        for b in range(B):
            if n_samples_processed >= args.num_samples:
                break

            scores_b = importance_scores[b]  # (N_vis,)
            grad_b = grad_mags[b]            # (N_vis,)
            attn_b = attn_per_token[b]       # (N_vis,)

            # Top-k / bottom-k split
            sorted_idx = scores_b.argsort(descending=True)
            retained_idx = sorted_idx[:k]
            deleted_idx = sorted_idx[k:]

            attn_retained = attn_b[retained_idx]
            attn_deleted = attn_b[deleted_idx]

            all_attn_retained.extend(attn_retained.cpu().tolist())
            all_attn_deleted.extend(attn_deleted.cpu().tolist())

            # Pearson correlation
            scores_np = scores_b.cpu().numpy()
            grad_np = grad_b.cpu().numpy()

            if scores_np.std() > 1e-8 and grad_np.std() > 1e-8:
                pearson = np.corrcoef(scores_np, grad_np)[0, 1]
            else:
                pearson = 0.0
            all_grad_correlations_pearson.append(float(pearson))

            # Spearman correlation
            from scipy.stats import spearmanr
            if scores_np.std() > 1e-8 and grad_np.std() > 1e-8:
                spearman_r, _ = spearmanr(scores_np, grad_np)
            else:
                spearman_r = 0.0
            all_grad_correlations_spearman.append(float(spearman_r))

            # Store raw data (subsample for storage)
            all_importance_scores_list.append(scores_np.tolist())
            all_grad_magnitudes_list.append(grad_np.tolist())
            all_attn_weights_list.append(attn_b.cpu().tolist())

            n_samples_processed += 1

        if (batch_idx + 1) % 25 == 0:
            log.info("Processed %d/%d samples (batch %d/%d), "
                     "mean Pearson=%.4f, mean Spearman=%.4f",
                     n_samples_processed, args.num_samples, batch_idx + 1, max_batches,
                     np.mean(all_grad_correlations_pearson),
                     np.mean(all_grad_correlations_spearman))

        if n_samples_processed >= args.num_samples:
            break

    log.info("Analysis complete: %d samples processed", n_samples_processed)

    # --- Compute aggregate statistics ---
    attn_retained_arr = np.array(all_attn_retained)
    attn_deleted_arr = np.array(all_attn_deleted)

    # Histogram bins
    all_attn = np.concatenate([attn_retained_arr, attn_deleted_arr])
    hist_bins = np.linspace(all_attn.min(), all_attn.max(), 51).tolist()
    hist_retained, _ = np.histogram(attn_retained_arr, bins=hist_bins)
    hist_deleted, _ = np.histogram(attn_deleted_arr, bins=hist_bins)

    attention_stats = {
        "retained": {
            "mean": float(attn_retained_arr.mean()),
            "median": float(np.median(attn_retained_arr)),
            "std": float(attn_retained_arr.std()),
            "min": float(attn_retained_arr.min()),
            "max": float(attn_retained_arr.max()),
            "q25": float(np.percentile(attn_retained_arr, 25)),
            "q75": float(np.percentile(attn_retained_arr, 75)),
            "count": len(attn_retained_arr),
        },
        "deleted": {
            "mean": float(attn_deleted_arr.mean()),
            "median": float(np.median(attn_deleted_arr)),
            "std": float(attn_deleted_arr.std()),
            "min": float(attn_deleted_arr.min()),
            "max": float(attn_deleted_arr.max()),
            "q25": float(np.percentile(attn_deleted_arr, 25)),
            "q75": float(np.percentile(attn_deleted_arr, 75)),
            "count": len(attn_deleted_arr),
        },
        "histogram": {
            "bins": hist_bins,
            "retained_counts": hist_retained.tolist(),
            "deleted_counts": hist_deleted.tolist(),
        },
        "effect_size_cohens_d": float(
            (attn_retained_arr.mean() - attn_deleted_arr.mean())
            / np.sqrt((attn_retained_arr.std() ** 2 + attn_deleted_arr.std() ** 2) / 2)
        ) if (attn_retained_arr.std() > 1e-8 or attn_deleted_arr.std() > 1e-8) else 0.0,
        "n_samples": n_samples_processed,
        "k_ratio": model.k_ratio,
        "N_vis": N_vis,
        "k": k,
    }

    gradient_correlation = {
        "pearson": {
            "mean": float(np.mean(all_grad_correlations_pearson)),
            "median": float(np.median(all_grad_correlations_pearson)),
            "std": float(np.std(all_grad_correlations_pearson)),
            "min": float(np.min(all_grad_correlations_pearson)),
            "max": float(np.max(all_grad_correlations_pearson)),
            "q25": float(np.percentile(all_grad_correlations_pearson, 25)),
            "q75": float(np.percentile(all_grad_correlations_pearson, 75)),
            "values": all_grad_correlations_pearson,
        },
        "spearman": {
            "mean": float(np.mean(all_grad_correlations_spearman)),
            "median": float(np.median(all_grad_correlations_spearman)),
            "std": float(np.std(all_grad_correlations_spearman)),
            "min": float(np.min(all_grad_correlations_spearman)),
            "max": float(np.max(all_grad_correlations_spearman)),
            "q25": float(np.percentile(all_grad_correlations_spearman, 25)),
            "q75": float(np.percentile(all_grad_correlations_spearman, 75)),
            "values": all_grad_correlations_spearman,
        },
        "n_samples": n_samples_processed,
        "interpretation": (
            "Positive correlation means ACIS assigns higher importance to tokens "
            "that have larger gradient magnitude w.r.t. action loss, i.e., tokens "
            "that matter more for action prediction."
        ),
    }

    # Save results
    with open(output_dir / "attention_stats.json", "w") as f:
        json.dump(attention_stats, f, indent=2)
    log.info("Saved attention_stats.json")

    with open(output_dir / "gradient_correlation.json", "w") as f:
        json.dump(gradient_correlation, f, indent=2)
    log.info("Saved gradient_correlation.json")

    # Raw data (per-sample, may be large)
    raw_data = {
        "importance_scores": all_importance_scores_list,
        "gradient_magnitudes": all_grad_magnitudes_list,
        "attention_weights": all_attn_weights_list,
        "n_samples": n_samples_processed,
        "N_vis": N_vis,
        "k": k,
    }
    with open(output_dir / "raw_data.json", "w") as f:
        json.dump(raw_data, f)
    log.info("Saved raw_data.json")

    # Print summary
    log.info("=" * 60)
    log.info("RESULTS SUMMARY")
    log.info("=" * 60)
    log.info("Attention weights (ACIS cross-attention received):")
    log.info("  Retained tokens: mean=%.6f, std=%.6f",
             attention_stats["retained"]["mean"], attention_stats["retained"]["std"])
    log.info("  Deleted tokens:  mean=%.6f, std=%.6f",
             attention_stats["deleted"]["mean"], attention_stats["deleted"]["std"])
    log.info("  Cohen's d: %.4f", attention_stats["effect_size_cohens_d"])
    log.info("")
    log.info("Gradient correlation (ACIS score vs action-loss gradient):")
    log.info("  Pearson:  mean=%.4f, std=%.4f",
             gradient_correlation["pearson"]["mean"], gradient_correlation["pearson"]["std"])
    log.info("  Spearman: mean=%.4f, std=%.4f",
             gradient_correlation["spearman"]["mean"], gradient_correlation["spearman"]["std"])
    log.info("=" * 60)


if __name__ == "__main__":
    main()
