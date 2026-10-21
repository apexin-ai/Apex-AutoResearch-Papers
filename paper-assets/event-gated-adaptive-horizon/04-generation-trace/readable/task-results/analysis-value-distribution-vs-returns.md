# analysis value distribution vs returns

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_value-distribution-vs-returns_20260526T115424_result.json`
- **Structured JSON:** [`649e9ae7dc91b88137e5.json`](../../sessions/64/649e9ae7dc91b88137e5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇报

### 输出文件
- 图: `artifacts/value_vs_returns.pdf` + `.png`
- 数据: `artifacts/value_vs_returns.json`
- 脚本: `scripts/plot_value_vs_returns.py`

### 008d (collapsed) vs 008a (healthy) V(s) 校准对比

| 指标 | 008d (collapsed) | 008a (healthy) |
|------|-----------------|----------------|
| N samples | 4,460 | 4,460 |
| V(s) mean | 162.30 | 263.99 |
| G_t mean | 68.37 | 156.24 |
| **Bias mean** | **93.93** | **107.75** |
| Overest. rate | **92.7%** | 82.8% |
| **Correlation** | **-0.20** | **0.54** |
| V/G ratio | 7.36 | 5.18 |
| RMSE | 110.39 | 149.74 |

### 关键发现

**最重要的区分指标是 correlation，不是 bias magnitude。**

1. **008d (collapsed): correlation = -0.20** — critic 预测与实际 return 负相关。V(s) 不仅高估，而且完全失去了对状态价值相对排序的判断力。这是 CIVO 的核心病理：delusional critic 导致 actor 朝错误方向优化。

2. **008a (healthy): correlation = 0.54** — critic 虽然也有正向 bias（因为 train_eps 包含早期低回报 episode，而 V(s) 来自最终 checkpoint），但保持了正相关。Critic 仍能正确区分好状态和差状态。

3. **Scatter plot 形态差异**：
   - 008d: 点云集中在 y=x 线上方，呈水平带状（V(s) 几乎不随 G_t 变化）
   - 008a: 点云虽在 y=x 上方，但有清晰正斜率（V(s) 随 G_t 增大）

4. **Bias 分布**：008d 偏差集中在 +60~+120 区间（窄且偏移大）；008a 偏差分布更宽但包含负值区域（部分状态 V(s) < G_t）。

**注意**：两者 bias 都较大，部分原因是 train_eps 包含训练早期 episode（behavior policy 较差时的低 return），而 V(s) 来自最终 checkpoint。这不影响两者的相对对比。

---
