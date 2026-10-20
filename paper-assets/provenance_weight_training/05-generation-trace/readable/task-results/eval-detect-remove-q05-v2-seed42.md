# eval detect remove q05 v2 seed42

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_detect_remove_q05_v2_seed42_20260521T200809_result.json`
- **Structured JSON:** [`7fb5957e3d55f6824f0a.json`](../../sessions/7f/7fb5957e3d55f6824f0a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。

---

## 结果汇总

### detect_remove_q05_v2_seed42 三组 Eval

| 数据集 | Loss | PPL |
|--------|------|-----|
| **Holdout** | 2.8499 | **17.2853** |
| **OWT** | 2.8911 | **18.0139** |
| **Wiki** | 2.7116 | **15.0528** |

### 与 Baseline 对比

| 数据集 | detect_remove | adaptive | Δ vs adaptive | uniform | Δ vs uniform |
|--------|-------------|----------|--------------|---------|-------------|
| Holdout | **17.285** | 17.653 | **-0.367** (-2.08%) | 17.694 | **-0.409** (-2.31%) |
| OWT | **18.014** | 18.424 | **-0.410** (-2.23%) | — | — |
| Wiki | **15.053** | 15.473 | **-0.420** (-2.72%) | — | — |

### 判断：Hard Filtering vs Soft Reweighting

**Hard filtering (detect-and-remove q=0.5) 全面优于 soft reweighting (adaptive)**。三个评估集上 PPL 均低 0.37–0.42，改善幅度 2.1%–2.7%，一致且显著。这说明在当前 contamination 比例下，直接移除低质量数据比对其降权训练更有效——低分样本即使被大幅降权，仍然通过梯度噪声拖累模型质量。

---
