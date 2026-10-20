# ops disk cleanup

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_disk-cleanup_20260514T220449_result.json`
- **Structured JSON:** [`0b1b4e7079e481b1ae7b.json`](../../sessions/0b/0b1b4e7079e481b1ae7b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cleanup complete.

| Metric | Before | After |
|---|---|---|
| Used | 165G | 135G |
| Available | 86G | 116G |
| **Freed** | — | **30G** |

Deleted: `plan006_prolog_exec_s43_r3` (16G), `plan018_additive_random_b01_s43_r2` (16G, failed secondary candidate), plus small/empty stubs (`plan013_random_reward_s42.log`, `plan009_sft_s42_r3`, `plan006_prolog_exec_s43_r2`, `plan006_prolog_exec_s43`). Other primary-list targets (`sta-phase1-*`, `plan001_exec_only_s43*`, `plan018_additive_random_b01_s43`) were not present on disk.

---
