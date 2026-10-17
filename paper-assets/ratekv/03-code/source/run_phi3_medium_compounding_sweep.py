"""Phi-3-medium-14B compounding sweep — measure super-additivity of 2-bit deltas.

Architecture: 40 layers × 10 KV heads (GQA 4:1), 400 total KV heads.
Progressively apply 2-bit quantization to increasing numbers of heads
(sorted by individual delta, most sensitive first) and measure joint PPL.
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
from eval_ppl import patch_attention, restore_attention

MODEL_PATH = "/root/autodl-tmp/.hf_cache/LLM-Research/Phi-3-medium-128k-instruct"
PROFILE_PATH = "artifacts/phi3_medium_profiles_hires.json"
OUTPUT_PATH = "artifacts/phi3_medium_compounding_sweep.json"


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
    parser = argparse.ArgumentParser(description="Phi-3-medium-14B compounding sweep")
    parser.add_argument("--gpu", type=str, default="cuda:1")
    parser.add_argument("--num_samples", type=int, default=64)
    parser.add_argument("--seq_len", type=int, default=2048)
    parser.add_argument("--batch_size", type=int, default=1)
    parser.add_argument("--calibration_data", type=str, default="calibration_hires.json")
    args = parser.parse_args()

    device = args.gpu
    n_values = [1, 2, 4, 8, 16, 32, 64, 128, 200, 400]
    t0 = time.time()

    # Load profiles
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
    n_values = [n for n in n_values if n <= total_kv_heads]
    print(f"Total KV heads: {total_kv_heads}")
    print(f"Sweep n values: {n_values}")
    print(f"Top-5: {[(h['key'], round(h['delta_2bit'], 4)) for h in head_deltas[:5]]}")

    # Load model
    print(f"\nLoading {MODEL_PATH} in bf16 to {device}...")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH, trust_remote_code=False)
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_PATH, torch_dtype=torch.bfloat16,
        attn_implementation="eager", trust_remote_code=False
    )
    model = model.to(device)
    model.eval()
    print(f"GPU mem: {torch.cuda.memory_allocated(device) / 1e9:.1f}GB")

    # Load calibration data
    print(f"Loading calibration data ({args.num_samples} x {args.seq_len})...")
    input_ids = load_calibration_data(
        tokenizer, args.calibration_data,
        args.num_samples, args.seq_len, device)
    print(f"Loaded {input_ids.shape[0]} sequences")

    # Baseline
    print("\nMeasuring baseline PPL...")
    baseline_ppl = compute_ppl_batched(
        model, input_ids, args.seq_len, args.batch_size, device)
    print(f"Baseline PPL: {baseline_ppl:.4f}")

    # Sweep
    results = []
    for n in n_values:
        print(f"\n--- n={n} ---")
        top_n = head_deltas[:n]
        allocation = {h["key"]: ["quant", 2] for h in top_n}
        sum_individual = sum(h["delta_2bit"] for h in top_n)

        orig_fwds = patch_attention(model, allocation)
        joint_ppl = compute_ppl_batched(
            model, input_ids, args.seq_len, args.batch_size, device)
        restore_attention(model, orig_fwds)

        joint_delta = joint_ppl - baseline_ppl
        predicted_ppl = baseline_ppl + sum_individual
        ratio = joint_delta / sum_individual if sum_individual > 0 else float('nan')

        print(f"  sum_indiv={sum_individual:.4f}  joint={joint_ppl:.4f}  "
              f"pred={predicted_ppl:.4f}  ratio={ratio:.4f}")

        results.append({
            "n": n,
            "heads": [h["key"] for h in top_n],
            "sum_individual_delta": round(sum_individual, 6),
            "joint_ppl": round(joint_ppl, 4),
            "joint_delta": round(joint_delta, 6),
            "predicted_ppl": round(predicted_ppl, 4),
            "super_additive_ratio": round(ratio, 4),
        })

    elapsed = time.time() - t0

    output = {
        "experiment": "phi3_medium_compounding_sweep",
        "model": MODEL_PATH,
        "model_name": "Phi-3-medium-14B",
        "pattern": "Spread",
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

    # Summary
    print(f"\n{'='*70}")
    print("COMPOUNDING SWEEP — Phi-3-medium-14B (Spread, c=0.17)")
    print(f"{'='*70}")
    print(f"{'n':>5}  {'sum_indiv':>10}  {'joint_ppl':>10}  {'pred_ppl':>10}  {'ratio':>8}")
    print("-" * 70)
    for r in results:
        print(f"{r['n']:>5}  {r['sum_individual_delta']:>10.4f}  "
              f"{r['joint_ppl']:>10.4f}  {r['predicted_ppl']:>10.4f}  "
              f"{r['super_additive_ratio']:>8.4f}")
    print(f"\nTotal time: {elapsed/60:.1f}min")


if __name__ == "__main__":
    main()
