# analyze eval pi05 random k085 goal seed42 v4

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_pi05_random_k085_goal_seed42_v4_20260523T203431_result.json`
- **Structured JSON:** [`b354af883fb4ccefaa20.json`](../../sessions/b3/b354af883fb4ccefaa20.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
overall_success_rate: 52.4%
per_task_rates:
  T0 open the middle drawer of the cabinet:       84%
  T1 put the bowl on the stove:                     2%
  T2 put the wine bottle on top of the cabinet:    22%
  T3 open the top drawer and put the bowl inside:  38%
  T4 put the bowl on top of the cabinet:           50%
  T5 push the plate to the front of the stove:     66%
  T6 put the cream cheese in the bowl:             82%
  T7 turn on the stove:                            88%
  T8 put the bowl on the plate:                    84%
  T9 put the wine bottle on the rack:               8%

conclusion: success
reasoning: v4(post-fix)=52.4% 与 v3(pre-fix)=52.4% 完全一致，说明 CPU RNG 修复对 random pruning 结果无影响。k=0.85 在 cliff zone 的结论稳定可复现。数据点完整（500 episodes），可用于论文表格。对比：k=0.9=62.2% → k=0.85=52.4% 存在约10pp的骤降，确认 cliff zone 在 k∈[0.85, 0.9) 区间。

key_metrics:
  overall_sr: 0.524
  total_successes: 262
  total_episodes: 500
  elapsed_min: 133.2
  per_task_sr: {T0: 0.84, T1: 0.02, T2: 0.22, T3: 0.38, T4: 0.50, T5: 0.66, T6: 0.82, T7: 0.88, T8: 0.84, T9: 0.08}
```

---
