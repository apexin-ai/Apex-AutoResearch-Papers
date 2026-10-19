# diagnose gpu contention check

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_gpu_contention_check_20260515T232846_result.json`
- **Structured JSON:** [`173c4e0fb7699f2de762.json`](../../sessions/17/173c4e0fb7699f2de762.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 争用检查报告

### 1. GPU 显存和利用率

| GPU | 型号 | 显存使用 | 利用率 |
|-----|------|---------|--------|
| GPU 0 | RTX PRO 6000 Blackwell (96GB) | 4,912 MiB / 97,887 MiB (5.0%) | **0%** |
| GPU 1 | RTX PRO 6000 Blackwell (96GB) | 17,877 MiB / 97,887 MiB (18.3%) | **97%** |

### 2. 各进程 GPU 占用

| PID | 任务 | GPU | 显存 | 运行时间 | CPU% |
|-----|------|-----|------|---------|------|
| 471056 | baseline_plus eval (libero_goal) | GPU 0 | 5,368 MiB | 14m44s | 1844% |
| 308788 | baseline_std eval (libero_object) | GPU 1 | 2,135 MiB | 1h58m | 2264% |
| 497308 | acib_v3_train | GPU 1 | 16,214 MiB | 2m37s | 967% |

注意：训练实际 PID 是 **497308**（非任务描述中的 497303），`--gpu 0` 通过 `CUDA_VISIBLE_DEVICES=1` 映射到物理 GPU 1。

### 3. 训练 loss 趋势

训练刚启动约 2.5 分钟，仅到 step 100/20000：
- Step 100: **loss=0.0501** (task=0.0449, ib=0.0599, β=0.0000 warmup 中)
- 训练速度：**~1.0 steps/s**
- 数据太少，无法判断趋势

训练日志中有一行 "Terminated" + EXIT_CODE=129 残留——来自之前一个被 SIGHUP 杀掉的进程，当前进程正常运行。

### 4. Eval episode 速度

baseline_std eval (GPU 1) rollout 步速：**2~8 it/s**（波动大），280 步/episode，估算单 episode 约 **40~56 秒**。无历史基线数据可对比，无法确认是否有减速。

baseline_plus eval (GPU 0) 独占 GPU，无争用参照。

### 5. 争用评估结论：**轻微**

- **显存**：GPU 1 仅用 18.3%（17.9GB / 96GB），远低于 80GB 阈值。**无显存争用。**
- **GPU 计算**：GPU 1 利用率 97%，主要由训练进程贡献。Eval 的推理请求需要和训练抢计算周期，存在**计算争用**。
- **实际影响**：eval 只需间歇性 GPU 推理（2,135 MiB 显存很小），大部分时间在 CPU 上跑环境仿真（CPU 2264%）。训练对 eval 的影响有限，但 eval 的 GPU 推理延迟会增加。
- **训练影响**：eval 的间歇推理对训练吞吐影响极小（eval 显存占比仅 2.2%）。

**结论：显存充裕，计算有轻微争用但两个任务的 GPU 使用模式互补（训练持续占用 vs eval 间歇推理），预计不会显著互相影响。可以继续共存。**

---
