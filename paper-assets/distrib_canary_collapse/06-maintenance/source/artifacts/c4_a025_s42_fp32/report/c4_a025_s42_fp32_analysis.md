# c4_a025_s42_fp32 — 5-Method Lead-Lag Analysis

**Date:** 2026-05-19
**Model:** Pythia-410M | **Data:** C4 5k | **α=0.25** | **seed=42** | **fp32**
**Server:** westd-17855 | **Generations:** 11 (gen_0–gen_10)
**Parent:** c4_a050_s42_fp32 (PermG=8/8, K≥4=8/8)
**Analysis script:** `batch_analysis.py` (n_perm=5000, BH FDR α=0.05)

---

## 1. Lead-Lag Summary (8 pairs: {token_entropy, ece} × {distinct_1, distinct_2, distinct_3, mauve})

| Method                   | Significant / Total |
|--------------------------|:-------------------:|
| **permg_fwd_fdr**        | **0/8**             |
| **permg_rev_fdr**        | **0/8**             |
| **consensus_K3_3sigma**  | **8/8**             |
| **consensus_K4_3sigma**  | **3/8**             |
| threshold_onset_3sigma   | 8/8                 |
| naive_xcorr              | 8/8                 |
| diff_xcorr               | 8/8                 |
| ty_granger               | 3/8                 |

### Consensus K≥4 Detail (3 pairs)
| Pair                      | Votes | Methods                    |
|---------------------------|:-----:|----------------------------|
| token_entropy → mauve     | 4     | naive, diff, thresh, ty    |
| ece → distinct_1          | 4     | naive, diff, thresh, ty    |
| ece → distinct_2          | 4     | naive, diff, thresh, ty    |

### Consensus K≥3 Detail (all 8 pairs)
All 8 pairs reach K≥3 via {naive_xcorr, diff_xcorr, threshold_onset}.

### PermG Marginal Notes
PermG raw p-values before FDR: 0.031–0.093 (fwd), 0.028–0.250 (rev). Closest to surviving FDR: ece→mauve fwd (raw p=0.031, FDR-adjusted p=0.094). Signal present but below FDR threshold at T=11.

---

## 2. Drift Metrics (gen_0 → gen_10)

| Metric           | gen_0     | gen_10    | Δ%          |
|------------------|-----------|-----------|-------------|
| token_entropy    | 3.1094    | 1.4610    | **-53.01%** |
| ece              | 0.0122    | 0.4073    | +3242.80%   |
| perplexity       | 24.012    | 892.539   | +3617.05%   |
| distinct_1       | 0.1149    | 0.1102    | -4.10%      |
| distinct_2       | 0.5570    | 0.5081    | -8.78%      |
| distinct_3       | 0.8388    | 0.7385    | **-11.95%** |
| mauve            | 0.8286    | 0.3971    | **-52.08%** |
| effective_rank   | 68.752    | 145.683   | +111.90%    |

---

## 3. Comparison with Parent c4_a050_s42_fp32

| Method           | α=0.25 (this) | α=0.50 (parent) |
|------------------|:--------------:|:----------------:|
| permg_fwd_fdr    | 0/8            | 8/8              |
| permg_rev_fdr    | 0/8            | 7/8              |
| consensus_K3     | 8/8            | 8/8              |
| consensus_K4     | 3/8            | 8/8              |
| naive_xcorr      | 8/8            | 8/8              |
| diff_xcorr       | 8/8            | 8/8              |
| threshold_onset  | 8/8            | 8/8              |
| ty_granger       | 3/8            | 4/8              |

**Key difference:** PermG drops from 8/8 → 0/8 between α=0.50 and α=0.25. Correlation and threshold methods remain saturated at 8/8 in both conditions.

### Drift Comparison
| Metric         | α=0.25    | α=0.50    |
|----------------|-----------|-----------|
| token_entropy  | -53.01%   | -47.99%   |
| distinct_1     | -4.10%    | -9.78%    |
| mauve          | -52.08%   | -54.25%   |
| perplexity     | +3617.05% | +2931.59% |

α=0.25 shows *larger* canary drift (token_entropy, perplexity) but *smaller* diversity drift (distinct_1). Mauve drift is comparable.

---

## 4. Cross-Domain Onset Interpretation

### WikiText Reference
- α≤0.40: PermG=0/8 (blind spot)
- α=0.50: PermG=6/8 (onset)
- Onset interval: (0.40, 0.50]

### C4 Results
- α=0.25: PermG=0/8 (this experiment)
- α=0.50: PermG=8/8 (parent)
- Onset interval: (0.25, 0.50]

### Conclusion
PermG=0/8 at C4 α=0.25 does **not** support the hypothesis that C4 onset is strictly lower than WikiText. Both domains show PermG onset ∈ (0.25–0.50]. The intervals overlap and cannot be separated without additional data points (e.g., C4 α=0.30, 0.35, 0.40).

However, the 8/8 detection by correlation/threshold methods at C4 α=0.25 is noteworthy — these weaker methods DO detect the canary→diversity lead-lag pattern even though PermG cannot. This suggests a real but subtle signal below PermG's detection threshold at T=11.

**Interpretation:** The result is a "success" in both senses — it establishes that C4's PermG onset is above 0.25, consistent with WikiText's pattern. The cross-domain onset comparison remains unresolved pending finer-grained α experiments in the (0.25, 0.50) range.

---

## 5. Registry Update Recommendation

```json
{
  "metrics": {
    "permg_fwd_fdr": "0/8",
    "permg_rev_fdr": "0/8",
    "consensus_K3_3sigma": "8/8",
    "consensus_K4_3sigma": "3/8",
    "threshold_onset_3sigma": "8/8",
    "naive_xcorr": "8/8",
    "diff_xcorr": "8/8",
    "ty_granger": "3/8",
    "drift_token_entropy": "-53.01%",
    "drift_ece": "+3242.80%",
    "drift_perplexity": "+3617.05%",
    "drift_d1": "-4.10%",
    "drift_d2": "-8.78%",
    "drift_d3": "-11.95%",
    "drift_mauve": "-52.08%",
    "drift_effective_rank": "+111.90%"
  },
  "conclusion": "PermG=0/8 at C4 α=0.25: canary→diversity lead-lag not detected by strictest test (FDR-corrected permutation Granger). Correlation/threshold methods detect 8/8. C4 PermG onset ∈ (0.25, 0.50], overlapping WikiText onset ∈ (0.40, 0.50]. Cross-domain onset cannot be separated without finer α grid. Collapse dynamics present (token_entropy -53%, mauve -52%) but PermG power insufficient at this α.",
  "status": "success"
}
```
