# diagnose eval pi05 attention k05 long seed42 v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_pi05_attention_k05_long_seed42_v2_20260526T143928_result.json`
- **Structured JSON:** [`23eb993939648afe89e5.json`](../../sessions/23/23eb993939648afe89e5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
RESULT: success
SR: 49.8%
DETAILS: 10/10 tasks completed (249/500 episodes), 249min runtime.
  Per-task: T0=74%, T1=46%, T2=60%, T3=70%, T4=46%, T5=52%, T6=10%, T7=54%, T8=18%, T9=68%
  v2 结果 (49.8%) 与 v1 (49.4%) 高度一致，确认 attention k=0.5 Long 的可复现性。
  对比: k=0.9=63.8%, k=0.75=52.4%, k=0.5=49.8% — 从 k=0.75→0.5 仅下降 2.6pp，cliff 不明显。
```

---
