# audit data correctness presubmit

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_data_correctness_presubmit_20260523T191928_result.json`
- **Structured JSON:** [`335afa9484be79e40890.json`](../../sessions/33/335afa9484be79e40890.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Report written to `artifacts/data_audit_report.md`.

**Top findings:**

- **CRITICAL (D1):** Fig 4 caption says "TF evaluation, GAR near 0.5, 7-8% decay" but the actual figure data shows AR-scale values (0.01–0.06) with 77-87% decay. Caption and data are fundamentally mismatched. The N=45 sample size in the caption is untraceable.
- **MEDIUM (D4):** Two SS seeds used different max-ratio schedules (s42: 0.3, s123: 0.5) but the paper describes a single "0 to 0.5" protocol.
- **MEDIUM (D2):** Fig 3b uses N=5 data showing 20–33× gaps, while main text reports N=50 with 7.8–16.7× gaps — unlabeled setting difference.
- **LOW-MEDIUM (D6):** The "27×" Llama gap uses median; Qwen "8×" uses mean. Abstract's "8–27×" spans two models with inconsistent aggregation.
- **LOW (D3):** PCGrad training time 7.2h/+20% vs actual 7.98h/+33%.

88% of ~85 audited claims verified consistent. 5 inconsistencies, 2 untraceable numbers.

---
