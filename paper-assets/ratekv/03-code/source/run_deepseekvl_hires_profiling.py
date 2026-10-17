"""DeepSeek-V2-Lite hires bf16 profiling — 2-bit only concentration measurement.

MLA (Multi-head Latent Attention): compressed KV via low-rank projection.
KV path: hidden → kv_a_proj_with_mqa → [kv_lora_rank + qk_rope_head_dim]
  → kv_a_layernorm → kv_b_proj → per-head k_nope + value_states.
RoPE applied only to k_pe (shared across heads, not quantized).
Per-head quantization targets decompressed k_nope and value_states.
Architecture: model.model.layers[i].self_attn, trust_remote_code=True required.

Input:  calibration_hires.json (64 seqs × 2048 tok)
Output: artifacts/deepseekvl_profiles_hires.json
"""
import os
os.environ["HF_HOME"] = "/root/autodl-tmp/.hf_cache"
os.environ["HF_DATASETS_OFFLINE"] = "1"

import argparse
import json
import math
import time
import torch
import torch.nn.functional as F
from transformers import AutoModelForCausalLM, AutoTokenizer, AutoConfig
from transformers.models.deepseek_v2.modeling_deepseek_v2 import apply_rotary_emb
from utils import quantize_per_channel, quantize_per_token


def load_calibration_data(tokenizer, path, num_samples, seq_len, device):
    with open(path) as f:
        samples = json.load(f)
    all_ids = []
    for s in samples:
        tokens = tokenizer.encode(s["text"], add_special_tokens=False)
        if len(tokens) >= seq_len:
            all_ids.append(tokens[:seq_len])
        if len(all_ids) >= num_samples:
            break
    if not all_ids:
        raise RuntimeError(f"No calibration seqs with >= {seq_len} tokens")
    return torch.tensor(all_ids, dtype=torch.long, device=device)


def compute_ppl_batched(model, input_ids, seq_len, batch_size, device):
    total_loss = 0.0
    total_tokens = 0
    n = input_ids.shape[0]
    with torch.no_grad():
        for start in range(0, n, batch_size):
            end = min(start + batch_size, n)
            batch = input_ids[start:end]
            outputs = model(
                batch, use_cache=False,
                cache_position=torch.arange(seq_len, device=device)
            )
            shift_logits = outputs.logits[:, :-1].contiguous()
            shift_labels = batch[:, 1:].contiguous()
            loss = F.cross_entropy(
                shift_logits.float().view(-1, shift_logits.shape[-1]),
                shift_labels.view(-1),
                reduction="sum"
            )
            total_loss += loss.item()
            total_tokens += shift_labels.numel()
            del outputs, shift_logits, loss
            torch.cuda.empty_cache()
    return math.exp(total_loss / total_tokens)


def patch_attention_deepseek_v2(model, allocations):
    """Monkey-patch DeepSeek-V2 MLA attention for per-head KV quantization.
    Quantizes decompressed k_nope and value_states per head.
    k_pe (shared RoPE component) is not quantized."""
    config = model.config
    num_heads = config.num_attention_heads
    qk_nope_head_dim = config.qk_nope_head_dim
    qk_rope_head_dim = config.qk_rope_head_dim
    v_head_dim = config.v_head_dim
    kv_lora_rank = config.kv_lora_rank
    qk_head_dim = qk_nope_head_dim + qk_rope_head_dim

    original_forwards = {}

    for layer_idx, layer in enumerate(model.model.layers):
        attn = layer.self_attn

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

        def make_forward(orig_attn, h_allocs, n_heads=num_heads,
                         qk_nope_dim=qk_nope_head_dim, qk_rope_dim=qk_rope_head_dim,
                         v_dim=v_head_dim, kv_lr=kv_lora_rank, qk_dim=qk_head_dim):
            def compressed_forward(hidden_states, attention_mask=None,
                                   past_key_values=None, cache_position=None,
                                   position_embeddings=None, position_ids=None,
                                   **kwargs):
                bsz, seq_len_local = hidden_states.shape[:-1]
                query_shape = (bsz, seq_len_local, -1, qk_dim)
                key_shape = (bsz, seq_len_local, -1, qk_nope_dim + v_dim)

                if orig_attn.q_lora_rank is None:
                    q = orig_attn.q_proj(hidden_states)
                else:
                    q = orig_attn.q_b_proj(orig_attn.q_a_layernorm(orig_attn.q_a_proj(hidden_states)))
                q = q.view(query_shape).transpose(1, 2)
                q_nope, q_pe = torch.split(q, [qk_nope_dim, qk_rope_dim], dim=-1)

                compressed_kv = orig_attn.kv_a_proj_with_mqa(hidden_states)
                k_nope_latent, k_pe = torch.split(compressed_kv, [kv_lr, qk_rope_dim], dim=-1)
                k_nope = orig_attn.kv_b_proj(orig_attn.kv_a_layernorm(k_nope_latent))
                k_nope = k_nope.view(key_shape).transpose(1, 2)
                k_nope, value_states = torch.split(k_nope, [qk_nope_dim, v_dim], dim=-1)

                for h in range(n_heads):
                    atype, param = h_allocs[h]
                    if atype == "quant" and int(param) < 16:
                        bits = int(param)
                        k_nope[:, h] = quantize_per_channel(k_nope[:, h:h + 1], bits).squeeze(1)
                        value_states[:, h] = quantize_per_token(value_states[:, h:h + 1], bits).squeeze(1)

                k_pe = k_pe.view(bsz, 1, seq_len_local, qk_rope_dim)
                q_pe, k_pe = apply_rotary_emb(q_pe, k_pe, position_embeddings.to(q_pe.device))

                k_pe = k_pe.expand(*k_nope.shape[:-1], -1)
                query_states = torch.cat((q_nope, q_pe), dim=-1)
                key_states = torch.cat((k_nope, k_pe), dim=-1)

                scaling = qk_dim ** (-0.5)
                attn_weights = torch.matmul(query_states, key_states.transpose(2, 3)) * scaling

                if attention_mask is not None:
                    cm = attention_mask[:, :, :, :key_states.shape[-2]]
                    attn_weights = attn_weights + cm
                else:
                    causal = torch.triu(
                        torch.full((seq_len_local, seq_len_local), float("-inf"),
                                   device=attn_weights.device, dtype=attn_weights.dtype),
                        diagonal=1
                    )
                    attn_weights = attn_weights + causal

                attn_w = F.softmax(attn_weights, dim=-1, dtype=torch.float32).to(query_states.dtype)
                out = torch.matmul(attn_w, value_states)
                out = out.transpose(1, 2).reshape(bsz, seq_len_local, -1).contiguous()
                out = orig_attn.o_proj(out)

                return out, None

            return compressed_forward

        attn.forward = make_forward(attn, head_allocs)

    return original_forwards


def restore_attention_deepseek_v2(model, original_forwards):
    for layer_idx, fwd in original_forwards.items():
        model.model.layers[layer_idx].self_attn.forward = fwd


def profile_single_head(model, input_ids, seq_len, batch_size, device, baseline_ppl,
                        layer, head, bits):
    if bits >= 16:
        return 0.0
    allocations = {f"{layer},{head}": ["quant", bits]}
    orig_fwds = patch_attention_deepseek_v2(model, allocations)
    ppl = compute_ppl_batched(model, input_ids, seq_len, batch_size, device)
    restore_attention_deepseek_v2(model, orig_fwds)
    return ppl - baseline_ppl


def main():
    parser = argparse.ArgumentParser(description="DeepSeek-V2-Lite hires bf16 2-bit-only profiling")
    parser.add_argument("--model", type=str,
                        default="/root/autodl-tmp/.hf_cache/deepseek-ai/DeepSeek-V2-Lite")
    parser.add_argument("--calibration_data", type=str, default="calibration_hires.json")
    parser.add_argument("--gpu", type=str, default="cuda:0")
    parser.add_argument("--batch_size", type=int, default=1)
    parser.add_argument("--num_samples", type=int, default=64)
    parser.add_argument("--seq_len", type=int, default=2048)
    args = parser.parse_args()

    device = args.gpu
    t0 = time.time()

    config = AutoConfig.from_pretrained(args.model, trust_remote_code=True)
    num_layers = config.num_hidden_layers
    num_heads = config.num_attention_heads
    num_kv_heads = getattr(config, 'num_key_value_heads', num_heads)
    qk_nope_head_dim = config.qk_nope_head_dim
    qk_rope_head_dim = config.qk_rope_head_dim
    v_head_dim = config.v_head_dim
    kv_lora_rank = config.kv_lora_rank
    q_lora_rank = getattr(config, 'q_lora_rank', None)
    qk_head_dim = qk_nope_head_dim + qk_rope_head_dim
    total_kv_heads = num_layers * num_heads

    print(f"DeepSeek-V2-Lite (MLA): {num_layers}L x {num_heads} heads, {total_kv_heads} total")
    print(f"  qk_nope_head_dim={qk_nope_head_dim}, qk_rope_head_dim={qk_rope_head_dim}, "
          f"v_head_dim={v_head_dim}")
    print(f"  kv_lora_rank={kv_lora_rank}, q_lora_rank={q_lora_rank}")
    print(f"  hidden_size={config.hidden_size}")

    print("\n" + "=" * 60)
    print(f"BF16 2-bit-only Profiling ({args.num_samples}seq x {args.seq_len}tok)")
    print("=" * 60)

    profile_start = time.time()

    print(f"Loading model in bf16 to {device}...")
    tokenizer = AutoTokenizer.from_pretrained(args.model, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(
        args.model, torch_dtype=torch.bfloat16, attn_implementation="eager",
        trust_remote_code=True
    )
    model = model.to(device)
    model.eval()
    mem_gb = torch.cuda.memory_allocated(device) / 1e9
    print(f"BF16 model loaded. GPU mem: {mem_gb:.1f}GB")

    input_ids = load_calibration_data(tokenizer, args.calibration_data,
                                       args.num_samples, args.seq_len, device)
    print(f"Calibration: {input_ids.shape[0]} seqs x {input_ids.shape[1]} tokens")

    print("Computing baseline PPL...")
    baseline_ppl = compute_ppl_batched(model, input_ids, args.seq_len, args.batch_size, device)
    print(f"Baseline PPL: {baseline_ppl:.4f}")

    total_evals = total_kv_heads
    done = 0
    profiles = {}

    for l in range(num_layers):
        profiles[str(l)] = {}
        for h in range(num_heads):
            delta = profile_single_head(
                model, input_ids, args.seq_len, args.batch_size,
                device, baseline_ppl, l, h, 2
            )
            profiles[str(l)][str(h)] = {"quantization": {"2": delta}}
            done += 1
            elapsed = time.time() - profile_start
            eta_min = (elapsed / done) * (total_evals - done) / 60
            print(f"[{done}/{total_evals}] L{l}H{h} @2bit: delta={delta:.6f}  "
                  f"(elapsed {elapsed/60:.1f}min, ETA {eta_min:.0f}min)", flush=True)

    profile_time = time.time() - profile_start

    os.makedirs("artifacts", exist_ok=True)
    with open("artifacts/deepseekvl_profiles_hires.json", "w") as f:
        json.dump(profiles, f, indent=2)
    print(f"\nProfiling done in {profile_time / 60:.1f}min")

    # ========== Concentration Analysis ==========
    print("\n" + "=" * 60)
    print("Concentration Analysis")
    print("=" * 60)

    all_deltas = []
    layer_deltas = {}
    for l_str in sorted(profiles.keys(), key=int):
        l = int(l_str)
        layer_deltas[l] = []
        for h_str in sorted(profiles[l_str].keys(), key=int):
            d2 = profiles[l_str][h_str]["quantization"]["2"]
            all_deltas.append((l, int(h_str), d2))
            layer_deltas[l].append(d2)

    sorted_by_d2 = sorted(all_deltas, key=lambda x: -x[2])
    n_top5 = max(1, int(len(sorted_by_d2) * 0.05))
    total_sum = sum(x[2] for x in all_deltas)
    top5_sum = sum(x[2] for x in sorted_by_d2[:n_top5])
    concentration = top5_sum / total_sum if total_sum > 0 else 0

    top1_delta = sorted_by_d2[0][2]
    t1_t5 = top1_delta / top5_sum if top5_sum > 0 else float("inf")

    l0_deltas = layer_deltas.get(0, [0])
    l0_mean = sum(l0_deltas) / max(len(l0_deltas), 1)
    other_means = [sum(layer_deltas[l]) / len(layer_deltas[l])
                   for l in range(1, num_layers) if l in layer_deltas and layer_deltas[l]]
    other_avg = sum(other_means) / len(other_means) if other_means else 0
    l0_ratio = l0_mean / other_avg if other_avg > 0 else float("inf")

    d_tensor = torch.tensor([x[2] for x in all_deltas])
    n_positive = int((d_tensor > 1e-6).sum().item())
    cv = d_tensor.std().item() / d_tensor.mean().item() if d_tensor.mean().item() > 0 else 0

    print(f"Top-5% concentration: {concentration:.4f} ({n_top5} heads)")
    print(f"t1/t5 ratio: {t1_t5:.4f}")
    print(f"Top-1: L{sorted_by_d2[0][0]}H{sorted_by_d2[0][1]} delta={sorted_by_d2[0][2]:.6f}")
    for i in range(min(10, len(sorted_by_d2))):
        l_i, h_i, d = sorted_by_d2[i]
        print(f"  Top-{i+1}: L{l_i}H{h_i} delta={d:.6f}")
    print(f"L0 dominance ratio: {l0_ratio:.2f}x")
    print(f"Positive delta heads: {n_positive}/{len(all_deltas)}")
    print(f"CV of delta(2bit): {cv:.4f}")

    shape = "Spread" if concentration >= 0.50 and t1_t5 <= 0.70 else \
            "Spike" if t1_t5 > 0.70 else "Flat"
    print(f"\nDiagnostic: concentration={concentration:.4f}, t1/t5={t1_t5:.4f} -> {shape}")
    print(f"\nNOTE: MLA quantizes decompressed k_nope/value per head. "
          f"k_pe (shared RoPE) is not quantized. "
          f"kv_lora_rank={kv_lora_rank} → compression ratio "
          f"= {kv_lora_rank}/{num_heads * (qk_nope_head_dim + v_head_dim)}")

    # ========== Save Results ==========
    total_time = time.time() - t0

    results = {
        "model": args.model,
        "model_name": "DeepSeek-V2-Lite",
        "precision": "bfloat16",
        "profiling_config": {
            "num_samples": args.num_samples,
            "seq_len": args.seq_len,
            "batch_size": args.batch_size,
            "bitwidths": [2],
        },
        "architecture": {
            "num_layers": num_layers,
            "num_attention_heads": num_heads,
            "num_key_value_heads": num_kv_heads,
            "qk_nope_head_dim": qk_nope_head_dim,
            "qk_rope_head_dim": qk_rope_head_dim,
            "qk_head_dim": qk_head_dim,
            "v_head_dim": v_head_dim,
            "kv_lora_rank": kv_lora_rank,
            "q_lora_rank": q_lora_rank,
            "hidden_size": config.hidden_size,
            "total_kv_heads": total_kv_heads,
            "attention_type": "MLA",
        },
        "baseline_calibration_ppl": baseline_ppl,
        "analysis": {
            "top5_concentration": round(concentration, 4),
            "top5_n_heads": n_top5,
            "t1_t5": round(t1_t5, 4),
            "shape": shape,
            "layer0_mean_delta_2bit": round(l0_mean, 6),
            "other_layers_mean_delta_2bit": round(other_avg, 6),
            "layer0_dominance_ratio": round(l0_ratio, 2),
            "delta_2bit_mean": round(d_tensor.mean().item(), 6),
            "delta_2bit_std": round(d_tensor.std().item(), 6),
            "delta_2bit_cv": round(cv, 4),
            "heads_with_positive_delta": n_positive,
            "total_heads": len(all_deltas),
        },
        "top10_heads": [
            {"layer": l, "head": h, "delta_2bit": round(d, 6)}
            for l, h, d in sorted_by_d2[:10]
        ],
        "timing": {
            "profile_seconds": round(profile_time, 1),
            "total_seconds": round(total_time, 1),
        },
    }

    results_path = "artifacts/deepseekvl_hires_profiling_results.json"
    with open(results_path, "w") as f:
        json.dump(results, f, indent=2)

    print(f"\nTotal elapsed: {total_time / 60:.1f}min")
    print(f"Saved: artifacts/deepseekvl_profiles_hires.json, {results_path}")


if __name__ == "__main__":
    main()
