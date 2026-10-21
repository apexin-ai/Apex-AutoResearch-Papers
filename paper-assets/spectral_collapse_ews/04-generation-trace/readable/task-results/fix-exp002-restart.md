# fix exp002 restart

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_exp002_restart_20260516T125040_result.json`
- **Structured JSON:** [`d2b6d38cac0863ede5b1.json`](../../sessions/d2/d2b6d38cac0863ede5b1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

| 项目 | 状态 |
|------|------|
| **脚本 device 设置** | `config.device = "cuda:0"` (line 85) — 当前指向 cuda:0 |
| **cuda:1 状态** | **被占用** — PID 23220 (`python run_phase0_1b.py`)，显存 25636 MiB，利用率 95% |
| **cuda:0 (exp_001)** | 正常运行中 — PID 7406，显存 25008 MiB |
| **部分产出** | `checkpoints_1b/` 为空；`results/phase0_1b/phase0_1b_run.log` 存在（仅含 padding 警告） |

### 结论

**cuda:1 上已经有一个 `run_phase0_1b.py` 进程在运行**（PID 23220），GPU 利用率 95%，看起来是之前提交的 1B 训练正在正常执行中。这可能就是之前的 exp_002 提交——它已经在跑了。

需要你确认：
1. 这个 PID 23220 是否就是你之前提交的 exp_002？如果是，无需重新提交，等它跑完即可。
2. 如果需要重新提交（比如这个跑的是错误版本），需要先 kill 23220 释放 cuda:1。

---
