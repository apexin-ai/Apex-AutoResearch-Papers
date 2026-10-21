# check gpu 2 3 training started

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_gpu-2-3-training-started_20260514T174628_result.json`
- **Structured JSON:** [`44a01971e1aed7cfc278.json`](../../sessions/44/44a01971e1aed7cfc278.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇报

### Westd GPU 2/3 — 8B 训练（第三次提交）

**结论：正常初始化中，尚未完成模型加载。**

| 实验 | PID (python) | 状态 | CPU RSS | GPU 显存 | 运行时间 |
|------|-------------|------|---------|----------|----------|
| CWM 8B v2 (cuda:2) | 266816 | **Rl** (running) | 3.7 GB | 0 MiB | ~3 min |
| CLS 8B s123 v2 (cuda:3) | 266896 | **Rl** (running) | 3.1 GB | 0 MiB | ~3 min |

- 两个 Python 进程都处于 **Rl**（actively running, multi-threaded）状态，CPU 内存持续增长中
- GPU 显存为 0 是因为 8B 模型正在加载到 CPU 内存（~16GB bf16），尚未 `.to(device)`
- 日志停在 `Class weights` 之后，下一步是模型加载 + checkpoint resume，对 8B 模型这需要几分钟
- **无 FileNotFoundError，无报错** — checkpoint 路径修复生效了（之前的 bug 在数据加载之前就会报错）

### Westd GPU 0/1 — 现有训练
- cuda:0: 12999 MiB, 86% util
- cuda:1: 12999 MiB, 87% util
- 正常运行中

### Home — CLS 8B val@5120 eval
- PID 3151214: **Rl+** 状态，已运行 **15 min 46 sec**，仍在执行中

**建议：3-5 分钟后再查一次，确认 GPU 2/3 显存已上升且日志出现 "Resuming training from checkpoint" 信息。**

---
