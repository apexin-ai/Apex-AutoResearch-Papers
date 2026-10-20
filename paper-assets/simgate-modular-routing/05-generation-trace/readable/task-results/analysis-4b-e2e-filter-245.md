# analysis 4b e2e filter 245

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_4b-e2e-filter-245_20260517T042104_result.json`
- **Structured JSON:** [`682540e0a335e6e698f8.json`](../../sessions/68/682540e0a335e6e698f8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

```
=== 4B Router E2E (filtered to 245 episodes) ===
mean_score: -12.03
95% CI: [-17.82, -6.45]
death_rate: 0.1878
success_rate: 0.2327
sim_ratio: 0.0531
fallback_rate: 0.9469
n_episodes: 245
delta_vs_always_det: -2.56
delta_vs_1.7b: -1.33
```

4B router 在 245 episodes 上表现比全 275 episodes 时略差（-12.03 vs -10.72），比 always-det baseline 低 2.56 分，比 1.7B router 低 1.33 分。fallback_rate 极高（94.7%），sim_ratio 仅 5.3%——说明 4B router 几乎总是选择 deterministic path。

---
