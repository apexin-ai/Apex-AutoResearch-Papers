# check math500 all progress v3

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_math500_all_progress_v3_20260518T045447_result.json`
- **Structured JSON:** [`1c129d00f7e5522b8bb3.json`](../../sessions/1c/1c129d00f7e5522b8bb3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下：

| 实验 | 服务器 | 进度 | Accuracy | 预估剩余 |
|---|---|---|---|---|
| **grpo_standard_20** | westd cuda:1 | **438/500** (88%) | 28.3% @300 | ~3h (avg ~180s/it × 62) |
| **grpo_rasp_20_v3** | westd cuda:3 | **422/500** (84%) | 25.0% @400 | ~4h (avg ~190s/it × 78) |
| **grpo_unpruned** | westd cuda:2 | **500/500 Done** | **69.0%** | - |
| **sft_cka_only_20_v2** | westd cuda:0 | **101/500** (20%) | 39.0% @100 | ~8-10h (avg ~75s/it × 399) |
| **grpo_cka_only_20** | westb cuda:1 | **80/500** (16%) | 32.0% @50 | ~10-12h (avg ~100s/it × 420) |

grpo_unpruned 已完成，accuracy 69.0%。grpo_standard_20 和 grpo_rasp_20_v3 预计今天内完成。sft_cka_only_20_v2 和 grpo_cka_only_20 速度较慢，预计明天凌晨才能跑完。

---
