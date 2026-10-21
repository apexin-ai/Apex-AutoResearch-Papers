# analysis grpo random 20 early wandb

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_grpo_random_20_early_wandb_20260517T144342_result.json`
- **Structured JSON:** [`ff229c8e8b04daad8cf4.json`](../../sessions/ff/ff229c8e8b04daad8cf4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成，写入 `artifacts/grpo_random_20_early_analysis.md`。

核心发现：

1. **所有三个 run 的 logging_steps=10，W&B 在 steps 1-8 没有任何数据。** Step 10 是最早的 log 点。

2. **grpo_random_20 目前在 step 8**，step time 从 314s 缓慢增长到 378s（+20%），属于正常范围。**没有发现 immediate collapse 信号**（RASP v9 的 catastrophic collapse 到 step 10 时 grad_norm 已降至 0.007、mean_length 991/1024）。

3. **初步判断倾向 Scenario B 或 C**（Random collapse 晚于 RASP），这对论文叙事有利：说明 CKA-aware pruning（RASP）特别伤 RL recovery，而不是所有结构剪枝都导致 immediate collapse。

4. **预测 Random collapse 窗口：step 20-40**（介于 RASP 的 ~10 和 Standard 的 ~60 之间），但置信度低，需 step 10 数据确认。

5. **关键下一步**：step 10 的 W&B 数据将在 ~22:51 UTC 可用，届时可直接判断 Random 是否已 collapse。

---
