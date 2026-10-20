# Natural Experiment: Base→Chat Δlz* Cross-Benchmark Analysis

## Overview
- **Pairs**: 21 base/chat model pairs
- **Benchmarks**: MMLU, HellaSwag, ARC-Challenge, GSM8K
- **Complete pairs** (all benchmarks): 9/21

## Hypothesis
Instruction-tuning produces a consistent cross-benchmark Δlz* shift.
Contamination on specific benchmarks manifests as outlier Δlz* on those
benchmarks relative to the pair's mean Δlz* across benchmarks.

## IRT Fitting Summary
- **MMLU**: 63 models × 14042 items, 3PL (c=0.25), a∈[0.01, 5.00], b∈[-6.00, 6.00]
- **HellaSwag**: 57 models × 10042 items, 3PL (c=0.25), a∈[0.01, 5.00], b∈[-6.00, 6.00]
- **ARC-Challenge**: 57 models × 1172 items, 3PL (c=0.25), a∈[0.01, 5.00], b∈[-6.00, 6.00]
- **GSM8K**: 45 models × 1319 items, 2PL (c=0.0), a∈[0.16, 5.00], b∈[-0.49, 6.00]

## lz* Distribution Per Benchmark
- **MMLU**: mean=11.69, std=6.68, range=[-5.88, 23.37]
- **HellaSwag**: mean=12.53, std=9.61, range=[-7.89, 35.91]
- **ARC-Challenge**: mean=6.30, std=2.79, range=[-2.23, 12.53]
- **GSM8K**: mean=-0.32, std=3.42, range=[-12.01, 4.53]

## Δlz* Across Benchmarks
- **MMLU**: mean Δlz*=-1.32 ± 5.12, mean Δacc=+0.0395
- **HellaSwag**: mean Δlz*=-6.82 ± 5.56, mean Δacc=-0.0105
- **ARC-Challenge**: mean Δlz*=-3.87 ± 2.45, mean Δacc=+0.0068
- **GSM8K**: mean Δlz*=+0.43 ± 1.20, mean Δacc=+0.0284

## Deviation Analysis
For each pair, Δlz* deviation = Δlz*(benchmark) − mean Δlz*(pair).
A positive deviation means lz* increased more on this benchmark than average.

### Per-Benchmark Deviation (one-sample t-test, H0: mean=0)
- **MMLU**: mean_dev=+1.167, t(15)=+1.52, p=0.1502
- **HellaSwag**: mean_dev=-3.401, t(14)=-3.97, p=0.0014 **significant at p<0.05**
- **ARC-Challenge**: mean_dev=-0.458, t(14)=-0.91, p=0.3778
- **GSM8K**: mean_dev=+3.922, t(9)=+3.35, p=0.0085 **significant at p<0.05**

### Outlier Pairs (|within-pair z| > 1.5)
- None detected

## Interpretation

### Key Findings
1. Benchmarks with significant systematic deviation: **HellaSwag, GSM8K**
2. 0 (pair, benchmark) combinations flagged as outliers (|z| > 1.5).

### Caveats
- lz* values are systematically miscalibrated (mean >> 0) due to model violations
  of IRT assumptions. However, Δlz* deviations within pairs should be interpretable
  since systematic bias cancels.
- With only 4 benchmarks per pair, within-pair z-scores have very few degrees of freedom.
- IRT parameters fitted on ~60 models may not generalize perfectly.
- Runtime: 924s

## Files
- `pairs_data.csv`: Per (pair, benchmark) raw data
- `deviation_analysis.csv`: Deviation analysis
- `delta_lz_heatmap.png`: Δlz* heatmap
- `deviation_heatmap.png`: Deviation heatmap
- `benchmark_boxplot.png`: Per-benchmark deviation boxplot
- `delta_acc_vs_lz.png`: Δacc vs Δlz* scatter
- `natural_experiment_summary.json`: Full statistics