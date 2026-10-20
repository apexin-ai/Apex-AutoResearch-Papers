# eval plan 008 v4 1 7b nothinking

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_plan-008-v4-1_7b-nothinking_20260515T212036_result.json`
- **Structured JSON:** [`a99dc4261bb870ca1b61.json`](../../sessions/a9/a99dc4261bb870ca1b61.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== 1.7B generation-based enable_thinking=False eval ===
Seed 42: balanced_acc=0.3759, internal_recall=0.4000
Seed 43: balanced_acc=0.4574, internal_recall=0.3000
Mean: balanced_acc=0.4167±0.0408

=== 真正统一 pipeline 三模型对比 ===
| Model | Seed 42 | Seed 43 | Mean±Std |
|-------|---------|---------|----------|
| 0.6B  | 0.6241  | 0.5574  | 0.5908±0.0472 |
| 1.7B  | 0.3759  | 0.4574  | 0.4167±0.0408 |
| 4B    | 0.6241  | 0.5463  | 0.5852±0.0550 |

=== 与旧 Trainer eval 对比 ===
Seed 42: Trainer=0.5761 → gen-based=0.3759 (Δ=-0.2002)
Seed 43: Trainer=0.4852 → gen-based=0.4574 (Δ=-0.0278)
```

1.7B 在 generation-based nothinking eval 下表现显著低于 0.6B 和 4B，也远低于其 Trainer logit-based 结果。从混淆矩阵看，seed 42 的 1.7B 模型将 175/270 的 deterministic 样本错误预测为 internal（pred_distribution: 187 internal vs 113 deterministic），说明该 checkpoint 在无 thinking 生成模式下严重偏向预测 "internal"。

用的 checkpoint：
- Seed 42: `checkpoints/plan-008-qwen3-1.7b/final_adapter`
- Seed 43: `checkpoints/seed-robustness-seed43/final_adapter`

---
