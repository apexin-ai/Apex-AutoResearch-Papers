# ops westd pull gsm8k results

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd-pull-gsm8k-results_20260519T222836_result.json`
- **Structured JSON:** [`4eacdee59a2a9e9ceb17.json`](../../sessions/4e/4eacdee59a2a9e9ceb17.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**cqa1 上所有 Qwen2.5-7B eval 目录都没有 gsm8k_results.json。** 所有 7B 目录（d000/d005/d025/d050/d100，s42/s123）只有 arc_challenge_results.json 和 mmlu_results.json，GSM8K eval 并未完成。

任务前提（"Qwen-7B s42 GSM8K d000+d100 eval 已完成"）与实际不符，无法传输不存在的文件。需要先在 cqa1 上跑 7B 的 GSM8K eval，才能拉取结果。

---
