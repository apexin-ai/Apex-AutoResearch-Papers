# eval plan 008 v4 1 7b seed44 45 nothinking

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_plan-008-v4-1_7b-seed44-45-nothinking_20260515T222045_result.json`
- **Structured JSON:** [`0e634915a581a8f82cf7.json`](../../sessions/0e/0e634915a581a8f82cf7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== 1.7B seed 44, 45 generation-based nothinking eval ===
Seed 44: balanced_acc=0.6833, internal_recall=0.8333
Seed 45: balanced_acc=0.6037, internal_recall=0.8000

=== 完整 4-seed 三模型对比（统一 generation-based nothinking eval）===
| Model | s42 | s43 | s44 | s45 | Mean±Std |
|-------|-----|-----|-----|-----|----------|
| 0.6B  | 0.6241 | 0.5574 | 0.6907 | 0.7333 | 0.6514±0.0771 |
| 1.7B  | 0.3759 | 0.4574 | 0.6833 | 0.6037 | 0.5301±0.1390 |
| 4B    | 0.6241 | 0.5463 | 0.6556 | 0.7000 | 0.6315±0.0648 |
```

1.7B 的 mean 最低（0.5301），且 seed 间方差最大（std=0.1390，远高于 0.6B 的 0.0771 和 4B 的 0.0648）。seed 42/43 表现很差（0.37/0.46），seed 44/45 则接近 0.6B/4B 水平（0.68/0.60），说明 1.7B 在 nothinking 模式下训练稳定性较差。

---
