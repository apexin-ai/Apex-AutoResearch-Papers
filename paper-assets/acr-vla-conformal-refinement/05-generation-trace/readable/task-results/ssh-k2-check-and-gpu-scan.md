# ssh k2 check and gpu scan

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_k2-check-and-gpu-scan_20260519T214013_result.json`
- **Structured JSON:** [`19c1766dc79bc8c2d5ed.json`](../../sessions/19/19c1766dc79bc8c2d5ed.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据已收集。汇总如下：

---

## 任务 1: K=2 L2 校准状态

- **PID 995736**: 仍在运行，已耗时 **1h08m**，CPU 358%，内存 ~10GB
- **命令**: `calibrate_fmvd.py --benchmark object --n_episodes 5 --seed 42 --output logs/k2_l2_calibration.json`
- **输出文件**: `k2_l2_calibration.json` **尚未生成**
- **进度**: 已完成 8237/~14500 步 (**~57%**)，当前在 `pick_up_the_tomato_sauce` ep 3/5，预计还需 **~50 分钟**
- **参考**: 之前 `fmvd_calibration.json`（K=10）的 Spearman ρ = **0.0825**（远低于 0.3 阈值）

**Go/No-Go**: 待定——K=2 L2 结果尚未产出。若与 K=10 基线（ρ=0.08）一致，则大概率 **No-Go**。

---

## 任务 2: 全服务器 GPU 扫描汇总

### bjb2-28827（6× RTX 4090）

| GPU | 显存占用 | 利用率 | 状态 | 进程 |
|-----|---------|--------|------|------|
| cuda:0 | 1/24564 MiB | 0% | **空闲** | — |
| cuda:1 | 3378/24564 MiB | 27% | 占用 | PID 995736 — K=2 L2 calibration (miniconda python) |
| cuda:2 | 1/24564 MiB | 0% | **空闲** | — |
| cuda:3 | 1/24564 MiB | 0% | **空闲** | — |
| cuda:4 | 23006/24564 MiB | 42% | 占用 | PID 900134 — OpenVLA (python) |
| cuda:5 | 1/24564 MiB | 0% | **空闲** | — |

**可用**: cuda:0, 2, 3, 5 (4 GPU 空闲)

### bjb1-18228（4× RTX 4090）

| GPU | 显存占用 | 利用率 | 状态 | 进程 |
|-----|---------|--------|------|------|
| cuda:0 | 5706/24564 MiB | 29% | 占用 | PID 160888 (miniconda python) |
| cuda:1 | 7510/24564 MiB | 85% | 占用 | PID 132329 (python, 1889M) + PID 161154 (miniconda python, 5587M) |
| cuda:2 | 5166/24564 MiB | 22% | 占用 | PID 161421 (miniconda python) |
| cuda:3 | 1815/24564 MiB | 38% | 占用 | PID 132125 (python) |

**可用**: 无 (4/4 全占用)

### bjb1-32546（6× RTX 4090）

| GPU | 显存占用 | 利用率 | 状态 | 进程 |
|-----|---------|--------|------|------|
| cuda:0 | 4077/24564 MiB | 23% | 占用 | PID 105899 (miniconda python) |
| cuda:1 | 2/24564 MiB | 0% | **空闲** | — |
| cuda:2 | 4222/24564 MiB | 0% | 占用 | PID 106169 (miniconda python) |
| cuda:3 | 2/24564 MiB | 0% | **空闲** | — |
| cuda:4 | 3021/24564 MiB | 21% | 占用 | PID 86797 (miniconda python) |
| cuda:5 | 2502/24564 MiB | 22% | 占用 | PID 88043 (miniconda python) |

**可用**: cuda:1, 3 (2 GPU 空闲)

### bjb2-40593（1× RTX 4090 D）

| GPU | 显存占用 | 利用率 | 状态 | 进程 |
|-----|---------|--------|------|------|
| cuda:0 | 4496/24564 MiB | 11% | 占用 | PID 628941 (python) |

**可用**: 无

---

### 总览

| 服务器 | 总 GPU | 空闲 | 可部署 |
|--------|--------|------|--------|
| bjb2-28827 | 6 | 4 | cuda:0, 2, 3, 5 |
| bjb1-18228 | 4 | 0 | — |
| bjb1-32546 | 6 | 2 | cuda:1, 3 |
| bjb2-40593 | 1 | 0 | — |
| **合计** | **17** | **6** | |

---
