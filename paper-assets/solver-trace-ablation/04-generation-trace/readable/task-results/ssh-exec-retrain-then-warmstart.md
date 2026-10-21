# ssh exec retrain then warmstart

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exec-retrain-then-warmstart_20260516T154159_result.json`
- **Structured JSON:** [`c99e2b7455effcecae7f.json`](../../sessions/c9/c99e2b7455effcecae7f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Exec-only retrain running on cuda:0. Summary so far:

**Completed:**
- Modified `train_grpo.py`: `save_steps`/`save_total_limit` now configurable via YAML, added `_is_h7()` function + H7 gate in isr_gated mode with `h7_blocked` tracking
- Created `configs/grpo_exec_retrain.yaml` (500 steps, save every 50, keep 10 checkpoints)
- Created `configs/grpo_isr_gated_warmstart_v2.yaml` (pointing to checkpoint-200)
- Submitted exec-only retrain on cuda:0 (PID in tmux `exec-retrain`)

**First steps:**
- step 1: prove_rate=0.125, parse_rate=1.0
- step 3: prove_rate=0.375 (non-zero, training healthy)
- ~6.3s/step → checkpoint-200 expected in ~21 min

Will check back at step ~45 and continue polling until checkpoint-200 is ready.

---
