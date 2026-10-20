# P2 θ-Exposure Confounding Test Results

- N_models=50, N_items=300, γ_true=0.5
- seed=123
- Target confounding correlation: 0.4
- **Actual confounding correlation: 0.3814**

## 4PL NUTS

| Metric | Value | Threshold | Result |
|--------|-------|-----------|--------|
| γ mean (sd) | 0.5386 (0.0938) | — | — |
| γ 95% CI | [0.3562, 0.7228] | — | — |
| γ bias | 0.0386 | — | — |
| γ relative bias | 0.0771 | < 0.3 | PASS |
| γ CI covers true | True | Yes | PASS |
| γ CI excludes 0 | True | Yes | PASS |
| θ correlation | 0.9733 | > 0.9 | PASS |
| θ RMSE | 0.2407 | < 0.2 | PASS |
| θ-exp corr | 0.3857 | — | — |
| θ residual-exp corr | 0.0582 | — | — |
| Max R-hat | 1.007 | < 1.01 | PASS |
| Divergent | 0 (0.0%) | < 1% | PASS |
| Min ESS | 1371.9 | — | — |
| Fit time | 832.0s | — | — |

**Overall: PASS**

## Kill-or-Go Assessment

**VERDICT: GO** — 4pl_nuts pass(es) under confounding (corr≈0.38).