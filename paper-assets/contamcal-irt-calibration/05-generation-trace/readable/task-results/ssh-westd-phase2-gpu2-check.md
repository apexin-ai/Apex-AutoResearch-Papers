# ssh westd phase2 gpu2 check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_westd-phase2-gpu2-check_20260519T105902_result.json`
- **Structured JSON:** [`681d987eed2f00ba7677.json`](../../sessions/68/681d987eed2f00ba7677.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### 1. GPU 2 eval 进度：**1/6 完成，正在跑第 2 个**

| 任务 | 状态 |
|------|------|
| qwen7b_d000 | **完成** |
| qwen7b_d005 | **运行中** (PID 149714) |
| qwen7b_d025 | 未开始 |
| qwen7b_d050 | 未开始 |
| qwen7b_d100 | 未开始 |
| gemma2_d000 | 未开始 |

原 PID 147533 已退出，当前 GPU 2 进程是 PID 149714（qwen7b_d005 eval）。

### 2. GPU 2 已完成结果

| 模型 | MMLU | ARC |
|------|------|-----|
| qwen7b_d000 | 0.6611 | 0.8788 |

### 3. 所有已完成 eval（跨 GPU）

| 模型 | MMLU | ARC |
|------|------|-----|
| phi4_d000 | 0.7644 | 0.9206 |
| qwen7b_d000 | 0.6611 | 0.8788 |
| sanity_check_gemma2_d005_arc | N/A | 0.7782 |

### 4. 其他 3 个 GPU 进程状态

| GPU | PID | 任务 | 状态 |
|-----|-----|------|------|
| 0 | 150487 | phi4_d005 | **运行中** (刚启动 ~1min) |
| 1 | 147458 | qwen14b_d000 | **运行中** (原始 PID，MMLU 评测中) |
| 3 | 147609 | gemma2_d005 | **运行中** (原始 PID) |

4 个 GPU 全部在工作，无空闲。无失败任务。GPU 2 还有 4 个任务排队。

---
