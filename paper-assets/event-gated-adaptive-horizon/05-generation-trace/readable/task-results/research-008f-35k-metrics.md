# research 008f 35k metrics

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_008f_35k_metrics_20260514T062046_result.json`
- **Structured JSON:** [`99d1554ae3eb3d381024.json`](../../sessions/99/99d1554ae3eb3d381024.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据齐全，计算结果：

```
=== exp_008f (no_dt_embed) 关键指标 ===

008f@25K: eval=196.78, value=17.51, v/e=8.90%, normalized=1.02x
008f@35K: eval=206.67, value=36.28, v/e=17.56%, normalized=0.73x

对比 008d@35K: v/e=41.2%, normalized=1.71x

结论: ✅ C2 CONFIRMED
```

**分析**:
- 008f@25K v/e=8.90% vs baseline 8.7% → 几乎与 baseline 持平 (1.02x)
- 008f@35K v/e=17.56% vs baseline 24.1% → **低于 baseline** (0.73x)
- 对比 008d@35K 的 1.71x → 008f 直接从 1.71x 降到 0.73x，**差距 2.3 倍**

去掉 dt_embedding conditioning 后，value overestimation 不仅没有恶化，反而**被抑制到 baseline 以下**。dt_embedding 是 value 崩塌的因果根因确认。

**Loss 趋势**:

| Step | model_loss | actor_loss | value_loss |
|------|-----------|------------|------------|
| 5K   | 21.05     | -0.109     | 9.33       |
| 15K  | 7.46      | (截断)      | (截断)      |
| 25K  | 5.09      | -0.195     | 1.47       |
| 35K  | 4.60      | -0.075     | 1.10       |

model_loss 和 value_loss 持续健康下降，actor_loss 稳定。没有任何发散迹象。

**额外观察**: gate_dt 全程锁定在 dt=2 (gate_dt_2_frac=1.0)，gate 尚未激活多步跳转——这是 no_dt_embed 下的预期行为。

---
