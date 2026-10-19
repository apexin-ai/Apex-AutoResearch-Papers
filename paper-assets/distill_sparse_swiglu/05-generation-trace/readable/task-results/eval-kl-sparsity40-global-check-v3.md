# eval kl sparsity40 global check v3

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_kl_sparsity40_global_check_v3_20260520T092245_result.json`
- **Structured JSON:** [`3042e157a108d93a0356.json`](../../sessions/30/3042e157a108d93a0356.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态总结

**PID 195152**: 已不存在（进程结束或服务器重启后消失）

**PID 197972**: **仍在运行**（已 ~1h4m），无错误

### 已有结果

**WikiText-2 PPL = 12.8894**（已完成）

### Per-layer sparsity（global_topk 分配）

| Layer | Sparsity | Layer | Sparsity |
|-------|----------|-------|----------|
| 0 | 0.410 | 16 | 0.410 |
| 1 | 0.434 | 17 | 0.430 |
| 2 | 0.496 | 18 | 0.418 |
| 3 | 0.457 | 19 | 0.473 |
| 4 | 0.430 | 20 | 0.488 |
| 5 | 0.430 | 21 | 0.504 |
| 6 | 0.453 | 22 | 0.545 |
| 7 | 0.453 | 23 | 0.549 |
| 8 | 0.449 | 24 | 0.613 |
| 9 | 0.457 | 25 | 0.670 |
| 10 | 0.461 | 26 | 0.705 |
| 11 | 0.461 | 27 | 0.707 |
| 12 | 0.465 | 28 | 0.713 |
| 13 | 0.461 | 29 | 0.674 |
| 14 | 0.449 | 30 | 0.484 |
| 15 | 0.418 | 31 | 0.426 |
| **Model-level** | **0.500** | | |

### Downstream tasks

进度：81%（32617/40168 loglikelihood requests），速率 ~24 it/s，剩余 ~7500 requests ≈ **~5 分钟后完成**。

正在跑 arc_challenge, winogrande, mmlu, gsm8k, hellaswag, piqa 的联合 eval。结果会在全部完成后一次性输出到日志和 results 目录。

### 注意

Model-level sparsity 是 **0.500**（50%），不是 40%。global_topk 分配下后层（L24-L29）sparsity 高达 0.67-0.71，前层则 ~0.41-0.43。这说明 predictor 在 global 分配下自动将更多 budget 给了前层。

需要等 ~5 分钟后再查一次获取完整的 6 项下游指标。要我稍后再查吗？

---
