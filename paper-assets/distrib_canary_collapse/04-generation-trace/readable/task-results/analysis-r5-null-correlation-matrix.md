# analysis r5 null correlation matrix

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r5_null_correlation_matrix_20260520T204816_result.json`
- **Structured JSON:** [`7ed59192d0ab65e97033.json`](../../sessions/7e/7ed59192d0ab65e97033.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出 `artifacts/r5_null_correlation_matrix.json`，核心结果：

| Method | s42 | s43 | s44 | Total |
|--------|-----|-----|-----|-------|
| **PermG_fdr** | 0/8 | 0/8 | 0/8 | **0/24** |
| DiffXCorr_fdr | 4/8 | 2/8 | 3/8 | 9/24 |
| NaiveXCorr | 8/8 | 7/8 | 7/8 | 22/24 |
| ThresholdOnset | 3/8 | 1/8 | 2/8 | 6/24 |
| TY_Granger | 2/8 | 2/8 | 0/8 | 4/24 |

**Clopper-Pearson CI (PermG, 0 rejections):**
- 0/3 seeds: [0, 0.708]
- 0/24 (if pairs independent): [0, 0.142]

**Effective N:**
- PermG 全零 → effective N = 3（下界），无法区分 pair 独立性
- DiffXCorr ICC = 0.3386（中等聚类），te→d2 跨 3 seed 一致 reject (3/3)，ece 系列一致 non-reject (0/3)，说明 pair 间不独立，effective N 介于 3 和 24 之间

**关键发现：** PermG_fdr 是唯一在 α=0 null 下保持 0% FPR 的方法。NaiveXCorr 在 null 下 FPR 高达 92%，DiffXCorr_fdr 37.5%，ThresholdOnset 25%，TY_Granger 17%——这些方法在无真实信号时大量误报。

---
