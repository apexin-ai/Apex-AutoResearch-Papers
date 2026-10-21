# survey westd full status

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_survey_westd_full_status_20260521T235529_result.json`
- **Structured JSON:** [`2b2a77bd878d5ae7f2ab.json`](../../sessions/2b/2b2a77bd878d5ae7f2ab.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-29022 GPU 状态总结

| GPU | 任务 | PID | 进度 | 最新 Acc | 状态 |
|-----|------|-----|------|---------|------|
| 0 | eval_gsm8k_sft_alpha4_20_v4 | 426311 | **820/1319 (62%)** | 0.6125 (@800) | 运行中 |
| 1 | eval_math500_grpo_random_20_v2 | 382472 | **498/500 (99.6%)** | 0.1244 (@450) | 即将完成 |
| 2 | eval_math500_grpo_alpha4_20 | 412822 | **388/500 (78%)** | 0.2743 (@350) | 运行中 |
| 3 | eval_math500_sft_random_20 | 385685 | **466/500 (93%)** | 0.1200 (@450) | 运行中 |

**关键发现：**
- **无空闲 GPU**，4 张卡全部占满
- **GPU 1** 还剩 2 个样本，预计几分钟内完成
- **GPU 3** 还剩 34 个样本，预计 ~40min 完成
- **GPU 2** 还剩 112 个样本，预计 ~2h 完成
- **GPU 0 (D100 critical)** 还剩 499 个样本，预计 ~1.5h 完成

**Accuracy 速览：**
- GSM8K sft_alpha4_20: **61.25%** (trending, 进行中)
- MATH500 grpo_random_20: **12.44%** (接近最终)
- MATH500 grpo_alpha4_20: **27.43%** (进行中)
- MATH500 sft_random_20: **12.00%** (接近最终)

---
