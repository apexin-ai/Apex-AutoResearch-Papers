# infra check eval status

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_check-eval-status_20260515T210406_result.json`
- **Structured JSON:** [`4cc3cac941f20292291c.json`](../../sessions/4c/4cc3cac941f20292291c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

日志很大（大量进度条输出），grep 超时了。从 tail 输出已经拿到关键信息，汇总如下：

## Baseline Eval 状态汇报

### GPU 使用
- **GPU 0** (RTX PRO 6000 Black, 96GB): PID 109501 (baseline_plus), 2220 MiB 显存, 0% 利用率
- **GPU 1** (RTX PRO 6000 Black, 96GB): PID 109428 (baseline_std), 2757 MiB 显存, 0% 利用率
- GPU 利用率 0% 是正常的——rollout 阶段主要在 CPU 端跑仿真环境

### mvp1_baseline_std (PID 109428, GPU 1)
- **状态**: 运行中
- **日志**: `/root/acib/outputs/baseline_std_v3/main.log`
- **模型**: `lerobot/smolvla_libero`
- **Suite**: `libero_spatial` (10 个 task, 每 task 50 episodes)
- **当前进度**: 45/50 batches (90%), running_success_rate = **68.9%**
- **预计剩余**: ~1.5 分钟完成当前 task（15s/batch × 5 remaining）

### mvp1_baseline_plus (PID 109501, GPU 0)
- **状态**: 运行中
- **日志**: `/root/acib/outputs/baseline_plus_v2/main.log`
- **模型**: `lerobot/smolvla_libero_plus`
- **Suite**: `libero_spatial` (10 个 task, 每 task 50 episodes)
- **当前进度**: 22/50 batches (44%), running_success_rate = **81.8%**
- **预计剩余**: ~6 分钟完成当前 task（13s/batch × 28 remaining）

### 备注
- 两个进程都只配了 `libero_spatial` 这一个 suite，各 10 个 task
- 从 tail 只能看到当前 task 的进度条，无法确认已完成了几个 task（日志太大 grep 超时）。但 baseline_std 的 batch 进度（45/50）和 baseline_plus 的（22/50）分别是当前 task 内的 episode 进度
- baseline_plus (81.8%) 表现优于 baseline_std (68.9%)，符合预期

---
