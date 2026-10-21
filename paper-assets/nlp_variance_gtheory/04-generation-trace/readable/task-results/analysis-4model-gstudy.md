# analysis 4model gstudy

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_4model_gstudy_20260521T072418_result.json`
- **Structured JSON:** [`12a31158fe513bc21b5c.json`](../../sessions/12/12a31158fe513bc21b5c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。以下是 exp-001 四模型 G-study 最终结果。

---

## 1. 模型准确率

| Model | Accuracy |
|-------|----------|
| gemma-2-9b-it | 0.7311 |
| qwen3-8b | 0.7263 |
| llama-3.1-8b-instruct | 0.7108 |
| mistral-7b-instruct-v0.3 | 0.6376 |

Grand mean = 0.7015, N = 345,600 (4 models × 432 conditions × 200 items)

## 2. 方差分量 (EMS, %) + 95% Bootstrap CI

| Component | % | 95% CI |
|-----------|---|--------|
| **item_id** | **42.07** | [36.03, 48.76] |
| **model×item_id** | **33.64** | [28.40, 37.86] |
| residual | 19.55 | [17.08, 21.66] |
| prompt_template×item_id | 1.43 | [1.20, 1.67] |
| seed×item_id | 1.32 | [1.08, 1.66] |
| model | 0.73 | [0.16, 2.07] |
| temperature×item_id | 0.65 | [0.43, 0.91] |
| ordering×item_id | 0.54 | [0.40, 0.72] |

## 3. G_item

**G_item = 0.8200** [0.7816, 0.8609]

## 4. D-study (n_models sweep)

| n_models | G_item |
|----------|--------|
| 1 | 0.5495 |
| 2 | 0.7044 |
| 3 | 0.7775 |
| **4** | **0.8200** |
| 5 | 0.8479 |
| 6 | 0.8675 |
| 8 | 0.8934 |
| 10 | 0.9096 |

## 5. 与 3-model 对比

| Metric | 3-Model | 4-Model | Delta |
|--------|---------|---------|-------|
| item_id % | 42.80 | 42.07 | -0.73 |
| model×item % | 31.68 | 33.64 | +1.96 |
| G_item | 0.7766 | 0.8200 | **+0.0434** |

item_id 和 model×item 的相对比例基本稳定。G_item 从 0.777 提升到 0.820，符合 D-study 预测（3-model 预测 n=4 时 G=0.816）。

## 6. 各模型对 model×item 交互的贡献

| Model | Contribution |
|-------|-------------|
| mistral-7b-instruct-v0.3 | **29.25%** |
| qwen3-8b | 27.11% |
| gemma-2-9b-it | 23.95% |
| llama-3.1-8b-instruct | 19.69% |

Mistral 对 model×item 交互贡献最大（29.25%），因为它整体准确率最低且在不同 item 上的表现模式与其他模型差异最大。Qwen 紧随其后（27.11%）。

结果已保存至 `results/analysis/dataset_a4_gstudy.json`。

---
