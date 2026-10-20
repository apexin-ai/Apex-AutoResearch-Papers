# ops cuda2 cleanup a050 aggregate

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cuda2_cleanup_a050_aggregate_20260519T095405_result.json`
- **Structured JSON:** [`34a4b6bb5f5e8fff6163.json`](../../sessions/34/34a4b6bb5f5e8fff6163.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Artifact registration tool not available. Report written.

**Summary:**

**cuda:2 清理**: GPU 2 已经是 0 MiB，无孤儿进程。GPU 0/1 有活跃训练进程。

**all_metrics.json**: 三个 seed (s42/s43/s44) 的 `all_metrics.json` 均已存在，各含 11 generations (gen_0 to gen_10)，无需重新聚合。

**Drift 一致性**: alpha=0.50 在 3 seed 间高度一致:
- token_entropy: -16.2% (std 0.3%)
- distinct_1/2/3: -28.7% / -36.1% / -32.0%
- ECE: +697% (校准退化显著)
- perplexity: +16.8%

报告写入 `artifacts/a050_fp32_3seed_metrics_summary.md`。

---
