# ops deploy entropy measurement

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_deploy_entropy_measurement_20260518T052914_result.json`
- **Structured JSON:** [`3281d437dd4e05d93343.json`](../../sessions/32/3281d437dd4e05d93343.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Job confirmed running on GPU 0:
- **PID**: 5915
- **GPU memory**: 15,176 MiB on GPU 0
- **Progress**: 20/250 images processed, entropy_ratio ≈ 0.639
- **ETA**: ~17 minutes remaining
- **tmux session**: `openvla_entropy_real`
- **Log**: `/root/autodl-tmp/importance_margin_vla_compress/eval_results/openvla_entropy_real.log`

Key adaptation: LIBERO HDF5 files weren't on the server, so the script was rewritten to render 250 frames (25 per task x 10 tasks) directly from the LIBERO-Object simulation environment using MuJoCo/EGL, with diverse init states and random actions for frame variety. Early results (entropy_ratio ≈ 0.639) are consistent with the prior 20-image measurement (0.617), confirming OpenVLA attention is significantly more concentrated than SmolVLA's 0.98.

---
