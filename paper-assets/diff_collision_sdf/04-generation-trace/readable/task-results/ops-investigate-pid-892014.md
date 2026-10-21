# ops investigate pid 892014

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_investigate-pid-892014_20260528T024225_result.json`
- **Structured JSON:** [`44d21fb80beb44595867.json`](../../sessions/44/44d21fb80beb44595867.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

PID 892014 是本项目的训练进程，**无需处理**。

### PID 892014 详情

| 项目 | 值 |
|------|-----|
| 命令 | `python scripts/train_a1_sdf_aux_pi05.py --scene object_pudding --seed 0 --lambda_sdf 0 --gpu 1 --num_train_steps 30000 --resume` |
| 运行时长 | 4 小时 7 分钟 |
| GPU | cuda:1 (GPU-8ec4b84d)，占用 **27036 MiB** |

这是 diff_collision_sdf 项目的 A1 SDF 辅助训练（object_pudding scene, baseline λ_sdf=0）。

### westd-35807 全卡占用情况

| GPU | 显存占用 | 总显存 | 利用率 | 占用进程 |
|-----|---------|--------|--------|---------|
| cuda:0 | 9014 MiB | 97887 MiB | 48% | PID 960263 (8995 MiB) |
| cuda:1 | 36055 MiB | 97887 MiB | 100% | **PID 892014 (27036 MiB)** + PID 960408 (8995 MiB) |
| cuda:2 | 27045 MiB | 97887 MiB | 100% | PID 856471 (27036 MiB) |
| cuda:3 | 8978 MiB | 97887 MiB | 4% | PID 960554 (8356 MiB) |

4 张卡都有进程在跑，cuda:1 和 cuda:2 利用率 100%、各占用约 27GB（看起来是主训练进程），cuda:0 和 cuda:3 各有约 9GB 的轻量进程。

---
