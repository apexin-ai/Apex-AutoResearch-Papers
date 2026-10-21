# edit tier1 task2 results table

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_edit_tier1_task2_results_table_20260522T034851_result.json`
- **Structured JSON:** [`1e2e6fcd81a23af69342.json`](../../sessions/1e/1e2e6fcd81a23af69342.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Decision: ADDED** — enhanced existing Table 1 rather than adding a new table.

**What changed in `experiments.tex`**:
1. Added **95% CI** column (Newcombe CIs, computed from per-type data with N=250) merged with Δpp as `Δpp [95% CI]`
2. Added **Tier** column encoding TOST ±15pp equivalence clusters: U (upper/incompleteness), M (mid-tier, 6/6 pairwise equivalent), L (lower/coreferential)
3. Switched from `\small` to `\footnotesize` + `\setlength{\tabcolsep}{3.8pt}` to fit 11 columns
4. Abbreviated model headers (GPT-5.4→5.4, Claude→Cla., etc.) with legend in caption
5. Per-model rates rounded to integers to save horizontal space

**Space impact**: Net zero vertical lines added (same row count). The `\footnotesize` switch actually reduced total page count from 16→15. Main text remains exactly 8 pages (Conclusion on p8, Limitations starts p9).

**No overfull hbox** on the table. Two pre-existing overfull warnings from other sections remain unchanged.

**CI values** (Newcombe method, verified against `gen_fig2_forest_plot.py`):
| Type | Δpp | 95% CI |
|------|-----|--------|
| Incompleteness | +49.2 | [42.2, 55.6] |
| Auth. Scope | +36.0 | [29.1, 42.6] |
| Lexical | +35.2 | [28.0, 42.0] |
| Scopal | +34.2 | [27.4, 40.7] |
| Cond. Prec. | +30.8 | [24.0, 37.4] |
| Coreferential | +18.7 | [11.5, 25.7] |
| Overall | +34.0 | [31.3, 36.9] |

---
