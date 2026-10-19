# ops eval s0 l01 cuda2

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_eval_s0_l01_cuda2_20260525T183310_result.json`
- **Structured JSON:** [`57e0dc5a05359d55fe5a.json`](../../sessions/57/57e0dc5a05359d55fe5a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

正常启动，正在加载模型。

- **exp_id**: `eval_pi05_a1_30k_s0_l01`
- **GPU**: westd-35807 cuda:2
- **Checkpoint**: `/root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/a1_sdf_pi05_object_pudding_seed0_l01/30000`
- **Output**: `/root/autodl-tmp/eval_results/eval_s0_l01_30k_final.json`
- **Log**: `~/runs/diff_collision_sdf/eval_pi05_a1_30k_s0_l01.log`

注意：原始任务步骤中 `--checkpoint_path` 应为 `--checkpoint`，另外补加了 `--suite safelibero_object` 和 `--pi05` flag（与同项目其他 pi05 eval 一致）。

---
