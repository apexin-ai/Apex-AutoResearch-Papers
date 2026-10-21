# ops check gpu processes

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-gpu-processes_20260514T222812_result.json`
- **Structured JSON:** [`77465aadc92d7d87e15b.json`](../../sessions/77/77465aadc92d7d87e15b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Processes are β=0.3 seed 43 training, actively progressing — DO NOT kill.**

| PID | Run | Step | Progress | GPU |
|-----|-----|------|----------|-----|
| 963576 | `exp1_isr_b03_s43` (additive_bonus) | 248/500 | 49.6% | GPU 0, 91% util |
| 963653 | `exp1_random_b03_s43` (additive_random) | 186/500 | 37.2% | GPU 1, 89% util |

- Both started 05:52, running 36 min, status `Rl` (running, not stuck).
- Latest reward log timestamps: 22:28:50 / 22:28:49 UTC (current).
- Checkpoints saved (200 / 150).
- tmux: no sessions — processes orphaned but still attached to GPUs via parent PIDs 963575/963652 (likely nohup/disowned shells). Safe to leave running.

---
