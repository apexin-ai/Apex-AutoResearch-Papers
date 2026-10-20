# paper writing experiments

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_experiments_20260515T183211_result.json`
- **Structured JSON:** [`640510b2d4a5a90df141.json`](../../sessions/64/640510b2d4a5a90df141.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All structure verified:
- 5 subsections (5.1–5.5) with labels
- 3 tables (drift_summary, method_comparison, fpr_fnr)
- All 5 figure refs (differencing_dmax, consensus_heatmap, regime_map, metric_trajectory, consensus_workflow)
- 6 citations (biderman2023pythia, merity2017pointer, shumailov2024curse, scheffer2009early, li2016diversity, shojaie2022granger, boettiger2012limits)

Constraint compliance verified:
- "diversity collapse" scoping (not "model collapse") [PC07] — line 129
- effective_rank/Self-BLEU failure reported [PC08] — lines 151–153
- distinct-3 to Appendix [PC09] — lines 20, 136, 155
- No Cohen f² benchmarks [PC10]
- No "consistently outperforms"/"state-of-the-art"/"significantly" without test [PC14]
- Dual spurious rates 75%/62.5% [PC15] — lines 56–57
- α=0.75 single-seed caveat [PC16] — lines 114, 143–144
- Non-monotonicity "observed at seed=42" [PC17] — line 110
- α=0.75 vs α=1.0 consensus not directly compared [PC01]
- token_entropy→perplexity@α=0.75 not cited [PC02]

Two bib entries need to be added to `references.bib`: `biderman2023pythia` (Pythia) and `merity2017pointer` (WikiText-103).

---
