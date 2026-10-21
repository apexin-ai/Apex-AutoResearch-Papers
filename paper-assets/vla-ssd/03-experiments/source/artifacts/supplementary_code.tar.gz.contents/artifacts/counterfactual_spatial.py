"""Counterfactual instruction experiment on all 10 LIBERO-Spatial tasks.

Replicates the LIBERO-Goal counterfactual analysis on LIBERO-Spatial.
Tests spatial language grounding: all tasks share the same object/action
but differ in spatial reference only.
Single GPU, all 4 conditions (wrong/empty/shuffled/paraphrased).
Output: /root/autodl-tmp/vla-ssd/results/counterfactual_spatial/
"""

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
import torch.nn.functional as F
from PIL import Image
from scipy import stats

SEED = 42
MODEL_PATH = "/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b"
UNNORM_KEY = "bridge_orig"
DATA_DIR = "/root/autodl-tmp/vla-ssd/data/libero/libero_spatial"
RESULTS_DIR = "/root/autodl-tmp/vla-ssd/results/counterfactual_spatial"
N_TASKS = 10
N_DEMOS = 10
N_TIMESTEPS = 50
DIM_NAMES = ["dx", "dy", "dz", "rx", "ry", "rz", "gripper"]
CONDITIONS = ["wrong", "empty", "shuffled", "paraphrased"]

# For LIBERO-Spatial, "wrong" uses another spatial task's instruction
# (same object/action, different spatial reference) to test spatial grounding.
TASK_INSTRUCTIONS = {
    "pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate": {
        "correct": "pick up the black bowl between the plate and the ramekin and place it on the plate",
        "paraphrased": "grab the black bowl situated between the plate and ramekin and put it on the plate",
        "wrong": "pick up the black bowl on the stove and place it on the plate",
    },
    "pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate": {
        "correct": "pick up the black bowl from table center and place it on the plate",
        "paraphrased": "grab the black bowl from the middle of the table and put it on the plate",
        "wrong": "pick up the black bowl on the wooden cabinet and place it on the plate",
    },
    "pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate": {
        "correct": "pick up the black bowl in the top drawer of the wooden cabinet and place it on the plate",
        "paraphrased": "retrieve the black bowl from the upper drawer of the wooden cabinet and put it on the plate",
        "wrong": "pick up the black bowl on the ramekin and place it on the plate",
    },
    "pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate": {
        "correct": "pick up the black bowl next to the cookie box and place it on the plate",
        "paraphrased": "grab the black bowl beside the cookie box and put it on the plate",
        "wrong": "pick up the black bowl between the plate and the ramekin and place it on the plate",
    },
    "pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate": {
        "correct": "pick up the black bowl next to the plate and place it on the plate",
        "paraphrased": "grab the black bowl beside the plate and put it on the plate",
        "wrong": "pick up the black bowl from table center and place it on the plate",
    },
    "pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate": {
        "correct": "pick up the black bowl next to the ramekin and place it on the plate",
        "paraphrased": "grab the black bowl beside the ramekin and put it on the plate",
        "wrong": "pick up the black bowl on the cookie box and place it on the plate",
    },
    "pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate": {
        "correct": "pick up the black bowl on the cookie box and place it on the plate",
        "paraphrased": "grab the black bowl sitting on the cookie box and put it on the plate",
        "wrong": "pick up the black bowl next to the ramekin and place it on the plate",
    },
    "pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate": {
        "correct": "pick up the black bowl on the ramekin and place it on the plate",
        "paraphrased": "grab the black bowl sitting on the ramekin and put it on the plate",
        "wrong": "pick up the black bowl in the top drawer of the wooden cabinet and place it on the plate",
    },
    "pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate": {
        "correct": "pick up the black bowl on the stove and place it on the plate",
        "paraphrased": "grab the black bowl sitting on the stove and put it on the plate",
        "wrong": "pick up the black bowl next to the plate and place it on the plate",
    },
    "pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate": {
        "correct": "pick up the black bowl on the wooden cabinet and place it on the plate",
        "paraphrased": "grab the black bowl sitting on the wooden cabinet and put it on the plate",
        "wrong": "pick up the black bowl next to the cookie box and place it on the plate",
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

    ci_95 = stats.t.interval(
        0.95, df=len(paired_mse) - 1,
        loc=cohens_d,
        scale=np.std(paired_mse, ddof=1) / (np.mean(paired_mse) + 1e-12) * cohens_d / np.sqrt(len(paired_mse))
    ) if len(paired_mse) > 1 else (cohens_d, cohens_d)

    return {
        "paired_mse": {
            "mean": float(np.mean(paired_mse)),
            "std": float(np.std(paired_mse)),
            "t_stat": float(t_res.statistic),
            "p_value": float(t_res.pvalue),
            "cohens_d": float(cohens_d),
            "ci_95": [float(ci_95[0]), float(ci_95[1])],
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


def main():
    random.seed(SEED)
    np.random.seed(SEED)
    torch.manual_seed(SEED)
    rng = random.Random(SEED)

    device = "cuda:0"
    os.makedirs(RESULTS_DIR, exist_ok=True)

    print(f"Loading model on {device}...")
    model, processor = load_model(device)
    print("Model loaded.")

    task_files = get_task_files()
    print(f"Found {len(task_files)} tasks")

    cond_global = {c: {"c_actions": [], "cf_actions": [], "c_ids": [], "cf_ids": [], "kls": []}
                   for c in CONDITIONS}
    per_task_cond = {c: {} for c in CONDITIONS}
    correct_global = {"actions": [], "token_ids": []}
    per_task_correct = {}

    total_passes = 0
    t_start = time.time()
    total_expected = N_TASKS * N_DEMOS * N_TIMESTEPS * (1 + len(CONDITIONS))

    for task_idx, hdf5_path in enumerate(task_files):
        task_name = os.path.basename(hdf5_path).replace("_demo.hdf5", "")
        correct_instruction = get_language_instruction(hdf5_path)
        task_cfg = TASK_INSTRUCTIONS[task_name]

        print(f"\nTask {task_idx}/{N_TASKS}: {task_name}")
        print(f"  correct: {correct_instruction}")

        cf_instructions = {}
        for cond in CONDITIONS:
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
        for cond in CONDITIONS:
            inst = cf_instructions[cond]
            if inst == "":
                cf_prompts[cond] = "In: What action should the robot take to ?\nOut:"
            else:
                cf_prompts[cond] = f"In: What action should the robot take to {inst}?\nOut:"

        task_c_actions, task_c_ids = [], []
        task_cf = {c: {"actions": [], "ids": [], "kls": []} for c in CONDITIONS}

        with h5py.File(hdf5_path, "r") as f:
            for demo_idx in range(N_DEMOS):
                demo_key = f"data/demo_{demo_idx}"
                actions_data = f[f"{demo_key}/actions"][:]
                images_data = f[f"{demo_key}/obs/agentview_rgb"][:]
                n_steps = min(N_TIMESTEPS, len(actions_data))

                for step_idx in range(n_steps):
                    img = Image.fromarray(images_data[step_idx])

                    inputs_c = processor(correct_prompt, img).to(device, dtype=torch.bfloat16)
                    c_action, c_ids, c_logits = predict_action_with_logits(
                        model, inputs_c["input_ids"], inputs_c["pixel_values"], UNNORM_KEY
                    )
                    task_c_actions.append(c_action)
                    task_c_ids.append(c_ids)
                    total_passes += 1

                    for cond in CONDITIONS:
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

                    if total_passes % 500 == 0:
                        elapsed = time.time() - t_start
                        rate = total_passes / elapsed
                        remaining = total_expected - total_passes
                        eta = remaining / rate if rate > 0 else 0
                        print(
                            f"  {total_passes}/{total_expected} passes, "
                            f"{rate:.1f} pass/s, ETA {eta:.0f}s ({eta/60:.1f}min)"
                        )

        for cond in CONDITIONS:
            metrics = compute_condition_metrics(
                task_c_actions, task_cf[cond]["actions"],
                task_c_ids, task_cf[cond]["ids"],
                task_cf[cond]["kls"],
            )
            metrics["instruction_correct"] = correct_instruction
            metrics["instruction_counterfactual"] = cf_instructions[cond]
            per_task_cond[cond][task_name] = metrics
            print(
                f"  {cond}: MSE={metrics['paired_mse']['mean']:.6f} "
                f"d={metrics['paired_mse']['cohens_d']:.3f} "
                f"tok_div={metrics['token_divergence_rate']:.4f} "
                f"KL={metrics['kl_divergence']['mean']:.4f}"
            )

        correct_global["actions"].extend(task_c_actions)
        correct_global["token_ids"].extend(task_c_ids)
        for cond in CONDITIONS:
            cond_global[cond]["c_actions"].extend(task_c_actions)
            cond_global[cond]["cf_actions"].extend(task_cf[cond]["actions"])
            cond_global[cond]["c_ids"].extend(task_c_ids)
            cond_global[cond]["cf_ids"].extend(task_cf[cond]["ids"])
            cond_global[cond]["kls"].extend(task_cf[cond]["kls"])

        tc_arr = np.array(task_c_actions)
        per_task_correct[task_name] = {
            "n_samples": len(task_c_actions),
            "action_mean": [float(x) for x in np.mean(tc_arr, axis=0)],
            "action_std": [float(x) for x in np.std(tc_arr, axis=0)],
        }

        gc.collect()
        torch.cuda.empty_cache()

    for cond in CONDITIONS:
        global_metrics = compute_condition_metrics(
            cond_global[cond]["c_actions"], cond_global[cond]["cf_actions"],
            cond_global[cond]["c_ids"], cond_global[cond]["cf_ids"],
            cond_global[cond]["kls"],
        )

        data = {
            "config": {
                "experiment": "counterfactual_instruction_spatial",
                "condition": cond,
                "n_tasks": N_TASKS,
                "n_demos_per_task": N_DEMOS,
                "n_timesteps_per_demo": N_TIMESTEPS,
                "model": "openvla-7b",
                "unnorm_key": UNNORM_KEY,
                "seed": SEED,
                "suite": "libero_spatial",
            },
            "global_metrics": global_metrics,
            "per_task": per_task_cond[cond],
        }

        out_path = os.path.join(RESULTS_DIR, f"counterfactual_{cond}.json")
        with open(out_path, "w") as fp:
            json.dump(data, fp, indent=2)
        print(f"\nSaved {cond} -> {out_path}")

    correct_data = {
        "config": {
            "experiment": "counterfactual_instruction_spatial",
            "condition": "correct",
            "n_tasks": N_TASKS,
            "n_demos_per_task": N_DEMOS,
            "n_timesteps_per_demo": N_TIMESTEPS,
            "model": "openvla-7b",
            "unnorm_key": UNNORM_KEY,
            "seed": SEED,
            "suite": "libero_spatial",
        },
        "per_task": per_task_correct,
        "global": {
            "n_samples": len(correct_global["actions"]),
            "action_mean": [float(x) for x in np.mean(correct_global["actions"], axis=0)],
            "action_std": [float(x) for x in np.std(correct_global["actions"], axis=0)],
        },
    }
    with open(os.path.join(RESULTS_DIR, "counterfactual_correct.json"), "w") as fp:
        json.dump(correct_data, fp, indent=2)

    # Combined summary
    combined = {
        "config": {
            "experiment": "counterfactual_instruction_spatial",
            "conditions": CONDITIONS,
            "n_tasks": N_TASKS,
            "n_demos_per_task": N_DEMOS,
            "n_timesteps_per_demo": N_TIMESTEPS,
            "model": "openvla-7b",
            "unnorm_key": UNNORM_KEY,
            "seed": SEED,
            "suite": "libero_spatial",
            "task_names": [os.path.basename(p).replace("_demo.hdf5", "") for p in task_files],
            "note": "wrong instructions use other spatial tasks (same object/action, different spatial reference)",
        },
        "conditions": {},
    }

    for cond in CONDITIONS:
        cond_path = os.path.join(RESULTS_DIR, f"counterfactual_{cond}.json")
        with open(cond_path) as fp:
            data = json.load(fp)

        task_ds = [v["paired_mse"]["cohens_d"] for v in data["per_task"].values()]
        task_mses = [v["paired_mse"]["mean"] for v in data["per_task"].values()]
        task_tok_divs = [v["token_divergence_rate"] for v in data["per_task"].values()]
        task_kls = [v["kl_divergence"]["mean"] for v in data["per_task"].values()]

        cross_task_variance = {
            "cohens_d": {
                "values": task_ds,
                "mean": float(np.mean(task_ds)),
                "std": float(np.std(task_ds, ddof=1)),
                "min": float(np.min(task_ds)),
                "max": float(np.max(task_ds)),
                "cv": float(np.std(task_ds, ddof=1) / (np.mean(task_ds) + 1e-12)),
            },
            "paired_mse": {
                "values": task_mses,
                "mean": float(np.mean(task_mses)),
                "std": float(np.std(task_mses, ddof=1)),
                "cv": float(np.std(task_mses, ddof=1) / (np.mean(task_mses) + 1e-12)),
            },
            "token_divergence_rate": {
                "values": task_tok_divs,
                "mean": float(np.mean(task_tok_divs)),
                "std": float(np.std(task_tok_divs, ddof=1)),
            },
            "kl_divergence": {
                "values": task_kls,
                "mean": float(np.mean(task_kls)),
                "std": float(np.std(task_kls, ddof=1)),
            },
        }

        combined["conditions"][cond] = {
            "global_metrics": data["global_metrics"],
            "per_task": data["per_task"],
            "cross_task_variance": cross_task_variance,
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

    combined["cross_task_summary"] = {}
    for cond in CONDITIONS:
        ctv = combined["conditions"][cond]["cross_task_variance"]
        combined["cross_task_summary"][cond] = {
            "cohens_d_mean_std": f"{ctv['cohens_d']['mean']:.3f} +/- {ctv['cohens_d']['std']:.3f}",
            "cohens_d_range": f"[{ctv['cohens_d']['min']:.3f}, {ctv['cohens_d']['max']:.3f}]",
            "cohens_d_cv": f"{ctv['cohens_d']['cv']:.3f}",
            "mse_mean_std": f"{ctv['paired_mse']['mean']:.6f} +/- {ctv['paired_mse']['std']:.6f}",
        }

    out_path = os.path.join(RESULTS_DIR, "counterfactual_spatial_combined.json")
    with open(out_path, "w") as f:
        json.dump(combined, f, indent=2)

    elapsed = time.time() - t_start
    print(f"\nTotal time: {elapsed:.0f}s ({elapsed/60:.1f}min)")
    print(f"Combined results: {out_path}")

    print(f"\n{'='*70}")
    print("COUNTERFACTUAL INSTRUCTION EXPERIMENT - LIBERO-SPATIAL SUMMARY")
    print(f"{'='*70}")
    for k, v in ranking:
        ctv = combined["conditions"][k]["cross_task_variance"]["cohens_d"]
        print(
            f"  {k:12s}: MSE={v['paired_mse']['mean']:.6f} "
            f"d={v['paired_mse']['cohens_d']:.3f} "
            f"(cross-task: {ctv['mean']:.3f}+/-{ctv['std']:.3f}) "
            f"tok_div={v['token_divergence_rate']:.4f} "
            f"KL={v['kl_divergence']['mean']:.4f}"
        )

    print(f"\n{'='*70}")
    print("CROSS-TASK VARIANCE (Cohen's d per task)")
    print(f"{'='*70}")
    for cond in CONDITIONS:
        ctv = combined["conditions"][cond]["cross_task_variance"]["cohens_d"]
        vals = ctv["values"]
        task_names = combined["config"]["task_names"]
        print(f"\n  {cond}:")
        for tn, dv in zip(task_names, vals):
            print(f"    {tn:70s}: d={dv:.3f}")
        print(f"    {'mean +/- std':70s}: {ctv['mean']:.3f} +/- {ctv['std']:.3f} (CV={ctv['cv']:.3f})")


if __name__ == "__main__":
    main()
