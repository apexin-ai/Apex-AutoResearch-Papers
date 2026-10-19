# ssh verify baseline status 35807

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_verify_baseline_status_35807_20260520T144745_result.json`
- **Structured JSON:** [`254ff1d5d912a02169c1.json`](../../sessions/25/254ff1d5d912a02169c1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总报告

### GPU 状态（4× NVIDIA RTX PRO 6000 Blackwell, 98GB VRAM each）

| GPU | PID | 进程 | 显存 | GPU利用率 | 运行时间 | 状态 |
|-----|------|------|------|-----------|----------|------|
| 0 | 222903 | `train_baseline.py --scene spatial_bowl --seed 0 --resume` | 35738 MiB | 0% | 11min | **存活** ✓ step 14158/30000 (47%) |
| 1 | 227389 | `train_a1_sdf_aux.py --scene object_pudding --seed 0 --gpu 1` | 550 MiB | 0% | 53s | **刚启动** ✓ 正在初始化 |
| 2 | 222982 | `train_baseline.py --scene object_pudding --seed 0 --resume` | 35738 MiB | 100% | 11min | **存活** ✓ step 16159/30000 (54%) |
| 3 | 185994 | `train_a1_sdf_aux.py --scene spatial_bowl --seed 0 --resume` | 13376 MiB | 98% | 6h23m | **存活** ✓ step 12416/30000 (41%) |

### 结论

- **两个 baseline 重启成功**，PID 222903/222982 均在正常训练，从 checkpoint 恢复（spatial_bowl 从 step 14000，object_pudding 从 step 16000）
- **A1 spatial_bowl**（PID 185994）稳定运行 6h+，step 12416
- **A1 object_pudding**（PID 227389）刚启动 53s，还在加载模型/数据，尚未出训练日志
- 旧 PID 100319/95429 已不存在
- 磁盘 `/root/autodl-tmp`：350G 用了 121G (35%)，充裕

**所有 4 个训练进程均在运行，无异常。**

---
