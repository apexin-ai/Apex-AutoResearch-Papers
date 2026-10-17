"""KIVI + MCKP orthogonality test on Qwen2.5-7B (cuda:1).

Goal: prove KIVI (intra-head) and MCKP (inter-head) are orthogonal and complementary.
  - KIVI = asymmetric min-max quantization with group_size + residual_length
  - MCKP = per-head bit allocation via constrained knapsack solver

Input:
  - hires_profiles.json: per-head distortion profiles for MCKP solver
  - Qwen/Qwen2.5-7B model weights

Output:
  - artifacts/kivi_mckp_combined_results.json

Conditions compared:
  1. BF16 baseline (no quantization)
  2. KIVI alone: uniform 4-bit, KIVI quantization, all heads same
  3. MCKP alone: mixed 2/4/8-bit, simple symmetric quantization
  4. KIVI + MCKP: mixed 2/4/8-bit, KIVI asymmetric grouped quantization
"""

import os
os.environ["HF_HOME"] = "/root/autodl-tmp/.hf_cache"
os.environ["HF_DATASETS_OFFLINE"] = "1"
os.environ["TRANSFORMERS_OFFLINE"] = "1"
os.environ["HF_HUB_OFFLINE"] = "1"

import json
import math
import time
import importlib
import torch
import torch.nn.functional as F
from transformers import AutoModelForCausalLM, AutoTokenizer, AutoConfig
from solver import solve_mckp_constrained, enforce_monotonicity


# ---------------------------------------------------------------------------
# KIVI quantization functions (asymmetric min-max, grouped)
# ---------------------------------------------------------------------------

def kivi_quantize_k(k, bits, group_size):
    """Asymmetric per-channel quantization for K cache.
    K shape: (B, nh, T, D). Groups along T with group_size.
    """
    B, nh, T, D = k.shape
    if T == 0:
        return k
    max_int = 2 ** bits - 1
    pad = (group_size - T % group_size) % group_size
    if pad > 0:
        k = F.pad(k, (0, 0, 0, pad))
    T_padded = k.shape[2]
    k = k.reshape(B, nh, T_padded // group_size, group_size, D)
    mn = k.min(dim=3, keepdim=True)[0]
    mx = k.max(dim=3, keepdim=True)[0]
    scale = ((mx - mn) / max_int).clamp(min=1e-10)
    k = ((k - mn) / scale).clamp(0, max_int).round() * scale + mn
    k = k.reshape(B, nh, T_padded, D)
    if pad > 0:
        k = k[:, :, :T_padded - pad, :]
    return k


def kivi_quantize_v(v, bits, group_size):
    """Asymmetric per-token quantization for V cache.
    V shape: (B, nh, T, D). Groups along D with group_size.
    """
    B, nh, T, D = v.shape
    if T == 0:
        return v
    max_int = 2 ** bits - 1
    pad = (group_size - D % group_size) % group_size
    if pad > 0:
        v = F.pad(v, (0, pad))
    D_padded = v.shape[3]
    v = v.reshape(B, nh, T, D_padded // group_size, group_size)
    mn = v.min(dim=4, keepdim=True)[0]
    mx = v.max(dim=4, keepdim=True)[0]
    scale = ((mx - mn) / max_int).clamp(min=1e-10)
    v = ((v - mn) / scale).clamp(0, max_int).round() * scale + mn
    v = v.reshape(B, nh, T, D_padded)
    if pad > 0:
        v = v[:, :, :, :D_padded - pad]
    return v


# ---------------------------------------------------------------------------
# Simple symmetric quantization (baseline MCKP uses these)
# ---------------------------------------------------------------------------

def simple_quantize_per_channel(tensor, bits):
    qmax = 2 ** (bits - 1) - 1
    abs_max = tensor.abs().amax(dim=-2, keepdim=True).clamp(min=1e-8)
    scale = abs_max / qmax
    return (tensor / scale).round().clamp(-qmax - 1, qmax) * scale


def simple_quantize_per_token(tensor, bits):
    qmax = 2 ** (bits - 1) - 1
    abs_max = tensor.abs().amax(dim=-1, keepdim=True).clamp(min=1e-8)
    scale = abs_max / qmax
    return (tensor / scale).round().clamp(-qmax - 1, qmax) * scale


# ---------------------------------------------------------------------------
# Attention patching
# ---------------------------------------------------------------------------

def _get_rotary_fn(model):
    model_type = model.config.model_type
    module_name = f"transformers.models.{model_type}.modeling_{model_type}"
    module = importlib.import_module(module_name)
    return module.apply_rotary_pos_emb


def repeat_kv(hidden_states, n_rep):
    if n_rep == 1:
        return hidden_states
    batch, n_kv, seq_len, head_dim = hidden_states.shape
    hidden_states = hidden_states[:, :, None, :, :].expand(batch, n_kv, n_rep, seq_len, head_dim)
    return hidden_states.reshape(batch, n_kv * n_rep, seq_len, head_dim)


def patch_attention_combined(model, allocations, group_size, residual_length, use_kivi):
    """Patch attention with per-head bit allocation.

    If use_kivi=True: KIVI asymmetric grouped quantization + residual
    If use_kivi=False: simple symmetric per-channel/per-token (original MCKP)
    """
    config = model.config
    num_kv_heads = config.num_key_value_heads
    num_q_heads = config.num_attention_heads
    head_dim = config.hidden_size // num_q_heads
    n_groups = num_q_heads // num_kv_heads
    rotary_fn = _get_rotary_fn(model)
    original_forwards = {}

    for layer_idx, layer in enumerate(model.model.layers):
        attn = layer.self_attn

        head_allocs = {}
        for h in range(num_kv_heads):
            key = f"{layer_idx},{h}"
            if key in allocations:
                atype, param = allocations[key]
                head_allocs[h] = (atype, int(param) if atype == "quant" else param)
            else:
                head_allocs[h] = ("full", 16)

        all_full = all(a[0] == "full" or (a[0] == "quant" and a[1] >= 16) for a in head_allocs.values())
        if all_full:
            continue

        original_forwards[layer_idx] = attn.forward

        def make_forward(orig_attn, h_allocs, n_kv=num_kv_heads, ng=n_groups,
                         hd=head_dim, rope_fn=rotary_fn, gs=group_size,
                         rl=residual_length, kivi=use_kivi):
            def combined_forward(hidden_states, position_embeddings, attention_mask=None, **kwargs):
                bsz, seq_len = hidden_states.shape[:2]

                q = orig_attn.q_proj(hidden_states).view(bsz, seq_len, -1, hd).transpose(1, 2)
                k = orig_attn.k_proj(hidden_states).view(bsz, seq_len, n_kv, hd).transpose(1, 2)
                v = orig_attn.v_proj(hidden_states).view(bsz, seq_len, n_kv, hd).transpose(1, 2)

                cos, sin = position_embeddings
                q, k = rope_fn(q, k, cos, sin)

                for h in range(n_kv):
                    atype, bits = h_allocs[h]
                    if atype != "quant" or bits >= 16:
                        continue

                    if kivi:
                        T = k.shape[2]
                        quant_len = T - rl if T > rl else 0
                        quant_len = (quant_len // gs) * gs
                        if quant_len > 0:
                            k_h = k[:, h:h+1, :, :]
                            v_h = v[:, h:h+1, :, :]
                            k_q = kivi_quantize_k(k_h[:, :, :quant_len], bits, gs)
                            k[:, h:h+1] = torch.cat([k_q, k_h[:, :, quant_len:]], dim=2)
                            v_q = kivi_quantize_v(v_h[:, :, :quant_len], bits, gs)
                            v[:, h:h+1] = torch.cat([v_q, v_h[:, :, quant_len:]], dim=2)
                    else:
                        k[:, h] = simple_quantize_per_channel(k[:, h:h+1], bits).squeeze(1)
                        v[:, h] = simple_quantize_per_token(v[:, h:h+1], bits).squeeze(1)

                k_exp = repeat_kv(k, ng)
                v_exp = repeat_kv(v, ng)

                attn_scores = torch.matmul(q, k_exp.transpose(2, 3)) * orig_attn.scaling
                if attention_mask is not None:
                    cm = attention_mask[:, :, :, :k_exp.shape[-2]]
                    attn_scores = attn_scores + cm
                else:
                    causal = torch.triu(
                        torch.full((seq_len, seq_len), float("-inf"),
                                   device=attn_scores.device, dtype=attn_scores.dtype),
                        diagonal=1,
                    )
                    attn_scores = attn_scores + causal

                attn_w = F.softmax(attn_scores, dim=-1, dtype=torch.float32).to(q.dtype)
                out = torch.matmul(attn_w, v_exp)
                out = out.transpose(1, 2).contiguous().reshape(bsz, seq_len, -1)
                out = orig_attn.o_proj(out)
                return out, attn_w

            return combined_forward

        attn.forward = make_forward(attn, head_allocs)

    return original_forwards


def patch_kivi_uniform(model, bits, group_size, residual_length):
    """KIVI uniform: all heads same bit-width with KIVI quantization."""
    config = model.config
    num_kv_heads = config.num_key_value_heads
    num_layers = config.num_hidden_layers
    alloc = {}
    for l in range(num_layers):
        for h in range(num_kv_heads):
            alloc[f"{l},{h}"] = ("quant", bits)
    return patch_attention_combined(model, alloc, group_size, residual_length, use_kivi=True)


def restore_attention(model, original_forwards):
    for layer_idx, fwd in original_forwards.items():
        model.model.layers[layer_idx].self_attn.forward = fwd


# ---------------------------------------------------------------------------
# Perplexity evaluation (WikiText-2)
# ---------------------------------------------------------------------------

def evaluate_perplexity(model, tokenizer, device, stride=512):
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

    print(f"Evaluating on {total_len} tokens, stride={stride}, {n_chunks} chunks")

    for i, begin in enumerate(range(0, total_len - 1, stride)):
        end = min(begin + stride, total_len)
        chunk = input_ids[:, begin:end]

        with torch.no_grad():
            outputs = model(chunk, use_cache=False,
                            cache_position=torch.arange(chunk.shape[1], device=chunk.device))
            logits = outputs.logits

        shift_logits = logits[:, :-1].contiguous()
        shift_labels = chunk[:, 1:].contiguous()

        loss = F.cross_entropy(
            shift_logits.float().view(-1, shift_logits.shape[-1]),
            shift_labels.view(-1),
            reduction="sum",
        )
        total_loss += loss.item()
        total_tokens += shift_labels.numel()

        if (i + 1) % 50 == 0:
            print(f"  chunk {i + 1}/{n_chunks}, running ppl={math.exp(total_loss / total_tokens):.2f}")

    ppl = math.exp(total_loss / total_tokens)
    return ppl


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    device = "cuda:1"
    model_name = "/root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-7B"
    profiles_path = "hires_profiles.json"
    output_path = "artifacts/kivi_mckp_combined_results.json"
    budget = 0.25
    max_2bit = 8
    group_size = 32
    residual_length = 128
    t0 = time.time()

    config = AutoConfig.from_pretrained(model_name)
    num_layers = config.num_hidden_layers
    num_kv_heads = config.num_key_value_heads
    total_kv_heads = num_layers * num_kv_heads
    print(f"Qwen2.5-7B: {num_layers}L x {num_kv_heads}KV, {total_kv_heads} total heads")

    # ---- MCKP allocation ----
    print(f"\nLoading profiles from {profiles_path}...")
    with open(profiles_path) as f:
        raw = json.load(f)
    profiles_raw = raw["profiles"] if "profiles" in raw else raw
    profiles = enforce_monotonicity(profiles_raw)

    print(f"Running constrained MCKP (max_2bit={max_2bit}, budget={budget})...")
    mckp_result = solve_mckp_constrained(
        profiles, budget, mode="quant_only",
        max_2bit=max_2bit, l0_exclude_2bit=True)

    bit_counts = {}
    for key, (atype, param) in mckp_result["allocation"].items():
        b = int(param) if atype == "quant" else 16
        bit_counts[b] = bit_counts.get(b, 0) + 1
    print(f"Bit distribution: {bit_counts}")
    print(f"Memory ratio: {mckp_result['actual_memory_ratio']:.4f}")

    # ---- Load model ----
    print(f"\nLoading model in bf16 to {device}...")
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(
        model_name, torch_dtype=torch.bfloat16, attn_implementation="eager"
    )
    model = model.to(device)
    model.eval()
    mem_gb = torch.cuda.memory_allocated(device) / 1e9
    print(f"Model loaded. GPU mem: {mem_gb:.1f}GB")

    results = {
        "experiment": "kivi_mckp_orthogonality",
        "model": model_name,
        "architecture": {
            "num_layers": num_layers,
            "num_kv_heads": num_kv_heads,
            "head_dim": config.hidden_size // config.num_attention_heads,
            "total_kv_heads": total_kv_heads,
        },
        "kivi_params": {"group_size": group_size, "residual_length": residual_length},
        "mckp_params": {"budget": budget, "max_2bit": max_2bit},
        "bit_distribution": bit_counts,
    }

    # ---- Condition 1: BF16 baseline ----
    print("\n" + "=" * 60)
    print("Condition 1: BF16 baseline")
    print("=" * 60)
    bf16_ppl = evaluate_perplexity(model, tokenizer, device)
    print(f"  → PPL = {bf16_ppl:.4f}")
    results["bf16_ppl"] = round(bf16_ppl, 4)

    # ---- Condition 2: KIVI alone (uniform 4-bit, KIVI quantization) ----
    print("\n" + "=" * 60)
    print("Condition 2: KIVI alone (uniform 4-bit)")
    print("=" * 60)
    orig = patch_kivi_uniform(model, bits=4, group_size=group_size,
                               residual_length=residual_length)
    kivi_ppl = evaluate_perplexity(model, tokenizer, device)
    restore_attention(model, orig)
    print(f"  → PPL = {kivi_ppl:.4f}")
    results["kivi_uniform4_ppl"] = round(kivi_ppl, 4)

    # ---- Condition 3: MCKP alone (mixed-bit, simple symmetric quantization) ----
    print("\n" + "=" * 60)
    print("Condition 3: MCKP alone (mixed-bit, simple symmetric quant)")
    print("=" * 60)
    orig = patch_attention_combined(model, mckp_result["allocation"],
                                     group_size=group_size,
                                     residual_length=residual_length,
                                     use_kivi=False)
    mckp_ppl = evaluate_perplexity(model, tokenizer, device)
    restore_attention(model, orig)
    print(f"  → PPL = {mckp_ppl:.4f}")
    results["mckp_simple_ppl"] = round(mckp_ppl, 4)

    # ---- Condition 4: KIVI + MCKP (mixed-bit, KIVI quantization) ----
    print("\n" + "=" * 60)
    print("Condition 4: KIVI + MCKP (mixed-bit, KIVI quantization)")
    print("=" * 60)
    orig = patch_attention_combined(model, mckp_result["allocation"],
                                     group_size=group_size,
                                     residual_length=residual_length,
                                     use_kivi=True)
    combined_ppl = evaluate_perplexity(model, tokenizer, device)
    restore_attention(model, orig)
    print(f"  → PPL = {combined_ppl:.4f}")
    results["kivi_mckp_combined_ppl"] = round(combined_ppl, 4)

    # ---- Summary ----
    results["analysis"] = {
        "kivi_vs_bf16": round(kivi_ppl - bf16_ppl, 4),
        "mckp_vs_bf16": round(mckp_ppl - bf16_ppl, 4),
        "combined_vs_bf16": round(combined_ppl - bf16_ppl, 4),
        "combined_vs_kivi": round(combined_ppl - kivi_ppl, 4),
        "combined_vs_mckp": round(combined_ppl - mckp_ppl, 4),
        "orthogonal": combined_ppl < min(kivi_ppl, mckp_ppl),
        "beats_kivi": combined_ppl < kivi_ppl,
        "beats_mckp": combined_ppl < mckp_ppl,
    }
    results["timing_seconds"] = round(time.time() - t0, 1)
    results["allocation"] = {k: list(v) for k, v in mckp_result["allocation"].items()}

    os.makedirs("artifacts", exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(results, f, indent=2)

    print(f"\n{'=' * 60}")
    print("KIVI + MCKP Orthogonality Results")
    print(f"{'=' * 60}")
    print(f"{'Method':<45} {'PPL':>8} {'Δ vs BF16':>10}")
    print("-" * 65)
    print(f"{'BF16 baseline':<45} {bf16_ppl:>8.4f} {'---':>10}")
    print(f"{'KIVI alone (uniform 4-bit)':<45} {kivi_ppl:>8.4f} {kivi_ppl - bf16_ppl:>+10.4f}")
    print(f"{'MCKP alone (mixed-bit, simple quant)':<45} {mckp_ppl:>8.4f} {mckp_ppl - bf16_ppl:>+10.4f}")
    print(f"{'KIVI + MCKP (mixed-bit, KIVI quant)':<45} {combined_ppl:>8.4f} {combined_ppl - bf16_ppl:>+10.4f}")
    print(f"\nOrthogonal complementarity: {'YES' if combined_ppl < min(kivi_ppl, mckp_ppl) else 'NO'}")
    print(f"Combined vs KIVI: {combined_ppl - kivi_ppl:+.4f}")
    print(f"Combined vs MCKP: {combined_ppl - mckp_ppl:+.4f}")
    print(f"Saved to {output_path}")


if __name__ == "__main__":
    main()
