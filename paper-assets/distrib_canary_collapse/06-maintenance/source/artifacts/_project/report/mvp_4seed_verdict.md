# MVP 4-Seed Formal Verdict Report

**Date:** 2026-05-14
**Seeds:** 42, 43, 44, 45
**Verdict: STRONG PASS**

---

## Pre-Analysis Decisions

| Check | Result |
|-------|--------|
| MAUVE floor effect (§4) | **Demoted** — Gen 0 MAUVE < 0.10 across all seeds, CV < 0.50 |
| effective_rank monotonicity (§3) | **Inconclusive** — slopes mixed: seed42=+0.81, seed43=-1.90, seed44=-2.11, seed45=+1.56 |

Active canary families for verdict: **token_entropy, self_bleu, ece** (3/4; effective_rank excluded)
Active downstream metrics: **perplexity, distinct_1, distinct_2, distinct_3** (4/5; mauve supplementary)

---

## Verdict Summary

| Count | Category |
|-------|----------|
| 6 | SIGNIFICANT LEAD |
| 1 | WEAK LEAD |
| 9 | NO LEAD |

**STRONG PASS**: 2 canary families (token_entropy, ece) each have ≥1 SIGNIFICANT LEAD pair.

---

## SIGNIFICANT LEAD Pairs (6)

### token_entropy → distinct_1
| Seed | Lag | |r| | p-value |
|------|-----|-----|---------|
| 42 | -1 | 0.993 | 0.0036 |
| 43 | -1 | 0.994 | 0.0028 |
| 44 | -1 | 0.998 | 0.0007 |
| 45 | -1 | 0.994 | 0.0006 |
**Mean lag: -1.0, std: 0.0** — Perfect consistency across all 4 seeds.

### token_entropy → distinct_2
| Seed | Lag | |r| | p-value |
|------|-----|-----|---------|
| 42 | -1 | 0.968 | 0.0231 |
| 43 | -1 | 0.970 | 0.0197 |
| 44 | -2 | 0.999 | 0.0001 |
| 45 | -1 | 0.970 | 0.0172 |
**Mean lag: -1.25, std: 0.43** — Low dispersion. Seed 44 shows lag=-2 with near-perfect correlation.

### token_entropy → distinct_3
| Seed | Lag | |r| | p-value |
|------|-----|-----|---------|
| 42 | -5 | 0.953 | 0.0224 |
| 43 | -1 | 0.941 | 0.0392 |
| 44 | -2 | 0.998 | 0.0001 |
| 45 | -1 | 0.942 | 0.0341 |
**Mean lag: -2.25, std: 1.64** — Higher dispersion. Seed 42 outlier at lag=-5; seeds 43/44/45 cluster at -1 to -2.

### ece → distinct_1
| Seed | Lag | |r| | p-value |
|------|-----|-----|---------|
| 42 | -2 | 0.998 | 0.0000 |
| 43 | -2 | 0.995 | 0.0000 |
| 44 | -4 | 0.996 | 0.0000 |
| 45 | -1 | 0.995 | 0.0010 |
**Mean lag: -2.25, std: 1.09** — All p-values near zero. Seed 44 shows larger lead (-4).

### ece → distinct_2
| Seed | Lag | |r| | p-value |
|------|-----|-----|---------|
| 42 | -1 | 0.996 | 0.0005 |
| 43 | -1 | 0.997 | 0.0001 |
| 44 | -1 | 0.995 | 0.0023 |
| 45 | -1 | 0.997 | 0.0002 |
**Mean lag: -1.0, std: 0.0** — Perfect consistency, strongest result in the dataset.

### ece → distinct_3
| Seed | Lag | |r| | p-value |
|------|-----|-----|---------|
| 42 | -5 | 0.991 | 0.0008 |
| 43 | -1 | 0.987 | 0.0013 |
| 44 | -1 | 0.998 | 0.0002 |
| 45 | -1 | 0.986 | 0.0023 |
**Mean lag: -2.0, std: 1.73** — Seed 42 outlier at -5; others at -1.

---

## WEAK LEAD Pair (1)

### token_entropy → perplexity
| Seed | Lag | |r| | p-value |
|------|-----|-----|---------|
| 42 | -5 | 0.812 | 0.1198 |
| 43 | -5 | 0.823 | 0.0849 |
| 44 | -5 | 0.837 | 0.0702 |
| 45 | -5 | 0.838 | 0.0580 |
**Mean lag: -5.0, std: 0.0** — Perfect lag consistency (all -5). Effect sizes moderate (|r| ~0.83). P-values borderline: seeds 43/44/45 approach p<0.10 but seed 42 fails. Note: 4-seed trend suggests more power would likely push this to significance.

---

## NO LEAD Pairs (9)

| Canary | Downstream | Reason |
|--------|-----------|--------|
| token_entropy | mauve | Seed 45 lag=+4 (direction reversal) |
| self_bleu | perplexity | Lag direction inconsistent across seeds |
| self_bleu | distinct_1 | Mean lag=+0.75 (canary lags downstream) |
| self_bleu | distinct_2 | Mean lag=+1.0 (canary lags downstream) |
| self_bleu | distinct_3 | Mean lag=+1.0 (canary lags downstream) |
| self_bleu | mauve | Direction inconsistent |
| ece | perplexity | Mean lag=+4.75 (ece LAGS perplexity) |
| ece | mauve | Direction inconsistent, weak correlation |
| effective_rank | all 5 | Excluded — inconclusive monotonicity |

---

## 4-Seed vs 2-Seed Pre-Analysis Comparison

| Finding | 2-Seed | 4-Seed | Change |
|---------|--------|--------|--------|
| Overall verdict | STRONG PASS | STRONG PASS | **Confirmed** |
| token_entropy → distinct_1 | SIGNIFICANT LEAD, lag=-1 | SIGNIFICANT LEAD, lag=-1 | Strengthened (seeds 44/45 confirm) |
| token_entropy → distinct_2 | SIGNIFICANT LEAD | SIGNIFICANT LEAD | Strengthened |
| token_entropy → distinct_3 | SIGNIFICANT LEAD (high dispersion) | SIGNIFICANT LEAD (lag_std=1.64) | Dispersion remains; seed 42 outlier identified |
| ece → distinct_1/2/3 | SIGNIFICANT LEAD | SIGNIFICANT LEAD | Strengthened |
| token_entropy → perplexity | WEAK LEAD | WEAK LEAD | Seeds 44/45 p-values trending toward significance |
| ece → perplexity | NO LEAD (ece lags) | NO LEAD (lag=+4.75) | Confirmed |
| self_bleu direction | Inconsistent | Inconsistent | Confirmed: self_bleu not a useful canary |
| effective_rank | Inconclusive | Inconclusive (worse: 2+/2- slopes) | Confirmed unreliable |
| Canary leads perplexity? | No (only diversity) | No (only diversity) | **Unchanged** |

### Key Takeaways from 4-Seed Expansion

1. **Core finding rock-solid**: Both token_entropy and ece reliably lead diversity metrics (distinct_1/2/3) by 1-2 generations. All 4 seeds confirm with |r| > 0.94 and p < 0.04.

2. **Canary-perplexity gap persists**: Canary metrics lead diversity collapse but NOT perplexity degradation. This is a fundamental insight — diversity loss and quality loss (perplexity) may operate on different timescales.

3. **distinct_3 lag dispersion**: Seed 42 consistently shows lag=-5 for both token_entropy and ece vs distinct_3, while other seeds show lag=-1 to -2. This may reflect a seed-specific sensitivity in trigram diversity.

4. **self_bleu is not a canary**: Confirmed across 4 seeds. It correlates with downstream but does not lead.

5. **effective_rank is noise**: 4 seeds make it worse (2 positive slopes, 2 negative). This metric lacks consistent directionality in the MVP setup.

---

## Rep44 Gen 10 Metrics (for Registry)

| Metric | Value |
|--------|-------|
| token_entropy | 1.2205 |
| ece | 0.4237 |
| perplexity | 1033.16 |
| distinct_1 | 0.0731 |
| distinct_2 | 0.3637 |
| distinct_3 | 0.6075 |
| effective_rank | 88.09 |
| self_bleu | 0.0129 |
| mauve | 0.0321 |
