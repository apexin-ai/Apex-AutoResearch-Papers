# ssh westd phase2 collect remaining

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_westd-phase2-collect-remaining_20260519T115332_result.json`
- **Structured JSON:** [`3ee98b0a5ec0ff64c323.json`](../../sessions/3e/3ee98b0a5ec0ff64c323.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Found the 5th family: **OLMo-2-7B** (5 checkpoints, 0 evals started). Also confirmed qwen14b_d100 checkpoint exists but eval hasn't started.

3 GPUs active (0, 1, 3), GPU 2 idle.

## Phase 2 Eval Status (25 total)

| Family | Dosage | MMLU | ARC | Status |
|--------|--------|------|-----|--------|
| gemma2 | d000 | 0.6186 | 0.8601 | DONE |
| gemma2 | d005 | 0.6342 | 0.7782 | DONE |
| gemma2 | d025 | 0.6456 | 0.8737 | DONE |
| gemma2 | d050 | 0.6401 | 0.7108 | DONE |
| gemma2 | d100 | - | - | RUNNING (GPU 1) |
| phi4 | d000 | 0.7644 | 0.9206 | DONE |
| phi4 | d005 | 0.7636 | 0.9181 | DONE |
| phi4 | d025 | 0.7698 | 0.9232 | DONE |
| phi4 | d050 | 0.7675 | 0.9241 | DONE |
| phi4 | d100 | - | - | RUNNING (GPU 3, ARC 34%) |
| qwen14b | d000 | 0.6944 | 0.9104 | DONE |
| qwen14b | d005 | 0.6901 | 0.9036 | DONE |
| qwen14b | d025 | 0.6204 | 0.8891 | DONE |
| qwen14b | d050 | - | - | RUNNING (GPU 0, MMLU 0%) |
| qwen14b | d100 | - | - | PENDING |
| qwen7b | d000 | 0.6611 | 0.8788 | DONE |
| qwen7b | d005 | 0.6474 | 0.8609 | DONE |
| qwen7b | d025 | 0.6298 | 0.8404 | DONE |
| qwen7b | d050 | 0.6307 | 0.8456 | DONE |
| qwen7b | d100 | 0.6433 | 0.8498 | DONE |
| olmo2 | d000 | - | - | PENDING |
| olmo2 | d005 | - | - | PENDING |
| olmo2 | d025 | - | - | PENDING |
| olmo2 | d050 | - | - | PENDING |
| olmo2 | d100 | - | - | PENDING |

**Summary**: 16 DONE, 3 RUNNING, 6 PENDING (1 qwen14b_d100 + 5 OLMo-2-7B). GPU 2 is idle and available for scheduling pending evals.

---
