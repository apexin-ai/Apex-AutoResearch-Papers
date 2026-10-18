# diag all servers status 20260524

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_all-servers-status-20260524_20260523T182651_result.json`
- **Structured JSON:** [`f635f8a6cfbd1fd05904.json`](../../sessions/f6/f635f8a6cfbd1fd05904.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告

---

### 1. westd-38929 (4x RTX PRO 6000 Blackwell 96GB)

| GPU | Util | VRAM | 状态 |
|-----|------|------|------|
| 0 | 0% | 1 MiB | **空闲** |
| 1 | 0% | 1 MiB | **空闲** |
| 2 | 0% | 1 MiB | **空闲** |
| 3 | 50% | 5080 MiB | PID 153091 (未知进程) |

**4 个实验全部失败** — 参数错误 `--mode l2norm`，正确值应为 `l2_norm`（下划线）：
- `eval_xvla_l2norm_k05_spatial_seed42_v2` — FAILED (EXIT_CODE=2)
- `eval_xvla_l2norm_k05_goal_seed42_v2` — FAILED (EXIT_CODE=2)
- `eval_xvla_l2norm_k05_long_seed42_v2` — FAILED (EXIT_CODE=2)
- `eval_xvla_l2norm_k03_goal_seed42` — FAILED (EXIT_CODE=2)

GPU 3 上 PID 153091 不属于以上任何实验（原始 PID 均不匹配），来源未知。**GPU 0-2 空闲可用。**

---

### 2. westd-27271 (2x RTX PRO 6000 Blackwell 96GB)

| GPU | Util | VRAM | 状态 |
|-----|------|------|------|
| 0 | 0% | 1 MiB | **空闲** |
| 1 | 71% | 15916 MiB | PID 291098 |

| 实验 | 状态 | 结果 |
|------|------|------|
| eval_openvla_baseline_goal_seed42_v3 | **完成** | **SR=74.8% (374/500), 242.4min** |
| eval_openvla_baseline_long_seed42 | 运行中 | Task 4/10, ep 20/50 (~约完成 36%) |

---

### 3. westd-41074 (4x RTX PRO 6000 Blackwell 96GB)

| GPU | Util | VRAM | 状态 |
|-----|------|------|------|
| 0 | 0% | 10059 MiB | PID 728249 |
| 1 | 0% | 1 MiB | **空闲** |
| 2 | 35% | 10614 MiB | PID 530425 |
| 3 | 0% | 1 MiB | **空闲** |

| 实验 | 状态 | 结果 |
|------|------|------|
| eval_pi05_l2norm_k0925_goal_seed43 | 运行中 | T0 ep 30/50（刚启动） |
| eval_pi05_random_k0925_goal_seed42_v2 | **完成** | **SR=71.2% (356/500), 74.8min** |
| eval_pi05_random_k085_spatial_seed42_v2 | 运行中 | T9 ep 10/50（接近完成，~92%） |
| eval_pi05_l2norm_k085_spatial_seed42_v2 | **完成** | **SR=88.6% (443/500), 67.3min** |

**GPU 1, 3 空闲可用。**

---

### 4. cqa1-33015 (4x RTX 4090 D 24GB)

| GPU | Util | VRAM | 状态 |
|-----|------|------|------|
| 0 | 24% | 10196 MiB | PID 88440 |
| 1 | 25% | 10292 MiB | PID 88538 |
| 2 | 26% | 10294 MiB | PID 88688 |
| 3 | 32% | 10140 MiB | PID 97992 |

所有 4 个实验刚启动（时间戳 ~02:17-02:27），均在 Task 0-1 阶段：

| 实验 | 进度 | keep tokens |
|------|------|-------------|
| eval_pi05_random_k05_goal_seed42_v2 | T0 ep 40 | 128/256 |
| eval_pi05_random_k085_goal_seed42_v4 | T0 ep 50, SR=84% | 217/256 |
| eval_pi05_l2norm_k085_goal_seed42 | T0 ep 50, SR=94% | 217/256 |
| eval_pi05_random_k03_goal_seed43_v2 | T0 ep 10 | 76/256 |

**满载，无空闲 GPU。**

---

### 已收割的完成结果汇总

| 实验 | 模型 | Pruning | Keep | Suite | SR | Time |
|------|------|---------|------|-------|----|------|
| openvla_baseline_goal_seed42_v3 | OpenVLA | baseline | 1.0 | goal | **74.8%** | 242min |
| pi05_random_k0925_goal_seed42_v2 | π0.5 | random | 0.925 | goal | **71.2%** | 75min |
| pi05_l2norm_k085_spatial_seed42_v2 | π0.5 | l2norm | 0.85 | spatial | **88.6%** | 67min |

### 需要处理的问题

1. **westd-38929 全部失败**：4 个 xvla 实验启动参数 `--mode l2norm` 应为 `--mode l2_norm`。3 个 GPU 空闲等待重跑。
2. **westd-38929 GPU 3 未知进程** PID 153091，占用 5GB 显存，需要确认身份。
3. **westd-41074 GPU 1/3 空闲**，可部署新实验。

---
