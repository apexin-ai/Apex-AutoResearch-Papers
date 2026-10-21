# eval exp2 missing seeds v2

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_exp2-missing-seeds-v2_20260518T123457_result.json`
- **Structured JSON:** [`07e0287695a62e37a3c3.json`](../../sessions/07/07e0287695a62e37a3c3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results saved to `exp2_missing_seeds_complete.json`. Summary:

**Binary 3-seed ActorAttack (seed 42/123/456):**

| K | Mean | Std |
|---|------|-----|
| 1 | 0.737 | 0.074 |
| 2 | 0.890 | 0.065 |
| 3 | 0.951 | 0.036 |
| 5 | 0.987 | 0.012 |
| Full | 0.990 | 0.008 |

**Scrambled 3-seed ActorAttack (seed 42/123/456):**

| K | Mean | Std |
|---|------|-----|
| 1 | 0.721 | 0.101 |
| 2 | 0.828 | 0.054 |
| 3 | 0.893 | 0.067 |
| 5 | 0.937 | 0.057 |
| Full | 0.951 | 0.043 |

Compared to the 2-seed registry values, the 3-seed binary mean dropped from 0.788 to 0.737 at K=1 (seed42 was the outlier at 0.636), while full-turn performance remained essentially the same (0.990). Scrambled 3-seed means shifted slightly: K=1 went from 0.652 to 0.721 (seed123 was the strong one at 0.857).

---
