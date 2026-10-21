# code exp029 seed2 submit

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp029_seed2_submit_20260518T051247_result.json`
- **Structured JSON:** [`cf2bb612c444205f81da.json`](../../sessions/cf/cf2bb612c444205f81da.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**exp029_episode_level_seed2 已经在 bjb1-17606 上启动并正常运行。** 无需再做验证或提交。

## 当前状态汇总

| 项目 | 状态 |
|---|---|
| **训练进程** | 已在运行（PID 509, tmux session `exp029_episode_level_seed2`, 启动于 13:10） |
| **wandb** | 已连接，run ID `vugdm2sw`，[查看链接](https://wandb.ai/xiaoyucorynne-/cost-verify-agent-rl/runs/vugdm2sw) |
| **GPU** | cuda:0,1 被训练进程占用（各 ~36GB），正常 |
| **磁盘** | /root/autodl-tmp 122GB 可用，充足 |
| **SFT checkpoint** | `/root/autodl-tmp/checkpoints/qwen3_exp021_ragen_sft_v4` 存在 |
| **配置** | seed.train=43, experiment_name=exp029-episode-level-seed2 |
| **输出目录** | `/root/autodl-tmp/checkpoints/exp029-seed2/` |

### 需要注意

**`total_training_steps: 15`**（seed2 配置）vs 原始 exp029 的 `100`。如果目标是完整复现，训练完成后可能需要增加 steps 重跑或 resume。请确认 15 steps 是否为预期设置。

---
