# ops resume spatial bowl cuda0

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_resume_spatial_bowl_cuda0_20260525T175418_result.json`
- **Structured JSON:** [`efd21d1eff7695abbeb9.json`](../../sessions/ef/efd21d1eff7695abbeb9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Training resumed and running.

- Resumed at step 8000/30000, Phase 2 LoRA unfrozen
- step=8000 loss=0.0199; step 8002 currently advancing
- GPU 0: 27GB VRAM, 100% utilization
- tmux session `train_pi05_a1_spatial_bowl_s0_l005`, PID 3708, timeout 36h
- Fix applied: `WANDB_MODE=offline` (API key wiped by server reboot — same pattern as prior A3 runs)

Pace ~9s/it for 22K remaining steps → ~55h, exceeds 36h timeout. Will need monitoring; if it doesn't finish in 36h, resubmit again from the latest checkpoint.

---
