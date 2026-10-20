# Paper Data Audit Report — 2026-05-23

## Summary
| Category | Count |
|----------|-------|
| ✅ Consistent | 35 |
| ⚠️ Minor rounding | 2 |
| 📝 Placeholders | 5 |
| ❌ Not traceable (not errors) | 7 |

## Minor rounding fixes needed
1. appendix.tex:370 — N=8 θ RMSE improvement: -50.1% → -50.3%
2. appendix.tex:389 — N=20 θ RMSE improvement: -45.0% → -45.2%

## Placeholders to fill
1. experiments.tex:7 — "XX,XXX observations" → 5,661
2. experiments.tex:7 — "XX.X% fill rate" → 44.7%
3. limitations.tex:1 — "XX.X% fill rate (XX,XXX of XX,XXX potential cells)" → 44.7% (5,661 of 12,672)
4. experiments.tex:9 — "τ = TBD" (self-eval) → 0.857
5. experiments.tex:29-37 — 17-model columns → pending N=17 results

## Not traceable to registry (7 items)
These come from analysis scripts, not registry experiments:
- N ≈ 17 for 80% power
- P(Δτ ≥ 0) = 0.927
- P(θ_mini > θ_qwen) = 0.853
- PPC: predicted 0.593 vs observed 0.599
- Self-eval win rates
- θ CI coverage 90.1%, c_n 67.9%
- Horseshoe vs HalfNormal r > 0.999