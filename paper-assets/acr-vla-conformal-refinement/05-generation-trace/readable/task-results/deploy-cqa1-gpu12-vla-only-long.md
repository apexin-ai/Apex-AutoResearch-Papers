# deploy cqa1 gpu12 vla only long

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_cqa1-gpu12-vla-only-long_20260526T071652_result.json`
- **Structured JSON:** [`c317047fd0a59b3436b1.json`](../../sessions/c3/c317047fd0a59b3436b1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Critical finding: GPU 1 and GPU 2 are NOT idle. Both processes are alive and actively running:

- **GPU 1 (PID 219038, child 219043, 14GB VRAM)**: pi05-adaptive-object-s42-cqa1 — log updated 15:11:53 (~recent), currently at task 1/10, rollout 10/20, 10/10 success so far. Actively progressing.
- **GPU 2 (PID 219674, child 219679, 13.9GB VRAM)**: pi05-adaptive-goal-s42-cqa1 — log updated 15:16:37 (~recent), currently at task 1/10, rollout 10/20, 6/10 success. Actively progressing.

Both are long-form `adaptive_conformal_crm` evaluations (200 rollouts × ~280 steps each, K=2 means 2x inference per step). These take many hours; "21 minutes etime + 14GB VRAM + log writing every few seconds" = healthy in-progress, not stuck.

**Director's "3+ hours idle" report is incorrect.** I will NOT kill these healthy processes or deploy on top of them — that would destroy in-progress data for Table 2.

**No action taken. Recommend:**
1. Director re-verify the "idle" signal source — possibly looking at stale `nvidia-smi` snapshot or wrong GPU IDs.
2. If new VLA-only Long experiments still need a home, deploy on a different server or wait for these to complete (ETA ~6-8h based on 21min for 10/200 rollouts).
3. Registry state is correct as-is; no updates needed.

---
