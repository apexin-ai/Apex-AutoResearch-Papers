# code r1 8b hs text bootstrap

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_r1_8b_hs_text_bootstrap_20260516T230705_result.json`
- **Structured JSON:** [`1c62b9bb05fc428d4cd6.json`](../../sessions/1c/1c62b9bb05fc428d4cd6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Done. Results:

| Metric | Value |
|--------|-------|
| **HS pre-CP FPR** | 14.8% |
| **Text pre-CP FPR** | 22.2% |
| **Difference (HS - Text)** | -7.4pp |
| **95% CI** | [-15.6%, -0.4%] |
| **p-value** | 0.044 |
| **N test traces** | 43 |

The HS probe has significantly lower pre-CP FPR than the text probe (p=0.044). The CI excludes zero, confirming the effect. This is consistent with QwQ-32B (p=0.001), though the effect size is smaller (7.4pp vs 14.8pp).

Output saved to `artifacts/r1_8b_bootstrap_hs_text/results.json` and report at `artifacts/r1_8b_bootstrap_hs_text/report.md`.

---
