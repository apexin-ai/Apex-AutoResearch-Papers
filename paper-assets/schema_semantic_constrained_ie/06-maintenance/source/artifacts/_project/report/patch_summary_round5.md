# Paper Round 5 Patch Summary

## Date: 2026-05-16

## Changes Made

### 1. `appendix_discussion.tex` — FT Ablation Table Expanded (tab:ft-ablation)

- **Before**: Table showed only DR (%) and R-F1 columns (2 metrics per row)
- **After**: Full 9-column table with DR, RV, ET, CF, PF (parse fail%), E-F1, R-F1
- All 8 rows (2 models x 2 datasets x 4 modes) populated with final data from completed experiments
- Caption updated to document F1 cost: max ΔR-F1 = -0.30pp (Qwen DocRED full vs unconstrained)

### 2. `appendix_discussion.tex` — F1 Cost Statement Added

- Added sentence after FT ablation narrative: "F1 cost is negligible: the maximum R-F1 decrease across all 16 model×dataset×mode combinations is −0.30pp (Qwen DocRED, full vs. unconstrained), attributable to parse failure increase (7.11%→8.52%) rather than constraint-induced extraction degradation."

### 3. `appendix_discussion.tex` — Residual DR Error Analysis (NEW paragraph, \label{app:residual-dr-analysis})

- 36 violations root cause taxonomy: entity type errors (39%), schema coverage gaps (33%), incorrect relation selection (17%), direction reversal (11%)
- Key insight 1: SciERC residual = 100% schema gap → constraint system at theoretical ceiling
- Key insight 2: Llama DocRED = 92% of violations → weaker entity typing, addressable via stronger models
- Framed as limitation + future work evidence (not failure)

### 4. `paper_tables_draft.tex` — TBD/RUNNING Replaced

- DocRED S1 row: TBD → 10.21 (DR_S1), TBD → -8.3 (ΔDR)
- Removed "(RUNNING)" from exp_id footnote
- Removed "pending (experiment in progress)" from caption

## Files NOT Modified (old drafts with placeholders, not compiled)

- `section7_conclusion_550cbf.tex` — historical draft, main uses `section7_conclusion_compressed.tex`
- `abstract_d3264e.tex`, `abstract_fd4b26.tex` — historical drafts, main uses `abstract.tex`

## Key Narrative Coverage Verification

| Finding | Location | Status |
|---------|----------|--------|
| Grammar redundant post-FT (DR change <0.2pp) | appendix tab:ft-ablation caption + narrative | Complete |
| Semantic is sole DR defense (39-72%) | appendix narrative + tab caption | Complete |
| Full DR ≤ 0.20% (near-elimination) | appendix narrative + composability §5 | Complete |
| F1 cost negligible (max -0.30pp) | appendix narrative + tab caption | Complete |
| Residual 36 violations root cause | appendix app:residual-dr-analysis | NEW |
| Schema gap = irreducible floor | appendix + Limitations section | Complete |
| Llama typing weakness = reducible | appendix + Limitations section | Complete |
