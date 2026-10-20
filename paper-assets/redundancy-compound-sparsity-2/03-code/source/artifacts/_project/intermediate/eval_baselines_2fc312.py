"""
Baseline KV cache eviction evaluation using kvpress.

Benchmarks H2O (KnormPress) / SnapKV / KeyDiff / StreamingLLM / ExpectedAttention /
ObservedAttention / TOVA against full cache on WikiText-2 PPL at configurable budget ratio.

Usage:
    python eval_baselines.py --model /root/carc/models/DeepSeek-R1-Distill-Qwen-14B --gpu 0
    python eval_baselines.py --dry-run
    python eval_baselines.py --budget-ratio 0.3 --seq-len 4096 --num-samples 50
"""

import argparse
import json
import math
import os
import sys
import time
from pathlib import Path

import torch
import torch.nn.functional as F
from tqdm import tqdm

BASELINE_CONFIGS = {
    "full": None,
    "knorm": ("KnormPress", {}),
    "snapkv": ("SnapKVPress", {"window_size": 64, "kernel_size": 5}),
    "keydiff": ("KeyDiffPress", {}),
    "streaming_llm": ("StreamingLLMPress", {"n_sink": 4}),
    "expected_attn": ("ExpectedAttentionPress", {}),
    "observed_attn": ("ObservedAttentionPress", {}),
    "tova": ("TOVAPress", {}),
}


def get_press(name: str, compression_ratio: float):
    """Instantiate a kvpress press by name."""
    import kvpress
    cls_name, extra_kwargs = BASELINE_CONFIGS[name]
    cls = getattr(kvpress, cls_name)
    return cls(compression_ratio=compression_ratio, **extra_kwargs)


def load_wikitext_samples(tokenizer, num_samples: int = 100, seq_len: int = 2048):
    """Load WikiText-2 validation data as fixed-length token sequences."""
    from datasets import load_dataset

    ds = load_dataset("wikitext", "wikitext-2-raw-v1", split="test", trust_remote_code=True)
    buffer = []
    for item in ds:
        text = item.get("text", "")
        if text and len(text.strip()) >= 50:
            buffer.append(text)

    samples = []
    for text in buffer:
        ids = tokenizer(text, return_tensors="pt", add_special_tokens=False).input_ids[0]
        if len(ids) >= seq_len:
            samples.append(ids[:seq_len])
        if len(samples) >= num_samples:
            break

    if len(samples) < num_samples:
        all_ids = torch.cat(
            [tokenizer(t, return_tensors="pt", add_special_tokens=False).input_ids[0] for t in buffer]
        )
        for i in range(0, len(all_ids) - seq_len + 1, seq_len):
            if len(samples) >= num_samples:
                break
            samples.append(all_ids[i : i + seq_len])

    return samples[:num_samples]


def evaluate_ppl_full(model, samples, stride: int, seq_len: int, device: str):
    """PPL without any KV compression (full cache baseline)."""
    total_nll, total_tokens = 0.0, 0
    model.eval()
    with torch.no_grad():
        for seq in tqdm(samples, desc="PPL(full)"):
            input_ids = seq.unsqueeze(0).to(device)
            L = input_ids.shape[1]
            prev_end = 0
            for begin in range(0, L, stride):
                end = min(begin + seq_len, L)
                trg_len = end - prev_end
                ids = input_ids[:, begin:end]
                target_ids = ids.clone()
                target_ids[:, :-trg_len] = -100
                outputs = model(ids, labels=target_ids)
                total_nll += (outputs.loss * trg_len).item()
                total_tokens += trg_len
                prev_end = end
                if end >= L:
                    break
    ppl = math.exp(total_nll / total_tokens) if total_tokens > 0 else float("inf")
    return {"ppl": round(ppl, 4), "num_tokens": total_tokens}


def evaluate_ppl_with_press(model, samples, press, stride: int, seq_len: int, device: str, label: str):
    """PPL with a kvpress compression method applied."""
    total_nll, total_tokens = 0.0, 0
    model.eval()
    with torch.no_grad(), press(model):
        for seq in tqdm(samples, desc=f"PPL({label})"):
            input_ids = seq.unsqueeze(0).to(device)
            L = input_ids.shape[1]
            prev_end = 0
            for begin in range(0, L, stride):
                end = min(begin + seq_len, L)
                trg_len = end - prev_end
                ids = input_ids[:, begin:end]
                target_ids = ids.clone()
                target_ids[:, :-trg_len] = -100
                outputs = model(ids, labels=target_ids)
                total_nll += (outputs.loss * trg_len).item()
                total_tokens += trg_len
                prev_end = end
                if end >= L:
                    break
    ppl = math.exp(total_nll / total_tokens) if total_tokens > 0 else float("inf")
    return {"ppl": round(ppl, 4), "num_tokens": total_tokens}


def print_results_table(results: dict, budget_ratio: float):
    """Pretty-print a comparison table."""
    print(f"\n{'='*60}")
    print(f"  Baseline KV Eviction Results  (budget={budget_ratio:.0%})")
    print(f"{'='*60}")
    print(f"  {'Method':<20} {'PPL':>10} {'vs Full':>10}")
    print(f"  {'-'*20} {'-'*10} {'-'*10}")
    full_ppl = results.get("full", {}).get("ppl", float("inf"))
    for name in BASELINE_CONFIGS:
        if name not in results:
            continue
        r = results[name]
        if r.get("error"):
            print(f"  {name:<20} {'ERROR':>10} {r['error']}")
            continue
        ppl = r["ppl"]
        delta = ((ppl - full_ppl) / full_ppl * 100) if full_ppl > 0 and full_ppl != float("inf") else 0
        marker = "" if name == "full" else f"{delta:+.2f}%"
        print(f"  {name:<20} {ppl:>10.2f} {marker:>10}")
    print(f"{'='*60}\n")


def main():
    parser = argparse.ArgumentParser(description="Baseline KV eviction evaluation with kvpress")
    parser.add_argument("--model", type=str, default="/root/carc/models/DeepSeek-R1-Distill-Qwen-14B")
    parser.add_argument("--gpu", type=int, default=0)
    parser.add_argument("--output", type=str, default="baseline_results.json")
    parser.add_argument("--budget-ratio", type=float, default=0.5, help="Fraction of KV cache to KEEP")
    parser.add_argument("--seq-len", type=int, default=2048)
    parser.add_argument("--stride", type=int, default=512)
    parser.add_argument("--num-samples", type=int, default=100)
    parser.add_argument("--methods", type=str, nargs="+", default=list(BASELINE_CONFIGS.keys()),
                        choices=list(BASELINE_CONFIGS.keys()))
    parser.add_argument("--dry-run", action="store_true", help="Only verify imports and config, skip GPU work")
    args = parser.parse_args()

    compression_ratio = 1.0 - args.budget_ratio

    if args.dry_run:
        print("[DRY-RUN] Config:")
        print(f"  model: {args.model}")
        print(f"  gpu: {args.gpu}")
        print(f"  budget_ratio: {args.budget_ratio} (compression_ratio={compression_ratio})")
        print(f"  seq_len: {args.seq_len}, stride: {args.stride}, num_samples: {args.num_samples}")
        print(f"  methods: {args.methods}")
        print(f"  output: {args.output}")
        print("\n[DRY-RUN] Checking imports...")
        import kvpress
        for method in args.methods:
            if method == "full":
                continue
            try:
                p = get_press(method, compression_ratio)
                print(f"  {method}: OK ({type(p).__name__})")
            except Exception as e:
                print(f"  {method}: FAIL ({e})")
        print("\n[DRY-RUN] All checks passed.")
        return

    device = f"cuda:{args.gpu}"
    os.environ["CUDA_VISIBLE_DEVICES"] = str(args.gpu)

    from transformers import AutoModelForCausalLM, AutoTokenizer

    print(f"Loading tokenizer from {args.model} ...")
    tokenizer = AutoTokenizer.from_pretrained(args.model, trust_remote_code=True)

    print(f"Loading model to {device} (bf16) ...")
    model = AutoModelForCausalLM.from_pretrained(
        args.model,
        torch_dtype=torch.bfloat16,
        device_map=device,
        trust_remote_code=True,
    )
    model.eval()

    print(f"Loading WikiText-2 ({args.num_samples} samples, seq_len={args.seq_len}) ...")
    samples = load_wikitext_samples(tokenizer, num_samples=args.num_samples, seq_len=args.seq_len)
    print(f"  Loaded {len(samples)} samples")

    results = {"_config": {
        "model": args.model,
        "budget_ratio": args.budget_ratio,
        "compression_ratio": compression_ratio,
        "seq_len": args.seq_len,
        "stride": args.stride,
        "num_samples": len(samples),
    }}

    for method in args.methods:
        print(f"\n--- Evaluating: {method} ---")
        t0 = time.time()
        try:
            if method == "full":
                r = evaluate_ppl_full(model, samples, args.stride, args.seq_len, device)
            else:
                press = get_press(method, compression_ratio)
                r = evaluate_ppl_with_press(model, samples, press, args.stride, args.seq_len, device, method)
            r["elapsed_s"] = round(time.time() - t0, 1)
            results[method] = r
            print(f"  {method}: PPL={r['ppl']:.2f} ({r['elapsed_s']}s)")
        except Exception as e:
            results[method] = {"error": str(e), "elapsed_s": round(time.time() - t0, 1)}
            print(f"  {method}: ERROR - {e}")

    print_results_table(results, args.budget_ratio)

    out_path = Path(args.output)
    out_path.write_text(json.dumps(results, indent=2, ensure_ascii=False))
    print(f"Results saved to {out_path}")


if __name__ == "__main__":
    main()
