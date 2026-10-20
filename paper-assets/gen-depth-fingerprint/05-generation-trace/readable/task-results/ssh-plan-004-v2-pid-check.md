# ssh plan 004 v2 pid check

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_plan-004-v2-pid-check_20260515T004804_result.json`
- **Structured JSON:** [`a062e9262fe357896b72.json`](../../sessions/a0/a062e9262fe357896b72.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总：

**Plan-004-v2 进程（全部活跃）：**

| GPU | Wrapper PID | Python PID | 当前任务 |
|-----|-------------|------------|----------|
| GPU2 | 142675 | 142680 | size_matched_seed42 (bs2×ga8) |
| GPU1 | 143757 | 143765 | size_matched_seed42 (bs4×ga4, via run_downstream.sh) |
| GPU3 | **145799** | 145805 | size_matched_seed123 (40%, 后续还有 4 个任务) |

Registry 已更新 `spec.pid = 145799`（GPU3 wrapper，最慢进程）。

**Plan-014：**
- PID 134817: ALIVE
- PID 134823: ALIVE（在 GPU0 上运行）

**注意：** 没有 "all" variant 在运行。`run_gpu3.sh` 只跑 `size_matched`（seed 123, 456）和 `binary_filtered`（seed 42, 123, 456）。

---
