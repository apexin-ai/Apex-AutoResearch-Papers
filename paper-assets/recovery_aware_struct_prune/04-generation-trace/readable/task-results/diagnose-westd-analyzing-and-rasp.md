# diagnose westd analyzing and rasp

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_westd_analyzing_and_rasp_20260519T130713_result.json`
- **Structured JSON:** [`896fd8335c6d1aec62aa.json`](../../sessions/89/896fd8335c6d1aec62aa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

| 实验 | 状态 | Accuracy | n_correct / n_total |
|------|------|----------|---------------------|
| eval_math500_sft_standard_20_2048_v2 | **DONE** ✓ | 25.8% | 129 / 500 |
| eval_math500_grpo_cka_only_20_2048 | **DONE** ✓ | 29.2% | 146 / 500 |
| eval_gsm8k_grpo_rasp_20_fair | **RUNNING** | ~66% (interim) | 249 / 1319 进行中 |

GSM8K eval 在 cuda:0 上正常运行，约 2.2s/it，预计还需 ~40 分钟完成。

---
