# launch eval gsm8k sft alpha3p0 westd2

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_launch_eval_gsm8k_sft_alpha3p0_westd2_20260522T102447_result.json`
- **Structured JSON:** [`e18dac86cd5e706f18c0.json`](../../sessions/e1/e18dac86cd5e706f18c0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Checkpoint 不在 westd，需要在 westb 上跑。**

`sft_rasp_alpha3p0_20` 目录在 westd-32935 上完全不存在（目录本身和 find 搜索均无结果）。checkpoint-935 应该仍在 westb-23072 上。

GPU 2 和 3 在 westd 上是空闲的，如果需要可以先把 checkpoint 从 westb 同步过来再跑，或者直接在 westb 上执行 eval。请指示。

---
