# benchmark f11 slv timing v2

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_benchmark_f11_slv_timing_v2_20260521T030340_result.json`
- **Structured JSON:** [`cb94075a91edbc70cc9d.json`](../../sessions/cb/cb94075a91edbc70cc9d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

现在我有了所有需要的数据。让我汇总。

关键数据来源：

**源 1: `ews_v2_all.log`** — GPU 上的 spectral 诊断耗时（EXP_001, cuda:0, 1K 样本）

| 步骤 | 耗时 |
|------|------|
| Embeddings collected (1K samples → 7258 tokens) | 0.2–0.4s |
| RankMe (包含 SVD) | 0.3s |
| Model load | 0.5–1.2s |

**源 2: `logdet_gen012.json`** — CPU 上 `compute_effective_rank` (forward pass + SVD)

| Generation | 耗时 |
|-----------|------|
| Gen 0 | 424.1s |
| Gen 1 | 374.1s |
| Gen 2 | 360.5s |

**源 3: `hellaswag_gen0` lm_eval 结果** — HellaSwag 0-shot on GPU

- `total_evaluation_time_seconds`: **4230.1s** (70.5 min)
- 10,042 samples, batch_size=64, cuda:1
- RTX PRO 6000 Blackwell Server Edition

**源 4: `src/rankme.py`** — `compute_effective_rank` 实际做的事：
1. GPU forward pass (batch_size=32, 1K samples) → (1000, 1024) mean-pooled embeddings
2. `np.linalg.svd()` on CPU → singular values
3. log_det = sum(log(sv))

---

```
SLV computation breakdown (GPU: RTX PRO 6000 Blackwell 98GB):
  Forward pass (1K samples, bs=32):  ~0.3s    [from ews_v2_all.log: Embeddings collected 0.2–0.4s]
  SVD on (1000×1024) matrix (CPU):   ~0.01s   [NumPy SVD, trivially fast at this size]
  Total SLV per checkpoint:          ~0.3–0.5s

HellaSwag 0-shot evaluation (same GPU):
  lm_eval end-to-end:               70.5 min (4230s)
  Samples: 10,042 × 4 choices, batch_size=64
  Note: includes dataset loading, tokenization, auto-batch-size detection overhead

Speedup (end-to-end): SLV is ~8,500–14,000× faster than HellaSwag

Conservative estimate (pure inference only):
  HellaSwag pure inference (~628 batches × ~30ms):  ~20–60s
  Speedup (inference-only): SLV is ~40–200× faster

Source: ews_v2_all.log (SLV GPU), logdet_gen012.json (SLV CPU),
        hellaswag_gen0/results_2026-05-16*.json (HellaSwag)
Device: NVIDIA RTX PRO 6000 Blackwell Server Edition (×2)
Model: Pythia-410M-deduped (405M params)
```

**关于 lm_eval 的 4230s**：这个数字包含了大量非推理开销（数据集下载/处理、tokenization、auto batch size 探测）。lm_eval 对 10K 样本的纯 GPU 推理时间估计在 20–60s 左右。论文中引用 4230s 不公平；引用 conservative 估计更可信。

**建议**：如果需要论文可引用的精确数字，运行已有的 `scripts/benchmark_slv_timing.py`（通过 `scripts/run_benchmark.sh`），它会在同一 GPU 上公平对比 SLV 和 HellaSwag，输出精确的 forward pass / SVD / HellaSwag 分解耗时。脚本已写好，只需执行。要现在跑吗？

---
