# research 008e v3 metrics

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_008e_v3_metrics_20260514T062054_result.json`
- **Structured JSON:** [`160c7b9b93b6ddf5c81a.json`](../../sessions/16/160c7b9b93b6ddf5c81a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
008e_v3@25K: eval=155.7, value=26.19, train=176.5, loss=5.31, v/e=16.8%, normalized=1.93x
008e_v3@35K: eval=276.5, value=62.76, train=291.3, loss=5.03, v/e=22.7%, normalized=0.94x
008e_v3@45K: eval=382.2, value=110.67, train=381.0, loss=4.96, v/e=29.0%, normalized=0.87x
对比 008a@45K: eval=563, v/e=需查
对比 baseline@45K: eval=443, v/e=33.1%
```

**Gate 状态**: 三个 checkpoint 均 gate_dt_mean=1.0, gate_dt_1_frac=1.0。符合预期（gate_fixed_dt=1）。

**分析**:
- 25K 时 v/e=16.8% 远高于 baseline 的 8.7%（1.93x），说明 value 早期增长正常甚至偏快
- 35K 时开始下降到 baseline 水平（0.94x）
- 45K 时 v/e=29.0% 低于 baseline 33.1%（0.87x），出现轻度 value growth suppression（~13%）
- eval_return=382 也低于 baseline 的 443（86%），说明 subsample ON + dt=1 imagination 对整体性能有负面影响
- 与 008a（eval=563）相比，008e_v3 的 eval 明显更低，说明 subsample 对 eval 性能有较大负面影响，但 008a 的 dt=2 imagination 可能补偿了这一点

**结论**: subsample ON + dt=1 imagination 确实出现了轻度 value growth suppression（45K 时 normalized=0.87x），但幅度不如预期大。eval 性能下降更显著（382 vs baseline 443），暗示 subsample 本身对数据质量/效率有负面影响，不仅仅是 value 抑制。

---
