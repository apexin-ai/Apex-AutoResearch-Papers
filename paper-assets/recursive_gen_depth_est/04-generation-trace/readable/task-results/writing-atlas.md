# writing atlas

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_atlas_20260515T155256_result.json`
- **Structured JSON:** [`965e27408f148ca956eb.json`](../../sessions/96/965e27408f148ca956eb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Section 4 写入完成。报告：

**Word count**: ~1090 words prose + ~110 words captions = ~1200 total (within budget)

**Citations needed** (placeholder keys to resolve):
- `\cite{placeholder_Shumailov2024Nature}` — Shumailov et al. Nature 2024, model collapse theory (used 2x: feature hierarchy shift interpretation + temperature attractor distribution)

**Figures needed** (4, all placeholder):
| Label | Content |
|---|---|
| `fig_atlas_heatmap` | 19-feature × 9-cell importance heatmap |
| `fig_feature_trajectory` | p90_ppl / var_surprisal / rep_3gram across d0-d3, stratified by model+strategy |
| `fig_auc_decay` | Binary pairwise AUC decay curves (3 models, d0-d5) with threshold lines |

**Tables** (3):
| Label | Status |
|---|---|
| `tab:main_matrix` | Complete (3×3 accuracy data filled) |
| `tab:feature_importance` | Placeholder (needs per-cell top-5 from atlas_v2 artifacts) |
| `tab:edd_sensitivity` | Summary row filled (9/9, 8/9, 7/9, 5/9); per-cell breakdown deferred |

**Key narrative decisions honored**:
- D024/D027: EDD uses continuous AUC decay narrative, NOT "three models all achieve statistically significant EDD=4"; full bootstrap CI + p-values reported
- D015: Three-tier strategy classification (nucleus/temperature/top-k), no "soft sampling" grouping
- D007: Feature universality framed as "consistent feature set" not "var_surprisal as single best"
- All quantitative claims traceable to registry data

---
