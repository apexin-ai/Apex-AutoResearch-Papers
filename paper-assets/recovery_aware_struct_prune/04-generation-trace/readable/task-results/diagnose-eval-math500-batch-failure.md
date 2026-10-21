# diagnose eval math500 batch failure

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_math500_batch_failure_20260521T134102_result.json`
- **Structured JSON:** [`f64d7dfa1b72d960de26.json`](../../sessions/f6/f64d7dfa1b72d960de26.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断报告已写入 memory.md。

**总结**：3 个 MATH-500 eval 被外部 SIGTERM 主动终止，不是 OOM/磁盘/脚本问题。grpo_cka_only_25 和 sft_cka_only_25 已被重启为 _v2（加了 `--max_new_tokens 2048`），正在 GPU 0/2 上运行。**grpo_random_20 未被重启，GPU 1 空闲**，需手动处理。数据盘 99% 满需关注。

---
