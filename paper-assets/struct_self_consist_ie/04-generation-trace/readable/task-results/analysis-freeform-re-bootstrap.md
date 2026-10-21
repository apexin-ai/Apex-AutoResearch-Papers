# analysis freeform re bootstrap

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_freeform_re_bootstrap_20260517T044401_result.json`
- **Structured JSON:** [`dab582bd0325466d4628.json`](../../sessions/da/dab582bd0325466d4628.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results:

**Free-form RE LP Selection (gold-non-empty, n=397)**
| Metric | Value |
|---|---|
| Point estimate | +2.35 pp |
| 95% CI | [0.24, 4.50] pp |
| Bootstrap p-value | 0.0250 |
| Cohen's d | 0.107 |
| Sign test | 45W / 45L / 307T (win rate 11.3%) |
| Wilcoxon p | 0.1327 |
| Conclusion | **Significant at α=0.05** (bootstrap) |

**Free-form RE LP Selection (all instances, n=551) — matches report's +1.69pp**
| Metric | Value |
|---|---|
| Point estimate | +1.69 pp |
| 95% CI | [0.18, 3.32] pp |
| Bootstrap p-value | 0.0272 |

Key observations:
- Bootstrap CI excludes zero in both cases → statistically significant at α=0.05.
- Wilcoxon is non-significant (p=0.13) because 77% of instances are tied (diff=0), and the sign test shows equal wins/losses (45/45). The gain comes from LP selection producing **larger improvements when it wins** vs **smaller degradations when it loses** — the mean of non-zero diffs is positive.
- Effect size is small (Cohen's d ≈ 0.1), consistent with the modest +1.69–2.35pp gap.

---
