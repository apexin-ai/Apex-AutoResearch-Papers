# code exp44 check and submit

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp44_check_and_submit_20260522T054742_result.json`
- **Structured JSON:** [`213eced89abef178abe3.json`](../../sessions/21/213eced89abef178abe3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Data completeness — all pass:**

| Family | Count | Threshold | Status |
|--------|-------|-----------|--------|
| DD Llama | 50 | 50 | ✓ |
| AA Llama | 50 | 50 | ✓ |
| FITD Llama | 50 | ≥47 | ✓ |
| Crescendo Llama | 251 | ≥200 | ✓ |
| Benign Llama | 250 | — | ✓ |

FITD JSON validity: OK (last line parses correctly).

**Pipeline NOT submitted.** GPU 0 is busy — PID 31463 is running `exp44_train_mixed_llm.py` (5132 MiB used, 69-71% utilization). Submitting `exp44_full_pipeline.py` on the same GPU would likely conflict with this existing exp44 training job.

Options:
1. Wait for PID 31463 to finish, then submit the pipeline
2. Submit the pipeline on a different GPU (e.g. cuda:1) if the pipeline and the existing training are independent
3. Kill PID 31463 if it's stale/unwanted and then submit

---
