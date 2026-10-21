# ssh d006 quick status

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_d006_quick_status_20260520T220712_result.json`
- **Structured JSON:** [`17d556a8773efc0d4305.json`](../../sessions/17/17d556a8773efc0d4305.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇报

**4 张 GPU 全部 100% 利用率，共 4 个训练进程：**

| GPU | PID | 实验 | 启动时间 | 显存占用 | 备注 |
|-----|-----|------|----------|----------|------|
| cuda:0 | 222903 | `train_baseline --scene spatial_bowl --seed 0 --resume` | 22:37 | 35738 MiB / 97887 MiB | **旧进程** |
| cuda:1 | 263726 | `train_baseline --scene spatial_bowl --seed 0 --num_train_steps 30000` | 05:34 | 23884 MiB / 97887 MiB | **新进程** |
| cuda:2 | 222982 | `train_baseline --scene object_pudding --seed 0 --resume` | 22:37 | 35738 MiB / 97887 MiB | **旧进程** |
| cuda:3 | 263799 | `train_baseline --scene object_pudding --seed 0 --num_train_steps 30000` | 05:34 | 23884 MiB / 97887 MiB | **新进程** |

**日志进度（来自新进程的输出目录）：**

- **baseline_lora_spa_s0**: step **464/30000**, loss=0.1208, lr=1.16e-05, ~4.0s/it
- **baseline_lora_obj_s0**: step **464/30000**, loss=0.0878, lr=1.16e-05, ~4.0s/it

**注意：存在重复运行问题。** 每个场景有两个进程——22:37 启动的旧进程（带 `--resume`）和 05:34 启动的新进程（从头训练 30000 步）同时跑在不同 GPU 上。旧进程各占 ~36GB 显存，新进程各占 ~24GB。如果旧进程不需要了，应该 kill 掉释放 GPU 0 和 GPU 2。

---
