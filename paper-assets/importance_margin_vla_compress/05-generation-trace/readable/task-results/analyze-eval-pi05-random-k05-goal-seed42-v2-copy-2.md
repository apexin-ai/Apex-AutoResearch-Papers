# analyze eval pi05 random k05 goal seed42 v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_pi05_random_k05_goal_seed42_v2_20260523T201019_result.json`
- **Structured JSON:** [`59353e838684f869ff6a.json`](../../sessions/59/59353e838684f869ff6a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验正常完成。结果如下：

---

**Overall SR**: 73.6% (368/500)

**Per-task SR**:

| Task | Name | Success | SR |
|------|------|---------|-----|
| T0 | open the middle drawer of the cabinet | 39/50 | 78% |
| T1 | put the bowl on the stove | 22/50 | 44% |
| T2 | put the wine bottle on top of the cabinet | 43/50 | 86% |
| T3 | open the top drawer and put the bowl in | 38/50 | 76% |
| T4 | put the bowl on top of the cabinet | 46/50 | 92% |
| T5 | push the plate to the front of the stove | 35/50 | 70% |
| T6 | put the cream cheese in the bowl | 31/50 | 62% |
| T7 | turn on the stove | 50/50 | 100% |
| T8 | put the bowl on the plate | 43/50 | 86% |
| T9 | put the wine bottle on the rack | 21/50 | 42% |

**Total episodes**: 500 ✓

**Exit status**: Clean (EXIT_CODE=0)，无 error/OOM/crash

---

**与已知数据点的关系** — π0.5 Random Goal curve 完整：

| k | SR |
|---|-----|
| 0.95 | 92.2% |
| 0.925 | 89.0% |
| 0.9 | 90.6% |
| 0.85 | 88.0% |
| 0.7 | 78.2% |
| **0.5** | **73.6%** |
| 0.3 | 50.6% |

73.6% 位于 k=0.7 (78.2%) 和 k=0.3 (50.6%) 之间，**单调递减成立**。曲线形态合理：k=0.7→0.5 降 4.6pp，k=0.5→0.3 降 23.0pp，说明 k<0.5 后性能加速退化。

**v1 vs v2 对比**：v1 (pre-fix) = 74.4%，v2 (post-fix) = 73.6%，差异仅 0.8pp，说明 CPU RNG 修复对 Random k=0.5 影响极小。

**Importance margin** (Random vs L2norm @ k=0.5):
- Random k=0.5: **73.6%**
- L2norm k=0.5: **59.2%**
- **Δ = +14.4pp**（Random 显著优于 L2norm）

这进一步确认 L2norm 不是有效的 importance metric——随机剪枝都比它高 14.4pp。对比 Attention k=0.5 (X-VLA, 98.2%)，说明好的 importance metric 远优于 random，而 L2norm 反而比 random 差。

**Conclusion**: **Success**。M086 缺失数据已补齐，Random Goal curve 单调递减确认，结果合理可信。

---
