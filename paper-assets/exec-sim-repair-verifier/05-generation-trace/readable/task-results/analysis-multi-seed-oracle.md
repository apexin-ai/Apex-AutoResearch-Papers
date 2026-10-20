# analysis multi seed oracle

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_multi-seed-oracle_20260522T124959_result.json`
- **Structured JSON:** [`e3abdcf2f92b08514995.json`](../../sessions/e3/e3abdcf2f92b08514995.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results with all individual accuracies matching expected values (CWM s42=65.17, s123=67.33, s456=66.93):

```
=== Individual Accuracies (n=9784) ===
CLS s42:  85.34%
CWM s42:  65.17%
CWM s123: 67.33%
CWM s456: 66.93%

=== Oracle (CLS ∪ CWM correct) ===
Oracle CLS+CWM(s42):  91.28%
Oracle CLS+CWM(s123): 95.86%
Oracle CLS+CWM(s456): 95.68%

Mean ± Std: 94.27 ± 2.59%
```

Note: the s42 oracle is lower than s123/s456 because CLS and CWM s42 share the same training seed, making their errors more correlated. The cross-seed oracles (s123, s456) are tightly clustered at ~95.8%.

---
