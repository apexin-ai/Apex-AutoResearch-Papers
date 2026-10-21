# eval loto guided router

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_loto-guided-router_20260516T150433_result.json`
- **Structured JSON:** [`7ad064acf28f5b6b3851.json`](../../sessions/7a/7ad064acf28f5b6b3851.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

LOTO 评估完成。

```
=== LOTO Guided Router Results ===

| Strategy             | Fold-mean bal_acc | Episode-level bal_acc | Delta vs in-sample |
|----------------------|-------------------|-----------------------|--------------------|
| prior_majority       | 77.3% (±24.9%)    | 50.00%                | -12.9 pp           |
| prior_mean_threshold | 77.3% (±24.9%)    | 50.00%                | -12.9 pp           |
| learned              | 77.3% (±24.9%)    | 62.92%                |  0.0 pp            |

Per-fold (learned):
  chemistry-mix                                  50.0%  route=deterministic
  find-animal                                   100.0%  route=deterministic
  find-non-living-thing                          50.0%  route=internal      ← 正确识别
  freeze                                        100.0%  route=deterministic
  grow-fruit                                     50.0%  route=deterministic
  identify-life-stages-1                        100.0%  route=deterministic
  identify-life-stages-2                        100.0%  route=deterministic
  inclined-plane-determine-angle                100.0%  route=deterministic
  lifespan-longest-lived                         50.0%  route=deterministic
  lifespan-longest-lived-then-shortest-lived     50.0%  route=deterministic
  measure-melting-point-unknown-substance       100.0%  route=deterministic
```

**结论**：learned variant 的字符串模式匹配在 LOTO 设置下完美泛化，episode-level balanced accuracy 与 in-sample oracle 完全一致（62.92%，0pp 损失）。Prior-based 策略因为无法识别唯一的 safe task（find-non-living-thing）而退化到 50%。

---
