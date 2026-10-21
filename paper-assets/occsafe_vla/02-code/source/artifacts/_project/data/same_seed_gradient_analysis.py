"""
Same-seed gradient analysis for OccSafe-VLA 4-condition ablation (seed=42).

Runs one condition at a time. Each run produces a JSON with per-layer gradient
stats and BN drift data. Use plot_gradient_comparison.py to compare results.

Usage:
  # Full OCC + BN
  python same_seed_gradient_analysis.py \
    --checkpoint_path /root/autodl-tmp/checkpoints/ablation_occ_s0/.../50000_chkpt \
    --condition_name full_occ_bn \
    --occ_detach false --occ_norm bn \
    --output_dir /root/occsafe_vla/analysis/same_seed_results

  # Detach + BN
  python same_seed_gradient_analysis.py \
    --checkpoint_path /root/autodl-tmp/checkpoints/ablation_occ_detach_s0_retrain/.../50000_chkpt \
    --condition_name detach_bn \
    --occ_detach true --occ_norm bn \
    --output_dir /root/occsafe_vla/analysis/same_seed_results

  # Full OCC + LN
  python same_seed_gradient_analysis.py \
    --checkpoint_path /root/autodl-tmp/checkpoints/full_occ_ln_s0/.../50000_chkpt \
    --condition_name full_occ_ln \
    --occ_detach false --occ_norm ln \
    --output_dir /root/occsafe_vla/analysis/same_seed_results

  # Detach + LN
  python same_seed_gradient_analysis.py \
    --checkpoint_path /root/autodl-tmp/checkpoints/detach_ln_s0/.../50000_chkpt \
    --condition_name detach_ln \
    --occ_detach true --occ_norm ln \
    --output_dir /root/occsafe_vla/analysis/same_seed_results

Env: conda activate occsafe, Python 3.10+, PyTorch 2.x
Server: /root/occsafe_vla/openvla-oft
"""

import argparse
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


def parse_args():
    parser = argparse.ArgumentParser(description="Same-seed gradient analysis for OccSafe-VLA")
    parser.add_argument("--checkpoint_path", type=str, required=True,
                        help="Path to merged checkpoint directory (with action_head, occ_head)")
    parser.add_argument("--condition_name", type=str, required=True,
                        help="Condition label: full_occ_bn / detach_bn / full_occ_ln / detach_ln")
    parser.add_argument("--occ_detach", type=str, default="false",
                        help="Whether occ gradients are detached from backbone")
    parser.add_argument("--occ_norm", type=str, choices=["bn", "ln"], default="bn",
                        help="OCC head norm type: bn (BatchNorm) or ln (GroupNorm-1)")
    parser.add_argument("--data_root", type=str,
                        default="/root/autodl-tmp/data/modified_libero_rlds",
                        help="Root directory of RLDS datasets")
    parser.add_argument("--dataset_name", type=str, default="libero_spatial_no_noops")
    parser.add_argument("--occ_data_dir", type=str,
                        default="/root/occsafe_vla/occ_data",
                        help="Path to BEV occupancy label HDF5 files")
    parser.add_argument("--num_batches", type=int, default=200,
                        help="Number of validation batches to process")
    parser.add_argument("--batch_size", type=int, default=4)
    parser.add_argument("--seed", type=int, default=42,
                        help="Random seed for data sampling (must match across conditions)")
    parser.add_argument("--gpu", type=int, default=0)
    parser.add_argument("--output_dir", type=str, required=True)
    return parser.parse_args()


def get_layer_groups(model):
    """Group vision backbone parameters by encoder block."""
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
    """Compute L2 norm and flattened gradient vector per layer group."""
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


def extract_bn_stats(occ_head):
    """Extract BatchNorm running statistics from the occ head.

    Returns dict with layer_name -> {running_mean, running_var, num_batches_tracked}.
    Only applicable when occ_head uses BatchNorm2d (norm_type='bn').
    """
    bn_stats = {}
    for name, module in occ_head.named_modules():
        if isinstance(module, nn.BatchNorm2d):
            bn_stats[name] = {
                "running_mean": module.running_mean.cpu().tolist(),
                "running_var": module.running_var.cpu().tolist(),
                "num_batches_tracked": module.num_batches_tracked.item(),
                "weight": module.weight.data.cpu().tolist(),
                "bias": module.bias.data.cpu().tolist(),
                "mean_drift_l2": module.running_mean.float().norm().item(),
                "var_drift_from_one_l2": (module.running_var.float() - 1.0).norm().item(),
            }
    return bn_stats


def main():
    args = parse_args()
    occ_detach = args.occ_detach.lower() in ("true", "1", "yes")
    device = torch.device(f"cuda:{args.gpu}")
    os.makedirs(args.output_dir, exist_ok=True)

    # Fix seed for reproducible data sampling across conditions
    torch.manual_seed(args.seed)
    np.random.seed(args.seed)

    print(f"=== Same-Seed Gradient Analysis: {args.condition_name} ===")
    print(f"Checkpoint: {args.checkpoint_path}")
    print(f"OCC detach={occ_detach}, norm={args.occ_norm}, seed={args.seed}")
    print(f"Device: {device}")

    # ---- Load model ----
    print("\nLoading model...")
    vla = AutoModelForVision2Seq.from_pretrained(
        args.checkpoint_path, torch_dtype=torch.bfloat16,
        low_cpu_mem_usage=True, trust_remote_code=True,
    )
    vla = vla.to(device)
    vla.eval()

    for p in vla.parameters():
        p.requires_grad_(False)
    for p in vla.vision_backbone.parameters():
        p.requires_grad_(True)

    processor = AutoProcessor.from_pretrained(args.checkpoint_path, trust_remote_code=True)

    vision_embed_dim = vla.vision_backbone.embed_dim
    llm_dim = vla.config.text_config.hidden_size
    num_patches = vla.vision_backbone.get_num_patches()
    num_images = vla.vision_backbone.get_num_images_in_input()
    NUM_PATCHES_TOTAL = num_patches * num_images

    print(f"Vision embed_dim={vision_embed_dim}, LLM dim={llm_dim}")
    print(f"Patches={num_patches}, images={num_images}, total={NUM_PATCHES_TOTAL}")

    # ---- Load action head ----
    action_head = L1RegressionActionHead(
        input_dim=llm_dim, hidden_dim=llm_dim, action_dim=ACTION_DIM,
    ).to(torch.bfloat16).to(device)
    ah_ckpts = sorted(Path(args.checkpoint_path).glob("action_head--*.pt"))
    if ah_ckpts:
        sd = torch.load(ah_ckpts[0], map_location=device, weights_only=False)
        sd = {k.replace("module.", ""): v for k, v in sd.items()}
        action_head.load_state_dict(sd)
        print(f"Loaded action head: {ah_ckpts[0].name}")
    action_head.eval()
    for p in action_head.parameters():
        p.requires_grad_(False)

    # ---- Load occ head ----
    occ_head = BEVOccupancyHead(
        in_dim=vision_embed_dim, out_resolution=64,
        num_classes=1, num_patches_per_image=num_patches, norm_type=args.occ_norm,
    ).to(torch.bfloat16).to(device)
    oh_ckpts = sorted(Path(args.checkpoint_path).glob("occ_head--*.pt"))
    if oh_ckpts:
        sd = torch.load(oh_ckpts[0], map_location=device, weights_only=False)
        sd = {k.replace("module.", ""): v for k, v in sd.items()}
        occ_head.load_state_dict(sd)
        print(f"Loaded occ head: {oh_ckpts[0].name}")
    else:
        print("WARNING: No occ_head checkpoint found, using random init")
    occ_head.eval()
    for p in occ_head.parameters():
        p.requires_grad_(False)

    occ_loss_fn = FocalLoss().to(device)

    # ---- Extract BN stats before analysis ----
    bn_drift = extract_bn_stats(occ_head)
    if bn_drift:
        print(f"\nBN layers found: {len(bn_drift)}")
        for name, stats in bn_drift.items():
            print(f"  {name}: mean_drift_L2={stats['mean_drift_l2']:.4f}, "
                  f"var_drift_L2={stats['var_drift_from_one_l2']:.4f}, "
                  f"tracked={stats['num_batches_tracked']}")
    else:
        print("\nNo BatchNorm layers (norm_type=ln uses GroupNorm)")

    # ---- Data pipeline ----
    print("\nSetting up data pipeline...")
    action_tokenizer = ActionTokenizer(processor.tokenizer)
    batch_transform = RLDSBatchTransform(
        action_tokenizer,
        processor.tokenizer,
        image_transform=processor.image_processor.apply_transform,
        prompt_builder_fn=PurePromptBuilder,
        occ_data_dir=args.occ_data_dir,
        occ_resolution=64,
    )
    dataset = RLDSDataset(
        args.data_root, args.dataset_name, batch_transform,
        resize_resolution=tuple(vla.config.image_sizes),
        shuffle_buffer_size=10000, image_aug=False,
    )
    collator = PaddedCollatorForActionPrediction(
        processor.tokenizer.model_max_length,
        processor.tokenizer.pad_token_id,
        padding_side="right",
    )
    dataloader = DataLoader(
        dataset, batch_size=args.batch_size,
        collate_fn=collator, num_workers=0,
    )

    # ---- Layer groups ----
    layer_groups = get_layer_groups(vla)
    all_params = []
    for params in layer_groups.values():
        all_params.extend(params)
    layer_names = list(layer_groups.keys())
    n_params = sum(p.numel() for p in all_params)
    print(f"Tracking {n_params:,} parameters in {len(layer_groups)} groups")

    # ---- Storage ----
    all_action_norms = {g: [] for g in layer_names}
    all_occ_norms = {g: [] for g in layer_names}
    all_cosine = {g: [] for g in layer_names}
    batch_stats = []

    # ---- Main loop ----
    print(f"\nStarting gradient analysis ({args.num_batches} batches, bs={args.batch_size})...\n")
    t0 = time.time()

    for batch_idx, batch in enumerate(dataloader):
        if batch_idx >= args.num_batches:
            break

        try:
            # Forward pass
            with torch.amp.autocast("cuda", dtype=torch.bfloat16):
                output = vla(
                    input_ids=batch["input_ids"].to(device),
                    attention_mask=batch["attention_mask"].to(device),
                    pixel_values=batch["pixel_values"].to(torch.bfloat16).to(device),
                    labels=batch["labels"].to(device),
                    output_hidden_states=True,
                )

            # ---- Action loss ----
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

            # ---- OCC loss ----
            patch_features = vla._cached_patch_features
            pf = patch_features.detach() if occ_detach else patch_features
            occ_logits = occ_head(pf.to(torch.bfloat16))
            occ_targets = batch["occ_labels"].to(device).float()
            occ_loss = occ_loss_fn(occ_logits.float(), occ_targets)

            # ---- Action gradients ----
            action_grads = torch.autograd.grad(
                action_loss.float(), all_params,
                retain_graph=(not occ_detach), allow_unused=True,
            )
            action_norms, action_vecs = compute_per_layer_grads(action_grads, layer_groups)

            # ---- OCC gradients (only for non-detach conditions) ----
            occ_norms = {}
            cosines = {}
            if not occ_detach:
                try:
                    occ_grads = torch.autograd.grad(
                        occ_loss.float(), all_params,
                        retain_graph=False, allow_unused=True,
                    )
                    occ_norms, occ_vecs = compute_per_layer_grads(occ_grads, layer_groups)
                    for g in layer_names:
                        av, ov = action_vecs.get(g), occ_vecs.get(g)
                        if av is not None and ov is not None:
                            cosines[g] = nn.functional.cosine_similarity(
                                av.unsqueeze(0), ov.unsqueeze(0),
                            ).item()
                        else:
                            cosines[g] = float("nan")
                except RuntimeError as e:
                    print(f"  [batch {batch_idx}] occ grad error: {e}")
                    for g in layer_names:
                        occ_norms[g] = 0.0
                        cosines[g] = float("nan")
            else:
                for g in layer_names:
                    occ_norms[g] = 0.0
                    cosines[g] = float("nan")

            # ---- Record ----
            batch_stats.append({
                "batch_idx": batch_idx,
                "action_loss": action_loss.item(),
                "occ_loss": occ_loss.item(),
            })
            for g in layer_names:
                all_action_norms[g].append(action_norms.get(g, 0))
                all_occ_norms[g].append(occ_norms.get(g, 0))
                all_cosine[g].append(cosines.get(g, float("nan")))

            if batch_idx % 10 == 0:
                elapsed = time.time() - t0
                avg_an = np.mean(list(action_norms.values()))
                mem = torch.cuda.max_memory_allocated(device) / 1e9
                print(f"  [{batch_idx:>4d}/{args.num_batches}] "
                      f"act={action_loss.item():.4f} occ={occ_loss.item():.4f} "
                      f"avg_grad={avg_an:.6f} mem={mem:.1f}GB t={elapsed:.0f}s")

        except Exception as e:
            print(f"  [batch {batch_idx}] ERROR: {e}")
            import traceback; traceback.print_exc()
            continue

    total_batches = len(batch_stats)
    total_time = time.time() - t0
    print(f"\nCompleted {total_batches} batches in {total_time:.0f}s ({total_time/60:.1f} min)")

    # ---- Aggregate ----
    summary = {
        "condition": args.condition_name,
        "occ_detach": occ_detach,
        "occ_norm": args.occ_norm,
        "seed": args.seed,
        "checkpoint_path": args.checkpoint_path,
        "num_batches": total_batches,
        "batch_size": args.batch_size,
        "avg_action_loss": float(np.mean([b["action_loss"] for b in batch_stats])),
        "avg_occ_loss": float(np.mean([b["occ_loss"] for b in batch_stats])),
        "total_time_sec": total_time,
        "bn_drift": bn_drift,
        "per_layer": {},
    }

    for g in layer_names:
        an = all_action_norms[g]
        on = all_occ_norms[g]
        cs = [c for c in all_cosine[g] if not np.isnan(c)]
        summary["per_layer"][g] = {
            "action_grad_norm_mean": float(np.mean(an)),
            "action_grad_norm_std": float(np.std(an)),
            "occ_grad_norm_mean": float(np.mean(on)),
            "occ_grad_norm_std": float(np.std(on)),
            "cosine_sim_mean": float(np.mean(cs)) if cs else None,
            "cosine_sim_std": float(np.std(cs)) if cs else None,
            "conflict_rate": float(sum(1 for c in cs if c < 0) / len(cs)) if cs else None,
        }

    # ---- Save ----
    out_json = os.path.join(args.output_dir, f"{args.condition_name}_gradient_stats.json")
    with open(out_json, "w") as f:
        json.dump(summary, f, indent=2)
    print(f"Saved summary: {out_json}")

    raw_json = os.path.join(args.output_dir, f"{args.condition_name}_gradient_raw.json")
    raw = {
        "batch_stats": batch_stats,
        "action_norms": dict(all_action_norms),
        "occ_norms": dict(all_occ_norms),
        "cosine_sims": {g: [x if not np.isnan(x) else None for x in v]
                        for g, v in all_cosine.items()},
    }
    with open(raw_json, "w") as f:
        json.dump(raw, f, indent=2)
    print(f"Saved raw data: {raw_json}")

    # ---- Summary table ----
    print(f"\n{'='*80}")
    print(f"SUMMARY: {args.condition_name} (detach={occ_detach}, norm={args.occ_norm})")
    print(f"{'='*80}")
    print(f"Avg action loss: {summary['avg_action_loss']:.4f}")
    print(f"Avg occ loss:    {summary['avg_occ_loss']:.4f}")
    print(f"\n{'Layer':<35s} {'ActGrad':>10s} {'OccGrad':>10s} {'Cosine':>10s} {'Conflict':>10s}")
    print("-" * 80)
    for g in layer_names:
        s = summary["per_layer"][g]
        cos_str = f"{s['cosine_sim_mean']:.4f}" if s["cosine_sim_mean"] is not None else "N/A"
        conf_str = f"{s['conflict_rate']:.2%}" if s["conflict_rate"] is not None else "N/A"
        print(f"{g:<35s} {s['action_grad_norm_mean']:>10.6f} {s['occ_grad_norm_mean']:>10.6f} "
              f"{cos_str:>10s} {conf_str:>10s}")
    print(f"{'='*80}")

    if bn_drift:
        print(f"\nBN Running Stats Drift (from init: mean=0, var=1):")
        for name, stats in bn_drift.items():
            print(f"  {name}: mean_drift_L2={stats['mean_drift_l2']:.4f}, "
                  f"var_drift_L2={stats['var_drift_from_one_l2']:.4f}")

    print(f"\nDone. Results saved to {args.output_dir}")


if __name__ == "__main__":
    main()
