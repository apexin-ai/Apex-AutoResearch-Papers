# ops registry standard fair

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_registry_____standard_fair_20260519T063521_result.json`
- **Structured JSON:** [`9ce463a910518f65f6df.json`](../../sessions/9c/9ce463a910518f65f6df.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个任务的实际状态与预期不同：

## Task B: `grpo_standard_20_fair`

**已经是 DONE/success**，不需要更新。Registry 完整记录如下：
- **status**: DONE, **conclusion**: success
- **W&B**: `tyv20u2k`
- **server**: westd-11672 (原始)，checkpoint 在 westd-29022
- **checkpoint**: `/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_fair`
- **metrics**: total_steps=100, runtime=3017s, peak_reward=0.081 (step 40), final_reward=0.054
- **dynamics**: `dip_then_partial_recovery` — reward flat 0.03-0.08，frac_zero_std stuck 0.5-0.55

## Task A: `eval_gsm8k_grpo_standard_20_fair`

**GSM8K eval 不存在**。搜索确认：
1. 服务器上无 `*gsm8k*standard*fair*` 结果文件
2. `bootstrap_ci_accuracy_v2.json` 明确记录: `"grpo_standard_20": "no n=1319 eval (only 25% available)"`
3. 数字 `0.5891` 不存在于任何结果文件中
4. 唯一存在的 GSM8K 标准模型 eval 是 300 步 extended: accuracy=59.29% (782/1319)

**需要先在 westd-29022 上跑 GSM8K eval**，然后才能注册。要现在提交评测任务吗？

---
