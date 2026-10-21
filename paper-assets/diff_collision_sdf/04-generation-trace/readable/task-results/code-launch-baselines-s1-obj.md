# code launch baselines s1 obj

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_launch_baselines_s1_obj_20260519T201140_result.json`
- **Structured JSON:** [`00de573a9303116178a7.json`](../../sessions/00/00de573a9303116178a7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个 GPU 全部在跑：

| GPU | 实验 | PID | 显存 | GPU Util |
|-----|------|-----|------|----------|
| cuda:0 | baseline_spatial_bowl seed 0 | 49555 | 37358MiB | 9% |
| cuda:1 | baseline_spatial_bowl seed 1 | 58919 | 37358MiB | 99% |
| cuda:2 | baseline_object_pudding seed 0 | 59904 | 20750MiB (加载中) | 100% |

启动完成。

**修正说明**：任务中写的 `--scene object_chocolate` 在脚本中不存在，SCENE_CONFIG 只有 `spatial_bowl` 和 `object_pudding`，已用 `object_pudding` 替代。另外脚本内部会用 `--gpu` 参数覆盖 `CUDA_VISIBLE_DEVICES`，所以需要用 `--gpu 1` / `--gpu 2` 而非环境变量。

日志路径：
- `/root/autodl-tmp/logs/baseline_spatial_bowl_seed1.log`
- `/root/autodl-tmp/logs/baseline_object_pudding_seed0.log`

---
