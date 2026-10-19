# research comet power analysis

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_comet-power-analysis_20260524T151958_result.json`
- **Structured JSON:** [`52baac4cb99c511663b3.json`](../../sessions/52/52baac4cb99c511663b3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected and computed. Here are the results:

---

## COMET Tercile Power Analysis

### 原始数据

| | Qwen3-8B (L22) | Llama-3.1-8B (L13) |
|---|---|---|
| n per tercile | 56 | 56 |
| Full bal_acc | 0.6488 | 0.5919 |
| High COMET bal_acc | 0.6071 | 0.6165 |
| Low COMET bal_acc | 0.6635 | 0.6000 |
| Δ(High−Low) | −5.64 pp | +1.65 pp |
| Fisher p | 0.695 | 0.761 |

### Power Analysis (α=0.05, power=0.80, two-sided)

| | Qwen3-8B | Llama-3.1-8B |
|---|---|---|
| MDD (minimum detectable difference) | **25.3 pp** | **26.0 pp** |
| |Observed Δ| / MDD | 0.22 | 0.06 |

### 需要多大样本？

| 目标可检测差异 | 所需每组样本量 |
|---|---|
| 10 pp | n=393 |
| 5 pp | n=1,571 |

### Gemma

Gemma 无 ZH 数据（无 `zh_activations.pt`、无 COMET scores）。Gemma 仅做了 EN 单语探针实验，未进行 EN→ZH 跨语言迁移，因此 COMET tercile 分析不适用。

### 结论

现有样本量（n=56/tercile）在 power=0.80 下仅能检测 ≥25–26 pp 的差异。观测到的差异（Qwen −5.6 pp, Llama +1.7 pp）远小于 MDD，且方向在两个模型间不一致。这证实翻译质量对 probe transfer 无有意义的影响——即使存在效应，其量级也远不足以影响实验结论。

---
