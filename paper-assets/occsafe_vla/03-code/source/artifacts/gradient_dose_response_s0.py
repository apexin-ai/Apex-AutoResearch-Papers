#!/usr/bin/env python3
"""
Per-layer gradient dose-response analysis for OccSafe-VLA (all s0/seed 42).

For each condition (50K checkpoint), computes:
- Action gradients: from cross-entropy language model loss (full model path)
- Aux gradients: from OCC head focal loss (vision backbone path only)

Per vision backbone layer metrics:
- Gradient norms (action vs aux)
- Cosine similarity between action and aux gradient vectors
- Conflict rate (fraction of dimensions with opposite gradient signs)

Usage:
    CUDA_VISIBLE_DEVICES=2 python gradient_dose_response_s0.py
"""

import gc
import json
import os
import sys
import time
from collections import OrderedDict
from pathlib import Path

import h5py
import numpy as np
import torch
from PIL import Image

sys.path.insert(0, "/root/occsafe_vla/openvla-oft")
from peft import PeftModel
from transformers import AutoModelForVision2Seq, AutoProcessor
from prismatic.models.occ_head import BEVOccupancyHead, FocalLoss


def log(msg):
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)


PRETRAINED_PATH = "/root/autodl-tmp/models/openvla-7b"
LIBERO_DATA_DIR = "/root/autodl-tmp/libero_datasets/libero_spatial"
OCC_DATA_DIR = "/root/occsafe_vla/occ_data"
OUTPUT_DIR = "/root/autodl-tmp/analysis/gradient_dose_response_s0"
CKPT_BASE = "/root/autodl-tmp/checkpoints"
NUM_SAMPLES = 16
BATCH_SIZE = 4
DEVICE = "cuda:0"

COLORS = {
    "Vanilla": "#607D8B",
    "Full OCC BN": "#4CAF50",
    "Detach BN": "#FF5722",
    "Full OCC LN": "#2196F3",
    "Cutoff 15K": "#03A9F4",
    "Cutoff 25K": "#00BCD4",
    "Cutoff 35K": "#FF9800",
    "Cutoff 45K": "#F44336",
    "Reverse Cutoff": "#9C27B0",
}


def find_checkpoint_dir(base_dir):
    for d in sorted(Path(base_dir).iterdir()):
        if d.is_dir() and "50000_chkpt" in d.name:
            return str(d)
    return None


def build_conditions():
    conditions = OrderedDict()
    # (name, dirname, use_shared_occ, occ_detach, norm_type)
    # use_shared_occ: "own" = use own occ_head, "shared" = use full_occ_retrain_s0's occ_head,
    #                 None = no occ analysis, "detach" = own occ_head with detach
    specs = [
        ("Vanilla", "vanilla_retrain_s0", None, False, "bn"),
        ("Full OCC BN", "full_occ_retrain_s0", "own", False, "bn"),
        ("Detach BN", "ablation_occ_detach_s0_retrain", "own", True, "bn"),
        ("Full OCC LN", "full_occ_ln_s0", "own", False, "ln"),
        ("Cutoff 15K", "cutoff_15k_s0", "shared", False, "bn"),
        ("Cutoff 25K", "cutoff_25k_s0", "shared", False, "bn"),
        ("Cutoff 35K", "cutoff_s0", "shared", False, "bn"),
        ("Cutoff 45K", "cutoff_45k_s0", "shared", False, "bn"),
        ("Reverse Cutoff", "reverse_cutoff_s0", "shared", False, "bn"),
    ]

    # Shared OCC head path from full_occ_retrain_s0
    shared_occ_base = os.path.join(CKPT_BASE, "full_occ_retrain_s0")
    shared_occ_dir = find_checkpoint_dir(shared_occ_base) if os.path.isdir(shared_occ_base) else None
    shared_occ_path = None
    if shared_occ_dir:
        candidate = os.path.join(shared_occ_dir, "occ_head--50000_checkpoint.pt")
        if os.path.exists(candidate):
            shared_occ_path = candidate
            log(f"  Shared OCC head: {candidate}")

    for name, dirname, occ_mode, detach, norm_type in specs:
        base = os.path.join(CKPT_BASE, dirname)
        if not os.path.isdir(base):
            continue
        ckpt_dir = find_checkpoint_dir(base)
        if not ckpt_dir:
            continue
        lora_path = os.path.join(ckpt_dir, "lora_adapter")
        if not os.path.isdir(lora_path):
            continue

        occ_path = None
        if occ_mode == "own":
            candidate = os.path.join(ckpt_dir, "occ_head--50000_checkpoint.pt")
            if os.path.exists(candidate):
                occ_path = candidate
        elif occ_mode == "shared":
            occ_path = shared_occ_path

        conditions[name] = {
            "lora_path": lora_path,
            "occ_head_path": occ_path,
            "occ_detach": detach,
            "norm_type": norm_type if occ_mode != "shared" else "bn",
        }
        log(f"  Found: {name}")

    return conditions


def load_data(data_dir, occ_dir, num_samples=16):
    images, occ_labels = [], []

    hdf5_files = sorted(Path(data_dir).glob("*.hdf5"))
    with open(os.path.join(occ_dir, "occ_index.json")) as f:
        occ_index = json.load(f)

    task_occ_map = {}
    for task_key, info in occ_index.items():
        task_occ_map[task_key] = os.path.join(occ_dir, info["occ_file"])

    for hdf5_file in hdf5_files:
        if len(images) >= num_samples:
            break
        task_name = hdf5_file.stem.replace("_demo", "")
        occ_file = task_occ_map.get(task_name)

        with h5py.File(hdf5_file, "r") as f:
            occ_f = h5py.File(occ_file, "r") if occ_file and os.path.exists(occ_file) else None
            try:
                for demo_key in sorted(f["data"].keys()):
                    if len(images) >= num_samples:
                        break
                    rgb = f["data"][demo_key]["obs"]["agentview_rgb"]
                    mid = rgb.shape[0] // 2
                    images.append(Image.fromarray(rgb[mid]))

                    if occ_f and demo_key in occ_f["data"]:
                        occ_labels.append(occ_f["data"][demo_key]["bev_binary"][mid].astype(np.float32))
                    else:
                        occ_labels.append(np.zeros((64, 64), dtype=np.float32))
            finally:
                if occ_f:
                    occ_f.close()

    log(f"Loaded {len(images)} images, {len(occ_labels)} OCC labels")
    return images[:num_samples], occ_labels[:num_samples]


def classify_param(name):
    if "vision_backbone.featurizer.blocks." in name:
        block = int(name.split("vision_backbone.featurizer.blocks.")[1].split(".")[0])
        return ("dinov2", block)
    elif "vision_backbone.fused_featurizer.blocks." in name:
        block = int(name.split("vision_backbone.fused_featurizer.blocks.")[1].split(".")[0])
        return ("siglip", block)
    elif "vision_backbone.featurizer" in name:
        return ("dinov2", -1)
    elif "vision_backbone.fused_featurizer" in name:
        return ("siglip", -1)
    elif "projector" in name:
        return ("projector", 0)
    elif "language_model.model.layers." in name:
        layer = int(name.split("language_model.model.layers.")[1].split(".")[0])
        return ("llm", layer)
    elif "language_model" in name:
        return ("llm", -1)
    else:
        return ("other", 0)


def collect_grads(model, sections=None):
    layer_grads = {}
    for name, param in model.named_parameters():
        if param.grad is None:
            continue
        section, block = classify_param(name)
        if sections and section not in sections:
            continue
        key = f"{section}_block_{block}" if block >= 0 else f"{section}_other"
        if key not in layer_grads:
            layer_grads[key] = []
        layer_grads[key].append(param.grad.detach().float().flatten())

    for key in layer_grads:
        layer_grads[key] = torch.cat(layer_grads[key])
    return layer_grads


def analyze_condition(cond_name, cond_config, processor, all_pv, input_ids, attention_mask, occ_targets, device):
    log(f"\n=== Analyzing: {cond_name} ===")
    t0 = time.time()

    log(f"  Loading model + LoRA...")
    model = AutoModelForVision2Seq.from_pretrained(
        PRETRAINED_PATH, torch_dtype=torch.bfloat16,
        low_cpu_mem_usage=True, trust_remote_code=True,
    )
    model = PeftModel.from_pretrained(model, cond_config["lora_path"])
    model = model.merge_and_unload()
    model = model.to(device)
    model.eval()

    for p in model.parameters():
        p.requires_grad_(True)

    occ_head = None
    focal_loss_fn = None
    if cond_config["occ_head_path"]:
        embed_dim = model.vision_backbone.embed_dim
        num_patches = model.vision_backbone.get_num_patches()
        occ_head = BEVOccupancyHead(
            in_dim=embed_dim, out_resolution=64, num_classes=1,
            num_patches_per_image=num_patches, norm_type=cond_config["norm_type"],
        )
        sd = torch.load(cond_config["occ_head_path"], map_location="cpu", weights_only=True)
        sd = {k.replace("module.", ""): v for k, v in sd.items()}
        occ_head.load_state_dict(sd)
        occ_head = occ_head.to(device).to(torch.bfloat16)
        occ_head.eval()
        for p in occ_head.parameters():
            p.requires_grad_(True)
        focal_loss_fn = FocalLoss().to(device)
        log(f"  Loaded OCC head ({cond_config['norm_type']})")

    N = all_pv.shape[0]
    num_batches = (N + BATCH_SIZE - 1) // BATCH_SIZE

    # --- Action gradients (CE loss through full model) ---
    log(f"  Computing action gradients ({N} samples, {num_batches} batches)...")
    model.zero_grad()
    total_action_loss = 0.0

    for b in range(num_batches):
        s, e = b * BATCH_SIZE, min((b + 1) * BATCH_SIZE, N)
        bs = e - s
        batch_pv = all_pv[s:e].to(device, dtype=torch.bfloat16)
        batch_ids = input_ids.expand(bs, -1).to(device)
        batch_attn = attention_mask.expand(bs, -1).to(device)
        batch_labels = batch_ids.clone()

        output = model(
            input_ids=batch_ids,
            attention_mask=batch_attn,
            pixel_values=batch_pv,
            labels=batch_labels,
        )
        loss = output.loss / num_batches
        loss.backward()
        total_action_loss += output.loss.item()

    action_grads = collect_grads(model)
    log(f"  Action loss: {total_action_loss / num_batches:.4f}, layers with grads: {len(action_grads)}")

    # --- Aux gradients (OCC loss through vision backbone only) ---
    aux_grads = None
    total_aux_loss = 0.0

    if occ_head is not None:
        log(f"  Computing aux gradients...")
        model.zero_grad()
        occ_head.zero_grad()

        for b in range(num_batches):
            s, e = b * BATCH_SIZE, min((b + 1) * BATCH_SIZE, N)
            batch_pv = all_pv[s:e].to(device, dtype=torch.bfloat16)
            batch_occ = occ_targets[s:e]

            patch_features = model.vision_backbone(batch_pv)
            if cond_config["occ_detach"]:
                patch_features = patch_features.detach()

            occ_logits = occ_head(patch_features.to(torch.bfloat16))
            occ_loss = focal_loss_fn(occ_logits.float(), batch_occ)
            (occ_loss / num_batches).backward()
            total_aux_loss += occ_loss.item()

        aux_grads = collect_grads(model, sections=("dinov2", "siglip"))
        log(f"  Aux loss: {total_aux_loss / num_batches:.4f}, layers with grads: {len(aux_grads)}")

    # --- Compute per-layer metrics ---
    all_keys = set(action_grads.keys())
    if aux_grads:
        all_keys.update(aux_grads.keys())

    def sort_key(k):
        if k.startswith("dinov2_block_"):
            return (0, int(k.split("_")[-1]))
        elif k == "dinov2_other":
            return (0, 999)
        elif k.startswith("siglip_block_"):
            return (1, int(k.split("_")[-1]))
        elif k == "siglip_other":
            return (1, 999)
        elif k.startswith("projector"):
            return (2, 0)
        elif k.startswith("llm_block_"):
            return (3, int(k.split("_")[-1]))
        elif k == "llm_other":
            return (3, 999)
        return (9, 0)

    sorted_keys = sorted(all_keys, key=sort_key)

    result = {"action_loss": total_action_loss / num_batches}
    if occ_head:
        result["aux_loss"] = total_aux_loss / num_batches

    layers = OrderedDict()
    for key in sorted_keys:
        m = {}
        if key in action_grads:
            m["action_grad_norm"] = action_grads[key].norm().item()
        else:
            m["action_grad_norm"] = 0.0

        if aux_grads and key in aux_grads:
            ag = aux_grads[key]
            m["aux_grad_norm"] = ag.norm().item()

            if key in action_grads and action_grads[key].shape == ag.shape:
                act_g = action_grads[key]
                cos = torch.nn.functional.cosine_similarity(act_g.unsqueeze(0), ag.unsqueeze(0)).item()
                m["cosine_similarity"] = cos
                conflict = (torch.sign(act_g) != torch.sign(ag)).float().mean().item()
                m["conflict_rate"] = conflict
            else:
                m["cosine_similarity"] = 0.0
                m["conflict_rate"] = 0.0
        else:
            m["aux_grad_norm"] = 0.0
            m["cosine_similarity"] = 0.0
            m["conflict_rate"] = 0.0

        layers[key] = m

    result["layers"] = layers

    del model, occ_head, action_grads, aux_grads
    gc.collect()
    torch.cuda.empty_cache()

    elapsed = time.time() - t0
    log(f"  Done in {elapsed:.1f}s")
    return result


def plot_results(results):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, axes = plt.subplots(2, 2, figsize=(16, 10))

    for cond_name, cond_data in results.items():
        layers = cond_data["layers"]

        dinov2 = [(k, v) for k, v in layers.items() if k.startswith("dinov2_block_")]
        siglip = [(k, v) for k, v in layers.items() if k.startswith("siglip_block_")]

        dinov2.sort(key=lambda x: int(x[0].split("_")[-1]))
        siglip.sort(key=lambda x: int(x[0].split("_")[-1]))

        all_layers = dinov2 + siglip
        if not all_layers:
            continue
        xs = list(range(len(all_layers)))
        color = COLORS.get(cond_name)

        for ax_idx, metric in enumerate(["action_grad_norm", "aux_grad_norm", "cosine_similarity", "conflict_rate"]):
            ax = axes[ax_idx // 2, ax_idx % 2]
            ys = [v[metric] for _, v in all_layers]
            ax.plot(xs, ys, "o-", label=cond_name, color=color, markersize=2, linewidth=1.5, alpha=0.85)

    n_dino = 24
    n_total = n_dino + 27

    titles = [
        "Per-layer Action Gradient Norm",
        "Per-layer Aux (OCC) Gradient Norm",
        r"Per-layer Cosine Similarity (Action $\leftrightarrow$ Aux)",
        r"Per-layer Conflict Rate (Action $\leftrightarrow$ Aux)",
    ]
    ylabels = [r"$\|\|\nabla_{action}\|\|$", r"$\|\|\nabla_{aux}\|\|$",
               r"$\cos(\nabla_{action}, \nabla_{aux})$", "Conflict Rate"]

    for ax, title, ylabel in zip(axes.flat, titles, ylabels):
        ax.axvline(x=n_dino - 0.5, color="gray", linestyle="--", alpha=0.5, linewidth=0.8)
        ax.set_xlabel("Vision Backbone Layer Index")
        ax.set_ylabel(ylabel)
        ax.set_title(title, fontsize=11)
        ax.legend(fontsize=7, loc="best")
        ax.grid(True, alpha=0.3)
        ax.set_xlim(-0.5, n_total - 0.5)

    fig.suptitle("Gradient Dose-Response: Per-Layer Vision Backbone Analysis (50K steps, seed 42)",
                 fontsize=13, fontweight="bold")
    plt.tight_layout()

    for ext in ("pdf", "png"):
        path = os.path.join(OUTPUT_DIR, f"gradient_dose_response.{ext}")
        fig.savefig(path, dpi=200, bbox_inches="tight")
    plt.close(fig)
    log("Saved: gradient_dose_response.pdf/png")


def print_summary(results):
    log("\n" + "=" * 90)
    log("GRADIENT ANALYSIS SUMMARY (mean across vision backbone layers)")
    log("=" * 90)

    fmt = "{:18s}  {:>14s}  {:>14s}  {:>12s}  {:>12s}"
    log(fmt.format("Condition", "Action Norm", "Aux Norm", "Cos Sim", "Conflict"))
    log("-" * 90)

    for cond_name, cond_data in results.items():
        layers = cond_data["layers"]
        vision_layers = {k: v for k, v in layers.items()
                         if k.startswith("dinov2_block_") or k.startswith("siglip_block_")}
        if not vision_layers:
            continue

        vals = list(vision_layers.values())
        action_mean = np.mean([v["action_grad_norm"] for v in vals])
        aux_mean = np.mean([v["aux_grad_norm"] for v in vals])
        cos_mean = np.mean([v["cosine_similarity"] for v in vals])
        conf_mean = np.mean([v["conflict_rate"] for v in vals])

        log(f"{cond_name:18s}  {action_mean:14.6f}  {aux_mean:14.6f}  {cos_mean:12.4f}  {conf_mean:12.4f}")

    log("=" * 90)


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    log("Building conditions...")
    conditions = build_conditions()
    if not conditions:
        log("ERROR: No conditions found!")
        return
    log(f"Found {len(conditions)} conditions: {list(conditions.keys())}")

    log("Loading processor...")
    processor = AutoProcessor.from_pretrained(PRETRAINED_PATH, trust_remote_code=True)

    log("Loading data...")
    images, occ_labels_np = load_data(LIBERO_DATA_DIR, OCC_DATA_DIR, NUM_SAMPLES)

    log("Processing images...")
    pv_list = []
    for img in images:
        pv = processor.image_processor(img, return_tensors="pt")["pixel_values"]
        pv_list.append(pv)
    all_pv = torch.cat(pv_list, dim=0)
    log(f"  pixel_values shape: {all_pv.shape}")

    text = "In: What action should the robot take to pick up the black bowl and place it on the plate?\nOut: the robot should move"
    tokens = processor.tokenizer(text, return_tensors="pt", add_special_tokens=True)
    input_ids = tokens["input_ids"]
    attention_mask = tokens["attention_mask"]
    log(f"  input_ids shape: {input_ids.shape}")

    occ_targets = torch.tensor(np.stack(occ_labels_np), dtype=torch.float32).to(DEVICE)

    results = {}
    for cond_name, cond_config in conditions.items():
        results[cond_name] = analyze_condition(
            cond_name, cond_config, processor, all_pv, input_ids, attention_mask, occ_targets, DEVICE
        )

    results_path = os.path.join(OUTPUT_DIR, "results.json")
    with open(results_path, "w") as f:
        json.dump(results, f, indent=2)
    log(f"Saved: {results_path}")

    log("Generating plots...")
    plot_results(results)

    print_summary(results)
    log("DONE")


if __name__ == "__main__":
    main()
