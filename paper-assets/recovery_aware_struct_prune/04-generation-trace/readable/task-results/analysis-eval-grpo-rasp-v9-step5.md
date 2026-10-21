# analysis eval grpo rasp v9 step5

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_grpo_rasp_v9_step5_20260516T044244_result.json`
- **Structured JSON:** [`a67ceff417fd1b4823b5.json`](../../sessions/a6/a67ceff417fd1b4823b5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Got all the data. Here's the full analysis:

---

## eval_grpo_rasp_v9_step5 结果报告

### 原始指标

| 指标 | 值 |
|------|-----|
| **Accuracy** | **60.65% (800/1319)** |
| Stderr | ±1.35pp |
| EOS rate | 98.56% (1300/1319 natural) |
| Truncated | 19 |
| Avg response length | 205.3 tokens |
| Min response length | 42 tokens |
| Max response length | 4096 tokens |
| Mode | greedy (T=0.0, do_sample=false) |
| Model path | `/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_v9/checkpoint-5` |

### 基准对比

| 对比基准 | 基准 acc | v9-step5 acc | Δpp |
|----------|---------|-------------|-----|
| Standard GRPO v8 step-50 | 58.91% | 60.65% | **+1.74** |
| RASP SFT baseline | 61.49% | 60.65% | **−0.84** |
| Standard SFT baseline | 59.29% | 60.65% | **+1.36** |
| Unpruned SFT baseline | 81.27% | 60.65% | **−20.62** |

### 分析

1. **Step 5 是 v9 最好的 checkpoint。** 60.65% 超过了 Standard GRPO v8 经过 50 步训练的最终结果（+1.74pp），说明 RASP 剪枝模型在 GRPO 初期恢复能力更强。

2. **略低于 RASP SFT baseline（−0.84pp）。** 在 stderr 范围内（±1.35pp），差异不显著。说明 step-5 时 GRPO 尚未对 RASP SFT 起点产生明显增益，但也没有损害。

3. **Collapse 时间线验证。** v9 训练 metrics 显示 step 10 已经 reward=0.015, frac_zero_std=0.875，step 30 彻底 collapse。Step 5 的 60.65% 与 RASP SFT baseline 接近，表明此时模型还基本保持了 SFT 阶段的能力，collapse 尚未开始。

4. **EOS 健康。** 98.56% 的 natural EOS rate，仅 19 条 truncated，生成行为正常。

5. **核心结论：RASP GRPO v9 的 peak performance 在 collapse 前约 60.65%，与 RASP SFT 持平，未能通过 GRPO 进一步提升。collapse 发生在 step 5-10 之间，导致后续步骤全部退化。**

---
