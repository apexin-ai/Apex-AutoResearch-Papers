# eval openvla crossmodel pruning

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_openvla_crossmodel_pruning_20260517T151030_result.json`
- **Structured JSON:** [`d11f88956d131577ef44.json`](../../sessions/d1/d11f88956d131577ef44.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All existing results are from the IMM model. The current OpenVLA eval is the first of its kind on this server.

**Current status:**
- OpenVLA baseline eval running (PID 643978, 686% CPU)
- Task 1/10, episode 10/50 completed, 7/10 success rate (70% so far)
- Rate: 2 episodes/min
- Estimated total time: ~8 hours for both conditions (baseline + random prune k=0.5)
- Started: ~23:44 CST (May 17)
- Expected completion: ~07:45 CST (May 18)

Early signal from baseline Task 1: 7/10 (70%) success rate on "pick up the alphabet soup and place it in the basket" — this is a strong baseline, suggesting OpenVLA is well-calibrated on LIBERO-Object. This will make the pruning comparison meaningful.

I'll check back on progress later to track completion and collect final results.

---
