# code tost equivalence test

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_tost-equivalence-test_20260517T115207_result.json`
- **Structured JSON:** [`48c51a8452a2edccf0e6.json`](../../sessions/48/48c51a8452a2edccf0e6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results saved to `/root/gen-depth-fingerprint/results/tost_equivalence.json`.

### TOST Equivalence Test Results

| Comparison | Mean diff | Δ=0.05 p_TOST | Equiv? | Δ=2% p_TOST | Equiv? | Min margin |
|---|---|---|---|---|---|---|
| all_data vs size_matched | -0.0321 | 0.000144 | **Yes** | 0.000217 | **Yes** | 0.0330 (1.41%) |
| all_data vs depth01 | -0.0520 | 0.985 | **No** | 0.998 | **No** | 0.0531 (2.27%) |
| size_matched vs depth01 | -0.0200 | 0.000095 | **Yes** | 0.000114 | **Yes** | 0.0212 (0.89%) |

Key findings:
- **all_data vs size_matched**: Equivalent at both margins (diff ~0.032, well within Δ=0.05)
- **all_data vs depth01**: **Not equivalent** at either margin. The diff (~0.052) slightly exceeds Δ=0.05. Minimum margin for equivalence is 0.053 (2.27% of baseline)
- **size_matched vs depth01**: Equivalent at both margins (diff ~0.020, comfortably within Δ=0.05)

---
