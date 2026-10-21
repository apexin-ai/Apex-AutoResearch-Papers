# ops harvest grpo standard v2 and westb progress

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_harvest_grpo_standard_v2_and_westb_progress_20260519T013822_result.json`
- **Structured JSON:** [`aef8501ade8c7a2dcc59.json`](../../sessions/ae/aef8501ade8c7a2dcc59.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### Part 1: westd-29022 — eval_math500_grpo_standard_20_fair_v2 ✅ 完成

| 指标 | 值 |
|---|---|
| **Accuracy** | **26.4%** (132/500) |
| stderr | ±1.97% |
| natural_eos_pct | 55.6% |
| truncated | 222/500 |
| avg_response_length | 1127.8 tokens |

Registry 已更新为 DONE/success。westd cuda:1 已释放（0% util, 0 MiB）。

### Part 2: westb-23072 — 1.5B eval 进度

| 实验 | GPU | 进度 | 当前 acc |
|---|---|---|---|
| eval_gsm8k_sft_standard_20_1p5b | cuda:1 | **650/1319 (49%)** | 23.38% |
| eval_gsm8k_sft_rasp_20_1p5b | cuda:0 | **839/1319 (64%)** | 28.88% (@ 800) |

两个 eval 都在正常跑，GPU 利用率 98%。按当前速度预计还需 ~1.5-2 小时。

---
