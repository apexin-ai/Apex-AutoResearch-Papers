# analysis 010b nve calculation

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_010b-nve-calculation_20260517T203521_result.json`
- **Structured JSON:** [`61f090d66283cbfdcce1.json`](../../sessions/61/61f090d66283cbfdcce1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

| Experiment | value_mean | eval_return | V/E ratio |
|---|---|---|---|
| 023a (baseline s0) | 239.16 | 321.97 | 0.7428 |
| 023b (baseline s1) | 243.83 | 436.02 | 0.5592 |
| 010b (CIVO trigger) | 35.51 | 51.72 | 0.6867 |

- **Baseline avg V/E** = 0.6510
- **NVE_010b** = **1.0548**

010b 的 NVE 略大于 1（约 +5.5%），说明 CIVO trigger 实验相对 baseline 存在轻微的 value overestimation。注意 010b 的绝对性能远低于 baseline（eval_return 51.7 vs 321/436），说明 collapse 确实发生了，但 V/E 比例并未严重失调。

结果已写入 `artifacts/analysis/exp_010b_nve_calculation.json`。

---
