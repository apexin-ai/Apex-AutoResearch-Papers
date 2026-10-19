# ops kill exp029 deploy h20 bjb1

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill-exp029-deploy-h20-bjb1_20260518T180531_result.json`
- **Structured JSON:** [`0d5a37c686d3b8e8bc60.json`](../../sessions/0d/0d5a37c686d3b8e8bc60.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已成功启动，进入 step 0/15。

## 报告

| 项目 | 状态 |
|------|------|
| **exp029_seed2 kill** | 已 kill PID 66897，ray 已清理，无残留进程。checkpoints/logs 保留 |
| **h=20 config** | 使用已有 `_alfworld_hsweep_h20.yaml`，修改 `val_before_train: false`、`max_actor_ckpt_to_keep: 3` |
| **训练启动** | PID **71823**，tmux session `hsweep_h20_seed1` |
| **W&B run** | `hsweep-h20-seed1`，run ID **qoan2ma6** |
| **W&B URL** | `https://wandb.ai/xiaoyucorynne-/cost-verify-agent-rl/runs/qoan2ma6` |
| **Log path** | `~/runs/cost-verify-agent-rl/hsweep_h20_seed1.log` |
| **磁盘** | `/root/autodl-tmp` 103GB 可用（60% 使用） |

**Config 关键参数**: model=Qwen3 1.72B (SFT v4), h=20, seed=10000, 15 steps, GRPO, lr=1e-6, GPU 0,1, max_ckpt=3

---
