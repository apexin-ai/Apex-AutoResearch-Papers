# ops check ckpt3600 test result

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-ckpt3600-test-result_20260515T233243_result.json`
- **Structured JSON:** [`e19e0786ce8840a22fee.json`](../../sessions/e1/e19e0786ce8840a22fee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

## ckpt-3600 Test Eval 结果 (s42 resume)

| 指标 | 值 |
|------|-----|
| **Accuracy** | **84.48%** |
| **F1 macro** | **78.17%** |
| F1 fail | 66.43% (P=80.1%, R=56.8%) |
| F1 pass | 89.91% (P=85.5%, R=94.8%) |
| Majority baseline | 72.96% |
| Gap vs majority | +11.53pp |
| 样本数 | 9784/9784 |
| Unparseable | 0 |

**对比原 val-best ckpt-1000**: test accuracy 83.52% → **84.48%** (+0.96pp)

ckpt-3600 在 val 上提升显著 (88.71% → 90.28%)，test 上也有近 1pp 提升，确认 resume 训练有效。

- Registry: `cls8b-s42-resume-ckpt3600-test` → DONE/success，metrics 已写入
- Cron: 本 session 无活跃 cron，无需删除

---
