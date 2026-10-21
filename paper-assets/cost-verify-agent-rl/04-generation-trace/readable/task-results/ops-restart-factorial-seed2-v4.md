# ops restart factorial seed2 v4

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_restart-factorial-seed2-v4_20260518T112102_result.json`
- **Structured JSON:** [`9d650ff466d27c40f337.json`](../../sessions/9d/9d650ff466d27c40f337.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 启动完成

### 前置检查结果
| 项目 | 状态 |
|------|------|
| g095 (PID 416289) | 运行中，GPU 2,3 各 26589MiB |
| GPU 0,1 | 启动前空闲 → 启动后各 4731MiB |
| RAM | 启动前 920Gi → 启动后 899Gi 可用（1Ti total） |
| /tmp 问题 | 已通过 TMPDIR=/root/autodl-tmp/tmp 绕过 |

### 启动信息
- **PID**: 576727
- **W&B run ID**: w0n74omu
- **tmux session**: factorial_seed2
- **Log**: `/root/autodl-tmp/cost-verify-agent-rl/logs/factorial_seed2_v4.log`
- **Training Progress**: 0/15 steps（已开始第一个 step 的 rollout）
- **val_before_train**: False（已确认跳过）

### 修正项
- 任务中的 `train_grpo_alfworld.py --config configs/...` 路径有误，实际入口是 `RAGEN/train.py --config-name` (Hydra)
- 首次启动因 tmux 环境缺少 conda PATH 导致 `python: command not found`，已通过 `export PATH=/root/miniconda3/bin:$PATH` 修复

### Registry & Cron
- Registry: RUNNING，spec 含完整 provenance
- Cron: 每 15 分钟自动检查（job ee68c5e2）

---
