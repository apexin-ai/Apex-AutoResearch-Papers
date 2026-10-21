# paper writing experiments d032

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_experiments_d032_20260517T154238_result.json`
- **Structured JSON:** [`4f1129534cc84a4af47b.json`](../../sessions/4f/4f1129534cc84a4af47b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Labels and cross-references are all correct. Key labels defined:
- `sec:experiments`, `sec:setup`, `sec:layer-results`, `sec:hs-text`, `sec:temporal`, `sec:32b-analysis`, `sec:negative`
- `tab:layer_selection`, `tab:hs_vs_text`, `tab:32b_divergence`, `tab:negative`, `fig:window_ablation`

The method section's cross-references to `\cref{sec:layer-results}` and `\cref{tab:layer_selection}` will resolve correctly.

The complete experiments.tex is written to the target path. Structure:

- **4.1 Experimental Setup** (~280w): Models, training protocol, layer selection overview
- **4.2 Layer Selection Results** (~370w): Primary contribution. Table `tab:layer_selection` shows biased vs corrected layers with downstream p-value impact. Key finding: crossing rate component reverses 32B conclusions
- **4.3 HS vs Text Comparison** (~480w): Secondary contribution. Table `tab:hs_vs_text` with 12/12 Holm-Bonferroni. Precision +15.4 to +23.6pp across all 4 models. Caveats: different W per model, R1-32B 25% coverage, QwQ negative lead time
- **4.4 Temporal Context Effects** (~370w): Universal text probe benefit, 3/4 HS probe benefit, OT-7B exception detailed. Figure `fig:window_ablation`
- **4.5 32B Model-Specific Analysis** (~290w): Table `tab:32b_divergence`. R1-32B: excellent lead time, narrow coverage. QwQ: robust significance, poor timing
- **4.6 Negative Results** (~300w): Table `tab:negative`. 7 methods fail: BOCPD, CUSUM, Mahalanobis, RepE, MLP, CCS, cross-transfer

---
