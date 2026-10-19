# MVP Phase 1 Results — CodeQL Feasibility + H2 Sanity Check

## Conclusion: PASS (both H1 and H2)

## Phase 1a: CodeQL Pilot — PASS

| Instance | DB(s) | CG(s) | DF(s) | Reachable Files | Status |
|---|---|---|---|---|---|
| flask-4045 | 0 | 7.0 | 11.6 | 15/83 | OK |
| requests-1963 | 0 | 7.4 | 12.5 | 9/37 | OK |
| pytest-11143 | 0 | 9.3 | 17.7 | 41/262 | OK |
| pylint-5859 | 0 | 22.9 | 35.5 | 36/2366 | OK |
| xarray-3364 | 0 | 2.2 | 2.3 | 1/236 | OK |
| astropy-12907 | 0 | 24.6 | 28.5 | 20/995 | OK |
| sphinx-10325 | 0 | 16.4 | 31.1 | 131/774 | OK |
| matplotlib-18869 | 43 | 119.8 | 167.1 | 164/912 | OK |

- **Timeout rate: 0%** (threshold <30%)
- CG mean: 29.6s, max: 119.8s
- DF mean: 43.4s, max: 167.1s
- 2 repos skipped (seaborn, scikit-learn: buggy file not found)

## H2 Sanity Check — PASS

- Connected files coverage: **1.44%**
- Disconnected files coverage: **0.00%**
- Fisher exact test: OR=inf, **p=0.0000**
- 6/8 repos have gold patch in connected set (75%)