# code fix and analyze llama8b

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-and-analyze-llama8b_20260519T080946_result.json`
- **Structured JSON:** [`302e110df4049ffc4d0b.json`](../../sessions/30/302e110df4049ffc4d0b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

## 结果汇总

### LLaMA-3.1-8B Code 实验 (exp_code_llama8b)

**K\* = 2** (AUC 阈值 θ=0.6)

| Depth Pair | AUC | CI (±) | JSD |
|---|---|---|---|
| 0 vs 1 | 0.9161 | 0.0040 | 0.0604 |
| 1 vs 2 | **0.7394** (K\* boundary) | 0.0102 | 0.0470 |
| 2 vs 3 | 0.5112 | 0.0095 | 0.0035 |
| 3 vs 4 | 0.5200 | 0.0137 | 0.0030 |
| 4 vs 5 | 0.4996 | 0.0069 | 0.0029 |

Ordinal Classification: MAE=1.2542, Acc=0.3485

### 与 Qwen Code K\*=2 对比

| 指标 | Qwen2.5-1.5B | LLaMA-3.1-8B |
|---|---|---|
| K\* | 2 | 2 |
| AUC(0v1) | 0.9388 | 0.9161 |
| AUC(1v2) | 0.7382 | 0.7394 |
| AUC(2v3) | 0.5300 | 0.5112 |

LLaMA-8B 和 Qwen-1.5B 在 code domain 的 K\* 一致 (K\*=2)，AUC(1v2) 几乎相同 (0.74)。LLaMA-8B 的 AUC(0v1) 略低 (0.916 vs 0.939)，说明更大模型的第一代文本略难与原始文本区分。

### Cross-model 表格
`code_crossmodel_table.tex` 已更新。Qwen-7B 和 Mistral-7B 仍在运行中 (TBD)。Pythia-1.4B K\*=1 是唯一的异类。

---
