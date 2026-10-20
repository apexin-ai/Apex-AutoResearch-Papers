# analysis cross alpha comparison v2

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cross_alpha_comparison_v2_20260515T052844_result.json`
- **Structured JSON:** [`f1f7bec43bc46a331f3f.json`](../../sessions/f1/f1f7bec43bc46a331f3f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。总结关键发现：

### D024 回答

**1. 非单调 dose-response 确认**
α=0.50 的 diversity collapse 在所有 distinct_N 指标上弱于 α=0.25（d1: -36.6% vs -39.9%，d3: -51.0% vs -57.7%），即使匹配相同代数 (gen0-9)。

**2. 机制：不是"前期快后期饱和"，而是"完全不同的 collapse regime"**
- α=0.50 在 gen1 触发 entropy 崩塌（-22%）+ ECE 爆炸（6x），模型立即进入低熵/高miscalibration 状态
- 这个 regime shift 产生"地板效应"——模型从一开始就生成较同质的文本，diversity 进一步下降的空间有限
- α=0.50 全程 collapse 速率都低于 α=0.25，不是前快后慢

**3. Canary regime switch（核心发现）**

| α | entropy→d1 | ECE→d1 |
|---|---|---|
| 0.00 | p=0.048* | p=0.958 |
| 0.25 | p=0.012* | p=0.238 |
| 0.50 | p=0.105 | p=0.021* |

低 α 用 entropy 预警，高 α 用 ECE 预警。Cross-correlation 也确认 ECE 在 α=0.50 从"跟随者"变为"领先者"（lag=+1, r=-1.013）。

**4. 对论文的启示**：实用的 canary 系统应同时监控 entropy 和 ECE，并根据估计的污染强度调整权重。α=0.10/0.60/0.75 的数据将帮助精确定位 regime 切换边界（预计 α~0.3-0.4）。

产出已保存至 `results/analysis/` 和 artifact registry。Registry 已更新 a050_s42 的完整分析指标。

---
