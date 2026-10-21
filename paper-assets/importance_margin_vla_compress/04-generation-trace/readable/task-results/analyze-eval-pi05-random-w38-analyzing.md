# analyze eval pi05 random w38 analyzing

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_pi05_random_w38_analyzing_20260528T073952_result.json`
- **Structured JSON:** [`183f0654a604eb1ae313.json`](../../sessions/18/183f0654a604eb1ae313.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均已完成并更新 registry 为 DONE。

### 结果汇总

| 实验 | Overall SR | 历史均值 | 判定 |
|------|-----------|---------|------|
| **Random k=0.95 s45** | **62.4%** | 60.8% (s42=60.6, s43=60.8, s44=61.0) | ✓ 合理，4-seed 均值更新为 61.2% |
| **Random k=0.7 s45** | **61.6%** | 64.5% (s42=66.0, s43=64.4, s44=63.2) | ✓ 略低但在方差内，4-seed 均值更新为 63.8% |

Per-task breakdown:

| Task | Random k=0.95 s45 | Random k=0.7 s45 |
|------|-------------------|-------------------|
| T0 | 74% | 84% |
| T1 | 92% | 62% |
| T2 | 66% | 68% |
| T3 | 80% | 80% |
| T4 | 50% | 74% |
| T5 | 84% | 38% |
| T6 | 4% | 62% |
| T7 | 70% | 74% |
| T8 | 18% | 4% |
| T9 | 86% | 70% |

配置确认：k=0.95 keep 243/256 ✓，k=0.7 keep 179/256 ✓，seed=45，EXIT_CODE=0。

---
