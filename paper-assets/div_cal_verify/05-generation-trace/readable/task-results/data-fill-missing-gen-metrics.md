# data fill missing gen metrics

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_fill_missing_gen_metrics_20260514T072807_result.json`
- **Structured JSON:** [`5b68b8ad38be6492f401.json`](../../sessions/5b/5b68b8ad38be6492f401.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 registry 已更新完成：

1. **medium_uncurated_seed123** — gen0-gen7 全部 5 项指标已补全（之前只有 gen7 汇总）
2. **medium_rgds_seed123** — gen0-gen6 的 ratio 已补全（之前只有 gen7 的 ratio=0.8728）

RGDS ratio 在 0.85-0.96 之间波动，与 seed42 的趋势一致（逐代下降但幅度不大）。

---
