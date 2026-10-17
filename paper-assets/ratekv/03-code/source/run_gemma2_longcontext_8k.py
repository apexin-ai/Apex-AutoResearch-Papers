"""Gemma-2-9B 8K long-context PPL eval: BF16 / uniform-4bit / constrained MCKP(k=8).
Input:  gemma2_hires_bf16_2bitonly_profiles.json (2-bit deltas)
        gemma2_profiling_results.json (4/8-bit deltas)
Output: artifacts/gemma2_longcontext_8k_results.json

Gemma-2 specifics:
  - Uses patch_attention_gemma2 (handles head_dim=256, attn_logit_softcapping,
    sliding_window via 4D attention mask + cache_position).
  - Custom evaluate_perplexity with cache_position for sliding window layers.
  - BOS prepending on eval chunks (Gemma-2 tokenizer expects BOS).
"""
import os
os.environ["HF_HOME"] = "/root/autodl-tmp/.hf_cache"
os.environ["HF_DATASETS_OFFLINE"] = "1"
os.environ["TRANSFORMERS_OFFLINE"] = "1"

import argparse
import json
import math
import time
import torch
import torch.nn.functional as F
from transformers import AutoModelForCausalLM, AutoTokenizer, AutoConfig
from run_gemma2_full_pipeline import patch_attention_gemma2, restore_attention
from solver import solve_mckp_constrained, uniform_quantization_baseline, enforce_monotonicity


def evaluate_perplexity_gemma2(model, tokenizer, device, stride=512):
    """WikiText-2 PPL eval adapted for Gemma-2 (cache_position + BOS handling)."""
    from datasets import load_dataset, Dataset
    try:
        ds = load_dataset("wikitext", "wikitext-2-raw-v1", split="test")
    except Exception:
        arrow_path = "/root/autodl-tmp/.hf_cache/datasets/wikitext/wikitext-2-raw-v1/0.0.0/b08601e04326c79dfdd32d625aee71d232d685c3/wikitext-test.arrow"
        print(f"  Hub unavailable, loading from arrow: {arrow_path}")
        ds = Dataset.from_file(arrow_path)
    text = "\n\n".join([t for t in ds["text"] if t.strip()])

    encodings = tokenizer(text, return_tensors="pt")
    input_ids = encodings.input_ids.to(device)
    total_len = input_ids.shape[1]
    total_loss = 0.0
    total_tokens = 0
    n_chunks = (total_len - 1) // stride
    bos_id = tokenizer.bos_token_id
    bos_tensor = torch.tensor([[bos_id]], device=device)

    print(f"Evaluating PPL on {total_len} tokens, stride={stride}, {n_chunks} chunks")
    for i, begin in enumerate(range(0, total_len - 1, stride)):
        end = min(begin + stride, total_len)
        chunk = input_ids[:, begin:end]

        needs_bos = chunk[0, 0].item() != bos_id
        if needs_bos:
            model_input = torch.cat([bos_tensor, chunk], dim=1)
        else:
            model_input = chunk

        with torch.no_grad():
            outputs = model(model_input, use_cache=False,
                            cache_position=torch.arange(model_input.shape[1], device=device))
            logits = outputs.logits

        if needs_bos:
            shift_logits = logits[:, 1:-1].contiguous()
        else:
            shift_logits = logits[:, :-1].contiguous()
        shift_labels = chunk[:, 1:].contiguous()

        loss = F.cross_entropy(
            shift_logits.float().view(-1, shift_logits.shape[-1]),
            shift_labels.view(-1), reduction="sum")
        total_loss += loss.item()
        total_tokens += shift_labels.numel()
        if (i + 1) % 50 == 0:
            print(f"  chunk {i+1}/{n_chunks}, running ppl={math.exp(total_loss/total_tokens):.2f}")

    return math.exp(total_loss / total_tokens)


def main():
    parser = argparse.ArgumentParser(description="Gemma-2-9B 8K long-context eval")
    parser.add_argument("--gpu", type=str, default="cuda:0")
    args = parser.parse_args()

    device = args.gpu
    model_name = "/root/autodl-tmp/.hf_cache/google/gemma-2-9b"
    hires_2bit_path = "gemma2_hires_bf16_2bitonly_profiles.json"
    standard_path = "gemma2_profiling_results.json"
    output_path = "artifacts/gemma2_longcontext_8k_results.json"
    budget = 0.25
    max_2bit = 8
    seq_len = 8192
    t0 = time.time()

    config = AutoConfig.from_pretrained(model_name)
    num_layers = config.num_hidden_layers
    num_kv_heads = config.num_key_value_heads
    num_q_heads = config.num_attention_heads
    head_dim = getattr(config, "head_dim", config.hidden_size // num_q_heads)
    gqa_ratio = num_q_heads // num_kv_heads
    total_kv_heads = num_layers * num_kv_heads
    softcap = getattr(config, "attn_logit_softcapping", None)
    sliding_window = getattr(config, "sliding_window", None)
    print(f"Gemma-2-9B: {num_layers}L x {num_kv_heads}KV, GQA {gqa_ratio}:1, {total_kv_heads} total heads")
    print(f"head_dim={head_dim}, softcap={softcap}, sliding_window={sliding_window}")
    print(f"8K long-context eval (stride={seq_len})")

    # Merge hires 2-bit deltas with standard 4-bit/8-bit deltas
    print(f"\nLoading hires 2-bit profiles from {hires_2bit_path}...")
    with open(hires_2bit_path) as f:
        hires_data = json.load(f)
    print(f"Hires: {len(hires_data)} layers, {len(hires_data['0'])} heads/layer")

    print(f"Loading standard profiles from {standard_path}...")
    with open(standard_path) as f:
        std_raw = json.load(f)
    std_data = std_raw["profiles"] if "profiles" in std_raw else std_raw
    print(f"Standard: {len(std_data)} layers, {len(std_data['0'])} heads/layer")

    print("Merging profiles (hires 2-bit + standard 4-bit/8-bit)...")
    merged = {}
    for l_str in sorted(hires_data.keys(), key=int):
        merged[l_str] = {}
        for h_str in sorted(hires_data[l_str].keys(), key=int):
            d2_hires = hires_data[l_str][h_str]["quantization"]["2"]
            d4_std = std_data[l_str][h_str]["quantization"]["4"]
            d8_std = std_data[l_str][h_str]["quantization"]["8"]
            merged[l_str][h_str] = {"quantization": {"2": d2_hires, "4": d4_std, "8": d8_std}}

    profiles = enforce_monotonicity(merged)

    # Constrained MCKP
    print(f"\nRunning constrained MCKP (max_2bit={max_2bit}, budget={budget})...")
    mckp_result = solve_mckp_constrained(
        profiles, budget, mode="quant_only",
        max_2bit=max_2bit, l0_exclude_2bit=True)

    bit_counts = {}
    for key, (atype, param) in mckp_result["allocation"].items():
        b = int(param) if atype == "quant" else 16
        bit_counts[b] = bit_counts.get(b, 0) + 1
    print(f"Bit distribution: {bit_counts}")
    print(f"Total distortion: {mckp_result['total_distortion']:.6f}")

    # Uniform 4-bit allocation
    uniform_result = uniform_quantization_baseline(profiles, bits=4)

    # Load model
    print(f"\nLoading model in bf16 to {device}...")
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(
        model_name, torch_dtype=torch.bfloat16, attn_implementation="eager"
    )
    model = model.to(device)
    model.eval()
    mem_gb = torch.cuda.memory_allocated(device) / 1e9
    print(f"Model loaded. GPU mem: {mem_gb:.1f}GB")

    # BF16 baseline @ 8K
    print(f"\nEvaluating bf16 baseline on WikiText-2 (stride={seq_len})...")
    baseline_ppl = evaluate_perplexity_gemma2(model, tokenizer, device, stride=seq_len)
    print(f"BF16 8K PPL: {baseline_ppl:.4f}")

    # MCKP @ 8K
    print(f"\nEvaluating constrained MCKP (k={max_2bit}) on WikiText-2 (stride={seq_len})...")
    orig_fwds = patch_attention_gemma2(model, mckp_result["allocation"])
    mckp_ppl = evaluate_perplexity_gemma2(model, tokenizer, device, stride=seq_len)
    restore_attention(model, orig_fwds)
    print(f"MCKP 8K PPL: {mckp_ppl:.4f}")

    # Uniform 4-bit @ 8K
    print(f"\nEvaluating uniform 4-bit on WikiText-2 (stride={seq_len})...")
    orig_fwds = patch_attention_gemma2(model, uniform_result["allocation"])
    uniform_ppl = evaluate_perplexity_gemma2(model, tokenizer, device, stride=seq_len)
    restore_attention(model, orig_fwds)
    print(f"Uniform 4-bit 8K PPL: {uniform_ppl:.4f}")

    delta = uniform_ppl - mckp_ppl
    pct_improvement = delta / (uniform_ppl - baseline_ppl) * 100 if uniform_ppl != baseline_ppl else 0

    # Concentration analysis from hires 2-bit deltas
    all_deltas_2bit = []
    for l_str in sorted(merged.keys(), key=int):
        for h_str in sorted(merged[l_str].keys(), key=int):
            d2 = merged[l_str][h_str]["quantization"]["2"]
            all_deltas_2bit.append(d2)
    sorted_d2 = sorted(all_deltas_2bit, reverse=True)
    n_top5 = max(1, int(len(sorted_d2) * 0.05))
    total_sum = sum(all_deltas_2bit)
    top5_sum = sum(sorted_d2[:n_top5])
    top5_concentration = top5_sum / total_sum if total_sum > 0 else 0

    total_time = time.time() - t0

    results = {
        "model": "google/gemma-2-9b",
        "model_name": "Gemma-2-9B",
        "experiment": "8K_longcontext_eval",
        "seq_len": seq_len,
        "architecture": {
            "num_layers": num_layers,
            "num_kv_heads": num_kv_heads,
            "num_attention_heads": num_q_heads,
            "head_dim": head_dim,
            "hidden_size": config.hidden_size,
            "gqa_ratio": gqa_ratio,
            "total_kv_heads": total_kv_heads,
            "attn_logit_softcapping": softcap,
            "sliding_window": sliding_window,
        },
        "profiling_sources": {
            "2bit": f"{hires_2bit_path} (bf16, hires)",
            "4bit_8bit": f"{standard_path}",
        },
        "constraint": {"max_2bit": max_2bit, "budget": budget, "l0_exclude_2bit": True},
        "results_8k": {
            "baseline_ppl": round(baseline_ppl, 4),
            "mckp_ppl": round(mckp_ppl, 4),
            "uniform4bit_ppl": round(uniform_ppl, 4),
            "mckp_improvement_over_uniform": round(delta, 4),
            "mckp_improvement_pct": round(pct_improvement, 2),
        },
        "bit_distribution": bit_counts,
        "mckp_total_distortion": mckp_result["total_distortion"],
        "mckp_actual_memory_ratio": mckp_result["actual_memory_ratio"],
        "analysis": {
            "top5_concentration": round(top5_concentration, 4),
        },
        "timing": {"total_seconds": round(total_time, 1)},
    }

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(results, f, indent=2)

    print(f"\n{'=' * 60}")
    print("RESULTS — Gemma-2-9B 8K Long-Context Eval")
    print(f"{'=' * 60}")
    print(f"{'Method':<30} {'8K PPL':>10}")
    print("-" * 42)
    print(f"{'Baseline (bf16)':<30} {baseline_ppl:>10.4f}")
    print(f"{'Constrained MCKP (k=8)':<30} {mckp_ppl:>10.4f}")
    print(f"{'Uniform 4-bit':<30} {uniform_ppl:>10.4f}")
    print(f"\nMCKP improvement over uniform: {delta:+.4f} ({pct_improvement:+.1f}%)")
    print(f"Top-5% concentration: {top5_concentration:.4f}")
    print(f"Total time: {total_time / 60:.1f}min")
    print(f"Saved to {output_path}")


if __name__ == "__main__":
    main()
