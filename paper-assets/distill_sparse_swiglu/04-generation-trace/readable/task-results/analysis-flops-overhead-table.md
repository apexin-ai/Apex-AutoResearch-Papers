# analysis flops overhead table

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_flops-overhead-table_20260519T121505_result.json`
- **Structured JSON:** [`3c35d1e4b87833685473.json`](../../sessions/3c/3c35d1e4b87833685473.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已写入并注册 `art_20260519_48cc33`。

**原始任务中的关键修正：**

| 原始值 | 修正值 | 原因 |
|--------|--------|------|
| FFN FLOPs ~11.3**T** | 11.27**B** | 单 token 过 32 层 FFN 的 FLOPs 是 billion 级，非 trillion |
| 总 FLOPs ~16**T** | ~16.1**B** | 2N 近似：2 × 8.03B = 16.1B |
| Predictor 占比 ~0.001% | **~0.94%** | 151M / 16.1B ≈ 0.94%，原始计算分母单位错了 1000 倍 |

其余数值（FFN 参数 5.64B/70.2%、Predictor 151M FLOPs、30% sparsity 省 ~20% 总 FLOPs、latency overhead 2.5%/6-8%、net speedup 1.13-1.17x）均验证正确。

训练成本：单 seed 约 0.86 GPU-hours（1000 steps, 1× RTX PRO 6000）。

---
