# analysis r17 p2 within sj rho and confounds

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r17_p2_within_sj_rho_and_confounds_20260517T075432_result.json`
- **Structured JSON:** [`0cf69548e3a9a0a46beb.json`](../../sessions/0c/0cf69548e3a9a0a46beb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 3 analyses completed. Results:

---

**Q3: Within-instance SJ-F1 ρ distribution (SciERC)**

| Statistic | Value |
|---|---|
| Valid instances | 440 / 551 (486 non-degenerate, 46 with zero variance filtered) |
| Mean ρ | 0.3226 |
| Median ρ | 0.5575 |
| Std | 0.6969 |
| **Negative ρ fraction** | **29.1% (128/440)** |

Distribution is bimodal: strong peak at ρ ∈ [0.87, 1.0] (148 instances) and a secondary peak at ρ ∈ [-1.0, -0.87) (52 instances). Nearly 30% of instances show negative SJ-F1 correlation, meaning higher consistency does *not* predict higher correctness at the instance level for a substantial minority.

---

**Q4: Entity-type frequency as confound (Few-NERD)**

| Correlation | ρ | p |
|---|---|---|
| Raw Spearman(degen, LP Δ) | -0.381 | 0.352 |
| Partial Spearman(degen, LP Δ \| n_instances) | -0.473 | 0.237 |
| Δ\|ρ\| | 0.092 | — |

Frequency is **not** a strong confound — the partial correlation (controlling for type frequency) is similar to the raw correlation (Δ = 0.09). The n=8 types means limited statistical power (all p > 0.2). The negative trend (higher degeneracy → lower LP benefit) actually strengthens slightly after partialing out frequency.

---

**Q6: Output space size vs degeneracy**

| Dataset | Degen% | Mean Unique (of 8) | Median | Std |
|---|---|---|---|---|
| SciERC | 11.8% | 3.42 | 3.0 | 1.73 |
| CoNLL | 49.6% | 2.25 | 2.0 | 1.88 |
| Few-NERD | 19.1% | 3.35 | 3.0 | 1.92 |

Expected inverse relationship confirmed: CoNLL (highest degeneracy) has lowest output diversity. SciERC and Few-NERD are similar in diversity despite different degeneracy rates.

Results saved to `output/r17_analyses/p2_supplementary.json`.

---
