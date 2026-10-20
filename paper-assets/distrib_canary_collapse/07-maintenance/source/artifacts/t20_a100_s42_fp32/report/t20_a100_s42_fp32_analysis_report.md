# T=20 α=1.0 s42 fp32 — 5-Method Analysis Report

**Experiment**: t20_a100_s42_fp32 | Pythia-410M | WikiText | α=1.0 | seed=42 | T=20 (21 gens) | 5000 steps/gen
**Server**: westd-17855 | **Analysis date**: 2026-05-20
**Script**: run_5method_analysis_d102.py (D120 fix)

---

## Training Final Metrics (Gen 20)

| Metric | Value |
|--------|-------|
| Perplexity | 2041.50 |
| Token Entropy | 1.2052 |
| Effective Rank | 94.4 |
| MAUVE | 0.0341 |
| EXIT_CODE | 0 |

---

## 5-Method Forward Significance

| Method | Fwd Sig | /8 |
|--------|---------|-----|
| Naive XCorr | 8 | 8 |
| Diff XCorr (FDR) | 6 | 8 |
| Threshold Onset (3σ D105) | 6 | 8 |
| PermG (FDR) | 6 | 8 |
| TY Granger | 1 | 8 |

Reverse: PermG rev FDR = **0/8** (strong directionality)

---

## Consensus (Robust Pairs)

| Pair | Votes | Methods |
|------|-------|---------|
| token_entropy → distinct_1 | 4/5 | naive, diff, threshold, perm |
| token_entropy → distinct_2 | 4/5 | naive, diff, threshold, perm |
| token_entropy → distinct_3 | 4/5 | naive, diff, threshold, perm |
| token_entropy → mauve | 1/5 | naive |
| ece → distinct_1 | **5/5** | naive, diff, threshold, perm, ty |
| ece → distinct_2 | 4/5 | naive, diff, threshold, perm |
| ece → distinct_3 | 4/5 | naive, diff, threshold, perm |
| ece → mauve | 1/5 | naive |

- **K≥3: 6/8** | **K≥4: 6/8** | K=5: 1/8
- mauve pairs consistently fail (both canaries) — same pattern as T=10

---

## Power Theory Prediction Verification

| Metric | Predicted | Observed | Match |
|--------|-----------|----------|-------|
| PermG count | 7/8 | **6/8** | within_range ✓ |
| Rate | 0.832 | **0.750** | within_ci ✗ (CI: [0.76, 0.96]) |
| T=10 baseline | 6/8 | 6/8 | Δ = 0 |

Observed rate 0.75 is **barely below** the 95% CI lower bound (0.76). The √T Power Theory predicted that T=20 would yield higher PermG than T=10, but both produce 6/8. The count matches the predicted range lower bound [6, 8].

---

## Interpretation

1. **Collapse signal strong at α=1.0**: 6/8 pairs show robust forward causation (K≥3), with 0/8 reverse PermG — clean directionality.
2. **No T-scaling benefit observed**: T=20 yields identical PermG to T=10 (both 6/8). The mauve pairs remain non-significant regardless of series length.
3. **mauve resistance**: Both canary→mauve pairs fail all methods except naive xcorr, consistent with known mauve noise floor at small sample sizes.
4. **TY limited**: Only 1/8 TY significant (ece→distinct_1), consistent with known TY instability at moderate T.
5. **Conclusion**: **NEGATIVE_MARGINAL** — Power Theory √T prediction not confirmed. Observed at range lower bound, rate below CI. The extra 10 generations provided no additional statistical power for the 2 resistant (mauve) pairs.
