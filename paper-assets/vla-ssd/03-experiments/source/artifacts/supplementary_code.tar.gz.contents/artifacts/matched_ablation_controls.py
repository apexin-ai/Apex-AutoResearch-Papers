"""Matched-size ablation controls: random-24 and image-dominant-24 heads.

Two ablation control experiments for action trajectory specificity analysis:
1. Random-24: 5 seeds, each randomly selecting 24/32 L1 heads
2. Image-dominant-24: top-24 heads by vision attention fraction
"""

import argparse
import gc
import glob
import json
import math
import os
import sys
import time

sys.path.insert(0, "/root/autodl-tmp/LIBERO")

os.environ["MUJOCO_GL"] = "egl"
os.environ["HDF5_USE_FILE_LOCKING"] = "FALSE"

import h5py
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from PIL import Image
from scipy import stats

MODEL_PATH = "/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b"
UNNORM_KEY = "bridge_orig"
DATA_DIR = "/root/autodl-tmp/vla-ssd/data/libero/libero_goal"
RESULTS_DIR = "/root/autodl-tmp/vla-ssd/results"
DECOMP_PATH = "/root/autodl-tmp/vla-ssd/results/attention_decomposition.json"

NUM_IMAGE_TOKENS = 256
INST_START = 1 + NUM_IMAGE_TOKENS
NUM_HEADS = 32
N_ABLATE = 24

RANDOM_SEEDS = [42, 123, 456, 789, 1024]
INSTRUCTION_DOMINANT_24_TRAJ_D = 0.65
DIM_NAMES = ["dx", "dy", "dz", "rx", "ry", "rz", "gripper"]


def load_model():
    from transformers import AutoModelForVision2Seq, AutoProcessor
    processor = AutoProcessor.from_pretrained(MODEL_PATH, trust_remote_code=True)
    model = AutoModelForVision2Seq.from_pretrained(
        MODEL_PATH,
        torch_dtype=torch.bfloat16,
        trust_remote_code=True,
        low_cpu_mem_usage=True,
        attn_implementation="eager",
    ).to("cuda:0").eval()
    return model, processor


def predict_action(model, input_ids, pixel_values, unnorm_key):
    action_dim = model.get_action_dim(unnorm_key)
    if not torch.all(input_ids[:, -1] == 29871):
        input_ids = torch.cat(
            (input_ids, torch.tensor([[29871]], device=input_ids.device, dtype=input_ids.dtype)),
            dim=1,
        )
    with torch.no_grad():
        outputs = model(
            input_ids=input_ids,
            attention_mask=torch.ones_like(input_ids),
            pixel_values=pixel_values,
            past_key_values=None,
            use_cache=True,
        )
    past_key_values = outputs.past_key_values
    next_token_logits = outputs.logits[:, -1, :]

    generated_ids = []
    for _ in range(action_dim):
        next_token = torch.argmax(next_token_logits, dim=-1, keepdim=True)
        generated_ids.append(next_token.squeeze().item())
        attn_mask = torch.ones(
            (1, past_key_values[0][0].shape[2] + 1),
            device=input_ids.device,
            dtype=input_ids.dtype,
        )
        with torch.no_grad():
            outputs = model(
                input_ids=next_token,
                attention_mask=attn_mask,
                pixel_values=None,
                past_key_values=past_key_values,
                use_cache=True,
            )
        past_key_values = outputs.past_key_values
        next_token_logits = outputs.logits[:, -1, :]

    predicted_action_token_ids = np.array(generated_ids)
    discretized_actions = model.vocab_size - predicted_action_token_ids
    discretized_actions = np.clip(
        discretized_actions - 1, a_min=0, a_max=model.bin_centers.shape[0] - 1
    )
    normalized_actions = model.bin_centers[discretized_actions]
    action_norm_stats = model.get_action_stats(unnorm_key)
    mask = action_norm_stats.get("mask", np.ones_like(action_norm_stats["q01"], dtype=bool))
    action_high = np.array(action_norm_stats["q99"])
    action_low = np.array(action_norm_stats["q01"])
    action = np.where(
        mask,
        0.5 * (normalized_actions + 1) * (action_high - action_low) + action_low,
        normalized_actions,
    )
    return action, predicted_action_token_ids


def install_ablation_hook(model):
    from transformers.models.llama.modeling_llama import apply_rotary_pos_emb, repeat_kv

    layer_attn = model.language_model.model.layers[1].self_attn
    layer_attn._ablate_heads = None
    original_forward = layer_attn.forward

    def ablated_forward(
        hidden_states,
        attention_mask=None,
        position_ids=None,
        past_key_value=None,
        output_attentions=False,
        use_cache=False,
        cache_position=None,
        **kwargs,
    ):
        bsz, q_len, _ = hidden_states.size()
        query_states = layer_attn.q_proj(hidden_states)
        key_states = layer_attn.k_proj(hidden_states)
        value_states = layer_attn.v_proj(hidden_states)

        query_states = query_states.view(bsz, q_len, layer_attn.num_heads, layer_attn.head_dim).transpose(1, 2)
        key_states = key_states.view(bsz, q_len, layer_attn.num_key_value_heads, layer_attn.head_dim).transpose(1, 2)
        value_states = value_states.view(bsz, q_len, layer_attn.num_key_value_heads, layer_attn.head_dim).transpose(1, 2)

        pkv = getattr(layer_attn, "past_key_value", past_key_value)
        cos, sin = layer_attn.rotary_emb(value_states, position_ids)
        query_states, key_states = apply_rotary_pos_emb(query_states, key_states, cos, sin)

        if pkv is not None:
            cache_kwargs = {"sin": sin, "cos": cos, "cache_position": cache_position}
            key_states, value_states = pkv.update(key_states, value_states, layer_attn.layer_idx, cache_kwargs)

        key_states = repeat_kv(key_states, layer_attn.num_key_value_groups)
        value_states = repeat_kv(value_states, layer_attn.num_key_value_groups)

        attn_weights = torch.matmul(query_states, key_states.transpose(2, 3)) / math.sqrt(layer_attn.head_dim)
        if attention_mask is not None:
            causal_mask = attention_mask[:, :, :, :key_states.shape[-2]]
            attn_weights = attn_weights + causal_mask

        attn_weights = nn.functional.softmax(attn_weights, dim=-1, dtype=torch.float32).to(query_states.dtype)
        attn_weights = nn.functional.dropout(attn_weights, p=layer_attn.attention_dropout, training=layer_attn.training)

        if layer_attn._ablate_heads is not None:
            kv_len = attn_weights.shape[-1]
            if INST_START < kv_len:
                attn_weights[:, layer_attn._ablate_heads, :, INST_START:] = 0.0
                row_sums = attn_weights.sum(dim=-1, keepdim=True).clamp(min=1e-9)
                attn_weights = attn_weights / row_sums

        attn_output = torch.matmul(attn_weights, value_states)
        attn_output = attn_output.transpose(1, 2).contiguous()
        attn_output = attn_output.reshape(bsz, q_len, layer_attn.hidden_size)
        attn_output = layer_attn.o_proj(attn_output)

        if not output_attentions:
            attn_weights = None
        return attn_output, attn_weights, pkv

    layer_attn.forward = ablated_forward
    return original_forward, layer_attn


def remove_ablation_hook(layer_attn, original_forward):
    layer_attn._ablate_heads = None
    layer_attn.forward = original_forward


def get_task_files(n_tasks):
    hdf5_files = sorted(glob.glob(os.path.join(DATA_DIR, "*.hdf5")))
    return hdf5_files[:n_tasks]


def get_language_instruction(hdf5_path):
    with h5py.File(hdf5_path, "r") as f:
        info = json.loads(f["data"].attrs["problem_info"])
    return info["language_instruction"]


def get_image_dominant_heads(n=24):
    with open(DECOMP_PATH) as f:
        decomp = json.load(f)
    fracs = decomp["trained"]["per_head_attention_fractions"]
    vision_by_head = {}
    for i in range(NUM_HEADS):
        vision_by_head[i] = fracs[f"head_{i}"]["vision"]
    sorted_heads = sorted(range(NUM_HEADS), key=lambda h: vision_by_head[h], reverse=True)
    top_n = sorted(sorted_heads[:n])
    top_n_fracs = [vision_by_head[h] for h in top_n]
    return top_n, top_n_fracs


def get_random_heads(seed, n=24):
    rng = np.random.RandomState(seed)
    return sorted(rng.choice(NUM_HEADS, size=n, replace=False).tolist())


def compute_cohens_d_and_ci(baseline_actions, ablated_actions, baseline_ids, ablated_ids, gt_actions):
    all_b = np.array(baseline_actions)
    all_a = np.array(ablated_actions)
    all_b_ids = np.array(baseline_ids)
    all_a_ids = np.array(ablated_ids)
    all_gt = np.array(gt_actions)

    paired_mse = np.mean((all_b - all_a) ** 2, axis=1)
    traj_d = float(np.mean(paired_mse) / (np.std(paired_mse, ddof=1) + 1e-12))

    token_diff = (all_b_ids != all_a_ids).astype(float)
    per_sample_token_div = np.mean(token_diff, axis=1)
    token_d = float(np.mean(per_sample_token_div) / (np.std(per_sample_token_div, ddof=1) + 1e-12))

    n_boot = 1000
    rng = np.random.RandomState(42)
    n = len(paired_mse)
    boot_ds = []
    for _ in range(n_boot):
        idx = rng.choice(n, size=n, replace=True)
        boot_mse = paired_mse[idx]
        d = float(np.mean(boot_mse) / (np.std(boot_mse, ddof=1) + 1e-12))
        boot_ds.append(d)
    traj_ci = [float(np.percentile(boot_ds, 2.5)), float(np.percentile(boot_ds, 97.5))]

    mse_gt_baseline = float(np.mean(np.mean((all_b - all_gt) ** 2, axis=1)))
    mse_gt_ablated = float(np.mean(np.mean((all_a - all_gt) ** 2, axis=1)))

    return {
        "token_d": token_d,
        "traj_d": traj_d,
        "traj_ci": traj_ci,
        "token_divergence_rate": float(np.mean(all_b_ids != all_a_ids)),
        "paired_mse_mean": float(np.mean(paired_mse)),
        "paired_mse_std": float(np.std(paired_mse)),
        "mse_gt_baseline": mse_gt_baseline,
        "mse_gt_ablated": mse_gt_ablated,
        "n_samples": len(all_b),
    }


def main():
    parser = argparse.ArgumentParser(description="Matched-size ablation controls")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    n_tasks = 1 if args.dry_run else 3
    n_demos = 1 if args.dry_run else 10
    n_timesteps = 2 if args.dry_run else 50

    os.makedirs(RESULTS_DIR, exist_ok=True)

    random_head_sets = {seed: get_random_heads(seed, N_ABLATE) for seed in RANDOM_SEEDS}
    image_dom_heads, image_dom_fracs = get_image_dominant_heads(N_ABLATE)

    print("=== Matched-Size Ablation Controls ===")
    print(f"Config: {n_tasks} tasks, {n_demos} demos/task, {n_timesteps} steps/demo")
    print(f"Random seeds: {RANDOM_SEEDS}")
    for seed, heads in random_head_sets.items():
        print(f"  Seed {seed}: {heads}")
    print(f"Image-dominant-24: {image_dom_heads}")
    print(f"  Vision fractions: {[round(v, 4) for v in image_dom_fracs]}")

    print("\nLoading model...")
    model, processor = load_model()
    print("Model loaded.")

    original_forward, layer1_attn = install_ablation_hook(model)

    task_files = get_task_files(n_tasks)
    print(f"Tasks ({n_tasks}): {[os.path.basename(f) for f in task_files]}")

    baseline_actions = []
    baseline_ids = []
    gt_actions_all = []

    conditions = [f"random_{s}" for s in RANDOM_SEEDS] + ["image_dominant"]
    cond_heads = {f"random_{s}": random_head_sets[s] for s in RANDOM_SEEDS}
    cond_heads["image_dominant"] = image_dom_heads

    cond_actions = {c: [] for c in conditions}
    cond_ids = {c: [] for c in conditions}

    total_passes = 0
    t_start = time.time()
    n_conditions = len(conditions)
    total_expected = n_tasks * n_demos * n_timesteps * (1 + n_conditions)

    for task_idx, hdf5_path in enumerate(task_files):
        task_name = os.path.basename(hdf5_path).replace("_demo.hdf5", "")
        instruction = get_language_instruction(hdf5_path)
        print(f"\n[Task {task_idx+1}/{n_tasks}] {task_name}")
        print(f"  Instruction: {instruction}")

        prompt = f"In: What action should the robot take to {instruction}?\nOut:"

        with h5py.File(hdf5_path, "r") as f:
            for demo_idx in range(n_demos):
                demo_key = f"data/demo_{demo_idx}"
                actions_data = f[f"{demo_key}/actions"][:]
                images_data = f[f"{demo_key}/obs/agentview_rgb"][:]
                n_steps = min(n_timesteps, len(actions_data))

                for step_idx in range(n_steps):
                    image_np = images_data[step_idx]
                    gt_action = actions_data[step_idx]

                    img = Image.fromarray(image_np)
                    inputs = processor(prompt, img).to("cuda:0", dtype=torch.bfloat16)
                    input_ids = inputs["input_ids"]
                    pixel_values = inputs["pixel_values"]

                    layer1_attn._ablate_heads = None
                    b_action, b_ids = predict_action(model, input_ids, pixel_values, UNNORM_KEY)
                    baseline_actions.append(b_action)
                    baseline_ids.append(b_ids)
                    gt_actions_all.append(gt_action)
                    total_passes += 1

                    for cond in conditions:
                        layer1_attn._ablate_heads = cond_heads[cond]
                        a_action, a_ids = predict_action(model, input_ids, pixel_values, UNNORM_KEY)
                        cond_actions[cond].append(a_action)
                        cond_ids[cond].append(a_ids)
                        total_passes += 1

                    torch.cuda.empty_cache()

                    if total_passes % (7 * 20) == 0:
                        elapsed = time.time() - t_start
                        rate = total_passes / elapsed
                        eta = (total_expected - total_passes) / rate
                        print(
                            f"  [{total_passes}/{total_expected} passes, "
                            f"{elapsed:.0f}s, {rate:.1f} pass/s, ETA {eta:.0f}s]"
                        )

        gc.collect()
        torch.cuda.empty_cache()

    remove_ablation_hook(layer1_attn, original_forward)

    print("\nComputing metrics...")

    random_per_seed = []
    for seed in RANDOM_SEEDS:
        cond = f"random_{seed}"
        m = compute_cohens_d_and_ci(
            baseline_actions, cond_actions[cond],
            baseline_ids, cond_ids[cond],
            gt_actions_all,
        )
        random_per_seed.append({
            "seed": seed,
            "heads": random_head_sets[seed],
            "token_d": m["token_d"],
            "traj_d": m["traj_d"],
            "traj_ci": m["traj_ci"],
            "mse_gt_baseline": m["mse_gt_baseline"],
            "mse_gt_ablated": m["mse_gt_ablated"],
        })
        print(f"  Random seed={seed}: token_d={m['token_d']:.3f}, traj_d={m['traj_d']:.3f}")

    random_token_ds = [r["token_d"] for r in random_per_seed]
    random_traj_ds = [r["traj_d"] for r in random_per_seed]

    img_m = compute_cohens_d_and_ci(
        baseline_actions, cond_actions["image_dominant"],
        baseline_ids, cond_ids["image_dominant"],
        gt_actions_all,
    )
    print(f"  Image-dominant: token_d={img_m['token_d']:.3f}, traj_d={img_m['traj_d']:.3f}")

    output = {
        "random_24": {
            "seeds": RANDOM_SEEDS,
            "per_seed": random_per_seed,
            "mean_token_d": float(np.mean(random_token_ds)),
            "std_token_d": float(np.std(random_token_ds, ddof=1)),
            "mean_traj_d": float(np.mean(random_traj_ds)),
            "std_traj_d": float(np.std(random_traj_ds, ddof=1)),
        },
        "image_dominant_24": {
            "heads": image_dom_heads,
            "image_attn_fractions": image_dom_fracs,
            "token_d": img_m["token_d"],
            "traj_d": img_m["traj_d"],
            "traj_ci": img_m["traj_ci"],
            "mse_gt_baseline": img_m["mse_gt_baseline"],
            "mse_gt_ablated": img_m["mse_gt_ablated"],
        },
        "comparison": {
            "instruction_dominant_24_traj_d": INSTRUCTION_DOMINANT_24_TRAJ_D,
            "random_24_mean_traj_d": float(np.mean(random_traj_ds)),
            "random_24_std_traj_d": float(np.std(random_traj_ds, ddof=1)),
            "image_dominant_24_traj_d": img_m["traj_d"],
        },
        "config": {
            "n_tasks": n_tasks,
            "n_demos_per_task": n_demos,
            "n_timesteps_per_demo": n_timesteps,
            "total_forward_passes": total_passes,
            "model": "openvla-7b",
            "unnorm_key": UNNORM_KEY,
        },
    }

    elapsed_total = time.time() - t_start
    print(f"\n{'='*60}")
    print(f"Done. {total_passes} forward passes in {elapsed_total:.0f}s")
    print(f"Random-24 mean traj_d: {np.mean(random_traj_ds):.3f} +/- {np.std(random_traj_ds, ddof=1):.3f}")
    print(f"Image-dominant-24 traj_d: {img_m['traj_d']:.3f}")
    print(f"Instruction-dominant-24 traj_d (reference): {INSTRUCTION_DOMINANT_24_TRAJ_D}")

    out_path = os.path.join(RESULTS_DIR, "matched_ablation_controls.json")
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"Results saved to {out_path}")


if __name__ == "__main__":
    main()
