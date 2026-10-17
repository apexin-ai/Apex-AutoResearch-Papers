"""Mistral-7B-v0.3 3-seed downstream CI evaluation.

Input:
  - mistral_multi_seed_profiles_s{0,1,2}.json  (per-seed distortion profiles)
  - Model: /root/autodl-tmp/models/Mistral-7B-v0.3
Output:
  - artifacts/mistral_3seed_downstream_ci_results.json
    (per-seed per-task scores, mean +/- std, delta table)

Evaluates 4 downstream tasks under bf16 / uniform-4bit / MCKP-k8 (x3 seeds).
"""
import os
os.environ["HF_HOME"] = "/root/autodl-tmp/.hf_cache"
os.environ["HF_HUB_OFFLINE"] = "1"
os.environ["HF_DATASETS_OFFLINE"] = "1"
os.environ["TRANSFORMERS_OFFLINE"] = "1"

import argparse
import gc
import json
import time
import numpy as np
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

import sys
sys.path.insert(0, "/root/ratekv")
from solver import solve_mckp_constrained, uniform_quantization_baseline, enforce_monotonicity
from eval_ppl import patch_attention, restore_attention

import lm_eval
from lm_eval.models.huggingface import HFLM

MODEL_PATH = "/root/autodl-tmp/models/Mistral-7B-v0.3"
BUDGET = 0.25
MAX_2BIT = 2
SEEDS = [0, 1, 2]
TASKS = ["arc_challenge", "hellaswag", "winogrande", "piqa"]
NUM_FEWSHOT = 0
OUTPUT = "/root/ratekv/artifacts/mistral_3seed_downstream_ci_results.json"


def load_seed_profiles(seed):
    path = f"/root/ratekv/mistral_multi_seed_profiles_s{seed}.json"
    with open(path) as f:
        raw = json.load(f)
    profiles = raw["profiles"] if "profiles" in raw else raw
    return enforce_monotonicity(profiles)


def run_eval(model, tokenizer, device, task_list, num_fewshot):
    lm = HFLM(pretrained=model, tokenizer=tokenizer, device=device, batch_size=8)
    results = lm_eval.simple_evaluate(
        model=lm,
        tasks=task_list,
        num_fewshot=num_fewshot,
        device=device,
    )
    scores = {}
    for task_name, task_result in results["results"].items():
        acc_key = "acc,none" if "acc,none" in task_result else "acc_norm,none"
        scores[task_name] = round(task_result.get(acc_key, 0.0), 4)
    return scores


def main():
    parser = argparse.ArgumentParser(description="Mistral-7B-v0.3 3-seed downstream CI")
    parser.add_argument("--gpu", type=str, default="cuda:0")
    args = parser.parse_args()

    device = args.gpu
    t_start = time.time()

    # Load profiles and compute allocations
    seed_profiles = {}
    seed_allocations = {}
    for seed in SEEDS:
        profiles = load_seed_profiles(seed)
        seed_profiles[seed] = profiles
        mckp = solve_mckp_constrained(
            profiles, BUDGET, mode="quant_only",
            max_2bit=MAX_2BIT, l0_exclude_2bit=True
        )
        seed_allocations[seed] = mckp
        print(f"Seed {seed}: bits={mckp['bit_distribution']}, mem={mckp['actual_memory_ratio']:.4f}", flush=True)

    # Uniform baseline (use seed 0 profiles, result is deterministic)
    uniform = uniform_quantization_baseline(seed_profiles[0], bits=4)

    # Load model
    print(f"\nLoading model to {device}...", flush=True)
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_PATH, torch_dtype=torch.bfloat16, attn_implementation="eager"
    )
    model = model.to(device)
    model.eval()

    result = {
        "model": "Mistral-7B-v0.3",
        "tasks": TASKS,
        "num_fewshot": NUM_FEWSHOT,
        "budget": BUDGET,
        "max_2bit": MAX_2BIT,
        "seeds": SEEDS,
    }

    # 1) Baseline (bf16)
    print("\n[1] Baseline (bf16)...", flush=True)
    result["baseline"] = run_eval(model, tokenizer, device, TASKS, NUM_FEWSHOT)
    print(f"  Baseline: {result['baseline']}", flush=True)

    # 2) Uniform 4-bit (once)
    print("\n[2] Uniform 4-bit...", flush=True)
    orig = patch_attention(model, uniform["allocation"])
    result["uniform_4bit"] = run_eval(model, tokenizer, device, TASKS, NUM_FEWSHOT)
    restore_attention(model, orig)
    print(f"  Uniform: {result['uniform_4bit']}", flush=True)

    # 3) Per-seed MCKP
    result["seed_mckp"] = {}
    for i, seed in enumerate(SEEDS):
        print(f"\n[3.{i}] MCKP seed {seed} (k={MAX_2BIT})...", flush=True)
        orig = patch_attention(model, seed_allocations[seed]["allocation"])
        scores = run_eval(model, tokenizer, device, TASKS, NUM_FEWSHOT)
        restore_attention(model, orig)
        result["seed_mckp"][str(seed)] = scores
        print(f"  Seed {seed}: {scores}", flush=True)

    # Compute mean +/- std per task
    summary = {}
    for task in TASKS:
        vals = [result["seed_mckp"][str(s)][task] for s in SEEDS]
        summary[task] = {
            "values": vals,
            "mean": round(float(np.mean(vals)), 4),
            "std": round(float(np.std(vals)), 4),
        }
    result["summary"] = summary
    result["elapsed_seconds"] = round(time.time() - t_start, 1)

    # Print table
    print(f"\n{'='*80}")
    print(f"{'Task':<20} {'BF16':>8} {'Uni4':>8} {'MCKP mean':>10} {'MCKP std':>10} {'D(M-U)':>10}")
    print("-" * 80)
    for task in TASKS:
        bl = result["baseline"].get(task, 0)
        uni = result["uniform_4bit"].get(task, 0)
        m = summary[task]["mean"]
        s = summary[task]["std"]
        delta = m - uni
        print(f"{task:<20} {bl:>8.4f} {uni:>8.4f} {m:>10.4f} {s:>10.4f} {delta:>+10.4f}")
    print(f"{'='*80}")

    # Save
    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    with open(OUTPUT, "w") as f:
        json.dump(result, f, indent=2)
    print(f"\nSaved to {OUTPUT}", flush=True)

    del model, tokenizer
    gc.collect()
    torch.cuda.empty_cache()


if __name__ == "__main__":
    main()
