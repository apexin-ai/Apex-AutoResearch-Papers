# eval cluster bootstrap w4

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_cluster-bootstrap-w4_20260516T200409_result.json`
- **Structured JSON:** [`ae2eb2103af7a79c033e.json`](../../sessions/ae/ae2eb2103af7a79c033e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

```
=== Cluster Bootstrap DAF CI ===

Point estimate (all-episodes DAF): 0.9041

Episode-level bootstrap (previous):
  95% CI: [0.8160, 0.9876] (N=245 episodes, B=10000)
  Width: 0.1716

Cluster bootstrap (task-type level):
  95% CI: [0.7332, 1.0000] (K=11 clusters, B=10000)
  Width: 0.2668

CI widening: +0.0828 lower, +0.0124 upper
Width change: +0.0952 (+55.5%)
Mean bootstrap DAF: 0.9105 (std: 0.0819)
```

Cluster bootstrap CI 比 episode-level 宽 55.5%（符合预期，因为只有 11 个 cluster 可 resample），但下界仍为 0.733，远高于 0.5。DAF 在 non-i.i.d. 假设下依然有意义。

脚本和结果已保存到 `guided_router/cluster_bootstrap.py` 和 `guided_router/cluster_bootstrap_results.json`。

---
