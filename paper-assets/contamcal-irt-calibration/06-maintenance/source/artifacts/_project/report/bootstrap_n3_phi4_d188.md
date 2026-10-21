## Bootstrap n=3 Phi-4 (D188 fix applied)

Generated: 2026-05-20T16:53Z

### Full Table
| Family | n | Δ(d100) | 95% CI | Pattern | Dir. | Dir-Con | ρ |
|---|---|---|---|---|---|---|---|
| Phi-4 | 3 | +0.72pp | [-0.17, +1.39](boot) | Immune† | 0 | ✗ | 0.31 |
| Qwen2.5-14B | 2 | -11.05pp | [-32.41, +10.30](t) | Collapse | − | ✓ | 0.80 |
| Qwen2.5-7B | 2 | -0.89pp | [-12.16, +10.37](t) | V-recovery | 0 | ✗ | 0.40 |
| Gemma-2-9B | 2 | +2.62pp | [-11.81, +17.06](t) | Benefit-sat† | + | ✓ | 0.30 |
| OLMo-2-7B | 3 | +1.35pp | [-0.55, +2.60](boot) | Benefit-sat† | + | ✗ | 0.03 |

### Phi-4 n=2→3 key change
- CI method: t(df=1) → BCa bootstrap (10k resamples)
- CI width: extremely wide → [-0.17, +1.39] (1.56pp range)
- CI excludes 0 (p≈0.039) but effect +0.72pp is practically negligible
- Direction: neutral (|mean| < 1pp)