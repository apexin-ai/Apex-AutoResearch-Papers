# ssh 72b data consolidation

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_72b-data-consolidation_20260519T115818_result.json`
- **Structured JSON:** [`5f1cec54b70899ac2910.json`](../../sessions/5f/5f1cec54b70899ac2910.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据验证完毕，reason 分布与 death counts 一致。现在输出完整结果。

```
=== 72B CONSOLIDATED METRICS ===
Data sources: westb-13313 (9 tasks, 175 eps) + westd-18266 (2 tasks, 80 eps)
Total: 11 tasks, 255 episodes

NOTE: westd-18266 的 2 个 task 各 40 eps（2 batches of 20），其余 task 20 eps（lifespan-longest-lived 15 eps）

=====================================
Aggregate (11 tasks, 255 eps)
=====================================
  Internal DR:  30.59% (78/255)
  Det DR:        2.75%  (7/255)
  Δ DR (72B):   27.84 pp

  Δ_full:       30.07  (mean det_score - int_score, all eps)
  Δ_nd:          2.28  (mean det_score - int_score, both-survive eps only)
  DAF:          92.42% (Death Attribution Fraction)

  n_both_survive: 174/255 (68.2%)

=====================================
Death-prone (excl find-non-living-thing)
=====================================
  N = 235
  Internal DR:  33.19% (78/235)
  Det DR:        2.98%  (7/235)

=====================================
Labels
=====================================
  det-preferred:  84  (32.9%)
  int-preferred:   0   (0.0%)
  no-preference: 171  (67.1%)

=====================================
Reason breakdown (255 eps)
=====================================
  tie:                    162  (63.5%)
  int_died_det_alive:      74  (29.0%)
  both_alive_det_wins:     10   (3.9%)
  both_died:                4   (1.6%)
  det_died_int_alive:       3   (1.2%)
  both_alive_int_wins:      2   (0.8%)

=====================================
Per-task breakdown
=====================================
Task                                   |  N | IntDR  | DetDR  | IntD | DetD | BothD | Δ_full |  Δ_nd  | n_nd
---------------------------------------|----| -------|--------|------|------|-------|--------|--------|-----
chemistry-mix                          | 20 | 50.0%  |  5.0%  |  10  |   1  |   1   |  46.10 |  0.00  |  10
find-animal                            | 20 | 40.0%  |  0.0%  |   8  |   0  |   0   |  40.40 |  0.00  |  12
find-non-living-thing                  | 20 |  0.0%  |  0.0%  |   0  |   0  |   0   |  20.00 | 20.00  |  20
freeze                                 | 20 | 45.0%  |  0.0%  |   9  |   0  |   0   |  45.00 |  0.00  |  11
grow-fruit                             | 20 | 40.0%  | 10.0%  |   8  |   2  |   1   |  30.00 |  0.00  |  11
identify-life-stages-1                 | 20 | 40.0%  |  0.0%  |   8  |   0  |   0   |  40.00 |  0.00  |  12
identify-life-stages-2                 | 20 | 30.0%  |  5.0%  |   6  |   1  |   0   |  24.80 | -0.31  |  13
inclined-plane-determine-angle         | 20 | 30.0%  |  5.0%  |   6  |   1  |   0   |  25.50 |  0.00  |  13
lifespan-longest-lived                 | 15 | 26.7%  |  0.0%  |   4  |   0  |   0   |  30.00 |  0.00  |  11
lifespan-longest-lived-then-s-s*       | 40 | 22.5%  |  2.5%  |   9  |   1  |   1   |  21.65 |  0.00  |  31
measure-melting-point-unknown-s*       | 40 | 25.0%  |  2.5%  |  10  |   1  |   1   |  22.90 |  0.03  |  30

* = data from westd-18266 (40 eps = 2 batches)

=====================================
Key observations
=====================================
- 72B internal routing DR=30.6% vs det DR=2.75%, gap 27.84 pp
- DAF=92.4%: 几乎全部 score gap 来自 death asymmetry
- 除 find-non-living-thing 外，当双方都存活时 Δ_nd ≈ 0（10/11 tasks）
- find-non-living-thing 是唯一 0% death rate 的 task，但 det 仍高 20 分（纯 score 差异，非 death 驱动）
- int-preferred = 0：72B 在所有 255 episodes 中 internal routing 从未被判定为更优
- chemistry-mix 和 freeze 死亡率最高（50%、45%）
```

---
