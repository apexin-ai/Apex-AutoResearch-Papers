# analysis perlayer kl k2 s42

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_perlayer_kl_k2_s42_20260523T055755_result.json`
- **Structured JSON:** [`a27c75b75974512be808.json`](../../sessions/a2/a27c75b75974512be808.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`perlayer_kl_k2_s42_train` 不存在，不需要处理重复条目。

---

## 总结

**K=2 训练 (perlayer_kl_k2_s42)** — 正常完成，1000 steps，EXIT_CODE=0。

| 指标 | K=2 | K=4 | K=8 | K=16 | K=32 (joint) |
|------|-----|-----|-----|------|-------------|
| final_avg_kl | 0.0358 | — | 0.0983 | 0.1582 | — |
| final_avg_sparsity | 0.268 | 0.282 | 0.281 | 0.286 | — |
| wall_time (s) | 3841 | — | 1894 | 1983 | — |
| WikiText-2 PPL | **未评估** | 8.8932 | 8.9704 | 8.6737 | 8.8157 |

**关键发现：**
- K=2 的 avg_kl (0.0358) 是所有 K 值中最低的，符合预期（每步只训练 2 层，梯度信号更集中）
- avg_sparsity 0.268 略低于目标 0.3，部分层的 lambda 没有收敛到足够高
- wall_time 3841s 约为 K=8 的 2 倍，因为 K=2 每步只覆盖 2/32 层，需要更多步数累积覆盖
- **PPL eval 尚未运行**——需要单独跑 benchmark_eval.py 才能获得 WikiText-2 PPL 和下游任务分数，完成 K-curve 数据点

---
