"""W9 v2: Compounding scaling on WikiText-2 eval set.

Redesigned to address v1 bias:
- Use marginal benefit ranking d_h(4) - d_h(2) (descending) for top-k selection
  (this matches solver behavior: heads with smallest 4-bit -> 2-bit penalty
   are the ones the solver pushes to 2-bit first)
- Exclude all Layer-0 heads (solver always assigns them >=8-bit in constrained
  regime, so they never appear in 2-bit allocations)
- Add Random-k control (3 seeds, mean +/- std) from non-L0 pool
- Use the WikiText-2 stride eval that matches the paper's baseline (~9.81)
  -- NOT the calibration set used in v1 (which gave 8.20)
"""
import os
os.environ["HF_HOME"] = "/root/autodl-tmp/.hf_cache"
os.environ["HF_DATASETS_OFFLINE"] = "1"
os.environ["HF_HUB_OFFLINE"] = "1"
os.environ["TRANSFORMERS_OFFLINE"] = "1"

import json
import random
import time
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from eval_ppl import patch_attention, restore_attention, evaluate_perplexity


def build_head_table(profiles, exclude_layers):
    """Return list of dicts: layer, head, key, d2, d4, marginal=d4-d2.

    Heads in `exclude_layers` are dropped.
    """
    table = []
    for l_str in sorted(profiles.keys(), key=int):
        layer = int(l_str)
        if layer in exclude_layers:
            continue
        for h_str in sorted(profiles[l_str].keys(), key=int):
            q = profiles[l_str][h_str]["quantization"]
            d2 = float(q["2"])
            d4 = float(q["4"])
            table.append({
                "layer": layer,
                "head": int(h_str),
                "key": f"{l_str},{h_str}",
                "d2": d2,
                "d4": d4,
                "marginal": d4 - d2,
            })
    return table


def eval_with_allocation(model, tokenizer, device, allocation):
    orig_fwds = patch_attention(model, allocation)
    try:
        ppl = evaluate_perplexity(model, tokenizer, device)
    finally:
        restore_attention(model, orig_fwds)
    return ppl


def main():
    device = "cuda:0"
    model_name = "/root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-7B"
    profiles_path = "hires_profiles.json"
    output_json = "w9_compounding_v2_results.json"
    output_pdf = "figures/fig_compounding_v2.pdf"
    output_png = "figures/fig_compounding_v2.png"
    exclude_layers = [0]
    k_values = [1, 2, 4, 8, 12, 16, 20, 24, 32, 48, 64]
    random_seeds = [42, 123, 456]

    t0 = time.time()

    print(f"Loading profiles from {profiles_path}...")
    with open(profiles_path) as f:
        raw = json.load(f)
    profiles = raw["profiles"] if "profiles" in raw else raw

    head_table = build_head_table(profiles, exclude_layers=set(exclude_layers))
    print(f"Total non-L0 KV heads: {len(head_table)}")

    # Rank by marginal benefit (d4 - d2) descending.
    # Top heads have the smallest penalty when demoted from 4-bit to 2-bit,
    # i.e. the heads solver pushes to 2-bit first.
    ranked = sorted(head_table, key=lambda x: x["marginal"], reverse=True)
    print("Top-10 by marginal d4-d2 (excluding L0):")
    for h in ranked[:10]:
        print(f"  {h['key']:>6}  d2={h['d2']:.4f}  d4={h['d4']:.4f}  marg={h['marginal']:.4f}")

    non_l0_pool = [h for h in head_table]
    print(f"Random-k pool size: {len(non_l0_pool)}")

    print(f"\nLoading {model_name} in bf16 to {device}...")
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(
        model_name, torch_dtype=torch.bfloat16, attn_implementation="eager"
    )
    model = model.to(device)
    model.eval()
    print(f"GPU mem: {torch.cuda.memory_allocated(device) / 1e9:.1f}GB")

    print("\n=== Baseline (bf16) on WikiText-2 ===")
    baseline_ppl = evaluate_perplexity(model, tokenizer, device)
    print(f"baseline_ppl = {baseline_ppl:.4f}")

    top_k_results = []
    random_k_results = []

    for k in k_values:
        print(f"\n=== k = {k} ===")

        # A) Top-k by marginal benefit
        selected = ranked[:k]
        sel_keys = [h["key"] for h in selected]
        sum_d2 = sum(h["d2"] for h in selected)
        allocation = {h["key"]: ["quant", 2] for h in selected}

        print(f"[top-k] keys={sel_keys[:5]}{'...' if k > 5 else ''}  sum_d2={sum_d2:.4f}")
        joint_ppl = eval_with_allocation(model, tokenizer, device, allocation)
        joint_delta = joint_ppl - baseline_ppl
        additive_pred = baseline_ppl + sum_d2
        ratio = joint_delta / sum_d2 if sum_d2 > 0 else float("nan")
        print(f"[top-k] joint_ppl={joint_ppl:.4f}  add_pred={additive_pred:.4f}  ratio={ratio:.4f}")

        top_k_results.append({
            "k": k,
            "heads": sel_keys,
            "sum_d2": round(sum_d2, 6),
            "joint_ppl": round(joint_ppl, 4),
            "joint_delta": round(joint_delta, 6),
            "additive_pred": round(additive_pred, 4),
            "ratio": round(ratio, 4),
        })

        # B) Random-k from non-L0 pool, 3 seeds
        seed_ppls = []
        seed_sum_d2s = []
        seed_ratios = []
        seed_heads_record = []
        for seed in random_seeds:
            rng = random.Random(seed)
            sampled = rng.sample(non_l0_pool, k)
            s_keys = [h["key"] for h in sampled]
            s_sum_d2 = sum(h["d2"] for h in sampled)
            s_alloc = {h["key"]: ["quant", 2] for h in sampled}
            print(f"[rand seed={seed}] sum_d2={s_sum_d2:.4f}")
            s_ppl = eval_with_allocation(model, tokenizer, device, s_alloc)
            s_delta = s_ppl - baseline_ppl
            s_ratio = s_delta / s_sum_d2 if s_sum_d2 > 0 else float("nan")
            print(f"[rand seed={seed}] joint_ppl={s_ppl:.4f}  ratio={s_ratio:.4f}")
            seed_ppls.append(s_ppl)
            seed_sum_d2s.append(s_sum_d2)
            seed_ratios.append(s_ratio)
            seed_heads_record.append(s_keys)

        mean_ppl = sum(seed_ppls) / len(seed_ppls)
        var = sum((x - mean_ppl) ** 2 for x in seed_ppls) / len(seed_ppls)
        std_ppl = var ** 0.5
        mean_sum_d2 = sum(seed_sum_d2s) / len(seed_sum_d2s)
        mean_ratio = sum(seed_ratios) / len(seed_ratios)
        additive_pred_mean = baseline_ppl + mean_sum_d2

        random_k_results.append({
            "k": k,
            "seeds": random_seeds,
            "ppls": [round(x, 4) for x in seed_ppls],
            "mean_ppl": round(mean_ppl, 4),
            "std_ppl": round(std_ppl, 4),
            "mean_sum_d2": round(mean_sum_d2, 6),
            "mean_additive_pred": round(additive_pred_mean, 4),
            "mean_ratio": round(mean_ratio, 4),
            "ratios": [round(x, 4) for x in seed_ratios],
            "heads_per_seed": seed_heads_record,
        })

    total_time = time.time() - t0

    output = {
        "experiment": "w9_compounding_v2",
        "model": "Qwen2.5-7B",
        "model_path": model_name,
        "profiles_path": profiles_path,
        "ranking": "marginal benefit d_h(4) - d_h(2) descending",
        "excluded_layers": exclude_layers,
        "eval": "WikiText-2 test, stride=512 (matches paper baseline)",
        "baseline_ppl": round(baseline_ppl, 4),
        "k_values": k_values,
        "random_seeds": random_seeds,
        "top_k_results": top_k_results,
        "random_k_results": random_k_results,
        "timing_seconds": round(total_time, 1),
    }
    with open(output_json, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nJSON saved to {output_json}")

    # ----- plotting -----
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    os.makedirs("figures", exist_ok=True)

    ks = [r["k"] for r in top_k_results]
    top_joint = [r["joint_ppl"] for r in top_k_results]
    top_add = [r["additive_pred"] for r in top_k_results]
    top_ratio = [r["ratio"] for r in top_k_results]

    rand_mean = [r["mean_ppl"] for r in random_k_results]
    rand_std = [r["std_ppl"] for r in random_k_results]
    rand_add = [r["mean_additive_pred"] for r in random_k_results]
    rand_ratio = [r["mean_ratio"] for r in random_k_results]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4.5))

    ax1.plot(ks, top_joint, "o-", color="#d62728", linewidth=2, markersize=7, label="Top-k joint PPL")
    ax1.plot(ks, top_add, "^--", color="#d62728", linewidth=1.2, alpha=0.6, label="Top-k additive pred")
    ax1.errorbar(ks, rand_mean, yerr=rand_std, fmt="s-", color="#1f77b4",
                 linewidth=2, markersize=6, capsize=3, label="Random-k mean (3 seeds)")
    ax1.plot(ks, rand_add, "v--", color="#1f77b4", linewidth=1.2, alpha=0.6, label="Random-k additive pred")
    ax1.axhline(y=baseline_ppl, color="gray", linestyle=":", alpha=0.6, label=f"Baseline ({baseline_ppl:.2f})")
    ax1.axvline(x=8, color="black", linestyle="--", alpha=0.4)
    ax1.text(8, ax1.get_ylim()[1] if False else max(top_joint) * 0.95, " k=8 (paper)",
             fontsize=9, va="top", ha="left")
    ax1.set_xscale("log", base=2)
    ax1.set_xticks(ks)
    ax1.set_xticklabels([str(x) for x in ks], fontsize=8)
    ax1.set_xlabel("Number of heads at 2-bit ($k$)", fontsize=11)
    ax1.set_ylabel("Perplexity (WikiText-2)", fontsize=11)
    ax1.set_title("Joint vs additive PPL (Qwen2.5-7B, excl. L0)", fontsize=11)
    ax1.legend(fontsize=8, loc="upper left")
    ax1.grid(True, alpha=0.3)

    ax2.plot(ks, top_ratio, "o-", color="#d62728", linewidth=2, markersize=7, label="Top-k ratio")
    ax2.plot(ks, rand_ratio, "s-", color="#1f77b4", linewidth=2, markersize=6, label="Random-k mean ratio")
    ax2.axhline(y=1.0, color="gray", linestyle="--", alpha=0.6, label="Additive (=1)")
    ax2.axvline(x=8, color="black", linestyle="--", alpha=0.4, label="k=8 (paper)")
    ax2.set_xscale("log", base=2)
    ax2.set_xticks(ks)
    ax2.set_xticklabels([str(x) for x in ks], fontsize=8)
    ax2.set_xlabel("Number of heads at 2-bit ($k$)", fontsize=11)
    ax2.set_ylabel("Super-additive ratio", fontsize=11)
    ax2.set_title("Compounding ratio", fontsize=11)
    ax2.legend(fontsize=8, loc="upper left")
    ax2.grid(True, alpha=0.3)

    fig.suptitle("W9 v2 — Compounding scaling on WikiText-2 (excl. Layer-0 heads)", fontsize=12)
    fig.tight_layout()
    fig.savefig(output_pdf, bbox_inches="tight")
    fig.savefig(output_png, dpi=200, bbox_inches="tight")
    plt.close(fig)
    print(f"Plot saved to {output_pdf} and {output_png}")

    print(f"\n{'=' * 78}")
    print("W9 v2 COMPOUNDING SCALING — Qwen2.5-7B, WikiText-2 eval, excl L0")
    print(f"{'=' * 78}")
    print(f"baseline_ppl = {baseline_ppl:.4f}")
    print(f"{'k':>3}  {'top_ppl':>8} {'top_add':>8} {'top_r':>7}  "
          f"{'rnd_ppl':>10} {'rnd_add':>8} {'rnd_r':>7}")
    print("-" * 78)
    for tr, rr in zip(top_k_results, random_k_results):
        print(f"{tr['k']:>3}  {tr['joint_ppl']:>8.3f} {tr['additive_pred']:>8.3f} {tr['ratio']:>7.3f}  "
              f"{rr['mean_ppl']:>5.3f}+-{rr['std_ppl']:<4.2f} {rr['mean_additive_pred']:>8.3f} {rr['mean_ratio']:>7.3f}")
    print(f"\nTotal time: {total_time / 60:.1f}min")


if __name__ == "__main__":
    main()
