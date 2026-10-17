"""InternLM2-7B hires bf16 profiling — 2-bit only concentration measurement.
Custom attention patching for InternLM2's fused wqkv architecture.
64 samples x 2048 tokens, bfloat16 precision, only 2-bit quantization deltas.
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
from einops import rearrange
from transformers import AutoModelForCausalLM, AutoTokenizer, AutoConfig
from utils import quantize_per_channel, quantize_per_token, repeat_kv


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

        all_full = all(a[0] == "full" for a in head_allocs.values())
        if all_full:
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


def profile_single_head(model, input_ids, seq_len, batch_size, device, baseline_ppl, layer, head, bits):
    if bits >= 16:
        return 0.0
    allocations = {f"{layer},{head}": ["quant", bits]}
    orig_fwds = patch_attention_internlm2(model, allocations)
    ppl = compute_ppl_batched(model, input_ids, seq_len, batch_size, device)
    restore_attention_internlm2(model, orig_fwds)
    return ppl - baseline_ppl


def main():
    parser = argparse.ArgumentParser(description="InternLM2-7B hires bf16 2-bit-only profiling")
    parser.add_argument("--model", type=str, default="/root/autodl-tmp/.hf_cache/Shanghai_AI_Laboratory/internlm2-7b")
    parser.add_argument("--calibration_data", type=str, default="calibration_hires.json")
    parser.add_argument("--gpu", type=str, default="cuda:1")
    parser.add_argument("--batch_size", type=int, default=2)
    parser.add_argument("--num_samples", type=int, default=64)
    parser.add_argument("--seq_len", type=int, default=2048)
    args = parser.parse_args()

    device = args.gpu
    t0 = time.time()

    config = AutoConfig.from_pretrained(args.model, trust_remote_code=True)
    num_layers = config.num_hidden_layers
    num_kv_heads = config.num_key_value_heads
    num_q_heads = config.num_attention_heads
    gqa_ratio = num_q_heads // num_kv_heads
    total_kv_heads = num_layers * num_kv_heads

    print(f"InternLM2-7B: {num_layers}L x {num_kv_heads}KV, GQA {gqa_ratio}:1, {total_kv_heads} total heads")

    print("\n" + "=" * 60)
    print(f"BF16 2-bit-only Profiling ({args.num_samples}seq x {args.seq_len}tok)")
    print("=" * 60)

    profile_start = time.time()

    print(f"Loading model in bf16 to {device}...")
    tokenizer = AutoTokenizer.from_pretrained(args.model, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(
        args.model, torch_dtype=torch.bfloat16,
        attn_implementation="eager", trust_remote_code=True
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
        for h in range(num_kv_heads):
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
    with open("artifacts/internlm2_profiles_hires.json", "w") as f:
        json.dump(profiles, f, indent=2)
    print(f"\nProfiling done in {profile_time / 60:.1f}min")

    # ========== Concentration Analysis ==========
    print("\n" + "=" * 60)
    print("Concentration Analysis")
    print("=" * 60)

    all_deltas_2bit = []
    layer_deltas = {}
    for l_str in sorted(profiles.keys(), key=int):
        l = int(l_str)
        layer_deltas[l] = []
        for h_str in sorted(profiles[l_str].keys(), key=int):
            d2 = profiles[l_str][h_str]["quantization"].get("2", 0.0)
            all_deltas_2bit.append((l, int(h_str), d2))
            layer_deltas[l].append(d2)

    sorted_by_d2 = sorted(all_deltas_2bit, key=lambda x: -x[2])
    n_top5 = max(1, int(len(sorted_by_d2) * 0.05))
    total_sum = sum(x[2] for x in all_deltas_2bit)
    top5_sum = sum(x[2] for x in sorted_by_d2[:n_top5])
    top5_concentration = top5_sum / total_sum if total_sum > 0 else 0

    l0_deltas = layer_deltas.get(0, [0])
    l0_mean = sum(l0_deltas) / max(len(l0_deltas), 1)
    other_means = []
    for l in range(1, num_layers):
        if l in layer_deltas and layer_deltas[l]:
            other_means.append(sum(layer_deltas[l]) / len(layer_deltas[l]))
    other_avg = sum(other_means) / len(other_means) if other_means else 0
    l0_ratio = l0_mean / other_avg if other_avg > 0 else float("inf")

    d_tensor = torch.tensor([x[2] for x in all_deltas_2bit])
    n_positive = int((d_tensor > 1e-6).sum().item())
    cv = d_tensor.std().item() / d_tensor.mean().item() if d_tensor.mean().item() > 0 else 0

    print(f"Top-5% concentration: {top5_concentration:.4f} ({n_top5} heads)")
    print(f"Layer 0 mean delta(2bit): {l0_mean:.6f}")
    print(f"Other layers mean delta(2bit): {other_avg:.6f}")
    print(f"L0 dominance ratio: {l0_ratio:.2f}x")
    print(f"Heads with positive delta: {n_positive}/{len(all_deltas_2bit)}")
    print(f"CV of delta(2bit): {cv:.4f}")

    print("\nTop-5 most sensitive heads:")
    for name_l, name_h, d2 in sorted_by_d2[:5]:
        print(f"  L{name_l}H{name_h}: 2bit={d2:+.4f}")

    # ========== Save Results ==========
    total_time = time.time() - t0

    results = {
        "model": args.model,
        "model_name": "InternLM2-7B",
        "precision": "bfloat16",
        "profiling_config": {
            "num_samples": args.num_samples,
            "seq_len": args.seq_len,
            "batch_size": args.batch_size,
            "bitwidths": [2],
        },
        "architecture": {
            "num_layers": num_layers,
            "num_kv_heads": num_kv_heads,
            "num_attention_heads": num_q_heads,
            "head_dim": config.hidden_size // num_q_heads,
            "hidden_size": config.hidden_size,
            "gqa_ratio": gqa_ratio,
            "total_kv_heads": total_kv_heads,
        },
        "baseline_calibration_ppl": baseline_ppl,
        "analysis": {
            "top5_concentration": round(top5_concentration, 4),
            "top5_n_heads": n_top5,
            "layer0_mean_delta_2bit": round(l0_mean, 6),
            "other_layers_mean_delta_2bit": round(other_avg, 6),
            "layer0_dominance_ratio": round(l0_ratio, 2),
            "delta_2bit_mean": round(d_tensor.mean().item(), 6),
            "delta_2bit_std": round(d_tensor.std().item(), 6),
            "delta_2bit_cv": round(cv, 4),
            "heads_with_positive_delta": n_positive,
            "total_heads": len(all_deltas_2bit),
        },
        "top5_sensitive_heads": [
            {"layer": l, "head": h, "delta_2bit": round(d2, 6)}
            for l, h, d2 in sorted_by_d2[:5]
        ],
        "timing": {
            "profile_seconds": round(profile_time, 1),
            "total_seconds": round(total_time, 1),
        },
    }

    with open("artifacts/internlm2_hires_bf16_2bitonly_results.json", "w") as f:
        json.dump(results, f, indent=2)

    print(f"\nTotal time: {total_time / 3600:.2f}h")
    print(f"Saved: artifacts/internlm2_profiles_hires.json, artifacts/internlm2_hires_bf16_2bitonly_results.json")


if __name__ == "__main__":
    main()
