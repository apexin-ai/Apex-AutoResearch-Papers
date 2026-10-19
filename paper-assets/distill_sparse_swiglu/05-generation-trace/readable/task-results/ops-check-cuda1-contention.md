# ops check cuda1 contention

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_cuda1_contention_20260516T045521_result.json`
- **Structured JSON:** [`95e65340a44d58afa883.json`](../../sessions/95/95e65340a44d58afa883.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### GPU 状态

| GPU | 进程 | PID | 显存占用 | GPU 利用率 |
|-----|------|-----|---------|-----------|
| cuda:0 | d030_kl50_uniform (benchmark_eval.py) | 203707 | 66,988 MiB / 97,887 MiB | 92% |
| cuda:1 | bce_isocompute_v3_s42 (训练) | 205598 | 90,938 MiB / 97,887 MiB | 100% |

### PID 204280 (bench_kl70_s42)
**已自行退出**，不在进程列表中，cuda:1 上无残留。无需 kill。

### BCE v3 训练进度 (cuda:1)
- **Step 900/2700** (33.3%)，运行 942.6s (~15.7 min)
- 速度稳定：**1.05s/step**
- 最新指标：loss=0.6366, bce=0.6351, reg=0.0015, sparsity=0.513
- loss 呈下降趋势（0.6660 → 0.6366），训练正常
- 预计剩余 ~31 分钟完成

### d030_kl50_uniform 评估进度 (cuda:0)
- 正在执行 GSM8K generate_until 任务：**657/1319** (50%)
- 之前的 loglikelihood 任务（wikitext2, arc_challenge, winogrande, mmlu）已完成
- 速度 ~1.2 it/s，预计还需 ~8 分钟完成 GSM8K

### 结论
两张 GPU 各跑一个进程，无竞争，状态健康。bench_kl70_s42 已自行结束，无需干预。

---
