# ssh kill cpu ghost a3 45947

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_kill_cpu_ghost_a3_45947_20260520T082730_result.json`
- **Structured JSON:** [`35401485f349b7b197ed.json`](../../sessions/35/35401485f349b7b197ed.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### 1. Kill 前进程列表
| PID | 类型 | 场景 | 特征 |
|-----|------|------|------|
| 66862 | CPU 幽灵 (bash) | spatial_bowl | 无 --gpu，~270s/it |
| 66867 | CPU 幽灵 (python) | spatial_bowl | CPU 2130%，RSS 10.7GB |
| 66941 | CPU 幽灵 (bash) | object_pudding | 无 --gpu，~270s/it |
| 66946 | CPU 幽灵 (python) | object_pudding | CPU 2239%，RSS 9.5GB |
| 71494 | GPU 正常 | spatial_bowl --gpu 0 | ~10-15s/it |
| 73165 | GPU 正常 | object_pudding --gpu 1 | ~10-15s/it |

### 2. Kill 结果
`ALL_KILLED` — 4 个 CPU 幽灵进程全部清除，无残留 A3 进程。

### 3. GPU 进程验证
- PID 71494: 存活，运行 28min，CPU 157%，RSS ~4.9GB，step ~98/30000
- PID 73165: 存活，运行 28min，CPU 171%，RSS ~5.0GB，step ~2598/30000
- GPU 0/1 各占用 16907 MiB 显存

### 4. 日志污染
**有污染，但无需清理。** 两个 log 文件都有 CPU 和 GPU 进程的交叉写入：
- `spatial_bowl` log: GPU (steps 1→98, ~10-15s/it) 与 CPU (steps 1→6, ~270s/it) 进度条交错
- `object_pudding` log: GPU (steps 2501→2598, ~10-15s/it) 与 CPU (steps 2501→2507, ~270s/it) 进度条交错

CPU 进程已死，不会再写入。GPU 进程继续正常追加。历史交错内容是噪声但不影响训练本身。

### 5. Checkpoint 污染
**无污染。**
- `spatial_bowl`: checkpoint 目录仅有 `wandb_id.txt`（16:00 GPU 进程写入）。GPU 在 step 98，CPU 在 step 6，均未触发 save_interval=2000
- `object_pudding`: 仅有 step-2500 checkpoint（15:04 创建，早于 CPU/GPU 进程启动），为之前训练的正常产出。GPU 在 step 2598，CPU 在 step 2507，均未触发下一个 save_interval=4500

**结论：无需任何清理操作。GPU 训练正常继续。**

---
