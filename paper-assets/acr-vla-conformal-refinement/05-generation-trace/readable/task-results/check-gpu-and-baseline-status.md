# check gpu and baseline status

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_gpu-and-baseline-status_20260522T231625_result.json`
- **Structured JSON:** [`c73eb055e48f63e8f44a.json`](../../sessions/c7/c73eb055e48f63e8f44a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### 1. bjb1-32546 (6×4090)

| GPU | 显存占用 | 利用率 | 进程 |
|-----|---------|--------|------|
| 0 | 1 MiB | 0% | **空闲** |
| 1 | 1 MiB | 0% | **空闲** |
| 2 | 1 MiB | 0% | **空闲** |
| 3 | 542 MiB | 10% | `train_crm_unified_4suite_r4` (PID 322367) — epoch 28/50, batch 6300/6316 |
| 4 | 1 MiB | 0% | **空闲** |
| 5 | 1 MiB | 0% | **空闲** |

- **CRM 训练正常运行**，epoch 28 快结束，loss ~0.01
- **SmolVLA baseline eval 全部不在运行**。没有任何 `eval-smolvla-lerobot-*` 进程。只有一个 stale 的 tmux session `eval-pi05-crm-object-seed42`（无活跃 python 子进程）
- 空闲 GPU：**0, 1, 2, 4, 5**（5 张）

### 2. bjb2-28827 (6×4090)

| GPU | 显存占用 | 利用率 | 进程 |
|-----|---------|--------|------|
| 0 | 5730 MiB | 31% | SmolVLA CRM eval object seed42 |
| 1 | 5730 MiB | 32% | SmolVLA CRM eval object seed43 |
| 2 | 5730 MiB | 30% | SmolVLA CRM eval object seed44 |
| 3 | 1 MiB | 0% | **空闲** |
| 4 | 1 MiB | 0% | **空闲** |
| 5 | 1 MiB | 0% | **空闲** |

- **跑的不是 baseline eval，而是 SmolVLA CRM eval**（`--mode crm_obs_only --benchmark object`），3 个 seed (42/43/44)
- 三个 eval 都刚启动，日志停留在 "10 tasks loaded"，尚未输出 rollout 进度
- 空闲 GPU：**3, 4, 5**（3 张）

### 3. bjb1-18228 (4×4090)

| GPU | 显存占用 | 利用率 | 进程 |
|-----|---------|--------|------|
| 0 | 9884 MiB | 24% | π0.5 precompute object — 5300/72507 (7.3%) |
| 1 | 9884 MiB | 24% | π0.5 precompute spatial — 5200/60250 (8.6%) |
| 2 | 9883 MiB | 26% | π0.5 precompute goal — 5300/61728 (8.6%) |
| 3 | 9883 MiB | 25% | π0.5 precompute long — 5700/136090 (4.2%) |

- **4 张 GPU 全满**，cuda:3 在跑 long precompute（未被 kill）
- 速度 ~2s/sample，预估剩余时间：object ~37h, spatial ~31h, goal ~31h, long ~66h
- 磁盘：根分区 53% (15G 可用)，数据盘 78% (57G 可用)，暂无压力
- 空闲 GPU：**无**

### 关键发现

1. **SmolVLA baseline eval 没有在任何服务器上运行**。bjb2-28827 上跑的是 CRM eval（`--mode crm_obs_only`），不是 baseline（`--mode baseline`）
2. bjb1-18228 的 cuda:3 并未空闲，在跑 long benchmark precompute
3. bjb1-32546 有 5 张 GPU 空闲，可部署 baseline eval

---
