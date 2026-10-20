# d066 Beam Sweep — DocRED Eval Results

**Date**: 2026-05-20
**Eval script**: `eval_d064.py` (DocRED ontology hardcoded)
**Samples**: 200 per file

## Full Results

| Config | Model | Beam | Mode | E-F1 | R-F1 | ET% | RV% | DR% | CF% | PF% |
|--------|-------|------|------|------|------|-----|-----|-----|-----|-----|
| qwen_greedy_s1 | Qwen | greedy | constrained | 80.54 | 43.64 | 0.00 | 0.00 | 0.00 | 0.12 | 7.5 |
| qwen_greedy_unc | Qwen | greedy | unconstrained | 81.34 | 44.56 | 0.00 | 0.24 | 0.20 | 0.03 | 6.5 |
| qwen_beam2_s1 | Qwen | 2 | constrained | 84.46 | 47.30 | 0.00 | 0.00 | 0.00 | 0.08 | 1.0 |
| qwen_beam2_unc | Qwen | 2 | unconstrained | 84.25 | 47.39 | 0.00 | 0.11 | 0.43 | 0.00 | 1.5 |
| qwen_beam8_s1 | Qwen | 8 | constrained | 84.54 | 48.43 | 0.00 | 0.00 | 0.00 | 0.00 | 1.0 |
| qwen_beam8_unc | Qwen | 8 | unconstrained | 83.95 | 47.84 | 0.00 | 0.11 | 0.33 | 0.00 | 2.0 |
| llama_beam2_s1 | Llama | 2 | constrained | 85.60 | 51.17 | 0.00 | 0.00 | 0.00 | 0.00 | 0.5 |
| llama_beam2_unc | Llama | 2 | unconstrained | 85.34 | 51.31 | 0.00 | 0.07 | 0.11 | 0.05 | 1.0 |
| llama_beam8_s1 | Llama | 8 | constrained | 85.76 | 51.74 | 0.00 | 0.00 | 0.00 | 0.00 | 0.5 |
| llama_beam8_unc | Llama | 8 | unconstrained | 85.77 | 51.97 | 0.00 | 0.07 | 0.00 | 0.05 | 0.5 |

## By Model — Best Config

| Model | Best Config | E-F1 | R-F1 |
|-------|-------------|------|------|
| Qwen | beam8_constrained | 84.54 | 48.43 |
| Llama | beam8_unconstrained | 85.77 | 51.97 |

## Beam Width Effect (Constrained, R-F1)

| Model | Greedy | Beam=2 | Beam=8 | Δ(greedy→8) |
|-------|--------|--------|--------|-------------|
| Qwen | 43.64 | 47.30 | 48.43 | +4.79 |
| Llama | — | 51.17 | 51.74 | +0.57 |

## Constrained vs Unconstrained (R-F1)

| Model | Beam | Constrained | Unconstrained | Δ |
|-------|------|-------------|---------------|---|
| Qwen | greedy | 43.64 | 44.56 | -0.92 |
| Qwen | 2 | 47.30 | 47.39 | -0.09 |
| Qwen | 8 | 48.43 | 47.84 | +0.59 |
| Llama | 2 | 51.17 | 51.31 | -0.14 |
| Llama | 8 | 51.74 | 51.97 | -0.23 |

## Violation Summary

Constrained decoding (full_s1) eliminates RV% and DR% to 0.00 across all configs. Unconstrained shows small but nonzero violations (RV up to 0.24%, DR up to 0.43%). ET% is 0.00 everywhere — both models produce valid entity types. CF% is near-zero in all configs.

## Parse Failure Rate

Beam search dramatically reduces PF% for Qwen: 7.5% (greedy) → 1.0% (beam2/8). Llama maintains low PF% (0.5-1.0%) regardless of beam width.
