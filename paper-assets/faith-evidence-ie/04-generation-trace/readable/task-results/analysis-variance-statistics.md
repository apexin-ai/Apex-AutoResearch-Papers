# analysis variance statistics

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_variance-statistics_20260523T012204_result.json`
- **Structured JSON:** [`ec9ef9931b0343b7d7f5.json`](../../sessions/ec/ec9ef9931b0343b7d7f5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results computed. Here's the final output:

---

## Sign test

4/4 scales: SFT_std > RSFT_std
- Binomial p-value (one-sided, H0: p≤0.5): **0.0625**
- Binomial p-value (two-sided): **0.1250**
- 14B excluded: n=1 for both SFT and RSFT, sample std undefined (ddof=1)
- Note: p=0.0625 is marginal. With 4 scales, even 4/4 cannot reach α=0.05 (minimum achievable = 2^{-4} = 0.0625). This is a power limitation of the sign test with small N, not evidence against the claim.

## χ² 95% CI for standard deviations

| Scale | n_SFT | SFT_std (pp) | SFT_std 95% CI (pp) | n_RSFT | RSFT_std (pp) | RSFT_std 95% CI (pp) | Compression |
|-------|-------|-------------|---------------------|--------|--------------|---------------------|-------------|
| 1.7B | 3 | 2.79 | [1.45, 17.55] | 3 | 0.09 | [0.04, 0.54] | 32.6× |
| 4B | 3 | 3.80 | [1.98, 23.89] | 3 | 0.51 | [0.27, 3.21] | 7.5× |
| 8B | 3 | 3.23 | [1.68, 20.31] | 3 | 0.50 | [0.26, 3.15] | 6.5× |
| LLaMA-8B | 3 | 2.92 | [1.52, 18.37] | 3 | 0.64 | [0.33, 4.01] | 4.6× |

CIs are wide (df=2 gives broad chi-squared tails), but 1.7B CIs are fully non-overlapping (SFT lower=1.45 > RSFT upper=0.54). For 4B/8B/LLaMA, SFT lower bound exceeds RSFT point estimate by 3-4×, though CIs technically overlap at the tails.

## Cohen's d (SFT mean vs RSFT mean)

| Scale | SFT_mean (pp) | RSFT_mean (pp) | Δ (pp) | pooled_std (pp) | Cohen's d | Effect |
|-------|--------------|----------------|--------|----------------|-----------|--------|
| 1.7B | 44.64 | 51.19 | +6.54 | 1.98 | +3.31 | large |
| 4B | 43.58 | 44.82 | +1.24 | 2.71 | +0.46 | small |
| 8B | 50.19 | 54.33 | +4.14 | 2.31 | +1.79 | large |
| LLaMA-8B | 51.09 | 56.54 | +5.45 | 2.12 | +2.58 | large |

Direction: positive d = RSFT mean > SFT mean. 3/4 scales show **large** effect (d>0.8), 4B shows **small** effect (d=0.46). All positive — RSFT consistently improves mean while compressing variance.

---

**Key caveat**: n=3 seeds per condition makes chi-squared CIs very wide and individual-scale significance tests underpowered. The strongest statistical argument is the **consistency across 4 independent scales** (sign test direction) combined with the **magnitude of compression** (4.6-32.6×), rather than any single-scale test.

---
