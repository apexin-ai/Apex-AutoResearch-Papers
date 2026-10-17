"""W3: downstream task evaluation under constrained quantization.

Evaluates Llama-3.1-8B and Yi-1.5-9B on 0-shot downstream tasks
(arc_easy, arc_challenge, hellaswag, winogrande, piqa) under three conditions:
1. Baseline (bf16, no quantization)
2. Uniform 4-bit quantization
3. Constrained MCKP allocation

Uses lm-evaluation-harness Python API with monkey-patched attention.
"""
import os
os.environ["HF_HOME"] = "/root/autodl-tmp/.hf_cache"

import argparse
import gc
import json
import time
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

from solver import solve_mckp_constrained, uniform_quantization_baseline, enforce_monotonicity
from eval_ppl import patch_attention, restore_attention

import lm_eval
from lm_eval.models.huggingface import HFLM


TASKS = ["arc_easy", "arc_challenge", "hellaswag", "winogrande", "piqa"]
NUM_FEWSHOT = 0
BUDGET = 0.25
MAX_2BIT = 2
DEVICE = "cuda:0"


MODELS = {
    "llama": {
        "name": "Llama-3.1-8B",
        "path": "/root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-8B",
        "hires_2bit": "llama_hires_bf16_2bitonly_profiles.json",
        "standard": "llama_profiling_results.json",
    },
    "yi": {
        "name": "Yi-1.5-9B",
        "path": "/root/autodl-tmp/.hf_cache/01ai/Yi-1___5-9B",
        "hires_2bit": "yi15_hires_bf16_2bitonly_profiles.json",
        "standard": "yi15_profiling_results.json",
    },
}


def load_merged_profiles(cfg):
    base = "/root/ratekv/"
    with open(os.path.join(base, cfg["hires_2bit"])) as f:
        hires_raw = json.load(f)
    hires = hires_raw.get("profiles", hires_raw)

    with open(os.path.join(base, cfg["standard"])) as f:
        std_raw = json.load(f)
    std = std_raw.get("profiles", std_raw)

    merged = {}
    for l_str in sorted(hires.keys(), key=int):
        merged[l_str] = {}
        for h_str in sorted(hires[l_str].keys(), key=int):
            d2 = hires[l_str][h_str]["quantization"]["2"]
            q = {"2": d2}
            if l_str in std and h_str in std[l_str]:
                sq = std[l_str][h_str].get("quantization", {})
                for b in ["4", "8"]:
                    if b in sq:
                        q[b] = sq[b]
            merged[l_str][h_str] = {"quantization": q}
    return enforce_monotonicity(merged)


def run_eval(model, tokenizer, device, task_list, num_fewshot):
    """Run lm-eval tasks on a (potentially patched) model."""
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


def run_model(model_key):
    cfg = MODELS[model_key]
    print(f"\n{'='*70}\nMODEL: {cfg['name']}\n{'='*70}")
    t0 = time.time()

    profiles = load_merged_profiles(cfg)

    # Constrained MCKP allocation
    mckp = solve_mckp_constrained(profiles, BUDGET, mode="quant_only",
                                   max_2bit=MAX_2BIT, l0_exclude_2bit=True)
    uniform = uniform_quantization_baseline(profiles, bits=4)

    print(f"Loading model to {DEVICE}...")
    tokenizer = AutoTokenizer.from_pretrained(cfg["path"])
    model = AutoModelForCausalLM.from_pretrained(
        cfg["path"], torch_dtype=torch.bfloat16, attn_implementation="eager"
    )
    model = model.to(DEVICE)
    model.eval()

    result = {"model": cfg["name"], "tasks": TASKS, "num_fewshot": NUM_FEWSHOT}

    # Baseline (no quantization)
    print("\n[1/3] Baseline (bf16)...")
    result["baseline"] = run_eval(model, tokenizer, DEVICE, TASKS, NUM_FEWSHOT)
    print(f"  Baseline: {result['baseline']}")

    # Uniform 4-bit
    print("\n[2/3] Uniform 4-bit...")
    orig = patch_attention(model, uniform["allocation"])
    result["uniform_4bit"] = run_eval(model, tokenizer, DEVICE, TASKS, NUM_FEWSHOT)
    restore_attention(model, orig)
    print(f"  Uniform: {result['uniform_4bit']}")

    # Constrained MCKP
    print("\n[3/3] Constrained MCKP (k={MAX_2BIT})...")
    orig = patch_attention(model, mckp["allocation"])
    result["constrained_mckp"] = run_eval(model, tokenizer, DEVICE, TASKS, NUM_FEWSHOT)
    restore_attention(model, orig)
    print(f"  MCKP: {result['constrained_mckp']}")

    result["elapsed_seconds"] = round(time.time() - t0, 1)

    # Summary
    print(f"\n{'Task':<20} {'Baseline':>10} {'Uniform':>10} {'MCKP':>10} {'MCKP-Uni':>10}")
    print("-" * 65)
    for task in TASKS:
        bl = result["baseline"].get(task, 0)
        uni = result["uniform_4bit"].get(task, 0)
        mckp_s = result["constrained_mckp"].get(task, 0)
        delta = mckp_s - uni
        print(f"{task:<20} {bl:>10.4f} {uni:>10.4f} {mckp_s:>10.4f} {delta:>+10.4f}")

    del model, tokenizer
    gc.collect()
    torch.cuda.empty_cache()
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", choices=list(MODELS.keys()), default="llama")
    args = parser.parse_args()

    result = run_model(args.model)

    out_path = f"/root/ratekv/artifacts/w3_downstream_{args.model}_results.json"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(result, f, indent=2)
    print(f"\nSaved to {out_path}")


if __name__ == "__main__":
    main()
