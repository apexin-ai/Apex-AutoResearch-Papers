#!/usr/bin/env python3
"""Gradient dose-response analysis for OccSafe-VLA cutoff conditions.

Compares per-layer gradient norms and action-occ cosine similarity across:
vanilla, full_occ, cutoff_15k, cutoff_25k, reverse_cutoff.
"""

import gc
import json
import os
import sys
import time
from collections import OrderedDict
from pathlib import Path

import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import DataLoader

sys.path.insert(0, "/root/occsafe_vla/openvla-oft")

from transformers import AutoModelForVision2Seq, AutoProcessor
from prismatic.models.occ_head import BEVOccupancyHead, FocalLoss
from prismatic.models.action_heads import L1RegressionActionHead
from prismatic.models.backbones.llm.prompting import PurePromptBuilder
from prismatic.vla.action_tokenizer import ActionTokenizer
from prismatic.vla.constants import ACTION_DIM, NUM_ACTIONS_CHUNK
from prismatic.vla.datasets import RLDSBatchTransform, RLDSDataset
from prismatic.util.data_utils import PaddedCollatorForActionPrediction
from prismatic.training.train_utils import get_current_action_mask, get_next_actions_mask

# ---- Configuration ----
GPU = 1
NUM_BATCHES = 200
BATCH_SIZE = 4
OCC_NORM = "bn"
DATA_ROOT = "/root/autodl-tmp/data/modified_libero_rlds"
DATASET_NAME = "libero_spatial_no_noops"
OCC_DATA_DIR = "/root/occsafe_vla/occ_data"
OUTPUT_DIR = "/root/autodl-tmp/analysis/gradient_dose_response"

CKPT_BASE = "/root/autodl-tmp/checkpoints"

CONDITIONS = OrderedDict([
    ("vanilla", {
        "path": f"{CKPT_BASE}/vanilla_retrain_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt",
        "step": 50000,
        "label": "Vanilla",
    }),
    ("full_occ", {
        "path": f"{CKPT_BASE}/full_occ_retrain_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt",
        "step": 50000,
        "label": "Full OCC",
    }),
    ("cutoff_15k", {
        "path": f"{CKPT_BASE}/cutoff_15k_s1/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--cutoff_15k_s1--50000_chkpt",
        "step": 50000,
        "label": "Cutoff 15K",
    }),
    ("cutoff_25k", {
        "path": f"{CKPT_BASE}/cutoff_25k_s2/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--cutoff_25k_s2--30000_chkpt",
        "step": 30000,
        "label": "Cutoff 25K†",
    }),
    ("reverse_cutoff", {
        "path": f"{CKPT_BASE}/reverse_cutoff_s2/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--reverse_cutoff_s2--30000_chkpt",
        "step": 30000,
        "label": "Reverse Cutoff†",
    }),
])


def get_layer_groups(model):
    groups = OrderedDict()
    for name, param in model.vision_backbone.named_parameters():
        parts = name.split(".")
        if "blocks" in parts:
            idx = parts.index("blocks")
            group = ".".join(parts[:idx + 2])
        else:
            prefix = parts[0] if parts[0] in ("featurizer", "fused_featurizer") else "other"
            group = prefix + ".stem"
        if group not in groups:
            groups[group] = []
        groups[group].append(param)
    return groups


def compute_per_layer_grads(grads, layer_groups):
    norms = {}
    vectors = {}
    idx = 0
    for group_name, params in layer_groups.items():
        parts = []
        for _ in params:
            g = grads[idx]
            if g is not None:
                parts.append(g.flatten().float())
            idx += 1
        if parts:
            vec = torch.cat(parts)
            norms[group_name] = vec.norm().item()
            vectors[group_name] = vec
        else:
            norms[group_name] = 0.0
            vectors[group_name] = None
    return norms, vectors


def analyze_condition(cond_name, cond_info, device, batches):
    print(f"\n{'='*60}")
    print(f"Analyzing: {cond_info['label']} ({cond_name})")
    print(f"Checkpoint: {cond_info['path']}")
    print(f"Step: {cond_info['step']}")
    print(f"{'='*60}")

    vla = AutoModelForVision2Seq.from_pretrained(
        cond_info["path"], torch_dtype=torch.bfloat16,
        low_cpu_mem_usage=True, trust_remote_code=True,
    )
    vla = vla.to(device)
    vla.eval()

    for p in vla.parameters():
        p.requires_grad_(False)
    for p in vla.vision_backbone.parameters():
        p.requires_grad_(True)

    vision_embed_dim = vla.vision_backbone.embed_dim
    llm_dim = vla.config.text_config.hidden_size
    num_patches = vla.vision_backbone.get_num_patches()
    num_images = vla.vision_backbone.get_num_images_in_input()
    NUM_PATCHES_TOTAL = num_patches * num_images

    print(f"Vision embed_dim={vision_embed_dim}, LLM dim={llm_dim}")
    print(f"Patches={num_patches}, images={num_images}, total={NUM_PATCHES_TOTAL}")

    # Action head
    action_head = L1RegressionActionHead(
        input_dim=llm_dim, hidden_dim=llm_dim, action_dim=ACTION_DIM,
    ).to(torch.bfloat16).to(device)
    ah_ckpts = sorted(Path(cond_info["path"]).glob("action_head--*.pt"))
    if ah_ckpts:
        sd = torch.load(ah_ckpts[0], map_location=device, weights_only=False)
        sd = {k.replace("module.", ""): v for k, v in sd.items()}
        action_head.load_state_dict(sd)
        print(f"Loaded action head: {ah_ckpts[0].name}")
    action_head.eval()
    for p in action_head.parameters():
        p.requires_grad_(False)

    # OCC head
    occ_head = BEVOccupancyHead(
        in_dim=vision_embed_dim, out_resolution=64,
        num_classes=1, num_patches_per_image=num_patches, norm_type=OCC_NORM,
    ).to(torch.bfloat16).to(device)
    oh_ckpts = sorted(Path(cond_info["path"]).glob("occ_head--*.pt"))
    if oh_ckpts:
        sd = torch.load(oh_ckpts[0], map_location=device, weights_only=False)
        sd = {k.replace("module.", ""): v for k, v in sd.items()}
        occ_head.load_state_dict(sd)
        print(f"Loaded occ head: {oh_ckpts[0].name}")
    else:
        print("WARNING: No occ_head checkpoint, using random init")
    occ_head.eval()
    for p in occ_head.parameters():
        p.requires_grad_(False)

    occ_loss_fn = FocalLoss().to(device)

    layer_groups = get_layer_groups(vla)
    all_params = []
    for params in layer_groups.values():
        all_params.extend(params)
    layer_names = list(layer_groups.keys())
    n_params = sum(p.numel() for p in all_params)
    print(f"Tracking {n_params:,} parameters in {len(layer_groups)} groups")

    all_action_norms = {g: [] for g in layer_names}
    all_occ_norms = {g: [] for g in layer_names}
    all_cosine = {g: [] for g in layer_names}
    batch_losses = []

    t0 = time.time()
    for batch_idx, batch in enumerate(batches):
        try:
            with torch.amp.autocast("cuda", dtype=torch.bfloat16):
                output = vla(
                    input_ids=batch["input_ids"].to(device),
                    attention_mask=batch["attention_mask"].to(device),
                    pixel_values=batch["pixel_values"].to(torch.bfloat16).to(device),
                    labels=batch["labels"].to(device),
                    output_hidden_states=True,
                )

            last_hidden = output.hidden_states[-1]
            text_hidden = last_hidden[:, NUM_PATCHES_TOTAL:-1]
            gt_token_ids = batch["labels"][:, 1:].to(device)
            cur_mask = get_current_action_mask(gt_token_ids)
            nxt_mask = get_next_actions_mask(gt_token_ids)
            all_mask = cur_mask | nxt_mask

            bs = batch["input_ids"].shape[0]
            actions_hidden = (
                text_hidden[all_mask]
                .reshape(bs, NUM_ACTIONS_CHUNK * ACTION_DIM, -1)
                .to(torch.bfloat16)
            )
            gt_actions = batch["actions"].to(device).to(torch.bfloat16)
            pred_actions = action_head.predict_action(actions_hidden)
            action_loss = nn.L1Loss()(gt_actions, pred_actions)

            patch_features = vla._cached_patch_features
            occ_logits = occ_head(patch_features.to(torch.bfloat16))
            occ_targets = batch["occ_labels"].to(device).float()
            occ_loss = occ_loss_fn(occ_logits.float(), occ_targets)

            action_grads = torch.autograd.grad(
                action_loss.float(), all_params,
                retain_graph=True, allow_unused=True,
            )
            action_norms, action_vecs = compute_per_layer_grads(action_grads, layer_groups)

            occ_grads = torch.autograd.grad(
                occ_loss.float(), all_params,
                retain_graph=False, allow_unused=True,
            )
            occ_norms, occ_vecs = compute_per_layer_grads(occ_grads, layer_groups)

            cosines = {}
            for g in layer_names:
                av, ov = action_vecs.get(g), occ_vecs.get(g)
                if av is not None and ov is not None:
                    cosines[g] = nn.functional.cosine_similarity(
                        av.unsqueeze(0), ov.unsqueeze(0),
                    ).item()
                else:
                    cosines[g] = float("nan")

            batch_losses.append({
                "action_loss": action_loss.item(),
                "occ_loss": occ_loss.item(),
            })
            for g in layer_names:
                all_action_norms[g].append(action_norms.get(g, 0))
                all_occ_norms[g].append(occ_norms.get(g, 0))
                all_cosine[g].append(cosines.get(g, float("nan")))

            if batch_idx % 20 == 0:
                elapsed = time.time() - t0
                print(f"  Batch {batch_idx}/{len(batches)}: "
                      f"act={action_loss.item():.4f}, occ={occ_loss.item():.4f} "
                      f"[{elapsed:.1f}s]")

        except Exception as e:
            print(f"  [batch {batch_idx}] ERROR: {e}")
            import traceback
            traceback.print_exc()
            continue

    elapsed = time.time() - t0
    print(f"  Done: {len(batch_losses)}/{len(batches)} batches in {elapsed:.1f}s")

    stats = OrderedDict()
    for g in layer_names:
        an = np.array(all_action_norms[g])
        on = np.array(all_occ_norms[g])
        cs = np.array(all_cosine[g])
        cs_valid = cs[~np.isnan(cs)]
        stats[g] = {
            "action_grad_norm_mean": float(np.mean(an)) if len(an) > 0 else 0.0,
            "action_grad_norm_std": float(np.std(an)) if len(an) > 0 else 0.0,
            "occ_grad_norm_mean": float(np.mean(on)) if len(on) > 0 else 0.0,
            "occ_grad_norm_std": float(np.std(on)) if len(on) > 0 else 0.0,
            "cosine_sim_mean": float(np.mean(cs_valid)) if len(cs_valid) > 0 else None,
            "cosine_sim_std": float(np.std(cs_valid)) if len(cs_valid) > 0 else None,
            "conflict_rate": float(np.mean(cs_valid < 0)) if len(cs_valid) > 0 else None,
        }

    avg_action_loss = np.mean([b["action_loss"] for b in batch_losses]) if batch_losses else 0
    avg_occ_loss = np.mean([b["occ_loss"] for b in batch_losses]) if batch_losses else 0

    result = {
        "condition": cond_name,
        "label": cond_info["label"],
        "step": cond_info["step"],
        "num_batches": len(batch_losses),
        "avg_action_loss": float(avg_action_loss),
        "avg_occ_loss": float(avg_occ_loss),
        "per_layer": stats,
    }

    del vla, action_head, occ_head, occ_loss_fn
    gc.collect()
    torch.cuda.empty_cache()

    return result


def extract_block_idx(name):
    parts = name.split(".")
    for i, p in enumerate(parts):
        if p == "blocks" and i + 1 < len(parts):
            return int(parts[i + 1])
    return -1


def create_comparison_plots(results, output_dir):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    os.makedirs(output_dir, exist_ok=True)

    colors = {
        "vanilla": "#1f77b4",
        "full_occ": "#d62728",
        "cutoff_15k": "#ff7f0e",
        "cutoff_25k": "#2ca02c",
        "reverse_cutoff": "#9467bd",
    }

    first = list(results.values())[0]
    layer_names = list(first["per_layer"].keys())

    dino_layers = [(i, n) for i, n in enumerate(layer_names) if "fused_featurizer.blocks" in n]
    siglip_layers = [(i, n) for i, n in enumerate(layer_names) if n.startswith("featurizer.blocks")]

    for backbone_name, backbone_layers in [("DINOv2", dino_layers), ("SigLIP", siglip_layers)]:
        if not backbone_layers:
            continue

        fig, axes = plt.subplots(2, 2, figsize=(16, 12))
        fig.suptitle(f"Gradient Dose-Response Analysis ({backbone_name} Backbone)",
                     fontsize=16, fontweight="bold")

        for cond_name, res in results.items():
            stats = res["per_layer"]
            xs = [extract_block_idx(n) for _, n in backbone_layers]
            label = res["label"]
            color = colors[cond_name]

            ys_act = [stats[n]["action_grad_norm_mean"] for _, n in backbone_layers]
            axes[0, 0].plot(xs, ys_act, "o-", color=color, label=label,
                            markersize=3, linewidth=1.5)

            ys_occ = [stats[n]["occ_grad_norm_mean"] for _, n in backbone_layers]
            axes[0, 1].plot(xs, ys_occ, "o-", color=color, label=label,
                            markersize=3, linewidth=1.5)

            ys_cos = [stats[n]["cosine_sim_mean"] for _, n in backbone_layers]
            ys_cos = [y if y is not None else float("nan") for y in ys_cos]
            axes[1, 0].plot(xs, ys_cos, "o-", color=color, label=label,
                            markersize=3, linewidth=1.5)

            ys_conf = [stats[n]["conflict_rate"] for _, n in backbone_layers]
            ys_conf = [y if y is not None else float("nan") for y in ys_conf]
            axes[1, 1].plot(xs, ys_conf, "o-", color=color, label=label,
                            markersize=3, linewidth=1.5)

        axes[0, 0].set_title("Action Gradient Norms")
        axes[0, 0].set_ylabel("L2 Norm (mean)")
        axes[0, 0].set_yscale("log")
        axes[0, 0].legend(fontsize=9)
        axes[0, 0].grid(True, alpha=0.3)

        axes[0, 1].set_title("OCC Gradient Norms")
        axes[0, 1].set_ylabel("L2 Norm (mean)")
        axes[0, 1].set_yscale("log")
        axes[0, 1].legend(fontsize=9)
        axes[0, 1].grid(True, alpha=0.3)

        axes[1, 0].set_title("Action–OCC Gradient Cosine Similarity")
        axes[1, 0].set_ylabel("Cosine Similarity")
        axes[1, 0].axhline(y=0, color="gray", linestyle="--", alpha=0.5)
        axes[1, 0].legend(fontsize=9)
        axes[1, 0].grid(True, alpha=0.3)

        axes[1, 1].set_title("Gradient Conflict Rate (cosine < 0)")
        axes[1, 1].set_ylabel("Conflict Rate")
        axes[1, 1].axhline(y=0.5, color="gray", linestyle="--", alpha=0.5)
        axes[1, 1].legend(fontsize=9)
        axes[1, 1].grid(True, alpha=0.3)

        for ax in axes.flat:
            ax.set_xlabel(f"{backbone_name} Block Index")

        plt.tight_layout()
        tag = backbone_name.lower().replace("v2", "v2")
        for ext in ("pdf", "png"):
            fig.savefig(os.path.join(output_dir, f"gradient_dose_response_{tag}.{ext}"),
                        dpi=150, bbox_inches="tight")
        plt.close(fig)
        print(f"Saved {backbone_name} comparison plots")

    # Summary table as text
    print("\n" + "=" * 100)
    print(f"{'Condition':<20} {'Step':>6} {'Avg Act Loss':>12} {'Avg OCC Loss':>12} "
          f"{'Mean Cosine (DINOv2)':>20} {'Conflict (DINOv2)':>18}")
    print("-" * 100)
    for name, res in results.items():
        dino_cosines = [res["per_layer"][n]["cosine_sim_mean"]
                        for _, n in dino_layers
                        if res["per_layer"][n]["cosine_sim_mean"] is not None]
        dino_conflicts = [res["per_layer"][n]["conflict_rate"]
                          for _, n in dino_layers
                          if res["per_layer"][n]["conflict_rate"] is not None]
        avg_cos = np.mean(dino_cosines) if dino_cosines else float("nan")
        avg_conf = np.mean(dino_conflicts) if dino_conflicts else float("nan")
        print(f"{res['label']:<20} {res['step']:>6} {res['avg_action_loss']:>12.4f} "
              f"{res['avg_occ_loss']:>12.4f} {avg_cos:>20.4f} {avg_conf:>18.2%}")
    print("=" * 100)
    print("† = 30K checkpoint (training did not save 50K)")


def main():
    device = torch.device(f"cuda:{GPU}")
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print("=== Gradient Dose-Response Analysis ===")
    print(f"Device: {device}")
    print(f"Conditions: {list(CONDITIONS.keys())}")
    print(f"Batches: {NUM_BATCHES}, BS: {BATCH_SIZE}")

    # Preload data batches
    print("\nPreloading data batches...")
    first_path = list(CONDITIONS.values())[0]["path"]
    processor = AutoProcessor.from_pretrained(first_path, trust_remote_code=True)

    action_tokenizer = ActionTokenizer(processor.tokenizer)
    batch_transform = RLDSBatchTransform(
        action_tokenizer,
        processor.tokenizer,
        image_transform=processor.image_processor.apply_transform,
        prompt_builder_fn=PurePromptBuilder,
        occ_data_dir=OCC_DATA_DIR,
        occ_resolution=64,
    )
    dataset = RLDSDataset(
        DATA_ROOT, DATASET_NAME, batch_transform,
        resize_resolution=(224, 224),
        shuffle_buffer_size=10000, image_aug=False,
    )
    collator = PaddedCollatorForActionPrediction(
        processor.tokenizer.model_max_length,
        processor.tokenizer.pad_token_id,
        padding_side="right",
    )
    dataloader = DataLoader(
        dataset, batch_size=BATCH_SIZE,
        collate_fn=collator, num_workers=0,
    )

    batches = []
    for i, batch in enumerate(dataloader):
        if i >= NUM_BATCHES:
            break
        cpu_batch = {}
        for k, v in batch.items():
            if isinstance(v, torch.Tensor):
                cpu_batch[k] = v.cpu()
            else:
                cpu_batch[k] = v
        batches.append(cpu_batch)
        if i % 50 == 0:
            print(f"  Loaded batch {i}/{NUM_BATCHES}")

    print(f"Preloaded {len(batches)} batches")
    del dataloader, dataset

    # Analyze each condition
    results = OrderedDict()
    for cond_name, cond_info in CONDITIONS.items():
        result = analyze_condition(cond_name, cond_info, device, batches)
        results[cond_name] = result

        with open(os.path.join(OUTPUT_DIR, f"{cond_name}_gradient_stats.json"), "w") as f:
            json.dump(result, f, indent=2)
        print(f"Saved {cond_name}_gradient_stats.json")

    # Combined results
    combined = {name: res for name, res in results.items()}
    with open(os.path.join(OUTPUT_DIR, "gradient_dose_response_results.json"), "w") as f:
        json.dump(combined, f, indent=2)

    # Plots
    create_comparison_plots(results, OUTPUT_DIR)

    print(f"\nAll results saved to {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
