# diag 10894 queue check

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_10894_queue_check_20260527T000407_result.json`
- **Structured JSON:** [`d71ef9efef15babc9676.json`](../../sessions/d7/d71ef9efef15babc9676.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### 总结：3 个实验均在 stall，GPU 利用率 0%

| 实验 | PID | 存活 | 运行时间 | 最新 step | 总 step | 速度 | 状态 |
|------|-----|------|----------|-----------|---------|------|------|
| `full_occ_ln_v2_s0b` | 458140 (子: 458224) | Yes | 9h33m | **479**/50005 | 50005 | 5.71 s/it | **STALL** |
| `full_occ_ln_v2_s1b` | 458300 (子: 458541) | Yes | 9h30m | **477**/50005 | 50005 | 5.79 s/it | **STALL** |
| `detach_ln_v2_s0b` | 458618 (子: 458889) | Yes | 9h27m | **478**/50005 | 50005 | 5.85 s/it | **STALL** |

### GPU 使用情况

| GPU | 利用率 | 显存占用 | 进程 |
|-----|--------|----------|------|
| cuda:0 | **0%** | 79788/97887 MiB | PID 428963 (16.7GB) + PID 433768 (63GB) — **不属于这 3 个实验** |
| cuda:1 | **0%** | 62203/97887 MiB | PID 458224 (full_occ_ln_v2_s0b) |
| cuda:2 | **0%** | 62203/97887 MiB | PID 458541 (full_occ_ln_v2_s1b) |
| cuda:3 | **0%** | 63013/97887 MiB | PID 458889 (detach_ln_v2_s0b) |

### 关键观察

1. **初始化耗时 ~7.5h**：进程在 05/26 23:54 UTC 启动，但 dataset 构建日志直到 05/27 07:55 UTC 才出现。启动到开始训练花了约 8 小时（可能是模型加载/数据加载瓶颈）。

2. **训练仅跑了 ~475-479 步后 stall**：三个实验的日志都显示相同模式——正常速度 ~1.07 it/s 持续到 ~step 440，然后突然出现剧烈减速（4-6 s/it），短暂恢复后再次 stall。这与前身实验（v2_s0, v2_s1）在 step 275 stall 的模式一致。

3. **GPU 利用率 0% + 显存已占用** = 进程 hang 住了，不在做计算。

4. **cuda:0 不空闲**：有两个其他进程（PID 428963 和 433768）占用了 ~80GB 显存，利用率也是 0%。

### 结论

三个实验全部 stall，和之前的 v2 实验相同症状。问题不在于偶发，而是系统性的——可能是数据加载管线 deadlock 或某个 CUDA 操作 hang。已按要求不杀进程。

---
