# check eval gsm8k alpha4 progress

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_eval_gsm8k_alpha4_progress_20260521T211148_result.json`
- **Structured JSON:** [`7651c09c25fb8a2e7c20.json`](../../sessions/76/7651c09c25fb8a2e7c20.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总报告

| 实验 | GPU | PID | 状态 | 进度 | 运行时间 | 当前 Acc | 预计剩余 |
|------|-----|-----|------|------|---------|---------|---------|
| eval_gsm8k_grpo_alpha4_20 | cuda:0 | 412988 | **ALIVE** | 689/1319 (52%) | 1h44m | **62.77%** @650 | ~1.5h |
| eval_math500_grpo_random_20_v2 | cuda:1 | 382470 | **ALIVE** | 364/500 (73%) | 7h15m | **10.86%** @350 | ~3h |
| eval_math500_grpo_alpha4_20 | cuda:2 | 412817 | **ALIVE** | 143/500 (29%) | 1h44m | **30.00%** @100 | ~5h |
| eval_math500_sft_random_20 | cuda:3 | 385685 | **ALIVE** | 331/500 (66%) | 6h27m | **10.67%** @300 | ~3h |

**磁盘**: /root/autodl-tmp 215G 可用 / 619G 总计 (66% used)

**要点**:
- 4 个实验全部在跑，无异常
- GSM8K eval (grpo_alpha4_20) acc 62.77%，进度过半
- MATH-500 上 grpo_alpha4_20 (30%) 远好于 grpo_random_20 (10.86%) 和 sft_random_20 (10.67%)，alpha4 剪枝的 GRPO 恢复效果显著

---
