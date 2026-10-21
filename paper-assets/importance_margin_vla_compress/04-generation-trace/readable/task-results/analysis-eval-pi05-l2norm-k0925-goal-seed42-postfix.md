# analysis eval pi05 l2norm k0925 goal seed42 postfix

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_pi05_l2norm_k0925_goal_seed42_postfix_20260525T120353_result.json`
- **Structured JSON:** [`9fd2fc36ac9d5858da1f.json`](../../sessions/9f/9fd2fc36ac9d5858da1f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

**总结：**

| 配置 | Goal SR |
|------|---------|
| π0.5 Baseline (no pruning) | ~88% |
| L2norm k=0.85 | 87.4% |
| **L2norm k=0.925** | **89.8%** |
| Random k=0.925 | 70.0% |

L2norm k=0.925 在 cliff zone 取得 89.8%，甚至略超 baseline，而 Random 同比例下降 18pp 至 70%。**Importance margin 在 cliff zone 强确认**：基于重要性的 pruning 在 random pruning 崩溃的区间仍能维持全性能。

---
