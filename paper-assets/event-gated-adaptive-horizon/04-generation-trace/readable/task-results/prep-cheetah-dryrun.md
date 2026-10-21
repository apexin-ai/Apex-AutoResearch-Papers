# prep cheetah dryrun

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_cheetah_dryrun_20260514T095445_result.json`
- **Structured JSON:** [`8b43547f9e4b9bb94a4e.json`](../../sessions/8b/8b43547f9e4b9bb94a4e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Dry-Run 验证结果

### dmc_cheetah_run: 可用

环境正常创建，prefill 完成，训练循环启动，metrics.jsonl 正常写入。无需任何代码或配置修改，直接用 `--configs defaults dmc_proprio --task dmc_cheetah_run` 即可。

### Obs/Action Space 对比

| | Cheetah Run | Walker Walk |
|---|---|---|
| obs keys | position(8), velocity(9) | orientations(14), height(1), velocity(9) |
| **total obs dim** | **17** | **24** |
| **action dim** | **6** | **6** |
| action range | [-1, 1] | [-1, 1] |

- **Action space 完全一致**（6维，连续，[-1,1]）
- **Obs space 维度不同**（17 vs 24），但 `dmc_proprio` 配置用 MLP encoder（`mlp_keys: '.*'`），自动适配输入维度，无需修改网络架构

### Metrics 格式

与 Walker Walk 一致：`{"step", "dataset_size", "train_return", "train_length", "train_episodes"}`

### 其他
- Prefill 阶段随机 return：~4-7（符合预期，随机策略下 cheetah 能获得少量前进奖励）
- CPU 上 prefill 2500步约需 2 分钟，训练很慢（不适合正式实验，仅验证用）
- 无需额外配置修改，plan_020 可以直接启动

---
