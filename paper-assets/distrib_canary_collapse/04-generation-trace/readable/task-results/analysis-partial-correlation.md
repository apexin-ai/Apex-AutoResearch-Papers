# analysis partial correlation

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_partial_correlation_20260524T160927_result.json`
- **Structured JSON:** [`dba3805464cd15ea29b7.json`](../../sessions/db/dba3805464cd15ea29b7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Done. Here are the results:

**W11 Partial Correlation Analysis — Summary**

| Metric | Mean |r| | Significant (p<0.05) |
|---|---|---|
| **Contemporaneous zero-order** | 0.613 | 18/36 (50%) |
| **Contemporaneous partial (∥gen)** | 0.451 | 5/36 (14%) |
| **Lagged zero-order** | 0.795 | 29/36 (81%) |
| **Lagged partial (∥gen)** | **0.877** | **35/36 (97%)** |

**Key findings:**

1. **Contemporaneous**: ~25% of zero-order correlation is attributable to shared generational trend, but 75% persists after controlling for generation.

2. **Lagged (the one that matters for Granger)**: Partial correlations are *stronger* than zero-order by 13% on average. Removing the shared monotonic trend actually makes the canary[t]→downstream[t+1] relationship clearer. 35/36 pairs remain significant.

3. **Null control (α=0.0)**: Mean |r|=0.41 zero-order, 0.32 partial, 0/18 significant after partialing — confirming the effect is specific to detection conditions.

**Deliverables:**
- `artifacts/partial_correlation_results.json` — full per-condition results (registered)
- `docs/paper/figures/fig_partial_correlation.pdf/.png` — detailed per-pair figure
- `docs/paper/figures/fig_partial_correlation_agg.pdf/.png` — aggregated by α (cleaner for paper)
- `scripts/w11_partial_correlation.py` — analysis script

---
