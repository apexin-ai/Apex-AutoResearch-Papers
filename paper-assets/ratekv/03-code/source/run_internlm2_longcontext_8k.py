"""InternLM2-7B 8K long-context PPL eval: BF16 / uniform-4bit / constrained MCKP(k=8).

Architecture: 32 layers x 8 KV heads (GQA 4:1), 256 total KV heads.
InternLM2 uses fused wqkv — custom patch_attention_internlm2 handles
QKV splitting: [Q_groups (ng dims), K (2nd-to-last), V (last)].

Input:  artifacts/internlm2_profiles_hires.json (2-bit-only, synthesize 4/8-bit)
Output: artifacts/internlm2_longcontext_8k_results.json
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
from einops import rearrange
from transformers import AutoModelForCausalLM, AutoTokenizer, AutoConfig
from solver import solve_mckp_constrained, uniform_quantization_baseline, enforce_monotonicity
from utils import quantize_per_channel, quantize_per_token, repeat_kv

RATIO_4BIT = 0.25
RATIO_8BIT = 0.05


def rotate_half(x):
    x1 = x[..., : x.shape[-1] // 2]
    x2 = x[..., x.shape[-1] // 2 :]
    return torch.cat((-x2, x1), dim=-1)


def apply_rotary_pos_emb(q, k, cos, sin, position_ids=None, unsqueeze_dim=1):
    cos = cos.unsqueeze(unsqueeze_dim)
    sin = sin.unsqueeze(unsqueeze_dim)
    q_embed = (q * cos) + (rotate_half(q) * sin)
    k_embed = (k * cos) + (rotate_half(k) * sin)
    return q_embed, k_embed


def patch_attention_internlm2(model, allocations):
    config = model.config
    num_kv_heads = config.num_key_value_heads
    num_q_heads = config.num_attention_heads
    head_dim = config.hidden_size // num_q_heads
    n_groups = num_q_heads // num_kv_heads

    original_forwards = {}

    for layer_idx, layer in enumerate(model.model.layers):
        attn = layer.attention

        head_allocs = {}
        for h in range(num_kv_heads):
            key = f"{layer_idx},{h}"
            if key in allocations:
                atype, param = allocations[key]
                head_allocs[h] = (atype, param)
            else:
                head_allocs[h] = ("full", 16)

        if all(a[0] == "full" for a in head_allocs.values()):
            continue

        original_forwards[layer_idx] = attn.forward

        def make_forward(orig_attn, h_allocs, n_kv=num_kv_heads, ng=n_groups, hd=head_dim):
            def compressed_forward(hidden_states, attention_mask=None, position_ids=None,
                                   past_key_value=None, output_attentions=False,
                                   use_cache=False, cache_position=None, **kwargs):
                bsz, q_len, _ = hidden_states.size()

                qkv_states = orig_attn.wqkv(hidden_states)
                qkv_states = rearrange(
                    qkv_states,
                    "b q (h gs d) -> b q h gs d",
                    gs=2 + ng,
                    d=hd,
                )

                query_states = qkv_states[..., :ng, :]
                query_states = rearrange(query_states, "b q h gs d -> b q (h gs) d").transpose(1, 2)
                key_states = qkv_states[..., -2, :].transpose(1, 2)
                value_states = qkv_states[..., -1, :].transpose(1, 2)

                cos, sin = orig_attn.rotary_emb(value_states, position_ids)
                query_states, key_states = apply_rotary_pos_emb(
                    query_states, key_states, cos, sin, position_ids
                )

                for h in range(n_kv):
                    atype, param = h_allocs[h]
                    if atype == "quant" and int(param) < 16:
                        bits = int(param)
                        key_states[:, h] = quantize_per_channel(key_states[:, h:h + 1], bits).squeeze(1)
                        value_states[:, h] = quantize_per_token(value_states[:, h:h + 1], bits).squeeze(1)

                key_exp = repeat_kv(key_states, ng)
                value_exp = repeat_kv(value_states, ng)

                attn_weights = torch.matmul(query_states, key_exp.transpose(2, 3)) / math.sqrt(hd)

                if attention_mask is not None:
                    causal_mask = attention_mask[:, :, :, :key_exp.shape[-2]]
                    attn_weights = attn_weights + causal_mask
                else:
                    causal = torch.triu(
                        torch.full((q_len, q_len), float("-inf"),
                                   device=attn_weights.device, dtype=attn_weights.dtype),
                        diagonal=1,
                    )
                    attn_weights = attn_weights + causal

                attn_weights = F.softmax(attn_weights, dim=-1, dtype=torch.float32).to(query_states.dtype)
                attn_output = torch.matmul(attn_weights, value_exp)

                attn_output = attn_output.transpose(1, 2).contiguous()
                attn_output = attn_output.reshape(bsz, q_len, -1)
                attn_output = orig_attn.wo(attn_output)

                if not output_attentions:
                    attn_weights = None

                return attn_output, attn_weights, past_key_value

            return compressed_forward

        attn.forward = make_forward(attn, head_allocs)

    return original_forwards


def restore_attention_internlm2(model, original_forwards):
    for layer_idx, fwd in original_forwards.items():
        model.model.layers[layer_idx].attention.forward = fwd


def evaluate_perplexity_internlm2(model, tokenizer, device, stride=512):
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

    print(f"Evaluating PPL on {total_len} tokens, stride={stride}, {n_chunks} chunks")
    for i, begin in enumerate(range(0, total_len - 1, stride)):
        end = min(begin + stride, total_len)
        chunk = input_ids[:, begin:end]
        chunk_len = chunk.shape[1]

        with torch.no_grad():
            outputs = model(chunk, use_cache=False,
                            cache_position=torch.arange(chunk_len, device=device))
            logits = outputs.logits

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


def synthesize_multibit_profiles(raw_profiles, num_layers, num_kv_heads):
    profiles = {}
    for li in range(num_layers):
        l_str = str(li)
        layer_data = raw_profiles[l_str]
        profiles[l_str] = {}
        for hi in range(num_kv_heads):
            h_str = str(hi)
            d2 = layer_data[h_str]["quantization"]["2"]
            profiles[l_str][h_str] = {
                "quantization": {
                    "2": d2,
                    "4": d2 * RATIO_4BIT,
                    "8": d2 * RATIO_8BIT,
                }
            }
    return profiles


def main():
    parser = argparse.ArgumentParser(description="InternLM2-7B 8K long-context eval")
    parser.add_argument("--gpu", type=str, default="cuda:0")
    args = parser.parse_args()

    device = args.gpu
    model_name = "/root/autodl-tmp/.hf_cache/Shanghai_AI_Laboratory/internlm2-7b"
    profiles_path = "artifacts/internlm2_profiles_hires.json"
    output_path = "artifacts/internlm2_longcontext_8k_results.json"
    budget = 0.25
    max_2bit = 2
    seq_len = 8192
    t0 = time.time()

    config = AutoConfig.from_pretrained(model_name, trust_remote_code=True)
    num_layers = config.num_hidden_layers
    num_kv_heads = config.num_key_value_heads
    num_q_heads = config.num_attention_heads
    gqa_ratio = num_q_heads // num_kv_heads
    total_kv_heads = num_layers * num_kv_heads
    print(f"InternLM2-7B: {num_layers}L x {num_kv_heads}KV, GQA {gqa_ratio}:1, {total_kv_heads} total heads")
    print(f"8K long-context eval (stride={seq_len})")

    # Load 2-bit-only profiles and synthesize multi-bit
    print(f"\nLoading profiles from {profiles_path}...")
    with open(profiles_path) as f:
        raw = json.load(f)
    raw_profiles = raw["profiles"] if "profiles" in raw else raw
    profiles = synthesize_multibit_profiles(raw_profiles, num_layers, num_kv_heads)
    print(f"Synthesized multi-bit profiles: {num_layers} layers x {num_kv_heads} heads")
    print(f"Ratios: 4bit={RATIO_4BIT}, 8bit={RATIO_8BIT}")

    profiles = enforce_monotonicity(profiles)

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
    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(
        model_name, torch_dtype=torch.bfloat16,
        attn_implementation="eager", trust_remote_code=True
    )
    model = model.to(device)
    model.eval()
    mem_gb = torch.cuda.memory_allocated(device) / 1e9
    print(f"Model loaded. GPU mem: {mem_gb:.1f}GB")

    # BF16 baseline @ 8K
    print(f"\nEvaluating bf16 baseline on WikiText-2 (stride={seq_len})...")
    baseline_ppl = evaluate_perplexity_internlm2(model, tokenizer, device, stride=seq_len)
    print(f"BF16 8K PPL: {baseline_ppl:.4f}")

    # MCKP @ 8K
    print(f"\nEvaluating constrained MCKP (k={max_2bit}) on WikiText-2 (stride={seq_len})...")
    orig_fwds = patch_attention_internlm2(model, mckp_result["allocation"])
    mckp_ppl = evaluate_perplexity_internlm2(model, tokenizer, device, stride=seq_len)
    restore_attention_internlm2(model, orig_fwds)
    print(f"MCKP 8K PPL: {mckp_ppl:.4f}")

    # Uniform 4-bit @ 8K
    print(f"\nEvaluating uniform 4-bit on WikiText-2 (stride={seq_len})...")
    orig_fwds = patch_attention_internlm2(model, uniform_result["allocation"])
    uniform_ppl = evaluate_perplexity_internlm2(model, tokenizer, device, stride=seq_len)
    restore_attention_internlm2(model, orig_fwds)
    print(f"Uniform 4-bit 8K PPL: {uniform_ppl:.4f}")

    delta = uniform_ppl - mckp_ppl
    pct_improvement = delta / (uniform_ppl - baseline_ppl) * 100 if uniform_ppl != baseline_ppl else 0

    # Concentration analysis
    all_deltas_2bit = []
    for l_str in sorted(profiles.keys(), key=int):
        for h_str in sorted(profiles[l_str].keys(), key=int):
            d2 = profiles[l_str][h_str]["quantization"]["2"]
            all_deltas_2bit.append(d2)
    sorted_d2 = sorted(all_deltas_2bit, reverse=True)
    n_top5 = max(1, int(len(sorted_d2) * 0.05))
    total_sum = sum(all_deltas_2bit)
    top5_sum = sum(sorted_d2[:n_top5])
    top5_concentration = top5_sum / total_sum if total_sum > 0 else 0

    total_time = time.time() - t0

    results = {
        "model": model_name,
        "model_name": "InternLM2-7B",
        "experiment": "8K_longcontext_eval",
        "seq_len": seq_len,
        "architecture": {
            "num_layers": num_layers,
            "num_kv_heads": num_kv_heads,
            "num_attention_heads": num_q_heads,
            "head_dim": config.hidden_size // num_q_heads,
            "hidden_size": config.hidden_size,
            "gqa_ratio": gqa_ratio,
            "total_kv_heads": total_kv_heads,
        },
        "profiling_sources": {
            "2bit": f"{profiles_path} (bf16, hires)",
            "4bit_8bit": f"synthesized (ratio_4bit={RATIO_4BIT}, ratio_8bit={RATIO_8BIT})",
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
    print("RESULTS — InternLM2-7B 8K Long-Context Eval")
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
