# ops ht acc zscore recompute

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_ht-acc-zscore-recompute_20260523T012227_result.json`
- **Structured JSON:** [`a47ca7865e6789ea579e.json`](../../sessions/a4/a47ca7865e6789ea579e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Sanity check passed, all 4 values match. Results:

```
SANITY CHECK (seed 42):
HT 15%: orig=7.26, recalc=7.26  [MATCH]
HT 50%: orig=1.66, recalc=1.66  [MATCH]
Acc z 15%: orig=42.3, recalc=42.3  [MATCH]
Acc z 50%: orig=68.7, recalc=68.7  [MATCH]

HT Cohen's |d|:        15%        25%        50%
s1 (seed42):           7.26       8.90       1.66
s2 (seed123):          5.52       9.51       5.80
s3 (seed456):          4.72       5.10       8.41
Mean:                  5.83       7.84       5.29
SD:                    1.30       2.39       3.41

Acc z Cohen's |d|:     15%        25%        50%
s1 (seed42):           42.3       49.8       68.7
s2 (seed123):          47.3       53.4       70.8
s3 (seed456):          45.4       51.3       70.4
Mean:                  45.0       51.5       70.0
SD:                     2.5        1.8        1.1
```

Key observations:
- **Acc z-score** Cohen's d is very stable across seeds (small SD), monotonically increasing with contamination level
- **HT** Cohen's d shows much higher variance across seeds (SD up to 3.41), and the non-monotonic pattern in seed 42 (15% > 50%) does **not** hold for seeds 123 and 456 — it's an artifact of that single seed
- Results saved to `/root/autodl-tmp/ctrl_contam_pilot/results/multiseed_ht_accz_cohens_d.json`

---
