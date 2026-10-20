# monitor v7 status check

**collapse aware mixing** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_v7_status_check_20260513T030758_result.json`
- **Structured JSON:** [`a731ce9551b6176c88f9.json`](../../sessions/a7/a731ce9551b6176c88f9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## mvp_pilot_v7 状态报告

**进程：存活** (PID 60104 确认运行中)

**当前阶段：Generation 0 / 2 → 评估阶段**
- G0 训练已完成：305 steps, `train_loss = 2.593`, epoch 1.0, 耗时 ~771s
- 5 个 checkpoint 已保存：76, 152, 228, 304, 305
- 评估进度：checkpoint 1/6 已完成，**正在评估 checkpoint 2/6** (checkpoint-152)
- Checkpoint 1 指标：`eff_rank=679.7  ppl=13.53  entropy_var=2.8285  unigram_H=6.906  coverage=0.4686` (耗时 815s)

**GPU：** 0% utilization, 38479 / 97887 MiB 已用
- GPU 利用率 0% 是因为当前在做 perplexity 评估（CPU-bound 的 n-gram/entropy 计算），非异常

**无错误**，无 Traceback。

**预估进度：** G0 共 6 个 checkpoint 要评估，每个 ~815s（~13.5min），评估完 G0 后还有 G1、G2 两轮训练+评估。整体预计还需数小时。

---
