# code paraphrase gen

**afford invar** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_paraphrase-gen_20260519T190517_result.json`
- **Structured JSON:** [`b8888b84605813289617.json`](../../sessions/b8/b8888b84605813289617.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All verification checks pass. Task C complete.

**Summary:**

| Step | Status | Details |
|------|--------|---------|
| 1. Kill Qwen3-8B & cleanup | Done | Freed ~12GB disk |
| 2. Download Qwen3-4B | Done | 3 shards (3.7G + 3.8G + 96M) at `/root/autodl-tmp/models/Qwen/Qwen3-4B/`, 4.02B params verified |
| 3. Extract LIBERO tasks | Done | 130 tasks across 5 suites (spatial:10, object:10, goal:10, libero_10:10, libero_90:90) |
| 4. Generate paraphrases | Done | Script at `/root/afford_invar/scripts/phase0/generate_paraphrases.py`, ran in ~3.5min |
| 5. Verify paraphrases | Done | 130 tasks × 5 = **650 paraphrases**, 0 empty, 0 duplicates with original |

Output: `/root/afford_invar/data/paraphrases.json` (61KB)

Note: had to upgrade `transformers` from 4.40.1 → 5.8.1 (Qwen3 requires ≥4.43).

---
