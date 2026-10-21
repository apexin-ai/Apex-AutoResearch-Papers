# analysis dataset a gstudy

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_dataset_a_gstudy_20260521T053533_result.json`
- **Structured JSON:** [`f7995b6c00e82591e8a7.json`](../../sessions/f7/f7995b6c00e82591e8a7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

G-study 完整完成。结果保存到 `results/analysis/dataset_a_gstudy.json`（46.4s total runtime）。

---

## Dataset A G-study 完整结果

### 方差分量（% of total, 95% CI）

| Component | % | 95% CI |
|---|---|---|
| **item_id** | **42.81%** | [34.79%, 50.06%] |
| **model×item_id** | **31.68%** | [24.61%, 37.34%] |
| **residual** | **19.34%** | [16.38%, 22.70%] |
| prompt_template×item_id | 1.77% | [1.43%, 2.18%] |
| seed×item_id | 1.73% | [1.26%, 2.17%] |
| temperature×item_id | 1.01% | [0.65%, 1.40%] |
| model (main) | 0.97% | [0.10%, 2.82%] |
| ordering×item_id | 0.64% | [0.41%, 0.93%] |

### G_item

**G_item = 0.7766**, 95% CI [0.7245, 0.8285]

### D-study（n_models sweep）

| n_models | G_item |
|---|---|
| 1 | 0.5615 |
| 2 | 0.7088 |
| 3 | 0.7766 |
| 4 | 0.8157 |
| 5 | 0.8411 |
| 6 | 0.8589 |
| 8 | 0.8823 |
| 10 | 0.8969 |

### G_condition
G_condition = 0.0289（极低，因为方法学 facets 的方差远小于 item-related 方差）

### 模型 accuracy
- Gemma-2-9B: 73.11%
- Llama-3.1-8B: 71.08%
- Mistral-7B: 63.76%

### 与 2-model 旧结果对比

| Component | 2-model | 3-model | 变化 |
|---|---|---|---|
| item_id | 37.9% | **42.81%** | +4.9pp |
| model×item_id | 26.2% | **31.68%** | +5.5pp |
| residual | — | 19.34% | — |

### 关键观察

1. **加入 Mistral 后 model×item_id 交互跃升至 31.68%** — Mistral accuracy (63.8%) 显著低于 Llama/Gemma (71-73%)，且在不同 items 上的表现模式不同，放大了 model×item 交互
2. **item_id 仍是最大方差源 (42.8%)**，确认 item 难度差异是评测变异的主导因素
3. **G_item = 0.78 > 0.70 阈值**，3 个模型已足够可靠排序 items；D-study 显示 5+ 模型可达 0.84+
4. **方法学 facets（temp, prompt, seed, ordering）的 main effects 极小 (<1%)**，但它们与 item 的交互合计贡献 ~5%
5. **residual 19.3% 包含所有 ≥3-way 交互**，不可忽视

---
