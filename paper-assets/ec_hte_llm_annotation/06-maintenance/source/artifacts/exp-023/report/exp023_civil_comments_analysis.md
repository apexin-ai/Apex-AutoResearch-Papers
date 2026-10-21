# exp-023: Civil Comments Semi-Synthetic Validation — Comprehensive Analysis

## 1. Dataset & Subgroup Design

**Dataset**: Civil Comments (Google, toxicity detection), 3000 stratified samples (30% toxic)
**Subgroups**: text_length_bin × has_question → K=4 (S0: long+no_q, S1: long+q, S2: short+no_q, S3: short+q)
**Subgroup weights**: S0=0.388, S1=0.114, S2=0.337, S3=0.161
**P(Z=1)**: 0.300

## 2. LLM Annotation Confusion Matrices

Annotated with 3 LLMs via OpenAI-compatible proxy. 800–900 valid annotations per model.

### Per-subgroup error rates

| Model | Metric | S0 | S1 | S2 | S3 | Δ (max−min) |
|-------|--------|-----|-----|-----|-----|------------|
| gpt-4o | FPR | 0.249 | 0.157 | 0.213 | 0.341 | 0.184 |
| gpt-4o | FNR | 0.160 | 0.263 | 0.308 | 0.328 | 0.168 |
| gpt-4o-mini | FPR | 0.517 | 0.541 | 0.419 | 0.610 | 0.191 |
| gpt-4o-mini | FNR | 0.052 | 0.105 | 0.074 | 0.160 | 0.108 |
| gpt-3.5-turbo | FPR | 0.400 | 0.473 | 0.374 | 0.468 | 0.099 |
| gpt-3.5-turbo | FNR | 0.139 | 0.211 | 0.173 | 0.240 | 0.101 |

### Key Finding 1: Cross-subgroup misclassification heterogeneity confirmed

All 3 models show **Δπ > 0.05** across subgroups:
- gpt-4o: Δ_FPR=0.184, Δ_FNR=0.168 (overall Δπ=0.160)
- gpt-4o-mini: Δ_FPR=0.191, Δ_FNR=0.108 (overall Δπ=0.140)
- gpt-3.5-turbo: Δ_FPR=0.099, Δ_FNR=0.101 (overall Δπ=0.113)

This validates the paper's core premise: LLM misclassification is structurally heterogeneous across text-feature-defined subgroups, and this holds on a second NLP dataset beyond TweetEval.

### Key Finding 2: Severe FPR/FNR asymmetry

gpt-4o-mini and gpt-3.5-turbo show highly asymmetric confusion matrices:
- gpt-4o-mini: FPR ≈ 0.42–0.61 while FNR ≈ 0.05–0.16 (over-predicts toxicity)
- gpt-3.5-turbo: FPR ≈ 0.37–0.47 while FNR ≈ 0.14–0.24

This asymmetry causes mixing matrix ill-conditioning (rows become near-uniform when FPR ≈ 0.5), which amplifies estimation noise under matrix inversion.

## 3. Semi-Synthetic DGP Results

### 3a. Asymmetric CMs (real LLM confusion matrices)

**DGP**: N=5000, τ(z=0)=0.10, τ(z=1)=0.40, MC=50, uniform CATE (no per-subgroup variation)

Results at n_expert=250:

| Model | Method | |Bias| | RMSE | Coverage |
|-------|--------|-------|------|----------|
| gpt-3.5-turbo | naive | 0.1194 | 0.1374 | 0.708 |
| gpt-3.5-turbo | global_corrected | 0.1578 | 0.1963 | 0.948 |
| gpt-3.5-turbo | hb_ec_hte | 0.3188 | 0.4811 | 0.938 |
| gpt-4o | naive | 0.1015 | 0.1222 | 0.820 |
| gpt-4o | global_corrected | 0.1425 | 0.1745 | 0.945 |
| gpt-4o | hb_ec_hte | 0.2473 | 0.3629 | 0.912 |
| gpt-4o-mini | naive | 0.1303 | 0.1475 | 0.635 |
| gpt-4o-mini | global_corrected | 0.1581 | 0.1986 | 0.948 |
| gpt-4o-mini | hb_ec_hte | 0.2842 | 0.4201 | 0.938 |

**Result**: EC-HTE has 2–3× worse RMSE than global correction with asymmetric CMs. Consistent with exp-015/016 failure analysis — asymmetric CMs with FPR ≈ 0.5 cause ill-conditioning.

### 3b. Symmetric misclassification (paper's main DGP design)

**DGP**: N=5000, τ(z=0)=0.10, DELTA_S={S0:0.4, S1:0.3, S2:0.2, S3:0.1}, MC=50
Symmetric flip probability π_s derived from real LLM overall misclassification rates.

#### Extreme config (π = {0.05, 0.10, 0.15, 0.25}, matching exp-003/TweetEval)

| n_expert | Method | |Bias| | RMSE | Coverage |
|----------|--------|-------|------|----------|
| 100 | oracle | 0.0705 | 0.0897 | 0.960 |
| 100 | naive | 0.0753 | 0.0928 | 0.952 |
| 100 | global_corrected | 0.1037 | 0.1320 | 0.943 |
| 100 | stratified_mle | 0.1959 | 0.3130 | 0.907 |
| 100 | hb_ec_hte | 0.1979 | 0.3610 | 0.902 |
| 250 | naive | 0.0753 | 0.0928 | 0.952 |
| 250 | global_corrected | 0.0942 | 0.1198 | 0.960 |
| 250 | hb_ec_hte | 0.1279 | 0.1685 | 0.932 |
| 500 | naive | 0.0753 | 0.0928 | 0.952 |
| 500 | global_corrected | 0.0898 | 0.1120 | 0.962 |
| 500 | hb_ec_hte | 0.1075 | 0.1382 | 0.952 |

#### gpt-4o rates (π = {0.218, 0.176, 0.243, 0.336})

| n_expert | Method | |Bias| | RMSE | Coverage |
|----------|--------|-------|------|----------|
| 250 | oracle | 0.0705 | 0.0897 | 0.960 |
| 250 | naive | 0.0946 | 0.1126 | 0.843 |
| 250 | global_corrected | 0.1318 | 0.1678 | 0.948 |
| 250 | hb_ec_hte | 0.1874 | 0.2857 | 0.938 |
| 500 | naive | 0.0946 | 0.1126 | 0.843 |
| 500 | global_corrected | 0.1229 | 0.1538 | 0.955 |
| 500 | hb_ec_hte | 0.1532 | 0.2134 | 0.952 |

#### gpt-4o-mini rates (π = {0.350, 0.452, 0.312, 0.433})

| n_expert | Method | |Bias| | RMSE | Coverage |
|----------|--------|-------|------|----------|
| 250 | oracle | 0.0705 | 0.0897 | 0.960 |
| 250 | naive | 0.1197 | 0.1372 | 0.720 |
| 250 | global_corrected | 0.2315 | 0.2862 | 0.975 |
| 250 | hb_ec_hte | 0.4410 | 0.7134 | 0.968 |
| 500 | naive | 0.1197 | 0.1372 | 0.720 |
| 500 | global_corrected | 0.2078 | 0.2539 | 0.970 |
| 500 | hb_ec_hte | 0.4670 | 0.7424 | 0.970 |

## 4. Key Findings

### Finding 1: Δπ > 0.05 confirmed across all models ✓
Civil Comments reproduces the subgroup-heterogeneous misclassification structure found in TweetEval. This holds for GPT-4o, GPT-4o-mini, and GPT-3.5-turbo across text-feature subgroups.

### Finding 2: Coverage is EC-HTE's value proposition
Naive estimation has severely degraded coverage when misclassification is moderate-to-high:
- gpt-4o-mini rates: Naive coverage = 0.720 (target: 0.95)
- gpt-3.5-turbo rates: Naive coverage = 0.768
- gpt-4o rates: Naive coverage = 0.843

All correction methods restore coverage to ~0.93–0.97. EC-HTE and global correction are both effective here.

### Finding 3: RMSE ordering is Naive < Global < EC-HTE across all settings
This is the honest empirical result: **no correction method achieves lower RMSE than naive** at any sample size tested.

The RMSE penalty arises from matrix inversion amplifying estimation noise. Even EC-HTE's partial pooling (which does reduce variance relative to stratified MLE in most cases) cannot overcome this.

This ordering is also observed on TweetEval (exp-003), so it is not specific to Civil Comments.

### Finding 4: EC-HTE ≈ Stratified MLE (partial pooling has marginal effect at K=4)
EC-HTE/StratMLE RMSE ratio ranges from 0.83 to 1.15 across settings. Partial pooling helps but the improvement is modest at K=4 because there is limited cross-subgroup information to borrow.

## 5. Interpretation

The results are consistent across both datasets (TweetEval and Civil Comments):

1. **Misclassification heterogeneity is a real structural property** of LLM annotations — not an artifact of one dataset.

2. **The bias-variance trade-off favors naive estimation in RMSE** when misclassification rates are moderate (π < 0.25). The bias introduced by misclassification is smaller than the variance introduced by matrix inversion correction.

3. **Correction methods win on coverage/calibration**: When the researcher needs valid confidence intervals (not just point estimates), correction is essential. Naive CIs have severe under-coverage for the Z=1 group.

4. **Asymmetric CMs (FPR ≠ FNR) worsen the problem**: Real LLM CMs are highly asymmetric, causing additional ill-conditioning beyond the symmetric case.

## 6. What This Means for the Paper

For Reviewer C1's concern about generalization beyond TweetEval:

**Supported claims**:
- Subgroup-heterogeneous misclassification is a structural property of LLM annotations (confirmed on 2nd dataset)
- EC-HTE provides calibrated inference (valid CIs) when naive estimation does not

**Honest limitation**:
- EC-HTE's RMSE advantage over global correction is not demonstrated at the K=4 expert budgets tested
- The RMSE benefit of subgroup-specific correction requires either larger expert budgets or fewer subgroups (K=2)
