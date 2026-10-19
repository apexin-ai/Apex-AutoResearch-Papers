# eval launch true oracle action space cuda1

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_launch_true_oracle_action_space_cuda1_20260522T195419_result.json`
- **Structured JSON:** [`4b777a851a120b2adcd3.json`](../../sessions/4b/4b777a851a120b2adcd3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

**启动确认**:
- **tmux session**: `oracle_true_gt`
- **PID**: 84587
- **GPU**: cuda:1 (8580 MiB)

**GT SDF**: `/root/colliforce-vla/data/sdf_gt_object_chocolate.npz` (4084 points, KDTree built)

**日志确认**:
- GT SDF oracle 加载成功 ✓
- LoRA params 加载成功 (504 params) ✓
- SDF decoder + EE extractor 加载成功 ✓
- Task 0 已开始: `pick up the orange juice and place it in the basket` ✓

**注意**: 任务描述的参数名与脚本实际参数不一致，已修正：`--scene` → `--suite`，`--level` → `--safety_level`，`--checkpoint_dir/--ckpt_step` → `--checkpoint`，`--output_path` → `--save_dir` + `--output_prefix`。

---
