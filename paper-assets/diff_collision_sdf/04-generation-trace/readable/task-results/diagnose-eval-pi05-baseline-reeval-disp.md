# diagnose eval pi05 baseline reeval disp

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_pi05_baseline_reeval_disp_20260526T070553_result.json`
- **Structured JSON:** [`58d02c08871113d33914.json`](../../sessions/58/58d02c08871113d33914.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### 1. 失败根因：被新实验抢占 GPU 导致 SIGTERM

**不是 OOM，不是系统超时。** 证据：

- EXIT_CODE=143 = SIGTERM（signal 15），OOM killer 用的是 SIGKILL（signal 9, exit code 137）
- GPU 1 显存仅用 ~8.8GB / 97.9GB，无内存压力
- 日志无任何 error/exception，干净地打印 `Terminated`

**时间线重建：**
| 时间 | 事件 |
|------|------|
| 12:44 | eval_pi05_baseline_reeval_disp 启动，GPU 1 |
| 12:45–14:44 | 完成 Task 0/1/2（各200 episodes，~40min/task） |
| 14:44–14:50 | Task 3 运行到 Episode 30/200 |
| ~14:50 | 收到 SIGTERM，进程被杀 |
| 15:02 | 新的 sanity check 实验启动在 GPU 1（`/tmp/pi05_full_eval.log` 中可见） |
| 15:02 | 产出 `sanity_check_pi05_base_rotation_fix.json` |

**结论：实验被杀是为了给 sanity check 让出 GPU 1。** 可能是手动 kill 或调度系统所为。

### 2. 部分结果可挽救

日志中有 3 个 task 的完整结果（但无 JSON 文件产出，脚本只在全部完成后才写文件）：

| Task | 内容 | TSR | CAR | Smoothness | Max Disp |
|------|------|-----|-----|------------|----------|
| 0 | orange juice → basket | 0% | 70% | 0.001372 | 0.0131m |
| 1 | chocolate pudding → basket | 0% | 100% | 0.002167 | 0.0000m |
| 2 | milk → basket | 0% | 100% | 0.001369 | 0.0000m |
| 3 | bbq sauce → basket | 仅 30/200 ep | — | — | — |
| 4 | 未启动 | — | — | — | — |

### 3. 重跑建议

- **用 tmux 启动**，避免被调度系统或超时机制打断
- GPU 1 当前有进程（PID 208628, 8.8GB），需等其结束或确认可共存
- 如果脚本支持 `--start_task` 参数，可从 Task 3 开始跑，省掉已完成的 ~2h
- 如果不支持断点续跑，完整重跑预估需 ~3.5h（5 tasks × ~40min）

---
