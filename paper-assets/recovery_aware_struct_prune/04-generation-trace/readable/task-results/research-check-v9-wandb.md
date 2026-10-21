# research check v9 wandb

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_check_v9_wandb_20260516T014728_result.json`
- **Structured JSON:** [`d15c2ad9ada8738df40a.json`](../../sessions/d1/d15c2ad9ada8738df40a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### v9 RASP (`mrikafz3`) — `grpo_stage2_rasp_20_v9`

| 指标 | Step 10 值 | Collapse 阈值 | 判定 |
|------|-----------|--------------|------|
| grad_norm | **0.00735** | < 0.05 | COLLAPSED |
| frac_reward_zero_std | **0.875** | ≥ 0.85 | COLLAPSED |
| reward | **0.015** | < 0.03 | COLLAPSED |
| entropy | **0.054** | — | 极低 |
| loss | **0.0069** | — | 近零 |
| clipped_ratio | **0.956** | — | 95.6% 输出打满 max_length |
| mean_completion_length | **991.4** | max=1024 | 几乎全部截断 |

**状态**: running, step 10/30, runtime ~1.7h

**结论: Step 10 已全面 collapse**，三项 collapse 指标全部触发。与 v8 RASP 完全一致——collapse onset 在 step ≤10。由于 `logging_steps=10`，第一个数据点就是 step 10，无法从 wandb 判断 step 5 的精确状态。但 `save_steps=5` 意味着 **step 5 的 checkpoint 已保存在磁盘**——这是可能的 pre-collapse/early-collapse 快照，需要 SSH 到服务器手动检查。

### v8 Standard (`q34vz8j2`) — `grpo_stage2_standard_20_v8`

| 指标 | Step 90 值 | 判定 |
|------|-----------|------|
| grad_norm | **2.14** | 健康 |
| frac_reward_zero_std | **0.475** | 健康 |
| reward | **0.065** | 健康 |
| entropy | **0.151** | 正常 |
| clipped_ratio | **0.588** | 正常 |

**状态**: running, step 90/100, runtime ~10.9h。预计 ~1h 内跑完最后 10 步。训练完全健康，无 collapse 迹象。

### 对比

| | v9 RASP (step 10) | v8 Standard (step 90) |
|--|-------------------|----------------------|
| reward | 0.015 | 0.065 |
| grad_norm | 0.007 | 2.14 |
| frac_zero_std | 0.875 | 0.475 |
| collapse | **YES** | **NO** |

v9 RASP 复现了 v8 RASP 的 collapse 模式——RASP 剪枝模型在 GRPO 训练中迅速 collapse（step ≤10），而 standard 剪枝模型健康训练到 100 步。核心发现稳固。关键下一步：SSH 检查 step 5 checkpoint 是否捕获了 collapse 前的状态。

---
