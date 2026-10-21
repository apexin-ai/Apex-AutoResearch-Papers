# code fill 3gpu urgent

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fill-3gpu-urgent_20260521T085106_result.json`
- **Structured JSON:** [`0d9f53ab691a15a02acb.json`](../../sessions/0d/0d9f53ab691a15a02acb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 4 GPUs fully utilized:

| GPU | Task | Status |
|-----|------|--------|
| 0 | ARC-C clean_s1 training | Running (step ~21/939, ~1.05 s/it) |
| 1 | Pilot clean_s10 training | Running (step ~23/939, ~1.0 s/it) |
| 2 | Existing task | 70% util |
| 3 | MIA sft eval | Running (~18 it/s) |

**Phase 1-3 complete.** Summary of eval results so far:

| Metric | s7 | s9 |
|--------|-----|-----|
| accuracy | 67.83% | 67.43% |
| theta_mle | -0.0892 | -0.1242 |
| lz_star | 8.770 | 9.013 |

**MIA base:** AUC-ROC ≈ 0.486 (loss), 0.493 (min_k_10), 0.488 (min_k_pp_10) — near random, as expected for base model.

**Remaining Phase 4 tasks:**
- Wait for MIA sft eval to complete (~12 min at 18 it/s), then read `mia_sft_results.json`
- Both trainings will take ~15-16 min (939 steps at ~1 s/step)

Shall I continue polling for MIA sft completion, or do you want me to check back later?

---
