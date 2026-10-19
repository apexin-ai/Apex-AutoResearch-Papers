# code data pipeline

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_data_pipeline_20260519T175625_result.json`
- **Structured JSON:** [`a73b65d99947d31598bc.json`](../../sessions/a7/a73b65d99947d31598bc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

No `register_artifact` tool available. The report is already saved at `artifacts/report_data_pipeline.md`.

Pipeline complete. Here's the summary:

**Both MVP scenes processed successfully:**

| Task | Episodes | Avg Length | Output Size |
|------|----------|------------|-------------|
| spatial_bowl | 50 | 101 steps | 403.4 MB |
| object_chocolate | 50 | 160 steps | 715.9 MB |

**Output at** `/root/autodl-tmp/colliforce_data/` with per-episode data:
- `observations/agentview` [T, 224, 224, 3] uint8
- `observations/eye_in_hand` [T, 224, 224, 3] uint8
- `observations/state` [T, 8] float32 (ee_pos + ee_axisangle + gripper)
- `actions` [T, 7] float32 (delta EE)
- `ee_positions` [T, 3] float32 (EE position GT)
- `sdf_gt/` (per-scene query points + SDF values)

**Key finding**: LIBERO demos store `ee_ori` as 3D axis-angle (not quaternion), so no conversion was needed. Images were 128x128, resized to 224x224 for pi0 compatibility.

Report saved at `artifacts/report_data_pipeline.md`.

---
