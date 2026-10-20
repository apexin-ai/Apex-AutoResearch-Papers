# analysis verify dstudy design params

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_verify_dstudy_design_params_20260522T012230_result.json`
- **Structured JSON:** [`4146a3e3f8954d80d43d.json`](../../sessions/41/4146a3e3f8954d80d43d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论

### 设计参数确认

`single_condition_dstudy.json` 使用的是 **exp-001 单模型（Llama）设计**：

| 参数 | 值 |
|------|-----|
| 数据源 | `unified_henderson_i_numbers.json` → `single_model_6facet` |
| 记录数 | 259,200 |
| Facets | precision(3), temperature(3), prompt(6), seed(6), ordering(4) |
| Conditions | 1296 = 3×3×6×6×4 |
| τ (item) | 0.1271 |
| 方法 | Henderson I, negatives truncated |

### 判断：不需要 8-model 重算

当前设计**适用于论文上下文**。理由：

1. **论文的 Claim 3 问的是**："practitioner 用单一配置评估单一模型，需要多少 items？" — 这正是 exp-001 单模型 D-study 回答的问题。

2. **8-model 设计回答的是不同问题**：如果 model 作为 facet，`model:item_id`（30.2%）会成为误差项，σ²_δ 会远超 τ，G < 0.5 — 这说明的是"跨模型排名不一致"，不是"item count 效率"。

3. **ROADMAP 已确认**：`[TBD-RATIO]=10.0×` 已定稿，对应的就是 55 vs 552 items（单模型内的对比）。

4. **概念一致性**：precision 是单模型评估中合理的变异来源（practitioner 选 fp16 还是 bf16 确实影响结果），纳入 facet 是正确的。

### 唯一问题

文件放在 `exp004_8model_analysis/` 目录下但内容是 exp-001 数据 — 这是组织问题，不影响正确性。8-model G-study（`per_benchmark_gstudy_mmlu.json`）已独立回答跨模型方差分解问题。

**无需进一步计算。**

---
