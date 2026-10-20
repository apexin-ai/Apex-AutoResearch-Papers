# ops kill dup eval

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill-dup-eval_20260523T125009_result.json`
- **Structured JSON:** [`61d20564507cc08ad3ae.json`](../../sessions/61/61d20564507cc08ad3ae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Killed the two duplicate `contam_25 llama` processes on GPU 3 (PIDs 130063, 130608 + parent shells). However, two **new** eval processes appeared on GPU 3 right after (likely spawned by another agent):

- **PID 131131**: `contam_25 llama` on GPU 3
- **PID 131201**: `contam_15_s1 llama` on GPU 3

## Report

**Killed:**
- PID 123754 — already dead
- PIDs 130058/130063 — duplicate `contam_25 llama` on GPU 3
- PIDs 130601/130606/130608 — duplicate `contam_25 llama` on GPU 3

**Currently running eval processes (4 GPUs):**

| GPU | PID | Condition | Model | Notes |
|-----|-----|-----------|-------|-------|
| 0 | 123059 | contam_25 | llama | Part of chain (→ contam_5 mistral next) |
| 1 | 128364 | contam_15_s3 | llama | Part of chain (→ contam_25_s2 llama, etc.) |
| 2 | 124248 | contam_5 | mistral | Standalone |
| 3 | 128943 | contam_50_s3 | llama | Part of chain (→ contam_5_s2 llama, etc.) |
| 3 | 131131 | contam_25 | llama | **New, appeared after cleanup** |
| 3 | 131201 | contam_15_s1 | llama | **New, appeared after cleanup** |

**GPU memory after cleanup:**

| GPU | Used | Total | Util |
|-----|------|-------|------|
| 0 | 41.5 GB | 97.9 GB | 96% |
| 1 | 16.3 GB | 97.9 GB | 93% |
| 2 | 22.8 GB | 97.9 GB | 98% |
| 3 | 8.7 GB | 97.9 GB | 91% |

GPU 0 freed ~8.6 GB from the killed process. GPU 3 still has 3 eval processes — the two new ones (131131, 131201) may need to be killed if they weren't intentionally launched.

---
