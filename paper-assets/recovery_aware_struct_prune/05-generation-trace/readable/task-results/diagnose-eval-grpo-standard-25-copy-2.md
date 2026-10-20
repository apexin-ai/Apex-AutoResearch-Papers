# diagnose eval grpo standard 25

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_grpo_standard_25_20260516T213003_result.json`
- **Structured JSON:** [`2e6cd9f188123ace9e6e.json`](../../sessions/2e/2e6cd9f188123ace9e6e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**根本原因**: GRPO checkpoint 的 `config.json` 设置了 `"use_cache": false`（训练残留），`eval_gsm8k.py` 未覆盖该设置。导致 generate 时每步重算全序列 attention，极慢且最终 CUDA OOM 崩溃。

**修复**: 在 `eval_gsm8k.py` 的三处 `gen_kwargs` 中统一加入 `use_cache=True`。

**inference_speedup_plan016**: 日志文件不存在，实验可能从未启动。

---
