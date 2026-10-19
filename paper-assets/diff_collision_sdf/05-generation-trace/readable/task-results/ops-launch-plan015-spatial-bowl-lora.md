# ops launch plan015 spatial bowl lora

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_launch_plan015_spatial_bowl_lora_20260526T122724_result.json`
- **Structured JSON:** [`9347d6a902478f9a9240.json`](../../sessions/93/9347d6a902478f9a9240.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Plan 015 已启动，registry 已更新为 RUNNING。

**状态汇总：**
- **服务器**: westd-35807, cuda:3
- **tmux session**: `plan015`
- **训练**: 30000 steps, ~5.5s/it, 已正常出 step 0-1（loss=0.1257→0.1136）
- **日志**: `/root/runs/diff_collision_sdf/plan015_lora_baseline_spatial_bowl_s0.log`
- **Checkpoint 目录**: `/root/autodl-tmp/checkpoints/a1_sdf_pi05_spatial_bowl/pi05_lora_baseline_spatial_bowl_seed0`
- **预估完成**: ~46h（按当前 5.5s/it），比预估略长
- **注意**: 用 tmux 启动（符合 C002 约束，>24h 训练禁用 submit_training_job）

---
