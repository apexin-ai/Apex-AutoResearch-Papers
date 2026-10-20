# ssh check westd eval progress

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_westd_eval_progress_20260520T162531_result.json`
- **Structured JSON:** [`21324a128980aa4ec347.json`](../../sessions/21/21324a128980aa4ec347.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

| GPU | 任务 | 状态 | 进度 | 准确率 | 备注 |
|-----|------|------|------|--------|------|
| cuda:1 | eval_gsm8k_sft_cka_only_15 | **ALIVE** | 158/1319 (12%) | 80.67% @150 | 运行 20m47s，~3.1s/it，ETA ~60min |
| cuda:2 | eval_gsm8k_sft_standard_15 | **DONE** | 1319/1319 | **66.49%** (877/1319) | 已保存结果 |
| cuda:3 | eval_gsm8k_grpo_standard_15_v2 | **DONE** | 1319/1319 | **66.11%** (872/1319) | 已保存结果 |

两个已完成任务的 eos_rate 均为 99.3%，avg_response_length ~183-184 tokens。sft_cka_only_15 目前中期 acc 80.67%，显著高于另外两个。

---
