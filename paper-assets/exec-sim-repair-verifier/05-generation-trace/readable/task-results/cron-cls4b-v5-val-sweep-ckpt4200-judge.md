# cron cls4b v5 val sweep ckpt4200 judge

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_cron_cls4b-v5-val-sweep-ckpt4200-judge_20260515T043941_result.json`
- **Structured JSON:** [`a9033956fb36d197257f.json`](../../sessions/a9/a9033956fb36d197257f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结论：success**

**cls4b-v5-val-sweep-ckpt4200 指标：**

| 指标 | 值 |
|------|-----|
| Accuracy | **89.06%** |
| F1 macro | 83.07% |
| fail P/R/F1 | 90.3% / 61.3% / 73.0% |
| pass P/R/F1 | 88.8% / 97.9% / 93.1% |

**4B v5 val sweep 汇总：**

| Checkpoint | Accuracy |
|------------|----------|
| ckpt-600 | 82.82% |
| ckpt-4000 | 89.84% |
| **ckpt-4200** | **89.06%** |
| ckpt-4400 | 89.96% |

ckpt-4200 (89.06%) 略低于 ckpt-4000 (89.84%) 和 ckpt-4400 (89.96%)，处于该区间的局部低点。

---
