# analysis g q progress t60

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_g-q-progress-t60_20260520T122318_result.json`
- **Structured JSON:** [`0959f51ab745bbe80721.json`](../../sessions/09/0959f51ab745bbe80721.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Q 实验的日志没有 progress 行，进度只能从 results.json 中已有的 56 个 problem 和运行时间推算。

---

## 实验进度报告

### 1. G Decoupling (PID 307169)

| 项目 | 值 |
|------|-----|
| **进程状态** | alive, 运行 2h08m |
| **已完成** | **120 / 204** (58.8%) |
| **当前 accuracy** | 57.5% (69/120) |
| **avg_trunc** | 4.2%, matched 98% |
| **速度** | ~0.02 prob/s (~50s/问题) |
| **ETA** | 日志报 5250s ≈ **~1h27m** (约 21:50 UTC 完成) |

注：results.json 只写了 3 个问题（可能是 pilot 写入），实时进度以日志为准。

### 2. Q Premise Mutation (PID 314817)

| 项目 | 值 |
|------|-----|
| **进程状态** | alive, 运行 1h08m |
| **已完成** | **56 / 204** (27.5%) |
| **SC accuracy (original)** | 60.7% (34/56) |
| **SICA accuracy (original)** | 64.3% (36/56) |
| **速度** | ~0.82 prob/min (68s 运行 56 问题 → ~73s/问题) |
| **ETA** | 剩 148 问题 × 73s ≈ **~3h00m** (约 23:25 UTC 完成) |

**Mutation flip rates (56 问题):**

| Mutation | SC acc | SICA acc | SC flip rate | SICA flip rate |
|----------|--------|----------|-------------|---------------|
| original | 60.7% | 64.3% | — | — |
| synonym | 66.1% | 60.7% | 12.5% | 12.5% |
| reorder | 67.9% | 60.7% | 21.4% | 25.0% |
| inject | 57.1% | 57.1% | 7.1% | 12.5% |
| combined | 58.9% | 57.1% | 21.4% | 19.6% |

初步观察：reorder 和 combined 的 flip rate 最高 (~20-25%)，说明前提顺序扰动对 SC 和 SICA 都有明显影响。SICA 在 mutation 下并未显著优于 SC（甚至 original 上 SICA 略高但 mutation 后两者差距缩小），后续 204 题全量数据会更有统计意义。

---
