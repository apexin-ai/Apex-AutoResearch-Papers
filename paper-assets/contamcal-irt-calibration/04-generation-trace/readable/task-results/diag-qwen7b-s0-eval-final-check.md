# diag qwen7b s0 eval final check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_qwen7b-s0-eval-final-check_20260520T235421_result.json`
- **Structured JSON:** [`1f3a18c0ad0a7622f058.json`](../../sessions/1f/1f3a18c0ad0a7622f058.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**ARC eval still in progress.** Current status:

| Dosage | MMLU | ARC |
|--------|------|-----|
| d000 | 66.32% | **87.20%** ✓ |
| d005 | 64.68% | ~37% running |
| d025 | 65.67% | pending |
| d050 | 65.78% | pending |
| d100 | 65.29% | pending |

ARC d000 completed at 07:53 with accuracy **87.20%** (1022/1172). d005 is currently running at 37%.

Each ARC dosage takes ~5 min (1172 items at ~4.4 it/s + model load). Estimated completion for all 5 ARC dosages: **~08:15 CST** (about 20 min from now).

evaluate.py md5 verified: `001a9bc23f808c47d25ef9eaeecb81f1` (37591 bytes) — consistent with reference hash.

---
