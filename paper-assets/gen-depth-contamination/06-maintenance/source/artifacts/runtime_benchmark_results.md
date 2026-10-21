# OBD Pipeline Per-Document Runtime Benchmark

## Setup
- **Scorer model**: Qwen2.5-1.5B-Instruct
- **GPU**: NVIDIA RTX PRO 6000 Blackwell Server Edition (96GB)
- **Documents**: 1,000 (10 warmup, excluded from timing)
- **Max sequence length**: 512 tokens
- **LightGBM**: pairwise binary classifier (200 trees, max_depth=6, 15D features)

## Per-Document Latency (ms)

| Stage | Mean | Std | Median | P5 | P95 |
|-------|------|-----|--------|-----|-----|
| Scorer log-prob (GPU) | 20.6 | 1.9 | 21.7 | 17.6 | 22.1 |
| Feature extraction (CPU) | 23.4 | 6.1 | 25.4 | 13.0 | 30.6 |
| LightGBM inference (CPU) | 0.74 | 0.10 | 0.72 | 0.71 | 0.80 |
| **Total** | **44.7** | **7.7** | **47.7** | **31.3** | **53.3** |

## Throughput
- **22.4 documents/second** (single-document, no batching)

## Stage Breakdown
- Scorer log-prob (GPU): 46.1%
- CPU features (TTR, hapax, self-BLEU, tail stats): 52.3%
- LightGBM inference: 1.6%

## Raw JSON

```json
{
  "scorer_model": "Qwen2.5-1.5B-Instruct",
  "gpu_model": "NVIDIA RTX PRO 6000 Blackwell Server Edition",
  "n_documents": 1000,
  "n_warmup": 10,
  "max_seq_len": 512,
  "scorer_logprob_ms_per_doc": {
    "mean": 20.598,
    "std": 1.891,
    "median": 21.711,
    "p5": 17.564,
    "p95": 22.11
  },
  "feature_extraction_cpu_ms_per_doc": {
    "mean": 23.362,
    "std": 6.071,
    "median": 25.41,
    "p5": 12.965,
    "p95": 30.575
  },
  "lgbm_inference_cpu_ms_per_doc": {
    "mean": 0.736,
    "std": 0.1,
    "median": 0.718,
    "p5": 0.705,
    "p95": 0.797
  },
  "total_ms_per_doc": {
    "mean": 44.696,
    "std": 7.734,
    "median": 47.728,
    "p5": 31.264,
    "p95": 53.3
  },
  "throughput_docs_per_sec": 22.37,
  "stage_breakdown_pct": {
    "scorer_logprob": 46.1,
    "cpu_features": 52.3,
    "lgbm_inference": 1.6
  }
}
```

## Notes
- Scorer log-prob: single-document forward pass (batch_size=1) timed with CUDA events
- CPU features: TTR, hapax ratio, self-BLEU (100 random references), freq kurtosis, freq entropy, low-freq ratio
- All times exclude one-time model loading cost (~5s)
- Self-BLEU computation dominates the CPU feature time (100 BLEU comparisons per document)
- With batched inference (e.g., batch_size=8), scorer throughput would improve significantly
