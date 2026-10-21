# ops gpu check westd 28034

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-check-westd-28034_20260521T103634_result.json`
- **Structured JSON:** [`995692802b08707cad2d.json`](../../sessions/99/995692802b08707cad2d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### GPU 使用情况

| GPU | 显存占用 | GPU利用率 | 占用进程 |
|-----|---------|----------|---------|
| cuda:0 | 16884/32607 MiB | 49% | PID 867046 — **exp003s2-ckpt3500** |
| cuda:1 | 16864/32607 MiB | 49% | PID 868607 — **exp003-ckpt8000** |
| **cuda:2** | **2/32607 MiB** | **0%** | **空闲** |
| cuda:3 | 16884/32607 MiB | 45% | PID 865026 — **exp003s2-ckpt2500** |

### 各 eval 进程状态

1. **exp003-ckpt8000** (PID 868607, GPU 1) — **存活，刚启动**。18:23 启动，模型已加载完成，正在跑 362 pairs eval。预估还需 ~60-70 分钟（参考 ckpt6000 用了 ~85 min）。

2. **exp003s2-ckpt3500** (PID 867046, GPU 0) — **存活**。18:02 启动，已运行 ~34 分钟，预计还需 ~50 分钟。

3. **exp003s2-ckpt2500** (PID 865026, GPU 3) — **存活，正在运行**。17:29 启动，已运行 ~67 分钟，预计还需 ~20 分钟。Registry 显示 RUNNING 是正确的，进程确实在跑，只是没有 cron 监控而已。

4. **exp-003-eval-ckpt6000** — 已完成（EXIT_CODE=0），tmux session 残留但进程已退出。

### 空闲 GPU

**cuda:2 完全空闲**，可立即使用。

### 已完成的 eval 结果（results/exp003_d027_eval/）

exp003 系列：ckpt1000–7500（含 5000-v2），共 10 个  
exp003s2 系列：ckpt2000、ckpt3000，共 2 个

---
