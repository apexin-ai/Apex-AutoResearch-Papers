# ops gpu5 conflict fix

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu5-conflict-fix_20260513T234235_result.json`
- **Structured JSON:** [`1d7bf46d911f131943a8.json`](../../sessions/1d/1d7bf46d911f131943a8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇报

### GPU 5 冲突已解决
- **PID 234755（3B eval）**：已 kill，GPU 5 显存从 6791 MiB 降至 **0 MiB**，完全释放
- **PID 235331（d005 SFT）**：**已崩溃**（非预期）。日志显示在 step 8/3177 时因 **CUDA OOM** 挂掉——正是因为 eval 进程 234755 占了 6.62 GiB 显存，导致 SFT 训练分配 3.45 GiB 时内存不足

### 两个 SFT 训练状态

| 实验 | 状态 | 进度 | 说明 |
|------|------|------|------|
| **d005 SFT** (GPU 5) | **崩溃** | 8/3177 (0%) | OOM，需要重启 |
| **d100 SFT** (GPU 0) | **运行中** | 164/4159 (4%) | ~1.07 it/s，有 bitsandbytes 警告但不影响训练 |

**d005 SFT 需要重新启动。** GPU 5 现在完全空闲，可以直接重跑。是否需要我重启 d005？

---
