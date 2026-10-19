# ops c2s42 eval final check

**tbab multi turn** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_c2s42-eval-final-check_20260518T235652_result.json`
- **Structured JSON:** [`59d342bd8f6b617be81e.json`](../../sessions/59/59d342bd8f6b617be81e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## C2_s42 Eval 最终结果

**状态**: eval 已完成，tmux session 已退出。结果文件写入于 `2026-05-19T07:07`。

### Overall

| 指标 | 值 |
|------|-----|
| **P̄** | **5.49%** (5/91) |
| a90 | 0.0 |
| u10_90 | 38.5% |
| Model | `c2_pos_reset_seed42/checkpoint-471` |
| Condition | `position_reset` |

### Per-source

| Source | Pass | Rate |
|--------|------|------|
| sharded-HumanEval | 3/36 | **8.3%** |
| sharded-livecodebench | 2/55 | **3.6%** |

### Per-turn 分析

| num_turns | Pass | Rate |
|-----------|------|------|
| 1 | 4/4 | **100.0%** |
| 5 | 1/9 | 11.1% |
| 6 | 0/21 | 0.0% |
| 7 | 0/18 | 0.0% |
| 8 | 0/18 | 0.0% |
| 9 | 0/9 | 0.0% |
| 10+ | 0/12 | 0.0% |

### Passed samples

- `sharded-HumanEval/25` — num_turns=1, num_shards=6
- `sharded-HumanEval/7` — num_turns=5, num_shards=5
- `sharded-HumanEval/97` — num_turns=1, num_shards=5
- `sharded-livecodebench/2876` — num_turns=1, num_shards=8
- `sharded-livecodebench/2917` — num_turns=1, num_shards=5

### 关键发现

模型几乎只能解 num_turns=1 的问题（4/4=100%），num_turns>=6 全部失败。唯一的多轮通过是 HumanEval/7（5 turns）。这表明 position_reset 条件下模型的多轮代码生成能力极弱。

### 系统状态

- **GPU**: RTX PRO 6000, 0MiB/97887MiB, 0% util, idle
- **磁盘**: 18G/30G used (59%)

---
