#!/usr/bin/env python
"""π0 Attention Entropy Analysis — Per-Layer Attention to Vision Tokens.

Measures how much attention each layer devotes to vision tokens,
and how uniformly that attention is distributed.

Uses monkey-patching on eager_attention_forward to capture attention
weights from the dual-stream forward pass without modifying model code.
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
TOKENIZER_MAX_LENGTH = 48
ARTIFACTS_DIR = "/root/autodl-tmp/importance_margin_vla_compress/artifacts"

layer_attention_store = {}


def entropy_from_weights(attn_row):
    """Compute normalized entropy of an attention distribution."""
    p = attn_row.clamp(min=1e-12)
    ent = -(p * p.log()).sum(dim=-1)
    max_ent = np.log(attn_row.shape[-1])
    return (ent / max_ent).mean().item() if max_ent > 0 else 0.0


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
    del test_img, img_emb
    torch.cuda.empty_cache()

    n_vlm_layers = len(vlm_expert.paligemma.model.language_model.layers)
    chunk_size = policy.config.chunk_size
    max_state_dim = policy.config.max_state_dim
    max_action_dim = policy.config.max_action_dim
    empty_cameras = getattr(policy.config, "empty_cameras", 0)

    n_real_images = 2
    n_real_vis = n_vis_per_img * n_real_images
    n_total_images = n_real_images + empty_cameras
    n_total_vis = n_vis_per_img * n_total_images

    print(f"  Vision tokens/image: {n_vis_per_img}")
    print(f"  Real vision tokens: {n_real_vis}, Total: {n_total_vis}")
    print(f"  VLM layers: {n_vlm_layers}")

    # ═══ Monkey-patch eager_attention_forward ═══
    from transformers.models.gemma import modeling_gemma
    original_eager_attn = modeling_gemma.eager_attention_forward

    call_counter = [0]

    def patched_eager_attention_forward(module, query, key, value, attention_mask, scaling, **kwargs):
        attn_weights = torch.matmul(query, key.transpose(2, 3)) * scaling
        if attention_mask is not None:
            causal_mask = attention_mask
            if causal_mask.size() != attn_weights.size():
                causal_mask = causal_mask[:, :, :attn_weights.size(2), :attn_weights.size(3)]
            attn_weights = attn_weights + causal_mask
        attn_probs = F.softmax(attn_weights, dim=-1, dtype=torch.float32).to(query.dtype)

        layer_idx = call_counter[0] % n_vlm_layers
        layer_attention_store[layer_idx] = attn_probs.detach().cpu().float()
        call_counter[0] += 1

        attn_output = torch.matmul(attn_probs, value)
        attn_output = attn_output.transpose(1, 2).contiguous()
        return attn_output, attn_probs
    modeling_gemma.eager_attention_forward = patched_eager_attention_forward

    tokenizer = load_tokenizer()

    # ═══ Load data ═══
    print("\nLoading LIBERO-Object data...")
    snap = Path(
        "/root/autodl-tmp/.hf_cache/lerobot/hub/"
        "datasets--HuggingFaceVLA--libero/snapshots/"
        "86958911c0f959db2bbbdb107eb3e17c5f9c798e"
    )
    data_dir = snap / "data" / "chunk-000"
    tasks_tbl = pq.read_table(snap / "meta" / "tasks.parquet")
    task_descs = tasks_tbl.column("__index_level_0__").to_pylist()

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

    print(f"  {len(frames)} frames from {len({f['task_idx'] for f in frames})} tasks")

    # ═══ Attention Entropy Analysis ═══
    print("\n--- Attention Entropy Analysis ---")

    per_layer_metrics = defaultdict(lambda: {
        "entropy_vis2vis": [],
        "entropy_suffix2vis": [],
        "attn_mass_on_vis": [],
        "entropy_all": [],
    })

    model_dtype = vlm_expert.paligemma.model.language_model.layers[0].self_attn.q_proj.weight.dtype

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
            images.append(torch.ones_like(img1) * -1.0)
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

        n_prefix = prefix_embs.shape[1]
        n_suffix = suffix_embs.shape[1]

        if model_dtype == torch.bfloat16:
            pp = prefix_embs.to(torch.bfloat16)
            sc = suffix_embs.to(torch.bfloat16)
        else:
            pp = prefix_embs
            sc = suffix_embs

        pad_m = torch.cat([prefix_pad_masks, suffix_pad_masks], dim=1)
        att_m = torch.cat([prefix_att_masks, suffix_att_masks], dim=1)
        att_2d = make_att_2d_masks(pad_m, att_m)
        pos_ids = torch.cumsum(pad_m.long(), dim=1) - 1
        att_4d = flow._prepare_attention_masks_4d(att_2d)

        layer_attention_store.clear()
        call_counter[0] = 0

        (_, suffix_out), _ = vlm_expert.forward(
            attention_mask=att_4d,
            position_ids=pos_ids,
            past_key_values=None,
            inputs_embeds=[pp, sc],
            use_cache=False,
            adarms_cond=[None, adarms_cond],
        )

        for layer_idx in sorted(layer_attention_store.keys()):
            attn = layer_attention_store[layer_idx]  # [batch, heads, seq, seq]

            vis_start = 0
            vis_end = n_real_vis
            suffix_start = n_prefix
            suffix_end = n_prefix + n_suffix

            vis2vis_attn = attn[:, :, vis_start:vis_end, vis_start:vis_end]
            vis2vis_flat = vis2vis_attn.mean(dim=1)
            vis_entropy = entropy_from_weights(vis2vis_flat[0])

            suffix2all_attn = attn[:, :, suffix_start:suffix_end, :]
            suffix2vis = suffix2all_attn[:, :, :, vis_start:vis_end]
            attn_mass = suffix2vis.sum(dim=-1).mean().item()

            suffix2vis_normed = suffix2vis / (suffix2vis.sum(dim=-1, keepdim=True) + 1e-12)
            suffix2vis_mean = suffix2vis_normed.mean(dim=1)
            suffix_vis_entropy = entropy_from_weights(suffix2vis_mean[0])

            all_attn = attn.mean(dim=1)
            all_entropy = entropy_from_weights(all_attn[0])

            per_layer_metrics[layer_idx]["entropy_vis2vis"].append(vis_entropy)
            per_layer_metrics[layer_idx]["entropy_suffix2vis"].append(suffix_vis_entropy)
            per_layer_metrics[layer_idx]["attn_mass_on_vis"].append(attn_mass)
            per_layer_metrics[layer_idx]["entropy_all"].append(all_entropy)

    # ═══ Results ═══
    results = {
        "model": "pi0-3.3B (lerobot/pi0_libero_base)",
        "dataset": "LIBERO-Object (task_index 20-29)",
        "n_frames": len(frames),
        "vision_tokens_per_image": int(n_vis_per_img),
        "num_real_images": n_real_images,
        "total_real_vision_tokens": int(n_real_vis),
        "n_layers": n_vlm_layers,
        "analysis": "attention_entropy_per_layer",
        "metrics_description": {
            "entropy_vis2vis": "Normalized entropy of vision-to-vision attention (how uniformly vision tokens attend to each other)",
            "entropy_suffix2vis": "Normalized entropy of suffix-to-vision attention (how uniformly action tokens attend to vision tokens)",
            "attn_mass_on_vis": "Fraction of attention mass from suffix tokens directed at vision tokens",
            "entropy_all": "Normalized entropy of full attention distribution (all tokens)",
        },
        "per_layer": {},
    }

    print("\nPer-layer attention entropy:")
    print(f"{'Layer':>5} {'vis2vis_ent':>12} {'suf2vis_ent':>12} {'vis_mass':>10} {'all_ent':>10}")
    for layer_idx in sorted(per_layer_metrics.keys()):
        m = per_layer_metrics[layer_idx]
        entry = {
            "entropy_vis2vis": round(float(np.mean(m["entropy_vis2vis"])), 4),
            "entropy_suffix2vis": round(float(np.mean(m["entropy_suffix2vis"])), 4),
            "attn_mass_on_vis": round(float(np.mean(m["attn_mass_on_vis"])), 4),
            "entropy_all": round(float(np.mean(m["entropy_all"])), 4),
            "std_entropy_vis2vis": round(float(np.std(m["entropy_vis2vis"])), 4),
            "std_entropy_suffix2vis": round(float(np.std(m["entropy_suffix2vis"])), 4),
        }
        results["per_layer"][str(layer_idx)] = entry
        print(f"{layer_idx:>5} {entry['entropy_vis2vis']:>12.4f} {entry['entropy_suffix2vis']:>12.4f} {entry['attn_mass_on_vis']:>10.4f} {entry['entropy_all']:>10.4f}")

    layer_entropies = [results["per_layer"][str(i)]["entropy_suffix2vis"] for i in range(n_vlm_layers)]
    results["summary"] = {
        "mean_suffix2vis_entropy": round(float(np.mean(layer_entropies)), 4),
        "std_suffix2vis_entropy": round(float(np.std(layer_entropies)), 4),
        "min_suffix2vis_entropy": round(float(np.min(layer_entropies)), 4),
        "max_suffix2vis_entropy": round(float(np.max(layer_entropies)), 4),
        "mean_vis_attn_mass": round(float(np.mean([
            results["per_layer"][str(i)]["attn_mass_on_vis"] for i in range(n_vlm_layers)
        ])), 4),
    }

    os.makedirs(ARTIFACTS_DIR, exist_ok=True)
    out_path = os.path.join(ARTIFACTS_DIR, "pi0_attention_entropy_perlayer.json")
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)

    print(f"\nResults saved to {out_path}")
    print(f"Summary: mean_suffix2vis_entropy={results['summary']['mean_suffix2vis_entropy']:.4f}")

    modeling_gemma.eager_attention_forward = original_eager_attn


if __name__ == "__main__":
    main()
