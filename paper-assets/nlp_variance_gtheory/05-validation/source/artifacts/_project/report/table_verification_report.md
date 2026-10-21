# Table 2 + Table 3 Verification Report

## Table 2 (MMLU 8-model) — 7/9 rows need fix

| Component | JSON exact | Paper current | Diff (pp) | Action |
|-----------|-----------|---------------|-----------|--------|
| item_id | 37.88 | 37.9 | 0.02 | OK |
| model×item | **30.21** | 33.0 | **2.79** | FIX→30 |
| residual | **25.01** | 23.1 | **1.91** | FIX→25 |
| model | **2.83** | 0.9 | **1.93** | FIX→3 |
| model×prompt | **1.59** | (in "others <0.2") | **1.39** | FIX→add row |
| prompt×item | **0.95** | 2.1 | **1.15** | FIX→1 |
| seed×item | **0.53** | 1.5 | **0.97** | FIX→1 |
| temp×item | 0.56 | 0.8 | 0.24 | OK |
| ordering×item | 0.31 | 0.5 | 0.19 | OK |

Body text fixes needed:
- "model main effect below 1%" → "below 3%" (actual 2.83%)
- "model×item up to 33%" → "30%" (actual 30.21%)

## Table 3 (5-benchmark) — 19/30 cells need fix

### Worst errors by benchmark:
- MATH: residual 32→44 (+11.9pp), prompt 8→1 (-7.2pp), m×i 12→17 (+5.3pp)
- GSM8K: residual 30→40 (+9.9pp), prompt 12→5 (-6.6pp), m×i 8→15 (+6.6pp)
- ARC: m×prompt <1→8 (+7.0pp), residual 22→15 (-6.6pp)

### Full correction matrix:

| BM | item | m×i | model | prompt | m×p | resid |
|----|------|-----|-------|--------|-----|-------|
| MMLU | 38✓ | 33→30 | 1→3 | <1✓ | <1→2 | 23→25 |
| ARC | 38✓ | 32→34 | 1→3 | <1✓ | <1→8 | 22→15 |
| HellaSwag | 34✓ | 34→36 | 1→5 | <1✓ | <1✓ | 25→21 |
| GSM8K | 17✓ | 8→15 | 15→11 | 12→5 | 9✓ | 30→40 |
| MATH | 24✓ | 12→17 | 10→9 | 8→1 | 6→2 | 32→44 |