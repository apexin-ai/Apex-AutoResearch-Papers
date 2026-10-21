# ops gpu status check

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_status_check_20260515T222746_result.json`
- **Structured JSON:** [`5c37af5318aea17af2fc.json`](../../sessions/5c/5c37af5318aea17af2fc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### PID 364466 — 存活
父 shell 进程存活，实际训练进程是 PID 364471（`curation_poc.py --phase finetune`），CPU 160%，正在运行。

### GPU 状态

| GPU | 型号 | 利用率 | 显存占用 |
|-----|------|--------|----------|
| GPU 0 | RTX PRO 6000 Blackwell | **61%** | 10,334 / 97,887 MiB |
| GPU 1 | RTX PRO 6000 Blackwell | **0%** | 3 / 97,887 MiB（空闲） |

### plan_013 finetune 进度
- 已完成 **2/40 runs**（`unfiltered/seed_42`, `unfiltered/seed_123` 含 adapter + PPL 结果）
- 当前正在跑第 3 个 run：`unfiltered/seed_456`，步数 37/939（~4%），速度 ~3.6 it/s
- 训练 loss 稳定在 ~1.65，PPL 结果 seed_123 = 15.83，正常
- 每个 run 约 262s（~4.5 min），40 个 run 预计总耗时 ~3 小时，已过 ~9 min

### plan_015 进程
- PID 365317：`plan_015_c4_supplement.py --gpu 0 --batch_size 16 --n_passages 5000`，CPU 175%，占用 ~19GB 内存，运行在 GPU 0 上

### 注意
GPU 0 同时跑着 plan_013 finetune 和 plan_015 c4_supplement 两个进程，目前显存占用 10.3GB / 97.9GB 尚有余量。GPU 1 完全空闲。

---
