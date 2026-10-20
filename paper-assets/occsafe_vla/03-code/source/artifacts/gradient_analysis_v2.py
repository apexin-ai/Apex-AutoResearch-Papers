#!/usr/bin/env python3
"""V2 Gradient Analysis for OccSafe-VLA 2x2 Factorial Study.

Analyzes gradient orthogonality and variance across 5 conditions:
  Cell 1: Full OCC BN  (gradient ON + BatchNorm)
  Cell 2: Full OCC LN  (gradient ON + LayerNorm)
  Cell 3: Detach BN    (gradient OFF + BatchNorm)
  Cell 4: Detach LN    (gradient OFF + LayerNorm)
  Vanilla: no auxiliary head

For each condition, computes on shared vision encoder parameters:
  a) Cosine similarity between action-loss and OCC-loss gradients
  b) L2 gradient norms for each loss
  c) Gradient variance across eval batches

Usage:
  # All 5 conditions via config JSON
  python gradient_analysis_v2.py --config conditions.json \
      --output_dir /root/occsafe_vla/artifacts/gradient_v2/

  # Single condition
  python gradient_analysis_v2.py \
      --checkpoint_dir /path/to/50000_chkpt \
      --condition_name "Cell1_FullOCC_BN" \
      --output_dir /root/occsafe_vla/artifacts/gradient_v2/

Config JSON format:
  {
    "Cell1_FullOCC_BN": {"checkpoint_dir": "/path/to/ckpt"},
    "Cell2_FullOCC_LN": {"checkpoint_dir": "/path/to/ckpt"},
    "Cell3_Detach_BN":  {"checkpoint_dir": "/path/to/ckpt"},
    "Cell4_Detach_LN":  {"checkpoint_dir": "/path/to/ckpt"},
    "Vanilla":          {"checkpoint_dir": "/path/to/ckpt"}
  }
"""

import argparse
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
import torch.nn.functional as F
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

os.environ["TOKENIZERS_PARALLELISM"] = "false"


def parse_args():
    parser = argparse.ArgumentParser(description="V2 Gradient Analysis for OccSafe-VLA factorial study")
    g = parser.add_mutually_exclusive_group(required=True)
    g.add_argument("--config", type=str, help="JSON config with all conditions")
    g.add_argument("--checkpoint_dir", type=str, help="Single checkpoint directory")

    parser.add_argument("--condition_name", type=str, default=None,
                        help="Condition label (required in single-condition mode)")
    parser.add_argument("--output_dir", type=str, required=True)
    parser.add_argument("--data_dir", type=str,
                        default="/root/autodl-tmp/data/modified_libero_rlds/libero_spatial_no_noops")
    parser.add_argument("--occ_data_dir", type=str, default="/root/occsafe_vla/occ_data")
    parser.add_argument("--num_batches", type=int, default=200,
                        help="Number of eval batches per condition")
    parser.add_argument("--batch_size", type=int, default=4)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--gpu", type=int, default=0)
    return parser.parse_args()


# ---------------------------------------------------------------------------
# Condition detection
# ---------------------------------------------------------------------------

def detect_condition_settings(condition_name, checkpoint_dir):
    """Auto-detect occ_detach, occ_norm, is_vanilla from name and checkpoint."""
    cond = condition_name.lower()
    ckpt_dir = Path(checkpoint_dir)

    if "vanilla" in cond:
        return True, "ln", False, True

    has_occ_head = len(list(ckpt_dir.glob("occ_head--*.pt"))) > 0
    if not has_occ_head:
        return True, "ln", False, True

    occ_detach = "detach" in cond
    occ_norm = "bn" if "bn" in cond.replace("vanilla", "") else "ln"

    return occ_detach, occ_norm, has_occ_head, False


# ---------------------------------------------------------------------------
# Encoder parameter groups
# ---------------------------------------------------------------------------

def get_encoder_params(model):
    """Get flat list of vision encoder params with requires_grad=True."""
    params = []
    for p in model.vision_backbone.parameters():
        p.requires_grad_(True)
        params.append(p)
    return params


def get_layer_groups(model):
    """Group vision backbone params by transformer block."""
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


# ---------------------------------------------------------------------------
# Model loading
# ---------------------------------------------------------------------------

def load_model_and_heads(checkpoint_dir, occ_norm, has_occ_head, device):
    """Load VLA model, action head, and OCC head from checkpoint."""
    ckpt = Path(checkpoint_dir)

    vla = AutoModelForVision2Seq.from_pretrained(
        checkpoint_dir, torch_dtype=torch.bfloat16,
        low_cpu_mem_usage=True, trust_remote_code=True,
    ).to(device)
    vla.eval()

    for p in vla.parameters():
        p.requires_grad_(False)

    processor = AutoProcessor.from_pretrained(checkpoint_dir, trust_remote_code=True)

    llm_dim = vla.config.text_config.hidden_size
    vision_dim = vla.vision_backbone.embed_dim
    num_patches = vla.vision_backbone.get_num_patches()
    num_images = vla.vision_backbone.get_num_images_in_input()

    action_head = L1RegressionActionHead(
        input_dim=llm_dim, hidden_dim=llm_dim, action_dim=ACTION_DIM,
    ).to(torch.bfloat16).to(device)
    ah_ckpts = sorted(ckpt.glob("action_head--*.pt"))
    if ah_ckpts:
        sd = torch.load(ah_ckpts[0], map_location=device, weights_only=False)
        sd = {k.replace("module.", ""): v for k, v in sd.items()}
        action_head.load_state_dict(sd)
    action_head.eval()
    for p in action_head.parameters():
        p.requires_grad_(False)

    occ_head = None
    occ_loss_fn = None
    if has_occ_head:
        proj_dim = vision_dim * (2 if vla.vision_backbone.use_fused_vision_backbone else 1)
        occ_head = BEVOccupancyHead(
            in_dim=proj_dim, out_resolution=64, num_classes=1,
            hidden_dim=256, num_patches_per_image=256, norm_type=occ_norm,
        ).to(torch.bfloat16).to(device)
        oh_ckpts = sorted(ckpt.glob("occ_head--*.pt"))
        if oh_ckpts:
            sd = torch.load(oh_ckpts[0], map_location=device, weights_only=False)
            sd = {k.replace("module.", ""): v for k, v in sd.items()}
            occ_head.load_state_dict(sd)
        occ_head.eval()
        for p in occ_head.parameters():
            p.requires_grad_(False)
        occ_loss_fn = FocalLoss().to(device)

    return vla, processor, action_head, occ_head, occ_loss_fn, num_patches * num_images


# ---------------------------------------------------------------------------
# Data pipeline
# ---------------------------------------------------------------------------

def make_dataloader(data_dir, occ_data_dir, processor, has_occ_head, vla, batch_size):
    data_root = str(Path(data_dir).parent)
    dataset_name = Path(data_dir).name

    action_tokenizer = ActionTokenizer(processor.tokenizer)
    batch_transform = RLDSBatchTransform(
        action_tokenizer,
        processor.tokenizer,
        image_transform=processor.image_processor.apply_transform,
        prompt_builder_fn=PurePromptBuilder,
        occ_data_dir=occ_data_dir if has_occ_head else None,
        occ_resolution=64,
    )
    dataset = RLDSDataset(
        data_root, dataset_name, batch_transform,
        resize_resolution=tuple(vla.config.image_sizes),
        shuffle_buffer_size=10000, image_aug=False,
    )
    collator = PaddedCollatorForActionPrediction(
        processor.tokenizer.model_max_length,
        processor.tokenizer.pad_token_id,
        padding_side="right",
    )
    return DataLoader(dataset, batch_size=batch_size, collate_fn=collator, num_workers=0)


# ---------------------------------------------------------------------------
# Gradient computation for one condition
# ---------------------------------------------------------------------------

def analyze_condition(condition_name, checkpoint_dir, args, device):
    """Run gradient analysis for a single condition. Returns results dict."""
    print(f"\n{'='*70}")
    print(f"CONDITION: {condition_name}")
    print(f"Checkpoint: {checkpoint_dir}")
    print(f"{'='*70}")

    occ_detach, occ_norm, has_occ_head, is_vanilla = detect_condition_settings(
        condition_name, checkpoint_dir
    )
    print(f"Settings: occ_detach={occ_detach}, occ_norm={occ_norm}, "
          f"has_occ={has_occ_head}, vanilla={is_vanilla}")

    torch.manual_seed(args.seed)
    np.random.seed(args.seed)

    vla, processor, action_head, occ_head, occ_loss_fn, NUM_PATCHES = load_model_and_heads(
        checkpoint_dir, occ_norm, has_occ_head, device
    )
    encoder_params = get_encoder_params(vla)
    layer_groups = get_layer_groups(vla)
    layer_names = list(layer_groups.keys())
    n_enc_params = sum(p.numel() for p in encoder_params)
    print(f"Encoder: {n_enc_params:,} params, {len(layer_groups)} layer groups")

    dataloader = make_dataloader(
        args.data_dir, args.occ_data_dir, processor,
        has_occ_head, vla, args.batch_size
    )

    # Storage: per-batch metrics
    batch_action_losses = []
    batch_occ_losses = []
    # Aggregate encoder-level
    agg_action_norms = []
    agg_occ_norms = []
    agg_cosines = []
    # Per-layer
    layer_action_norms = {g: [] for g in layer_names}
    layer_occ_norms = {g: [] for g in layer_names}
    layer_cosines = {g: [] for g in layer_names}

    t0 = time.time()
    print(f"\nRunning {args.num_batches} batches (bs={args.batch_size})...\n")

    for batch_idx, batch in enumerate(dataloader):
        if batch_idx >= args.num_batches:
            break

        try:
            with torch.amp.autocast("cuda", dtype=torch.bfloat16):
                output = vla(
                    input_ids=batch["input_ids"].to(device),
                    attention_mask=batch["attention_mask"].to(device),
                    pixel_values=batch["pixel_values"].to(torch.bfloat16).to(device),
                    labels=batch["labels"].to(device),
                    output_hidden_states=True,
                )

            # Action loss
            last_hidden = output.hidden_states[-1]
            text_hidden = last_hidden[:, NUM_PATCHES:-1]
            gt_token_ids = batch["labels"][:, 1:].to(device)
            cur_mask = get_current_action_mask(gt_token_ids)
            nxt_mask = get_next_actions_mask(gt_token_ids)

            bs = batch["input_ids"].shape[0]
            actions_hidden = (
                text_hidden[cur_mask | nxt_mask]
                .reshape(bs, NUM_ACTIONS_CHUNK * ACTION_DIM, -1)
                .to(torch.bfloat16)
            )
            gt_actions = batch["actions"].to(device).to(torch.bfloat16)
            pred_actions = action_head.predict_action(actions_hidden)
            action_loss = nn.L1Loss()(gt_actions, pred_actions)

            # OCC loss
            occ_loss = torch.tensor(0.0, device=device)
            has_occ_grad = False
            if occ_head is not None and "occ_labels" in batch:
                patch_features = vla._cached_patch_features
                pf = patch_features.detach() if occ_detach else patch_features
                occ_logits = occ_head(pf.to(torch.bfloat16))
                occ_targets = batch["occ_labels"].to(device).float()
                occ_loss = occ_loss_fn(occ_logits.float(), occ_targets)
                has_occ_grad = not occ_detach

            # Compute action gradients on encoder
            retain = has_occ_grad
            action_grads = torch.autograd.grad(
                action_loss, encoder_params,
                retain_graph=retain, allow_unused=True,
            )

            # Compute OCC gradients on encoder (only if gradient flows through)
            occ_grads = None
            if has_occ_grad:
                occ_grads = torch.autograd.grad(
                    occ_loss, encoder_params, allow_unused=True,
                )

            # --- Aggregate encoder-level metrics ---
            flat_action = torch.cat([
                (g.flatten().float() if g is not None else torch.zeros(p.numel(), device=device))
                for g, p in zip(action_grads, encoder_params)
            ])
            action_norm = flat_action.norm().item()
            agg_action_norms.append(action_norm)

            if occ_grads is not None:
                flat_occ = torch.cat([
                    (g.flatten().float() if g is not None else torch.zeros(p.numel(), device=device))
                    for g, p in zip(occ_grads, encoder_params)
                ])
                occ_norm_val = flat_occ.norm().item()
                agg_occ_norms.append(occ_norm_val)
                cos = F.cosine_similarity(
                    flat_action.unsqueeze(0), flat_occ.unsqueeze(0)
                ).item()
                agg_cosines.append(cos)
            else:
                agg_occ_norms.append(0.0)

            # --- Per-layer metrics ---
            param_idx = 0
            for group_name, group_params in layer_groups.items():
                n = len(group_params)
                parts_a = []
                parts_o = []
                for j in range(n):
                    ag = action_grads[param_idx + j]
                    parts_a.append(ag.flatten().float() if ag is not None
                                   else torch.zeros(group_params[j].numel(), device=device))
                    if occ_grads is not None:
                        og = occ_grads[param_idx + j]
                        parts_o.append(og.flatten().float() if og is not None
                                       else torch.zeros(group_params[j].numel(), device=device))
                param_idx += n

                vec_a = torch.cat(parts_a)
                layer_action_norms[group_name].append(vec_a.norm().item())

                if parts_o:
                    vec_o = torch.cat(parts_o)
                    layer_occ_norms[group_name].append(vec_o.norm().item())
                    cos_l = F.cosine_similarity(vec_a.unsqueeze(0), vec_o.unsqueeze(0)).item()
                    layer_cosines[group_name].append(cos_l)
                else:
                    layer_occ_norms[group_name].append(0.0)

            batch_action_losses.append(action_loss.item())
            batch_occ_losses.append(occ_loss.item())

            if (batch_idx + 1) % 20 == 0:
                elapsed = time.time() - t0
                mem = torch.cuda.max_memory_allocated(device) / 1e9
                cos_str = f"{agg_cosines[-1]:.4f}" if agg_cosines else "N/A"
                print(f"  [{batch_idx+1:>4d}/{args.num_batches}] "
                      f"act={action_loss.item():.4f} occ={occ_loss.item():.4f} "
                      f"cos={cos_str} mem={mem:.1f}GB t={elapsed:.0f}s")

        except Exception as e:
            print(f"  [batch {batch_idx}] ERROR: {e}")
            import traceback; traceback.print_exc()
            continue

        del output, action_loss, occ_loss, action_grads, occ_grads
        torch.cuda.empty_cache()

    total_time = time.time() - t0
    total_batches = len(batch_action_losses)
    print(f"\nCompleted {total_batches} batches in {total_time:.0f}s")

    # --- Aggregate results ---
    result = {
        "condition": condition_name,
        "checkpoint_dir": checkpoint_dir,
        "occ_detach": occ_detach,
        "occ_norm": occ_norm,
        "is_vanilla": is_vanilla,
        "seed": args.seed,
        "num_batches": total_batches,
        "batch_size": args.batch_size,
        "total_time_sec": total_time,
        "avg_action_loss": float(np.mean(batch_action_losses)) if batch_action_losses else None,
        "avg_occ_loss": float(np.mean(batch_occ_losses)) if batch_occ_losses else None,
        "encoder_aggregate": {
            "action_grad_norm": {
                "mean": float(np.mean(agg_action_norms)),
                "std": float(np.std(agg_action_norms)),
                "variance": float(np.var(agg_action_norms)),
            },
            "occ_grad_norm": {
                "mean": float(np.mean(agg_occ_norms)),
                "std": float(np.std(agg_occ_norms)),
                "variance": float(np.var(agg_occ_norms)),
            },
            "cosine_similarity": {
                "mean": float(np.mean(agg_cosines)) if agg_cosines else None,
                "std": float(np.std(agg_cosines)) if agg_cosines else None,
                "min": float(np.min(agg_cosines)) if agg_cosines else None,
                "max": float(np.max(agg_cosines)) if agg_cosines else None,
            },
            "conflict_rate": (
                float(sum(1 for c in agg_cosines if c < 0) / len(agg_cosines))
                if agg_cosines else None
            ),
            "occ_to_action_ratio": (
                float(np.mean(agg_occ_norms) / np.mean(agg_action_norms))
                if np.mean(agg_action_norms) > 0 and np.mean(agg_occ_norms) > 0 else None
            ),
        },
        "per_layer": {},
    }

    for g in layer_names:
        an = layer_action_norms[g]
        on = layer_occ_norms[g]
        cs = layer_cosines.get(g, [])
        result["per_layer"][g] = {
            "action_grad_norm_mean": float(np.mean(an)),
            "action_grad_norm_std": float(np.std(an)),
            "action_grad_norm_var": float(np.var(an)),
            "occ_grad_norm_mean": float(np.mean(on)),
            "occ_grad_norm_std": float(np.std(on)),
            "occ_grad_norm_var": float(np.var(on)),
            "cosine_sim_mean": float(np.mean(cs)) if cs else None,
            "cosine_sim_std": float(np.std(cs)) if cs else None,
            "conflict_rate": float(sum(1 for c in cs if c < 0) / len(cs)) if cs else None,
        }

    # Save per-condition JSON
    safe_name = condition_name.replace(" ", "_").replace("/", "_")
    out_path = os.path.join(args.output_dir, f"{safe_name}_gradient_v2.json")
    with open(out_path, "w") as f:
        json.dump(result, f, indent=2)
    print(f"Saved: {out_path}")

    # Cleanup
    del vla, processor, action_head, occ_head, occ_loss_fn
    torch.cuda.empty_cache()
    gc.collect()

    return result


# ---------------------------------------------------------------------------
# Summary table
# ---------------------------------------------------------------------------

def print_summary(all_results):
    """Print comparison table across all conditions."""
    print(f"\n{'='*90}")
    print("CROSS-CONDITION SUMMARY")
    print(f"{'='*90}")

    header = f"{'Metric':<30s}"
    for name in all_results:
        short = name[:15]
        header += f" {short:>14s}"
    print(header)
    print("-" * 90)

    def val(r, *keys):
        v = r
        for k in keys:
            if isinstance(v, dict):
                v = v.get(k)
            else:
                return "N/A"
        if v is None:
            return "N/A"
        if isinstance(v, float):
            if abs(v) < 0.001:
                return f"{v:.6f}"
            return f"{v:.4f}"
        return str(v)

    rows = [
        ("Action loss", "avg_action_loss"),
        ("OCC loss", "avg_occ_loss"),
        ("Action grad norm (mean)", "encoder_aggregate", "action_grad_norm", "mean"),
        ("Action grad norm (var)", "encoder_aggregate", "action_grad_norm", "variance"),
        ("OCC grad norm (mean)", "encoder_aggregate", "occ_grad_norm", "mean"),
        ("OCC grad norm (var)", "encoder_aggregate", "occ_grad_norm", "variance"),
        ("Cosine similarity", "encoder_aggregate", "cosine_similarity", "mean"),
        ("Cosine sim std", "encoder_aggregate", "cosine_similarity", "std"),
        ("Conflict rate", "encoder_aggregate", "conflict_rate"),
        ("OCC/Action ratio", "encoder_aggregate", "occ_to_action_ratio"),
    ]

    for row_spec in rows:
        label = row_spec[0]
        keys = row_spec[1:]
        line = f"{label:<30s}"
        for name, r in all_results.items():
            line += f" {val(r, *keys):>14s}"
        print(line)

    print(f"{'='*90}")

    # Variance asymmetry analysis
    names = list(all_results.keys())
    results_list = list(all_results.values())
    action_vars = []
    for r in results_list:
        v = r.get("encoder_aggregate", {}).get("action_grad_norm", {}).get("variance")
        action_vars.append(v)

    if all(v is not None for v in action_vars) and len(action_vars) >= 2:
        print("\nGradient Variance Ratios:")
        for i in range(len(names)):
            for j in range(i + 1, len(names)):
                if action_vars[j] > 0:
                    ratio = action_vars[i] / action_vars[j]
                    print(f"  {names[i]} / {names[j]} = {ratio:.2f}x")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    args = parse_args()
    device = torch.device(f"cuda:{args.gpu}")
    os.makedirs(args.output_dir, exist_ok=True)

    if args.config:
        with open(args.config) as f:
            conditions = json.load(f)
        print(f"Loaded {len(conditions)} conditions from {args.config}")
    else:
        if not args.condition_name:
            print("ERROR: --condition_name required in single-condition mode")
            sys.exit(1)
        conditions = {args.condition_name: {"checkpoint_dir": args.checkpoint_dir}}

    all_results = OrderedDict()
    for cond_name, cond_cfg in conditions.items():
        ckpt_dir = cond_cfg["checkpoint_dir"]
        if not os.path.isdir(ckpt_dir):
            print(f"\nWARNING: Checkpoint not found: {ckpt_dir} — skipping {cond_name}")
            continue
        result = analyze_condition(cond_name, ckpt_dir, args, device)
        all_results[cond_name] = result

    if len(all_results) > 1:
        # Save combined results
        combined_path = os.path.join(args.output_dir, "gradient_v2_all_conditions.json")
        with open(combined_path, "w") as f:
            json.dump(all_results, f, indent=2)
        print(f"\nCombined results saved: {combined_path}")

        print_summary(all_results)

    elif len(all_results) == 1:
        name, r = next(iter(all_results.items()))
        agg = r["encoder_aggregate"]
        print(f"\n--- {name} ---")
        print(f"Action grad norm: {agg['action_grad_norm']['mean']:.6f} "
              f"(var={agg['action_grad_norm']['variance']:.6f})")
        print(f"OCC grad norm:    {agg['occ_grad_norm']['mean']:.6f} "
              f"(var={agg['occ_grad_norm']['variance']:.6f})")
        cos = agg["cosine_similarity"]["mean"]
        if cos is not None:
            print(f"Cosine sim:       {cos:.4f}")
        print(f"Conflict rate:    {agg['conflict_rate']}")

    print("\nDone.")


if __name__ == "__main__":
    main()
