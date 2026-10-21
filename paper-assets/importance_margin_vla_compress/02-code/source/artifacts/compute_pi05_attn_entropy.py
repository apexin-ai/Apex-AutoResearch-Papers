#!/usr/bin/env python
"""Measure π0.5 per-layer attention entropy on LIBERO-Object images.

Hooks into Gemma-2B's attention layers to capture how text tokens attend
to vision tokens. Consistent methodology with SmolVLA/X-VLA entropy scripts.
"""

import os
os.environ["CUDA_VISIBLE_DEVICES"] = "1"
os.environ["HF_HOME"] = "/root/autodl-tmp/.hf_cache"
os.environ["HF_HUB_OFFLINE"] = "1"
os.environ["MUJOCO_GL"] = "egl"

import sys
sys.path.insert(0, "/root/autodl-tmp/importance_margin_vla_compress")

import json
import math
import io
import types
from pathlib import Path
from collections import defaultdict

import torch
import torch.nn.functional as F
import numpy as np
import pyarrow.parquet as pq
from PIL import Image
from torchvision.transforms.functional import to_tensor, resize

N_VIS_PER_IMAGE = 256
N_IMAGES = 3
N_VIS = N_VIS_PER_IMAGE * N_IMAGES
N_DUMMY_LANG = 20
FRAMES_PER_TASK = 10
LIBERO_OBJECT_TASKS = range(20, 30)


@torch.no_grad()
def main():
    device = torch.device("cuda:0")

    # ── Load π0.5 ──────────────────────────────────────────
    print("Loading π0.5 model...")
    from lerobot.policies.pi05.modeling_pi05 import PI05Policy
    policy = PI05Policy.from_pretrained("/root/autodl-tmp/pi05_libero_finetuned")

    paligemma_expert = policy.model.paligemma_with_expert

    def patched_embed_image(self, image):
        out_dtype = image.dtype
        if image.dtype != torch.float32:
            image = image.to(torch.float32)
        image_outputs = self.paligemma.model.vision_tower(image)
        selected_image_feature = image_outputs.last_hidden_state
        features = self.paligemma.model.multi_modal_projector(selected_image_feature)
        features = features * self.paligemma.config.text_config.hidden_size**0.5
        if features.dtype != out_dtype:
            features = features.to(out_dtype)
        return features

    paligemma_expert.embed_image = types.MethodType(patched_embed_image, paligemma_expert)

    policy = policy.to(device)
    policy.eval()

    language_model = paligemma_expert.paligemma.model.language_model
    n_layers = language_model.config.num_hidden_layers
    hidden_size = language_model.config.hidden_size

    print(f"  Gemma-2B: {n_layers} layers, hidden_size={hidden_size}")
    print(f"  Vision tokens: {N_VIS_PER_IMAGE}/img x {N_IMAGES} = {N_VIS}")

    # ── Force eager attention + monkey-patch to capture weights ──
    from transformers.models.gemma import modeling_gemma

    language_model.config._attn_implementation = "eager"

    _original_eager = modeling_gemma.eager_attention_forward
    captured_attn = []

    def capturing_eager(module, query, key, value, attention_mask, scaling, dropout=0.0, **kwargs):
        attn_output, attn_weights = _original_eager(
            module, query, key, value, attention_mask, scaling, dropout, **kwargs
        )
        captured_attn.append(attn_weights.detach().cpu())
        return attn_output, attn_weights

    modeling_gemma.eager_attention_forward = capturing_eager

    # ── Load LIBERO-Object images ──────────────────────────
    print("\nLoading LIBERO-Object images...")
    snap = Path("/root/autodl-tmp/.hf_cache/lerobot/hub/"
                "datasets--HuggingFaceVLA--libero/snapshots/"
                "86958911c0f959db2bbbdb107eb3e17c5f9c798e")
    data_dir = snap / "data" / "chunk-000"

    per_task_rows = defaultdict(list)
    for pf in sorted(os.listdir(data_dir)):
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
            frames.append(dict(
                img1=Image.open(io.BytesIO(
                    tbl.column("observation.images.image")[idx]["bytes"].as_py()
                )).convert("RGB"),
                img2=Image.open(io.BytesIO(
                    tbl.column("observation.images.image2")[idx]["bytes"].as_py()
                )).convert("RGB"),
                task_idx=tid,
            ))

    n_tasks = len(per_task_rows)
    print(f"  {len(frames)} frames from {n_tasks} tasks")

    # ── Process each frame ─────────────────────────────────
    per_layer_ent = defaultdict(list)
    per_layer_vfrac = defaultdict(list)

    for fi, frame in enumerate(frames):
        captured_attn.clear()

        img1 = to_tensor(frame["img1"])
        img1 = resize(img1, [224, 224], antialias=True)
        img1 = (img1 * 2.0 - 1.0).unsqueeze(0).to(device)

        img2 = to_tensor(frame["img2"])
        img2 = resize(img2, [224, 224], antialias=True)
        img2 = (img2 * 2.0 - 1.0).unsqueeze(0).to(device)

        img3 = torch.ones(1, 3, 224, 224, device=device) * -1.0

        emb1 = paligemma_expert.embed_image(img1)
        emb2 = paligemma_expert.embed_image(img2)
        emb3 = paligemma_expert.embed_image(img3)

        dummy_tokens = torch.arange(100, 100 + N_DUMMY_LANG, device=device).unsqueeze(0)
        lang_emb = paligemma_expert.embed_language_tokens(dummy_tokens)

        prefix = torch.cat([emb1, emb2, emb3, lang_emb], dim=1)
        seq_len = prefix.shape[1]

        language_model(
            inputs_embeds=prefix,
            attention_mask=torch.ones(1, seq_len, dtype=torch.long, device=device),
            position_ids=torch.arange(seq_len, device=device).unsqueeze(0),
        )

        if len(captured_attn) != n_layers:
            print(f"  WARNING: got {len(captured_attn)} attn calls, expected {n_layers}, skipping frame {fi}")
            continue

        for layer_idx in range(n_layers):
            attn = captured_attn[layer_idx]  # [1, heads, seq, seq]

            text_to_vis = attn[:, :, N_VIS:, :N_VIS]
            full_attn_row = attn[:, :, N_VIS:, :]

            v_frac = (text_to_vis.sum(dim=-1) / full_attn_row.sum(dim=-1).clamp(min=1e-10)).mean().item()

            vis_norm = text_to_vis / text_to_vis.sum(dim=-1, keepdim=True).clamp(min=1e-10)
            ent = -(vis_norm * torch.log(vis_norm + 1e-10)).sum(dim=-1)
            ent_ratio = (ent / math.log(N_VIS)).mean().item()

            per_layer_ent[layer_idx].append(ent_ratio)
            per_layer_vfrac[layer_idx].append(v_frac)

        if (fi + 1) % 20 == 0 or fi == 0:
            print(f"  Processed {fi+1}/{len(frames)} frames")

    # ── Aggregate ──────────────────────────────────────────
    results = {
        "model": "π0.5 (Gemma-2B backbone)",
        "dataset": "LIBERO-Object (task_index 20-29)",
        "n_images": len(frames),
        "n_tasks": n_tasks,
        "architecture": {
            "vision_encoder": "SigLIP So400m/14",
            "connector": f"Linear projection → Gemma-2B (hidden_size={hidden_size})",
            "vlm_backbone": f"Gemma-2B ({n_layers} layers)",
            "vision_tokens": N_VIS,
            "vision_tokens_per_image": N_VIS_PER_IMAGE,
            "n_image_slots": N_IMAGES,
        },
        "methodology": (
            "Per-layer attention entropy: for each Gemma-2B layer, measure how uniformly "
            "text query tokens attend to vision key tokens. Entropy is normalized by "
            f"log({N_VIS})={math.log(N_VIS):.4f}. Ratio=1.0 means perfectly uniform attention."
        ),
        "per_layer_entropy_ratio": {},
        "per_layer_entropy_std": {},
        "per_layer_vision_attention_fraction": {},
    }

    all_ent = []
    for L in range(n_layers):
        vals = per_layer_ent[L]
        if vals:
            results["per_layer_entropy_ratio"][str(L)] = round(float(np.mean(vals)), 4)
            results["per_layer_entropy_std"][str(L)] = round(float(np.std(vals)), 4)
            results["per_layer_vision_attention_fraction"][str(L)] = round(
                float(np.mean(per_layer_vfrac[L])), 4)
            all_ent.extend(vals)

    results["overall_entropy_ratio"] = round(float(np.mean(all_ent)), 4)
    results["overall_entropy_std"] = round(float(np.std(all_ent)), 4)

    out_path = "/root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_attention_entropy_perlayer.json"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)

    print(f"\nResults saved to {out_path}")
    print(f"Overall entropy ratio: {results['overall_entropy_ratio']:.4f} ± {results['overall_entropy_std']:.4f}")
    print(f"\nComparison:")
    print(f"  SmolVLA (pixel-shuffle):  0.9521")
    print(f"  X-VLA (linear):           0.6138")
    print(f"  π0.5 (this, linear):      {results['overall_entropy_ratio']:.4f}")
    print(f"\nPer-layer breakdown:")
    for L in range(n_layers):
        if str(L) in results["per_layer_entropy_ratio"]:
            e = results["per_layer_entropy_ratio"][str(L)]
            s = results["per_layer_entropy_std"][str(L)]
            v = results["per_layer_vision_attention_fraction"][str(L)]
            print(f"  L{L:2d}: entropy={e:.4f} ± {s:.4f}  vis_frac={v:.4f}")


if __name__ == "__main__":
    main()
