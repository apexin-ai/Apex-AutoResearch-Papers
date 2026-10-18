# analyze goal l2norm postfix batch

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_goal_l2norm_postfix_batch_20260524T111041_result.json`
- **Structured JSON:** [`ec715466c8120b3d0dd8.json`](../../sessions/ec/ec715466c8120b3d0dd8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新完毕。汇总：

## π0.5 L2norm Goal Post-fix 结果

| 实验 | keep ratio | tokens kept | overall SR | Δ vs baseline (88.4%) |
|------|-----------|-------------|------------|----------------------|
| k=0.9 | 90% | 230/256 | **88.6%** | +0.2% |
| k=0.7 | 70% | 179/256 | **70.2%** | -18.2% |
| k=0.5 | 50% | 128/256 | **59.8%** | -28.6% |

已知数据点：L2norm k=0.85 = 87.4%

L2norm Goal disruption curve: k=0.9 几乎无损（88.6% ≈ baseline 88.4%），k=0.85 轻微下降（87.4%），k=0.7 开始明显退化（70.2%），k=0.5 严重退化（59.8%）。cliff zone 在 k=0.85~0.7 之间。

值得注意：T9（put wine bottle on rack）在所有 keep ratio 下都是最弱 task（k=0.9: 38%, k=0.7: 44%, k=0.5: 48%），说明该 task 对 vision tokens 不敏感，性能瓶颈在其他方面。T1（put bowl on stove）在 k=0.5 时崩塌到 2%，是受 pruning 影响最大的 task。

---
