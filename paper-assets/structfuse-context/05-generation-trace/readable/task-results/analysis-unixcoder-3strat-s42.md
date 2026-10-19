# analysis unixcoder 3strat s42

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_unixcoder-3strat-s42_20260516T092457_result.json`
- **Structured JSON:** [`4433e5f5255ec39e8b3a.json`](../../sessions/44/4433e5f5255ec39e8b3a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果汇总：

| 策略 | best_val_loss (step) | best_R@1 (step) | best_R@5 | early_stop |
|------|---------------------|-----------------|----------|------------|
| random_s42 | 0.4513 (400) | **0.5534** (1000) | **0.9772** | step 1000 |
| embedding_distance_s42 | **0.4466** (600) | 0.5497 (600) | 0.9772 | step 1200 |
| dataflow_aware_s42 | 0.4628 (400) | 0.5510 (1000) | 0.9755 | step 1000 |

关键发现：3 个策略性能差异极小（R@1 跨度 < 0.4%）。random 在 R@1 上反而最好，embedding_distance 在 val_loss 上最好但 R@1 最低。dataflow_aware 居中。负采样策略对 UniXcoder 影响不显著。

结果已保存到 `artifacts/unixcoder-3strat-s42/analysis.json`。

---
