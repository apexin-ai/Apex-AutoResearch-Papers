# analyze eval pi05 l2norm k07 long seed43 strict w27

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_pi05_l2norm_k07_long_seed43_strict_w27_20260527T204834_result.json`
- **Structured JSON:** [`28df839a44ecbde60a8e.json`](../../sessions/28/28df839a44ecbde60a8e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已完成，EXIT_CODE=0。

```
exp_id: eval_pi05_l2norm_k07_long_seed43_strict_w27
overall_SR: 65.6%
total_episodes: 500 (10 tasks × 50 eps)
per_task: [T0=78%, T1=84%, T2=78%, T3=58%, T4=66%, T5=82%, T6=52%, T7=62%, T8=4%, T9=92%]
source: server_log
anomalies: 无
runtime: 166.5min (~2.8h)
```

与 seed42 对比：seed42=63.2%, seed43=65.6%, 差值+2.4pp。两个 seed 均值 **64.4%**。

T8（put both moka pots on the stove）仅 4%，是明显的弱项 task，两个 seed 一致偏低。

---
