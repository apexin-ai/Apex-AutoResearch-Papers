# analysis llama70b henderson

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_llama70b_henderson_20260523T185433_result.json`
- **Structured JSON:** [`6faf0afbe4e250cca1bf.json`](../../sessions/6f/6faf0afbe4e250cca1bf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果如下：

## 1. 方差分量表

| Component | σ² | % |
|---|---|---|
| item_id | 0.1125 | **74.51%** |
| residual | 0.0180 | 11.92% |
| seed:item_id | 0.0076 | 5.02% |
| prompt_template:item_id | 0.0064 | 4.24% |
| temperature:item_id | 0.0044 | 2.92% |
| ordering:item_id | 0.0020 | 1.33% |
| temperature:seed | 0.0001 | 0.05% |
| 其余所有 main effects 和 interactions | 0.0 | 0.0% |

## 2. G_item = **0.9566**

## 3. 与 Qwen2.5-72B 对比

| Metric | Llama-3.1-70B | Qwen2.5-72B |
|---|---|---|
| Grand mean | 0.8157 | 0.8703 |
| item_id % | **74.51%** | **83.25%** |
| G_item | **0.9566** | **0.9785** |

**Facet 排序差异**：
- Llama: item_id > residual > **seed:item_id** > prompt:item > temp:item > order:item
- Qwen: item_id > residual > **prompt:item** > order:item > seed:item > temp:item

Llama 的 seed:item_id 交互显著更大（5.02% vs Qwen 0.93%），说明 Llama-70B 对 random seed 更敏感。

## 4. 结论

G-theory 方差结构在两个模型家族间**部分一致**：
- **一致**：item_id 是绝对主导方差源（两个模型均 >74%），所有 main effects（temperature, prompt, seed, ordering 单独）方差为零，residual 排第二
- **不一致**：(1) Llama item_id% 低 8.7 个百分点，residual 高 4.5 个百分点 → Llama 有更多未建模的高阶交互；(2) interaction 排序不同（Llama 的 seed 敏感性远高于 Qwen）；(3) G_item 低 0.022 → 需要更多 items 达到同等可靠性
- 总体：core structure 一致（item dominance + zero main effects），但 Llama 在 seed/temperature 维度的 item-level 不稳定性更高

## 5. JSON 结果路径
`/root/nlp_variance_gtheory/data/exp_llama70b/llama70b_mmlu_gstudy.json`

---
