# audit cqa1 westd27271 gpu status

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_cqa1-westd27271-gpu-status_20260524T021400_result.json`
- **Structured JSON:** [`b2ee77e4618d939646c1.json`](../../sessions/b2/b2ee77e4618d939646c1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 服务器审计 2026-05-24

### cqa1-33015 (4×RTX 4090 24GB)

| GPU | 显存 | 利用率 | 状态 |
|-----|------|--------|------|
| 0 | 1/24564 MiB | 0% | 空闲 |
| 1 | 1/24564 MiB | 0% | 空闲 |
| 2 | 1/24564 MiB | 0% | 空闲 |
| 3 | 10294/24564 MiB | 3% | 运行中 |

**运行中 (1个):**
- PID 617677 (GPU 3): `eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.85 --suite libero_goal --seed 43`
  - 进度: Task 8/10, 累计 365/400=91.2%, 启动于 09:02

**旧 PIDs (304615/304879/305122/305386):** 全部已结束。

**今日已完成实验 (6个):**

| 实验 | Suite | 方法 | k | SR |
|------|-------|------|---|-----|
| eval_pi05_random_k095_object_v2 | libero_object | random | 0.95 | **74.0%** |
| eval_pi05_random_k09_object_v2 | libero_object | random | 0.9 | **9.0%** |
| eval_pi05_random_k07_object_v3 | libero_object | random | 0.7 | **74.0%** |
| eval_pi05_random_k03_goal | libero_goal | random | 0.3 | **51.0%** |
| eval_pi05_l2norm_k095_goal | libero_goal | l2norm | 0.95 | **90.8%** |
| eval_pi05_l2norm_k03_goal | libero_goal | l2norm | 0.3 | **54.2%** |

**异常:** `eval_pi05_random_k05_spatial_seed42` 日志仅 2176 bytes，只有初始化输出后中断，疑似 crash。

---

### westd-27271 (2×RTX PRO 6000 48GB)

| GPU | 显存 | 利用率 | 状态 |
|-----|------|--------|------|
| 0 | 15964/97887 MiB | 86% | 运行中 |
| 1 | 15964/97887 MiB | 72% | 运行中 |

**运行中 (2个):**
- PID 486402 (GPU 0): `eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.5 --suite libero_goal --seed 42`
  - 进度: Task 5/10, 当前 "put the bowl on top of the cabinet" ep 40/50, 启动于 08:14
- PID 500676 (GPU 1): `eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.5 --suite libero_goal --seed 42`
  - 进度: Task 4/10, 当前进入 "open the top drawer", 启动于 09:05

**今日已完成实验 (2个):**

| 实验 | Suite | 方法 | SR |
|------|-------|------|----|
| eval_openvla_baseline_long | 10-task goal | baseline | **52.8%** |
| eval_openvla_l2norm_k05_goal_v3 | goal | l2norm k=0.5 | **43.4%** |

---

**总结:** cqa1 有 3 块 GPU 空闲，1 块在跑最后一个 pi05 l2norm k=0.85 goal seed43（接近完成，8/10 tasks）。westd 两块 GPU 满载运行 OpenVLA goal 评估。需关注 cqa1 上 spatial random k=0.5 实验的异常中断。

---
