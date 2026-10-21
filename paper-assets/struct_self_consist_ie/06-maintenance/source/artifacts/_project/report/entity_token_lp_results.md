## Entity-Token LP Analysis (exp-028)

| LP Variant | W-Range | W-Rho | G-Rho | Sel.F1 | ΔGreedy |
|---|---|---|---|---|---|
| full | 0.040 | 0.094 | 0.297 | **0.647** | +0.004 |
| entity_text | 0.086 | 0.000 | 0.351 | 0.626 | -0.017 |
| entity_type | 0.156 | 0.053 | 0.324 | 0.638 | -0.005 |
| entity_text_type | 0.135 | 0.109 | **0.440** | 0.636 | -0.007 |
| entity_all | 0.187 | 0.000 | 0.140 | 0.613 | -0.030 |
| schema_only | 0.009 | 0.000 | 0.318 | 0.614 | -0.029 |

Conclusion: NEGATIVE. Format tokens dilute cross-instance LP (32% dilution), but within-instance ranking unaffected (schema tokens constant across samples). Span offset tokens are pure noise (entity_all ρ=0.140).