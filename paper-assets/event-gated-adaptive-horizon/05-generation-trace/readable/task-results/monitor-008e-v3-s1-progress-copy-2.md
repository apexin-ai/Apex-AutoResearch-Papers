# monitor 008e v3 s1 progress

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_008e_v3_s1_progress_20260514T190812_result.json`
- **Structured JSON:** [`5cff956f248f93d062dc.json`](../../sessions/5c/5cff956f248f93d062dc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
== 008e_v3_s1 ==
Current step: 8000 / 105K (7.6%)
Latest eval: 31.0 @ step 5K
value_mean: 0.0018 @ step 5K
Uptime: 19 min, pid 898127 alive
Status: 正常训练中（早期阶段，gate_dt 全部=1）

== 009a ==
Current step: 245K / 500K (49%)
Latest eval: 950.3 @ step 245K ← 新高（之前 225K=892, 215K=956）
value_mean: 663.8
v/e ratio: 69.9%
fps: 7.4
Uptime: 9h36m, pid 142508 alive
Status: 正常训练中，从 225K→245K 进展顺利

== GPU ==
cuda:0: 0% util, 4.2 GB / 95.6 GB (009a, 瞬时快照低利用)
cuda:1: 21% util, 4.2 GB / 95.6 GB (008e)
```

**备注**: 009a 的 eval_return 趋势良好：185K 起稳定在 850-950 区间，245K 达到 950.3（仅次于 215K 的 956）。按当前 fps≈7.4 估算，剩余 255K steps 约需 9.5h 完成。

---
