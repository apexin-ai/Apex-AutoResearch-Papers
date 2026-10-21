# eval cross model guided router

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_cross-model-guided-router_20260516T152424_result.json`
- **Structured JSON:** [`beab220320886be81b49.json`](../../sessions/be/beab220320886be81b49.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。

```
=== Cross-Model Guided Router Results (Qwen→Llama) ===

Overall:
  Balanced accuracy: 100.00%
  Det recall: 100.0%
  Internal recall: 0.0% (n=0 int-preferred episodes)
  Active classes: 1 / 2
  Episodes evaluated: 24 / 70 (rest are no-preference)

Per-task breakdown:
  chemistry-mix                          route=deterministic  det=2  int=0  tie=8
  freeze                                 route=deterministic  det=3  int=0  tie=7
  grow-fruit                             route=deterministic  det=5  int=0  tie=5
  identify-life-stages-1                 route=deterministic  det=2  int=0  tie=8
  inclined-plane-determine-angle         route=deterministic  det=6  int=0  tie=4
  lifespan-longest-lived                 route=deterministic  det=4  int=0  tie=6
  measure-melting-point-unknown-substance route=deterministic  det=2  int=0  tie=8

Comparison:
  Qwen in-sample:            62.92%
  Qwen LOTO:                 62.92%
  Cross-model (Qwen→Llama):  100.00%

⚠ DEGENERATE CASE
```

**关键发现：** 这是一个退化评估。Llama 数据中 0 个 int-preferred episode（7 个 task 全都是 det-preferred 或 no-preference），Qwen 规则把所有 task 都 route 到 deterministic → 不可能出错。100% 反映的是 trivial correctness，不是真正的跨模型迁移判别力。

实质意义：Llama-3.1-8B 在这些 task 上表现出和 Qwen 相同的模式——internal mode 经常死亡，deterministic 从不劣于 internal。死亡风险是跨模型的 task-level 属性，但评估需要包含 `find-non-living-thing` 等 safe task 才能真正测试路由判别力。

---
