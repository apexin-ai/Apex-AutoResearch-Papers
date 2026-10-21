# ssh check qwen cwm progress

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-qwen-cwm-progress_20260520T030652_result.json`
- **Structured JSON:** [`e01a394d9e957025bc60.json`](../../sessions/e0/e01a394d9e957025bc60.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 训练进度报告

### 实验 1: qwen3-8b-cwm-repo-s123-train-v4

| 项目 | 状态 |
|------|------|
| 进程 | **存活** (PID 886273, 已运行 1h37m) |
| 进度 | **260 / 6633 steps (3.9%)** |
| 速度 | ~12.1 s/step |
| tqdm ETA | ~21h12m |
| 预计完成 | ~May 21 00:40 UTC |
| Checkpoints | `checkpoint-100`, `checkpoint-200`, `checkpoint-300` |
| 错误/警告 | 无 |

Step 200 处触发了一轮 eval（9335 样本，耗时 ~19min），已完成。

> 注意：checkpoint-300 存在但当前 step 仅 260——可能来自之前的训练运行。

### 实验 2: qwen3-8b-cwm-repo-s456-train-v3

| 项目 | 状态 |
|------|------|
| 进程 | **存活** (PID 886347, 已运行 1h37m) |
| 进度 | **266 / 6633 steps (4.0%)** |
| 速度 | ~12.1 s/step |
| tqdm ETA | ~21h26m |
| 预计完成 | ~May 21 01:00 UTC |
| Checkpoints | `checkpoint-100`, `checkpoint-200` |
| 错误/警告 | 无 |

同样在 step 200 处完成了 eval（9335 样本，~19min）。

### 总结

两个实验均正常运行，进度接近（~4%），速度稳定在 ~12s/step。预计 **May 21 凌晨 00:40–01:00 UTC** 完成，与原始预估一致。日志无异常。

---
