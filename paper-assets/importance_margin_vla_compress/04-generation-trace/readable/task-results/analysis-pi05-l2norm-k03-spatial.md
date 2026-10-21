# analysis pi05 l2norm k03 spatial

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_pi05_l2norm_k03_spatial_20260521T210255_result.json`
- **Structured JSON:** [`66843765d2c166521d54.json`](../../sessions/66/66843765d2c166521d54.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both experiments marked DONE (negative). Here's the analysis:

---

## π0.5 L2norm Spatial Suite Results

### Overall SR Comparison

| Configuration | Spatial SR | Object SR |
|---|---|---|
| **Baseline (no pruning)** | **97.2%** | — |
| Random k=0.5 | 71.6% | 68.4% |
| L2norm k=0.3 | **57.2%** | 51.0% |
| L2norm k=0.5 | **55.6%** | 33.4% |
| L2norm k=0.7 | — | 55.0% |

### Per-task Breakdown (k=0.3 vs k=0.5)

| Task | k=0.3 | k=0.5 | Baseline |
|---|---|---|---|
| T0 between plate | 62% | 74% | 100% |
| T1 next to ramekin | 72% | 82% | 100% |
| T2 from table center | 78% | 78% | 100% |
| T3 on cookie box | 24% | 28% | 100% |
| T4 in top drawer | 34% | 38% | 98% |
| T5 on ramekin | 26% | 44% | 78% |
| T6 next to cookie | **74%** | 32% | 100% |
| T7 on stove | **90%** | 74% | 98% |
| T8 next to plate | 66% | 62% | 98% |
| T9 on wooden cabinet | 46% | 44% | 100% |

### V-shape 分析：**不复现**

- **Object suite** 有清晰 V-shape：k=0.3 (51%) → k=0.5 (33.4%) → k=0.7 (55%)，valley 深度 ~18pp
- **Spatial suite** 曲线基本平坦：k=0.3 (57.2%) ≈ k=0.5 (55.6%)，差异仅 1.6pp，在噪声范围内

k=0.3 略高于 k=0.5，但这是因为个别 task 的大幅波动（T6: 74% vs 32%, T7: 90% vs 74%），而非系统性 V-shape recovery。其他 task 反而是 k=0.5 更好（T0/T1/T5）。

### 关键发现

1. **L2norm 在 Spatial 上同样远劣于 random**：k=0.5 处 L2norm 55.6% vs random 71.6%（-16pp），与 Object suite 上的 method gap 一致
2. **V-shape 是 Object-specific 现象**，不是 L2norm pruning 的通用行为模式
3. **Spatial 任务整体更 robust**：即使 70% token 被 L2norm 裁掉（k=0.3），仍有 57.2% SR；Object suite 同条件只有 51.0%

---
