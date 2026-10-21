# paper nve auroc fix

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_nve-auroc-fix_20260517T125720_result.json`
- **Structured JSON:** [`d9e390d0983fd1dc3dec.json`](../../sessions/d9/d9e390d0983fd1dc3dec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

008e_v3_s2 FP framing is intact — it correctly describes NVE identifying pathological value dynamics but being unable to distinguish CIVO Pathway A from non-CIVO collapse Pathway B.

All changes complete. Summary of edits:

| File | Line | Old | New |
|------|------|-----|-----|
| `results.tex` | 81 | `correctly classifies 7/8 seeds (AUROC${=}0.933$` | `correctly classifies 11 of 12 experimental configurations (AUROC${=}0.926$` + footnote |
| `methodology.tex` | 87 | `across 8 evaluable seeds, this achieves 7/8 accuracy (AUROC${=}0.933$)` | `across 12 experimental configurations, this achieves 11/12 accuracy (AUROC${=}0.926$)` |
| `abstract.tex` | 2 | `achieves 7/8 classification ($n{=}8$, Walker Walk)` | `achieves 11/12 classification ($n{=}12$, Walker Walk)` |
| `introduction.tex` | 6 | `achieves 7/8 CIVO classification ($n{=}8$, single environment)` | `achieves 11/12 CIVO classification ($n{=}12$, single environment)` |
| `conclusion.tex` | 8 | `achieves 7/8 CIVO classification ($n{=}8$, 87.5\%)` | `achieves 11/12 CIVO classification ($n{=}12$, 91.7\%)` |
| `conclusion.tex` | 18 | `(7/8, one non-CIVO false positive; margin $0.62$ excluding the outlier)` | `(11/12, one non-CIVO false positive)` |
| `appendix.tex` | 35 | `AUROC = 0.933` | `AUROC = 0.867` |
| `appendix.tex` | 61 | `AUROC=0.933` (table caption) | `AUROC=0.867` |
| `paper/tables/nve_sensitivity_table.tex` | 11 | `0.933` | `0.867` |
| `artifacts/.../nve_sensitivity_table.tex` | 11 | `0.933` | `0.867` |

No remaining `0.933` or stale `7/8` (outside the footnote) in `.tex` files. 008e_v3_s2 FP description unchanged.

---
