# research check grpo stage2 progress

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_check_grpo_stage2_progress_20260515T033013_result.json`
- **Structured JSON:** [`f6b78690c33e67a53af9.json`](../../sessions/f6/f6b78690c33e67a53af9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GRPO Stage 2 训练进度报告

### 进程状态

| | RASP (cuda:0) | Standard (cuda:1) |
|---|---|---|
| **PID** | 263893 (子进程) | 263971 (子进程) |
| **状态** | 运行中 | 运行中 |
| **已运行** | 2h 19m | 2h 19m |

### 训练进度

| | RASP | Standard |
|---|---|---|
| **进度** | **1/500** (0.2%) | **1/500** (0.2%) |
| **速度** | 6655 s/step (~111 min) | 6725 s/step (~112 min) |
| **ETA** | **922 小时 (38.4 天)** | **932 小时 (38.8 天)** |
| **训练指标** | 无（logging_steps=10） | 无 |
| **Checkpoints** | 无（save_steps=100） | 无 |

### GPU 状态

| GPU | 利用率 | 显存 | 温度 |
|---|---|---|---|
| cuda:0 (RASP) | 100% | 52GB / 98GB | 82°C |
| cuda:1 (Standard) | 100% | 52GB / 98GB | 81°C |

### W&B

| | Run Name | Run ID |
|---|---|---|
| RASP | `grpo_stage2_rasp_20` | `ve3er9un` |
| Standard | `grpo_stage2_standard_20` | `mqu3sg7j` |

两个 wandb run 最后写入时间均为 11:29，正在正常同步。

### 关键问题

**速度严重偏慢。** 每步 ~111 分钟，500 步需要 38 天。原因：
- `max_completion_length=4096` × `num_generations=4` × `batch_size=2` = 每个 micro-batch 生成 8 条长序列
- `gradient_accumulation_steps=8` → 每个 optimizer step 需要生成 64 条最长 4096 token 的 completion

**无法判断学习信号。** `logging_steps=10`，第一批指标要到 step 10 才输出（约开始后 ~18.5 小时，即今晚 ~03:45 左右）。目前无法确认 grad_norm > 0、reward 趋势、或 completion_length 是否截断。

**第一个 checkpoint 在 step 100**，约 19 天后才会保存。

### 建议

如果 38 天不可接受，可以考虑中断后调参重跑：
- `max_completion_length` 从 4096 降到 2048（速度提升最显著）
- `num_generations` 从 4 降到 2
- `gradient_accumulation_steps` 从 8 降到 4

但这些会影响 GRPO 训练质量。建议至少等到 step 10（今晚 ~03:45）看到第一批指标再决定是否调整。

---
