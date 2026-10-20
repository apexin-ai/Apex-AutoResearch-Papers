# collect home 4b ckpt4400 final

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_collect_home-4b-ckpt4400-final_20260515T075820_result.json`
- **Structured JSON:** [`874208501df0782b875c.json`](../../sessions/87/874208501df0782b875c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新完毕。结果汇总：

## 4B ckpt-4400 Test 结果

| 指标 | 值 |
|------|-----|
| **Accuracy** | **83.24%** |
| F1 macro | 74.44% |
| F1 fail | 59.45% (P=86.0%, R=45.4%) |
| F1 pass | 89.44% (P=82.8%, R=97.3%) |
| Majority baseline | 72.96% |
| Gap vs majority | +10.28pp |
| Unparseable | 0 |
| Total samples | 9,784 |

### 与 ckpt-4600 对比

| | ckpt-4400 | ckpt-4600 | 差异 |
|--|-----------|-----------|------|
| **Test acc** | 83.24% | 83.63% | -0.39pp |
| **Val acc** | 89.96% | 90.07% | -0.11pp |

ckpt-4400 略低于 ckpt-4600，差距很小（test -0.39pp, val -0.11pp），两者表现基本一致。

---
