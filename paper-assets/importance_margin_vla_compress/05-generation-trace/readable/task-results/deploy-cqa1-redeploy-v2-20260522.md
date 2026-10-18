# deploy cqa1 redeploy v2 20260522

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_cqa1_redeploy_v2_20260522_20260522T211115_result.json`
- **Structured JSON:** [`bd0c4d65b63b09b052b2.json`](../../sessions/bd/bd0c4d65b63b09b052b2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成，汇总：

**部署状态**：
| GPU | 任务 | VRAM | 状态 |
|-----|------|------|------|
| cuda:0 | L2norm k=0.7 Goal seed42 | 9781 MiB | 运行中，`n_keep=179/256` |
| cuda:1 | Random k=0.95 Goal seed42 | 10308 MiB | 运行中，`n_keep=243/256` |
| cuda:2 | Random k=0.3 Goal seed42（已有） | 10140 MiB | 运行中 |
| cuda:3 | L2norm k=0.9 Long seed42（已有） | 10525 MiB | 运行中 |

**修复内容**：
1. 添加 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base` 解决 `python: command not found`
2. `TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache` 环境变量已生效，tokenizer 离线加载成功

**Registry**：
- `eval_pi05_l2norm_k07_goal_seed42`：spec 已更新到 cqa1-33015（状态 DEPLOYED，旧条目不可转 RUNNING）
- `eval_pi05_random_k095_goal_seed42`：RUNNING

---
