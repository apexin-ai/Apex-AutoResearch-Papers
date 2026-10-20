"""
Runtime benchmark: OBD pipeline vs baselines (Binoculars, DivEye, Neural Probe).
Measures per-document latency on the same 1000 documents, same GPU.
Usage: python scripts/runtime_benchmark.py
"""

import csv
import gc
import json
import math
import os
import time
from collections import Counter
from pathlib import Path

import numpy as np
import torch
import torch.nn as nn
from scipy import stats

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
MODEL_QWEN = "/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B-Instruct"
MODEL_PYTHIA = "/root/autodl-tmp/.hf_cache/models--EleutherAI--pythia-1.4b/snapshots/fedc38a16eea3bd36a96b906d78d11d2ce18ed79"
MODEL_OLMO = "/root/autodl-tmp/.hf_cache/allenai/OLMo-1B-hf"
DATA_PATH = "/root/autodl-tmp/gen-depth-contamination/data/exp_qwen_cont_10k/depth_0.jsonl"
FEATURES_CSV = "/root/autodl-tmp/gen-depth-contamination/data/exp_qwen_cont_10k/features.csv"
OUT_DIR = Path("/root/autodl-tmp/gen-depth-contamination/results/runtime_benchmark")
N_DOCS = 1000
N_WARMUP = 10
DEVICE = "cuda:0"
MAX_LENGTH = 512

SURPRISAL_COLS = [
    "surp_mean", "surp_std", "surp_skew", "surp_kurt",
    "surp_d1_mean", "surp_d1_std", "surp_d1_skew",
    "surp_d2_mean", "surp_d2_std",
]
VOCAB_COLS = ["ttr", "hapax_ratio", "self_bleu"]
TAIL_COLS = ["freq_kurtosis", "freq_entropy", "low_freq_ratio"]
ALL_FEAT_COLS = SURPRISAL_COLS + VOCAB_COLS + TAIL_COLS


# ---------------------------------------------------------------------------
# Utilities
# ---------------------------------------------------------------------------

def stat_dict(arr):
    return {
        "mean": round(float(np.mean(arr)), 3),
        "std": round(float(np.std(arr)), 3),
        "median": round(float(np.median(arr)), 3),
        "p5": round(float(np.percentile(arr, 5)), 3),
        "p95": round(float(np.percentile(arr, 95)), 3),
    }


def load_causal_model(path, device=DEVICE):
    from transformers import AutoModelForCausalLM, AutoTokenizer
    tok = AutoTokenizer.from_pretrained(path, trust_remote_code=True)
    if tok.pad_token is None:
        tok.pad_token = tok.eos_token
        tok.pad_token_id = tok.eos_token_id
    model = AutoModelForCausalLM.from_pretrained(
        path, torch_dtype=torch.float16, device_map=device,
        trust_remote_code=True,
    )
    model.eval()
    return model, tok


def free_model(model):
    del model
    gc.collect()
    torch.cuda.empty_cache()


def ngrams(tokens, n):
    return [tuple(tokens[i : i + n]) for i in range(len(tokens) - n + 1)]


def simple_bleu(candidate_tokens, reference_tokens, max_n=4):
    if len(candidate_tokens) == 0:
        return 0.0
    precisions = []
    for n in range(1, max_n + 1):
        cand_ngrams = ngrams(candidate_tokens, n)
        ref_ngrams = ngrams(reference_tokens, n)
        if not cand_ngrams:
            precisions.append(0.0)
            continue
        ref_counts = Counter(ref_ngrams)
        clipped = 0
        cand_counts = Counter(cand_ngrams)
        for ng, cnt in cand_counts.items():
            clipped += min(cnt, ref_counts.get(ng, 0))
        precisions.append(clipped / len(cand_ngrams))
    if any(p == 0 for p in precisions):
        return 0.0
    log_avg = sum(math.log(p) for p in precisions) / max_n
    bp = min(1.0, math.exp(1 - len(reference_tokens) / max(len(candidate_tokens), 1)))
    return bp * math.exp(log_avg)


# ---------------------------------------------------------------------------
# OBD Pipeline
# ---------------------------------------------------------------------------

def obd_scorer_single(model, tokenizer, text):
    inputs = tokenizer(
        [text], return_tensors="pt", padding=False, truncation=True, max_length=MAX_LENGTH
    ).to(model.device)

    start_ev = torch.cuda.Event(enable_timing=True)
    end_ev = torch.cuda.Event(enable_timing=True)
    torch.cuda.synchronize()
    start_ev.record()

    with torch.no_grad():
        logits = model(**inputs).logits

    log_probs = torch.log_softmax(logits, dim=-1)
    input_ids = inputs["input_ids"]
    seq_len = inputs["attention_mask"].sum().item()

    token_lp = []
    for t in range(1, int(seq_len)):
        lp = log_probs[0, t - 1, input_ids[0, t]].item()
        token_lp.append(-lp)

    arr = np.array(token_lp)
    if len(arr) >= 3:
        d1 = np.diff(arr)
        d2 = np.diff(d1) if len(d1) > 1 else np.array([0.0])
        feats = [
            float(np.mean(arr)), float(np.std(arr)),
            float(stats.skew(arr)), float(stats.kurtosis(arr)),
            float(np.mean(d1)), float(np.std(d1)),
            float(stats.skew(d1)) if len(d1) >= 3 else 0.0,
            float(np.mean(d2)), float(np.std(d2)),
        ]
    else:
        feats = [0.0] * 9

    end_ev.record()
    torch.cuda.synchronize()
    gpu_ms = start_ev.elapsed_time(end_ev)
    return feats, gpu_ms


def obd_cpu_features(text, tokens_word, ref_pool_tokens, rng_seed=0):
    start = time.perf_counter()
    total = len(tokens_word)
    if total == 0:
        return [0.0] * 6, (time.perf_counter() - start) * 1000

    unique = set(tokens_word)
    ttr = len(unique) / total
    freq = Counter(tokens_word)
    hapax = sum(1 for v in freq.values() if v == 1)
    hapax_ratio = hapax / max(len(unique), 1)

    rng_local = np.random.RandomState(rng_seed)
    n_refs = min(100, len(ref_pool_tokens))
    ref_idx = rng_local.choice(len(ref_pool_tokens), n_refs, replace=False)
    bleu_scores = [simple_bleu(tokens_word, ref_pool_tokens[j]) for j in ref_idx]
    self_bleu = float(np.mean(bleu_scores)) if bleu_scores else 0.0

    counts = np.array(list(freq.values()), dtype=float)
    kurt = float(stats.kurtosis(counts)) if len(counts) >= 4 else 0.0
    total_c = counts.sum()
    probs = counts / total_c
    entropy = float(-np.sum(probs * np.log2(probs + 1e-12)))
    low_freq_ratio = float(np.sum(counts <= 2)) / max(len(counts), 1)

    elapsed = (time.perf_counter() - start) * 1000
    return [ttr, hapax_ratio, self_bleu, kurt, entropy, low_freq_ratio], elapsed


def train_lgbm_model(features_csv_path):
    import lightgbm as lgb
    with open(features_csv_path) as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    X_list, y_list = [], []
    for r in rows:
        d = int(r["depth"])
        if d > 1:
            continue
        feats = [float(r[c]) if r[c] not in ("", "nan") else 0.0 for c in ALL_FEAT_COLS]
        X_list.append(feats)
        y_list.append(d)

    X = np.array(X_list)
    y = np.array(y_list)
    X[np.isnan(X)] = 0.0

    clf = lgb.LGBMClassifier(
        n_estimators=200, max_depth=6, learning_rate=0.05,
        num_leaves=31, verbose=-1, n_jobs=-1,
    )
    clf.fit(X, y)
    return clf


def bench_lgbm_single(clf, fv_15d):
    x = np.array(fv_15d).reshape(1, -1)
    start = time.perf_counter()
    clf.predict_proba(x)
    return (time.perf_counter() - start) * 1000


def benchmark_obd(docs, all_tokens_word, model, tokenizer, clf):
    print(f"\n[OBD] Warmup {N_WARMUP} docs ...")
    for i in range(N_WARMUP):
        obd_scorer_single(model, tokenizer, docs[i])
        obd_cpu_features(docs[i], all_tokens_word[i], all_tokens_word, rng_seed=i)
        bench_lgbm_single(clf, [0.0] * 15)
    torch.cuda.empty_cache()

    scorer_times, cpu_times, lgbm_times = [], [], []
    print(f"[OBD] Benchmarking {N_DOCS} docs ...")
    for i in range(N_DOCS):
        if (i + 1) % 200 == 0:
            print(f"  [{i+1}/{N_DOCS}]")
        surp_feats, gpu_ms = obd_scorer_single(model, tokenizer, docs[i])
        scorer_times.append(gpu_ms)
        cpu_feats, cpu_ms = obd_cpu_features(docs[i], all_tokens_word[i], all_tokens_word, rng_seed=i)
        cpu_times.append(cpu_ms)
        fv = surp_feats + cpu_feats
        lgbm_times.append(bench_lgbm_single(clf, fv))

    scorer_arr = np.array(scorer_times)
    cpu_arr = np.array(cpu_times)
    lgbm_arr = np.array(lgbm_times)
    total_arr = scorer_arr + cpu_arr + lgbm_arr

    gpu_mem = torch.cuda.max_memory_allocated(DEVICE) / 1024**2

    return {
        "feature_extraction_ms_per_doc": stat_dict(scorer_arr + cpu_arr),
        "classifier_ms_per_doc": stat_dict(lgbm_arr),
        "total_ms_per_doc": stat_dict(total_arr),
        "throughput_docs_per_sec": round(1000.0 / float(np.mean(total_arr)), 2),
        "gpu_memory_mb": round(gpu_mem, 1),
        "breakdown": {
            "scorer_forward_ms": stat_dict(scorer_arr),
            "feature_compute_ms": stat_dict(cpu_arr),
            "classifier_ms": stat_dict(lgbm_arr),
        },
    }


# ---------------------------------------------------------------------------
# Binoculars (observer PPL / performer PPL)
# ---------------------------------------------------------------------------

def compute_logppl_single(model, tokenizer, text):
    inputs = tokenizer(
        [text], return_tensors="pt", padding=False, truncation=True, max_length=MAX_LENGTH
    ).to(model.device)

    start_ev = torch.cuda.Event(enable_timing=True)
    end_ev = torch.cuda.Event(enable_timing=True)
    torch.cuda.synchronize()
    start_ev.record()

    with torch.no_grad():
        logits = model(**inputs).logits

    shift_logits = logits[:, :-1, :].contiguous()
    shift_labels = inputs["input_ids"][:, 1:].contiguous()
    mask = inputs["attention_mask"][:, 1:].contiguous()

    loss_fn = torch.nn.CrossEntropyLoss(reduction="none")
    token_losses = loss_fn(
        shift_logits.view(-1, shift_logits.size(-1)),
        shift_labels.view(-1),
    ).view(shift_labels.size())
    token_losses = token_losses * mask
    mean_loss = (token_losses.sum(dim=1) / mask.sum(dim=1).clamp(min=1)).item()

    end_ev.record()
    torch.cuda.synchronize()
    gpu_ms = start_ev.elapsed_time(end_ev)
    return mean_loss, gpu_ms


def benchmark_binoculars(docs):
    print("\n[Binoculars] Loading observer (Pythia-1.4b) ...")
    observer, obs_tok = load_causal_model(MODEL_PYTHIA)
    print("[Binoculars] Loading performer (OLMo-1B) ...")
    performer, perf_tok = load_causal_model(MODEL_OLMO)

    print(f"[Binoculars] Warmup {N_WARMUP} docs ...")
    for i in range(N_WARMUP):
        compute_logppl_single(observer, obs_tok, docs[i])
        compute_logppl_single(performer, perf_tok, docs[i])

    torch.cuda.empty_cache()
    torch.cuda.reset_peak_memory_stats(DEVICE)

    obs_times, perf_times = [], []
    print(f"[Binoculars] Benchmarking {N_DOCS} docs ...")
    for i in range(N_DOCS):
        if (i + 1) % 200 == 0:
            print(f"  [{i+1}/{N_DOCS}]")
        _, obs_ms = compute_logppl_single(observer, obs_tok, docs[i])
        _, perf_ms = compute_logppl_single(performer, perf_tok, docs[i])
        obs_times.append(obs_ms)
        perf_times.append(perf_ms)

    obs_arr = np.array(obs_times)
    perf_arr = np.array(perf_times)
    total_arr = obs_arr + perf_arr

    gpu_mem = torch.cuda.max_memory_allocated(DEVICE) / 1024**2

    result = {
        "total_ms_per_doc": stat_dict(total_arr),
        "throughput_docs_per_sec": round(1000.0 / float(np.mean(total_arr)), 2),
        "gpu_memory_mb": round(gpu_mem, 1),
        "breakdown": {
            "observer_forward_ms": stat_dict(obs_arr),
            "performer_forward_ms": stat_dict(perf_arr),
        },
        "models": {
            "observer": "EleutherAI/pythia-1.4b",
            "performer": "allenai/OLMo-1B-hf",
        },
    }

    free_model(observer)
    free_model(performer)
    del obs_tok, perf_tok
    gc.collect()
    torch.cuda.empty_cache()

    return result


# ---------------------------------------------------------------------------
# DivEye (single-model log-PPL)
# ---------------------------------------------------------------------------

def benchmark_diveye(docs, model, tokenizer):
    print(f"\n[DivEye] Warmup {N_WARMUP} docs ...")
    for i in range(N_WARMUP):
        compute_logppl_single(model, tokenizer, docs[i])
    torch.cuda.empty_cache()
    torch.cuda.reset_peak_memory_stats(DEVICE)

    times = []
    print(f"[DivEye] Benchmarking {N_DOCS} docs ...")
    for i in range(N_DOCS):
        if (i + 1) % 200 == 0:
            print(f"  [{i+1}/{N_DOCS}]")
        _, ms = compute_logppl_single(model, tokenizer, docs[i])
        times.append(ms)

    arr = np.array(times)
    gpu_mem = torch.cuda.max_memory_allocated(DEVICE) / 1024**2

    return {
        "total_ms_per_doc": stat_dict(arr),
        "throughput_docs_per_sec": round(1000.0 / float(np.mean(arr)), 2),
        "gpu_memory_mb": round(gpu_mem, 1),
        "model": "Qwen2.5-1.5B-Instruct",
    }


# ---------------------------------------------------------------------------
# Neural Probe (frozen embeddings + MLP)
# ---------------------------------------------------------------------------

class DepthMLP(nn.Module):
    def __init__(self, input_dim=1536, num_classes=6):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, 512),
            nn.ReLU(),
            nn.Dropout(0.1),
            nn.Linear(512, 256),
            nn.ReLU(),
            nn.Dropout(0.1),
            nn.Linear(256, num_classes),
        )

    def forward(self, x):
        return self.net(x)


def embed_single(model, tokenizer, text):
    inputs = tokenizer(
        [text], return_tensors="pt", padding=False, truncation=True, max_length=MAX_LENGTH
    ).to(model.device)

    start_ev = torch.cuda.Event(enable_timing=True)
    end_ev = torch.cuda.Event(enable_timing=True)
    torch.cuda.synchronize()
    start_ev.record()

    with torch.no_grad():
        out = model(**inputs, output_hidden_states=True)
        hidden = out.hidden_states[-1]
        mask = inputs["attention_mask"].unsqueeze(-1).float()
        pooled = (hidden * mask).sum(dim=1) / mask.sum(dim=1).clamp(min=1)

    end_ev.record()
    torch.cuda.synchronize()
    gpu_ms = start_ev.elapsed_time(end_ev)
    return pooled.cpu().float(), gpu_ms


def benchmark_neural_probe(docs, model, tokenizer):
    mlp = DepthMLP(input_dim=1536, num_classes=6).to(DEVICE).half()
    mlp.eval()

    print(f"\n[Neural Probe] Warmup {N_WARMUP} docs ...")
    for i in range(N_WARMUP):
        emb, _ = embed_single(model, tokenizer, docs[i])
        with torch.no_grad():
            mlp(emb.half().to(DEVICE))
    torch.cuda.empty_cache()
    torch.cuda.reset_peak_memory_stats(DEVICE)

    embed_times, mlp_times = [], []
    print(f"[Neural Probe] Benchmarking {N_DOCS} docs ...")
    for i in range(N_DOCS):
        if (i + 1) % 200 == 0:
            print(f"  [{i+1}/{N_DOCS}]")
        emb, emb_ms = embed_single(model, tokenizer, docs[i])
        embed_times.append(emb_ms)

        start = time.perf_counter()
        with torch.no_grad():
            mlp(emb.half().to(DEVICE))
        torch.cuda.synchronize()
        mlp_times.append((time.perf_counter() - start) * 1000)

    embed_arr = np.array(embed_times)
    mlp_arr = np.array(mlp_times)
    total_arr = embed_arr + mlp_arr
    gpu_mem = torch.cuda.max_memory_allocated(DEVICE) / 1024**2

    return {
        "total_ms_per_doc": stat_dict(total_arr),
        "throughput_docs_per_sec": round(1000.0 / float(np.mean(total_arr)), 2),
        "gpu_memory_mb": round(gpu_mem, 1),
        "breakdown": {
            "embedding_extraction_ms": stat_dict(embed_arr),
            "mlp_inference_ms": stat_dict(mlp_arr),
        },
        "model": "Qwen2.5-1.5B-Instruct (frozen) + MLP(1536->512->256->6)",
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print("=" * 60)
    print("Runtime Benchmark: OBD vs Baselines")
    print("=" * 60)

    # Hardware info
    gpu_name = torch.cuda.get_device_name(0)
    cuda_version = torch.version.cuda
    driver = ""
    try:
        import subprocess
        r = subprocess.run(
            ["nvidia-smi", "--query-gpu=driver_version", "--format=csv,noheader"],
            capture_output=True, text=True,
        )
        driver = r.stdout.strip()
    except Exception:
        pass

    print(f"GPU: {gpu_name}")
    print(f"CUDA: {cuda_version}, Driver: {driver}")

    # Load documents
    print(f"\nLoading {N_DOCS} documents from {DATA_PATH} ...")
    docs = []
    with open(DATA_PATH) as f:
        for i, line in enumerate(f):
            if i >= N_DOCS:
                break
            docs.append(json.loads(line)["text"])
    print(f"  Loaded {len(docs)} documents")

    avg_len_tokens = int(np.mean([len(d.split()) for d in docs]))
    print(f"  Avg doc length: ~{avg_len_tokens} words")

    all_tokens_word = [text.split() for text in docs]

    # -------------------------------------------------------------------
    # 1) Binoculars (run first, then free models)
    # -------------------------------------------------------------------
    bino_result = benchmark_binoculars(docs)
    print(f"[Binoculars] Done: {bino_result['total_ms_per_doc']['mean']:.1f} ms/doc, "
          f"{bino_result['throughput_docs_per_sec']:.1f} docs/s")

    # -------------------------------------------------------------------
    # 2) Load Qwen for OBD + DivEye + Neural Probe
    # -------------------------------------------------------------------
    print("\nLoading Qwen2.5-1.5B-Instruct ...")
    qwen_model, qwen_tok = load_causal_model(MODEL_QWEN)
    print(f"  Model loaded on {qwen_model.device}")

    # Train LightGBM
    print(f"\nTraining LightGBM from {FEATURES_CSV} ...")
    clf = train_lgbm_model(FEATURES_CSV)

    # 3) OBD Pipeline
    torch.cuda.reset_peak_memory_stats(DEVICE)
    obd_result = benchmark_obd(docs, all_tokens_word, qwen_model, qwen_tok, clf)
    print(f"[OBD] Done: {obd_result['total_ms_per_doc']['mean']:.1f} ms/doc, "
          f"{obd_result['throughput_docs_per_sec']:.1f} docs/s")

    # 4) DivEye (reuses Qwen model)
    diveye_result = benchmark_diveye(docs, qwen_model, qwen_tok)
    print(f"[DivEye] Done: {diveye_result['total_ms_per_doc']['mean']:.1f} ms/doc, "
          f"{diveye_result['throughput_docs_per_sec']:.1f} docs/s")

    # 5) Neural Probe (reuses Qwen model)
    probe_result = benchmark_neural_probe(docs, qwen_model, qwen_tok)
    print(f"[Neural Probe] Done: {probe_result['total_ms_per_doc']['mean']:.1f} ms/doc, "
          f"{probe_result['throughput_docs_per_sec']:.1f} docs/s")

    free_model(qwen_model)

    # -------------------------------------------------------------------
    # Assemble output
    # -------------------------------------------------------------------
    results = {
        "hardware": {
            "gpu": gpu_name,
            "cuda": cuda_version,
            "driver": driver,
        },
        "methods": {
            "obd_pipeline": obd_result,
            "binoculars": bino_result,
            "diveye": diveye_result,
            "neural_probe": probe_result,
        },
        "test_config": {
            "n_docs": N_DOCS,
            "avg_doc_length_words": avg_len_tokens,
            "max_seq_len_tokens": MAX_LENGTH,
            "warmup_iters": N_WARMUP,
            "measure_iters": N_DOCS,
        },
    }

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    json_path = OUT_DIR / "benchmark_results.json"
    with open(json_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved: {json_path}")

    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY (ms/doc, mean +/- std)")
    print("=" * 60)
    for name, res in results["methods"].items():
        t = res["total_ms_per_doc"]
        tp = res["throughput_docs_per_sec"]
        mem = res["gpu_memory_mb"]
        print(f"  {name:15s}: {t['mean']:7.1f} +/- {t['std']:5.1f}  |  {tp:6.1f} docs/s  |  {mem:.0f} MB GPU")
    print("=" * 60)


if __name__ == "__main__":
    main()
