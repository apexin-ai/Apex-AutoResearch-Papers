#!/usr/bin/env python3
"""V2 Checkpoint Same-Seed Gradient Analysis for OccSafe-VLA.

Compares gradient flow patterns across v2 checkpoints to determine if
training dynamics match v1 D042 findings ("existence regularization").

Metrics computed on _cached_patch_features (shared visual representation):
  1. Action gradient norm (CE loss -> LLM -> projector -> patch_features)
  2. OCC gradient norm (focal loss -> OCC head -> patch_features)
  3. Cosine similarity between action and OCC gradients
  4. Conflict rate (fraction of dims where gradients disagree in sign)
  5. DINOv2 vs SigLIP action gradient ratio (split by feature dimension)
"""

import sys
sys.argv = ['gradient_analysis', '--dataset_name', 'libero_spatial_no_noops']

import os
import json
import gc
import types
import torch
import torch.nn.functional as F
import numpy as np
from pathlib import Path
from collections import OrderedDict

os.environ["TOKENIZERS_PARALLELISM"] = "false"

sys.path.insert(0, '/root/occsafe_vla/openvla-oft')

from prismatic.extern.hf.configuration_prismatic import OpenVLAConfig
from prismatic.extern.hf.modeling_prismatic import OpenVLAForActionPrediction
from prismatic.extern.hf.processing_prismatic import PrismaticImageProcessor, PrismaticProcessor
from prismatic.models.occ_head import BEVOccupancyHead, FocalLoss
from prismatic.vla.constants import (
    ACTION_DIM, NUM_ACTIONS_CHUNK, ACTION_TOKEN_BEGIN_IDX, IGNORE_INDEX
)
from transformers import AutoConfig, AutoImageProcessor, AutoModelForVision2Seq, AutoProcessor

# === Config ===
SEED = 42
NUM_BATCHES = 5
BATCH_SIZE = 1
DEVICE = "cuda:1"

CHECKPOINTS = OrderedDict([
    ("full_occ_bn_v2", {
        "path": "/root/autodl-tmp/checkpoints/full_occ_bn_v2_s1/"
                "openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0"
                "--image_aug--full_occ_bn_v2_s1--50000_chkpt",
        "has_occ": True,
        "occ_detach": False,
    }),
    ("detach_bn_v2", {
        "path": "/root/autodl-tmp/checkpoints/detach_bn_v2_s0/"
                "openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0"
                "--image_aug--detach_bn_v2_s0--50000_chkpt",
        "has_occ": True,
        "occ_detach": True,
    }),
    ("vanilla_v2", {
        "path": "/root/autodl-tmp/checkpoints/vanilla_retrain_s0/"
                "openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0"
                "--image_aug--50000_chkpt",
        "has_occ": False,
        "occ_detach": False,
    }),
])

# Register HF Auto Classes
AutoConfig.register("openvla", OpenVLAConfig)
AutoImageProcessor.register(OpenVLAConfig, PrismaticImageProcessor)
AutoProcessor.register(OpenVLAConfig, PrismaticProcessor)
AutoModelForVision2Seq.register(OpenVLAConfig, OpenVLAForActionPrediction)


def create_batch(processor, device, seed):
    """Create synthetic batch matching training data format."""
    g = torch.Generator().manual_seed(seed)
    B = BATCH_SIZE

    pixel_values = torch.randn(B, 6, 224, 224, generator=g, dtype=torch.bfloat16).to(device)

    prompt = ("In: What action should the robot take to pick up the red block "
              "and place it on the table?\n")
    enc = processor.tokenizer(prompt, return_tensors="pt", padding=False)
    prompt_ids = enc.input_ids
    prompt_len = prompt_ids.shape[1]

    n_act = NUM_ACTIONS_CHUNK * ACTION_DIM  # 56
    act_ids = torch.randint(
        ACTION_TOKEN_BEGIN_IDX, ACTION_TOKEN_BEGIN_IDX + 256,
        (B, n_act), generator=g
    )

    input_ids = torch.cat([prompt_ids.expand(B, -1), act_ids], dim=1).to(device)
    attention_mask = torch.ones_like(input_ids)

    labels = torch.full_like(input_ids, IGNORE_INDEX)
    labels[:, prompt_len:] = act_ids.to(device)

    occ_labels = (torch.rand(B, 64, 64, generator=g) > 0.85).float().to(device)

    return {
        "input_ids": input_ids,
        "attention_mask": attention_mask,
        "pixel_values": pixel_values,
        "labels": labels,
        "occ_labels": occ_labels,
    }


def analyze_one(name, info):
    """Run gradient analysis on a single checkpoint."""
    print(f"\n{'='*60}\nAnalyzing: {name}\n{'='*60}")
    path = info["path"]
    has_occ = info["has_occ"]
    occ_detach = info["occ_detach"]

    # Load model (merged LoRA checkpoint)
    print(f"Loading model...")
    model = AutoModelForVision2Seq.from_pretrained(
        path, torch_dtype=torch.bfloat16, low_cpu_mem_usage=True, trust_remote_code=True
    ).to(DEVICE).eval()

    processor = AutoProcessor.from_pretrained(path, trust_remote_code=True)

    # Vision backbone dimensions
    dino_dim = model.vision_backbone.featurizer.embed_dim
    siglip_dim = (model.vision_backbone.fused_featurizer.embed_dim
                  if model.vision_backbone.use_fused_vision_backbone else 0)
    total_dim = dino_dim + siglip_dim
    print(f"Vision dims: DINOv2={dino_dim}, SigLIP={siglip_dim}, total={total_dim}")

    # Load OCC head
    occ_head, occ_fn = None, None
    if has_occ:
        occ_head = BEVOccupancyHead(in_dim=total_dim)
        sd = torch.load(
            os.path.join(path, "occ_head--50000_checkpoint.pt"),
            map_location="cpu", weights_only=True
        )
        occ_head.load_state_dict({k.replace("module.", ""): v for k, v in sd.items()})
        occ_head = occ_head.to(torch.bfloat16).to(DEVICE).eval()
        occ_fn = FocalLoss()
        print("OCC head loaded")

    # Monkey-patch _process_vision_features to capture patch_features with grad
    pf_ref = [None]

    def patched_process(self, pixel_values, language_embeddings=None, use_film=False):
        if use_film:
            pf = self.vision_backbone(pixel_values, language_embeddings)
        else:
            pf = self.vision_backbone(pixel_values)
        # Detach from frozen backbone, enable grad for analysis
        pf = pf.detach().requires_grad_(True)
        self._cached_patch_features = pf
        pf_ref[0] = pf
        return self.projector(pf)

    model._process_vision_features = types.MethodType(patched_process, model)

    # Enable grad on projector params (for projector gradient analysis)
    for p in model.projector.parameters():
        p.requires_grad_(True)

    # Collect per-batch metrics
    metrics = {k: [] for k in [
        "action_grad_norm", "occ_grad_norm", "cosine_sim", "conflict_rate",
        "dino_grad_norm", "siglip_grad_norm", "proj_action_grad_norm",
    ]}

    for batch_idx in range(NUM_BATCHES):
        batch = create_batch(processor, DEVICE, SEED + batch_idx)
        model.zero_grad()
        if occ_head is not None:
            occ_head.zero_grad()

        # Forward pass -> CE loss on action tokens
        output = model(
            input_ids=batch["input_ids"],
            attention_mask=batch["attention_mask"],
            pixel_values=batch["pixel_values"],
            labels=batch["labels"],
        )

        pf = pf_ref[0]
        action_loss = output.loss
        proj_params = list(model.projector.parameters())

        # Compute action gradient on patch_features + projector
        grads = torch.autograd.grad(
            action_loss, [pf] + proj_params,
            retain_graph=has_occ,
            allow_unused=True,
        )

        ag = grads[0].float()  # Action gradient on patch_features

        metrics["action_grad_norm"].append(ag.norm().item())
        metrics["dino_grad_norm"].append(ag[:, :, :dino_dim].norm().item())
        metrics["siglip_grad_norm"].append(ag[:, :, dino_dim:].norm().item())
        metrics["proj_action_grad_norm"].append(
            sum(g.float().norm().item()**2 for g in grads[1:] if g is not None)**0.5
        )

        # OCC gradient on patch_features
        if has_occ:
            # For detach: compute OCC grad on a detached copy
            # For full_occ: compute OCC grad on the same pf (still connected to action graph)
            if occ_detach:
                occ_in = pf.detach().requires_grad_(True)
            else:
                occ_in = pf

            occ_logits = occ_head(occ_in)
            occ_loss = occ_fn(occ_logits.float(), batch["occ_labels"])

            og = torch.autograd.grad(occ_loss, [occ_in], allow_unused=True)[0].float()

            metrics["occ_grad_norm"].append(og.norm().item())

            a_flat = ag.flatten()
            o_flat = og.flatten()
            cos = F.cosine_similarity(a_flat.unsqueeze(0), o_flat.unsqueeze(0)).item()
            conf = (a_flat * o_flat < 0).float().mean().item()
            metrics["cosine_sim"].append(cos)
            metrics["conflict_rate"].append(conf)

            print(f"  Batch {batch_idx}: action={metrics['action_grad_norm'][-1]:.6f} "
                  f"occ={og.norm().item():.6f} cos={cos:.4f} conflict={conf:.4f}")
        else:
            print(f"  Batch {batch_idx}: action={metrics['action_grad_norm'][-1]:.6f} "
                  f"dino={metrics['dino_grad_norm'][-1]:.6f} siglip={metrics['siglip_grad_norm'][-1]:.6f}")

    # Aggregate results
    result = {
        "name": name,
        "has_occ": has_occ,
        "occ_detach": occ_detach,
        "checkpoint_path": path,
        "action_grad_norm": {
            "mean": float(np.mean(metrics["action_grad_norm"])),
            "std": float(np.std(metrics["action_grad_norm"])),
            "values": [float(v) for v in metrics["action_grad_norm"]],
        },
        "dino_action_grad_norm": {
            "mean": float(np.mean(metrics["dino_grad_norm"])),
            "std": float(np.std(metrics["dino_grad_norm"])),
        },
        "siglip_action_grad_norm": {
            "mean": float(np.mean(metrics["siglip_grad_norm"])),
            "std": float(np.std(metrics["siglip_grad_norm"])),
        },
        "dino_siglip_ratio": float(
            np.mean(metrics["dino_grad_norm"]) /
            max(np.mean(metrics["siglip_grad_norm"]), 1e-10)
        ),
        "projector_action_grad_norm": {
            "mean": float(np.mean(metrics["proj_action_grad_norm"])),
            "std": float(np.std(metrics["proj_action_grad_norm"])),
        },
    }

    if has_occ:
        result.update({
            "occ_grad_norm": {
                "mean": float(np.mean(metrics["occ_grad_norm"])),
                "std": float(np.std(metrics["occ_grad_norm"])),
                "values": [float(v) for v in metrics["occ_grad_norm"]],
            },
            "cosine_similarity": {
                "mean": float(np.mean(metrics["cosine_sim"])),
                "std": float(np.std(metrics["cosine_sim"])),
                "values": [float(v) for v in metrics["cosine_sim"]],
            },
            "conflict_rate": {
                "mean": float(np.mean(metrics["conflict_rate"])),
                "std": float(np.std(metrics["conflict_rate"])),
                "values": [float(v) for v in metrics["conflict_rate"]],
            },
            "occ_to_action_ratio": float(
                np.mean(metrics["occ_grad_norm"]) /
                max(np.mean(metrics["action_grad_norm"]), 1e-10)
            ),
        })

    # Cleanup
    del model, processor
    if occ_head is not None:
        del occ_head
    torch.cuda.empty_cache()
    gc.collect()

    return result


def main():
    print(f"V2 Gradient Analysis | Device: {DEVICE} | Seed: {SEED} | Batches: {NUM_BATCHES}")
    print(f"Constants: ACTION_DIM={ACTION_DIM}, NUM_ACTIONS_CHUNK={NUM_ACTIONS_CHUNK}")

    if torch.cuda.is_available():
        dev_idx = int(DEVICE.split(":")[-1])
        free, total = torch.cuda.mem_get_info(dev_idx)
        print(f"GPU {dev_idx}: {free/1024**3:.1f}GB free / {total/1024**3:.1f}GB total")

    results = {}
    for name, info in CHECKPOINTS.items():
        try:
            results[name] = analyze_one(name, info)
        except Exception as e:
            import traceback
            traceback.print_exc()
            results[name] = {"error": str(e)}
            torch.cuda.empty_cache()
            gc.collect()

    # Save JSON
    out_dir = Path("/root/occsafe_vla/artifacts")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "v2_gradient_analysis.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to {out_path}")

    # === Summary Table ===
    print(f"\n{'='*70}")
    print("SUMMARY")
    print(f"{'='*70}")

    v = results.get("vanilla_v2", {})
    fo = results.get("full_occ_bn_v2", {})
    d = results.get("detach_bn_v2", {})

    def g(r, *keys):
        for k in keys:
            if isinstance(r, dict):
                r = r.get(k, "N/A")
            else:
                return "N/A"
        if isinstance(r, float):
            return f"{r:.6f}"
        return str(r)

    print(f"\n{'Metric':<35} {'Vanilla':>12} {'Full OCC':>12} {'Detach':>12}")
    print("-" * 73)
    for label, *path in [
        ("Action grad norm", "action_grad_norm", "mean"),
        ("OCC grad norm", "occ_grad_norm", "mean"),
        ("OCC/Action ratio", "occ_to_action_ratio"),
        ("Cosine sim (act vs OCC)", "cosine_similarity", "mean"),
        ("Conflict rate", "conflict_rate", "mean"),
        ("DINOv2 action grad", "dino_action_grad_norm", "mean"),
        ("SigLIP action grad", "siglip_action_grad_norm", "mean"),
        ("DINOv2/SigLIP ratio", "dino_siglip_ratio"),
        ("Projector action grad", "projector_action_grad_norm", "mean"),
    ]:
        print(f"{label:<35} {g(v, *path):>12} {g(fo, *path):>12} {g(d, *path):>12}")

    # === D042 v1 Comparison ===
    print(f"\n{'='*70}")
    print("D042 v1 -> v2 COMPARISON")
    print(f"{'='*70}")
    print("D042 v1 findings:")
    print("  Detach grad norm = 4% of Vanilla")
    print("  Cosine similarity OCC vs action ~ 0")
    print("  Conflict rate ~ 44%")
    print('  Mechanism: "existence regularization"')

    if isinstance(d, dict) and "error" not in d and isinstance(v, dict) and "error" not in v:
        vgn = v.get("action_grad_norm", {}).get("mean", 0)
        dgn = d.get("action_grad_norm", {}).get("mean", 0)
        if vgn > 0:
            ratio = dgn / vgn
            print(f"\nV2 Detach/Vanilla action grad ratio: {ratio:.4f} (v1: 0.04)")
        if "cosine_similarity" in d:
            print(f"V2 Detach cosine sim: {d['cosine_similarity']['mean']:.4f} (v1: ~0)")
        if "conflict_rate" in d:
            print(f"V2 Detach conflict rate: {d['conflict_rate']['mean']:.4f} (v1: ~0.44)")

    if isinstance(fo, dict) and "error" not in fo:
        if "cosine_similarity" in fo:
            print(f"\nV2 Full OCC cosine sim: {fo['cosine_similarity']['mean']:.4f}")
        if "conflict_rate" in fo:
            print(f"V2 Full OCC conflict rate: {fo['conflict_rate']['mean']:.4f}")
        if "occ_to_action_ratio" in fo:
            print(f"V2 Full OCC OCC/Action grad ratio: {fo['occ_to_action_ratio']:.4f}")

    print("\nKey question: does v2 preserve 'existence regularization' pattern?")
    if isinstance(d, dict) and "error" not in d:
        cos = d.get("cosine_similarity", {}).get("mean", None)
        conf = d.get("conflict_rate", {}).get("mean", None)
        if cos is not None and conf is not None:
            if abs(cos) < 0.1 and 0.3 < conf < 0.6:
                print("=> YES: cosine~0, conflict~0.44 pattern preserved in v2")
            else:
                print(f"=> DIFFERENT from v1: cosine={cos:.4f}, conflict={conf:.4f}")
                if abs(cos) > 0.2:
                    print("   Non-trivial cosine suggests gradient competition/cooperation")
                if conf > 0.6:
                    print("   High conflict suggests pathological gradient competition")


if __name__ == "__main__":
    main()
