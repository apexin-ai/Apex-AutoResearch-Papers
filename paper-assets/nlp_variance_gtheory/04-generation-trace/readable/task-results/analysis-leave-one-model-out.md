# analysis leave one model out

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_leave_one_model_out_20260521T074432_result.json`
- **Structured JSON:** [`f0dcdb3322bee4173a9e.json`](../../sessions/f0/f0dcdb3322bee4173a9e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已保存。汇报如下：

---

## Leave-One-Model-Out 对比表

| Dropped | item_id% | model×item% | G_item |
|---|---:|---:|---:|
| (none — full 4-model) | 51.29 | 25.25 | 0.8801 |
| gemma-2-9b-it | 52.88 | 22.50 | 0.8629 |
| llama-3.1-8b-instruct | 52.70 | 24.68 | 0.8536 |
| mistral-7b-instruct-v0.3 | 56.57 | 21.47 | 0.8764 |
| qwen3-8b | 54.52 | 21.17 | 0.8728 |

## 稳定性指标

| 指标 | Range | Spread |
|---|---|---|
| item_id% | [52.70, 56.57] | 3.87 pp |
| model×item% | [21.17, 24.68] | 3.51 pp |
| G_item | [0.8536, 0.8764] | 0.0228 |

## 关键发现

1. **model×item ≥25% 未在所有子集达标** — 4-model 完整数据为 25.25%，但所有 3-model 子集均低于 25%（21.17%–24.68%）。这是因为去掉一个模型后，model×item 交互效应被部分吸收到 item 主效应和残差中。

2. **影响最大：去掉 qwen3-8b**（m×i 下降 4.08pp 至 21.17%），说明 qwen3-8b 与其他模型在 item 上的交互模式差异最大。

3. **影响最小：去掉 llama-3.1-8b-instruct**（m×i 仅下降 0.57pp 至 24.68%），说明 llama 的 item 响应模式与其余模型最相似。

4. **G_item 高度稳定**：所有子集的 G_item 均在 0.85–0.88 之间（spread 仅 0.023），item 难度始终是最可靠的方差来源，不依赖任何单个模型。

---
