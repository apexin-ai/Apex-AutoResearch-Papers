# ssh check kl training

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-kl-training_20260515T131130_result.json`
- **Structured JSON:** [`2f4006ce71bab70bbf0b.json`](../../sessions/2f/2f4006ce71bab70bbf0b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## mvp_kl_s42 训练状态报告

### 进程状态：存活，正常运行

| 指标 | 值 |
|------|-----|
| Python PID | 53759（bash wrapper 53754 → timeout 53758 → python 53759）|
| 状态 | `Sl`（多线程运行中），~300 线程 |
| CPU | 100% |
| 运行时间 | ~35 分钟 |

### 显存

| GPU | 使用 / 总量 | 利用率 |
|-----|------------|--------|
| cuda:0 | 88317 / 97887 MiB (90.2%) | 100% |
| cuda:1 | 69443 / 97887 MiB | 100% |

### 已完成 steps：**未知**

日志仅 6 行——模型加载完成 + 2 条 warning 后再无输出。Checkpoint 目录为空。

**原因：Python stdout 缓冲。** stdout 重定向到文件后，Python 使用 ~8KB 全缓冲而非行缓冲。训练循环的 print 输出还没有 flush 到磁盘。

### 判断

训练**大概率在正常进行**：
- GPU 利用率 100%，显存 88GB，符合 LLaMA-3.1-8B KL 蒸馏的预期
- Python 进程活跃（300+ 线程，100% CPU）
- 无 crash、无 OOM

但**无法确认具体进度**（step 数、loss 值、速度），也无法估算完成时间。

### 建议

未来启动时加 `PYTHONUNBUFFERED=1` 或 `python -u`，确保日志实时输出。当前这个 run 只能等 buffer flush 或进程结束后才能看到 step 日志。

---
