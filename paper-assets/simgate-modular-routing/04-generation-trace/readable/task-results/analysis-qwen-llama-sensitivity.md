# analysis qwen llama sensitivity

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_qwen-llama-sensitivity_20260521T005220_result.json`
- **Structured JSON:** [`95be8ed93bd46dbb3575.json`](../../sessions/95/95be8ed93bd46dbb3575.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果（跳过了 plan_c 中 freeze/lifespan-longest-lived/measure-melting-point 尾部附加的 `deep_internal` 格式行，不影响计算）：

```
=== SENSITIVITY ANALYSIS (excl. find-non-living-thing, 10 tasks) ===
Model             Int DR    Det DR    DDR       DAF [95% CI]
Qwen2.5-7B        51.2%     19.5%     +31.7pp   100.0% [100.0, 100.0]
Llama-3.1-8B      45.5%     12.5%     +33.0pp    97.0% [91.3, 100.0]
Gemma-2-9B        40.0%     15.5%     +24.5pp    99.9% [99.7, 100.0]
```

关键发现：
- **三个模型排除 find-non-living-thing 后 DAF 全部 ≥97%**，说明 deterministic 的优势几乎完全来自死亡避免
- Qwen Δ\_nd = 0.00（非死亡 episodes 中 internal 与 deterministic 得分完全持平），DAF 达到理论上限 100.0%
- Llama DAF 97.0% 稍低，Δ\_nd = 1.03 说明有少量非死亡 episodes 中 deterministic 仍略优，但置信区间上界触 100.0%
- Gemma 此前已知 99.9%，三模型一致性很强

---
