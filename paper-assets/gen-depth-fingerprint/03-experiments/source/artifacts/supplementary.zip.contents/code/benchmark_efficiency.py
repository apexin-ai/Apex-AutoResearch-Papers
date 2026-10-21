"""Efficiency benchmark: 7-feature ensemble vs 4-det+surface."""
import argparse
import json, time, gc, os
import numpy as np
import torch
import torch.nn.functional as F
from collections import Counter
from pathlib import Path
from scipy.sparse import lil_matrix
from transformers import AutoModelForCausalLM, AutoTokenizer

MAX_LEN = 512
N_SAMPLES = 100
WARMUP = 5

ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT.parent / "data"
RESULTS_DIR = ROOT / "results"


def load_sample_texts(n=N_SAMPLES):
    texts = []
    with open(DATA_DIR / "generations.jsonl") as f:
        for i, line in enumerate(f):
            if i >= n:
                break
            texts.append(json.loads(line)["text"])
    return texts


def get_gpu_memory_mb(device):
    torch.cuda.synchronize()
    return torch.cuda.max_memory_allocated(device) / 1024 / 1024


def reset_gpu_stats(device):
    torch.cuda.reset_peak_memory_stats(device)
    torch.cuda.empty_cache()
    gc.collect()


# ================================================================
# Method 1: 7-feature ensemble
# ================================================================

def benchmark_7feature(texts, tokenizer, model, device):
    """1x reference model forward pass -> 5 ref features + 2 surface features."""
    reset_gpu_stats(device)

    for t in texts[:WARMUP]:
        enc = tokenizer([t], return_tensors="pt", truncation=True, max_length=MAX_LEN, padding=True).to(device)
        with torch.no_grad():
            logits = model(**enc).logits
    torch.cuda.synchronize()
    reset_gpu_stats(device)

    torch.cuda.synchronize()
    t0 = time.perf_counter()
    seq_lens = []

    for text in texts:
        enc = tokenizer([text], return_tensors="pt", truncation=True, max_length=MAX_LEN, padding=True).to(device)
        with torch.no_grad():
            logits = model(**enc).logits

        mask = enc["attention_mask"][0].bool()
        seq_len = mask.sum().item()
        seq_lens.append(seq_len)

        if seq_len < 2:
            continue

        token_logits = logits[0, :seq_len - 1, :]
        log_probs = torch.log_softmax(token_logits, dim=-1)
        probs = torch.exp(log_probs)
        entropy = -(probs * log_probs).sum(dim=-1)
        entropy_np = entropy.float().cpu().numpy()

        _ = float(np.mean(entropy_np))
        _ = float(np.std(entropy_np))
        _ = float(np.min(entropy_np))
        _ = float(np.max(entropy_np))

        avg_lp = log_probs.float().mean(dim=0)
        sorted_lp, _ = torch.sort(avg_lp, descending=True)
        sorted_np = sorted_lp.cpu().numpy()
        V = sorted_np.shape[0]
        hi = min(1000, V)
        lo = min(100, hi)
        if hi - lo >= 2:
            x = np.arange(lo, hi, dtype=np.float64)
            y = sorted_np[lo:hi].astype(np.float64)
            _ = float(np.polyfit(x, y, 1)[0])

        words = text.lower().split()
        n = len(words)
        if n > 0:
            counter = Counter(words)
            _ = len(counter) / n
            _ = sum(1 for c in counter.values() if c == 1) / n

    torch.cuda.synchronize()
    elapsed = time.perf_counter() - t0
    peak_mem = get_gpu_memory_mb(device)

    return {
        "total_time_s": round(elapsed, 3),
        "per_text_ms": round(elapsed / len(texts) * 1000, 2),
        "gpu_memory_mb": round(peak_mem, 1),
        "avg_seq_len": round(np.mean(seq_lens), 1),
    }


# ================================================================
# Method 2: 4-det+surface
# ================================================================

def benchmark_4det_surface(texts, tokenizer_410m, model_410m, model_1b, device):
    """
    Avg-LogProb + FastDetectGPT: 1x observer pass
    Binoculars: 1x observer + 1x performer pass
    LD-Score: CPU trigram JSD
    Surface: CPU TTR + hapax
    """
    reset_gpu_stats(device)

    for t in texts[:WARMUP]:
        enc = tokenizer_410m([t], return_tensors="pt", truncation=True, max_length=MAX_LEN, padding=True).to(device)
        with torch.no_grad():
            _ = model_410m(**enc).logits
            _ = model_1b(**enc).logits
    torch.cuda.synchronize()
    reset_gpu_stats(device)

    # Part A: FDG + LogProb (1x observer)
    torch.cuda.synchronize()
    t0 = time.perf_counter()

    for text in texts:
        enc = tokenizer_410m([text], return_tensors="pt", truncation=True, max_length=MAX_LEN, padding=True).to(device)
        with torch.no_grad():
            logits = model_410m(**enc).logits

        log_p = F.log_softmax(logits[:, :-1], dim=-1)
        tgt = enc["input_ids"][:, 1:]
        mask = enc["attention_mask"][:, 1:].bool()
        actual = log_p.gather(2, tgt.unsqueeze(-1)).squeeze(-1)
        expected = (log_p.exp() * log_p).sum(-1)
        curv = actual - expected

        m = mask[0]
        if m.sum() >= 2:
            c = curv[0][m]
            mc, sc = c.mean().item(), c.std().item()
            _ = mc / (sc + 1e-8) if sc > 1e-8 else mc  # FDG
            _ = actual[0][m].mean().item()  # Avg-LogProb

    torch.cuda.synchronize()
    time_fdg_lp = time.perf_counter() - t0
    mem_after_fdg = get_gpu_memory_mb(device)

    # Part B: Binoculars (1x observer + 1x performer)
    torch.cuda.synchronize()
    t1 = time.perf_counter()

    for text in texts:
        enc = tokenizer_410m([text], return_tensors="pt", truncation=True, max_length=MAX_LEN, padding=True).to(device)
        with torch.no_grad():
            o_logits = model_410m(**enc).logits[:, :-1].contiguous()
            p_logits = model_1b(**enc).logits[:, :-1].contiguous()

        ids = enc["input_ids"][:, 1:].contiguous()
        mask = enc["attention_mask"][:, 1:].float()

        o_ce = F.cross_entropy(o_logits.view(-1, o_logits.size(-1)), ids.view(-1), reduction="none").view(ids.shape)
        p_ce = F.cross_entropy(p_logits.view(-1, p_logits.size(-1)), ids.view(-1), reduction="none").view(ids.shape)

        m = mask[0]
        if m.sum() >= 2:
            o_val = (o_ce[0] * m).sum() / m.sum()
            p_val = (p_ce[0] * m).sum() / m.sum()
            _ = (o_val / (p_val + 1e-8)).item()

    torch.cuda.synchronize()
    time_bino = time.perf_counter() - t1
    mem_after_bino = get_gpu_memory_mb(device)

    # Part C: LD-Score (CPU trigram JSD)
    t2 = time.perf_counter()

    vocab = {}
    rows_data = []
    for text in texts:
        t_lower = text.lower()
        c = Counter(t_lower[j:j+3] for j in range(len(t_lower) - 2))
        for ng in c:
            if ng not in vocab:
                vocab[ng] = len(vocab)
        rows_data.append(c)

    V = len(vocab)
    mat = lil_matrix((len(texts), V), dtype=np.float64)
    for i, c in enumerate(rows_data):
        total = sum(c.values())
        if total > 0:
            for ng, cnt in c.items():
                mat[i, vocab[ng]] = cnt / total
    mat_csr = mat.tocsr()

    ref_mask = np.zeros(len(texts), dtype=bool)
    ref_mask[:len(texts)//5] = True
    ref_dist = np.asarray(mat_csr[ref_mask].mean(axis=0)).flatten()
    ref_sum = ref_dist.sum()
    if ref_sum > 0:
        ref_dist /= ref_sum

    h_q = -np.sum(ref_dist[ref_dist > 0] * np.log(ref_dist[ref_dist > 0]))
    batch = mat_csr.toarray()
    row_sums = batch.sum(axis=1, keepdims=True)
    row_sums[row_sums == 0] = 1
    batch = batch / row_sums
    safe_batch = np.where(batch > 0, batch, 1.0)
    h_p = -np.sum(batch * np.log(safe_batch), axis=1)
    m_dist = (batch + ref_dist[np.newaxis, :]) / 2.0
    safe_m = np.where(m_dist > 0, m_dist, 1.0)
    h_m = -np.sum(m_dist * np.log(safe_m), axis=1)
    jsd_sq = np.clip(h_m - (h_p + h_q) / 2.0, 0, None)
    _ = np.sqrt(jsd_sq)

    time_ld = time.perf_counter() - t2

    # Part D: Surface features (CPU)
    t3 = time.perf_counter()
    for text in texts:
        words = text.lower().split()
        n = len(words)
        if n > 0:
            counter = Counter(words)
            _ = len(counter) / n
            _ = sum(1 for c in counter.values() if c == 1) / n
    time_surface = time.perf_counter() - t3

    total_time = time_fdg_lp + time_bino + time_ld + time_surface

    return {
        "total_time_s": round(total_time, 3),
        "per_text_ms": round(total_time / len(texts) * 1000, 2),
        "gpu_memory_mb": round(mem_after_bino, 1),
        "breakdown": {
            "fdg_logprob_s": round(time_fdg_lp, 3),
            "binoculars_s": round(time_bino, 3),
            "ld_score_s": round(time_ld, 3),
            "surface_s": round(time_surface, 3),
        }
    }


# ================================================================
# Main
# ================================================================

def main():
    parser = argparse.ArgumentParser(description="Efficiency benchmark: 7-feature vs 4-det+surface")
    parser.add_argument("--ref-model", type=str, required=True,
                        help="Path to observer/reference model (e.g. Pythia-410M)")
    parser.add_argument("--performer-model", type=str, required=True,
                        help="Path to performer model for Binoculars (e.g. Pythia-1B)")
    parser.add_argument("--device", type=str, default="cuda:0")
    args = parser.parse_args()

    device = args.device

    print("=" * 60)
    print("Efficiency Benchmark: 7-feature vs 4-det+surface")
    print("=" * 60)

    texts = load_sample_texts(N_SAMPLES)
    print(f"Loaded {len(texts)} sample texts")
    avg_words = np.mean([len(t.split()) for t in texts])
    print(f"Avg word count: {avg_words:.1f}")

    # Benchmark 7-feature
    print("\n[1] Loading reference model for 7-feature benchmark...")
    tokenizer_410m = AutoTokenizer.from_pretrained(args.ref_model)
    if tokenizer_410m.pad_token is None:
        tokenizer_410m.pad_token = tokenizer_410m.eos_token
    model_410m = AutoModelForCausalLM.from_pretrained(args.ref_model, torch_dtype=torch.float16)
    model_410m.to(device).eval()

    torch.cuda.synchronize()
    mem_410m = torch.cuda.max_memory_allocated(device) / 1024 / 1024
    print(f"  Reference model loaded: {mem_410m:.0f} MB")

    print("\n[2] Benchmarking 7-feature ensemble...")
    result_7feat = benchmark_7feature(texts, tokenizer_410m, model_410m, device)
    print(f"  Done: {result_7feat['per_text_ms']:.2f} ms/text, peak {result_7feat['gpu_memory_mb']:.0f} MB")
    print(f"  Avg seq len: {result_7feat['avg_seq_len']}")

    # Benchmark 4-det+surface
    print("\n[3] Loading performer model for 4-det+surface benchmark...")
    reset_gpu_stats(device)
    model_1b = AutoModelForCausalLM.from_pretrained(args.performer_model, torch_dtype=torch.float16)
    model_1b.to(device).eval()

    torch.cuda.synchronize()
    mem_both = torch.cuda.max_memory_allocated(device) / 1024 / 1024
    print(f"  Both models loaded: {mem_both:.0f} MB")

    print("\n[4] Benchmarking 4-det+surface...")
    result_4det = benchmark_4det_surface(texts, tokenizer_410m, model_410m, model_1b, device)
    print(f"  Done: {result_4det['per_text_ms']:.2f} ms/text, peak {result_4det['gpu_memory_mb']:.0f} MB")
    print(f"  Breakdown: {result_4det['breakdown']}")

    # Cleanup
    del model_410m, model_1b, tokenizer_410m
    torch.cuda.empty_cache()

    # FLOP estimates
    params_410m = 410e6
    params_1b = 1e9
    avg_seq_len = result_7feat["avg_seq_len"]

    flops_7feat = 2 * params_410m * avg_seq_len
    flops_4det_optimized = 2 * params_410m * avg_seq_len + 2 * params_1b * avg_seq_len
    flops_4det_naive = 2 * (2 * params_410m * avg_seq_len) + 2 * params_1b * avg_seq_len

    speedup = result_4det["per_text_ms"] / result_7feat["per_text_ms"]

    output = {
        "benchmark_config": {
            "n_samples": N_SAMPLES,
            "warmup_samples": WARMUP,
            "max_seq_len": MAX_LEN,
            "avg_seq_len": avg_seq_len,
            "dtype": "float16",
        },
        "methods": {
            "7_feature_ensemble": {
                "model_params_total": "410M",
                "forward_passes_per_text": 1,
                "gpu_memory_mb": round(mem_410m, 1),
                "inference_gpu_memory_mb": result_7feat["gpu_memory_mb"],
                "wall_clock_ms_per_text": result_7feat["per_text_ms"],
                "total_time_100_texts_s": result_7feat["total_time_s"],
                "flops_per_text": f"{flops_7feat:.2e}",
                "features": {
                    "reference (GPU)": ["entropy_mean", "entropy_std", "entropy_min", "entropy_max", "tail_decay"],
                    "surface (CPU)": ["ttr", "hapax_ratio"],
                },
            },
            "4_det_plus_surface": {
                "model_params_total": "1.41B",
                "forward_passes_per_text": "3 naive (2x observer + 1x performer) or 2 optimized (1x observer + 1x performer)",
                "gpu_memory_mb": round(mem_both, 1),
                "inference_gpu_memory_mb": result_4det["gpu_memory_mb"],
                "wall_clock_ms_per_text": result_4det["per_text_ms"],
                "total_time_100_texts_s": result_4det["total_time_s"],
                "flops_per_text_optimized": f"{flops_4det_optimized:.2e}",
                "flops_per_text_naive": f"{flops_4det_naive:.2e}",
                "time_breakdown_s": result_4det["breakdown"],
                "detectors": {
                    "avg_logprob": "1x observer forward pass",
                    "fastdetectgpt": "same observer pass (shared)",
                    "binoculars": "1x observer + 1x performer",
                    "ld_score": "CPU trigram JSD (no GPU model)",
                    "surface": "TTR + hapax_ratio (CPU string ops)",
                },
            },
        },
        "comparison": {
            "speedup_ratio": round(speedup, 2),
            "memory_ratio": round(mem_both / mem_410m, 2),
            "flop_ratio_optimized": round(flops_4det_optimized / flops_7feat, 2),
            "flop_ratio_naive": round(flops_4det_naive / flops_7feat, 2),
            "parameter_ratio": round(1.41e9 / 410e6, 2),
        },
    }

    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"{'Metric':<35s} {'7-feature':>15s} {'4-det+surface':>15s}")
    print("-" * 67)
    print(f"{'Models loaded':<35s} {'1':>15s} {'2':>15s}")
    print(f"{'Total params':<35s} {'410M':>15s} {'1.41B':>15s}")
    print(f"{'Forward passes/text':<35s} {'1':>15s} {'3 (naive)':>15s}")
    print(f"{'GPU memory (MB)':<35s} {result_7feat['gpu_memory_mb']:>15.0f} {result_4det['gpu_memory_mb']:>15.0f}")
    print(f"{'Wall-clock (ms/text)':<35s} {result_7feat['per_text_ms']:>15.2f} {result_4det['per_text_ms']:>15.2f}")
    print(f"{'Speedup (4det/7feat)':<35s} {'':>15s} {speedup:>15.2f}x")
    print(f"{'FLOPs/text (optimized)':<35s} {flops_7feat:>15.2e} {flops_4det_optimized:>15.2e}")

    RESULTS_DIR.mkdir(exist_ok=True)
    out_path = RESULTS_DIR / "efficiency_comparison.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    print(f"\nSaved: {out_path}")


if __name__ == "__main__":
    main()
