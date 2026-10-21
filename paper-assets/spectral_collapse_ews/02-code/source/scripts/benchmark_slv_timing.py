"""Benchmark SLV computation vs HellaSwag 0-shot evaluation time."""
import os
import time
import json
import torch
import numpy as np

os.environ["TOKENIZERS_PARALLELISM"] = "false"
os.environ["HF_HOME"] = "/root/autodl-tmp/.hf_cache"

MODEL_NAME = "EleutherAI/pythia-410m-deduped"
N_SAMPLES = 1000
MAX_LENGTH = 512
SLV_RUNS = 3
DEVICE = "cuda:0" if torch.cuda.is_available() else "cpu"


def load_texts(n_samples):
    """Load text samples from cached datasets, with fallback."""
    from datasets import load_dataset
    try:
        ds = load_dataset("monology/pile-uncopyrighted", split="train", streaming=True)
        texts = []
        for ex in ds:
            t = ex.get("text", "")
            if len(t.strip()) > 50:
                texts.append(t[:2000])
            if len(texts) >= n_samples:
                break
        if len(texts) >= n_samples:
            return texts
    except Exception as e:
        print(f"  pile-uncopyrighted failed: {e}")

    try:
        ds = load_dataset("wikitext", "wikitext-103-raw-v1", split="test")
        texts = [t for t in ds["text"] if len(t.strip()) > 50][:n_samples]
        if len(texts) >= n_samples:
            return texts
    except Exception as e:
        print(f"  wikitext failed: {e}")

    print("  Using synthetic data for timing benchmark")
    from transformers import AutoTokenizer
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    vocab_size = tokenizer.vocab_size
    texts = []
    for _ in range(n_samples):
        ids = torch.randint(100, vocab_size, (256,))
        texts.append(tokenizer.decode(ids))
    return texts


def measure_slv(model, tokenizer, texts, device):
    """Forward pass + SVD, return (total_time, forward_time, svd_time)."""
    model.eval()
    embeddings = []

    t_fwd_start = time.time()
    with torch.no_grad():
        for i in range(0, len(texts), 16):
            batch_texts = texts[i:i+16]
            inputs = tokenizer(
                batch_texts, return_tensors="pt", padding=True,
                truncation=True, max_length=MAX_LENGTH
            ).to(device)
            outputs = model(**inputs, output_hidden_states=True)
            last_hidden = outputs.hidden_states[-1]
            mask = inputs["attention_mask"].unsqueeze(-1)
            mean_emb = (last_hidden * mask).sum(dim=1) / mask.sum(dim=1)
            embeddings.append(mean_emb.cpu())
    t_fwd_end = time.time()

    E = torch.cat(embeddings, dim=0).float()  # (N, d)

    t_svd_start = time.time()
    sv = torch.linalg.svdvals(E)
    slv = torch.sum(torch.log(sv[sv > 0])).item()
    t_svd_end = time.time()

    forward_time = t_fwd_end - t_fwd_start
    svd_time = t_svd_end - t_svd_start
    total_time = forward_time + svd_time
    return total_time, forward_time, svd_time, slv


def measure_hellaswag(device):
    """Run HellaSwag 0-shot via lm_eval Python API."""
    import lm_eval
    t0 = time.time()
    results = lm_eval.simple_evaluate(
        model="hf",
        model_args=f"pretrained={MODEL_NAME},device={device}",
        tasks=["hellaswag"],
        num_fewshot=0,
        batch_size=16,
    )
    t1 = time.time()
    acc = results["results"]["hellaswag"]["acc_norm,none"]
    return t1 - t0, acc


def main():
    print(f"Device: {DEVICE}")
    if DEVICE.startswith("cuda"):
        print(f"GPU: {torch.cuda.get_device_name(0)}")
        print(f"GPU memory: {torch.cuda.get_device_properties(0).total_memory / 1024**3:.1f} GB")

    from transformers import AutoModelForCausalLM, AutoTokenizer

    print(f"\n--- Loading model: {MODEL_NAME} ---")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    model = AutoModelForCausalLM.from_pretrained(MODEL_NAME).to(DEVICE)

    print(f"\n--- Loading {N_SAMPLES} text samples ---")
    texts = load_texts(N_SAMPLES)
    print(f"Got {len(texts)} texts")

    print(f"\n--- SLV benchmark ({SLV_RUNS} runs) ---")
    slv_times = []
    fwd_times = []
    svd_times = []
    for run in range(SLV_RUNS):
        total, fwd, svd, slv_val = measure_slv(model, tokenizer, texts, DEVICE)
        slv_times.append(total)
        fwd_times.append(fwd)
        svd_times.append(svd)
        print(f"  Run {run+1}: total={total:.2f}s (fwd={fwd:.2f}s, svd={svd:.4f}s), SLV={slv_val:.2f}")

    del model
    if DEVICE.startswith("cuda"):
        torch.cuda.empty_cache()

    print(f"\n--- HellaSwag 0-shot benchmark ---")
    hs_time, hs_acc = measure_hellaswag(DEVICE)
    print(f"  HellaSwag time: {hs_time:.2f}s, acc_norm: {hs_acc:.4f}")

    slv_mean = np.mean(slv_times)
    slv_std = np.std(slv_times)
    fwd_mean = np.mean(fwd_times)
    svd_mean = np.mean(svd_times)

    print("\n" + "="*60)
    print("RESULTS")
    print("="*60)
    print(f"SLV computation: {slv_mean:.2f} ± {slv_std:.2f} seconds ({SLV_RUNS} runs, device={DEVICE})")
    print(f"  - Forward pass: {fwd_mean:.2f} seconds")
    print(f"  - SVD: {svd_mean:.4f} seconds")
    print(f"HellaSwag 0-shot: {hs_time:.2f} seconds ({hs_time/60:.2f} minutes) (1 run, device={DEVICE})")
    print(f"Speedup: {hs_time / slv_mean:.1f}×")
    if DEVICE.startswith("cuda"):
        gpu_name = torch.cuda.get_device_name(0)
    else:
        gpu_name = "CPU"
    print(f"Device: {gpu_name}")
    print(f"HellaSwag acc_norm: {hs_acc:.4f}")

    results = {
        "slv_mean_s": round(slv_mean, 2),
        "slv_std_s": round(slv_std, 2),
        "forward_mean_s": round(fwd_mean, 2),
        "svd_mean_s": round(svd_mean, 4),
        "hellaswag_time_s": round(hs_time, 2),
        "hellaswag_acc_norm": round(hs_acc, 4),
        "speedup": round(hs_time / slv_mean, 1),
        "device": DEVICE,
        "gpu_name": gpu_name if DEVICE.startswith("cuda") else "CPU",
        "model": MODEL_NAME,
        "n_samples": N_SAMPLES,
        "slv_runs": SLV_RUNS,
    }
    out_path = "/root/spectral_collapse_ews/results/benchmark_slv_timing.json"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to {out_path}")


if __name__ == "__main__":
    main()
