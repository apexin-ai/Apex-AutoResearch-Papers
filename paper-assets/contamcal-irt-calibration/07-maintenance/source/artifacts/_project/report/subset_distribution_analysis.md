# Subset Distribution Analysis: 300-item MMLU Subset

## Summary

The 300-item subset used for IRT fitting is a **random subsample** (seed=42) from the full 14,042 MMLU items. All statistical tests confirm the subset is representative of the full MMLU distribution across difficulty, domain, and RRF exposure dimensions.

## 1. Item Selection Mechanism

The 300 items are selected via `np.random.choice(14042, 300, replace=False)` with seed=42 in `run_pooled_rrf_irt.py:134-138`. RRF signals provide per-item *exposure scores* in the IRT model but do not influence item selection.

## 2. Difficulty Distribution

| Statistic | Full (N=14,042) | Subset (n=300) |
|-----------|----------------|----------------|
| Mean      | 0.5171         | 0.5100         |
| Std       | 0.3451         | 0.3522         |
| Median    | 0.5000         | 0.5000         |
| Q25       | 0.2500         | 0.2500         |
| Q75       | 0.7500         | 0.7500         |

**KS test**: D = 0.030, p = 0.946 (not significant)
**Cohen's d**: -0.020 (negligible effect)

Difficulty histogram (baseline accuracy bins):

| Bin         | Full % | Subset % | Δ     |
|-------------|--------|----------|-------|
| [0, 0.2)    | 18.3   | 21.3     | +3.0  |
| [0.2, 0.4)  | 17.5   | 13.7     | -3.8  |
| [0.4, 0.6)  | 22.9   | 24.3     | +1.4  |
| [0.6, 0.8)  | 21.7   | 21.0     | -0.7  |
| [0.8, 1.0]  | 19.6   | 19.7     | +0.0  |

## 3. Domain Distribution

| Domain          | Full %  | Subset % | Δ     | Full N | Sub N |
|-----------------|---------|----------|-------|--------|-------|
| Humanities      | 33.5    | 36.3     | +2.8  | 4,705  | 109   |
| Other           | 22.1    | 19.3     | -2.8  | 3,107  | 58    |
| STEM            | 22.5    | 23.3     | +0.9  | 3,153  | 70    |
| Social Sciences | 21.9    | 21.0     | -0.9  | 3,077  | 63    |

**Chi-square**: chi2 = 1.991, p = 0.574 (not significant)
**Cramer's V**: 0.047 (negligible effect)

## 4. Subject Coverage

- 52 of 57 MMLU subjects represented (91.2%)
- 5 missing subjects (all small, 100-173 items each): college_medicine, college_physics, econometrics, high_school_computer_science, jurisprudence
- Largest per-subject deviation: moral_scenarios (+4.3pp), professional_law (-3.3pp) — within expected sampling variance

## 5. RRF Exposure Score Distribution

| | Subset | Rest |
|---|--------|------|
| Mean | 0.0418 | 0.0425 |
| Std  | 0.0373 | 0.0374 |

**KS test**: D = 0.042, p = 0.664 (not significant)

The subset has essentially identical RRF exposure distributions to the remaining items, confirming no selection bias toward high- or low-exposure items.

## 6. Contrast: Hypothetical RRF Top-300 Selection

For comparison, if items were selected by highest aggregated RRF score (top-300), the subset would be significantly biased:
- **Domain**: chi2 = 31.6, p < 0.001 — Social Sciences overrepresented (34.7% vs 21.9%), STEM underrepresented (15.0% vs 22.5%)
- **Difficulty**: Cohen's d = 0.124 — slight shift toward easier items
- **Subject coverage**: only 47/57 subjects (82.5%)

This contrast confirms that random subsampling (our actual method) avoids the bias that signal-based selection would introduce.

## 7. Conclusion

The 300-item random subset is an unbiased representative sample of the full MMLU:
- **Difficulty**: KS p = 0.946, |d| = 0.020
- **Domain**: chi2 p = 0.574, V = 0.047
- **RRF exposure**: KS p = 0.664
- **Subject coverage**: 91.2% (52/57)

All effect sizes are negligible (<0.05). The subset faithfully preserves the distributional properties of the full benchmark.

## Files

- Analysis script: `cqa1:/root/contamcal-irt-calibration/analysis/subset_distribution_analysis.py`
- JSON results: `cqa1:/root/contamcal-irt-calibration/analysis/subset_distribution_results.json`
- Figure: `cqa1:/root/contamcal-irt-calibration/analysis/subset_distribution_analysis.png`
- Figure (PDF): `cqa1:/root/contamcal-irt-calibration/analysis/subset_distribution_analysis.pdf`
