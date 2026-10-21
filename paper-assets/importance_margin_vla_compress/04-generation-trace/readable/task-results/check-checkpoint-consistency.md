# check checkpoint consistency

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_checkpoint_consistency_20260517T131749_result.json`
- **Structured JSON:** [`05b519c12fd5af29462d.json`](../../sessions/05/05b519c12fd5af29462d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

三个 eval 文件中记录的 checkpoint 路径：

| Suite | 文件 | Checkpoint |
|-------|------|-----------|
| Object | `eval_stage1only_object_v2_fixed.json` | `checkpoints/libero_imm_twostage_fullft/stage1_done/checkpoint.pt` |
| Object | `eval_true_removal_k05_object.json` | `checkpoints/libero_imm_twostage_fullft/stage1_done/checkpoint.pt` |
| Spatial | `eval_spatial_prune_k05.json` | `checkpoints/libero_acis_stage1only_k03/stage1_done/checkpoint.pt` |
| Goal | `eval_goal_prune_k05.json` | `checkpoints/libero_acis_stage1only_k03/stage1_done/checkpoint.pt` |

### 一致性：**N（不一致）**

**具体差异：**
- Object suite 用的是 `checkpoints/libero_imm_twostage_fullft/stage1_done/checkpoint.pt`
- Spatial 和 Goal suite 用的是 `checkpoints/libero_acis_stage1only_k03/stage1_done/checkpoint.pt`

两组用了不同的 checkpoint。且都不是预期的 `checkpoints/acis_stage1only_k05/stage1_done/checkpoint.pt`。

补充：config 也不一致——Object 用 `configs/libero_imm_twostage_fullft.yaml`，Spatial/Goal 用 `configs/libero_acis_stage1only_k03.yaml`。

---
