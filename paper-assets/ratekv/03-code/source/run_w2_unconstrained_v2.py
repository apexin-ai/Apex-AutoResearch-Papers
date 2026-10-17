"""W2 v2: unconstrained greedy & MCKP baselines with full {2,4,8,16} profiles + WikiText-2 eval.

Uses merged profiles (hires bf16 2-bit + standard 4/8-bit) for models without
full hires profiles. Evaluates on WikiText-2 test set to match Table 1/2 numbers.

Changes from v1:
- Full {2,4,8,16} action space (v1 had only {2,16} due to 2bitonly profiles)
- WikiText-2 test set eval (v1 used calibration data)
- Also evaluates uniform 4-bit baseline for comparison
"""
import os
os.environ["HF_HOME"] = "/root/autodl-tmp/.hf_cache"

import gc
import json
import math
import time
import torch
import torch.nn.functional as F
from pathlib import Path
from transformers import AutoModelForCausalLM, AutoTokenizer, AutoConfig

from solver import solve_mckp, enforce_monotonicity, uniform_quantization_baseline
from eval_ppl import patch_attention, restore_attention, evaluate_perplexity
from run_gemma2_full_pipeline import patch_attention_gemma2


MODELS = [
    {
        "name": "Yi-1.5-9B",
        "path": "/root/autodl-tmp/.hf_cache/01ai/Yi-1___5-9B",
        # Merge: hires 2-bit + standard 4/8-bit
        "hires_2bit": "yi15_hires_bf16_2bitonly_profiles.json",
        "standard": "yi15_profiling_results.json",
        "full_hires": None,
        "patch": "standard",
        "prepend_bos": False,
    },
    {
        "name": "Llama-3.1-8B",
        "path": "/root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-8B",
        # Try full hires first; if missing 4/8 deltas, merge with standard
        "hires_2bit": "llama_hires_bf16_2bitonly_profiles.json",
        "standard": "llama_profiling_results.json",
        "full_hires": None,
        "patch": "standard",
        "prepend_bos": False,
    },
    {
        "name": "Mistral-7B-v0.3",
        "path": "/root/autodl-tmp/models/Mistral-7B-v0.3",
        # Full hires profiles available
        "hires_2bit": None,
        "standard": None,
        "full_hires": "mistral_ppl_profiles_hires.json",
        "patch": "standard",
        "prepend_bos": False,
    },
    {
        "name": "Gemma-2-9B",
        "path": "/root/autodl-tmp/.hf_cache/google/gemma-2-9b",
        # Merge: hires 2-bit + standard 4/8-bit
        "hires_2bit": "gemma2_hires_bf16_2bitonly_profiles.json",
        "standard": "gemma2_profiling_results.json",
        "full_hires": None,
        "patch": "gemma2",
        "prepend_bos": True,
    },
]


DEVICE = "cuda:0"
BUDGET = 0.25
BIT_OPTIONS = [2, 4, 8, 16]


def load_profiles(cfg):
    """Load or merge profiles to get full {2,4,8} delta data per head."""
    base = "/root/ratekv/"

    # Option 1: full hires profiles (all bitwidths)
    if cfg["full_hires"]:
        path = os.path.join(base, cfg["full_hires"])
        print(f"  Loading full hires profiles: {path}")
        with open(path) as f:
            raw = json.load(f)
        profiles = raw.get("profiles", raw)
        # Verify all bitwidths present
        sample_layer = next(iter(profiles.values()))
        sample_head = next(iter(sample_layer.values()))
        qdata = sample_head.get("quantization", {})
        avail = set(qdata.keys())
        print(f"  Available bitwidths in profile: {avail}")
        return profiles, "full_hires"

    # Option 2: merge hires 2-bit + standard 4/8-bit
    hires_path = os.path.join(base, cfg["hires_2bit"])
    std_path = os.path.join(base, cfg["standard"])

    print(f"  Loading hires 2-bit: {hires_path}")
    with open(hires_path) as f:
        hires_raw = json.load(f)
    hires = hires_raw.get("profiles", hires_raw)

    print(f"  Loading standard profiles: {std_path}")
    with open(std_path) as f:
        std_raw = json.load(f)
    std = std_raw.get("profiles", std_raw)

    # Check if standard has full bitwidths (2,4,8)
    sample_layer = next(iter(std.values()))
    sample_head = next(iter(sample_layer.values()))
    std_qdata = sample_head.get("quantization", {})
    print(f"  Standard bitwidths: {set(std_qdata.keys())}")

    # Merge: 2-bit from hires, 4-bit and 8-bit from standard
    merged = {}
    for l_str in sorted(hires.keys(), key=int):
        merged[l_str] = {}
        for h_str in sorted(hires[l_str].keys(), key=int):
            d2_hires = hires[l_str][h_str]["quantization"]["2"]
            q_merged = {"2": d2_hires}
            if l_str in std and h_str in std[l_str]:
                std_q = std[l_str][h_str].get("quantization", {})
                for b in ["4", "8"]:
                    if b in std_q:
                        q_merged[b] = std_q[b]
            merged[l_str][h_str] = {"quantization": q_merged}

    n_layers = len(merged)
    n_heads = len(next(iter(merged.values())))
    sample = merged[next(iter(merged.keys()))][next(iter(next(iter(merged.values())).keys()))]
    print(f"  Merged: {n_layers}L x {n_heads}H, bitwidths={set(sample['quantization'].keys())}")
    return merged, "merged_hires_2bit_standard_4bit_8bit"


def unconstrained_greedy(profiles, budget, bit_options=BIT_OPTIONS):
    """Greedy downgrade with no cardinality constraint, full bitwidth options."""
    heads = []
    for l_str in sorted(profiles.keys(), key=lambda x: int(x)):
        for h_str in sorted(profiles[l_str].keys(), key=lambda x: int(x)):
            entry = profiles[l_str][h_str]
            dmap = {16: 0.0}
            qdata = entry.get("quantization", {})
            for b in bit_options:
                if b == 16:
                    continue
                for key in (str(b), str(float(b))):
                    if key in qdata:
                        dmap[b] = float(qdata[key])
                        break
            avail = sorted(dmap.keys())
            heads.append((int(l_str), int(h_str), dmap, avail))

    n_heads = len(heads)
    max_bits = max(bit_options)
    allocation = [max_bits] * n_heads
    target_mem = budget * n_heads * max_bits

    while sum(allocation) > target_mem + 1e-9:
        best_head = None
        best_next = None
        best_eff = float("inf")
        for i, (l, h, dmap, avail) in enumerate(heads):
            cur = allocation[i]
            cand = [b for b in avail if b < cur]
            if not cand:
                continue
            cur_d = dmap.get(cur, 0.0)
            for nb in cand:
                nb_d = dmap[nb]
                bits_saved = cur - nb
                eff = (nb_d - cur_d) / bits_saved
                if eff < best_eff - 1e-15:
                    best_eff = eff
                    best_head = i
                    best_next = nb
        if best_head is None:
            break
        allocation[best_head] = best_next

    alloc_dict = {}
    total_dist = 0.0
    bit_dist = {}
    for i, (l, h, dmap, _avail) in enumerate(heads):
        b = allocation[i]
        alloc_dict[f"{l},{h}"] = ["quant" if b < 16 else "full", b]
        total_dist += dmap.get(b, 0.0)
        bit_dist[b] = bit_dist.get(b, 0) + 1
    actual_ratio = sum(allocation) / (n_heads * max_bits)
    return {
        "allocation": alloc_dict,
        "total_distortion": total_dist,
        "actual_memory_ratio": actual_ratio,
        "bit_distribution": bit_dist,
        "n_2bit": bit_dist.get(2, 0),
    }


def run_one(model_cfg):
    print("\n" + "=" * 70)
    print(f"MODEL: {model_cfg['name']}")
    print("=" * 70)
    t0 = time.time()

    # Load/merge profiles
    profiles_raw, profile_source = load_profiles(model_cfg)
    profiles = enforce_monotonicity(profiles_raw)
    n_layers = len(profiles)
    n_heads_per = len(next(iter(profiles.values())))
    total_heads = n_layers * n_heads_per
    print(f"Profiles: {n_layers}L x {n_heads_per}H = {total_heads} heads ({profile_source})")

    # Run unconstrained greedy
    print(f"\nGreedy unconstrained ({BIT_OPTIONS}, budget={BUDGET})...")
    greedy = unconstrained_greedy(profiles, BUDGET, BIT_OPTIONS)
    print(f"  bit_dist={greedy['bit_distribution']}  mem={greedy['actual_memory_ratio']:.4f}  n_2bit={greedy['n_2bit']}")

    # Run unconstrained MCKP
    print(f"\nMCKP unconstrained (quant_only, budget={BUDGET})...")
    mckp = solve_mckp(profiles, BUDGET, mode="quant_only")
    bit_dist_mckp = {}
    for _, (atype, param) in mckp["allocation"].items():
        b = int(param) if atype == "quant" else 16
        bit_dist_mckp[b] = bit_dist_mckp.get(b, 0) + 1
    n_2bit_mckp = bit_dist_mckp.get(2, 0)
    print(f"  bit_dist={bit_dist_mckp}  mem={mckp['actual_memory_ratio']:.4f}  n_2bit={n_2bit_mckp}")

    # Uniform 4-bit allocation
    uniform = uniform_quantization_baseline(profiles, bits=4)

    # Load model
    print(f"\nLoading model {model_cfg['name']} to {DEVICE}...")
    tokenizer = AutoTokenizer.from_pretrained(model_cfg["path"])
    model = AutoModelForCausalLM.from_pretrained(
        model_cfg["path"], torch_dtype=torch.bfloat16, attn_implementation="eager"
    )
    model = model.to(DEVICE)
    model.eval()
    mem_gb = torch.cuda.memory_allocated(DEVICE) / 1e9
    print(f"  GPU mem: {mem_gb:.1f}GB")

    patcher = patch_attention_gemma2 if model_cfg["patch"] == "gemma2" else patch_attention

    # Evaluate baseline on WikiText-2 test set
    print("\nBaseline PPL (WikiText-2 test)...")
    baseline_ppl = evaluate_perplexity(model, tokenizer, DEVICE)
    print(f"  baseline_ppl={baseline_ppl:.4f}")

    # Evaluate uniform 4-bit
    print("Uniform 4-bit PPL (WikiText-2 test)...")
    orig = patcher(model, uniform["allocation"])
    uniform_ppl = evaluate_perplexity(model, tokenizer, DEVICE)
    restore_attention(model, orig)
    print(f"  uniform_ppl={uniform_ppl:.4f}")

    # Evaluate unconstrained greedy
    print("Greedy unconstrained PPL (WikiText-2 test)...")
    orig = patcher(model, greedy["allocation"])
    greedy_ppl = evaluate_perplexity(model, tokenizer, DEVICE)
    restore_attention(model, orig)
    print(f"  greedy_ppl={greedy_ppl:.4f}")

    # Evaluate unconstrained MCKP
    print("MCKP unconstrained PPL (WikiText-2 test)...")
    orig = patcher(model, mckp["allocation"])
    mckp_ppl = evaluate_perplexity(model, tokenizer, DEVICE)
    restore_attention(model, orig)
    print(f"  mckp_ppl={mckp_ppl:.4f}")

    elapsed = time.time() - t0
    greedy_vs_uniform = greedy_ppl / baseline_ppl
    mckp_vs_uniform = mckp_ppl / baseline_ppl
    is_catastrophic = greedy_ppl > 3 * baseline_ppl or mckp_ppl > 3 * baseline_ppl

    result = {
        "model_name": model_cfg["name"],
        "model_path": model_cfg["path"],
        "profile_source": profile_source,
        "eval_data": "wikitext-2-raw-v1 (test split)",
        "budget": BUDGET,
        "bit_options": BIT_OPTIONS,
        "baseline_wt2_ppl": round(baseline_ppl, 4),
        "uniform_4bit_wt2_ppl": round(uniform_ppl, 4),
        "unconstrained_greedy_wt2_ppl": round(greedy_ppl, 4),
        "unconstrained_mckp_wt2_ppl": round(mckp_ppl, 4),
        "greedy_vs_baseline_ratio": round(greedy_vs_uniform, 2),
        "mckp_vs_baseline_ratio": round(mckp_vs_uniform, 2),
        "catastrophic": is_catastrophic,
        "greedy": {
            "bit_distribution": {int(k): int(v) for k, v in greedy["bit_distribution"].items()},
            "n_2bit_heads": int(greedy["n_2bit"]),
            "actual_memory_ratio": round(greedy["actual_memory_ratio"], 4),
            "total_distortion": float(greedy["total_distortion"]),
        },
        "mckp": {
            "bit_distribution": {int(k): int(v) for k, v in bit_dist_mckp.items()},
            "n_2bit_heads": int(n_2bit_mckp),
            "actual_memory_ratio": round(mckp["actual_memory_ratio"], 4),
            "total_distortion": float(mckp["total_distortion"]),
        },
        "elapsed_seconds": round(elapsed, 1),
    }

    print(f"\n{'=' * 60}")
    print(f"  {model_cfg['name']} SUMMARY")
    print(f"{'=' * 60}")
    print(f"  Baseline:   {baseline_ppl:.4f}")
    print(f"  Uniform:    {uniform_ppl:.4f}")
    print(f"  Greedy:     {greedy_ppl:.4f}  ({greedy_vs_uniform:.2f}x baseline)")
    print(f"  MCKP:       {mckp_ppl:.4f}  ({mckp_vs_uniform:.2f}x baseline)")
    print(f"  Catastrophic: {is_catastrophic}")

    del model, tokenizer
    gc.collect()
    torch.cuda.empty_cache()
    return result


def main():
    t_total = time.time()
    out_path = "/root/ratekv/artifacts/w2_unconstrained_v2_results.json"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    results = {"exp_id": "w2_unconstrained_baselines_v2", "eval": "wikitext-2-test", "models": {}}

    for cfg in MODELS:
        try:
            results["models"][cfg["name"]] = run_one(cfg)
        except Exception as e:
            import traceback
            tb = traceback.format_exc()
            print(f"\nERROR on {cfg['name']}: {e}\n{tb}")
            results["models"][cfg["name"]] = {"error": str(e), "traceback": tb}
        with open(out_path, "w") as f:
            json.dump(results, f, indent=2)
        print(f"Intermediate save -> {out_path}")

    results["total_elapsed_seconds"] = round(time.time() - t_total, 1)
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nALL DONE. Total {(time.time()-t_total)/60:.1f}min. Saved {out_path}")


if __name__ == "__main__":
    main()
