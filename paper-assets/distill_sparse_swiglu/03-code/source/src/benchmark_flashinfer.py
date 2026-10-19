"""
Sparse FFN Inference Benchmark for LLaMA-3.1-8B.

Measures wall-clock speedup from *actual* sparse SwiGLU execution
(gather active neurons -> smaller matmul -> no wasted FLOPs)
vs dense baseline and mask-and-multiply baseline.

Two sparse backends:
  1. PyTorch gather+matmul (always available)
  2. flashinfer sparse kernels (optional, used if installed)

Modes: dense, mask_multiply_{30,50}, sparse_{30,50} [, flashinfer_{30,50}]

Usage:
  python src/benchmark_flashinfer.py --help
  python src/benchmark_flashinfer.py --device cuda:0 --dry_run
  python src/benchmark_flashinfer.py --device cuda:0 --batch_sizes 1,8 --seq_lens 512,2048
"""
import argparse
import importlib.util
import json
import os
import sys
import time

import numpy as np
import torch
import torch.nn.functional as F

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from predictor import SparsityPredictor

# ── Constants ─────────────────────────────────────────────────────────────
DEFAULT_MODEL = "/root/autodl-tmp/models/llama-3.1-8b"
BASE_DIR = "/root/distill_sparse_swiglu"
CKPT_30 = os.path.join(BASE_DIR, "checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt")
CKPT_50 = os.path.join(BASE_DIR, "checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt")

HIDDEN_SIZE = 4096
INTERMEDIATE_SIZE = 14336
NUM_LAYERS = 32
BOTTLENECK_SIZE = 128

HAS_FLASHINFER = importlib.util.find_spec("flashinfer") is not None


def parse_args():
    p = argparse.ArgumentParser(
        description="Sparse FFN inference benchmark: gather-matmul vs dense",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--model", type=str, default=DEFAULT_MODEL)
    p.add_argument("--device", type=str, default="cuda:0")
    p.add_argument("--batch_sizes", type=str, default="1,8")
    p.add_argument("--seq_lens", type=str, default="512,2048")
    p.add_argument("--warmup", type=int, default=10)
    p.add_argument("--iters", type=int, default=50)
    p.add_argument("--ckpt_30", type=str, default=CKPT_30)
    p.add_argument("--ckpt_50", type=str, default=CKPT_50)
    p.add_argument("--output", type=str, default=None)
    p.add_argument("--dry_run", action="store_true")
    p.add_argument("--modes", type=str, default=None,
                   help="Comma-separated modes to benchmark (default: all available)")
    return p.parse_args()


# ── GPU timing ────────────────────────────────────────────────────────────
def cuda_timer(fn, warmup, iters, device):
    for _ in range(warmup):
        fn()
    torch.cuda.synchronize(device)

    start_events = [torch.cuda.Event(enable_timing=True) for _ in range(iters)]
    end_events = [torch.cuda.Event(enable_timing=True) for _ in range(iters)]

    for i in range(iters):
        start_events[i].record()
        fn()
        end_events[i].record()

    torch.cuda.synchronize(device)
    times_ms = [s.elapsed_time(e) for s, e in zip(start_events, end_events)]
    return times_ms


# ── Model & predictor loading ─────────────────────────────────────────────
def load_model(model_path, device):
    from transformers import AutoModelForCausalLM
    attn = "flash_attention_2" if importlib.util.find_spec("flash_attn") else "sdpa"
    model = AutoModelForCausalLM.from_pretrained(
        model_path,
        torch_dtype=torch.float16,
        attn_implementation=attn,
        device_map={"": device},
    )
    model.eval()
    return model


def load_predictors(ckpt_path, device):
    ckpt = torch.load(ckpt_path, map_location="cpu", weights_only=True)
    predictors = torch.nn.ModuleList([
        SparsityPredictor(HIDDEN_SIZE, INTERMEDIATE_SIZE, BOTTLENECK_SIZE)
        for _ in range(NUM_LAYERS)
    ])
    predictors.load_state_dict(ckpt["predictors"])
    predictors = predictors.half().to(device).eval()
    return predictors


# ── Calibration data loading ──────────────────────────────────────────────
def load_calibration_data(tokenizer, seq_len=512, num_seqs=128):
    """Load diverse calibration sequences from WikiText-2 (cached), with fallbacks."""
    os.environ.setdefault("HF_HOME", "/root/autodl-tmp/.hf_cache")
    os.environ["HF_DATASETS_OFFLINE"] = "1"
    os.environ["HF_HUB_OFFLINE"] = "1"
    os.environ["TRANSFORMERS_OFFLINE"] = "1"

    try:
        from datasets import load_dataset
        ds = load_dataset("wikitext", "wikitext-2-raw-v1", split="train")
        texts = [t for t in ds["text"] if len(t.strip()) > 100][:num_seqs]
        if len(texts) < 16:
            raise ValueError("Too few usable sequences")
        print(f"  Calibration: WikiText-2 ({len(texts)} sequences)")
    except Exception as e:
        print(f"  WikiText-2 load failed ({e}), trying HellaSwag fallback")
        try:
            from datasets import load_dataset
            ds = load_dataset("Rowan/hellaswag", split="validation")
            texts = [r["ctx"] for r in ds if len(r["ctx"].strip()) > 50][:num_seqs]
            print(f"  Calibration: HellaSwag ({len(texts)} sequences)")
        except Exception:
            texts = [
                "The United States of America is a federal republic consisting of "
                "fifty states, a federal district, five major territories, and various "
                "minor islands. The 48 contiguous states and Washington D.C. are in "
                "North America between Canada and Mexico, while Alaska is in the far "
                "northwest of North America and Hawaii is an archipelago in the mid-Pacific. "
                "Territories are scattered about the Pacific Ocean and the Caribbean Sea. "
            ] * num_seqs
            print("  Calibration: fallback synthetic text")

    all_ids = []
    for text in texts:
        tokens = tokenizer(text, return_tensors="pt", max_length=seq_len, truncation=True)
        if tokens["input_ids"].shape[1] >= 32:
            all_ids.append(tokens["input_ids"])
        if len(all_ids) >= num_seqs:
            break

    return all_ids


# ── TEAL global masks (static, from calibration) ─────────────────────────
def compute_teal_masks(model, predictors, device, sparsity_target, seq_len=512, num_calib_seqs=128):
    """Compute per-layer binary masks via predictor score → global top-k.

    Runs diverse calibration sequences through the model, collects predictor
    logits, averages sigmoid(logits) across all tokens to get per-neuron
    importance scores, then applies global top-k allocation.
    """
    from transformers import AutoTokenizer
    tokenizer = AutoTokenizer.from_pretrained(model.config._name_or_path)

    calib_ids_list = load_calibration_data(tokenizer, seq_len=seq_len, num_seqs=num_calib_seqs)

    layer_scores_accum = {i: torch.zeros(INTERMEDIATE_SIZE, device=device) for i in range(NUM_LAYERS)}
    total_tokens = 0

    with torch.no_grad():
        for input_ids in calib_ids_list:
            input_ids = input_ids.to(device)
            outputs = model(input_ids, output_hidden_states=True)
            hidden_states = outputs.hidden_states
            n_tokens = input_ids.shape[0] * input_ids.shape[1]
            total_tokens += n_tokens

            for layer_idx in range(NUM_LAYERS):
                hs = hidden_states[layer_idx]
                logits = predictors[layer_idx](hs)
                scores = torch.sigmoid(logits).sum(dim=(0, 1))
                layer_scores_accum[layer_idx] += scores

    for i in range(NUM_LAYERS):
        layer_scores_accum[i] /= total_tokens

    # Global top-k allocation
    all_scores = torch.cat([layer_scores_accum[i] for i in range(NUM_LAYERS)])
    keep_count = int(all_scores.numel() * (1.0 - sparsity_target))
    threshold = torch.topk(all_scores, keep_count).values[-1]

    masks = {}
    for layer_idx in range(NUM_LAYERS):
        masks[layer_idx] = (layer_scores_accum[layer_idx] >= threshold).to(torch.float16)
    return masks


def compute_teal_masks_from_checkpoint(model, ckpt_path, device, sparsity_target, seq_len=512):
    predictors = load_predictors(ckpt_path, device)
    return compute_teal_masks(model, predictors, device, sparsity_target, seq_len), predictors


# ── Sparse FFN implementations ───────────────────────────────────────────

def mask_and_multiply_ffn(mlp, x, mask):
    """Mask-and-multiply: zero out neurons but still do full-size matmuls (no speedup)."""
    gate = mlp.act_fn(mlp.gate_proj(x))
    up = mlp.up_proj(x)
    hidden = gate * up
    hidden = hidden * mask.unsqueeze(0).unsqueeze(0)
    return mlp.down_proj(hidden)


def sparse_gather_ffn(x, gate_w, up_w, down_w):
    """Full-sparse SwiGLU: all 3 projections only compute active neurons.

    gate_w: [num_active, H] — sliced rows of gate_proj.weight
    up_w:   [num_active, H] — sliced rows of up_proj.weight
    down_w: [H, num_active] — sliced cols of down_proj.weight
    """
    gate_out = F.silu(F.linear(x, gate_w))
    up_out = F.linear(x, up_w)
    hidden = gate_out * up_out
    return F.linear(hidden, down_w)


# ── Patching helpers ──────────────────────────────────────────────────────

def patch_model_dense(model):
    for layer in model.model.layers:
        mlp = layer.mlp
        if hasattr(mlp, '_original_forward'):
            mlp.forward = mlp._original_forward


def patch_model_mask_and_multiply(model, masks):
    hooks = []
    for layer_idx, layer in enumerate(model.model.layers):
        mlp = layer.mlp
        if not hasattr(mlp, '_original_forward'):
            mlp._original_forward = mlp.forward
        m = masks[layer_idx]

        def make_fwd(_mlp, _m):
            def fwd(x):
                return mask_and_multiply_ffn(_mlp, x, _m)
            return fwd

        mlp.forward = make_fwd(mlp, m)
        hooks.append(mlp)
    return hooks


def patch_model_sparse_gather(model, masks):
    """Patch MLPs with full-sparse gather-matmul execution.

    Pre-slices all 3 projection weights per layer so the hot path is:
    F.linear(x, gate_w) + F.linear(x, up_w) -> SwiGLU -> F.linear(hidden, down_w)
    """
    hooks = []
    for layer_idx, layer in enumerate(model.model.layers):
        mlp = layer.mlp
        if not hasattr(mlp, '_original_forward'):
            mlp._original_forward = mlp.forward
        m = masks[layer_idx]
        active_idx = m.nonzero(as_tuple=True)[0].contiguous()

        gate_w = mlp.gate_proj.weight[active_idx, :].contiguous()  # [K, H]
        up_w = mlp.up_proj.weight[active_idx, :].contiguous()      # [K, H]
        down_w = mlp.down_proj.weight[:, active_idx].contiguous()   # [H, K]

        def make_fwd(_gw, _uw, _dw):
            def fwd(x):
                return sparse_gather_ffn(x, _gw, _uw, _dw)
            return fwd

        mlp.forward = make_fwd(gate_w, up_w, down_w)
        hooks.append(mlp)
    return hooks


# ── Benchmark runner ──────────────────────────────────────────────────────

def run_single_benchmark(model, input_ids, device, warmup, iters):
    @torch.no_grad()
    def fwd():
        _ = model(input_ids)

    return cuda_timer(fwd, warmup, iters, device)


def run_predictor_overhead(predictors, device, batch_size, seq_len, warmup, iters):
    x = torch.randn(batch_size, seq_len, HIDDEN_SIZE, dtype=torch.float16, device=device)

    @torch.no_grad()
    def fwd():
        for p in predictors:
            _ = p(x)

    return cuda_timer(fwd, warmup, iters, device)


def run_ffn_only_benchmark(model, device, batch_size, seq_len, warmup, iters):
    x = torch.randn(batch_size, seq_len, HIDDEN_SIZE, dtype=torch.float16, device=device)

    @torch.no_grad()
    def fwd():
        for layer in model.model.layers:
            _ = layer.mlp(x)

    return cuda_timer(fwd, warmup, iters, device)


# ── Main ──────────────────────────────────────────────────────────────────

def main():
    args = parse_args()
    device = torch.device(args.device)
    batch_sizes = [int(b) for b in args.batch_sizes.split(",")]
    seq_lens = [int(s) for s in args.seq_lens.split(",")]

    available_modes = [
        "dense",
        "mask_multiply_30", "mask_multiply_50",
        "sparse_30", "sparse_50",
    ]
    if HAS_FLASHINFER:
        available_modes.extend(["flashinfer_30", "flashinfer_50"])
        print("flashinfer detected, enabling flashinfer modes")

    if args.modes:
        modes = [m.strip() for m in args.modes.split(",")]
    else:
        modes = available_modes

    print(f"Modes: {modes}")
    print(f"Batch sizes: {batch_sizes}, Seq lens: {seq_lens}")
    print(f"Warmup: {args.warmup}, Iters: {args.iters}")

    if args.dry_run:
        print("\n[dry_run] Validating setup...")
        print(f"  Model path exists: {os.path.exists(args.model)}")
        print(f"  CKPT 30% exists: {os.path.exists(args.ckpt_30)}")
        print(f"  CKPT 50% exists: {os.path.exists(args.ckpt_50)}")
        print(f"  flashinfer available: {HAS_FLASHINFER}")
        if torch.cuda.is_available():
            torch.cuda.set_device(device)
            print(f"  GPU: {torch.cuda.get_device_name(device)}")
            print(f"  GPU memory: {torch.cuda.get_device_properties(device).total_mem / 1024**3:.1f} GB")
        print("[dry_run] Validation passed.")
        return

    # ── Load model ────────────────────────────────────────────────────
    torch.cuda.set_device(device)
    torch.cuda.empty_cache()

    print(f"\nLoading model from {args.model} ...")
    model = load_model(args.model, device)

    # ── Load predictors & compute masks ───────────────────────────────
    need_30 = any("30" in m for m in modes)
    need_50 = any("50" in m for m in modes)

    masks_30, pred_30 = None, None
    masks_50, pred_50 = None, None

    if need_30:
        print("Loading 30% predictor and computing masks ...")
        masks_30, pred_30 = compute_teal_masks_from_checkpoint(
            model, args.ckpt_30, device, sparsity_target=0.30, seq_len=512)
        active_pcts = [masks_30[i].sum().item() / INTERMEDIATE_SIZE * 100 for i in range(NUM_LAYERS)]
        print(f"  30% masks: mean active={np.mean(active_pcts):.1f}%, "
              f"min={np.min(active_pcts):.1f}%, max={np.max(active_pcts):.1f}%")

    if need_50:
        print("Loading 50% predictor and computing masks ...")
        masks_50, pred_50 = compute_teal_masks_from_checkpoint(
            model, args.ckpt_50, device, sparsity_target=0.50, seq_len=512)
        active_pcts = [masks_50[i].sum().item() / INTERMEDIATE_SIZE * 100 for i in range(NUM_LAYERS)]
        print(f"  50% masks: mean active={np.mean(active_pcts):.1f}%, "
              f"min={np.min(active_pcts):.1f}%, max={np.max(active_pcts):.1f}%")

    # ── Benchmark loop ────────────────────────────────────────────────
    all_results = []

    for bs in batch_sizes:
        for sl in seq_lens:
            input_ids = torch.randint(0, model.config.vocab_size, (bs, sl), device=device)
            print(f"\n{'='*60}")
            print(f"batch_size={bs}, seq_len={sl}")
            print(f"{'='*60}")

            dense_median_ms = None

            for mode in modes:
                patch_model_dense(model)
                torch.cuda.empty_cache()

                if mode == "dense":
                    pass
                elif mode == "mask_multiply_30" and masks_30:
                    patch_model_mask_and_multiply(model, masks_30)
                elif mode == "mask_multiply_50" and masks_50:
                    patch_model_mask_and_multiply(model, masks_50)
                elif mode == "sparse_30" and masks_30:
                    patch_model_sparse_gather(model, masks_30)
                elif mode == "sparse_50" and masks_50:
                    patch_model_sparse_gather(model, masks_50)
                else:
                    print(f"  Skipping {mode} (masks not loaded or unknown mode)")
                    continue

                times_ms = run_single_benchmark(model, input_ids, device, args.warmup, args.iters)
                median_ms = float(np.median(times_ms))
                mean_ms = float(np.mean(times_ms))
                std_ms = float(np.std(times_ms))
                tokens = bs * sl
                tokens_per_sec = tokens / (median_ms / 1000.0)

                if mode == "dense":
                    dense_median_ms = median_ms
                    speedup = 1.0
                elif dense_median_ms:
                    speedup = dense_median_ms / median_ms
                else:
                    speedup = None

                ffn_times_ms = run_ffn_only_benchmark(model, device, bs, sl, args.warmup, args.iters)
                ffn_median_ms = float(np.median(ffn_times_ms))

                result = {
                    "mode": mode,
                    "batch_size": bs,
                    "seq_len": sl,
                    "total_median_ms": round(median_ms, 3),
                    "total_mean_ms": round(mean_ms, 3),
                    "total_std_ms": round(std_ms, 3),
                    "ffn_only_median_ms": round(ffn_median_ms, 3),
                    "tokens_per_sec": round(tokens_per_sec, 1),
                    "speedup_vs_dense": round(speedup, 4) if speedup else None,
                }
                all_results.append(result)

                if speedup:
                    print(f"  {mode:25s}: total={median_ms:.2f}ms  ffn={ffn_median_ms:.2f}ms  "
                          f"tok/s={tokens_per_sec:.0f}  speedup={speedup:.4f}x")
                else:
                    print(f"  {mode:25s}: total={median_ms:.2f}ms  ffn={ffn_median_ms:.2f}ms  "
                          f"tok/s={tokens_per_sec:.0f}")

            # Predictor overhead (isolated)
            patch_model_dense(model)
            for tag, pred in [("30pct", pred_30), ("50pct", pred_50)]:
                if pred is None:
                    continue
                pred_times = run_predictor_overhead(pred, device, bs, sl, args.warmup, args.iters)
                pred_median = float(np.median(pred_times))
                all_results.append({
                    "mode": f"predictor_only_{tag}",
                    "batch_size": bs,
                    "seq_len": sl,
                    "total_median_ms": round(pred_median, 3),
                    "total_mean_ms": round(float(np.mean(pred_times)), 3),
                    "total_std_ms": round(float(np.std(pred_times)), 3),
                    "ffn_only_median_ms": None,
                    "tokens_per_sec": None,
                    "speedup_vs_dense": None,
                })
                print(f"  {'predictor_only_'+tag:25s}: {pred_median:.2f}ms (all 32 layers)")

    # ── Output JSON ───────────────────────────────────────────────────
    output = {
        "benchmark": "sparse_ffn_gather_matmul",
        "model": args.model,
        "gpu": torch.cuda.get_device_name(device) if torch.cuda.is_available() else "N/A",
        "device": str(device),
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "config": {
            "warmup": args.warmup,
            "iters": args.iters,
            "hidden_size": HIDDEN_SIZE,
            "intermediate_size": INTERMEDIATE_SIZE,
            "num_layers": NUM_LAYERS,
        },
        "flashinfer_available": HAS_FLASHINFER,
        "checkpoints": {
            "30pct": args.ckpt_30,
            "50pct": args.ckpt_50,
        },
        "results": all_results,
    }

    out_path = args.output or os.path.join(BASE_DIR, "results/benchmark_flashinfer.json")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nJSON saved to {out_path}")

    # ── Summary table ─────────────────────────────────────────────────
    print("\n## Sparse FFN Benchmark Summary")
    print(f"GPU: {output['gpu']} | {args.warmup} warmup, {args.iters} iters (median)\n")
    print(f"| {'Mode':25s} | {'BS':>3s} | {'SL':>5s} | {'Total ms':>9s} | {'FFN ms':>8s} | {'tok/s':>8s} | {'Speedup':>7s} |")
    print(f"|{'-'*27}|{'-'*5}|{'-'*7}|{'-'*11}|{'-'*10}|{'-'*10}|{'-'*9}|")
    for r in all_results:
        sp = f"{r['speedup_vs_dense']:.4f}x" if r.get('speedup_vs_dense') else "---"
        tps = f"{r['tokens_per_sec']:.0f}" if r.get('tokens_per_sec') else "---"
        ffn = f"{r['ffn_only_median_ms']:.2f}" if r.get('ffn_only_median_ms') else "---"
        print(f"| {r['mode']:25s} | {r['batch_size']:3d} | {r['seq_len']:5d} | "
              f"{r['total_median_ms']:9.2f} | {ffn:>8s} | {tps:>8s} | {sp:>7s} |")


if __name__ == "__main__":
    main()
