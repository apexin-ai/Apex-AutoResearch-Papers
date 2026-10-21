#!/usr/bin/env python
"""π0 Token Importance Analysis — Pruning Curve on LIBERO-Object.

Measures normalized action loss as a function of vision token keep ratio.
Uses L2-norm importance ranking of vision tokens after linear projection.

π0 architecture:
  - PaliGemma (SigLIP 224x224 + Gemma 2B) + Gemma 300M action expert
  - 256 vision tokens per image × (2 real + 1 empty) cameras
  - Linear projection connector (multi_modal_projector)
  - Flow matching loss on action velocity

Run on CUDA_VISIBLE_DEVICES=2.
"""

import os
os.environ["CUDA_VISIBLE_DEVICES"] = "2"
os.environ["HF_HOME"] = "/root/autodl-tmp/.hf_cache"

import sys
sys.path.insert(0, "/root/autodl-tmp/lerobot/src")

import json
import io
from pathlib import Path
from collections import defaultdict

import torch
import torch.nn.functional as F
import numpy as np
import pyarrow.parquet as pq
from PIL import Image
from torchvision.transforms.functional import to_tensor

LIBERO_OBJECT_TASKS = range(20, 30)
FRAMES_PER_TASK = 10
KEEP_RATIOS = [0.1, 0.2, 0.3, 0.5, 0.7, 0.9, 0.95, 1.0]
TOKENIZER_MAX_LENGTH = 48
ARTIFACTS_DIR = "/root/autodl-tmp/importance_margin_vla_compress/artifacts"


def gini(values):
    sorted_v = np.sort(values)
    n = len(sorted_v)
    index = np.arange(1, n + 1)
    return (2 * np.sum(index * sorted_v) - (n + 1) * sorted_v.sum()) / (n * sorted_v.sum() + 1e-12)


def top_fraction(norms_2d, top_pct):
    results = []
    for row in norms_2d:
        sv = np.sort(row)[::-1]
        n_top = max(1, int(len(sv) * top_pct))
        results.append(sv[:n_top].sum() / (sv.sum() + 1e-12))
    return float(np.mean(results))


def entropy_of_distribution(norms_2d):
    results = []
    for row in norms_2d:
        p = row / (row.sum() + 1e-12)
        p = p[p > 0]
        ent = -np.sum(p * np.log(p))
        max_ent = np.log(len(row))
        results.append(ent / max_ent if max_ent > 0 else 0)
    return float(np.mean(results))


def load_tokenizer():
    from transformers import AutoTokenizer
    candidates = [
        "google/paligemma-3b-pt-224",
        "google/gemma-2-2b-it",
        "google/gemma-2b",
    ]
    for name in candidates:
        try:
            tok = AutoTokenizer.from_pretrained(
                name, cache_dir="/root/autodl-tmp/.hf_cache",
            )
            print(f"  Tokenizer loaded from {name}")
            return tok
        except Exception as e:
            print(f"  Tokenizer {name} failed: {e}")
    print("  WARNING: No tokenizer available, using dummy tokens")
    return None


@torch.no_grad()
def main():
    device = torch.device("cuda:0")

    # ═══ 1. Load π0 ═══
    print("Loading π0 model...")
    from lerobot.policies.pi0.modeling_pi0 import (
        PI0Policy, make_att_2d_masks, resize_with_pad_torch, pad_vector,
    )

    local_ckpt = (
        "/root/autodl-tmp/.hf_cache/models--lerobot--pi0_libero_base/"
        "snapshots/1dc27a57cf4b54c6fb138ed80a97da150e812e76"
    )
    policy = PI0Policy.from_pretrained(local_ckpt)
    policy.eval().to(device)

    flow = policy.model
    vlm_expert = flow.paligemma_with_expert

    test_img = torch.zeros(1, 3, 224, 224, device=device, dtype=torch.float32)
    img_emb = vlm_expert.embed_image(test_img)
    n_vis_per_img = img_emb.shape[1]
    hidden_dim = img_emb.shape[2]
    del test_img, img_emb
    torch.cuda.empty_cache()

    vlm = vlm_expert.paligemma.model.language_model
    n_vlm_layers = len(vlm.layers)
    n_expert_layers = len(vlm_expert.gemma_expert.model.layers)

    chunk_size = policy.config.chunk_size
    max_state_dim = policy.config.max_state_dim
    max_action_dim = policy.config.max_action_dim
    empty_cameras = getattr(policy.config, "empty_cameras", 0)

    print(f"  Vision tokens/image: {n_vis_per_img}, hidden_dim: {hidden_dim}")
    print(f"  VLM layers: {n_vlm_layers}, Expert layers: {n_expert_layers}")
    print(f"  chunk_size={chunk_size}, max_state={max_state_dim}, max_action={max_action_dim}")
    print(f"  empty_cameras: {empty_cameras}")

    tokenizer = load_tokenizer()

    # ═══ 2. Load LIBERO-Object data ═══
    print("\nLoading LIBERO-Object data...")
    snap = Path(
        "/root/autodl-tmp/.hf_cache/lerobot/hub/"
        "datasets--HuggingFaceVLA--libero/snapshots/"
        "86958911c0f959db2bbbdb107eb3e17c5f9c798e"
    )
    data_dir = snap / "data" / "chunk-000"

    tasks_tbl = pq.read_table(snap / "meta" / "tasks.parquet")
    task_descs = tasks_tbl.column("__index_level_0__").to_pylist()
    print(f"  {len(task_descs)} tasks loaded")

    per_task_rows = defaultdict(list)
    for pf in sorted(os.listdir(str(data_dir))):
        if not pf.endswith(".parquet"):
            continue
        tbl = pq.read_table(data_dir / pf)
        task_col = tbl.column("task_index").to_pylist()
        for idx, tid in enumerate(task_col):
            if tid in LIBERO_OBJECT_TASKS:
                per_task_rows[tid].append((pf, idx))

    frames = []
    for tid in sorted(per_task_rows.keys()):
        rows = per_task_rows[tid]
        step = max(1, len(rows) // FRAMES_PER_TASK)
        sampled = rows[::step][:FRAMES_PER_TASK]
        for pf, idx in sampled:
            tbl = pq.read_table(data_dir / pf)
            frames.append({
                "img1": Image.open(io.BytesIO(
                    tbl.column("observation.images.image")[idx]["bytes"].as_py()
                )).convert("RGB"),
                "img2": Image.open(io.BytesIO(
                    tbl.column("observation.images.image2")[idx]["bytes"].as_py()
                )).convert("RGB"),
                "state": torch.tensor(
                    tbl.column("observation.state")[idx].as_py(), dtype=torch.float32
                ),
                "task_idx": tid,
            })

    n_tasks = len({f["task_idx"] for f in frames})
    print(f"  {len(frames)} frames from {n_tasks} tasks")

    # ═══ 3. Pruning Curve ═══
    print("\n--- Pruning Curve Analysis ---")
    n_real_images = 2
    n_real_vis = n_vis_per_img * n_real_images
    n_total_images = n_real_images + empty_cameras
    n_total_vis = n_vis_per_img * n_total_images
    print(f"  Real vision tokens: {n_real_vis} ({n_real_images} cameras)")
    print(f"  Total vision tokens incl empty: {n_total_vis} ({n_total_images} cameras)")

    keep_ratio_losses = defaultdict(list)
    all_importance_norms = []

    model_dtype = vlm.layers[0].self_attn.q_proj.weight.dtype
    print(f"  Model dtype: {model_dtype}")

    for fi, frame in enumerate(frames):
        if fi % 20 == 0:
            print(f"  Frame {fi}/{len(frames)}...")

        img1 = to_tensor(frame["img1"]).unsqueeze(0).to(device)
        img2 = to_tensor(frame["img2"]).unsqueeze(0).to(device)
        img1 = resize_with_pad_torch(img1, 224, 224) * 2.0 - 1.0
        img2 = resize_with_pad_torch(img2, 224, 224) * 2.0 - 1.0

        images = [img1, img2]
        img_masks = [
            torch.ones(1, dtype=torch.bool, device=device),
            torch.ones(1, dtype=torch.bool, device=device),
        ]

        for _ in range(empty_cameras):
            empty_img = torch.ones_like(img1) * -1.0
            images.append(empty_img)
            img_masks.append(torch.zeros(1, dtype=torch.bool, device=device))

        if tokenizer is not None:
            desc = task_descs[frame["task_idx"]]
            if not desc.endswith("\n"):
                desc += "\n"
            tokens = tokenizer(
                desc, return_tensors="pt",
                padding="max_length", max_length=TOKENIZER_MAX_LENGTH,
                truncation=True,
            )
            lang_tokens = tokens["input_ids"].to(device)
            lang_masks = tokens["attention_mask"].bool().to(device)
        else:
            lang_tokens = torch.full(
                (1, TOKENIZER_MAX_LENGTH), 2, dtype=torch.long, device=device
            )
            lang_masks = torch.ones(
                1, TOKENIZER_MAX_LENGTH, dtype=torch.bool, device=device
            )
            lang_masks[:, 8:] = False

        state = pad_vector(frame["state"].unsqueeze(0).to(device), max_state_dim)

        actions = torch.zeros(1, chunk_size, max_action_dim, device=device)
        noise = torch.randn(1, chunk_size, max_action_dim, device=device)
        time_val = torch.tensor([0.5], device=device, dtype=torch.float32)

        time_exp = time_val[:, None, None]
        x_t = time_exp * noise + (1 - time_exp) * actions
        u_t = noise - actions

        prefix_embs, prefix_pad_masks, prefix_att_masks = flow.embed_prefix(
            images, img_masks, lang_tokens, lang_masks
        )
        suffix_embs, suffix_pad_masks, suffix_att_masks, adarms_cond = flow.embed_suffix(
            state, x_t, time_val
        )

        vis_embs = prefix_embs[:, :n_real_vis, :].float()
        importance = vis_embs.norm(dim=-1)
        all_importance_norms.append(importance.cpu().numpy())

        for k in KEEP_RATIOS:
            n_keep = max(1, int(k * n_real_vis))
            _, topk_idx = importance.topk(n_keep, dim=-1)

            mask = torch.zeros(1, n_real_vis, 1, device=device)
            mask.scatter_(1, topk_idx.unsqueeze(-1), 1.0)
            mask = mask.expand(-1, -1, prefix_embs.shape[-1])

            pruned_prefix = prefix_embs.clone()
            pruned_prefix[:, :n_real_vis, :] = (
                prefix_embs[:, :n_real_vis, :] * mask.to(prefix_embs.dtype)
            )

            if model_dtype == torch.bfloat16:
                pp = pruned_prefix.to(torch.bfloat16)
                sc = suffix_embs.to(torch.bfloat16)
            else:
                pp = pruned_prefix
                sc = suffix_embs

            pad_m = torch.cat([prefix_pad_masks, suffix_pad_masks], dim=1)
            att_m = torch.cat([prefix_att_masks, suffix_att_masks], dim=1)
            att_2d = make_att_2d_masks(pad_m, att_m)
            pos_ids = torch.cumsum(pad_m.long(), dim=1) - 1
            att_4d = flow._prepare_attention_masks_4d(att_2d)

            (_, suffix_out), _ = vlm_expert.forward(
                attention_mask=att_4d,
                position_ids=pos_ids,
                past_key_values=None,
                inputs_embeds=[pp, sc],
                use_cache=False,
                adarms_cond=[None, adarms_cond],
            )

            suffix_out = suffix_out[:, -chunk_size:].to(torch.float32)
            v_t = flow.action_out_proj(suffix_out)
            loss = F.mse_loss(u_t, v_t).item()
            keep_ratio_losses[k].append(loss)

    # ═══ 4. Results ═══
    baseline_losses = keep_ratio_losses[1.0]
    mean_baseline = float(np.mean(baseline_losses))

    all_norms = np.concatenate(all_importance_norms, axis=0)

    results = {
        "model": "pi0-3.3B (lerobot/pi0_libero_base)",
        "dataset": "LIBERO-Object (task_index 20-29)",
        "n_frames": len(frames),
        "n_tasks": n_tasks,
        "vision_tokens_per_image": int(n_vis_per_img),
        "num_real_images": n_real_images,
        "num_total_images": n_total_images,
        "total_real_vision_tokens": int(n_real_vis),
        "connector_type": "linear_projection",
        "hidden_dim": int(hidden_dim),
        "vlm_backbone": "Gemma-2B",
        "vision_encoder": "SigLIP-So400m/14",
        "vlm_layers": n_vlm_layers,
        "expert_layers": n_expert_layers,
        "pruning_method": "L2_norm_zero_out",
        "baseline_loss": round(mean_baseline, 6),
        "keep_ratios": {},
        "importance_distribution": {
            "mean_norm": round(float(all_norms.mean()), 4),
            "std_norm": round(float(all_norms.std()), 4),
            "cv": round(float(all_norms.std() / (all_norms.mean() + 1e-12)), 4),
            "gini": round(gini(all_norms.flatten()), 4),
            "top10_frac": round(top_fraction(all_norms, 0.1), 4),
            "top30_frac": round(top_fraction(all_norms, 0.3), 4),
            "entropy_ratio": round(entropy_of_distribution(all_norms), 4),
        },
    }

    for k in KEEP_RATIOS:
        losses = keep_ratio_losses[k]
        mean_loss = float(np.mean(losses))
        results["keep_ratios"][str(k)] = {
            "raw_loss": round(mean_loss, 6),
            "normalized_loss": round(mean_loss / mean_baseline, 4),
            "std": round(float(np.std(losses)), 6),
        }

    os.makedirs(ARTIFACTS_DIR, exist_ok=True)
    out_path = os.path.join(ARTIFACTS_DIR, "pi0_pruning_curve.json")
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)

    print(f"\nResults saved to {out_path}")
    print(f"Baseline loss (k=1.0): {mean_baseline:.6f}")
    print(f"\nImportance distribution:")
    print(f"  Gini: {results['importance_distribution']['gini']:.4f}")
    print(f"  CV: {results['importance_distribution']['cv']:.4f}")
    print(f"  Entropy ratio: {results['importance_distribution']['entropy_ratio']:.4f}")
    print(f"  Top-10% fraction: {results['importance_distribution']['top10_frac']:.4f}")
    print(f"\nPruning curve:")
    for k in KEEP_RATIOS:
        r = results["keep_ratios"][str(k)]
        print(f"  k={k:.2f}: normalized={r['normalized_loss']:.4f} (raw={r['raw_loss']:.6f})")


if __name__ == "__main__":
    main()
