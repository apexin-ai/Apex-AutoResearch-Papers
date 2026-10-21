# ops audit cqa1

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_audit-cqa1_20260524T001642_result.json`
- **Structured JSON:** [`ae6d674cdc803e6ac278.json`](../../sessions/ae/ae6d674cdc803e6ac278.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the full audit:

---

## 1. eval_pi05_random_k05_object_seed42_v2 — **COMPLETED**

- **No log file** with v2 name exists — process likely ran without tee or used a different log name
- **Result file exists**: `pi05_random_k0.50_libero_object_seed42.json`, created **2026-05-24 08:08** (10 minutes ago)
- **SR = 68.2%** (341/500), all 10 tasks complete, elapsed 127 min
- Process exited normally after writing results. Not OOM/SIGKILL — it finished.

## 2. eval_pi05_random_k09_object_seed42_v2 — **RUNNING** (GPU 0)

- PID 459609, started 06:50, running 1.5h
- **Progress**: Task 4/10 complete, overall SR = 9.2% (23/250), 81 min elapsed
- Last log at 08:14 — actively progressing
- ETA: ~80 more minutes (10 tasks total, ~40% done)

## 3. GPU & tmux audit

| GPU | Memory | Util | Process |
|-----|--------|------|---------|
| 0 | 10313/24564 MiB | 53% | `eval_pi05_random_k09_object_seed42_v2` (T4/10) |
| 1 | 10324/24564 MiB | 62% | `eval_pi05_random_k095_object_seed42_v2` (T1/10, just started) |
| 2 | 10264/24564 MiB | 23% | `eval_pi05_random_k07_object_seed42_v3` (T6/10, ~60% done) |
| **3** | **1/24564 MiB** | **0%** | **IDLE** |

**Tmux sessions:**
- `eval_pi05_l2norm_k03_goal_seed42` — stale (eval completed SR=54.2%, process exited)

**Recently completed evals (today):**
- l2norm k0.95 goal: SR=90.8%
- l2norm k0.30 goal: SR=54.2%
- random k0.30 goal: SR=51.0%
- random k0.50 object: SR=68.2%

## 4. Summary

- **GPU 3 is free** and available for new work
- 3 evals running on GPUs 0-2, all progressing normally
- `eval_pi05_random_k05_object_seed42_v2` completed successfully — should be marked DONE in registry if not already

---
