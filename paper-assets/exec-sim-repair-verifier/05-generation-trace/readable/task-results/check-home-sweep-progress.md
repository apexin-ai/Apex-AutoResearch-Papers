# check home sweep progress

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_home-sweep-progress_20260514T025925_result.json`
- **Structured JSON:** [`c1b97aa2090a584b6db0.json`](../../sessions/c1/c1b97aa2090a584b6db0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Checkpoint Sweep 进度汇总

| Checkpoint | 状态 | Accuracy | F1_fail | F1_pass | F1_macro | Unparseable |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **400** | COMPLETED | 75.05% | 51.77 | 83.17 | 67.47 | 132 (1.35%) |
| **600** | COMPLETED | **80.73%** | 68.49 | 86.12 | **77.31** | 132 (1.35%) |
| **800** | RUNNING (4000/9784, ~41%) | running ~73.9% | — | — | — | — |
| **1000** | NOT STARTED | — | — | — | — | — |

### 关键发现

**checkpoint-600 accuracy = 80.73%**，比预期的 ~80.5% 略高，比 CLS v5 的 76.92% **高出 3.81pp**。F1_macro 77.31 也很强。

checkpoint-800 running accuracy 只有 73.9%，明显低于 ckpt-600 的 80.73%，看起来**过拟合了**。ckpt-800 最终 accuracy 大概率落在 73-74% 区间。

ckpt-800 约还需 ~16 分钟完成，ckpt-1000 约再 ~28 分钟，整体 sweep 预计还需 ~44 分钟。

**结论：checkpoint-600 是 sweet spot，seed123 的最佳 checkpoint。**

---
