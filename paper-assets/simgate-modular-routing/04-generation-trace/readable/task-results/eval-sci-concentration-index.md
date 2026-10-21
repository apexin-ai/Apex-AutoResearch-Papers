# eval sci concentration index

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_sci-concentration-index_20260516T175721_result.json`
- **Structured JSON:** [`400048e2054d981d6310.json`](../../sessions/40/400048e2054d981d6310.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Artifact 注册遇到类型问题，但结果已保存在服务器端 `guided_router/sci_results.json` 且 registry 已更新为 DONE。

---

```
=== Signal Concentration Index Results ===
SCI (Gini): 0.2147
Top-1 CR: 14.3% (identify-life-stages-1)
Top-2 CR: 27.5%
Top-3 CR: 39.8%

Per-task signal contributions:
  identify-life-stages-1                       : 14.3% (n=20, Δ_full=47.50, Δ_nd=0.00, death_rate_int=55%)
  lifespan-longest-lived                       : 13.2% (n=25, Δ_full=44.00, Δ_nd=0.00, death_rate_int=56%)
  lifespan-longest-lived-then-shortest-lived   : 12.3% (n=20, Δ_full=40.80, Δ_nd=0.00, death_rate_int=45%)
  inclined-plane-determine-angle               : 10.8% (n=20, Δ_full=36.00, Δ_nd=0.00, death_rate_int=55%)
  freeze                                       :  9.2% (n=20, Δ_full=30.50, Δ_nd=0.00, death_rate_int=55%)
  measure-melting-point-unknown-substance       :  9.0% (n=20, Δ_full=30.05, Δ_nd=0.00, death_rate_int=55%)
  identify-life-stages-2                       :  9.0% (n=20, Δ_full=30.00, Δ_nd=0.00, death_rate_int=50%)
  find-animal                                  :  8.0% (n=20, Δ_full=26.65, Δ_nd=0.00, death_rate_int=50%)
  grow-fruit                                   :  7.6% (n=20, Δ_full=25.10, Δ_nd=0.00, death_rate_int=45%)
  chemistry-mix                                :  6.6% (n=20, Δ_full=21.80, Δ_nd=0.00, death_rate_int=45%)
  find-non-living-thing                        :  0.0% (n=40, Δ_full=9.58, Δ_nd=9.58, death_rate_int=0%)
```

**关键发现：** SCI Gini = 0.2147，远低于假设的 ~1.0。Death-avoidance routing signal **不是**集中在少数 task types，而是广泛分布在 10/11 个 task 上（只有 find-non-living-thing 因 0% death rate 无贡献）。这意味着 death avoidance 是系统性现象而非局部特征——router 无法通过 task type 简单区分何时需要 deterministic policy。

---
