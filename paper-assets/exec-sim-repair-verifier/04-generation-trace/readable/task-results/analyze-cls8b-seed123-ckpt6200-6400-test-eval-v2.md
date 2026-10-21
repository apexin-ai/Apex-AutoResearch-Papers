# analyze cls8b seed123 ckpt6200 6400 test eval v2

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_cls8b-seed123-ckpt6200-6400-test-eval-v2_20260515T103210_result.json`
- **Structured JSON:** [`af4e7d04adbbf3798fd3.json`](../../sessions/af/af4e7d04adbbf3798fd3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。结果汇总：

| 指标 | ckpt-3000 (val-best) | ckpt-6200 | ckpt-6400 |
|------|---------------------|-----------|-----------|
| **accuracy** | 85.60% | 84.70% (-0.90) | 85.08% (-0.52) |
| **f1_fail** | — | 63.71 | 65.32 |
| **precision_fail** | — | 88.84 | 87.92 |
| **recall_fail** | — | 49.66 | 51.97 |
| **f1_macro** | — | 77.01 | 77.91 |

两个后段 checkpoint 的 test accuracy 都低于 val-best ckpt-3000 的 85.60%，符合过拟合后性能下降的预期。ckpt-6400 略优于 ckpt-6200（accuracy 85.08 vs 84.70, f1_fail 65.32 vs 63.71），但都不如早停点 ckpt-3000。

---
