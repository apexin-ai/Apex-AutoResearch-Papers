# deploy westd41074 gpu3 k085 goal seed43

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy-westd41074-gpu3-k085-goal-seed43_20260524T005440_result.json`
- **Structured JSON:** [`ccfb9496682a94b68076.json`](../../sessions/cc/ccfb9496682a94b68076.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

This experiment already exists in the registry — it was previously run on **cqa1-33015** and completed with **53.4% SR** (seed42=52.4%). The disruption peak is already confirmed as NOT seed-specific.

I've launched a re-run on westd-41074 GPU 3 anyway (tmux session `eval_pi05_random_k085_goal_seed43`, model loading confirmed in log). 

Key findings from the existing result:
- seed42=52.4%, seed43=53.4% → D191 disruption peak is reproducible across seeds
- Per-task: T1 (put_bowl_on_stove) = 6%, T9 (wine_bottle_on_rack) = 12% — same bottleneck tasks

Do you want to keep the re-run going on westd-41074, or kill it since results already exist?

---
