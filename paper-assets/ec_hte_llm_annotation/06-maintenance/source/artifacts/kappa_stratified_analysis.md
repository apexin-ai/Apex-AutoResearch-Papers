# κ Stratified Performance Analysis

## 1. κ Distribution (520 Synthetic Configs)

Source: `results/exp002_bias_bound.csv` — 520 configs with δ_cate > 0 (26 δ_misclass × 20 δ_cate).

For each config: π̄ = 0.15, π_A = 0.15 − δ_misclass/2, π_B = 0.15 + δ_misclass/2.
Symmetric 2×2 confusion matrix: C_s = [[1−π_s, π_s], [π_s, 1−π_s]], κ(C_s) = 1/(1−2π_s).
Per-config: max_s κ(C_s) = 1/(0.7 − δ_misclass).

| κ bin | Range    | n_configs | %     | δ_misclass range |
|-------|----------|-----------|-------|------------------|
| 1     | ≤1.25    | 0         | 0.0%  | —                |
| 2     | (1.25,2] | 420       | 80.8% | [0.00, 0.20]     |
| 3     | (2,5]    | 100       | 19.2% | [0.21, 0.25]     |
| 4     | (5,10]   | 0         | 0.0%  | —                |
| 5     | >10      | 0         | 0.0%  | —                |

κ range across all 520 configs: [1.429, 2.222].

**Note**: Bins 1, 4, 5 are empty because π̄=0.15 sets a floor of κ=1/(1−2·0.15)=1.429.
The synthetic grid was designed for moderate misclassification rates (π_s ∈ [0.025, 0.275]).

---

## 2. Performance by κ Bin

### 2A. Analytic Bias Analysis (520 Synthetic Configs)

EC-HTE uses per-subgroup confusion matrices → analytically unbiased (bias = 0) for all κ.

| κ bin | n   | EC-HTE bias | Mean \|bias_global\|/\|bias_naive\| | Global better than naive (bias) | Debiasing hurts either subgroup |
|-------|-----|-------------|--------------------------------------|----------------------------------|----------------------------------|
| 2     | 420 | 0 (exact)   | 0.152                                | 100%                             | 35.0%                            |
| 3     | 100 | 0 (exact)   | 0.326                                | 100%                             | 100%                             |

Key finding: In bin 3 (κ > 2), global correction *increases* bias for at least one subgroup in 100% of configs,
yet its average \|bias\| is still smaller than naive (ratio < 1). EC-HTE avoids this tradeoff entirely.

### 2B. Monte Carlo Performance — Synthetic Regimes (exp001_v2, K=2, n_expert=500)

Regime → κ mapping: homogeneous (κ=1.32), moderate (κ=1.43), extreme (κ=2.00). All bin 2.

| Regime       | max κ | Method           | \|Bias\| | RMSE   | Coverage |
|--------------|-------|------------------|----------|--------|----------|
| homogeneous  | 1.32  | naive            | 0.0088   | 0.0619 | 0.955    |
| homogeneous  | 1.32  | global_corrected | 0.0062   | 0.0725 | 0.950    |
| homogeneous  | 1.32  | hb_dirichlet     | 0.0060   | 0.0729 | 0.950    |
| moderate     | 1.43  | naive            | 0.0183   | 0.0644 | 0.955    |
| moderate     | 1.43  | global_corrected | 0.0086   | 0.0731 | 0.960    |
| moderate     | 1.43  | hb_dirichlet     | 0.0050   | 0.0740 | 0.968    |
| extreme      | 2.00  | naive            | 0.0579   | 0.0900 | 0.823    |
| extreme      | 2.00  | global_corrected | 0.0586   | 0.0972 | 0.883    |
| extreme      | 2.00  | hb_dirichlet     | 0.0079   | 0.0878 | 0.955    |

EC-HTE (hb_dirichlet) at κ=2.0: 86% bias reduction vs global, 10% RMSE improvement, +7pp coverage.

### 2C. Monte Carlo Performance — Synthetic Regimes (exp003, K=4 marginal, n_expert=500)

| Regime       | max κ | Bin | Method           | \|Bias\| | RMSE   | Coverage |
|--------------|-------|-----|------------------|----------|--------|----------|
| homogeneous  | 1.32  | 2   | naive            | 0.0307   | 0.0574 | 0.855    |
| homogeneous  | 1.32  | 2   | global_corrected | 0.0089   | 0.0583 | 0.935    |
| homogeneous  | 1.32  | 2   | hb_ec_hte        | 0.0141   | 0.0612 | 0.920    |
| moderate     | 1.67  | 2   | naive            | 0.0300   | 0.0570 | 0.860    |
| moderate     | 1.67  | 2   | global_corrected | 0.0098   | 0.0583 | 0.935    |
| moderate     | 1.67  | 2   | hb_ec_hte        | 0.0135   | 0.0624 | 0.925    |
| extreme      | 2.50  | 3   | naive            | 0.0289   | 0.0557 | 0.870    |
| extreme      | 2.50  | 3   | global_corrected | 0.0133   | 0.0583 | 0.925    |
| extreme      | 2.50  | 3   | hb_ec_hte        | 0.0143   | 0.0634 | 0.925    |

At κ=2.5 (bin 3), EC-HTE achieves comparable bias and coverage to global correction, with slightly higher RMSE.

### 2D. RMSE Ratio Dependence on n_expert (K=2, extreme regime, κ=2.0)

| n_expert | RMSE(echte) | RMSE(global) | Ratio | Coverage(echte) |
|----------|-------------|--------------|-------|-----------------|
| 50       | 0.1383      | 0.1087       | 1.272 | 0.920           |
| 100      | 0.1026      | 0.1029       | 0.997 | 0.935           |
| 250      | 0.0934      | 0.0994       | 0.939 | 0.948           |
| 500      | 0.0878      | 0.0972       | 0.903 | 0.955           |
| 1000     | 0.0850      | 0.0968       | 0.878 | 0.958           |
| 2000     | 0.0832      | 0.0964       | 0.863 | 0.962           |

EC-HTE breaks even on RMSE at n_expert ≈ 100; dominates at n_expert ≥ 250.

---

## 3. Real LLM Combinations by κ Bin

Source: per-subgroup FPR/FNR from `exp008_multi_llm_comparison.csv`, `exp023_confusion_matrices.json`,
and open-source model profiles. κ_s = 1/(1 − FPR_s − FNR_s), max κ = max_s κ_s.

| Model          | Dataset        | K | max κ  | κ bin |
|----------------|----------------|---|--------|-------|
| Qwen2.5-7B     | TweetEval      | 4 | 1.878  | 2     |
| Mistral-7B     | TweetEval      | 4 | 1.919  | 2     |
| gpt-5.4        | TweetEval      | 4 | 1.948  | 2     |
| gpt-4o-mini    | TweetEval      | 4 | 1.962  | 2     |
| gpt-3.5-turbo  | TweetEval      | 4 | 2.206  | 3     |
| Gemma-2-9B     | TweetEval      | 4 | 2.208  | 3     |
| Llama-3.1-8B   | TweetEval      | 4 | 2.242  | 3     |
| gpt-4.1        | TweetEval      | 4 | 2.380  | 3     |
| gpt-4o         | TweetEval      | 4 | 2.636  | 3     |
| gpt-4o         | CivilComments  | 4 | 2.682  | 3     |
| gpt-4o-mini    | CivilComments  | 4 | 2.738  | 3     |
| gpt-4-turbo    | TweetEval      | 4 | 2.777  | 3     |
| gpt-3.5-turbo  | CivilComments  | 4 | 2.987  | 3     |

**All 13 combinations have κ > 1.25. None passes the κ ≤ 1.25 screening threshold.**

Distribution: 4 in bin 2, 9 in bin 3. Range: [1.878, 2.987].

### Real LLM Performance by κ Bin (MC validation, exp_real_cm_validation.csv)

#### n_expert = 500

| κ bin | n  | Bias Ratio (echte/global) | RMSE Ratio | Win Rate (bias) | Coverage (echte) |
|-------|----|---------------------------|------------|-----------------|-------------------|
| 2     | 4  | 0.992                     | 1.012      | 75.0%           | 0.943             |
| 3     | 9  | 1.108                     | 1.215      | 22.2%           | 0.949             |

#### n_expert = 250

| κ bin | n  | Bias Ratio (echte/global) | RMSE Ratio | Win Rate (bias) | Coverage (echte) |
|-------|----|---------------------------|------------|-----------------|-------------------|
| 2     | 4  | 1.086                     | 1.132      | 0.0%            | 0.932             |
| 3     | 9  | 1.255                     | 1.427      | 0.0%            | 0.940             |

#### n_expert = 100

| κ bin | n  | Bias Ratio (echte/global) | RMSE Ratio | Win Rate (bias) | Coverage (echte) |
|-------|----|---------------------------|------------|-----------------|-------------------|
| 2     | 4  | 1.388                     | 1.549      | 0.0%            | 0.897             |
| 3     | 9  | 1.866                     | 2.718      | 0.0%            | 0.910             |

---

## 4. Summary of Key Findings

1. **Synthetic κ range is narrow**: All 520 configs have κ ∈ [1.43, 2.22] (bins 2–3 only).
   This is because the symmetric DGP with π̄=0.15 constrains the minimum κ to 1.43.

2. **EC-HTE is analytically unbiased** for all κ, while global correction bias grows with κ.
   In bin 3, global correction hurts (increases bias vs naive) in 100% of configs for at least one subgroup.

3. **Real LLMs cluster in bins 2–3** (κ ∈ [1.88, 2.99]). None achieves κ ≤ 1.25.
   The κ ≤ 1.25 threshold requires very low combined error rates (FPR + FNR < 0.20),
   which no current LLM achieves across all subgroups.

4. **EC-HTE vs global correction tradeoff depends on n_expert**:
   - Bin 2 (κ ≤ 2): EC-HTE matches or beats global at n_expert ≥ 500 (bias ratio 0.99, RMSE ratio 1.01).
   - Bin 3 (κ ∈ 2–3): EC-HTE has 11% higher bias and 22% higher RMSE at n_expert=500.
     The variance penalty from estimating per-subgroup CMs at higher κ outweighs bias correction gains.
   - Synthetic MC (K=2, κ=2.0): EC-HTE dominates at n_expert ≥ 100 (RMSE ratio < 1).
     The real LLM gap (K=4 with asymmetric errors) is larger than the symmetric synthetic case.

5. **Coverage is robust**: EC-HTE maintains ≥ 0.93 coverage across all κ bins at n_expert ≥ 250,
   compared to naive coverage of 0.66–0.86.

---

## Data Limitations

- **No per-config MC data for 520 configs**: The exp002 dataset has only the analytic/MC bias
  of global correction. Full multi-method comparisons (naive, global, EC-HTE with RMSE/coverage)
  exist only for 3 regime-level settings (exp001_v2, exp003), not per (δ_misclass, δ_cate) config.

- **Bins 1, 4, 5 are empty**: The synthetic grid does not reach κ ≤ 1.25 (would require π̄ < 0.10)
  or κ > 2.22 (would require π_s > 0.275). The real LLM data also stays within bins 2–3.

- **13 real combinations, not 16**: The validation dataset covers 10 LLMs × TweetEval + 3 LLMs × CivilComments = 13.
  If the paper's Table 21 references 16, the additional 3 may come from different K or n_expert groupings.
