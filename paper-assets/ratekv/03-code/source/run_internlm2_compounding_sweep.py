"""InternLM2-7B compounding sweep — measure super-additivity of 2-bit deltas.

Architecture: 32 layers x 8 KV heads (GQA), 256 total KV heads.
Progressively apply 2-bit quantization to increasing numbers of heads
(sorted by individual delta, most sensitive first) and measure joint PPL.

InternLM2 uses fused wqkv projection — custom patch_attention_internlm2 handles
the QKV splitting: [Q_groups (ng dims), K (2nd-to-last), V (last)].
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
from transformers import AutoModelForCausalLM, AutoTokenizer
from utils import quantize_per_channel, quantize_per_token, repeat_kv

MODEL_PATH = "/root/autodl-tmp/.hf_cache/Shanghai_AI_Laboratory/internlm2-7b"
PROFILE_PATH = "artifacts/internlm2_profiles_hires.json"
OUTPUT_PATH = "artifacts/internlm2_compounding_sweep.json"


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


def main():
    parser = argparse.ArgumentParser(description="InternLM2-7B compounding sweep")
    parser.add_argument("--gpu", type=str, default="cuda:0")
    parser.add_argument("--num_samples", type=int, default=64)
    parser.add_argument("--seq_len", type=int, default=2048)
    parser.add_argument("--batch_size", type=int, default=2)
    parser.add_argument("--calibration_data", type=str, default="calibration_hires.json")
    args = parser.parse_args()

    device = args.gpu
    k_values = [0, 2, 4, 8, 16, 32, 64, 128, 256]
    t0 = time.time()

    print("Loading profiles...")
    with open(PROFILE_PATH) as f:
        raw = json.load(f)
    profiles = raw["profiles"] if "profiles" in raw else raw

    head_deltas = []
    for l_str in sorted(profiles.keys(), key=int):
        for h_str in sorted(profiles[l_str].keys(), key=int):
            d2 = profiles[l_str][h_str]["quantization"].get("2", 0.0)
            head_deltas.append({
                "layer": int(l_str),
                "head": int(h_str),
                "key": f"{l_str},{h_str}",
                "delta_2bit": d2,
            })
    head_deltas.sort(key=lambda x: x["delta_2bit"], reverse=True)

    total_kv_heads = len(head_deltas)
    k_values = [k for k in k_values if k <= total_kv_heads]
    print(f"Total KV heads: {total_kv_heads}")
    print(f"Sweep k values: {k_values}")
    print(f"Top-5: {[(h['key'], round(h['delta_2bit'], 4)) for h in head_deltas[:5]]}")

    print(f"\nLoading {MODEL_PATH} in bf16 to {device}...")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_PATH, torch_dtype=torch.bfloat16,
        attn_implementation="eager", trust_remote_code=True
    )
    model = model.to(device)
    model.eval()
    print(f"GPU mem: {torch.cuda.memory_allocated(device) / 1e9:.1f}GB")

    print(f"Loading calibration data ({args.num_samples} x {args.seq_len})...")
    input_ids = load_calibration_data(
        tokenizer, args.calibration_data,
        args.num_samples, args.seq_len, device)
    print(f"Loaded {input_ids.shape[0]} sequences")

    print("\nMeasuring baseline PPL...")
    baseline_ppl = compute_ppl_batched(
        model, input_ids, args.seq_len, args.batch_size, device)
    print(f"Baseline PPL: {baseline_ppl:.4f}")

    results = []
    for k in k_values:
        print(f"\n--- k={k} ---")
        if k == 0:
            print(f"  baseline (no 2-bit heads): {baseline_ppl:.4f}")
            results.append({
                "k": 0,
                "heads": [],
                "sum_individual_delta": 0.0,
                "joint_ppl": round(baseline_ppl, 4),
                "joint_delta": 0.0,
                "predicted_ppl": round(baseline_ppl, 4),
                "super_additive_ratio": 1.0,
            })
            continue

        top_k = head_deltas[:k]
        allocation = {h["key"]: ["quant", 2] for h in top_k}
        sum_individual = sum(h["delta_2bit"] for h in top_k)

        orig_fwds = patch_attention_internlm2(model, allocation)
        joint_ppl = compute_ppl_batched(
            model, input_ids, args.seq_len, args.batch_size, device)
        restore_attention_internlm2(model, orig_fwds)

        joint_delta = joint_ppl - baseline_ppl
        predicted_ppl = baseline_ppl + sum_individual
        ratio = joint_delta / sum_individual if sum_individual > 0 else float('nan')

        print(f"  sum_indiv={sum_individual:.4f}  joint={joint_ppl:.4f}  "
              f"pred={predicted_ppl:.4f}  ratio={ratio:.4f}")

        results.append({
            "k": k,
            "heads": [h["key"] for h in top_k],
            "sum_individual_delta": round(sum_individual, 6),
            "joint_ppl": round(joint_ppl, 4),
            "joint_delta": round(joint_delta, 6),
            "predicted_ppl": round(predicted_ppl, 4),
            "super_additive_ratio": round(ratio, 4),
        })

    elapsed = time.time() - t0

    output = {
        "experiment": "internlm2_compounding_sweep",
        "model": MODEL_PATH,
        "model_name": "InternLM2-7B",
        "baseline_ppl_measured": round(baseline_ppl, 4),
        "calibration": {
            "path": args.calibration_data,
            "num_samples": args.num_samples,
            "seq_len": args.seq_len,
        },
        "total_kv_heads": total_kv_heads,
        "results": results,
        "top_heads": [
            {"key": h["key"], "delta_2bit": round(h["delta_2bit"], 6)}
            for h in head_deltas[:10]
        ],
        "timing_seconds": round(elapsed, 1),
    }

    os.makedirs("artifacts", exist_ok=True)
    with open(OUTPUT_PATH, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nJSON saved to {OUTPUT_PATH}")

    print(f"\n{'='*70}")
    print("COMPOUNDING SWEEP — InternLM2-7B (256 KV heads)")
    print(f"{'='*70}")
    print(f"{'k':>5}  {'sum_indiv':>10}  {'joint_ppl':>10}  {'pred_ppl':>10}  {'ratio':>8}")
    print("-" * 70)
    for r in results:
        print(f"{r['k']:>5}  {r['sum_individual_delta']:>10.4f}  "
              f"{r['joint_ppl']:>10.4f}  {r['predicted_ppl']:>10.4f}  "
              f"{r['super_additive_ratio']:>8.4f}")
    print(f"\nTotal time: {elapsed/60:.1f}min")


if __name__ == "__main__":
    main()
