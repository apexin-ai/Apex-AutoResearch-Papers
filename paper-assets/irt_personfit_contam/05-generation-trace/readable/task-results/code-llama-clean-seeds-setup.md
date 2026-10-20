# code llama clean seeds setup

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_llama-clean-seeds-setup_20260520T231843_result.json`
- **Structured JSON:** [`5ae3ba2a82a4d0169f50.json`](../../sessions/5a/5ae3ba2a82a4d0169f50.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Critical issue found**: Original `clean` was trained with `seed=42`. The current SEED_MAP has `clean_s2: 42` — identical to the original `clean`, which would produce a duplicate run rather than an independent seed.

Task spec says `clean_s2 (seed=42)` but this contradicts the n=3 requirement (we'd effectively have n=2 distinct seeds: 42 and 456).

Need user clarification before proceeding. The likely intended setup is:
- `clean_s2`: a different seed (e.g., 123) — most natural fix
- `clean_s3`: 456 (as specified)

Or perhaps a different mapping was intended. Should I:
1. Use `clean_s2: 123, clean_s3: 456` (3 distinct seeds: 42/123/456) — **recommended**
2. Use seeds exactly as task says (clean_s2=42, clean_s3=456) — keeps n=2 effectively
3. Other seeds you'd prefer?

---
