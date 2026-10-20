# analysis phase2 gstudy mmlu 8model

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_phase2_gstudy_mmlu_8model_20260521T220400_result.json`
- **Structured JSON:** [`4ea4041ea73d83f4f057.json`](../../sessions/4e/4ea4041ea73d83f4f057.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## MMLU 8-Model Henderson I G-Study 结果

**N = 460,800** (8 models × 2 temps × 6 prompts × 6 seeds × 4 orderings × 200 items)
**Grand mean accuracy = 0.6457**
**Models**: DeepSeek-7B, Gemma-2-9B, InternLM2.5-7B, Llama-3.1-8B, Mistral-7B-v0.3, OLMo-2-7B, Qwen3-8B, Yi-1.5-9B

### 方差分解表

| Facet | σ²% | 95% CI |
|---|---:|---:|
| item_id | 37.88% | [33.12%, 42.17%] |
| model:item_id | 30.21% | [26.81%, 33.32%] |
| residual | 25.01% | [22.89%, 27.22%] |
| model | 2.83% | [1.89%, 4.47%] |
| model:prompt_template | 1.59% | [1.27%, 2.07%] |
| prompt_template:item_id | 0.95% | [0.82%, 1.08%] |
| temperature:item_id | 0.56% | [0.38%, 0.78%] |
| seed:item_id | 0.53% | [0.41%, 0.64%] |
| ordering:item_id | 0.31% | [0.25%, 0.38%] |
| model:temperature | 0.04% | [0.03%, 0.12%] |
| model:seed | 0.03% | [0.03%, 0.07%] |
| model:ordering | 0.03% | [0.02%, 0.07%] |
| temperature | 0.02% | [0.00%, 0.06%] |
| 其余 10 个分量 | <0.01% each | — |

### G_item

**G_item = 0.8962  [0.8742, 0.9152]**

- σ²(τ) = 0.0872 (item_id)
- σ²(δ) = 0.0101 (item interactions + residual/n_conditions)

### 与已有结果对比

| Benchmark | n_models | item_id% | G_item |
|---|---:|---:|---:|
| MMLU (8) | 8 | 37.88% | 0.8962 |
| MMLU (6) | 6 | ~42% | — |
| GSM8K (8) | 8 | 16.86% | 0.2837 |
| MATH (7) | 7 | 26.48% | 0.3625 |

MMLU item_id% 从 6-model 的 ~42% 降至 37.88%（model:item_id 吸收了部分方差），但 G_item = 0.8962 远高于 GSM8K/MATH，说明 MMLU items 在 8 个模型间的难度排序高度可靠。

JSON 已保存至 `westd-32570:results/exp004_8model_analysis/per_benchmark_gstudy_mmlu.json`。

---
