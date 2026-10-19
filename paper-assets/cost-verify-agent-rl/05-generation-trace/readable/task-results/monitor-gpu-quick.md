# monitor gpu quick

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_gpu_quick_20260513T202516_result.json`
- **Structured JSON:** [`c0301916cacc3099044c.json`](../../sessions/c0/c0301916cacc3099044c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态汇报

### 1. GPU 进程

| GPU | PID | 进程 | 显存 | 利用率 |
|-----|-----|------|------|--------|
| cuda:0 | 120321 | `ray::WorkerDict.actor_rollout_generate_sequences` | 43612 MiB / 97887 MiB | 98% |
| cuda:1 | 120322 | `ray::WorkerDict.actor_rollout_generate_sequences` | 43614 MiB / 97887 MiB | 97% |

温度正常（72°C / 68°C），功耗 376W / 349W。

### 2. 实验身份

**exp_002**，配置 `_alfworld_exp002`，无 exp_001b 残留。

- 主进程 PID 116879：`python train.py --config-name _alfworld_exp002`
- tmux session: `exp_002`
- `CUDA_VISIBLE_DEVICES=0,1`
- 模型：**Qwen3 1.72B**（vocab_size=151936, tie_word_embeddings=true）
- 环境：AlfWorld，3553 训练 games，140 验证 games

### 3. 训练进度

刚完成**初始验证**（step 0/100），尚未开始第一个训练 step。

初始验证指标：
- **success: 0.0**
- pass@1: 0.0
- raw_reward: 0.0
- manager_invalid_action: **73.75%**（大部分动作无效）
- action_is_valid: 15.1%
- action_is_effective: 26.25%
- 验证耗时 699s（~12 min）

训练进度条刚显示 `0%| | 0/100`，正在开始第一个 training step。

---
