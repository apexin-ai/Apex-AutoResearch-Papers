"""Falcon-7B hires bf16 profiling — 2-bit only concentration measurement.

MQA (Multi-Query Attention): 71 query heads share 1 KV head per layer.
32 layers × 1 KV head = 32 total heads — profiling completes in ~30min.
Architecture: model.transformer.h[i].self_attention, fused query_key_value, dense output.
Requires custom attention patching (eval_ppl.patch_attention assumes LLaMA structure).

Input:  calibration_hires.json (64 seqs × 2048 tok)
Output: artifacts/falcon7b_profiles_hires.json
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
from transformers.models.falcon.modeling_falcon import apply_rotary_pos_emb
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


def patch_attention_falcon(model, allocations):
    """Monkey-patch Falcon attention for per-head KV quantization.
    Handles fused QKV (query_key_value), MQA broadcasting, and dense output."""
    config = model.config
    num_q_heads = config.num_attention_heads
    head_dim = config.hidden_size // num_q_heads
    if getattr(config, 'new_decoder_architecture', False):
        num_kv_heads = getattr(config, 'num_kv_heads', num_q_heads)
    elif getattr(config, 'multi_query', False):
        num_kv_heads = 1
    else:
        num_kv_heads = getattr(config, 'num_kv_heads', num_q_heads)

    original_forwards = {}

    for layer_idx, layer in enumerate(model.transformer.h):
        attn = layer.self_attention

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

        def make_forward(orig_attn, h_allocs, n_q=num_q_heads, n_kv=num_kv_heads,
                         hd=head_dim, rope_fn=apply_rotary_pos_emb):
            def compressed_forward(hidden_states, alibi=None, attention_mask=None,
                                   position_ids=None, layer_past=None, head_mask=None,
                                   use_cache=False, output_attentions=False,
                                   cache_position=None, position_embeddings=None):
                bsz, seq_len_local = hidden_states.shape[:2]

                fused_qkv = orig_attn.query_key_value(hidden_states)
                query_layer, key_layer, value_layer = orig_attn._split_heads(fused_qkv)

                query_layer = query_layer.transpose(1, 2).reshape(bsz, n_q, seq_len_local, hd)
                key_layer = key_layer.transpose(1, 2).reshape(bsz, n_kv, seq_len_local, hd)
                value_layer = value_layer.transpose(1, 2).reshape(bsz, n_kv, seq_len_local, hd)

                if alibi is None and position_embeddings is not None:
                    cos, sin = position_embeddings
                    query_layer, key_layer = rope_fn(query_layer, key_layer, cos, sin)

                for h in range(n_kv):
                    atype, param = h_allocs[h]
                    if atype == "quant" and int(param) < 16:
                        bits = int(param)
                        key_layer[:, h] = quantize_per_channel(key_layer[:, h:h + 1], bits).squeeze(1)
                        value_layer[:, h] = quantize_per_token(value_layer[:, h:h + 1], bits).squeeze(1)

                scale = 1.0 / math.sqrt(hd)
                attn_scores = torch.matmul(query_layer, key_layer.transpose(-1, -2)) * scale

                if attention_mask is not None:
                    cm = attention_mask[:, :, :, :key_layer.shape[-2]]
                    attn_scores = attn_scores + cm
                else:
                    causal = torch.triu(
                        torch.full((seq_len_local, seq_len_local), float("-inf"),
                                   device=attn_scores.device, dtype=attn_scores.dtype),
                        diagonal=1
                    )
                    attn_scores = attn_scores + causal

                attn_w = F.softmax(attn_scores, dim=-1, dtype=torch.float32).to(query_layer.dtype)
                out = torch.matmul(attn_w, value_layer)

                out = out.transpose(1, 2).contiguous().reshape(bsz, seq_len_local, n_q * hd)
                out = orig_attn.dense(out)

                return (out,)

            return compressed_forward

        attn.forward = make_forward(attn, head_allocs)

    return original_forwards


def restore_attention_falcon(model, original_forwards):
    for layer_idx, fwd in original_forwards.items():
        model.transformer.h[layer_idx].self_attention.forward = fwd


def profile_single_head(model, input_ids, seq_len, batch_size, device, baseline_ppl,
                        layer, head, bits):
    if bits >= 16:
        return 0.0
    allocations = {f"{layer},{head}": ["quant", bits]}
    orig_fwds = patch_attention_falcon(model, allocations)
    ppl = compute_ppl_batched(model, input_ids, seq_len, batch_size, device)
    restore_attention_falcon(model, orig_fwds)
    return ppl - baseline_ppl


def main():
    parser = argparse.ArgumentParser(description="Falcon-7B hires bf16 2-bit-only profiling")
    parser.add_argument("--model", type=str,
                        default="/root/autodl-tmp/.hf_cache/tiiuae/falcon-7b")
    parser.add_argument("--calibration_data", type=str, default="calibration_hires.json")
    parser.add_argument("--gpu", type=str, default="cuda:0")
    parser.add_argument("--batch_size", type=int, default=2)
    parser.add_argument("--num_samples", type=int, default=64)
    parser.add_argument("--seq_len", type=int, default=2048)
    args = parser.parse_args()

    device = args.gpu
    t0 = time.time()

    config = AutoConfig.from_pretrained(args.model, trust_remote_code=True)
    num_layers = config.num_hidden_layers
    num_q_heads = config.num_attention_heads
    head_dim = config.hidden_size // num_q_heads
    if getattr(config, 'new_decoder_architecture', False):
        num_kv_heads = getattr(config, 'num_kv_heads', num_q_heads)
    elif getattr(config, 'multi_query', False):
        num_kv_heads = 1
    else:
        num_kv_heads = getattr(config, 'num_kv_heads', num_q_heads)
    gqa_ratio = num_q_heads // num_kv_heads
    total_kv_heads = num_layers * num_kv_heads

    print(f"Falcon-7B: {num_layers}L x {num_kv_heads}KV (MQA), "
          f"{num_q_heads}Q, ratio {gqa_ratio}:1, {total_kv_heads} total KV heads")
    print(f"head_dim={head_dim}, hidden_size={config.hidden_size}")

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
    with open("artifacts/falcon7b_profiles_hires.json", "w") as f:
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
    print(f"\nNOTE: Falcon-7B MQA has only {total_kv_heads} KV heads — "
          f"each head is shared by {gqa_ratio} query heads, "
          f"quantization impact per head may be amplified.")

    # ========== Save Results ==========
    total_time = time.time() - t0

    results = {
        "model": args.model,
        "model_name": "Falcon-7B",
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
            "head_dim": head_dim,
            "hidden_size": config.hidden_size,
            "gqa_ratio": gqa_ratio,
            "total_kv_heads": total_kv_heads,
            "attention_type": "MQA",
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

    results_path = "artifacts/falcon7b_hires_profiling_results.json"
    with open(results_path, "w") as f:
        json.dump(results, f, indent=2)

    print(f"\nTotal elapsed: {total_time / 60:.1f}min")
    print(f"Saved: artifacts/falcon7b_profiles_hires.json, {results_path}")


if __name__ == "__main__":
    main()
