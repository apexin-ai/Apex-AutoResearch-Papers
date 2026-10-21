# exp-007: OLMo-1B Bootstrap CI (Rerun Data)

## Config
- **Data**: `data/exp_olmo1b_c4_rerun/features.csv` (30,000 samples, depth 0-5, Qwen-1.5B scorer)
- **Method**: GroupKFold(5) OOF + doc-level bootstrap (B=10,000) + label permutation (10,000)
- **Theta**: 0.60
- **Seed**: 42

## Results

| Pair | AUC   | 95% CI            | CI width | Perm p   | CI_lower > theta |
|------|-------|-------------------|----------|----------|------------------|
| 0v1  | 0.986 | [0.9843, 0.9877]  | 0.0034   | 0.0001   | True             |
| 1v2  | 0.507 | [0.4962, 0.5188]  | 0.0226   | 0.0955   | False            |
| 2v3  | 0.497 | [0.4855, 0.5085]  | 0.0230   | 0.6894   | False            |
| 3v4  | 0.502 | [0.4905, 0.5134]  | 0.0229   | 0.3631   | False            |
| 4v5  | 0.494 | [0.4827, 0.5057]  | 0.0230   | 0.8357   | False            |

## K* Determination

**K* = 1** (CI-based, theta=0.60)

- 0v1: CI lower (0.9843) > theta (0.60) => depth 0 vs 1 distinguishable
- 1v2: AUC=0.507, CI spans 0.50 => depth 1 vs 2 indistinguishable (as expected)
- All deeper pairs: AUC ~0.50, CIs all contain 0.50

## Comparison with Old Data

| Metric    | Old (K*=2) | Rerun (K*=1) |
|-----------|-----------|--------------|
| 1v2 AUC   | ~0.62     | 0.507        |
| K*        | 2         | 1            |

The rerun confirms K*=1 for OLMo-1B. The 1v2 CI [0.496, 0.519] comfortably contains 0.50, consistent with the standardized pipeline result (AUC_1v2=0.508).

## Output
- Server JSON: `results/exp007_olmo_rerun/bootstrap_ci_olmo_rerun.json`
- Runtime: 307.6s
