# analysis paper number audit

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_paper-number-audit_20260523T002633_result.json`
- **Structured JSON:** [`1235c5fdf28690e0ae8b.json`](../../sessions/12/1235c5fdf28690e0ae8b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Report written to `artifacts/paper_number_audit.md`.

Key findings:

**HIGH PRIORITY (6 locations):** SS gap ratio "1.57x" is stale — d048_eval_ss_s42 gives 1.29x, not 1.57x (old AR GAR 0.318 vs new 0.3887). With s123 data, mean is **1.25+/-0.06x**. Affected: abstract, introduction (x2), conclusion, discussion (x2). Must fix before submission.

**MEDIUM PRIORITY (3 locations):** TG gap range in experiments.tex says "30.5--32.1x" but actual data is 30.6--32.0x. Could express as 31.3+/-1.0x. Gate mean could optionally report 0.940+/-0.009 across seeds.

**LOW PRIORITY (~20 locations):** Steering, Llama, base model, gradient stats, TRC, instruction retention — all single-seed with no s123 counterpart provided. Not blockable for submission if flagged in Limitations (which already mentions single-seed).

---
