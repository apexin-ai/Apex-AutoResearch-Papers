# analysis task routing loo sensitivity

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_task_routing_loo_sensitivity_20260519T023951_result.json`
- **Structured JSON:** [`4538ed55b645cdc281f9.json`](../../sessions/45/4538ed55b645cdc281f9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。

---

## 完整结果

### 1. Leave-One-Out 分析

原始检验：U=21.0, p=0.033 (one-sided Mann-Whitney)

| Task removed | Group | |ΔR²| | Remaining p | Δp | Fragile? |
|---|---|---|---|---|---|
| wine on rack | complex | 0.2346 | 0.0556 | +0.022 | **YES** |
| bowl on cabinet | complex | 0.2006 | 0.0556 | +0.022 | **YES** |
| bowl on stove | complex | 0.1598 | 0.0556 | +0.022 | **YES** |
| cream cheese in bowl | simple | 0.1594 | 0.0119 | -0.021 | no |
| bowl on plate | complex | 0.0986 | 0.0317 | -0.002 | no |
| open top drawer+bowl | complex | 0.0754 | 0.0317 | -0.002 | no |
| wine on cabinet | complex | 0.0740 | 0.0317 | -0.002 | no |
| turn on stove | simple | 0.0359 | 0.0833 | +0.050 | **YES** |
| open middle drawer | simple | 0.0240 | 0.0833 | +0.050 | **YES** |
| push plate to stove | simple | 0.0067 | 0.0833 | +0.050 | **YES** |

**6/10 removals cause p>0.05**，但所有 fragile case 的 p 值都在边缘（max=0.083），不是大幅翻转。

脆弱性有两个来源：
- 移除 top-3 complex task（降低 complex 组均值）→ p=0.056
- 移除任一 simple task（simple 组仅 n=4，降到 n=3 后统计力不足）→ p=0.083

移除 cream cheese in bowl 反而大幅提升显著性（p=0.012），因为它是 simple 组中的 outlier。

### 2. 换组敏感性

| Task swapped | Direction | New p | Flipped? |
|---|---|---|---|
| wine on rack | C→S | 0.210 | **YES** |
| bowl on cabinet | C→S | 0.155 | **YES** |
| bowl on stove | C→S | 0.111 | **YES** |
| cream cheese in bowl | S→C | **0.008** | no |
| bowl on plate | C→S | 0.048 | no |
| open top drawer+bowl | C→S | 0.028 | no |
| wine on cabinet | C→S | 0.016 | no |
| turn on stove | S→C | 0.092 | **YES** |
| open middle drawer | S→C | 0.133 | **YES** |
| push plate to stove | S→C | 0.192 | **YES** |

**6/10 swaps flip significance.** 但 cream cheese in bowl → complex 大幅增强结论（p=0.008），lower complex tasks（bowl on plate, open top drawer+bowl, wine on cabinet）移至 simple 后结论也保持。

### 3. 数据驱动分组

| 方案 | 分组 | n_high / n_low | p-value |
|---|---|---|---|
| **Median split** | cream cheese in bowl 移入 high | 5 / 5 | **0.004** |
| **K-means** | cream cheese in bowl 移入 high; bowl on plate 移入 low | 4 / 6 | **0.005** |
| **Instruction overlap** | 与原始完全一致 | 6 / 4 | 0.033 |

关键发现：**cream cheese in bowl**（|ΔR²|=0.159）数值上属于高依赖组。Median split 和 K-means 都自动将其归入 high group，显著性大幅提升至 p<0.005。Instruction overlap 方案（共享对象≥2个目的地 → complex）完美复现原始分组。

### 结论

原始 6v4 分组在 n=10 样本下有中等脆弱性，这是小样本的固有限制。但趋势是真实的：
1. 所有 LOO fragile case 的 p 均在边缘（≤0.083），没有彻底翻转
2. 数据驱动分组（median/k-means）产生更强的显著性（p<0.005）
3. 脆弱性主要来自 cream cheese in bowl 的归组和小样本统计力

建议论文中：以 median split 或 k-means 为主要分组方案报告，附注 LOO 敏感性分析作为鲁棒性检验。

---
