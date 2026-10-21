# analysis 72b gstudy final

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_72b_gstudy_final_20260522T190141_result.json`
- **Structured JSON:** [`7838a50dd4d167f75fc2.json`](../../sessions/78/7838a50dd4d167f75fc2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### Part 1: 72B 单模型 Henderson I

| Component | % |
|---|---|
| **item_id** | **83.25%** |
| residual | 7.45% |
| prompt_template:item_id | 6.81% |
| ordering:item_id | 1.02% |
| seed:item_id | 0.93% |
| temperature:item_id | 0.51% |
| 其余 | <0.05% |

- Grand mean: 0.870 (87.0%)
- **G_item = 0.979**

**Scale 趋势（单模型 item_id% / G_item）**：
- 3B: 75.3% / 0.963
- 7B: 73.4% / 0.956
- **72B: 83.2% / 0.979**

72B 的 item variance 占比和 G 系数都显著高于 3B/7B——更大的模型对 evaluation facets 更稳定，item 难度成为更主导的方差来源。

### Part 2: 3-model Crossed G-study

| Component | % |
|---|---|
| **model:item_id** | **38.55%** |
| **item_id** | **35.71%** |
| residual | 15.94% |
| model | 4.84% |
| prompt_template:item_id | 3.09% |
| ordering:item_id | 0.72% |
| seed:item_id | 0.61% |
| temperature:item_id | 0.45% |
| 其余 | <0.1% |

- **G_item = 0.720**

**Crossed 对比**：

| Design | item_id% | model:item% | G_item |
|---|---|---|---|
| 8-model (exp002) | 37.9% | 30.2% | 0.896 |
| 2-model (3B+7B) | 43.5% | 31.7% | 0.713 |
| **3-model (3B/7B/72B)** | **35.7%** | **38.5%** | **0.720** |

72B 的加入使 model:item 交互超过了 item 主效应，成为最大方差源（38.5% > 35.7%）。这是因为 72B 与 3B/7B 在 item-level 上的 differential performance 比 3B 与 7B 之间更大。G_item=0.720 与 2-model 的 0.713 相近，远低于 8-model 的 0.896（8 模型的 n_model=8 在 δ 中分母更大，压低了 model:item 的贡献）。

---
