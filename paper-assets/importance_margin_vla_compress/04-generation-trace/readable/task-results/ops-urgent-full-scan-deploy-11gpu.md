# ops urgent full scan deploy 11gpu

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent_full_scan_deploy_11gpu_20260523T012919_result.json`
- **Structured JSON:** [`a6b9bc5f880d877a8d7a.json`](../../sessions/a6/a6b9bc5f880d877a8d7a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 扫描结果

| 服务器 | GPU | 状态 | 实验/备注 |
|--------|-----|------|----------|
| westd-38929 | 0 | **空闲** | Random k=0.9 Long s43 刚完成 (SR=30.8%) |
| westd-38929 | 1 | 🏃 10.9GB | L2norm k=0.7 Long s43 v2 — Task 3 |
| westd-38929 | 2 | 🏃 10.8GB | Random k=0.3 Long s43 v3 — Task 2 |
| westd-38929 | 3 | 🏃 10.0GB | L2norm k=0.85 Long s43 v2 — Task 4 |
| westd-27271 | 0 | **空闲** | L2norm k=0.3 Long s42 已完成 (SR=39.0%) |
| westd-27271 | 1 | **空闲** | L2norm k=0.5 Long s43 已完成 (SR=54.0%) |
| cqa1-33015 | 0 | **空闲** | — |
| cqa1-33015 | 1 | **空闲** | — |
| cqa1-33015 | 2 | 🏃 10.3GB | Random k=0.85 Goal s43 — Task 5 |
| cqa1-33015 | 3 | 🏃 10.5GB | L2norm k=0.85 Long s42 — Task 4 |
| westd-41074 | 0 | 🏃 10.5GB | Random k=0.85 Long s43 / Random k=0.5 Long s43 v2 |
| westd-41074 | 1 | 🏃 **新部署** 10.0GB | Random k=0.5 Spatial s43 v2 (PID 308908) |
| westd-41074 | 2 | 🏃 10.4GB | 进行中实验 |
| westd-41074 | 3 | 🏃 27.5GB | M64 训练 (train_openvla_sc_m64_v6_seed42) |

## 收割结果

| 实验 | SR | 状态 |
|------|-----|------|
| L2norm k=0.3 Long **seed42** | **39.0%** | ✅ DONE |
| L2norm k=0.3 Long **seed43** | **35.2%** | ✅ DONE |
| L2norm k=0.5 Long seed43 | **54.0%** | ✅ DONE |
| Random k=0.9 Long seed43 | **30.8%** | ✅ DONE (刚完成) |
| Random k=0.95 Goal seed42 | **84.0%** | ✅ DONE |
| L2norm k=0.85 Long seed43 v1 | failed | ✅ DONE (v2 已在跑) |
| Random k=0.3 Long seed43 v1 | failed | ✅ DONE (v3 已在跑) |
| L2norm k=0.7 Long seed43 v1 | failed | ✅ DONE (v2 已在跑) |

**cqa1-33015 上额外发现的已完成实验（未在 RUNNING registry）：**
- L2norm k=0.9 Long s42: **80.2%** | L2norm k=0.95 Long s42: **86.8%** | Baseline Long s42: **91.6%**
- Random k=0.3 Goal s42: **51.8%** | Random k=0.5 Goal s42: **74.4%** | Random k=0.7 Goal s42: **80.6%**
- L2norm k=0.7 Goal s42: **71.8%** | L2norm k=0.95 Goal s42: **89.4%**
- Random k=0.3 Goal s43: **52.0%** | L2norm k=0.7 Goal s43: **72.2%** | Random k=0.95 Goal s43: **83.2%**

## 部署结果

| GPU | 部署 | 状态 |
|-----|------|------|
| westd-41074:1 | Random k=0.5 Spatial s43 v2 | ✅ PID 308908, 9952 MiB |
| westd-27271:0 | ~~Random k=0.85 Goal s43~~ | ❌ 重复(cqa1已在跑)，已杀 |
| westd-27271:1 | ~~L2norm k=0.95 Spatial s43~~ | ❌ 已有DONE结果(98.0%)，已杀 |
| cqa1-33015:0 | ~~L2norm k=0.85 Spatial s43~~ | ❌ 已有DONE结果(88.0%)，已杀 |
| cqa1-33015:1 | ~~Random k=0.85 Spatial s43~~ | ❌ 已有DONE结果(57.6%)，已杀 |

## 异常

**用户列出的所有实验均已完成或正在运行：**
- Goal seed43: random k=0.85 🏃(cqa1), random k=0.95 ✅(83.2%), l2norm k=0.7 ✅(72.2%)
- Object seed43: random k=0.3 v3 ✅(32.2%), l2norm k=0.95 ✅(98.4%), l2norm k=0.85 ✅(98.4%)
- Spatial seed43: 全部 ✅ 或 🏃(random k=0.5 v2 重跑中)

**5 张空闲卡无实验可部署，需要新的实验列表：**
- westd-38929:0
- westd-27271:0, westd-27271:1
- cqa1-33015:0, cqa1-33015:1

## GPU 利用率

**9/14 GPU 在跑**（5 张空闲等待新任务）

---
