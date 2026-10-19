# ssh gpu health and sweep check

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_gpu-health-and-sweep-check_20260520T022429_result.json`
- **Structured JSON:** [`17ed70e94fd1845bf815.json`](../../sessions/17/17ed70e94fd1845bf815.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据收集完毕。

---

## Sweep 实验健康状态报告

### 一、已完成实验（4个 JSON）

| 实验 | 服务器 | SR | avg_K | fast_path_ratio | total/fast/full steps |
|------|--------|-----|-------|-----------------|----------------------|
| **p90_seed43** | bjb2-28827 | 0.14 | 2.612 | 92.3% | 27935 / 25797 / 2138 |
| **p90_seed42** | bjb1-32546 | 0.12 | 2.672 | 91.6% | 28258 / 25886 / 2372 |
| **p75_seed44** | bjb1-32546 | 0.16 | 3.022 | 87.2% | 27724 / 24181 / 3543 |
| **p50_seed44** | bjb1-32546 | 0.14 | 3.909 | 76.1% | 28067 / 21368 / 6699 |

趋势清晰：threshold 越高（p90），fast_path_ratio 越高（~92%），avg_K 越低（~2.6）；p50 threshold 触发更多 full inference（fast_path 降到 76%）。

### 二、运行中实验 & 进度

**bjb2-28827**（6 GPU，5 个实验）：

| 实验 | GPU | 当前任务 | 进度 |
|------|-----|----------|------|
| p75-seed42 | GPU1 | orange_juice (10/10), rollout 5/10 | ~95% |
| p75-seed43 | GPU4 | orange_juice (10/10), rollout 5/10 | ~95% |
| p50-seed42 | GPU5 | chocolate_pudding 完成，进入 orange_juice | ~90% |
| p90-seed44 | GPU2 | chocolate_pudding 完成 | ~90% |
| p25-seed43 | GPU0 | butter 完成 (task 7/10) | ~70% |

**bjb1-32546**（6 GPU，3 个实验）：

| 实验 | GPU | 当前进度 |
|------|-----|----------|
| p25-seed42 | GPU5 | orange_juice rollout 5/10 | ~95% |
| crm-spatial-seed48 | GPU1 | black_bowl_next_to_cookie_box 9/10 | progressing |
| vla-only-spatial-seed47 | GPU3 | black_bowl_in_top_drawer 1/10 | progressing |

**bjb1-18228**（4 GPU，4 个实验）：

| 实验 | GPU | 当前进度 |
|------|-----|----------|
| p50-seed43 | GPU3 | milk rollout 5/10 (task 8/10) | ~75% |
| crm-spatial-seed47 | GPU2 | black_bowl_next_to_cookie_box 9/10 | progressing |
| vla-only-object-seed49-r2 | GPU0 | tomato_sauce rollout 5/10 (task 6/10) | ~55% |
| vla-only-spatial-seed50 | GPU1 | black_bowl_in_top_drawer 0/5 | progressing |

**bjb2-40593**（1 GPU，1 个实验）：

| 实验 | GPU | 当前进度 |
|------|-----|----------|
| p25-seed44 | GPU0 | bbq_sauce 完成 (task 4/10) | ~40% |

### 三、GPU 利用率

| 服务器 | GPU 利用率 | 显存占用 |
|--------|-----------|---------|
| bjb2-28827 | 17-21%（6卡） | 1.9-2.4 GiB/卡 |
| bjb1-32546 | 0/36/0/18/0/32%（3卡活跃） | 活跃卡 2.0-3.6 GiB |
| bjb1-18228 | 22/20/25/27%（4卡） | 2.4-4.1 GiB/卡 |
| bjb2-40593 | 12%（1卡） | 4.1 GiB |

GPU 利用率 12-36% 是 LIBERO eval 的正常模式——大部分时间花在 MuJoCo 仿真渲染和环境步进（CPU-bound），GPU 仅在模型推理时被调用。

### 四、健康状态

- **无 hang/stuck 进程**：所有实验 log 均显示持续推进
- **所有 Python 进程 CPU 占用 300-530%**，正常（多线程仿真）
- bjb2-28827 的 4 个实验（p75×2, p50, p90）预计 30-60 分钟内完成
- bjb1-32546 的 p25-seed42 预计 15-30 分钟完成
- bjb2-40593 的 p25-seed44 进度最慢（~40%），预计还需 1.5-2 小时

---
