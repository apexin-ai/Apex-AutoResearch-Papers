# ops read latency log

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_read-latency-log_20260516T144719_result.json`
- **Structured JSON:** [`1416d73d82d6d65ac495.json`](../../sessions/14/1416d73d82d6d65ac495.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进程已完成。完整日志：

```
[transformers] `torch_dtype` is deprecated! Use `dtype` instead!
Loading model from /root/autodl-tmp/models/llama-3.1-8b ...
Loading weights: 100%|██████████| 291/291 [00:04<00:00, 66.29it/s]

Config: batch=1, seq_len=2048, warmup=10, iters=100
Device: NVIDIA RTX PRO 6000 Blackwell Server Edition
dtype: float16, attn: flash_attention_2

--- Mode 1: Dense forward ---
  Mean: 119.11 ± 0.57 ms

--- Mode 2: KL predictor-only 30% ---
  Mean: 126.64 ± 0.70 ms

--- Mode 3: KL predictor-only 50% ---
  Mean: 126.78 ± 0.31 ms

--- Mode 4: Predictor+compensation 30% ---
  Mean: 129.94 ± 0.75 ms

--- Mode 5: Predictor+compensation 50% ---
  Mean: 129.71 ± 0.53 ms

--- Predictor overhead (all 32 layers, isolated) ---
  All-layer predictor forward: 3.17 ± 0.06 ms
  Per-layer average: 0.099 ms

--- Per-layer FFN breakdown (layer 0) ---
  Dense FFN (1 layer): 2.427 ± 0.037 ms
  Sparse FFN+predictor (1 layer): 2.686 ± 0.014 ms

================================================================================
| Method                    | Sparsity | tokens/s   | ms/token   | speedup vs dense   |
|---------------------------|----------|------------|------------|--------------------|
| Dense                     | 0%       | 17194.5    | 0.0582     | 1.000             x |
| KL predictor-only         | 30%      | 16171.8    | 0.0618     | 0.941             x |
| KL predictor-only         | 50%      | 16154.2    | 0.0619     | 0.939             x |
| Predictor+compensation    | 30%      | 15761.4    | 0.0634     | 0.917             x |
| Predictor+compensation    | 50%      | 15788.8    | 0.0633     | 0.918             x |
================================================================================

--- Raw data ---
Predictor overhead (32 layers): 3.17 ms (2.7% of dense forward)
Dense FFN per layer: 2.427 ms
Sparse FFN+pred per layer: 2.686 ms
Compensation overhead estimate: 3.30 ms
```

---
