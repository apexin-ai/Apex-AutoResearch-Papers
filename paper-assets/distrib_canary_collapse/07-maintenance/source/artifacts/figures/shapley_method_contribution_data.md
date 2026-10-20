# Leave-One-Out Method Contribution Analysis

## Setup
- Consensus rule: K>=3 out of 5 methods (full), K>=3 out of 4 (LOO)
- FPR computed at α=0.0 (null, 2 seeds × 8 pairs = 16 obs)
- FNR computed at α=1.0 (4 seeds × 8 pairs, cross-seed aggregated = 8 obs)
- Baseline: FPR=25.0%, FNR=0.0%

## Results

| Method           | ΔFPR     | ΔFNR     | Interpretation                        |
|-----------------|----------|----------|---------------------------------------|
| Naive XCorr     | -25.0%   | +25.0%   | Major FP driver, essential for sensitivity |
| Diff XCorr      | -25.0%   | +25.0%   | Major FP driver, essential for sensitivity |
| Threshold Onset | -6.2%    | +25.0%   | Minor FP contributor, essential for sensitivity |
| Perm Granger    | -18.8%   | 0.0%     | Pure FP filter, no sensitivity cost   |
| TY Granger      | 0.0%     | 0.0%     | Zero marginal contribution            |

## Key Findings
1. **Naive XCorr and Diff XCorr** are "double-edged": they drive both correct detections and false positives equally
2. **Threshold Onset** is primarily a sensitivity contributor with minimal FPR contribution (-6.2%)
3. **Perm Granger** acts as a pure false-positive filter: removing it reduces FPR by 18.8% without affecting sensitivity
4. **TY Granger** has zero marginal effect on consensus decisions (redundant with other methods)
5. The three correlation-based methods (naive, diff, threshold) are all individually essential for FNR=0% at α=1.0

## Figure Location
- Server: `docs/paper/figures/shapley_method_contribution.pdf` (and .png)
- Data source: `results/method_ablation_phase2_panel.json` + individual `5method_leadlag.json` files
