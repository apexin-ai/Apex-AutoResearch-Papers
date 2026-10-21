"""
OpenVLA-OFT Token Importance Analysis: Pruning Curve + Attention Entropy.

Runs on REAL LIBERO-Object observations. Measures:
  A) Pruning curve: L2-norm based vision token pruning → hidden state degradation
  B) Attention entropy per layer (text→vision attention distribution)

Usage:
    source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
    CUDA_VISIBLE_DEVICES=0 python analyze_openvla_oft.py
"""

import glob
import json
import math
import os
import sys
import time

os.environ.setdefault("HF_HOME", "/root/autodl-tmp/.hf_cache")
os.environ["TRANSFORMERS_OFFLINE"] = "1"
os.environ["HF_HUB_OFFLINE"] = "1"

import h5py
import numpy as np
import torch
from PIL import Image

# Use base OpenVLA code via hf package (relative imports require package context)
sys.path.insert(0, "/root/autodl-tmp/openvla_code")
from hf.configuration_prismatic import OpenVLAConfig
from hf.modeling_prismatic import OpenVLAForActionPrediction
from hf.processing_prismatic import PrismaticImageProcessor, PrismaticProcessor

DEVICE = torch.device("cuda:0")
CHECKPOINT_PATH = os.environ.get("CHECKPOINT_PATH", "/root/autodl-tmp/openvla-oft-libero-object")
BASE_CHECKPOINT_PATH = os.environ.get("BASE_CHECKPOINT_PATH", "/root/autodl-tmp/openvla-libero-object")
LORA_ADAPTER_PATH = os.environ.get("LORA_ADAPTER_PATH", "")
MODEL_NAME = os.environ.get("MODEL_NAME", "OpenVLA-OFT-7B-libero-object")
LIBERO_DIR = "/root/autodl-tmp/libero_data/datasets/libero_object"
N_VISION_TOKENS = 256
IMAGES_PER_TASK = 10
OUTPUT_DIR = "/root/autodl-tmp/importance_margin_vla_compress/artifacts"

KEEP_RATIOS = [0.1, 0.2, 0.3, 0.5, 0.7, 0.9, 0.95, 1.0]

TASK_PROMPTS = {
    "pick_up_the_alphabet_soup": "pick up the alphabet soup and place it in the basket",
    "pick_up_the_cream_cheese": "pick up the cream cheese and place it in the basket",
    "pick_up_the_butter": "pick up the butter and place it in the basket",
    "pick_up_the_ketchup": "pick up the ketchup and place it in the basket",
    "pick_up_the_tomato_sauce": "pick up the tomato sauce and place it in the basket",
    "pick_up_the_bbq_sauce": "pick up the bbq sauce and place it in the basket",
    "pick_up_the_chocolate_pudding": "pick up the chocolate pudding and place it in the basket",
    "pick_up_the_salad_dressing": "pick up the salad dressing and place it in the basket",
    "pick_up_the_milk": "pick up the milk and place it in the basket",
    "pick_up_the_orange_juice": "pick up the orange juice and place it in the basket",
}
DEFAULT_PROMPT = "pick up the object and place it in the basket"


def get_prompt_for_task(task_name):
    tn_lower = task_name.lower()
    for key, desc in TASK_PROMPTS.items():
        if key in tn_lower:
            return f"In: What action should the robot take to {desc}?\nOut:"
    return f"In: What action should the robot take to {DEFAULT_PROMPT}?\nOut:"


def load_libero_images():
    hdf5_files = sorted(glob.glob(os.path.join(LIBERO_DIR, "*.hdf5")))
    if not hdf5_files:
        hdf5_files = sorted(glob.glob(os.path.join(LIBERO_DIR, "**/*.hdf5"), recursive=True))
    print(f"[*] Found {len(hdf5_files)} HDF5 files in {LIBERO_DIR}")

    all_images = []
    task_names = []

    for hdf5_path in hdf5_files:
        task_name = os.path.splitext(os.path.basename(hdf5_path))[0]

        with h5py.File(hdf5_path, "r") as f:
            if "data" not in f:
                continue
            demo_keys = sorted(
                [k for k in f["data"].keys() if k.startswith("demo")],
                key=lambda x: int(x.split("_")[-1])
            )
            if not demo_keys:
                continue

            obs_keys = list(f[f"data/{demo_keys[0]}/obs"].keys())
            img_key = None
            for candidate in ["agentview_rgb", "agentview_image", "image", "rgb"]:
                if candidate in obs_keys:
                    img_key = candidate
                    break
            if img_key is None:
                for k in obs_keys:
                    shape = f[f"data/{demo_keys[0]}/obs/{k}"].shape
                    if len(shape) == 4 and shape[-1] == 3:
                        img_key = k
                        break
            if img_key is None:
                continue

            frame_pool = []
            for dk in demo_keys:
                n_frames = f[f"data/{dk}/obs/{img_key}"].shape[0]
                frame_pool.append((dk, n_frames))
            total_frames = sum(n for _, n in frame_pool)

            rng = np.random.RandomState(42)
            target = min(IMAGES_PER_TASK, total_frames)
            indices = []
            for dk, n in frame_pool:
                for i in range(n):
                    indices.append((dk, i))
            chosen = rng.choice(len(indices), size=target, replace=False)
            chosen.sort()

            by_demo = {}
            for idx in chosen:
                dk, frame_i = indices[idx]
                by_demo.setdefault(dk, []).append(frame_i)

            sampled = 0
            for dk, frame_indices in by_demo.items():
                imgs = f[f"data/{dk}/obs/{img_key}"][:]
                for fi in frame_indices:
                    all_images.append(Image.fromarray(imgs[fi]))
                    task_names.append(task_name)
                    sampled += 1

            print(f"  {task_name}: {sampled} frames")

    unique_tasks = sorted(set(task_names))
    print(f"[*] Total: {len(all_images)} images from {len(unique_tasks)} tasks")
    return all_images, task_names, unique_tasks


def load_model():
    print(f"\n[*] Model name: {MODEL_NAME}", flush=True)

    if LORA_ADAPTER_PATH:
        print(f"[*] Loading base model from: {BASE_CHECKPOINT_PATH}", flush=True)
        print(f"[*] Applying LoRA adapter from: {LORA_ADAPTER_PATH}", flush=True)
        config = OpenVLAConfig.from_pretrained(BASE_CHECKPOINT_PATH)
        model = OpenVLAForActionPrediction.from_pretrained(
            BASE_CHECKPOINT_PATH,
            config=config,
            torch_dtype=torch.bfloat16,
            low_cpu_mem_usage=True,
            attn_implementation="eager",
        )
        from peft import PeftModel
        model = PeftModel.from_pretrained(model, LORA_ADAPTER_PATH, is_trainable=False)
        model = model.merge_and_unload()
        print("[*] LoRA adapter merged", flush=True)
        model = model.to(DEVICE)
    else:
        print(f"[*] Loading model from: {CHECKPOINT_PATH}", flush=True)
        config = OpenVLAConfig.from_pretrained(CHECKPOINT_PATH)
        model = OpenVLAForActionPrediction.from_pretrained(
            CHECKPOINT_PATH,
            config=config,
            torch_dtype=torch.bfloat16,
            low_cpu_mem_usage=True,
            attn_implementation="eager",
        ).to(DEVICE)

    stats_path = os.path.join(CHECKPOINT_PATH, "dataset_statistics.json")
    if not os.path.exists(stats_path):
        stats_path = os.path.join(BASE_CHECKPOINT_PATH, "dataset_statistics.json")
    with open(stats_path) as f:
        model.norm_stats = json.load(f)
    model.eval()

    from transformers import AutoTokenizer

    tok_path = CHECKPOINT_PATH if os.path.exists(os.path.join(CHECKPOINT_PATH, "tokenizer.json")) else BASE_CHECKPOINT_PATH
    tokenizer = AutoTokenizer.from_pretrained(tok_path)
    img_path = CHECKPOINT_PATH if os.path.exists(os.path.join(CHECKPOINT_PATH, "preprocessor_config.json")) else BASE_CHECKPOINT_PATH
    image_processor = PrismaticImageProcessor.from_pretrained(img_path)
    processor = PrismaticProcessor(image_processor=image_processor, tokenizer=tokenizer)

    print(f"[*] Model loaded, GPU mem: {torch.cuda.max_memory_allocated()/1e9:.1f} GB", flush=True)
    return model, processor


def compute_entropy_bits(p, eps=1e-10):
    p = p.clamp(min=eps)
    return -(p * p.log2()).sum(dim=-1)


class ProjectorHook:
    """Hook to capture and optionally prune projector output."""
    def __init__(self):
        self.keep_ratio = 1.0
        self.projected_features = None
        self.norms = None

    def __call__(self, module, input, output):
        self.projected_features = output.detach().clone()
        self.norms = output.detach().norm(dim=-1)  # (B, N)

        if self.keep_ratio < 1.0:
            B, N, D = output.shape
            k = max(1, int(N * self.keep_ratio))
            _, topk_idx = torch.topk(self.norms, k, dim=-1)
            mask = torch.zeros(B, N, device=output.device, dtype=output.dtype)
            mask.scatter_(1, topk_idx, 1.0)
            output = output * mask.unsqueeze(-1)

        return output


def run_analysis(model, processor, images, task_names, unique_tasks):
    n_images = len(images)
    n_layers = model.language_model.config.num_hidden_layers
    n_heads = model.language_model.config.num_attention_heads
    print(f"[*] LLM: {n_layers} layers, {n_heads} heads", flush=True)

    # Register projector hook
    hook = ProjectorHook()
    handle = model.projector.register_forward_hook(hook)

    # === Part A: Attention Entropy ===
    print(f"\n{'='*60}")
    print("Part A: Attention Entropy Analysis")
    print(f"{'='*60}", flush=True)

    all_entropies = []
    all_vision_attn_frac = []

    for idx in range(n_images):
        img = images[idx]
        task = task_names[idx]
        prompt = get_prompt_for_task(task)

        inputs = processor(prompt, img).to(DEVICE, dtype=torch.bfloat16)
        hook.keep_ratio = 1.0

        with torch.no_grad():
            outputs = model(
                **inputs,
                output_attentions=True,
                return_dict=True,
            )

        attentions = outputs.attentions

        if idx == 0:
            seq_len = attentions[0].shape[-1]
            text_start = 1 + N_VISION_TOKENS
            print(f"[*] Seq len: {seq_len}, vision: [1, {1+N_VISION_TOKENS}), text starts: {text_start}")
            print(f"[*] Attention shape: {attentions[0].shape}")
            print(f"[*] Layers returned: {len(attentions)}", flush=True)

        text_start = 1 + N_VISION_TOKENS
        sample_entropies = np.zeros((n_layers, n_heads))
        sample_vis_frac = np.zeros((n_layers, n_heads))

        for layer_idx in range(len(attentions)):
            attn = attentions[layer_idx]
            text_to_vision = attn[0, :, text_start:, 1:1+N_VISION_TOKENS].float()
            text_to_all = attn[0, :, text_start:, :].float()

            vis_frac = text_to_vision.sum(dim=-1) / text_to_all.sum(dim=-1).clamp(min=1e-10)
            sample_vis_frac[layer_idx] = vis_frac.mean(dim=-1).cpu().numpy()

            vis_sum = text_to_vision.sum(dim=-1, keepdim=True).clamp(min=1e-10)
            text_to_vision_norm = text_to_vision / vis_sum

            ent = compute_entropy_bits(text_to_vision_norm)
            sample_entropies[layer_idx] = ent.mean(dim=-1).cpu().numpy()

        all_entropies.append(sample_entropies)
        all_vision_attn_frac.append(sample_vis_frac)

        if (idx + 1) % 10 == 0 or idx == 0:
            cur_mean = np.mean(all_entropies)
            cur_ratio = cur_mean / math.log2(N_VISION_TOKENS)
            print(f"  [{idx+1}/{n_images}] entropy_ratio={cur_ratio:.4f}", flush=True)

        del outputs, attentions
        torch.cuda.empty_cache()

    all_entropies = np.array(all_entropies)
    all_vision_attn_frac = np.array(all_vision_attn_frac)
    max_entropy = math.log2(N_VISION_TOKENS)

    per_layer_mean = all_entropies.mean(axis=(0, 2))
    per_layer_std = all_entropies.std(axis=(0, 2))
    per_layer_ratio = per_layer_mean / max_entropy
    per_layer_ratio_std = per_layer_std / max_entropy
    per_layer_vis_frac = all_vision_attn_frac.mean(axis=(0, 2))

    overall_mean = float(all_entropies.mean())
    overall_std = float(all_entropies.std())
    overall_ratio = overall_mean / max_entropy
    overall_ratio_std = overall_std / max_entropy

    min_layer = int(per_layer_ratio.argmin())
    max_layer = int(per_layer_ratio.argmax())

    print(f"\n[ENTROPY RESULTS]")
    print(f"Overall entropy ratio: {overall_ratio:.4f} +/- {overall_ratio_std:.4f}")
    print(f"Min layer: {min_layer} (ratio={per_layer_ratio[min_layer]:.4f})")
    print(f"Max layer: {max_layer} (ratio={per_layer_ratio[max_layer]:.4f})")

    entropy_results = {
        "model": MODEL_NAME,
        "dataset": "LIBERO-Object",
        "n_images": n_images,
        "n_tasks_covered": len(unique_tasks),
        "tasks": unique_tasks,
        "n_vision_tokens": N_VISION_TOKENS,
        "max_entropy_bits": max_entropy,
        "n_layers": n_layers,
        "n_heads": n_heads,
        "per_layer_entropy_ratio": {str(i): round(float(per_layer_ratio[i]), 4) for i in range(len(per_layer_ratio))},
        "per_layer_entropy_std": {str(i): round(float(per_layer_ratio_std[i]), 4) for i in range(len(per_layer_ratio_std))},
        "per_layer_vision_attention_fraction": {str(i): round(float(per_layer_vis_frac[i]), 4) for i in range(len(per_layer_vis_frac))},
        "overall_entropy_ratio": round(overall_ratio, 4),
        "overall_entropy_std": round(overall_ratio_std, 4),
        "overall_vision_attention_fraction": round(float(all_vision_attn_frac.mean()), 4),
        "min_entropy_layer": {"layer": min_layer, "ratio": round(float(per_layer_ratio[min_layer]), 4)},
        "max_entropy_layer": {"layer": max_layer, "ratio": round(float(per_layer_ratio[max_layer]), 4)},
    }

    # === Part B: Pruning Curve ===
    print(f"\n{'='*60}")
    print("Part B: Pruning Curve (L2-norm, hidden state degradation)")
    print(f"{'='*60}", flush=True)

    pruning_losses = {k: [] for k in KEEP_RATIOS}

    for idx in range(n_images):
        img = images[idx]
        task = task_names[idx]
        prompt = get_prompt_for_task(task)
        inputs = processor(prompt, img).to(DEVICE, dtype=torch.bfloat16)

        # Full forward (k=1.0) to get reference hidden states
        hook.keep_ratio = 1.0
        with torch.no_grad():
            out_full = model(
                **inputs,
                output_hidden_states=True,
                return_dict=True,
            )
        h_full = out_full.hidden_states[-1][:, 1+N_VISION_TOKENS:, :].float()  # text positions only
        h_full_norm_sq = (h_full ** 2).sum().item()

        pruning_losses[1.0].append(0.0)

        for k in KEEP_RATIOS:
            if k >= 1.0:
                continue
            hook.keep_ratio = k
            with torch.no_grad():
                out_pruned = model(
                    **inputs,
                    output_hidden_states=True,
                    return_dict=True,
                )
            h_pruned = out_pruned.hidden_states[-1][:, 1+N_VISION_TOKENS:, :].float()
            degradation = ((h_pruned - h_full) ** 2).sum().item()
            normalized = degradation / max(h_full_norm_sq, 1e-10)
            pruning_losses[k].append(normalized)

            del out_pruned
            torch.cuda.empty_cache()

        del out_full
        torch.cuda.empty_cache()

        if (idx + 1) % 10 == 0 or idx == 0:
            summary = {k: f"{np.mean(v):.6f}" for k, v in pruning_losses.items() if v}
            print(f"  [{idx+1}/{n_images}] losses={summary}", flush=True)

    pruning_results = {}
    for k in KEEP_RATIOS:
        vals = pruning_losses[k]
        pruning_results[str(k)] = {
            "normalized_loss": round(float(np.mean(vals)), 6),
            "std": round(float(np.std(vals)), 6),
            "n_tokens_kept": max(1, int(N_VISION_TOKENS * k)),
        }

    print(f"\n[PRUNING RESULTS]")
    print(f"{'k':>6} {'tokens':>6} {'norm_loss':>12} {'std':>10}")
    for k in KEEP_RATIOS:
        r = pruning_results[str(k)]
        print(f"  {k:.2f}   {r['n_tokens_kept']:>4}   {r['normalized_loss']:>10.6f}   {r['std']:>8.6f}")

    handle.remove()

    return entropy_results, pruning_results


def main():
    print("=" * 60)
    print("OpenVLA-OFT Token Importance Analysis")
    print("=" * 60, flush=True)
    t0 = time.time()

    images, task_names, unique_tasks = load_libero_images()
    if not images:
        print("ERROR: No images loaded!")
        sys.exit(1)

    model, processor = load_model()
    entropy_results, pruning_results = run_analysis(model, processor, images, task_names, unique_tasks)

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    name_slug = MODEL_NAME.lower().replace(" ", "_").replace("-", "_")
    entropy_path = os.path.join(OUTPUT_DIR, f"{name_slug}_attention_entropy_perlayer.json")
    with open(entropy_path, "w") as f:
        json.dump(entropy_results, f, indent=2)
    print(f"\n[*] Entropy results saved to {entropy_path}")

    pruning_path = os.path.join(OUTPUT_DIR, f"{name_slug}_pruning_curve.json")
    pruning_out = {
        "model": MODEL_NAME,
        "dataset": "LIBERO-Object",
        "n_images": len(images),
        "metric": "hidden_state_degradation_normalized",
        "description": "MSE(H_pruned - H_full) / ||H_full||^2 at text token positions",
        "keep_ratios": {str(k): pruning_results[str(k)] for k in KEEP_RATIOS},
    }
    with open(pruning_path, "w") as f:
        json.dump(pruning_out, f, indent=2)
    print(f"[*] Pruning results saved to {pruning_path}")

    print(f"\n[*] Total time: {time.time()-t0:.1f}s")


if __name__ == "__main__":
    main()
