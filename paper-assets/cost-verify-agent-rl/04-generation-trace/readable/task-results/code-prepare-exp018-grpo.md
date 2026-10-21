# code prepare exp018 grpo

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prepare-exp018-grpo_20260514T154338_result.json`
- **Structured JSON:** [`0c36bed0a67ce8e3a959.json`](../../sessions/0c/0c36bed0a67ce8e3a959.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp018 配置报告

- **配置文件**: `/root/cost-verify-agent-rl/RAGEN/config/_alfworld_exp018_sft_grpo.yaml`
- **启动脚本**: `/root/cost-verify-agent-rl/scripts/run_exp018.sh`
- **SFT checkpoint 预期路径**: `/root/autodl-tmp/checkpoints/exp017_expert_sft/final/`

关键参数确认：
| 参数 | 值 |
|------|-----|
| model_path | exp017 SFT checkpoint |
| LR | 5e-7 |
| kl_loss_coef | 0.1 |
| grad_clip | 1.0 |
| resume_mode | disable |
| total_steps | 30 |
| env_groups | 4, group_size 16 |
| format_penalty | 0 |

**待完成**: exp017 训练结束后确认 `/root/autodl-tmp/checkpoints/exp017_expert_sft/final/` 存在，然后可直接 `nohup bash scripts/run_exp018.sh` 启动。

---
