# analysis tost multi margin

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_tost-multi-margin_20260515T122851_result.json`
- **Structured JSON:** [`04e6895752175155b466.json`](../../sessions/04/04e6895752175155b466.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

| Margin | 90% CI | p-value | Equivalent? |
|--------|--------|---------|-------------|
| ±1pp | [−0.275, +1.620] | 0.2854 | **NO** |
| ±2pp | [−0.275, +1.620] | 0.0104 | **YES** |
| ±3pp | [−0.275, +1.620] | 0.0000 | **YES** |

**关键数字：**
- 4 对 CLS-CWM 配对（2 CLS seeds × 2 CWM seeds），7560 obs，114 problem clusters，10K bootstrap resamples
- 池化均差 +0.661pp，95% CI [−0.479, +1.792]pp
- 最小等价 margin = **1.620pp**

**结论：**
- ±2pp TOST p=0.010，确认 C2 claim（与先前报告 p=0.007 一致量级）
- ±1pp 不能拒绝非等价（p=0.285），90% CI 上界 1.62pp 超出 1pp
- ±3pp 轻松等价
- 回复 W2：即使收紧至 ±1.62pp 仍可建立等价性，但 ±1pp 确实不够——差异的上界可达 1.6pp

---
