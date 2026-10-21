# analysis exp 013 014 voting baselines

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_013_014_voting_baselines_20260514T111404_result.json`
- **Structured JSON:** [`88cf0371b4328d9bf9ed.json`](../../sessions/88/88cf0371b4328d9bf9ed.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. Here's the consolidated results:

---

### exp-013 Exact-Match Voting Rate (negative)

```
=== Confidence Signal Comparison (NER, Full Set, n=529) ===
Signal               | ρ_spearman |  p-value   | τ_kendall  | AUROC
soft_jaccard         |    +0.3825 |   7.08e-20 |    +0.2810 | 0.6897
fleiss_kappa         |    +0.2590 |   1.47e-09 |    +0.1921 | 0.6247
exact_match_rate     |    +0.2941 |   5.12e-12 |    +0.2181 | 0.6398

=== Confidence Signal Comparison (RE, Full Set, n=397) ===
soft_jaccard         |    +0.2441 |   8.55e-07 |    +0.1831 | 0.6275
fleiss_kappa         |    +0.2782 |   1.72e-08 |    +0.2144 | 0.6484
exact_match_rate     |    +0.1562 |   1.80e-03 |    +0.1185 | 0.5863
```

EM 在 NER 上介于 SJ 和 FK 之间，在 RE 上最弱。粒度太粗，不如 element-level 信号。

### exp-014 Entity Majority Voting (success)

```
=== Confidence Signal Comparison (NER, Full Set, n=529) ===
Signal               | ρ_spearman |  p-value   | τ_kendall  | AUROC
soft_jaccard         |    +0.3825 |   7.08e-20 |    +0.2810 | 0.6897
fleiss_kappa         |    +0.2590 |   1.47e-09 |    +0.1921 | 0.6247
voting_confidence    |    +0.3915 |   8.10e-21 |    +0.2906 | 0.7039  ← BEST

=== Confidence Signal Comparison (RE, Full Set, n=397) ===
soft_jaccard         |    +0.2441 |   8.55e-07 |    +0.1831 | 0.6275
fleiss_kappa         |    +0.2782 |   1.72e-08 |    +0.2144 | 0.6484
voting_confidence    |    +0.3403 |   3.21e-12 |    +0.2560 | 0.6668  ← BEST

=== Selection Strategy Comparison ===
                     | NER Mean F1 | RE Mean F1
greedy (T=0)         |   0.6483    |   0.4022
majority_voting      |   0.6246    |   0.3577
oracle (best-of-N)   |   0.7793    |   0.5886
```

**voting_confidence 在 NER 和 RE 上都超过了 SJ，是目前发现的最强 correlation signal。** 但 majority voting 作为 selection strategy 不如 greedy — voting 更适合做 confidence estimation 而非 output construction。

产出文件：
- `code/analyze_exact_match_voting.py`
- `code/analyze_entity_voting.py`
- `output/mvp_pilot_004/exp013_exact_match_report.json`
- `output/mvp_pilot_004/exp014_entity_voting_report.json`

---
