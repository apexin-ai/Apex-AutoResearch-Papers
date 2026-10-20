# collect home 4b test

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_collect_home-4b-test_20260515T072448_result.json`
- **Structured JSON:** [`a5d8a927c48f3fb35ba4.json`](../../sessions/a5/a5d8a927c48f3fb35ba4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新完毕。

## 4B v5 ckpt-4600 Test Eval 结果

| 指标 | Val | Test | 差值 |
|------|-----|------|------|
| **Accuracy** | 90.07% | 83.63% | **-6.44pp** |
| **F1 macro** | — | 75.63% | — |
| **F1 fail** | — | 61.67% | — |
| **F1 pass** | — | 89.59% | — |
| Precision fail | — | 84.03% | — |
| Recall fail | — | 48.72% | — |
| Precision pass | — | 83.55% | — |
| Recall pass | — | 96.57% | — |
| Majority baseline | 72.96% | 72.96% | — |
| Gap vs majority | — | +10.67pp | — |
| Unparseable | — | 0 | — |
| Total samples | — | 9,784 | — |

**Val→Test 下降 6.44pp**（90.07% → 83.63%）。Recall fail 仅 48.72%，模型在 test 上漏掉了超过一半的 fail 样本，说明 fail 检测泛化不足。

**Home cuda:0 已释放**（0 MiB, 0% utilization）。

---
