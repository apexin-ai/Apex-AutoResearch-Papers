"""KIVI baseline PPL evaluation on WikiText-2.

Re-implements KIVI's per-channel asymmetric KV cache quantization
for compatibility with transformers 4.57+ and all model architectures.

KIVI scheme:
  K: asymmetric min-max quantization per channel (head_dim), grouped along token dim
  V: asymmetric min-max quantization per token, grouped along head_dim
  Last `residual_length` tokens kept in fp16.

Reference: https://github.com/jy-yuan/KIVI
"""

import argparse
import importlib
import json
import math
import torch
import torch.nn.functional as F
from transformers import AutoModelForCausalLM, AutoTokenizer


def kivi_quantize_k(k, bits, group_size):
    """Asymmetric per-channel quantization for K cache (KIVI scheme).

    K shape: (B, nh, T, D)
    Groups along T (token dim) with group_size.
    For each (B, nh, *, D) group of group_size tokens, compute min/max.
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
    """Asymmetric per-token quantization for V cache (KIVI scheme).

    V shape: (B, nh, T, D)
    Groups along D (head_dim) with group_size.
    For each (B, nh, T, *) group of group_size channels, compute min/max.
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


def patch_kivi(model, k_bits, v_bits, group_size, residual_length):
    config = model.config
    num_kv_heads = config.num_key_value_heads
    num_q_heads = config.num_attention_heads
    head_dim = config.hidden_size // num_q_heads
    n_groups = num_q_heads // num_kv_heads
    rotary_fn = _get_rotary_fn(model)
    original_forwards = {}

    for layer_idx, layer in enumerate(model.model.layers):
        attn = layer.self_attn
        original_forwards[layer_idx] = attn.forward

        def make_forward(orig_attn, n_kv=num_kv_heads, ng=n_groups, hd=head_dim,
                         rope_fn=rotary_fn, kb=k_bits, vb=v_bits, gs=group_size, rl=residual_length):
            def kivi_forward(hidden_states, position_embeddings, attention_mask=None, **kwargs):
                bsz, seq_len = hidden_states.shape[:2]

                q = orig_attn.q_proj(hidden_states).view(bsz, seq_len, -1, hd).transpose(1, 2)
                k = orig_attn.k_proj(hidden_states).view(bsz, seq_len, n_kv, hd).transpose(1, 2)
                v = orig_attn.v_proj(hidden_states).view(bsz, seq_len, n_kv, hd).transpose(1, 2)

                cos, sin = position_embeddings
                q, k = rope_fn(q, k, cos, sin)

                T = k.shape[2]
                quant_len = T - rl if T > rl else 0
                quant_len = (quant_len // gs) * gs

                if quant_len > 0:
                    k_q = kivi_quantize_k(k[:, :, :quant_len], kb, gs)
                    k = torch.cat([k_q, k[:, :, quant_len:]], dim=2)
                    v_q = kivi_quantize_v(v[:, :, :quant_len], vb, gs)
                    v = torch.cat([v_q, v[:, :, quant_len:]], dim=2)

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

            return kivi_forward

        attn.forward = make_forward(attn)

    return original_forwards


def restore_attention(model, original_forwards):
    for layer_idx, fwd in original_forwards.items():
        model.model.layers[layer_idx].self_attn.forward = fwd


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


def main():
    parser = argparse.ArgumentParser(description="KIVI baseline PPL evaluation")
    parser.add_argument("--model", type=str, required=True)
    parser.add_argument("--bits", type=int, nargs="+", default=[2, 4],
                        help="Bit-widths to evaluate (applied to both K and V)")
    parser.add_argument("--group-size", type=int, default=32)
    parser.add_argument("--residual-length", type=int, default=128)
    parser.add_argument("--device", type=str, default="cuda:0")
    parser.add_argument("--stride", type=int, default=512)
    parser.add_argument("--output", type=str, default=None)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    print(f"Loading model {args.model}...")
    tokenizer = AutoTokenizer.from_pretrained(args.model)
    model = AutoModelForCausalLM.from_pretrained(
        args.model, dtype=torch.bfloat16, attn_implementation="eager",
    )
    model = model.to(args.device)
    model.eval()

    if args.dry_run:
        print(f"  Model type: {model.config.model_type}")
        print(f"  Num layers: {model.config.num_hidden_layers}")
        print(f"  Num KV heads: {model.config.num_key_value_heads}")
        print(f"  Head dim: {model.config.hidden_size // model.config.num_attention_heads}")
        for b in args.bits:
            orig = patch_kivi(model, b, b, args.group_size, args.residual_length)
            test_ids = tokenizer("Hello world", return_tensors="pt").input_ids.to(args.device)
            with torch.no_grad():
                out = model(test_ids, use_cache=False,
                            cache_position=torch.arange(test_ids.shape[1], device=test_ids.device))
            print(f"  KIVI-{b}bit forward OK, logits shape: {out.logits.shape}")
            restore_attention(model, orig)
        print("Dry run passed.")
        return

    results = {}
    for b in args.bits:
        label = f"KIVI-{b}bit-g{args.group_size}-r{args.residual_length}"
        print(f"\n{'=' * 60}")
        print(f"{label}")
        print(f"{'=' * 60}")

        orig = patch_kivi(model, b, b, args.group_size, args.residual_length)
        ppl = evaluate_perplexity(model, tokenizer, args.device, args.stride)
        restore_attention(model, orig)

        results[label] = {
            "ppl": round(ppl, 4),
            "k_bits": b, "v_bits": b,
            "group_size": args.group_size,
            "residual_length": args.residual_length,
            "model": args.model,
        }
        print(f"  → PPL = {ppl:.4f}")

    if args.output:
        with open(args.output, "w") as f:
            json.dump(results, f, indent=2)
        print(f"\nSaved to {args.output}")
    else:
        print(f"\n{json.dumps(results, indent=2)}")


if __name__ == "__main__":
    main()
