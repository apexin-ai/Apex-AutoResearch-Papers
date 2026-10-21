# check westd full status

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_westd_full_status_20260520T091005_result.json`
- **Structured JSON:** [`6ab20335e6cfe4d12338.json`](../../sessions/6a/6ab20335e6cfe4d12338.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-29022 实验状态汇报

### GPU 总览

| GPU | 利用率 | 显存 | 状态 |
|-----|--------|------|------|
| 0 | 86% | 11.5/97.9 GB | 30% CKA-only eval 运行中 |
| 1 | 86% | 11.6/97.9 GB | 30% Standard eval 运行中 |
| 2 | 0% | 0 GB | **空闲** |
| 3 | 0% | 0 GB | **空闲** |

---

### 30% CKA-only eval (GPU 0) — 运行中

- 进度: **323/1319** (24.5%)
- 启动: 12:53, 已跑 ~4h15m
- 中间指标 (300样本): **acc=1.33%**, eos_rate=5.33%, avg_len=3999
- 速度: ~47.7s/sample
- 预计剩余: **~13.2h**, ETA 约明天 06:20

### 30% Standard eval (GPU 1) — 运行中

- 进度: **318/1319** (24.1%)
- 启动: 12:53, 已跑 ~4h15m
- 中间指标 (300样本): **acc=3.00%**, eos_rate=2.00%, avg_len=4031
- 速度: ~47.9s/sample
- 预计剩余: **~13.3h**, ETA 约明天 06:30

> 两个 eval 的 acc 都极低 (1.3%/3.0%)，avg_len 接近 max_tokens=4096，几乎所有 sample 都在打满 token 而不终止。

---

### GRPO seed123 (GPU 2) — 已完成 ✅

- 100/100 步, 耗时 46m23s, 15:12 完成
- 模型已保存: `grpo_standard_20_seed123/model.safetensors` (12.3GB)
- Reward trajectory (每10步):

| Step | reward_mean | frac_zero_std |
|------|-------------|---------------|
| 10 | 0.0431 | 0.650 |
| 20 | 0.0413 | 0.575 |
| 80 | 0.0619 | 0.400 |
| 90 | 0.0306 | 0.500 |
| 100 | **0.0594** | 0.600 |

- Peak reward: **0.0619** (step 80)
- W&B: offline run `pgzwv725`

### GRPO seed456 (GPU 3) — 已完成 ✅

- 100/100 步, 耗时 45m45s, 15:11 完成
- 模型已保存: `grpo_standard_20_seed456/model.safetensors` (12.3GB)
- Reward trajectory:

| Step | reward_mean | frac_zero_std |
|------|-------------|---------------|
| 10 | 0.0738 | 0.525 |
| 20 | 0.0456 | 0.675 |
| 80 | 0.0444 | 0.575 |
| 90 | 0.0844 | 0.525 |
| 100 | **0.0600** | 0.650 |

- Peak reward: **0.0844** (step 90)
- W&B: offline run `wg0iv4oi`

---

### 磁盘

`/root/autodl-tmp`: **594G/619G (96%)**, 剩余 26G — 偏紧

### 空闲 GPU

**cuda:2, cuda:3** 空闲，可立即分配新任务。

---
