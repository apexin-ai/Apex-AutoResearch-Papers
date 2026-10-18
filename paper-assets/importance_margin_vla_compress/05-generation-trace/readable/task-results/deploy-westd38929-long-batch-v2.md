# deploy westd38929 long batch v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_westd38929_long_batch_v2_20260522T163448_result.json`
- **Structured JSON:** [`14428e524a1bfc534d69.json`](../../sessions/14/14428e524a1bfc534d69.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 Python 进程都在运行（各占 ~9GB 内存正在加载模型）。模型加载到 GPU 前会先在 CPU 内存中加载。

## 部署结果

| 实验 | exp_id | GPU | 状态 |
|------|--------|-----|------|
| π0.5 L2norm k=0.85 Long | `eval_pi05_l2norm_k085_long_seed42` | cuda:0 | RUNNING，模型加载中 |
| π0.5 Random k=0.95 Long | `eval_pi05_random_k095_long_seed42` | cuda:3 | RUNNING，模型加载中 |

## 四卡 GPU 状态

| GPU | VRAM 占用 | 状态 |
|-----|----------|------|
| cuda:0 | 4 MiB（CPU 加载中，即将上 GPU） | 新实验 - L2norm k=0.85 |
| cuda:1 | 2776 MiB | 已有任务，未动 |
| cuda:2 | 2510 MiB | 已有任务，未动 |
| cuda:3 | 3 MiB（CPU 加载中，即将上 GPU） | 新实验 - Random k=0.95 |

两个进程 PID 分别为 781071（cuda:0）和 781144（cuda:3），CPU 内存各占 ~9GB，正在将 π0.5 模型加载到 GPU。Registry 已注册为 RUNNING。

---
