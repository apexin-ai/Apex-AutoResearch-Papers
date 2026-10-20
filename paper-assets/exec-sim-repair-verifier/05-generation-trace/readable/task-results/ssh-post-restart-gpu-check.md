# ssh post restart gpu check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_post-restart-gpu-check_20260520T092345_result.json`
- **Structured JSON:** [`1715ba4dc5bfe77d6393.json`](../../sessions/17/1715ba4dc5bfe77d6393.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 全面检查结果

### 1. GPU 状态总览

| GPU | 利用率 | 显存占用 | 总显存 | 温度 |
|-----|--------|----------|--------|------|
| 0 | 96% | 21255 / 32607 MiB | 76°C |
| 1 | 90% | 20251 / 32607 MiB | 75°C |
| 2 | 99% | 20001 / 32607 MiB | 73°C |
| 3 | 99% | 31261 / 32607 MiB | 73°C |

GPU 占用进程：
- PID 886278 → GPU 0, 21246 MiB
- PID 949112 → GPU 1, 20242 MiB
- PID 925638 → GPU 2, 19992 MiB
- PID 886352 → GPU 3, 31252 MiB

**4 块 GPU 全部满载运行。**

---

### 2. Qwen s123 (GPU 0, PID 886278) — ALIVE

```
运行时间: 07:54:08
命令: train_repo_cwm.py --seed 123 --device cuda:0 --epochs 3
```
- 日志进度: **72% (6706/9335)** epoch 内迭代，~8.35 it/s
- Checkpoints: checkpoint-300, 800, 900, 1000, **1100** (最新 16:50)

### 3. Qwen s456 (GPU 3, PID 886352) — ALIVE

```
运行时间: 07:54:07
命令: train_repo_cwm.py --seed 456 --device cuda:0 --epochs 3
```
- 日志进度: epoch 2 已完成 eval (9335/9335)，进入 epoch 3: **18% (1207/6633)**，~52 s/it（eval 后速度在恢复中）
- Checkpoints: checkpoint-300, 900, 1000, 1100, **1200** (最新 17:22)

### 4. DeepSeek s123-v2 (GPU 2, PID 925638) — ALIVE

```
运行时间: 03:40:55
命令: train_unified.py --seed 123 --model deepseek-coder-6.7b-instruct --epochs 3
包装进程 PID 925633 也存活
```
- 日志进度: **12% (1590/12627)**，~7.84 s/it，已训练 3h31m
- Checkpoint 目录: **空**（尚未保存第一个 checkpoint）
- training.log: 不存在（进度只在 tmux log 中）

### 5. DeepSeek s456-v2 (GPU 1, PID 949112) — ALIVE

```
运行时间: 00:19:51
命令: train_unified.py --seed 456 --model deepseek-coder-6.7b-instruct --epochs 3
```
- 日志进度: **step 84/12627**，~7.50 s/it，刚跑了约 11 分钟
- Checkpoint 目录: 有 training.log (6643 bytes)，**无 checkpoint 子目录**

---

### 汇总

| 任务 | GPU | PID | 状态 | 进度 | 最新 Checkpoint |
|------|-----|-----|------|------|----------------|
| Qwen s123 | 0 | 886278 | **ALIVE** | ~72% epoch内 | checkpoint-1100 |
| Qwen s456 | 3 | 886352 | **ALIVE** | epoch3 18% | checkpoint-1200 |
| DeepSeek s123-v2 | 2 | 925638 | **ALIVE** | 12% (1590/12627) | 无（目录空） |
| DeepSeek s456-v2 | 1 | 949112 | **ALIVE** | 0.7% (84/12627) | 无 |

**全部 4 个训练进程存活，无死亡进程。** 服务重启未影响训练。DeepSeek 两个任务尚未产生 checkpoint，需关注后续是否正常保存。

---
