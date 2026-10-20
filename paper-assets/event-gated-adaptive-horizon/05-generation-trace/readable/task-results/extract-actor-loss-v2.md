# extract actor loss v2

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_extract_actor_loss_v2_20260515T103622_result.json`
- **Structured JSON:** [`7607853114f806ef1f67.json`](../../sessions/76/7607853114f806ef1f67.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

JSON file saved. Here's the summary:

**Data availability:**
- **008d**: 2 actor_loss data points (25K: -0.195, 35K: -0.170) — the only experiment with actor_loss in the registry
- **009b**: 0 actor_loss data points — 11 checkpoints with eval_return/value_mean/ve_ratio only
- **009e**: 0 actor_loss data points — 8 checkpoints with eval_return/value_mean/ve_ratio only (still running at 75K/105K)

**Why actor_loss is missing**: The registry only tracked actor_loss for 008d (and only 2 snapshots). For 009b and 009e, the workers that analyzed these experiments never extracted actor_loss from `metrics.jsonl` — they focused on eval_return, value_mean, and v/e ratio.

**What I couldn't do**: The full actor_loss timeseries lives in `metrics.jsonl` on the remote server, but I have no SSH access (the `~/.ssh/id_ed25519` key doesn't exist, and the `ssh_read_only`/`ssh_execute` MCP tools are only available to spawned workers).

**Included as reference**: Full actor_loss timeseries for baseline (exp_001), exp_006 (dt=2 collapsed), and exp_007 (dt=4 collapsed) from the existing collapse mechanism analysis.

To get the actual actor_loss timeseries for 009b and 009e, a worker with SSH access would need to read the `metrics.jsonl` files from the server's logdir.

---
