# fix cross model g tau

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_cross_model_g_tau_20260521T045422_result.json`
- **Structured JSON:** [`3661134d9faeae54c836.json`](../../sessions/36/3661134d9faeae54c836.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已计算完成。

## 汇报

### 1. G_item = 0.707
tau = σ²_item = 0.0768 (37.9%)，delta = 0.0318。Delta 的分解：
- **model×item: 83.2% of delta** — 绝对主导。不同模型对 item 难度的排序有显著差异
- precision×item: 7.4%
- prompt×item: 3.0%
- temperature×item: 2.8%
- seed×item: 2.6%
- ordering×item: 1.0%
- residual: 0.1%

### 2. G_condition = 0.073（与原值吻合）
tau = σ²_prec + σ²_temp + σ²_prec:temp = 0.000179，delta = 0.00228。条件效应微弱，被 item 和 model 的变异淹没。

### 3. 单模型 vs 跨模型对比

| 指标 | 单模型 | 跨模型 |
|------|--------|--------|
| ICC_item (σ²_item / σ²_total) | 0.611 | 0.379 |
| G_item (D-study, observed design) | 0.611* | 0.707 |

*单模型 G=0.611 实际上就是 ICC（σ²_item / σ²_total），不是 D-study G。

ICC 从 0.611 降到 0.379 的原因：model×item 交互（26.2%）从 item_id 的份额中"偷走"了方差。但 D-study 表明，即使存在这个交互，平均 2 个模型后 G_item = 0.707——item 难度排序在跨模型场景下仍然可靠。

### 4. D-study 趋势

| n_models | G_item |
|----------|--------|
| 1 | 0.568 |
| 2 | 0.707 |
| 3 | 0.770 |
| 5 | 0.828 |
| 10 | 0.879 |

增加模型数量对 G_item 提升显著（因为 model×item 是 delta 的 83%）。3 个模型即可达到 G > 0.75，5 个达到 0.83。

结果已保存至 `results/analysis/cross_model_g_coefficients.json`。

---
