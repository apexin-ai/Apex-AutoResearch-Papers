# ops post restart healthcheck

**tbab multi turn** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_post-restart-healthcheck_20260518T130159_result.json`
- **Structured JSON:** [`f631bb1266e3f71adf91.json`](../../sessions/f6/f631bb1266e3f71adf91.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 健康检查报告

### 1. GPU 状态
| 项目 | 值 |
|---|---|
| GPU | NVIDIA RTX PRO 6000 (cuda:0) |
| 温度 | 68°C |
| 功耗 | 423W / 600W |
| 显存 | 57,286 MiB / 97,887 MiB (58.5%) |
| GPU 利用率 | **100%** |
| GPU 进程 | PID 24985 (train.py, 40,236 MiB) + PID 25961 (run_eval.py, 17,036 MiB) |

### 2. train.py 进程
**存活** — PID 24985, 运行于 tmux session `mvp_c1_s137`
- 配置: `condition1_lora_only.yaml --seed 137`
- 启动时间: 18:50

### 3. run_eval 进程
**存活** — PID 25961
- 配置: `c1_lora_only_seed42`, tasks=code, n_repeats=1
- 启动时间: 18:54

### 4. mvp_c1_s137 训练进度
**431 / 471 steps (91.5%)** — 预计剩余 ~10 分钟（~15.7s/it）

### 5. C1_s42 eval 进度
- 已完成 results 文件: **1**
- Eval log 显示正在处理 **75 / 91 samples (82.4%)**
- 当前样本: `sharded-livecodebench/2882`

### 6. 异常
**无异常** — 两个进程均正常运行，GPU 满载工作。两个任务预计都将在约 10-20 分钟内完成。

---
