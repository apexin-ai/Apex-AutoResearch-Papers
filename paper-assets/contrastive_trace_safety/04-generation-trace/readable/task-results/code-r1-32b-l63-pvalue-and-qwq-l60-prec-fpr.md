# code r1 32b l63 pvalue and qwq l60 prec fpr

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_r1_32b_l63_pvalue_and_qwq_l60_prec_fpr_20260517T145554_result.json`
- **Structured JSON:** [`3e012ee10a4ceed0d58f.json`](../../sessions/3e/3e012ee10a4ceed0d58f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both tasks complete. Summary:

## Task A: R1-32B L63 p-value unification

v2 (`exp_r3_r1_32b_l63_bootstrap_v2`) already had null-centered two-sided bootstrap. Created comparison at `exp_r3_r1_32b_l63_pvalue_unified/results.json`.

**Old (one-sided) → New (null-centered two-sided):**

| W | Metric | p_old | p_new | Bonf sig? |
|---|--------|-------|-------|-----------|
| W1 | bal_acc | 0.000 | 0.000 | **yes** |
| W1 | precision | 0.000 | 0.000 | **yes** |
| W1 | precp_fpr | 0.004 | 0.007 | **yes** |
| W3 | bal_acc | 0.009 | 0.020 | **lost** |
| W3 | precision | 0.004 | 0.032 | **lost** |
| W3 | precp_fpr | 0.037 | 0.077 | no |
| W5+ | all | — | — | no |

Significance changed: W3 bal_acc and W3 precision lost Bonferroni significance (5→3 significant tests).

## Task C: QwQ L60 W=3 precision/FPR

Extracted to `exp_r3_qwq_l60_precision_fpr/results.json`. QwQ already used null-centered two-sided.

| Metric | HS | Text | Diff | 95% CI | p | Bonf sig? |
|--------|-----|------|------|--------|---|-----------|
| precision | 0.631 | 0.439 | +0.236 | [0.130, 0.345] | 0.000 | **yes** |
| pre_cp_fpr | 0.140 | 0.224 | −0.098 | [−0.169, −0.031] | 0.004 | **yes** |
| bal_acc | 0.733 | 0.610 | +0.154 | [0.100, 0.218] | 0.000 | **yes** |

## Bonferroni summary (α=0.0167)

**R1-32B L63 (unified):** Only W1 passes all 3 metrics. W3+ all fail.

**QwQ L60 W=3:** All 3 metrics (bal_acc, precision, pre_cp_fpr) pass.

---
