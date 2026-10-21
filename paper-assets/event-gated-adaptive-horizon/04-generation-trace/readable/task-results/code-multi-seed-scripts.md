# code multi seed scripts

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_multi_seed_scripts_20260514T063238_result.json`
- **Structured JSON:** [`1796ab95c647e07080f3.json`](../../sessions/17/1796ab95c647e07080f3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 产出

**脚本路径**: `/root/autodl-tmp/event-gated-adaptive-horizon/scripts/multi_seed_runs.sh`

6 个实验命令，`cuda:X` 占位：

| exp_id | 配置 | steps | seed |
|--------|------|-------|------|
| exp_baseline_walker_s2 | vanilla DreamerV3 | 512K | 2 |
| exp_baseline_walker_s3 | vanilla DreamerV3 | 512K | 3 |
| exp_008d_walker_s2 | gate+dt_embed=32+subsample+H8 | 105K | 2 |
| exp_008d_walker_s3 | gate+dt_embed=32+subsample+H8 | 105K | 3 |
| exp_008f_walker_s2 | gate+dt_embed=0+subsample+H8 | 105K | 2 |
| exp_008f_walker_s3 | gate+dt_embed=0+subsample+H8 | 105K | 3 |

**Seed 参数行为**: `--seed` 同时控制 model seed 和 env seed。`set_seed_everywhere` 设置 `torch.manual_seed`、`torch.cuda.manual_seed_all`、`np.random.seed`、`random.seed`；env 侧用 `config.seed + env_id`。

**008d 的 gate_dt_embed_dim**: 默认值 **32**（`configs.yaml` 第 102 行），008d 原始命令未显式传此参数，使用默认值。

---
