# ops westb cleanup and qwen phase1

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westb_cleanup_and_qwen_phase1_20260520T050703_result.json`
- **Structured JSON:** [`4b0881a22fa956a67812.json`](../../sessions/4b/4b0881a22fa956a67812.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

当前状态汇总：

**Part 1 完成** — 释放 66 GB（13G → 79G 可用）

**Part 2 进行中** — Qwen2.5-Math-7B Phase 1：
- CKA scores + importance scores: 已完成
- CKA-only pruning @20%: 已完成 (actual 18.99%)
- Standard pruning @20%: 已完成 (actual 19.18%)
- GSM8K eval (N=200): 两个 eval 在 westb-23072 并行运行中
  - Standard: ~44/200, ETA ~17 min
  - CKA-only: ~25/200, ETA ~38 min

等待中，4.5 分钟后自动检查。

---
