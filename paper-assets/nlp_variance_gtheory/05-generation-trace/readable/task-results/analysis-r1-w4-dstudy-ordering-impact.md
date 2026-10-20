# analysis r1 w4 dstudy ordering impact

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r1_w4_dstudy_ordering_impact_20260521T201438_result.json`
- **Structured JSON:** [`fb0e066cf3ccafdfe728.json`](../../sessions/fb/fb0e066cf3ccafdfe728.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

JSON 已保存。以下是完整结果汇总：

---

## R1-W4 Ordering Facet Impact 结果

### 1. Ordering 验证
- **0 / 14,400 cells** 在不同 ordering 下有不同 `correct` 值 → **完美 no-op**

### 2. G_item 对比

| | Analysis A (with ordering) | Analysis B (without ordering) |
|---|---|---|
| Facets | temp, prompt, seed, ordering, item | temp, prompt, seed, item |
| Records | 57,600 | 14,400 |
| Conditions | 288 | 72 |
| **G_item** | **0.836835** | **0.836835** |
| σ²(δ) | 0.01126416 | 0.01126416 |

**差异 = 0.00000000**

### 3. Variance Components 对比（非零项）

| Effect | σ² | % |
|---|---|---|
| item_id | 0.0578 | 22.09% |
| prompt_id | 0.0670 | 25.62% |
| prompt_id:item_id | 0.0218 | 8.34% |
| temperature:item_id | 0.0052 | 1.97% |
| temperature:prompt_id:item_id | 0.0454 | 17.35% |
| temperature:seed:item_id | 0.0055 | 2.10% |
| temperature:prompt_id:seed:item_id (residual) | 0.0588 | 22.50% |

两个分析的所有共享 variance components **完全一致**（差异 = 0）。

### 4. Ordering 相关项
**全部 16 个含 ordering 的效应（主效应 + 所有交互）SS 和 σ² 均 = 0。**

### 5. 结论
Ordering 作为 pseudo-replicated facet 对 G 系数 **无任何影响**。因为 ordering 在非 MC benchmarks 上不改变输出，它只引入零方差项，在 δ 计算中完全抵消。移除 ordering facet 可以简化分析（从 31 个效应降到 15 个），但不改变 G 系数和方差分解结论。

---
