# fix exp004 sweep restart

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_exp004_sweep_restart_20260514T032129_result.json`
- **Structured JSON:** [`75dcadb7c3894fdd4a4b.json`](../../sessions/75/75dcadb7c3894fdd4a4b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Sweep is running. It correctly skipped the 2 completed conditions and resumed `auc0.55_n100` at seed 6 (4 remaining).

**Summary:**

| Item | Value |
|------|-------|
| **New PID** | 340553 |
| **Timeout added** | 7200s (2h) per fit, via CmdStanPy native `timeout` param |
| **Completed** | 27/120 seeds (3 conditions fully done) |
| **Remaining** | 93 seeds across 10 conditions |
| **Checkpoint integrity** | Clean — seed 6 had no partial entry |
| **Log** | `/tmp/exp004_sweep.log` |

**Estimated remaining time:** Completed seeds averaged ~1600s each. With 93 remaining and 4-chain parallelism (CPU-bound), expect ~40-60 hours. The `n100` conditions run ~3400s/seed; `n20` ~320s/seed; `n50` ~1000-1300s/seed. The stuck seed was an outlier — the 2h timeout will prevent that from recurring.

---
