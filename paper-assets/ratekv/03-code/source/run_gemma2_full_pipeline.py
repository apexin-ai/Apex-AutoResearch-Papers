"""Gemma-2-9B full pipeline: profile -> MCKP solve -> eval -> k ablation -> analysis.

Gemma-2 adaptations vs Llama/Qwen baseline code:
  - head_dim from config (256), not hidden_size//num_heads (224)
  - attn_logit_softcapping: tanh(scores/softcap)*softcap before mask+softmax
  - query_pre_attn_scalar for attention scaling (not 1/sqrt(head_dim))
  - sliding_window on alternating layers (handled by 4D attention mask)

Input:  model checkpoint, calibration JSON
Output: gemma2_full_results.json, gemma2_profiling_results.json
"""
import os
os.environ["HF_HOME"] = "/root/autodl-tmp/.hf_cache"
os.environ["HF_DATASETS_OFFLINE"] = "1"

import argparse
import copy
import importlib
import json
import math
import time
import torch
import torch.nn.functional as F
from transformers import AutoModelForCausalLM, AutoTokenizer, AutoConfig
from solver import solve_mckp_constrained, uniform_quantization_baseline, enforce_monotonicity
from utils import quantize_per_channel, quantize_per_token, repeat_kv


# ---------------------------------------------------------------------------
# Gemma-2-aware attention patching
# ---------------------------------------------------------------------------

def _get_rotary_fn(model):
    model_type = model.config.model_type
    module_name = f"transformers.models.{model_type}.modeling_{model_type}"
    module = importlib.import_module(module_name)
    return module.apply_rotary_pos_emb


def patch_attention_gemma2(model, allocations):
    """Monkey-patch Gemma-2 attention with per-head quantization.

    Handles head_dim != hidden_size//num_heads, logit soft-capping,
    and sliding window (via attention_mask from the model).
    """
    config = model.config
    num_kv_heads = config.num_key_value_heads
    num_q_heads = config.num_attention_heads
    head_dim = getattr(config, "head_dim", config.hidden_size // num_q_heads)
    n_groups = num_q_heads // num_kv_heads
    softcap = getattr(config, "attn_logit_softcapping", None)

    rotary_fn = _get_rotary_fn(model)
    original_forwards = {}

    for layer_idx, layer in enumerate(model.model.layers):
        attn = layer.self_attn

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

        def make_forward(orig_attn, h_allocs, n_kv=num_kv_heads, ng=n_groups,
                         hd=head_dim, rope_fn=rotary_fn, sc=softcap):
            def compressed_forward(hidden_states, position_embeddings,
                                   attention_mask=None, **kwargs):
                bsz, seq_len = hidden_states.shape[:2]

                q = orig_attn.q_proj(hidden_states).view(bsz, seq_len, -1, hd).transpose(1, 2)
                k = orig_attn.k_proj(hidden_states).view(bsz, seq_len, n_kv, hd).transpose(1, 2)
                v = orig_attn.v_proj(hidden_states).view(bsz, seq_len, n_kv, hd).transpose(1, 2)

                cos, sin = position_embeddings
                q, k = rope_fn(q, k, cos, sin)

                for h in range(n_kv):
                    atype, param = h_allocs[h]
                    if atype == "quant" and int(param) < 16:
                        bits = int(param)
                        k[:, h] = quantize_per_channel(k[:, h:h + 1], bits).squeeze(1)
                        v[:, h] = quantize_per_token(v[:, h:h + 1], bits).squeeze(1)

                k_exp = repeat_kv(k, ng)
                v_exp = repeat_kv(v, ng)

                attn_scores = torch.matmul(q, k_exp.transpose(2, 3)) * orig_attn.scaling

                # Gemma-2 logit soft-capping
                if sc is not None:
                    attn_scores = attn_scores / sc
                    attn_scores = torch.tanh(attn_scores)
                    attn_scores = attn_scores * sc

                if attention_mask is not None:
                    cm = attention_mask[:, :, :, :k_exp.shape[-2]]
                    attn_scores = attn_scores + cm
                else:
                    causal = torch.triu(
                        torch.full((seq_len, seq_len), float("-inf"),
                                   device=attn_scores.device, dtype=attn_scores.dtype),
                        diagonal=1
                    )
                    attn_scores = attn_scores + causal

                attn_w = F.softmax(attn_scores, dim=-1, dtype=torch.float32).to(q.dtype)
                out = torch.matmul(attn_w, v_exp)
                out = out.transpose(1, 2).contiguous().reshape(bsz, seq_len, -1)
                out = orig_attn.o_proj(out)
                return out, attn_w

            return compressed_forward

        attn.forward = make_forward(attn, head_allocs)

    return original_forwards


def restore_attention(model, original_forwards):
    for layer_idx, fwd in original_forwards.items():
        model.model.layers[layer_idx].self_attn.forward = fwd


# ---------------------------------------------------------------------------
# Profiler (replicates FullBitwidthProfiler logic with Gemma-2 patching)
# ---------------------------------------------------------------------------

class Gemma2Profiler:
    def __init__(self, model, tokenizer, calibration_data, device="cuda:0",
                 num_samples=16, seq_len=512):
        self.device = device
        self.seq_len = seq_len
        self.model = model
        self.tokenizer = tokenizer

        config = model.config
        self.num_layers = config.num_hidden_layers
        self.num_kv_heads = config.num_key_value_heads

        self.input_ids = self._load_calibration_data(calibration_data)
        total_heads = self.num_layers * self.num_kv_heads
        print(f"Config: {self.num_layers} layers, {self.num_kv_heads} KV heads/layer, "
              f"{total_heads} heads total")
        print(f"Calibration: {self.input_ids.shape[0]} seqs x {self.input_ids.shape[1]} tokens")
        self._baseline_ppl = None

    def _load_calibration_data(self, path):
        with open(path) as f:
            samples = json.load(f)
        bos_id = self.tokenizer.bos_token_id
        all_ids = []
        for s in samples:
            tokens = self.tokenizer.encode(s["text"], add_special_tokens=False)
            if len(tokens) >= self.seq_len:
                seq = [bos_id] + tokens[:self.seq_len - 1]
                all_ids.append(seq)
            if len(all_ids) >= 16:
                break
        if not all_ids:
            raise RuntimeError(f"No calibration seqs with >= {self.seq_len} tokens")
        return torch.tensor(all_ids, dtype=torch.long, device=self.device)

    def _compute_ppl(self):
        with torch.no_grad():
            outputs = self.model(
                self.input_ids, use_cache=False,
                cache_position=torch.arange(self.seq_len, device=self.device)
            )
        shift_logits = outputs.logits[:, :-1].contiguous()
        shift_labels = self.input_ids[:, 1:].contiguous()
        loss = F.cross_entropy(
            shift_logits.float().view(-1, shift_logits.shape[-1]),
            shift_labels.view(-1),
            reduction="sum"
        )
        return math.exp(loss.item() / shift_labels.numel())

    def compute_baseline_ppl(self):
        if self._baseline_ppl is None:
            print("Computing baseline PPL...")
            self._baseline_ppl = self._compute_ppl()
            print(f"Baseline PPL: {self._baseline_ppl:.4f}")
        return self._baseline_ppl

    def profile_single_head(self, layer, head, bits):
        self.compute_baseline_ppl()
        if bits >= 16:
            return 0.0
        allocations = {f"{layer},{head}": ["quant", bits]}
        orig_fwds = patch_attention_gemma2(self.model, allocations)
        ppl = self._compute_ppl()
        restore_attention(self.model, orig_fwds)
        return ppl - self._baseline_ppl

    def profile_all(self, bit_widths=(2, 4, 8)):
        self.compute_baseline_ppl()
        total_heads = self.num_layers * self.num_kv_heads
        total_evals = total_heads * len(bit_widths)
        done = 0

        profiles = {}
        for l in range(self.num_layers):
            profiles[str(l)] = {}
            for h in range(self.num_kv_heads):
                head_profile = {"quantization": {}}
                for bits in bit_widths:
                    delta = self.profile_single_head(l, h, bits)
                    head_profile["quantization"][str(bits)] = delta
                    done += 1
                    print(f"[{done}/{total_evals}] L{l}H{h} @{bits}bit: delta={delta:.6f}")
                profiles[str(l)][str(h)] = head_profile
        return profiles


# ---------------------------------------------------------------------------
# Eval (WikiText-2)
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


# ---------------------------------------------------------------------------
# Main pipeline
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Gemma-2-9B full pipeline")
    parser.add_argument("--model", type=str,
                        default="/root/autodl-tmp/.hf_cache/google/gemma-2-9b")
    parser.add_argument("--calibration_data", type=str, default="calibration_data.json")
    parser.add_argument("--device", type=str, default="cuda:0")
    parser.add_argument("--budget", type=float, default=0.25)
    parser.add_argument("--initial_k", type=int, default=8)
    parser.add_argument("--k_values", type=str, default="2,4,6,8,10,12,14,16")
    parser.add_argument("--output", type=str, default="gemma2_full_results.json")
    parser.add_argument("--profile_output", type=str, default="gemma2_profiling_results.json")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    k_values = [int(x) for x in args.k_values.split(",")]
    device = args.device

    # --- Verify model config ---
    print("=" * 60)
    print("Gemma-2-9B Full Pipeline")
    print("=" * 60)

    config = AutoConfig.from_pretrained(args.model)
    num_layers = config.num_hidden_layers
    num_kv_heads = config.num_key_value_heads
    num_q_heads = config.num_attention_heads
    head_dim = getattr(config, "head_dim", config.hidden_size // num_q_heads)
    total_kv_heads = num_layers * num_kv_heads
    softcap = getattr(config, "attn_logit_softcapping", None)
    sliding_window = getattr(config, "sliding_window", None)

    print(f"Model:         {args.model}")
    print(f"model_type:    {config.model_type}")
    print(f"Layers:        {num_layers}")
    print(f"Q heads:       {num_q_heads}")
    print(f"KV heads:      {num_kv_heads} (GQA {num_q_heads//num_kv_heads}:1)")
    print(f"head_dim:      {head_dim}")
    print(f"hidden_size:   {config.hidden_size}")
    print(f"Total KV heads:{total_kv_heads}")
    print(f"softcap:       {softcap}")
    print(f"sliding_window:{sliding_window}")
    print(f"Budget:        {args.budget}")
    print(f"Initial k:     {args.initial_k}")
    print(f"K sweep:       {k_values}")

    if args.dry_run:
        print("\n[DRY RUN] Exiting.")
        return

    # --- Load model ---
    print("\nLoading model...")
    t_load = time.time()
    tokenizer = AutoTokenizer.from_pretrained(args.model)
    model = AutoModelForCausalLM.from_pretrained(
        args.model, torch_dtype=torch.bfloat16, attn_implementation="eager"
    )
    model = model.to(device)
    model.eval()
    print(f"Model loaded in {time.time()-t_load:.1f}s")

    # ===================================================================
    # Phase 1: Profiling
    # ===================================================================
    print(f"\n{'='*60}")
    print("[Phase 1] Profiling per-head PPL sensitivity...")
    print(f"{'='*60}")
    t0 = time.time()

    profiler = Gemma2Profiler(
        model, tokenizer,
        calibration_data=args.calibration_data,
        device=device, num_samples=16, seq_len=512
    )
    baseline_cal_ppl = profiler.compute_baseline_ppl()
    profiles = profiler.profile_all(bit_widths=(2, 4, 8))
    profile_time = time.time() - t0
    print(f"\nProfiling done in {profile_time:.1f}s")

    profile_data = {
        "model": args.model,
        "model_name": "Gemma-2-9B",
        "baseline_calibration_ppl": baseline_cal_ppl,
        "num_layers": num_layers,
        "num_kv_heads": num_kv_heads,
        "num_attention_heads": num_q_heads,
        "head_dim": head_dim,
        "gqa_ratio": num_q_heads // num_kv_heads,
        "profiles": profiles,
        "profile_time_seconds": profile_time,
    }
    with open(args.profile_output, "w") as f:
        json.dump(profile_data, f, indent=2)
    print(f"Profiles saved to {args.profile_output}")

    _print_sensitivity(profiles)

    # ===================================================================
    # Phase 2: Constrained MCKP + Uniform eval
    # ===================================================================
    print(f"\n{'='*60}")
    print(f"[Phase 2] Constrained MCKP (k={args.initial_k}) + Uniform 4-bit eval")
    print(f"{'='*60}")
    t1 = time.time()

    enforced = enforce_monotonicity(profiles)

    mckp_result = solve_mckp_constrained(
        enforced, args.budget, mode="quant_only",
        max_2bit=args.initial_k, l0_exclude_2bit=True
    )
    uniform_result = uniform_quantization_baseline(enforced, bits=4)

    bit_counts = {}
    for key, (atype, param) in mckp_result["allocation"].items():
        b = param if atype == "quant" else 16
        bit_counts[b] = bit_counts.get(b, 0) + 1
    print(f"MCKP bit dist: {bit_counts}")
    print(f"MCKP mem ratio: {mckp_result['actual_memory_ratio']:.4f}")

    # Evaluate bf16 baseline on WikiText-2
    print("\n  Evaluating bf16 baseline on WikiText-2...")
    baseline_wt2 = evaluate_perplexity(model, tokenizer, device)
    print(f"  >>> Baseline PPL: {baseline_wt2:.4f}")

    # Evaluate MCKP
    print("\n  Evaluating non-uniform MCKP...")
    orig_fwds = patch_attention_gemma2(model, mckp_result["allocation"])
    mckp_wt2 = evaluate_perplexity(model, tokenizer, device)
    restore_attention(model, orig_fwds)
    print(f"  >>> MCKP PPL: {mckp_wt2:.4f}")

    # Evaluate uniform 4-bit
    print("\n  Evaluating uniform 4-bit...")
    orig_fwds = patch_attention_gemma2(model, uniform_result["allocation"])
    uniform_wt2 = evaluate_perplexity(model, tokenizer, device)
    restore_attention(model, orig_fwds)
    print(f"  >>> Uniform 4-bit PPL: {uniform_wt2:.4f}")

    phase2_time = time.time() - t1
    delta_phase2 = uniform_wt2 - mckp_wt2

    print(f"\n  Phase 2 result: MCKP={mckp_wt2:.4f}, Uniform={uniform_wt2:.4f}, "
          f"delta={delta_phase2:+.4f}")

    # ===================================================================
    # Phase 3: K Ablation Sweep
    # ===================================================================
    print(f"\n{'='*60}")
    print("[Phase 3] K Ablation Sweep")
    print(f"{'='*60}")
    t2 = time.time()

    k_results = []
    for k in k_values:
        print(f"\n--- max_2bit = {k} ---")
        sol = solve_mckp_constrained(
            enforced, args.budget, mode="quant_only",
            max_2bit=k, l0_exclude_2bit=True
        )
        bd = sol["bit_distribution"]
        print(f"  Bit dist: {bd}, mem={sol['actual_memory_ratio']:.4f}")

        orig = patch_attention_gemma2(model, sol["allocation"])
        ppl = evaluate_perplexity(model, tokenizer, device)
        restore_attention(model, orig)
        print(f"  >>> PPL = {ppl:.4f}")

        k_results.append({
            "max_2bit": k,
            "ppl": round(ppl, 4),
            "n_2bit": bd.get(2, 0),
            "n_4bit": bd.get(4, 0),
            "n_8bit": bd.get(8, 0),
            "n_16bit": bd.get(16, 0),
            "mem_ratio": round(sol["actual_memory_ratio"], 4),
            "total_distortion": round(sol["total_distortion"], 6),
        })

    ablation_time = time.time() - t2

    print(f"\n{'k':>5} {'PPL':>10} {'2bit':>6} {'4bit':>6} {'8bit':>6} {'16bit':>6} {'mem':>8}")
    print("-" * 55)
    for r in k_results:
        print(f"{r['max_2bit']:>5} {r['ppl']:>10.4f} {r['n_2bit']:>6} {r['n_4bit']:>6} "
              f"{r['n_8bit']:>6} {r['n_16bit']:>6} {r['mem_ratio']:>8.4f}")

    best_k = min(k_results, key=lambda r: r["ppl"])
    print(f"\nBest k: {best_k['max_2bit']} (PPL={best_k['ppl']:.4f})")

    # ===================================================================
    # Phase 4: Analysis
    # ===================================================================
    print(f"\n{'='*60}")
    print("[Phase 4] Heterogeneity Analysis")
    print(f"{'='*60}")

    all_deltas_2bit = []
    layer_deltas = {}
    for l_str in sorted(profiles.keys(), key=int):
        layer_deltas[int(l_str)] = []
        for h_str in sorted(profiles[l_str].keys(), key=int):
            d2 = profiles[l_str][h_str]["quantization"].get("2", 0.0)
            all_deltas_2bit.append((int(l_str), int(h_str), d2))
            layer_deltas[int(l_str)].append(d2)

    # Top-5% concentration
    sorted_by_d2 = sorted(all_deltas_2bit, key=lambda x: -x[2])
    n_top5 = max(1, int(len(sorted_by_d2) * 0.05))
    total_sum = sum(x[2] for x in all_deltas_2bit)
    top5_sum = sum(x[2] for x in sorted_by_d2[:n_top5])
    top5_concentration = top5_sum / total_sum if total_sum > 0 else 0

    print(f"\nTotal KV heads: {len(all_deltas_2bit)}")
    print(f"Top-5% heads ({n_top5}): concentration = {top5_concentration:.4f}")
    print(f"  (Qwen reference: 0.59-0.66)")

    # Layer 0 dominance
    l0_mean = sum(layer_deltas.get(0, [0])) / max(len(layer_deltas.get(0, [1])), 1)
    other_means = []
    for l in range(1, num_layers):
        if l in layer_deltas and layer_deltas[l]:
            other_means.append(sum(layer_deltas[l]) / len(layer_deltas[l]))
    other_avg = sum(other_means) / len(other_means) if other_means else 0
    l0_ratio = l0_mean / other_avg if other_avg > 0 else float("inf")

    print(f"\nLayer 0 mean delta(2-bit): {l0_mean:.6f}")
    print(f"Other layers mean delta(2-bit): {other_avg:.6f}")
    print(f"L0 dominance ratio: {l0_ratio:.2f}x")

    # Top-5 most sensitive
    print(f"\nTop-5 most sensitive heads:")
    for l, h, d2 in sorted_by_d2[:5]:
        d4 = profiles[str(l)][str(h)]["quantization"].get("4", 0.0)
        d8 = profiles[str(l)][str(h)]["quantization"].get("8", 0.0)
        print(f"  L{l}H{h}: 2bit={d2:+.6f}, 4bit={d4:+.6f}, 8bit={d8:+.6f}")

    # Heterogeneity stats
    deltas = [x[2] for x in all_deltas_2bit]
    d_tensor = torch.tensor(deltas)
    print(f"\n2-bit delta stats:")
    print(f"  min={min(deltas):.6f}, max={max(deltas):.6f}")
    print(f"  mean={d_tensor.mean().item():.6f}, std={d_tensor.std().item():.6f}")
    print(f"  CV (std/mean)={d_tensor.std().item()/d_tensor.mean().item():.4f}" if d_tensor.mean().item() > 0 else "")
    n_positive = sum(1 for d in deltas if d > 1e-6)
    print(f"  Heads with delta > 0: {n_positive}/{len(deltas)}")

    # ===================================================================
    # Phase 5: Save results
    # ===================================================================
    print(f"\n{'='*60}")
    print("[Phase 5] Save results")
    print(f"{'='*60}")

    total_time = time.time() - t0

    results = {
        "model": args.model,
        "model_name": "Gemma-2-9B",
        "model_type": config.model_type,
        "architecture": {
            "num_layers": num_layers,
            "num_kv_heads": num_kv_heads,
            "num_attention_heads": num_q_heads,
            "head_dim": head_dim,
            "hidden_size": config.hidden_size,
            "gqa_ratio": num_q_heads // num_kv_heads,
            "total_kv_heads": total_kv_heads,
            "attn_logit_softcapping": softcap,
            "sliding_window": sliding_window,
        },
        "verdict": "PASS" if delta_phase2 >= 0.5 else "MARGINAL" if delta_phase2 >= 0.1 else "FAIL",
        "baseline_calibration_ppl": baseline_cal_ppl,
        "baseline_wikitext2_ppl": baseline_wt2,
        "mckp_wikitext2_ppl": mckp_wt2,
        "uniform4bit_wikitext2_ppl": uniform_wt2,
        "mckp_improvement_over_uniform": delta_phase2,
        "initial_k": args.initial_k,
        "bit_distribution": bit_counts,
        "mckp_actual_memory_ratio": mckp_result["actual_memory_ratio"],
        "k_ablation": k_results,
        "best_k": best_k,
        "analysis": {
            "top5_concentration": round(top5_concentration, 4),
            "top5_n_heads": n_top5,
            "layer0_mean_delta_2bit": round(l0_mean, 6),
            "other_layers_mean_delta_2bit": round(other_avg, 6),
            "layer0_dominance_ratio": round(l0_ratio, 2),
            "delta_2bit_mean": round(d_tensor.mean().item(), 6),
            "delta_2bit_std": round(d_tensor.std().item(), 6),
            "heads_with_positive_delta": n_positive,
        },
        "timing": {
            "profile_seconds": round(profile_time, 1),
            "phase2_seconds": round(phase2_time, 1),
            "ablation_seconds": round(ablation_time, 1),
            "total_seconds": round(total_time, 1),
        },
        "config": {
            "budget": args.budget,
            "initial_k": args.initial_k,
            "k_values": k_values,
            "calibration_data": args.calibration_data,
        },
    }

    with open(args.output, "w") as f:
        json.dump(results, f, indent=2)

    print(f"\n{'='*60}")
    print("RESULTS — Gemma-2-9B")
    print(f"{'='*60}")
    print(f"\n{'Method':<30} {'PPL':>10} {'Delta vs uniform':>18}")
    print("-" * 60)
    print(f"{'Baseline (bf16)':<30} {baseline_wt2:>10.4f} {'---':>18}")
    print(f"{'Non-uniform MCKP':<30} {mckp_wt2:>10.4f} {delta_phase2:>+18.4f}")
    print(f"{'Uniform 4-bit':<30} {uniform_wt2:>10.4f} {'---':>18}")
    print(f"\nTop-5% concentration: {top5_concentration:.4f}")
    print(f"L0 dominance: {l0_ratio:.2f}x")
    print(f"Best k: {best_k['max_2bit']} (PPL={best_k['ppl']:.4f})")
    print(f"Verdict: {results['verdict']}")
    print(f"Total time: {total_time/3600:.1f}h")
    print(f"\nSaved to {args.output}")


def _print_sensitivity(profiles):
    all_2bit = []
    for l_str in sorted(profiles.keys(), key=int):
        for h_str in sorted(profiles[l_str].keys(), key=int):
            delta_2 = profiles[l_str][h_str]["quantization"].get("2", 0.0)
            delta_4 = profiles[l_str][h_str]["quantization"].get("4", 0.0)
            delta_8 = profiles[l_str][h_str]["quantization"].get("8", 0.0)
            all_2bit.append((f"L{l_str}H{h_str}", delta_2, delta_4, delta_8))

    deltas = [x[1] for x in all_2bit]
    print(f"\n2-bit delta stats: min={min(deltas):.4f}, max={max(deltas):.4f}, "
          f"mean={sum(deltas)/len(deltas):.4f}, "
          f"std={torch.tensor(deltas).std().item():.4f}")

    by_2bit = sorted(all_2bit, key=lambda x: -x[1])
    print("\nTop-5 most sensitive heads (2-bit):")
    for name, d2, d4, d8 in by_2bit[:5]:
        print(f"  {name}: 2bit={d2:+.4f}, 4bit={d4:+.4f}, 8bit={d8:+.4f}")
    print("\nBottom-5 least sensitive heads (2-bit):")
    for name, d2, d4, d8 in by_2bit[-5:]:
        print(f"  {name}: 2bit={d2:+.4f}, 4bit={d4:+.4f}, 8bit={d8:+.4f}")


if __name__ == "__main__":
    main()
