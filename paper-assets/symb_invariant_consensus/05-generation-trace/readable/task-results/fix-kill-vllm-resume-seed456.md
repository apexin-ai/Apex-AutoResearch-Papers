# fix kill vllm resume seed456

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_kill-vllm-resume-seed456_20260523T175316_result.json`
- **Structured JSON:** [`62ac92e8bd41317f0219.json`](../../sessions/62/62ac92e8bd41317f0219.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 4 GPUs now free (0 MiB each).

**Summary:**

**Part 1 — Kill idle vLLM:** Killed 3 vLLM servers, all confirmed idle (no experiment clients):
| GPU | Model | Port | PIDs killed |
|-----|-------|------|-------------|
| 0 | Llama-3.1-8B | 8009 | 744822, 745095 |
| 2 | Qwen2.5-14B | 8007 | 739631, 739913 |
| 3 | Qwen2.5-14B | 8005 | 776704, 776995 |

**Part 2 — Qwen2.5 seed456:** No resume needed — the experiment already completed 600/600 problems. Results at `/root/symb_invariant_consensus/results/multi_seed/qwen25_pw_seed456/results.json`:
- SICA accuracy: **72.17%** (433/600)
- SC accuracy: **73.0%** (438/600)
- Wall time: 8407.8s (~2.3h)

---
