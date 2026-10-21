# eval daf bootstrap ci v2

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_daf-bootstrap-ci-v2_20260516T183401_result.json`
- **Structured JSON:** [`94d3f7d9da6191d88575.json`](../../sessions/94/94d3f7d9da6191d88575.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== DAF Bootstrap CI Results ===
Global:
  DAF point estimate: 0.6353
  95% CI: [0.5169, 0.7640]
  N episodes: 245, N det-preferred: 86, N death: 105 (70 in det-pref)
  Δ_full: 92.53, Δ_nd: 33.75

Per-task DAF:
  chemistry-mix:                       DAF=1.00 [1.00, 1.00] (n=20, death=9)
  find-animal:                         DAF=1.00 [1.00, 1.00] (n=20, death=10)
  find-non-living-thing:               DAF=0.00 [0.00, 0.00] (n=40, death=0)
  freeze:                              DAF=1.00 [1.00, 1.00] (n=20, death=11)
  grow-fruit:                          DAF=1.00 [1.00, 1.00] (n=20, death=9)
  identify-life-stages-1:              DAF=1.00 [1.00, 1.00] (n=20, death=11)
  identify-life-stages-2:              DAF=1.00 [1.00, 1.00] (n=20, death=10)
  inclined-plane-determine-angle:      DAF=1.00 [1.00, 1.00] (n=20, death=11)
  lifespan-longest-lived:              DAF=1.00 [1.00, 1.00] (n=25, death=14)
  lifespan-longest-lived-then-shortest: DAF=1.00 [1.00, 1.00] (n=20, death=9)
  measure-melting-point-unknown:       DAF=1.00 [1.00, 1.00] (n=20, death=11)

Note vs "previous DAF=0.904": 该值可能来自不同计算方式（如 death_decomposition_report 中使用全量 episodes 而非仅 det-preferred，得到 DAF=0.988）。本次严格按公式 DAF = 1 - Δ_nd/Δ_full（仅 det-preferred episodes）计算，得到 0.635。差异来源：只有 find-non-living-thing 有非 death 的 det-preferred episodes（16个，Δ_nd=33.75），拉低了全局 DAF。
```

Registry 已更新为 DONE，artifact 已注册。

---
