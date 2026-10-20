# harvest cka only 25 math500 logs

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_cka_only_25_math500_logs_20260521T223435_result.json`
- **Structured JSON:** [`cb39b9e0a1396c43b967.json`](../../sessions/cb/cb39b9e0a1396c43b967.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验已经在 registry 中，且已是 DONE + success 状态，metrics 也已填入：

| 实验 | 状态 | Accuracy | Correct/Total |
|------|------|----------|---------------|
| `eval_math500_grpo_cka_only_25_v2` | DONE/success | 18.4% (±0.0173) | 92/500 |
| `eval_math500_sft_cka_only_25_v2` | DONE/success | 19.2% (±0.0176) | 96/500 |

**Registry 已经是最新的，无需更新。** 两个实验的结果之前已被恢复并注册。

确认关键发现：SFT (19.2%) > GRPO (18.4%)，CKA-only 25% 剪枝在 MATH-500 上 GRPO 未能提升甚至略低于 SFT baseline，与 GSM8K 上的趋势一致（SFT 60.12% vs GRPO 59.59%）。两个日志中均无 truncated 样本。

---
