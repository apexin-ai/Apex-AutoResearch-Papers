# analyze w27 batch 3exp

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_w27_batch_3exp_20260527T205516_result.json`
- **Structured JSON:** [`506d8d2845275deb02b9.json`](../../sessions/50/506d8d2845275deb02b9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新完毕。

## 结果汇总

### 实验 1: π0.5 Random k=0.5 Long

| Task | SR |
|------|-----|
| T0 | 70% |
| T1 | 34% |
| T2 | 82% |
| T3 | 78% |
| T4 | 62% |
| T5 | 32% |
| T6 | 44% |
| T7 | 54% |
| T8 | 8% |
| T9 | 50% |
| **Overall** | **51.4%** |

- seed42 = 49.8%, seed43 = 51.4%
- **mean = 50.6% ± 0.8%**

### 实验 2: π0.5 L2norm k=0.7 Long

| Task | SR |
|------|-----|
| T0 | 78% |
| T1 | 84% |
| T2 | 78% |
| T3 | 58% |
| T4 | 66% |
| T5 | 82% |
| T6 | 52% |
| T7 | 62% |
| T8 | 4% |
| T9 | 92% |
| **Overall** | **65.6%** |

- seed42 = 63.2%, seed43 = 65.6%
- **mean = 64.4% ± 1.2%**

两个实验 seed 间方差都很小（<1.5%），结果稳定。无错误或警告，500 episodes 全部完成，EXIT_CODE=0。

---
