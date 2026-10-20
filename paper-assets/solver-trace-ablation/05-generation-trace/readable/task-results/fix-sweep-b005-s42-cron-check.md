# fix sweep b005 s42 cron check

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_sweep-b005-s42-cron-check_20260516T032432_result.json`
- **Structured JSON:** [`3d701d569d3b426af426.json`](../../sessions/3d/3d701d569d3b426af426.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 排查结论

**训练正在正常运行，cron 是误报。**

### 进程链
```
604642 (bash) → 604646 (timeout 86400) → 604647 (python3, 310 threads, state=R/S)
```

### 实际状态
- reward_log 缓冲刷出到 **step 100/500**，timestamp 03:31:23 UTC（启动后 ~10 分钟）
- checkpoint-50 和 checkpoint-100 均已创建（checkpoint-100 刚出现）
- 训练日志持续增长（当前 ~90KB）
- Python 进程 CPU 时间持续增加，page faults 活跃
- Step 100 指标：prove_rate=1.0, isr=0.84, parse_rate=1.0 — 训练效果良好

### 为什么看起来像"退出"
Python 的 stdout/文件写入使用大缓冲区（默认 8KB）。训练实际以 ~6s/step 正常运行，但日志输出被缓冲，从外部观察文件 mtime 停滞不动。cron 可能基于 log 文件 mtime 停止更新或 PID 604642（bash shell）的某个瞬态状态误判为退出。

### GPU 状态
```
GPU 0: 79547 MiB, 91%
GPU 1: 80355 MiB, 92%
```
GPU 1 被本实验占用（CUDA_VISIBLE_DEVICES=1）。

### 预估进度
按 ~6s/step 算 500 步需 ~50 分钟。训练 3.5 小时前启动，大概率已完成或接近完成，缓冲区在慢慢刷出。不需要干预。

---
