# code r1 32b selectivity raw features

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_r1_32b_selectivity_raw_features_20260517T133358_result.json`
- **Structured JSON:** [`e8f45b970243af2a828e.json`](../../sessions/e8/e8f45b970243af2a828e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results:

| Metric | Value |
|--------|-------|
| Feature type | raw 5120-d (no PCA) |
| Baseline selectivity | 7.6pp (real=0.584, random=0.508) |
| Bootstrap mean | 8.4pp |
| Bootstrap std | 6.7pp |
| 95% CI | [-3.9, 22.7]pp |
| p-value (sel <= 0) | 0.107 |
| Significant (p<0.05) | **No** |
| CI lower > 5pp | **No** |

Key findings:
- The raw-feature selectivity (7.6pp) is consistent with the known 7.5pp
- However, it is **not statistically significant** (p=0.107, CI includes 0)
- The CI lower bound (-3.9pp) is well below both 0 and the 5pp threshold
- High variance in random probe accuracy (std=5.1%) drives the wide CI
- With only 20 test traces, the bootstrap has limited statistical power

This contrasts sharply with the PCA-128 result (15.9pp, p=0.000, CI [9.7, 21.9]pp). The raw features underperform because the 5120-d space is under-determined (n=2076 < p=5120) without dimensionality reduction.

---
