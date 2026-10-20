"""Counterfactual instruction experiment: measures how different instruction perturbations
affect action outputs, validating that L1 instruction-dominant heads perform
instruction-specific routing rather than generic text processing.

Conditions: correct (baseline), wrong, empty, shuffled, paraphrased
Input: LIBERO-Goal demos (3 tasks x 10 demos x 50 timesteps)
Output: /root/autodl-tmp/vla-ssd/results/counterfactual_{condition}.json
"""

import argparse
import gc
import glob
import json
import os
import random
import sys
import time

sys.path.insert(0, "/root/autodl-tmp/LIBERO")

os.environ["MUJOCO_GL"] = "egl"
os.environ["HDF5_USE_FILE_LOCKING"] = "FALSE"

import h5py
import numpy as np
import torch
import torch.multiprocessing as mp
import torch.nn.functional as F
from PIL import Image
from scipy import stats

SEED = 42
MODEL_PATH = "/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b"
UNNORM_KEY = "bridge_orig"
DATA_DIR = "/root/autodl-tmp/vla-ssd/data/libero/libero_goal"
RESULTS_DIR = "/root/autodl-tmp/vla-ssd/results"
N_TASKS = 3
N_DEMOS = 10
N_TIMESTEPS = 50
DIM_NAMES = ["dx", "dy", "dz", "rx", "ry", "rz", "gripper"]

TASK_INSTRUCTIONS = {
    "open_the_middle_drawer_of_the_cabinet": {
        "correct": "open the middle drawer of the cabinet",
        "paraphrased": "pull open the center drawer on the cabinet",
        "wrong": "push the plate to the front of the stove",
    },
    "open_the_top_drawer_and_put_the_bowl_inside": {
        "correct": "open the top drawer and put the bowl inside",
        "paraphrased": "open the upper drawer and place the bowl in it",
        "wrong": "open the middle drawer of the cabinet",
    },
    "push_the_plate_to_the_front_of_the_stove": {
        "correct": "push the plate to the front of the stove",
        "paraphrased": "slide the plate toward the front of the stove",
        "wrong": "open the top drawer and put the bowl inside",
    },
}


def load_model(device):
    from transformers import AutoModelForVision2Seq, AutoProcessor

    processor = AutoProcessor.from_pretrained(MODEL_PATH, trust_remote_code=True)
    model = AutoModelForVision2Seq.from_pretrained(
        MODEL_PATH,
        torch_dtype=torch.bfloat16,
        trust_remote_code=True,
        low_cpu_mem_usage=True,
        device_map=device,
    ).eval()
    return model, processor


def predict_action_with_logits(model, input_ids, pixel_values, unnorm_key):
    """Manual autoregressive generation (bypasses DynamicCache bug in transformers 4.40.1)."""
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

    logits_tensor = torch.cat(all_logits, dim=0)
    return action, predicted_action_token_ids, logits_tensor


def compute_kl_divergence(logits_p, logits_q):
    log_p = F.log_softmax(logits_p, dim=-1)
    log_q = F.log_softmax(logits_q, dim=-1)
    p = F.softmax(logits_p, dim=-1)
    kl = (p * (log_p - log_q)).sum(dim=-1)
    return kl.numpy()


def get_shuffled_instruction(instruction, rng):
    words = instruction.split()
    rng.shuffle(words)
    return " ".join(words)


def get_task_files():
    hdf5_files = sorted(glob.glob(os.path.join(DATA_DIR, "*.hdf5")))
    return hdf5_files[:N_TASKS]


def get_language_instruction(hdf5_path):
    with h5py.File(hdf5_path, "r") as f:
        info = json.loads(f["data"].attrs["problem_info"])
    return info["language_instruction"]


def compute_condition_metrics(c_actions, cf_actions, c_ids, cf_ids, kl_arrays):
    c = np.array(c_actions)
    cf = np.array(cf_actions)
    c_tok = np.array(c_ids)
    cf_tok = np.array(cf_ids)
    kls = np.array(kl_arrays)

    paired_mse = np.mean((c - cf) ** 2, axis=1)
    t_res = stats.ttest_1samp(paired_mse, 0)
    cohens_d = np.mean(paired_mse) / (np.std(paired_mse, ddof=1) + 1e-12)
    per_dim_shift = np.abs(c - cf)
    token_div = np.mean(c_tok != cf_tok)

    try:
        wilcoxon_res = stats.wilcoxon(paired_mse)
        wilcoxon_p = float(wilcoxon_res.pvalue)
    except Exception:
        wilcoxon_p = None

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
            "dim_names": DIM_NAMES,
        },
        "token_divergence_rate": float(token_div),
        "kl_divergence": {
            "mean": float(np.mean(kls)),
            "std": float(np.std(kls)),
            "per_token_position": [float(x) for x in np.mean(kls, axis=0)] if kls.ndim > 1 else [],
        },
        "wilcoxon_p": wilcoxon_p,
        "n_samples": int(len(c)),
    }


def gpu_worker(gpu_id, conditions, dry_run):
    random.seed(SEED)
    np.random.seed(SEED)
    torch.manual_seed(SEED)
    rng = random.Random(SEED)

    device = f"cuda:{gpu_id}"
    n_tasks = 1 if dry_run else N_TASKS
    n_demos = 1 if dry_run else N_DEMOS
    n_timesteps = 2 if dry_run else N_TIMESTEPS

    os.makedirs(RESULTS_DIR, exist_ok=True)

    print(f"[GPU {gpu_id}] Loading model on {device}...")
    model, processor = load_model(device)
    print(f"[GPU {gpu_id}] Model loaded. Conditions: {conditions}")

    task_files = get_task_files()[:n_tasks]

    correct_global = {"actions": [], "token_ids": []}
    cond_global = {c: {"actions": [], "ids": [], "kls": []} for c in conditions}
    correct_global_ids = []
    per_task_correct = {}
    per_task_cond = {c: {} for c in conditions}

    total_passes = 0
    t_start = time.time()

    for task_idx, hdf5_path in enumerate(task_files):
        task_name = os.path.basename(hdf5_path).replace("_demo.hdf5", "")
        correct_instruction = get_language_instruction(hdf5_path)
        task_cfg = TASK_INSTRUCTIONS[task_name]

        print(f"\n[GPU {gpu_id}] Task {task_idx}: {task_name}")
        print(f"  correct: {correct_instruction}")

        cf_instructions = {}
        for cond in conditions:
            if cond == "wrong":
                cf_instructions[cond] = task_cfg["wrong"]
            elif cond == "empty":
                cf_instructions[cond] = ""
            elif cond == "shuffled":
                cf_instructions[cond] = get_shuffled_instruction(correct_instruction, rng)
            elif cond == "paraphrased":
                cf_instructions[cond] = task_cfg["paraphrased"]
            print(f"  {cond}: '{cf_instructions[cond]}'")

        correct_prompt = f"In: What action should the robot take to {correct_instruction}?\nOut:"
        cf_prompts = {}
        for cond in conditions:
            inst = cf_instructions[cond]
            if inst == "":
                cf_prompts[cond] = "In: What action should the robot take to ?\nOut:"
            else:
                cf_prompts[cond] = f"In: What action should the robot take to {inst}?\nOut:"

        task_c_actions, task_c_ids = [], []
        task_cf = {c: {"actions": [], "ids": [], "kls": []} for c in conditions}

        with h5py.File(hdf5_path, "r") as f:
            for demo_idx in range(n_demos):
                demo_key = f"data/demo_{demo_idx}"
                actions_data = f[f"{demo_key}/actions"][:]
                images_data = f[f"{demo_key}/obs/agentview_rgb"][:]
                n_steps = min(n_timesteps, len(actions_data))

                for step_idx in range(n_steps):
                    img = Image.fromarray(images_data[step_idx])

                    inputs_c = processor(correct_prompt, img).to(device, dtype=torch.bfloat16)
                    c_action, c_ids, c_logits = predict_action_with_logits(
                        model, inputs_c["input_ids"], inputs_c["pixel_values"], UNNORM_KEY
                    )
                    task_c_actions.append(c_action)
                    task_c_ids.append(c_ids)
                    total_passes += 1

                    for cond in conditions:
                        inputs_cf = processor(cf_prompts[cond], img).to(
                            device, dtype=torch.bfloat16
                        )
                        cf_action, cf_ids, cf_logits = predict_action_with_logits(
                            model, inputs_cf["input_ids"], inputs_cf["pixel_values"], UNNORM_KEY
                        )
                        kl = compute_kl_divergence(c_logits, cf_logits)
                        task_cf[cond]["actions"].append(cf_action)
                        task_cf[cond]["ids"].append(cf_ids)
                        task_cf[cond]["kls"].append(kl)
                        total_passes += 1

                    if total_passes % 100 == 0:
                        elapsed = time.time() - t_start
                        rate = total_passes / elapsed
                        remaining = (n_tasks * n_demos * n_timesteps * (1 + len(conditions)) - total_passes)
                        eta = remaining / rate if rate > 0 else 0
                        print(
                            f"  [GPU {gpu_id}] {total_passes} passes, "
                            f"{rate:.1f} pass/s, ETA {eta:.0f}s"
                        )

        for cond in conditions:
            metrics = compute_condition_metrics(
                task_c_actions, task_cf[cond]["actions"],
                task_c_ids, task_cf[cond]["ids"],
                task_cf[cond]["kls"],
            )
            metrics["instruction_correct"] = correct_instruction
            metrics["instruction_counterfactual"] = cf_instructions[cond]
            per_task_cond[cond][task_name] = metrics
            print(
                f"  [GPU {gpu_id}] {cond}: MSE={metrics['paired_mse']['mean']:.6f} "
                f"d={metrics['paired_mse']['cohens_d']:.3f} "
                f"token_div={metrics['token_divergence_rate']:.4f} "
                f"KL={metrics['kl_divergence']['mean']:.4f}"
            )

        correct_global["actions"].extend(task_c_actions)
        correct_global["token_ids"].extend(task_c_ids)
        correct_global_ids.extend(task_c_ids)
        per_task_correct[task_name] = {
            "instruction": correct_instruction,
            "n_samples": len(task_c_actions),
            "action_mean": [float(x) for x in np.mean(task_c_actions, axis=0)],
            "action_std": [float(x) for x in np.std(task_c_actions, axis=0)],
            "dim_names": DIM_NAMES,
        }
        for cond in conditions:
            cond_global[cond]["actions"].extend(task_cf[cond]["actions"])
            cond_global[cond]["ids"].extend(task_cf[cond]["ids"])
            cond_global[cond]["kls"].extend(task_cf[cond]["kls"])

        gc.collect()
        torch.cuda.empty_cache()

    for cond in conditions:
        global_metrics = compute_condition_metrics(
            correct_global["actions"], cond_global[cond]["actions"],
            correct_global["token_ids"], cond_global[cond]["ids"],
            cond_global[cond]["kls"],
        )

        output = {
            "config": {
                "condition": cond,
                "n_tasks": n_tasks,
                "n_demos_per_task": n_demos,
                "n_timesteps_per_demo": n_timesteps,
                "total_forward_passes": total_passes,
                "model": "openvla-7b",
                "unnorm_key": UNNORM_KEY,
                "gpu": gpu_id,
                "seed": SEED,
            },
            "global_metrics": global_metrics,
            "per_task": per_task_cond[cond],
        }

        out_path = os.path.join(RESULTS_DIR, f"counterfactual_{cond}.json")
        with open(out_path, "w") as fout:
            json.dump(output, fout, indent=2)
        print(f"[GPU {gpu_id}] Saved {out_path}")

    if gpu_id == 0:
        all_actions = np.array(correct_global["actions"])
        correct_output = {
            "config": {
                "condition": "correct",
                "n_tasks": n_tasks,
                "n_demos_per_task": n_demos,
                "n_timesteps_per_demo": n_timesteps,
                "model": "openvla-7b",
                "unnorm_key": UNNORM_KEY,
                "seed": SEED,
            },
            "global": {
                "n_samples": len(all_actions),
                "action_mean": [float(x) for x in np.mean(all_actions, axis=0)],
                "action_std": [float(x) for x in np.std(all_actions, axis=0)],
                "dim_names": DIM_NAMES,
            },
            "per_task": per_task_correct,
        }
        out_path = os.path.join(RESULTS_DIR, "counterfactual_correct.json")
        with open(out_path, "w") as fout:
            json.dump(correct_output, fout, indent=2)
        print(f"[GPU {gpu_id}] Saved {out_path}")

    elapsed = time.time() - t_start
    print(f"\n[GPU {gpu_id}] Done. {total_passes} passes in {elapsed:.0f}s")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    os.makedirs(RESULTS_DIR, exist_ok=True)
    t_start = time.time()

    gpu0_conditions = ["wrong", "empty"]
    gpu1_conditions = ["shuffled", "paraphrased"]

    p0 = mp.Process(target=gpu_worker, args=(0, gpu0_conditions, args.dry_run))
    p1 = mp.Process(target=gpu_worker, args=(1, gpu1_conditions, args.dry_run))

    p0.start()
    p1.start()
    p0.join()
    p1.join()

    if p0.exitcode != 0 or p1.exitcode != 0:
        print(f"ERROR: GPU 0 exit={p0.exitcode}, GPU 1 exit={p1.exitcode}")
        sys.exit(1)

    print("\nGenerating combined summary...")
    combined = {
        "config": {
            "experiment": "counterfactual_instruction",
            "conditions": ["wrong", "empty", "shuffled", "paraphrased"],
            "n_tasks": 1 if args.dry_run else N_TASKS,
            "n_demos_per_task": 1 if args.dry_run else N_DEMOS,
            "n_timesteps_per_demo": 2 if args.dry_run else N_TIMESTEPS,
            "model": "openvla-7b",
            "unnorm_key": UNNORM_KEY,
            "seed": SEED,
        },
        "conditions": {},
    }

    for cond in ["wrong", "empty", "shuffled", "paraphrased"]:
        cond_path = os.path.join(RESULTS_DIR, f"counterfactual_{cond}.json")
        if os.path.exists(cond_path):
            with open(cond_path, "r") as f:
                data = json.load(f)
            combined["conditions"][cond] = {
                "global_metrics": data["global_metrics"],
                "per_task": data["per_task"],
            }

    ranking = sorted(
        [(k, v["global_metrics"]) for k, v in combined["conditions"].items()],
        key=lambda x: x[1]["paired_mse"]["cohens_d"],
        reverse=True,
    )
    combined["ranking_by_cohens_d"] = [
        {
            "condition": k,
            "cohens_d": v["paired_mse"]["cohens_d"],
            "paired_mse_mean": v["paired_mse"]["mean"],
            "token_divergence_rate": v["token_divergence_rate"],
            "kl_divergence_mean": v["kl_divergence"]["mean"],
        }
        for k, v in ranking
    ]

    out_path = os.path.join(RESULTS_DIR, "counterfactual_combined.json")
    with open(out_path, "w") as f:
        json.dump(combined, f, indent=2)

    elapsed = time.time() - t_start
    print(f"\nTotal time: {elapsed:.0f}s")
    print(f"Combined results: {out_path}")

    print(f"\n{'='*60}")
    print("COUNTERFACTUAL INSTRUCTION EXPERIMENT SUMMARY")
    print(f"{'='*60}")
    for k, v in ranking:
        print(
            f"  {k:12s}: MSE={v['paired_mse']['mean']:.6f} "
            f"d={v['paired_mse']['cohens_d']:.3f} "
            f"token_div={v['token_divergence_rate']:.4f} "
            f"KL={v['kl_divergence']['mean']:.4f}"
        )


if __name__ == "__main__":
    mp.set_start_method("spawn")
    main()
