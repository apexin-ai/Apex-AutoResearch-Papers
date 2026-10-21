# monitor 016e 009d metrics

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_016e_009d_metrics_20260515T221733_result.json`
- **Structured JSON:** [`49fb046a04a267b3ad52.json`](../../sessions/49/49fb046a04a267b3ad52.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
016e: step=95K/105K, eval=31.7@95K (peak 326.7@75K), value/eval=658%, GPU=14% — CRITICAL ⚠️
     崩溃确认：75K→95K eval从327跌至32，训练return也崩至28-75。Gate完全冻结(dt=2, entropy=0)。
     好消息：video deadlock修复成功（过了5K没hang）。坏消息：性能层面完全崩溃，极端CIVO。

009d: step=228K/500K, eval=638.2@218K, value/eval=72%, fps=7.4 — HEALTHY ✓
     持续上升中，218K创新高638。预计~19h完成500K。
```

**016e 诊断**：这不是 deadlock 问题（修好了），而是 SGS 方法本身在 walker 上不稳定。Gate 完全冻结在 dt=2（zero entropy）说明 gate 没有学到有意义的 temporal selection。75K 时 eval 达峰 327 后急速崩溃到 32，伴随极端 value overestimation（value 209 vs actual return 32）。实验还剩 ~10K steps 就自动结束，可以让它跑完但结论已明确：SGS with fixed-dt2 gate 在 walker 上 failed。

---
