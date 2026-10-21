# setup spatial bowl eval auto

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_setup_spatial_bowl_eval_auto_20260527T201318_result.json`
- **Structured JSON:** [`e5d86a8c8beaee5bf623.json`](../../sessions/e5/e5d86a8c8beaee5bf623.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Sentinel 已部署并运行。

| 项 | 值 |
|---|---|
| Sentinel PID | **875618** |
| 监控训练 PID | 341425 (spatial_bowl seed=0, gpu:3, 30K steps) |
| Checkpoint 路径 | `/root/autodl-tmp/checkpoints/a1_sdf_pi05_spatial_bowl/pi05_lora_baseline_spatial_bowl_seed0/30000`（fallback: `best`） |
| Eval GPU | cuda:0 |
| Eval 命令 | `--config_name pi05_libero --model_type lora_baseline --pi05 --suite safelibero_spatial --safety_level II --n_episodes 50 --seed 7` |
| Eval 日志 | `/root/autodl-tmp/eval_results/eval_spatial_bowl_lora_ctrl_s0.log` |
| Sentinel 日志 | `/root/autodl-tmp/auto_eval_spatial_bowl_sentinel.log` |
| 预计触发时间 | ~06:15 UTC 5/28 |

---
