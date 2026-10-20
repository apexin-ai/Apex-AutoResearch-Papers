# ops step50 eval collect

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_step50-eval-collect_20260515T223239_result.json`
- **Structured JSON:** [`d0123bf80e44a5ffdeb1.json`](../../sessions/d0/d0123bf80e44a5ffdeb1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。

## GRPO Standard v8 Step-50 Checkpoint Eval (N=1319, westd)

| Metric | Value |
|--------|-------|
| Accuracy | **58.91%** ±1.35% |
| N | 777/1319 |
| EOS Rate | 98.10% |
| Avg Len | 222.1 |
| Truncated | 25/1319 |
| vs SFT baseline | **Δ = -0.38pp** |

**结论: negative。** GRPO step-50 checkpoint (58.91%) 略低于 SFT baseline (59.29%)，差值 -0.38pp 在统计误差范围内（stderr ±1.35%）。Standard GRPO 在 step 50 没有带来显著的 accuracy recovery，尽管中间进度报告（300/1319 时 acc=62%）曾显示积极信号，最终结果回归均值。

---
