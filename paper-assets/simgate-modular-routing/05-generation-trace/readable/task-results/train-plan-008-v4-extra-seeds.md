# train plan 008 v4 extra seeds

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_plan-008-v4-extra-seeds_20260515T215949_result.json`
- **Structured JSON:** [`806b4adc40d61562fa61.json`](../../sessions/80/806b4adc40d61562fa61.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== 训练完成 ===
0.6B seed44: eval_loss=0.3117, checkpoint=checkpoints/plan-008-v4-0_6b-seed44/
0.6B seed45: eval_loss=0.2756, checkpoint=checkpoints/plan-008-v4-0_6b-seed45/
4B seed44: eval_loss=0.3050, checkpoint=checkpoints/plan-008-v4-4b-seed44/
4B seed45: eval_loss=0.2684, checkpoint=checkpoints/plan-008-v4-4b-seed45/

=== Generation-based eval (enable_thinking=False) ===
| Model | Seed 44 | Seed 45 | Mean (new 2 seeds) |
|-------|---------|---------|-------------------|
| 0.6B  | 0.6907  | 0.7333  | 0.7120 |
| 4B    | 0.6556  | 0.7000  | 0.6778 |

=== 4-seed 汇总（seed 42-45）===
| Model | s42    | s43    | s44    | s45    | Mean±Std |
|-------|--------|--------|--------|--------|----------|
| 0.6B  | 0.6241 | 0.5574 | 0.6907 | 0.7333 | 0.6514±0.0771 |
| 4B    | 0.6241 | 0.5463 | 0.6556 | 0.7000 | 0.6315±0.0648 |
```

---
