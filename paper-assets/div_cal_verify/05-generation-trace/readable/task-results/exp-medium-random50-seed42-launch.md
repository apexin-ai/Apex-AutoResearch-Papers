# exp medium random50 seed42 launch

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_medium_random50_seed42_launch_20260514T010130_result.json`
- **Structured JSON:** [`fb6dd7200f8d8debab46.json`](../../sessions/fb/fb6dd7200f8d8debab46.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**实验已经在跑了。**

结果：

1. **cuda:0 非空闲** — `medium_random50_seed42` 实验已在 cuda:0 上运行中
2. **启动命令**: `bash run_medium_random50.sh 0`（在 tmux session `chain_cuda0` 中）
3. **当前进度**: 已完成 gen_0 到 gen_5（6/8 代），正在跑 gen_6
4. **运行时长**: 已运行约 5 小时（PID 363296 启动于 07:42，累计 CPU 时间 305 分钟）

实验今天 03:32 创建 tmux session，07:42 实际启动进程。按照每代约 50 分钟估算，还剩 2 代（gen_6 + gen_7），预计再 ~1.5-2 小时完成。

需要我注册到 registry 并更新状态为 RUNNING 吗？

---
