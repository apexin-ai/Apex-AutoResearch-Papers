# ssh verify occ loss fix

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_verify-occ-loss-fix_20260528T230208_result.json`
- **Structured JSON:** [`2156691de68f5767d5be.json`](../../sessions/21/2156691de68f5767d5be.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**两个实验都已崩溃**，原因相同：**wandb API key 未配置**。

### 崩溃详情

| 实验 | 服务器 | 崩溃时间 | 错误 |
|------|--------|----------|------|
| full_occ_bn_v2_s2_r3 | westd-34685 | 07:01:58 | `wandb.errors.UsageError: No API key configured` |
| random_occ_v2_s0_r2 | westd-10894 | 07:02:03 | 同上 |

两个进程都已退出（PID 不存在，/proc/cmdline 也不存在），没有产生任何训练 step，因此没有 occ_loss 输出。

### 根因

`finetune.py:876` 调用 `wandb.init()` 时失败，服务器上没有配置 `WANDB_API_KEY` 环境变量，也没有执行过 `wandb login`。

### 修复方案

重新启动时需要在启动命令前设置 wandb key，或者禁用 wandb：
1. **设置 key**：`export WANDB_API_KEY=[REDACTED] 后再启动
2. **禁用 wandb**：如果 finetune.py 支持 `--wandb_project ""` 或 `WANDB_MODE=disabled` 参数

需要哪种方式？

---
