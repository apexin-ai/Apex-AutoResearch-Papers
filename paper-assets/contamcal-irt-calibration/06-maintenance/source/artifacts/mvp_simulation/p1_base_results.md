# P1 Base Condition Results

- N_models=50, N_items=100, γ_true=0.5, exposure_rate=0.3
- seed=42

## 2PL ADVI

| Metric | Value | Threshold | Result |
|--------|-------|-----------|--------|
| γ mean (sd) | 0.0355 (0.0) | — | — |
| γ 95% CI | [0.0355, 0.0355] | — | — |
| γ bias | -0.4645 | — | — |
| γ relative bias | 0.929 | < 0.3 | **FAIL** |
| γ CI covers true | False | Yes | **FAIL** |
| γ CI excludes 0 | True | Yes | PASS |
| θ correlation | 0.347 | > 0.9 | **FAIL** |
| θ RMSE | 0.7584 | < 0.2 | **FAIL** |
| Fit time | 80.4s | — | — |

**Overall: FAIL**

## 2PL NUTS

| Metric | Value | Threshold | Result |
|--------|-------|-----------|--------|
| γ mean (sd) | 0.1589 (0.067) | — | — |
| γ 95% CI | [0.0291, 0.286] | — | — |
| γ bias | -0.3411 | — | — |
| γ relative bias | 0.6821 | < 0.3 | **FAIL** |
| γ CI covers true | False | Yes | **FAIL** |
| γ CI excludes 0 | True | Yes | PASS |
| θ correlation | 0.8685 | > 0.9 | **FAIL** |
| θ RMSE | 0.427 | < 0.2 | **FAIL** |
| Max R-hat | 1.0076 | < 1.01 | PASS |
| Divergent | 0 (0.0%) | < 1% | PASS |
| Min ESS | 1240.9 | — | — |
| Fit time | 412.1s | — | — |

**Overall: FAIL**

## 4PL ADVI

| Metric | Value | Threshold | Result |
|--------|-------|-----------|--------|
| γ mean (sd) | -1.0095 (0.0) | — | — |
| γ 95% CI | [-1.0095, -1.0095] | — | — |
| γ bias | -1.5095 | — | — |
| γ relative bias | 3.0191 | < 0.3 | **FAIL** |
| γ CI covers true | False | Yes | **FAIL** |
| γ CI excludes 0 | True | Yes | PASS |
| θ correlation | 0.164 | > 0.9 | **FAIL** |
| θ RMSE | 1.0634 | < 0.2 | **FAIL** |
| Fit time | 100.5s | — | — |

**Overall: FAIL**

## 4PL NUTS

| Metric | Value | Threshold | Result |
|--------|-------|-----------|--------|
| γ mean (sd) | 0.3397 (0.1335) | — | — |
| γ 95% CI | [0.0807, 0.6043] | — | — |
| γ bias | -0.1603 | — | — |
| γ relative bias | 0.3206 | < 0.3 | **FAIL** |
| γ CI covers true | True | Yes | PASS |
| γ CI excludes 0 | True | Yes | PASS |
| θ correlation | 0.8763 | > 0.9 | **FAIL** |
| θ RMSE | 0.3742 | < 0.2 | **FAIL** |
| Max R-hat | 1.0052 | < 1.01 | PASS |
| Divergent | 0 (0.0%) | < 1% | PASS |
| Min ESS | 1229.0 | — | — |
| Fit time | 486.7s | — | — |

**Overall: FAIL**
