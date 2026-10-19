# check exp029 progress 2h20m

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp029_progress_2h20m_20260516T150629_result.json`
- **Structured JSON:** [`43605c6220d0ff8c71e1.json`](../../sessions/43/43605c6220d0ff8c71e1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp029_episode_level 训练进度

**进程状态**: PID 868459 存活，已运行 **~3h25m**

**当前阶段**: `val_before_train` — 初始化完成后正在做训练前验证，评估 **140 个 ALFWorld games**（`eval_in_distribution` split）

**W&B Run**:
- Run ID: `5rapt9f1`
- Run Name: `exp029-alfworld-episode-level`
- URL: `https://wandb.ai/xiaoyucorynne-/cost-verify-agent-rl/runs/5rapt9f1`

**GPU 状态**: 两卡均 0% utilization，显存 4.7GB/98GB（模型已加载但 ALFWorld rollout 主要消耗 CPU）

**关键配置**:
- 模型: Qwen3 1.72B（从 `qwen3_exp021_ragen_sft_v4` 加载）
- 总训练步数: 100 steps, 30 epochs
- val: 140 env_groups × group_size 1
- train: 16 env_groups × group_size 8
- ALFWorld: `parallel_friendly: False, max_workers: 1`，50 max actions/traj
- Checkpoint: `/root/autodl-tmp/checkpoints/exp029/`, save_freq=5

**Metrics**: **尚无训练 metrics**。训练尚未开始，停留在 val_before_train。

**Warnings（非致命）**:
- Ray docker CPU 检测警告
- Gym -> Gymnasium 迁移提醒
- FSDP state_dict_type 弃用警告
- Mistral tokenizer regex 模式不匹配警告

**诊断**: TaskRunner (PID 871702) 占 82% CPU，说明正在活跃执行 ALFWorld 环境交互。因为 `parallel_friendly: False` + `max_workers: 1`，140 个 games 是**串行执行**的，每个 game 最多 50 turns。所有输出被缓冲（stdout 重定向到文件），日志将在 val_before_train 结束后批量刷出。不是 hang，是 ALFWorld 串行 eval 本身就慢。

---
