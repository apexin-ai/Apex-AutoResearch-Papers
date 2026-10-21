# ops westd cleanup and cellc check

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd-cleanup-and-cellc-check_20260520T152944_result.json`
- **Structured JSON:** [`a0abd6dd6a8e03822ea5.json`](../../sessions/a0/a0abd6dd6a8e03822ea5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 任务 1：清理 westd 僵尸 vLLM 进程 — 完成

- PID 876718/876719 已确认存在（VLLM::Worker_TP0/TP1，各占 ~2.7GB RSS）
- `kill -9` 执行成功
- nvidia-smi 确认 4 张卡全部 0MiB，无残留进程

### 任务 2：Cell C 训练进度 — 已崩溃

- **PID 766820 已不存在**，进程已死
- 对应 wandb run `sx7h864t`，日志位于 `/root/autodl-tmp/cost-verify-agent-rl/RAGEN/outputs/2026-05-20/20-44-18/`
- **完成 1/15 步**（7%），每步耗时 ~33 分钟
- 最后一条日志 `2026-05-20 23:29:46`，报错：`ERROR: Exception while sending command.`（疑似 ScienceWorld 环境通信异常）
- Step 1 指标：
  - `success: 0.0`，`pass@8: 0.0`（无成功 episode）
  - `score: 2.74`，`final_score: 5.44`
  - `action_is_valid: 44%`，`action_is_effective: 89.7%`
  - `actor/kl_loss: 0.363`，`response_length/mean: 2952`

---
