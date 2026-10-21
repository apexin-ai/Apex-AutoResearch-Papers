# exp grpo unpruned v2 launch

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_grpo-unpruned-v2-launch_20260516T014541_result.json`
- **Structured JSON:** [`d92e9c6dadcc61b93532.json`](../../sessions/d9/d92e9c6dadcc61b93532.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Unpruned GRPO v2 训练已成功启动：

| 项目 | 值 |
|------|-----|
| PID | 75381 |
| GPU | cuda:1, 44836 MiB |
| wandb run | `nhsx0bt2` |
| wandb URL | https://wandb.ai/xiaoyucorynne-/recovery_aware_struct_prune/runs/nhsx0bt2 |
| tmux session | `grpo_unpruned_v2` |
| 输出目录 | `/root/autodl-tmp/recovery_aware_struct_prune/grpo_unpruned_v2` |
| 配置 | beta=0.01, loss=dapo, lr=1e-6, temp=0.4, rep_pen=1.15, format_reward=0.1, 100 steps |

首次启动时因缺少 wandb 凭据失败，已从 westb-23072 复制 `.netrc` 到 westd-11672 并加上 `source /etc/network_turbo` 后成功重启。

---
