# gpu check westd 35807 status

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu-check_westd-35807-status_20260525T203319_result.json`
- **Structured JSON:** [`04bf08fac6f76cfd5b3b.json`](../../sessions/04/04bf08fac6f76cfd5b3b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下：

---

## GPU 状态

| GPU | 温度 | 功耗 | 显存占用 | 利用率 | 进程 |
|-----|------|------|----------|--------|------|
| cuda:0 | 68°C | 477W/600W | 27GB/98GB | 100% | PID 3717 — spatial_bowl 训练 |
| cuda:1 | 40°C | 175W/600W | 9GB/98GB | 10% | PID 142394 — eval_s1_l005_30k_disp (**运行中**, 32min) |
| cuda:2 | 39°C | 88W/600W | 8GB/98GB | 0% | **空闲**（PID 134344 已结束） |
| cuda:3 | 40°C | 181W/600W | 9GB/98GB | 21% | PID 151915 — eval_s0_l005_30k_r4 (**运行中**, 25min) |

## Eval 进程状态

| Eval | PID | 状态 | 结果文件 |
|------|-----|------|----------|
| eval_pi05_a1_best_s1_l005_16k | 134344 | **已完成** | eval_s1_l005_best_16k.json ✓ |
| eval_pi05_a1_30k_s1_l005_disp | 142394 | **运行中** (32min) | eval_s1_l005_30k_disp.json（未生成） |
| eval_s0_l005_30k_r4 | 151915 | **运行中** (25min) | eval_s0_l005_30k_r4.json（未生成） |

## eval_s1_l005_best_16k 结果（best checkpoint, seed1）

**avg_TSR = 0.0650, avg_CAR = 0.5300**

| Task | TSR | CAR | avg_max_disp | avg_max_ee_disp |
|------|-----|-----|-------------|-----------------|
| pick_up_orange_juice → basket | 0.04 | 0.58 | 0.0416 | 0.5179 |
| pick_up_chocolate_pudding → basket | 0.22 | 0.50 | 0.1018 | 0.5146 |
| pick_up_milk → basket | 0.00 | 0.88 | 0.0073 | 0.6475 |
| pick_up_bbq_sauce → basket | 0.00 | 0.16 | 0.0934 | 0.3707 |

Per-episode 字段包含: `max_displacement`, `max_ee_displacement`, `total_ee_path_length`, `smoothness` — displacement 数据完整。

## spatial_bowl 训练

- PID 3708, 已运行 2h31m
- 进度: **9929/30000 (33%)**, ~4.63s/it
- ETA: ~25h48m
- 当前 loss: ~0.019, sdf: ~0.033, ee: ~0.015

## Tmux Sessions

- `train_pi05_a1_spatial_bowl_s0_l005` — 训练进程
- `eval_pi05_a1_30k_s1_l005_disp` — eval 进程
- `eval_pi05_a1_30k_s0_l005_r4` — eval 进程（GPU 3 上的新 eval）

## 磁盘

| 分区 | 容量 | 已用 | 可用 | 使用率 |
|------|------|------|------|--------|
| / (root) | 30G | 23G | 7.7G | 75% |
| /root/autodl-tmp | 350G | 210G | 141G | 60% |

根分区 75%，还有余量但需关注。数据盘充裕。

---
