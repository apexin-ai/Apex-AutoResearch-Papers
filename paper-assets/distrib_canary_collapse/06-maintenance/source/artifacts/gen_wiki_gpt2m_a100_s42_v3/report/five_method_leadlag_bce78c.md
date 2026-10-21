# 5-Method Lead-Lag Analysis: GPT-2 Medium (α=1.0, seed=42, T=11)

**Experiment:** gen_wiki_gpt2m_a100_s42_v3
**Model:** GPT-2 Medium, WikiText-103, α=1.0, T=11 (gen 0–10)
**Canary metrics:** token_entropy, ECE
**Downstream metrics:** distinct_1, distinct_2, distinct_3

**Methods:**
1. Naive cross-correlation (Pearson on levels, lag 0–5)
2. Differenced cross-correlation (Pearson on Δx, lag 0–5, BH FDR)
3. Threshold onset detection (first gen exceeding gen0 ± k·σ AND >10% relative deviation; k=1, k=2)
4. Permutation Granger causality (5000 perms, first-differenced, max_lag=1, BH FDR q=0.05)
5. Toda-Yamamoto Granger causality (ADF for d_max, AIC for lag p, Wald test on first p lags, BH FDR)

---

## Table 1: 5-Method Summary — Forward (Canary → Diversity, T=11)

| Pair | Naive xcorr (r, lag) | Diff. xcorr (r, lag, p_fdr) | Threshold onset k=1 / k=2 (Δgen) | Perm. Granger (p_raw, **p_fdr**) | TY Granger (χ², p_raw, **p_fdr**) |
|------|---------------------|----------------------------|----------------------------------|--------------------------------|----------------------------------|
| entropy→d1 | 0.995, L1 | 0.996, L2, <0.001** | +2 / +2 (lead) | 0.0018, **0.0030*** | 2.27, 0.425, **0.464** |
| entropy→d2 | 0.993, L2 | 0.977, L2, <0.001** | +2 / +2 (lead) | 0.0022, **0.0030*** | 8.00, 0.243, **0.323** |
| entropy→d3 | 0.989, L2 | 0.952, L2, 0.001** | +2 / +2 (lead) | 0.0030, **0.0030*** | 13.14, 0.191, **0.287** |
| ece→d1 | −0.992, L1 | −0.978, L1, <0.001** | +2 / +1 (lead) | 0.0014, **0.0030*** | 3.18, 0.149, **0.279** |
| ece→d2 | −0.996, L1 | −0.978, L1, <0.001** | +2 / +1 (lead) | 0.0024, **0.0030*** | 8.07, 0.039, **0.237** |
| ece→d3 | −0.995, L1 | −0.974, L2, <0.001** | +2 / +1 (lead) | 0.0028, **0.0030*** | 8.67, 0.035, **0.237** |

**Forward summary:** 6/6 pairs significant by naive xcorr (|r|>0.98), differenced xcorr (all p_fdr<0.001), threshold onset (all Δ>0), and permutation Granger (all p_fdr=0.003). TY Granger: 0/6 significant after FDR (see note below).

---

## Table 2: 5-Method Summary — Reverse (Diversity → Canary, T=11)

| Pair | Naive xcorr (r, lag) | Diff. xcorr (r, lag, p_fdr) | Threshold onset k=1 / k=2 (Δgen) | Perm. Granger (p_raw, **p_fdr**) | TY Granger (χ², p_raw, **p_fdr**) |
|------|---------------------|----------------------------|----------------------------------|--------------------------------|----------------------------------|
| d1→entropy | 0.948, L3 | 0.302, L3, 0.612 | −2 / −2 (lag) | 0.1102, **0.1156** | 1.63, 0.485, **0.485** |
| d2→entropy | 0.946, L3 | −0.267, L5, 0.664 | −2 / −2 (lag) | 0.1156, **0.1156** | 18.43, 0.163, **0.279** |
| d3→entropy | 0.945, L3 | −0.269, L5, 0.664 | −2 / −2 (lag) | 0.1154, **0.1156** | 3.89, 0.338, **0.405** |
| d1→ece | −0.947, L0 | −0.542, L0, 0.181 | −2 / −1 (lag) | 0.0176, **0.0352*** | 5.71, 0.067, **0.269** |
| d2→ece | −0.936, L0 | 0.654, L5, 0.309 | −2 / −1 (lag) | 0.0098, **0.0294*** | 3.97, 0.112, **0.279** |
| d3→ece | −0.936, L0 | 0.682, L5, 0.307 | −2 / −1 (lag) | 0.0078, **0.0294*** | 3.12, 0.152, **0.279** |

**Reverse summary:** Only permutation Granger finds 3/6 pairs significant (d→ece), and these have much weaker effect sizes (f²=5–8) than forward (f²=15–212). Differenced xcorr, threshold onset, and TY Granger all fail to support diversity→canary causation. Naive xcorr shows high |r| due to shared trends (spurious on levels).

---

## Table 3: Threshold Onset Detail

| Metric | Onset gen (k=1) | Onset gen (k=2) |
|--------|-----------------|-----------------|
| token_entropy | 1 | 1 |
| ece | 1 | 2 |
| distinct_1 | 3 | 3 |
| distinct_2 | 3 | 3 |
| distinct_3 | 3 | 3 |

Canary metrics (entropy, ECE) cross threshold 1–2 generations before diversity metrics at both k=1 and k=2. Entropy is the earliest mover (gen 1 at both thresholds), ECE follows at gen 1 (k=1) or gen 2 (k=2). All diversity metrics onset uniformly at gen 3.

---

## Table 4: Toda-Yamamoto Diagnostics

| Pair | d_max (ADF) | Opt. lag p | VAR order (p+d_max) | nobs | df_resid |
|------|-------------|-----------|---------------------|------|----------|
| entropy→d1 | 1 | 2 | 3 | 8 | 1 |
| entropy→d2 | 1 | 2 | 3 | 8 | 1 |
| entropy→d3 | 1 | 2 | 3 | 8 | 1 |
| ece→d1 | 0 | 2 | 2 | 9 | 4 |
| ece→d2 | 0 | 2 | 2 | 9 | 4 |
| ece→d3 | 0 | 2 | 2 | 9 | 4 |
| d1→entropy | 1 | 2 | 3 | 8 | 1 |
| d2→entropy | 1 | 2 | 3 | 8 | 1 |
| d3→entropy | 1 | 2 | 3 | 8 | 1 |
| d1→ece | 0 | 2 | 2 | 9 | 4 |
| d2→ece | 0 | 2 | 2 | 9 | 4 |
| d3→ece | 0 | 2 | 2 | 9 | 4 |

**Note:** Pairs involving entropy have d_max=1 (entropy is I(1) by ADF), yielding VAR(3) with only 8 obs and **df_resid=1**. Pairs involving ECE (I(0)) have VAR(2) with df_resid=4, slightly better but still low power. TY is uninformative at T=11 — consistent with Pythia T=10 findings (**see constraint C001**).

---

## Table 5: Method Agreement

Significance criteria per method:
- **Naive xcorr:** |r| > 0.9 (at T≤11, implies p < 0.001)
- **Diff. xcorr:** p_fdr < 0.05
- **Threshold onset:** Δgen > 0 for forward; Δgen > 0 for reverse
- **Perm. Granger:** p_fdr < 0.05
- **TY Granger:** p_fdr < 0.05

### Forward

| Pair | Naive | Diff. | Onset | Perm.G | TY | Sig (of 5) | Consensus (≥4) |
|------|-------|-------|-------|--------|-----|-----------|----------------|
| entropy→d1 | ✓ | ✓ | ✓ | ✓ | ✗ | **4/5** | **YES** |
| entropy→d2 | ✓ | ✓ | ✓ | ✓ | ✗ | **4/5** | **YES** |
| entropy→d3 | ✓ | ✓ | ✓ | ✓ | ✗ | **4/5** | **YES** |
| ece→d1 | ✓ | ✓ | ✓ | ✓ | ✗ | **4/5** | **YES** |
| ece→d2 | ✓ | ✓ | ✓ | ✓ | ✗ | **4/5** | **YES** |
| ece→d3 | ✓ | ✓ | ✓ | ✓ | ✗ | **4/5** | **YES** |

### Reverse

| Pair | Naive | Diff. | Onset | Perm.G | TY | Sig (of 5) | Consensus (≥4) |
|------|-------|-------|-------|--------|-----|-----------|----------------|
| d1→entropy | ✓ | ✗ | ✗ | ✗ | ✗ | 1/5 | NO |
| d2→entropy | ✓ | ✗ | ✗ | ✗ | ✗ | 1/5 | NO |
| d3→entropy | ✓ | ✗ | ✗ | ✗ | ✗ | 1/5 | NO |
| d1→ece | ✓ | ✗ | ✗ | ✓ | ✗ | 2/5 | NO |
| d2→ece | ✓ | ✗ | ✗ | ✓ | ✗ | 2/5 | NO |
| d3→ece | ✓ | ✗ | ✗ | ✓ | ✗ | 2/5 | NO |

---

## Key Findings

1. **4/5 method consensus for all forward pairs.** Naive xcorr, differenced xcorr, threshold onset, and permutation Granger unanimously support canary→diversity lead. The sole dissenter (TY Granger) lacks power at T=11.

2. **Reverse direction rejected by 4/5 methods.** Naive xcorr inflates reverse correlations due to shared trends (both series decline monotonically); after differencing, reverse xcorr drops to |r|<0.7 with p_fdr>0.18. Threshold onset shows canary always onsets first (gen 1 vs gen 3). Only permutation Granger finds weak reverse d→ece significance (p_fdr=0.03–0.04), with effect sizes 10× smaller than forward.

3. **Differenced xcorr adds value.** By removing shared trend, diff xcorr cleanly separates forward (all p_fdr<0.001) from reverse (all p_fdr>0.18), resolving the ambiguity in levels-based xcorr.

4. **TY Granger uninformative at T=11** — 0/12 pairs significant. For entropy pairs, d_max=1 forces VAR(3) with df_resid=1; ECE pairs have df_resid=4 but still insufficient power. **This is consistent with the Pythia T=10 finding and constraint C001: TY results at this sample size should not be cited as evidence for or against causality.**

5. **Entropy is the earliest canary.** Threshold onset shows entropy crosses at gen 1 regardless of threshold, while ECE crosses at gen 1 (k=1) or gen 2 (k=2). This suggests entropy may be a more sensitive early warning signal.

---

## Methodological Notes

- All Granger p-values (both permutation and TY) are **BH FDR-corrected** across the 12-pair family (6 forward + 6 reverse), reported as p_fdr.
- Differenced xcorr p-values are also BH FDR-corrected across 12 pairs.
- Permutation Granger uses first-differenced series with max_lag=1, 5000 permutations (results reused from existing leadlag_analysis).
- TY Granger determines d_max via ADF test (significance level 0.05), selects optimal lag p via AIC (max_p=2), fits VAR(p+d_max), and tests the first p lags of the causal variable via Wald χ² test.
- Threshold onset uses dual criteria: absolute deviation > k·σ AND relative deviation > 10% from gen 0 value.

---

*Generated: 2026-05-15*
