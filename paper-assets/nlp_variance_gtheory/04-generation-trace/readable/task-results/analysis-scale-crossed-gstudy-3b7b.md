# analysis scale crossed gstudy 3b7b

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_scale_crossed_gstudy_3b7b_20260522T113637_result.json`
- **Structured JSON:** [`c0716f9bdff312f56167.json`](../../sessions/c0/c0716f9bdff312f56167.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 3B+7B Crossed G-study 结果

**Design**: 2-model (Qwen2.5-3B/7B), 6 facets, 115,200 records, fully balanced

### 方差分解 (Henderson I, adjusted)

| Component | Estimate | Pct |
|---|---|---|
| **item_id** | 0.0899 | **43.53%** |
| **model:item_id** | 0.0655 | **31.74%** |
| residual | 0.0329 | 15.93% |
| prompt_template:item_id | 0.0108 | 5.25% |
| ordering:item_id | 0.0025 | 1.23% |
| seed:item_id | 0.0017 | 0.84% |
| temperature:item_id | 0.0014 | 0.69% |
| model | 0.0014 | 0.69% |
| 其余 11 个 | ≈0 | <0.1% |

### G 系数

- **G_item = 0.7125** (8-model ref: 0.896)
- item_related_pct = **83.28%** (8-model ref: 68.09%)
- sigma_tau = 0.0899, sigma_delta = 0.0363

### Delta 分解

| Source | Contribution to delta | % of delta |
|---|---|---|
| model:item_id | 0.0328 | **90.3%** |
| prompt_template:item_id | 0.0018 | 5.0% |
| temperature:item_id | 0.0007 | 2.0% |
| ordering:item_id | 0.0006 | 1.8% |
| seed:item_id | 0.0003 | 0.8% |
| residual | 0.0001 | 0.2% |

### D-study curve

| n_items | G |
|---|---|
| 25 | 0.236 |
| 50 | 0.383 |
| 100 | 0.553 |
| **200** | **0.712** |
| 500 | 0.861 |

### 关键发现

1. **item_id = 43.5%** — 符合预期 (>30%)，但低于单模型的 73-75%，因为 model:item_id 吸收了大量方差
2. **model:item_id = 31.7%** — 最大的交互效应，说明 3B 和 7B 在 item 难度排序上存在显著差异
3. **G_item = 0.71** — 低于 8-model reference (0.90)，因为只有 2 个模型时 model:item 交互的 delta 无法被充分平均掉（delta 的 90.3% 来自 model:item_id / n_model=2）
4. **item_related 总计 83.3%** — 高于 8-model 的 68.1%，说明 within-family 设计中 item 特性主导方差

JSON 已保存到 `artifacts/exp004/data/exp003_scale_crossed_gstudy_3b7b.json`。

---
