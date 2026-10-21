# investigate exp012 artifacts

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigate_exp012_artifacts_20260515T225057_result.json`
- **Structured JSON:** [`5ffbe45acd91eed24330.json`](../../sessions/5f/5ffbe45acd91eed24330.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结论：这是 N=5 的 dry-run 测试数据，不是全量结果。**

依据：

| 指标 | 值 |
|------|-----|
| 每个 (model, depth) 组合的样本数 | **5** |
| 模型数 | 4 (qwen-rewrite, pythia-1.4b, olmo-1b, qwen-cont) |
| depth 级别 | 6 (0-5) |
| 总样本量 | 4 × 6 × 5 = **120** |

AUC 值呈 0.04 步进（0.52, 0.56, 0.60, 0.64 …），这是典型的小 N 伪影（5 对中每改变 1 对结果变化 1/25 = 0.04）。threshold_accuracy 也只取 0.0667, 0.1, 0.1333 等值（1/15, 1.5/15, 2/15），印证了 30 个样本的分辨率。

需要用 N=500 重跑才能得到有效结果。

---
