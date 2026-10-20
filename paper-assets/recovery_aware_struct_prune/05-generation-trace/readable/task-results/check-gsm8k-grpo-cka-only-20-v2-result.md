# check gsm8k grpo cka only 20 v2 result

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_gsm8k_grpo_cka_only_20_v2_result_20260518T083323_result.json`
- **Structured JSON:** [`038a49b39dc0cfbeb993.json`](../../sessions/03/038a49b39dc0cfbeb993.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。

**eval_gsm8k_grpo_cka_only_20_v2 结果：**

| 指标 | 值 |
|---|---|
| accuracy | **64.37%** (849/1319) |
| stderr | ±1.32% |
| eos_rate | 98.86% |
| avg_response_length | 203.4 tokens |
| wall_time | ~2h29m |
| status | DONE (success) |

**Tab2 对比：**

| Method | SFT | GRPO | GRPO vs SFT |
|---|---|---|---|
| CKA-only | 63.91% | **64.37%** | +0.46pp |
| Standard | 59.29% | 58.91% | -0.38pp |
| RASP | 61.49% | 61.87% | +0.38pp |

CKA-only GRPO (64.37%) > CKA-only SFT (63.91%)，GRPO 对 CKA-only 恢复有正向增益，但幅度不大 (+0.46pp，在 stderr 范围内)。CKA-only 在 SFT 和 GRPO 两个阶段都是所有方法中最高的。

---
