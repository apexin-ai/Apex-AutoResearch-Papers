# ssh create s46 configs and cleanup

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_create-s46-configs-and-cleanup_20260516T184715_result.json`
- **Structured JSON:** [`bb7fe8cded2adf92cdcd.json`](../../sessions/bb/bb7fe8cded2adf92cdcd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All configs created and verified. Here's the summary:

## Task 1: Configs Created ✓

| File | seed | batch_size | reward_mode | beta |
|------|------|-----------|-------------|------|
| `sweep_exec_only_s46.yaml` | 46 | 2 | execution_only | — |
| `sweep_random_b01_s46.yaml` | 46 | 2 | additive_random | 0.1 |
| `sweep_isr_b01_s46.yaml` | 46 | 2 | additive_bonus | 0.1 |

All have `save_total_limit: 1`, `num_steps: 500`, `data_path: data/train_500_seed42.jsonl`.

## Task 2: 磁盘状态

**当前可用: 50G**（比预期好，`df` 显示 201G used / 250G total）

大目录清理候选：

| 目录 | 大小 | 内容 | 备注 |
|------|------|------|------|
| `gated_warmstart_v3_s43_r2/` | 31G | final model + checkpoint-300 | 旧 gated 实验 |
| `gated_warmstart_v3_t015_s43/` | 30G | final model + checkpoint-300 | 旧 gated 实验 |
| `exec_retrain_v3_s42/` | 15G | 仅 checkpoint-200 + log | 中间 checkpoint，无 final model |
| `exec_retrain_v3_s43/` | 15G | 仅 checkpoint-200 + log | 同上 |
| `plan001_exec_only_s43_1000_r2/` | 16G | final model + eval results | 论文用数据 |
| `plan001_exec_only_s44_1000_r2/` | 16G | final model + eval results | 论文用数据 |
| `plan018_additive_random_b01_s44_r2/` | 16G | final model + eval + taxonomy | 论文用数据 |
| `w2_1.7b_exec_only_s42/` | 13G | final model + checkpoint-500 | width 实验 |
| `w2_1.7b_isr_b01_s42/` | 13G | — | width 实验 |

**最安全的清理目标**（预估释放 ~91G）：
- `gated_warmstart_v3_*` 两个：61G（旧 gated curriculum 实验，已被 sweep 系列取代）
- `exec_retrain_v3_*` 两个：30G（仅中间 checkpoint，无 final model，应是失败/过渡实验）

**需谨慎**：plan001/plan018 有 eval results，可能是论文数据源。w2 是 width scaling 实验。

50G 当前已够跑两个 s46 实验（每个 ~16G final），但如果要留余量，清 gated_warmstart 两个就够。你决定删哪些。

---
