"""
Measure OpenVLA attention entropy on REAL LIBERO-Object observation images.

Replaces the prior analysis (20 random noise images) with >=200 real frames
sampled across all 10 LIBERO-Object tasks.

Usage:
    source /root/miniconda3/bin/activate
    HF_HOME=/root/autodl-tmp/.hf_cache CUDA_VISIBLE_DEVICES=0 \
        python measure_openvla_entropy_real.py
"""

import glob
import json
import math
import os
import sys
import time

os.environ["TRANSFORMERS_OFFLINE"] = "1"
os.environ["HF_HUB_OFFLINE"] = "1"
os.environ.setdefault("HF_HOME", "/root/autodl-tmp/.hf_cache")

sys.path.insert(0, "/root/autodl-tmp/openvla_deps")

import h5py
import numpy as np
import torch
from PIL import Image

hf_dir = "/root/autodl-tmp/openvla-repo/prismatic/extern/hf"
init_path = os.path.join(hf_dir, "__init__.py")
if not os.path.exists(init_path):
    open(init_path, "w").close()
sys.path.insert(0, "/root/autodl-tmp/openvla-repo/prismatic/extern")
from hf.configuration_prismatic import OpenVLAConfig
from hf.modeling_prismatic import OpenVLAForActionPrediction
from hf.processing_prismatic import PrismaticImageProcessor, PrismaticProcessor

DEVICE = torch.device("cuda:0")
CHECKPOINT_PATH = "/root/autodl-tmp/openvla-libero-object"
LIBERO_DIR = "/root/autodl-tmp/libero/libero_object"
N_VISION_TOKENS = 256
IMAGES_PER_TASK = 25
OUTPUT_DIR = "/root/autodl-tmp/importance_margin_vla_compress/eval_results"


def load_libero_images():
    """Load real observation images from LIBERO-Object HDF5 files."""
    hdf5_files = sorted(glob.glob(os.path.join(LIBERO_DIR, "*.hdf5")))
    if not hdf5_files:
        hdf5_files = sorted(glob.glob(os.path.join(LIBERO_DIR, "**/*.hdf5"), recursive=True))
    print(f"[*] Found {len(hdf5_files)} HDF5 files in {LIBERO_DIR}")

    all_images = []
    task_names = []

    for hdf5_path in hdf5_files:
        task_name = os.path.splitext(os.path.basename(hdf5_path))[0]
        print(f"  Loading: {task_name}")

        with h5py.File(hdf5_path, "r") as f:
            if "data" not in f:
                print(f"    WARNING: no 'data' key, keys = {list(f.keys())}")
                continue

            demo_keys = sorted(
                [k for k in f["data"].keys() if k.startswith("demo")],
                key=lambda x: int(x.split("_")[-1])
            )
            if not demo_keys:
                print(f"    WARNING: no demos found")
                continue

            # Discover image key from first demo
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
                print(f"    WARNING: no image key found, obs keys = {obs_keys}")
                continue

            # Collect frame indices across demos for uniform sampling
            frame_pool = []
            for dk in demo_keys:
                n_frames = f[f"data/{dk}/obs/{img_key}"].shape[0]
                frame_pool.append((dk, n_frames))

            total_frames = sum(n for _, n in frame_pool)
            print(f"    {len(demo_keys)} demos, {total_frames} total frames, img_key={img_key}")

            # Sample IMAGES_PER_TASK frames uniformly
            rng = np.random.RandomState(42)
            sampled = 0
            target = min(IMAGES_PER_TASK, total_frames)

            if total_frames <= target:
                # Take all frames
                for dk, n in frame_pool:
                    imgs = f[f"data/{dk}/obs/{img_key}"][:]
                    for i in range(n):
                        all_images.append(Image.fromarray(imgs[i]))
                        task_names.append(task_name)
                        sampled += 1
            else:
                # Sample uniformly across demos
                indices = []
                for dk, n in frame_pool:
                    for i in range(n):
                        indices.append((dk, i))
                chosen = rng.choice(len(indices), size=target, replace=False)
                chosen.sort()

                # Group by demo for efficient loading
                by_demo = {}
                for idx in chosen:
                    dk, frame_i = indices[idx]
                    by_demo.setdefault(dk, []).append(frame_i)

                for dk, frame_indices in by_demo.items():
                    imgs = f[f"data/{dk}/obs/{img_key}"][:]
                    for fi in frame_indices:
                        all_images.append(Image.fromarray(imgs[fi]))
                        task_names.append(task_name)
                        sampled += 1

            print(f"    Sampled {sampled} frames")

    unique_tasks = sorted(set(task_names))
    print(f"\n[*] Total: {len(all_images)} images from {len(unique_tasks)} tasks")
    for t in unique_tasks:
        count = task_names.count(t)
        print(f"    {t}: {count} images")

    return all_images, task_names, unique_tasks


def load_model():
    print(f"\n[*] Loading OpenVLA from: {CHECKPOINT_PATH}", flush=True)
    config = OpenVLAConfig.from_pretrained(CHECKPOINT_PATH)
    vla = OpenVLAForActionPrediction.from_pretrained(
        CHECKPOINT_PATH,
        config=config,
        torch_dtype=torch.bfloat16,
        low_cpu_mem_usage=True,
        attn_implementation="eager",
    ).to(DEVICE)
    with open(os.path.join(CHECKPOINT_PATH, "dataset_statistics.json")) as f:
        vla.norm_stats = json.load(f)
    vla.eval()

    from transformers import AutoTokenizer
    tokenizer = AutoTokenizer.from_pretrained(CHECKPOINT_PATH)
    image_processor = PrismaticImageProcessor.from_pretrained(CHECKPOINT_PATH)
    processor = PrismaticProcessor(image_processor=image_processor, tokenizer=tokenizer)
    print(f"[*] Model loaded, GPU mem: {torch.cuda.max_memory_allocated()/1e9:.1f} GB", flush=True)
    return vla, processor


TASK_PROMPTS = {
    "pick_up_the_alphabet_soup": "pick up the alphabet soup and place it in the basket",
    "pick_up_the_cream_cheese": "pick up the cream cheese and place it in the bowl",
    "pick_up_the_butter": "pick up the butter and place it in the basket",
    "pick_up_the_ketchup": "pick up the ketchup and place it in the basket",
    "pick_up_the_tomato_sauce": "pick up the tomato sauce and place it in the basket",
    "pick_up_the_bbq_sauce": "pick up the bbq sauce and place it in the basket",
    "pick_up_the_chocolate_pudding": "pick up the chocolate pudding and place it in the basket",
    "pick_up_the_salad_dressing": "pick up the salad dressing and place it in the basket",
    "turn_on_the_stove": "turn on the stove",
    "put_the_bowl_on_the_stove": "put the bowl on the stove",
}

DEFAULT_PROMPT = "pick up the object"


def get_prompt_for_task(task_name):
    tn_lower = task_name.lower()
    for key, desc in TASK_PROMPTS.items():
        if key in tn_lower:
            return f"In: What action should the robot take to {desc}?\nOut:"
    return f"In: What action should the robot take to {DEFAULT_PROMPT}?\nOut:"


def compute_entropy_bits(p, eps=1e-10):
    p = p.clamp(min=eps)
    return -(p * p.log2()).sum(dim=-1)


def main():
    print("=" * 60)
    print("OpenVLA Attention Entropy — REAL LIBERO-Object Images")
    print("=" * 60, flush=True)

    t0 = time.time()

    images, task_names, unique_tasks = load_libero_images()
    n_images = len(images)
    if n_images == 0:
        print("ERROR: No images loaded!")
        sys.exit(1)

    vla, processor = load_model()

    n_layers = vla.language_model.config.num_hidden_layers
    n_heads = vla.language_model.config.num_attention_heads
    print(f"[*] LLM: {n_layers} layers, {n_heads} heads", flush=True)
    print(f"[*] Processing {n_images} images...\n", flush=True)

    all_entropies = []
    all_vision_attn_frac = []

    for idx in range(n_images):
        img = images[idx]
        task = task_names[idx]
        prompt = get_prompt_for_task(task)

        inputs = processor(prompt, img).to(DEVICE, dtype=torch.bfloat16)

        with torch.no_grad():
            outputs = vla(
                **inputs,
                output_attentions=True,
                return_dict=True,
            )

        attentions = outputs.attentions

        if idx == 0:
            seq_len = attentions[0].shape[-1]
            text_start = 1 + N_VISION_TOKENS
            n_text = seq_len - text_start
            print(f"[*] Seq len: {seq_len}, vision: [1, {1+N_VISION_TOKENS}), text starts: {text_start}")
            print(f"[*] Attention shape: {attentions[0].shape}")
            print(f"[*] Layers returned: {len(attentions)}", flush=True)

        text_start = 1 + N_VISION_TOKENS
        sample_entropies = np.zeros((n_layers, n_heads))
        sample_vis_frac = np.zeros((n_layers, n_heads))

        for layer_idx in range(len(attentions)):
            attn = attentions[layer_idx]  # (1, H, seq_len, seq_len)

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
            elapsed = time.time() - t0
            eta = elapsed / (idx + 1) * (n_images - idx - 1)
            print(f"  [{idx+1}/{n_images}] entropy_ratio={cur_ratio:.4f} "
                  f"elapsed={elapsed:.0f}s ETA={eta:.0f}s", flush=True)

        del outputs, attentions
        torch.cuda.empty_cache()

    all_entropies = np.array(all_entropies)       # (N, n_layers, n_heads)
    all_vision_attn_frac = np.array(all_vision_attn_frac)

    max_entropy = math.log2(N_VISION_TOKENS)  # 8.0

    per_layer_mean = all_entropies.mean(axis=(0, 2))
    per_layer_std = all_entropies.std(axis=(0, 2))
    per_layer_ratio = per_layer_mean / max_entropy
    per_layer_ratio_std = per_layer_std / max_entropy
    per_layer_vis_frac = all_vision_attn_frac.mean(axis=(0, 2))

    overall_mean = float(all_entropies.mean())
    overall_std = float(all_entropies.std())
    overall_ratio = overall_mean / max_entropy
    overall_ratio_std = overall_std / max_entropy
    overall_vis_frac = float(all_vision_attn_frac.mean())

    min_layer = int(per_layer_ratio.argmin())
    max_layer = int(per_layer_ratio.argmax())

    print("\n" + "=" * 60)
    print("RESULTS — OpenVLA on REAL LIBERO-Object")
    print("=" * 60)
    print(f"Images: {n_images} (from {len(unique_tasks)} tasks)")
    print(f"Vision tokens: {N_VISION_TOKENS}, Max entropy: {max_entropy:.2f} bits")
    print()
    print(f"Overall entropy ratio:    {overall_ratio:.4f} +/- {overall_ratio_std:.4f}")
    print(f"Overall vision attn frac: {overall_vis_frac:.4f}")
    print()
    print(f"Comparison:")
    print(f"  SmolVLA entropy ratio:    0.98 (2400 real frames)")
    print(f"  OpenVLA (random, N=20):   0.617")
    print(f"  OpenVLA (REAL, N={n_images}):  {overall_ratio:.4f}")
    print()
    print(f"Min entropy layer: {min_layer} (ratio={per_layer_ratio[min_layer]:.4f})")
    print(f"Max entropy layer: {max_layer} (ratio={per_layer_ratio[max_layer]:.4f})")
    print()
    print(f"{'Layer':>5} {'Ratio':>7} {'Std':>7} {'VisFrac':>8}")
    print("-" * 35)
    for i in range(len(per_layer_ratio)):
        print(f"  {i:3d}  {per_layer_ratio[i]:.4f}  {per_layer_ratio_std[i]:.4f}  {per_layer_vis_frac[i]:.4f}")

    # Build output JSON in requested format
    results = {
        "model": "OpenVLA-7B-libero-object",
        "dataset": "LIBERO-Object",
        "n_images": n_images,
        "n_tasks_covered": len(unique_tasks),
        "tasks": unique_tasks,
        "per_layer_entropy_ratio": {str(i): round(float(per_layer_ratio[i]), 4) for i in range(len(per_layer_ratio))},
        "per_layer_entropy_std": {str(i): round(float(per_layer_ratio_std[i]), 4) for i in range(len(per_layer_ratio_std))},
        "per_layer_vision_attention_fraction": {str(i): round(float(per_layer_vis_frac[i]), 4) for i in range(len(per_layer_vis_frac))},
        "overall_entropy_ratio": round(overall_ratio, 4),
        "overall_entropy_std": round(overall_ratio_std, 4),
        "overall_vision_attention_fraction": round(overall_vis_frac, 4),
        "min_entropy_layer": {"layer": min_layer, "ratio": round(float(per_layer_ratio[min_layer]), 4)},
        "max_entropy_layer": {"layer": max_layer, "ratio": round(float(per_layer_ratio[max_layer]), 4)},
        "comparison_note": f"Measured on {n_images} real LIBERO-Object observations across {len(unique_tasks)} tasks (vs previous 20 random noise images)",
        "previous_random_result": {
            "n_images": 20,
            "overall_entropy_ratio": 0.617,
            "source": "random noise images"
        },
        "smolvla_reference": {
            "entropy_ratio": 0.98,
            "n_frames": 2400,
            "source": "real LIBERO-Object frames"
        }
    }

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    out_path = os.path.join(OUTPUT_DIR, "openvla_attention_entropy_real.json")
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\n[*] Results saved to {out_path}")
    print(f"[*] Total time: {time.time()-t0:.1f}s")


if __name__ == "__main__":
    main()
