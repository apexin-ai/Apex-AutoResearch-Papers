# code fig degen scatter redraw

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fig_degen_scatter_redraw_20260518T212740_result.json`
- **Structured JSON:** [`51f5dd7c279a8322a09e.json`](../../sessions/51/51f5dd7c279a8322a09e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Figure verified visually. The plot looks clean with CoNLL now correctly at 48.4% (was 59.1%).

## 产出总结

### 1. 数据源
- 退化率: `output/unified_degeneracy_audit/degeneracy_recalc_results.json` (unified constant-F1 gold-filtered)
- LP Delta: `output/dgs_selection_results.json` (gated_minus_greedy_pp)
- Per-type: `output/exp_021_inference/per_type_lp_analysis.csv`

### 2. PDF 路径
- `output/figures/fig_degeneracy_lp_scatter.pdf`
- `docs/paper/figures/fig_degeneracy_lp_scatter.pdf` (已复制)

### 3. 所有数据点坐标

**Cross-dataset (Qwen3-8B):**

| 数据集 | 退化率(unified) | LP Delta (pp) |
|--------|----------------|---------------|
| CoNLL | 48.4% | -0.81 |
| SciERC | 17.8% | +0.74 |
| Few-NERD | 7.1% | +1.37 |

**Per-type (Few-NERD entity types, unchanged):**

| Type | 退化率 | LP Delta (pp) |
|------|--------|---------------|
| event | 5.97% | +0.65 |
| other | 6.61% | +4.73 |
| organization | 6.74% | +1.21 |
| building | 7.18% | +0.23 |
| product | 8.17% | +2.01 |
| location | 11.42% | +0.53 |
| person | 13.42% | +1.25 |
| art | 19.81% | -0.17 |

**Spearman correlations (updated):**
- 11-point: rho = -0.5455, p = 0.0827
- Dataset-level (n=3): rho = -1.0000 (perfect negative)
- Per-type (n=8): rho = -0.3810, p = 0.3518

---
