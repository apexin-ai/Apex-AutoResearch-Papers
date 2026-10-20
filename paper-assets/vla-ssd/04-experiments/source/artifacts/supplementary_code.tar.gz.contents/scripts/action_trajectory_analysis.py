"""Open-loop action trajectory analysis: baseline vs L1-ablated on LIBERO demo observations."""

import argparse
import gc
import glob
import json
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

np.random.seed(42)
torch.manual_seed(42)

# ── Config ──────────────────────────────────────────────────────────────────
MODEL_PATH = "/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b"
UNNORM_KEY = "bridge_orig"
DATA_DIR = "/root/autodl-tmp/vla-ssd/data/libero/libero_goal"
RESULTS_DIR = "/root/autodl-tmp/vla-ssd/results"

NUM_IMAGE_TOKENS = 256
INST_START = 1 + NUM_IMAGE_TOKENS

INSTRUCTION_HEADS_24 = [
    0, 1, 2, 4, 7, 8, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20,
    22, 23, 25, 26, 27, 29, 30, 31,
]

DIM_NAMES = ["dx", "dy", "dz", "rx", "ry", "rz", "gripper"]


# ── Model loading ───────────────────────────────────────────────────────────
def load_model():
    from transformers import AutoModelForVision2Seq, AutoProcessor

    processor = AutoProcessor.from_pretrained(MODEL_PATH, trust_remote_code=True)
    model = AutoModelForVision2Seq.from_pretrained(
        MODEL_PATH,
        torch_dtype=torch.bfloat16,
        trust_remote_code=True,
        low_cpu_mem_usage=True,
    ).to("cuda:0").eval()
    return model, processor


# ── Manual autoregressive generation (bypasses generate() DynamicCache bug) ─
def predict_action_with_logits(model, input_ids, pixel_values, unnorm_key):
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
    all_logits = []

    for _ in range(action_dim):
        all_logits.append(next_token_logits.float().cpu())
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

    logits_tensor = torch.cat(all_logits, dim=0)  # (action_dim, vocab_size)
    return action, predicted_action_token_ids, logits_tensor


# ── Ablation hook ───────────────────────────────────────────────────────────
def install_ablation_hook(model, heads_to_ablate):
    import transformers.models.llama.modeling_llama as llama_mod
    from transformers.models.llama.modeling_llama import repeat_kv

    layer_attn = model.language_model.model.layers[1].self_attn
    layer_attn._ablate_heads = heads_to_ablate

    original_fn = llama_mod.eager_attention_forward

    def ablated_eager_attention_forward(
        module, query, key, value, attention_mask, scaling, dropout=0.0, **kwargs
    ):
        key_states = repeat_kv(key, module.num_key_value_groups)
        value_states = repeat_kv(value, module.num_key_value_groups)
        attn_weights = torch.matmul(query, key_states.transpose(2, 3)) * scaling
        if attention_mask is not None:
            causal_mask = attention_mask[:, :, :, : key_states.shape[-2]]
            attn_weights = attn_weights + causal_mask
        attn_weights = nn.functional.softmax(attn_weights, dim=-1, dtype=torch.float32).to(
            query.dtype
        )
        attn_weights = nn.functional.dropout(attn_weights, p=dropout, training=module.training)
        if hasattr(module, "_ablate_heads") and module._ablate_heads is not None:
            kv_len = attn_weights.shape[-1]
            if INST_START < kv_len:
                attn_weights[:, module._ablate_heads, :, INST_START:] = 0.0
                row_sums = attn_weights.sum(dim=-1, keepdim=True).clamp(min=1e-9)
                attn_weights = attn_weights / row_sums
        attn_output = torch.matmul(attn_weights, value_states)
        attn_output = attn_output.transpose(1, 2).contiguous()
        return attn_output, attn_weights

    llama_mod.eager_attention_forward = ablated_eager_attention_forward
    return original_fn


def remove_ablation_hook(model, original_fn):
    import transformers.models.llama.modeling_llama as llama_mod

    llama_mod.eager_attention_forward = original_fn
    model.language_model.model.layers[1].self_attn._ablate_heads = None


# ── KL divergence ───────────────────────────────────────────────────────────
def compute_kl_divergence(logits_p, logits_q):
    log_p = F.log_softmax(logits_p, dim=-1)
    log_q = F.log_softmax(logits_q, dim=-1)
    p = F.softmax(logits_p, dim=-1)
    kl = (p * (log_p - log_q)).sum(dim=-1)
    return kl.numpy()


# ── Helpers ─────────────────────────────────────────────────────────────────
def get_task_files(n_tasks):
    hdf5_files = sorted(glob.glob(os.path.join(DATA_DIR, "*.hdf5")))
    return hdf5_files[:n_tasks]


def get_language_instruction(hdf5_path):
    with h5py.File(hdf5_path, "r") as f:
        info = json.loads(f["data"].attrs["problem_info"])
    return info["language_instruction"]


def compute_task_metrics(task_b, task_a, task_b_ids, task_a_ids, task_kls):
    paired_mse = np.mean((task_b - task_a) ** 2, axis=1)
    t_res = stats.ttest_1samp(paired_mse, 0)
    cohens_d = np.mean(paired_mse) / (np.std(paired_mse, ddof=1) + 1e-12)

    per_dim_shift = np.abs(task_b - task_a)
    token_div = np.mean(task_b_ids != task_a_ids)

    return {
        "paired_mse": {
            "mean": float(np.mean(paired_mse)),
            "std": float(np.std(paired_mse)),
            "t_stat": float(t_res.statistic),
            "p_value": float(t_res.pvalue),
            "cohens_d": float(cohens_d),
        },
        "per_dim_shift": {
            "means": [float(x) for x in np.mean(per_dim_shift, axis=0)],
            "stds": [float(x) for x in np.std(per_dim_shift, axis=0)],
        },
        "token_divergence_rate": float(token_div),
        "kl_divergence": {
            "mean": float(np.mean(task_kls)),
            "std": float(np.std(task_kls)),
        },
        "n_samples": int(len(task_b)),
    }


# ── Main ────────────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    n_tasks = 1 if args.dry_run else 5
    n_demos = 1 if args.dry_run else 10
    n_timesteps = 2 if args.dry_run else 50

    os.makedirs(RESULTS_DIR, exist_ok=True)

    print("Loading model...")
    model, processor = load_model()
    print("Model loaded.")

    original_eager_fn = install_ablation_hook(model, INSTRUCTION_HEADS_24)
    layer1_attn = model.language_model.model.layers[1].self_attn

    task_files = get_task_files(n_tasks)
    print(f"Tasks ({n_tasks}): {[os.path.basename(f) for f in task_files]}")
    print(f"Config: {n_demos} demos/task, {n_timesteps} timesteps/demo")

    all_baseline_actions = []
    all_ablated_actions = []
    all_gt_actions = []
    all_baseline_token_ids = []
    all_ablated_token_ids = []
    all_kl_divs = []
    per_task_data = {}

    total_passes = 0
    t_start = time.time()

    for task_idx, hdf5_path in enumerate(task_files):
        task_name = os.path.basename(hdf5_path).replace("_demo.hdf5", "")
        instruction = get_language_instruction(hdf5_path)
        print(f"\n{'='*60}")
        print(f"Task {task_idx}: {task_name}")
        print(f"  Instruction: {instruction}")

        task_baseline_actions = []
        task_ablated_actions = []
        task_gt_actions = []
        task_baseline_token_ids = []
        task_ablated_token_ids = []
        task_kl_divs = []

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

                    # Baseline (ablation disabled)
                    layer1_attn._ablate_heads = None
                    b_action, b_ids, b_logits = predict_action_with_logits(
                        model, input_ids, pixel_values, UNNORM_KEY
                    )

                    # Ablated
                    layer1_attn._ablate_heads = INSTRUCTION_HEADS_24
                    a_action, a_ids, a_logits = predict_action_with_logits(
                        model, input_ids, pixel_values, UNNORM_KEY
                    )

                    kl_per_token = compute_kl_divergence(b_logits, a_logits)

                    task_baseline_actions.append(b_action)
                    task_ablated_actions.append(a_action)
                    task_gt_actions.append(gt_action)
                    task_baseline_token_ids.append(b_ids)
                    task_ablated_token_ids.append(a_ids)
                    task_kl_divs.append(kl_per_token)

                    total_passes += 2
                    if total_passes % 100 == 0:
                        elapsed = time.time() - t_start
                        rate = total_passes / elapsed
                        eta = (n_tasks * n_demos * n_timesteps * 2 - total_passes) / rate
                        print(
                            f"  [{total_passes} passes, {elapsed:.0f}s, "
                            f"{rate:.1f} pass/s, ETA {eta:.0f}s]"
                        )

                    del b_logits, a_logits
                    torch.cuda.empty_cache()

        task_b = np.array(task_baseline_actions)
        task_a = np.array(task_ablated_actions)
        task_b_ids = np.array(task_baseline_token_ids)
        task_a_ids = np.array(task_ablated_token_ids)
        task_kls = np.array(task_kl_divs)

        per_task_data[task_name] = compute_task_metrics(
            task_b, task_a, task_b_ids, task_a_ids, task_kls
        )
        m = per_task_data[task_name]
        print(
            f"  >> paired_mse={m['paired_mse']['mean']:.6f}, "
            f"token_div={m['token_divergence_rate']:.4f}, "
            f"kl={m['kl_divergence']['mean']:.4f}"
        )

        all_baseline_actions.extend(task_baseline_actions)
        all_ablated_actions.extend(task_ablated_actions)
        all_gt_actions.extend(task_gt_actions)
        all_baseline_token_ids.extend(task_baseline_token_ids)
        all_ablated_token_ids.extend(task_ablated_token_ids)
        all_kl_divs.extend(task_kl_divs)

        gc.collect()
        torch.cuda.empty_cache()

    # ── Global metrics ──────────────────────────────────────────────────────
    layer1_attn._ablate_heads = None
    remove_ablation_hook(model, original_eager_fn)

    all_b = np.array(all_baseline_actions)
    all_a = np.array(all_ablated_actions)
    all_gt = np.array(all_gt_actions)
    all_b_ids = np.array(all_baseline_token_ids)
    all_a_ids = np.array(all_ablated_token_ids)
    all_kls = np.array(all_kl_divs)

    paired_mse_all = np.mean((all_b - all_a) ** 2, axis=1)
    t_res_all = stats.ttest_1samp(paired_mse_all, 0)
    cohens_d_all = np.mean(paired_mse_all) / (np.std(paired_mse_all, ddof=1) + 1e-12)

    per_dim_shift_all = np.abs(all_b - all_a)
    token_div_all = np.mean(all_b_ids != all_a_ids)

    kl_per_position = np.mean(all_kls, axis=0)

    mse_gt_baseline = np.mean((all_b - all_gt) ** 2, axis=1)
    mse_gt_ablated = np.mean((all_a - all_gt) ** 2, axis=1)

    try:
        wilcoxon_res = stats.wilcoxon(paired_mse_all)
        wilcoxon_p = float(wilcoxon_res.pvalue)
    except Exception:
        wilcoxon_p = None

    output = {
        "config": {
            "n_tasks": n_tasks,
            "n_demos_per_task": n_demos,
            "n_timesteps_per_demo": n_timesteps,
            "total_forward_passes": total_passes,
            "model": "openvla-7b",
            "ablation": "L1_dominant_24_heads_zeroed",
            "ablated_heads": INSTRUCTION_HEADS_24,
            "unnorm_key": UNNORM_KEY,
        },
        "main_metrics": {
            "paired_action_mse": {
                "mean": float(np.mean(paired_mse_all)),
                "std": float(np.std(paired_mse_all)),
                "t_stat": float(t_res_all.statistic),
                "p_value": float(t_res_all.pvalue),
                "cohens_d": float(cohens_d_all),
            },
            "per_dim_action_shift": {
                "means": [float(x) for x in np.mean(per_dim_shift_all, axis=0)],
                "stds": [float(x) for x in np.std(per_dim_shift_all, axis=0)],
                "dim_names": DIM_NAMES,
            },
            "token_divergence_rate": float(token_div_all),
        },
        "secondary_metrics": {
            "kl_divergence": {
                "mean": float(np.mean(all_kls)),
                "std": float(np.std(all_kls)),
                "per_token_position": [float(x) for x in kl_per_position],
            },
            "mse_vs_gt_baseline": {
                "mean": float(np.mean(mse_gt_baseline)),
                "std": float(np.std(mse_gt_baseline)),
                "note": "OOD, secondary",
            },
            "mse_vs_gt_ablated": {
                "mean": float(np.mean(mse_gt_ablated)),
                "std": float(np.std(mse_gt_ablated)),
                "note": "OOD, secondary",
            },
            "wilcoxon_p": wilcoxon_p,
        },
        "per_task": per_task_data,
    }

    elapsed_total = time.time() - t_start
    print(f"\n{'='*60}")
    print(f"Done. {total_passes} forward passes in {elapsed_total:.0f}s")
    print(
        f"Paired MSE: {np.mean(paired_mse_all):.6f} "
        f"(p={t_res_all.pvalue:.2e}, d={cohens_d_all:.3f})"
    )
    print(f"Token divergence: {token_div_all:.4f}")
    print(f"KL divergence: {np.mean(all_kls):.4f}")
    print(f"MSE vs GT - baseline: {np.mean(mse_gt_baseline):.6f}, ablated: {np.mean(mse_gt_ablated):.6f}")

    out_path = os.path.join(RESULTS_DIR, "action_trajectory_analysis.json")
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"Results saved to {out_path}")


if __name__ == "__main__":
    main()
