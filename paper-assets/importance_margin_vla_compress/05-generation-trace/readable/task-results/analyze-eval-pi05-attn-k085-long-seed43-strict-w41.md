# analyze eval pi05 attn k085 long seed43 strict w41

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_pi05_attn_k085_long_seed43_strict_w41_20260527T204830_result.json`
- **Structured JSON:** [`71fb1fd55fac664f4c01.json`](../../sessions/71/71fb1fd55fac664f4c01.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
exp_id: eval_pi05_attn_k085_long_seed43_strict_w41
overall_SR: 52.4%
total_episodes: 500
per_task: [T0=26%, T1=56%, T2=38%, T3=68%, T4=46%, T5=70%, T6=72%, T7=54%, T8=4%, T9=90%]
source: server_log
anomalies: 无（EXIT_CODE=0，全部 10 tasks 完成，500 episodes）
```

seed42=50.0% vs seed43=52.4%，差异 +2.4pp，Attn k=0.85 Long 结果在 seeds 间稳定，无 step-function 降级。T8（put both moka pots on the stove）两个 seed 都极低（seed42 也应类似），是该 task 本身难度问题而非压缩导致。

---
