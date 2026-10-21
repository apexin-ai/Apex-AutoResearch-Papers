# infra phase1 progress v2

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_phase1-progress-v2_20260513T084557_result.json`
- **Structured JSON:** [`73b90a910b63cf21233c.json`](../../sessions/73/73b90a910b63cf21233c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Phase 1 实验进度

### GPU0（HF 后端，PID 20296）— boil/melt/change-state
- **进程存活**: 是，已运行 2h21m
- **当前位置**: Task 1/3 `boil`，正在跑 Episode 16/20（episode 0-15 的结果已写入 episodes.jsonl = 16 行）
- **GPU 利用率**: 79%，显存 15825/32607 MiB

### GPU1（vLLM 后端，PID 324895）— mix-paint/grow-plant
- **进程存活**: 是，已运行 35m
- **当前位置**: Task 1/2 `chemistry-mix-paint-secondary-color`，正在跑 Episode 3/20（episodes.jsonl = 3 行）
- **GPU 利用率**: 0%（vLLM 在做 CPU 端推理后处理），显存 28013/32607 MiB

### 产出文件
| 目录 | episodes |
|------|----------|
| boil | 16 |
| chemistry-mix-paint-secondary-color | 3 |
| melt | 未开始 |
| change-the-state-of-matter-of | 未开始 |
| grow-plant | 未开始 |

GPU0 的 boil task 接近完成（16/20），之后还有 melt 和 change-state 两个 task。GPU1 的 mix-paint 才刚起步（3/20）。

---
