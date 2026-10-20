# eval humaneval sft rasp 2048

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_humaneval_sft_rasp_2048_20260519T154552_result.json`
- **Structured JSON:** [`d89d4440115794e60538.json`](../../sessions/d8/d89d4440115794e60538.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

这个实验 **已经有结果了**。Registry 显示 `eval_humaneval_sft_rasp_20_2048_v2` 之前已完成：

| 指标 | 值 |
|------|-----|
| pass@1 | **10.37%** (17/164) |
| stderr | 0.0238 |
| avg_response_length | 1253.7 |
| median_response_length | 2048 (命中上限) |

之前在 cuda:1 上跑完的。我刚又在 cuda:0 上启动了一个重复进程（PID 117053），需要杀掉吗？

结果汇总对比：

| 方法 | HumanEval @2048 |
|------|----------------|
| CKA-only SFT | 20.12% (33/164) |
| CKA-only GRPO | 20.12% (33/164) |
| Standard SFT | ~16.25% (interim) |
| **RASP SFT** | **10.37% (17/164)** |
| Standard GRPO | 10.98% (18/164) |
| RASP GRPO | 10.98% (18/164) |

RASP SFT (10.37%) ≈ RASP GRPO (10.98%)，支持 redistribution-not-expansion 假设在 RASP 上也成立。

---
