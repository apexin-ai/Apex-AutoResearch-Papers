# analysis per benchmark dstudy non mmlu

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_per_benchmark_dstudy_non_mmlu_20260522T024329_result.json`
- **Structured JSON:** [`81cc13c3b51dbe4fb603.json`](../../sessions/81/81cc13c3b51dbe4fb603.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### D-Study 结果 (n_G80: items needed for G ≥ 0.80)

| Benchmark | Multi (2304 cond.) | Partial (4 cond.) | Single (1 cond.) | Ratio S/M |
|-----------|-------------------:|------------------:|-----------------:|----------:|
| ARC       | **98**             | 816               | 1,078            | 11.0×     |
| HellaSwag | **118**            | 1,000             | 1,403            | 11.9×     |
| GSM8K     | **128**            | 1,270             | 2,768            | 21.6×     |
| MATH      | **101**            | 1,014             | 2,160            | 21.4×     |

### G at 200 items (actual study size)

| Benchmark | Multi  | Partial | Single |
|-----------|-------:|--------:|-------:|
| ARC       | 0.892  | 0.495   | 0.426  |
| HellaSwag | 0.872  | 0.445   | 0.363  |
| GSM8K     | 0.863  | 0.387   | 0.224  |
| MATH      | 0.888  | 0.441   | 0.270  |

### Three_in_one 验证

| Benchmark | 本次 (8-model) | Three_in_one | 匹配 |
|-----------|-------------:|-----------:|------|
| ARC       | 98           | 98         | **match** |
| HellaSwag | 118          | 171        | **mismatch** — three_in_one 用 6 models (OLMo/Yi 缺失), σ²_δ 更大 |
| GSM8K     | 128          | 128        | **match** |
| MATH      | 101          | 101        | **match** |

HellaSwag 不一致原因：three_in_one 当时只有 6 个模型的 HellaSwag 数据 (n_model=6, σ²_δ=0.01408)，本次独立分析使用完整 8-model G-study (n_model=8, σ²_δ=0.01039)。**8-model 的 118 是正确值，应替换论文中的 171。**

所有 12 个 D-study 曲线通过单调性检查。Multi-facet 曲线与原始 G-study JSON 完全吻合 (max_diff = 0)。

产出文件已写入服务器 (`results/exp004_8model_analysis/dstudy_{benchmark}.json`) 和本地 (`artifacts/exp004/data/dstudy_{benchmark}.json`)。

---
