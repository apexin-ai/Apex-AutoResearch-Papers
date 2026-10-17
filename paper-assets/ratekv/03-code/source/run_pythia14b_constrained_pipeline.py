"""Pythia-1.4B constrained vs uniform pipeline (cuda:0).

Evaluates uniform-4bit, constrained MCKP, and unconstrained MCKP
on WikiText-2 to verify that Flat-shape models gain nothing from
non-uniform allocation.
"""
import os, json, time, copy
os.environ["HF_HOME"] = "/root/autodl-tmp/.hf_cache"
os.environ["HF_DATASETS_OFFLINE"] = "0"

import torch
import torch.nn.functional as F
from transformers import AutoModelForCausalLM, AutoTokenizer, AutoConfig
from transformers.models.gpt_neox.modeling_gpt_neox import apply_rotary_pos_emb

from eval_ppl import evaluate_perplexity
from solver import (solve_mckp_constrained, solve_mckp,
                    uniform_quantization_baseline)
from utils import quantize_per_channel

MODEL_PATH = "/root/autodl-tmp/.hf_cache/EleutherAI/pythia-1.4b"
PROFILE_PATH = "pythia14b_hires_bf16_2bitonly_profiles.json"
OUTPUT_PATH = "artifacts/pythia14b_constrained_pipeline_results.json"
DEVICE = "cuda:0"
BUDGET = 0.25
RATIO_4BIT = 0.25
RATIO_8BIT = 0.05
MAX_2BIT = 8


def patch_attention_pythia(model, allocations):
    config = model.config
    num_heads = config.num_attention_heads
    head_dim = config.hidden_size // num_heads
    original_forwards = {}

    for layer_idx, layer in enumerate(model.gpt_neox.layers):
        attn = layer.attention
        head_allocs = {}
        for h in range(num_heads):
            key = f"{layer_idx},{h}"
            if key in allocations:
                atype, param = allocations[key]
                head_allocs[h] = (atype, param)
            else:
                head_allocs[h] = ("full", 16)

        if all(a[0] == "full" for a in head_allocs.values()):
            continue

        original_forwards[layer_idx] = attn.forward

        def make_forward(orig_attn, h_allocs, nh=num_heads, hd=head_dim):
            def compressed_forward(hidden_states, attention_mask=None,
                                   position_embeddings=None, **kwargs):
                bsz, seq_len, _ = hidden_states.size()
                qkv = orig_attn.query_key_value(hidden_states)
                qkv = qkv.view(bsz, seq_len, nh, 3 * hd).transpose(1, 2)
                query_states, key_states, value_states = qkv.chunk(3, dim=-1)

                cos, sin = position_embeddings
                query_states, key_states = apply_rotary_pos_emb(
                    query_states, key_states, cos, sin)

                for h in range(nh):
                    atype, param = h_allocs[h]
                    if atype == "quant" and int(param) < 16:
                        bits = int(param)
                        key_states[:, h] = quantize_per_channel(
                            key_states[:, h:h+1], bits).squeeze(1)
                        value_states[:, h] = quantize_per_channel(
                            value_states[:, h:h+1], bits).squeeze(1)

                attn_weights = torch.matmul(
                    query_states,
                    key_states.transpose(2, 3)) * orig_attn.scaling
                if attention_mask is not None:
                    causal_mask = attention_mask[:, :, :, :key_states.shape[-2]]
                    attn_weights = attn_weights + causal_mask
                attn_weights = F.softmax(
                    attn_weights, dim=-1, dtype=torch.float32
                ).to(query_states.dtype)
                attn_output = torch.matmul(attn_weights, value_states)
                attn_output = attn_output.transpose(1, 2).reshape(
                    bsz, seq_len, -1).contiguous()
                attn_output = orig_attn.dense(attn_output)
                return attn_output, None

            return compressed_forward

        attn.forward = make_forward(attn, head_allocs)

    return original_forwards


def restore_attention_pythia(model, original_forwards):
    for layer_idx, orig_fwd in original_forwards.items():
        model.gpt_neox.layers[layer_idx].attention.forward = orig_fwd


def main():
    t0 = time.time()

    # --- Config ---
    cfg = AutoConfig.from_pretrained(MODEL_PATH)
    num_layers = cfg.num_hidden_layers
    num_heads = cfg.num_attention_heads
    total_heads = num_layers * num_heads
    print(f"Pythia-1.4B: {num_layers}L x {num_heads}H = {total_heads} heads (MHA)")

    # --- Load & synthesize profiles ---
    with open(PROFILE_PATH) as f:
        raw = json.load(f)
    baseline_ppl = raw["baseline_ppl"]
    print(f"Baseline PPL (from profiling): {baseline_ppl:.4f}")

    # Build profiles in solver dict format: {"layer_str": {"head_str": {"quantization": {...}}}}
    profiles = {}
    all_deltas = []
    for li in range(num_layers):
        layer_data = raw["profiles"][str(li)]
        profiles[str(li)] = {}
        for hi in range(num_heads):
            delta_2bit = layer_data[str(hi)]["quantization"]["2"]
            delta_4bit = delta_2bit * RATIO_4BIT
            delta_8bit = delta_2bit * RATIO_8BIT
            profiles[str(li)][str(hi)] = {
                "quantization": {
                    "2": delta_2bit,
                    "4": delta_4bit,
                    "8": delta_8bit,
                }
            }
            all_deltas.append(delta_2bit)

    # --- Concentration analysis ---
    all_deltas.sort(reverse=True)
    total = sum(all_deltas)
    t1 = all_deltas[0] / total if total > 0 else 0
    t5_sum = sum(all_deltas[:max(1, int(0.05 * len(all_deltas)))])
    t5 = t5_sum / total if total > 0 else 0
    print(f"Concentration: t1={t1:.4f}, t5={t5:.4f} (Flat shape)")

    # --- Solve ---
    print("\n--- Solving allocations ---")
    constrained = solve_mckp_constrained(
        profiles, BUDGET, mode="quant_only",
        max_2bit=MAX_2BIT, l0_exclude_2bit=True)
    unconstrained = solve_mckp(profiles, BUDGET, mode="quant_only")
    uniform = uniform_quantization_baseline(profiles, bits=4)

    for name, sol in [("Constrained", constrained),
                      ("Unconstrained", unconstrained),
                      ("Uniform-4bit", uniform)]:
        bits_dist = {}
        for k, v in sol["allocation"].items():
            b = int(v[1])
            bits_dist[b] = bits_dist.get(b, 0) + 1
        print(f"  {name}: mem={sol['actual_memory_ratio']:.4f}, "
              f"dist={sol['total_distortion']:.6f}, bits={bits_dist}")

    # --- Load model ---
    print("\nLoading model...")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_PATH, torch_dtype=torch.bfloat16,
        attn_implementation="eager")
    model.to(DEVICE).eval()
    print("Model loaded.")

    # --- Eval: BF16 baseline ---
    print("\n[1/4] BF16 baseline PPL...")
    ppl_bf16 = evaluate_perplexity(model, tokenizer, DEVICE)
    print(f"  BF16 PPL = {ppl_bf16:.4f}")

    # --- Eval: Uniform 4-bit ---
    print("\n[2/4] Uniform 4-bit PPL...")
    orig_fwds = patch_attention_pythia(model, uniform["allocation"])
    ppl_uniform = evaluate_perplexity(model, tokenizer, DEVICE)
    restore_attention_pythia(model, orig_fwds)
    print(f"  Uniform-4bit PPL = {ppl_uniform:.4f}")

    # --- Eval: Constrained MCKP ---
    print("\n[3/4] Constrained MCKP PPL...")
    orig_fwds = patch_attention_pythia(model, constrained["allocation"])
    ppl_constrained = evaluate_perplexity(model, tokenizer, DEVICE)
    restore_attention_pythia(model, orig_fwds)
    print(f"  Constrained PPL = {ppl_constrained:.4f}")

    # --- Eval: Unconstrained MCKP ---
    print("\n[4/4] Unconstrained MCKP PPL...")
    orig_fwds = patch_attention_pythia(model, unconstrained["allocation"])
    ppl_unconstrained = evaluate_perplexity(model, tokenizer, DEVICE)
    restore_attention_pythia(model, orig_fwds)
    print(f"  Unconstrained PPL = {ppl_unconstrained:.4f}")

    # --- Save results ---
    elapsed = time.time() - t0
    results = {
        "model": "EleutherAI/pythia-1.4b",
        "architecture": "GPT-NeoX",
        "shape": "Flat",
        "concentration": {"t1": round(t1, 4), "t5": round(t5, 4)},
        "budget": BUDGET,
        "max_2bit": MAX_2BIT,
        "baseline_ppl_profiling": round(baseline_ppl, 4),
        "ppl_bf16": round(ppl_bf16, 4),
        "ppl_uniform_4bit": round(ppl_uniform, 4),
        "ppl_constrained_mckp": round(ppl_constrained, 4),
        "ppl_unconstrained_mckp": round(ppl_unconstrained, 4),
        "delta_uniform": round(ppl_uniform - ppl_bf16, 4),
        "delta_constrained": round(ppl_constrained - ppl_bf16, 4),
        "delta_unconstrained": round(ppl_unconstrained - ppl_bf16, 4),
        "constrained_allocation": constrained["allocation"],
        "unconstrained_allocation": unconstrained["allocation"],
        "constrained_bit_distribution": constrained.get("bit_distribution", {}),
        "unconstrained_bit_distribution": unconstrained.get("bit_distribution", {}),
        "elapsed_seconds": round(elapsed, 1),
    }

    os.makedirs("artifacts", exist_ok=True)
    with open(OUTPUT_PATH, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to {OUTPUT_PATH}")
    print(f"Total time: {elapsed/60:.1f} min")

    # --- Summary ---
    print("\n=== SUMMARY ===")
    print(f"BF16 baseline:       {ppl_bf16:.4f}")
    print(f"Uniform 4-bit:       {ppl_uniform:.4f}  (delta={ppl_uniform-ppl_bf16:+.4f})")
    print(f"Constrained MCKP:    {ppl_constrained:.4f}  (delta={ppl_constrained-ppl_bf16:+.4f})")
    print(f"Unconstrained MCKP:  {ppl_unconstrained:.4f}  (delta={ppl_unconstrained-ppl_bf16:+.4f})")
    gap = ppl_constrained - ppl_uniform
    print(f"Constrained vs Uniform gap: {gap:+.4f}")
    if abs(gap) < 0.1:
        print("=> Flat shape confirmed: constrained ≈ uniform (as predicted)")
    else:
        print(f"=> Unexpected gap: {gap:+.4f}")


if __name__ == "__main__":
    main()
