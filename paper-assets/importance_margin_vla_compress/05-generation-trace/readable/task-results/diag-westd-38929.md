# diag westd 38929

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_westd-38929_20260527T012815_result.json`
- **Structured JSON:** [`9879f437accdd65d0730.json`](../../sessions/98/9879f437accdd65d0730.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据已收集。结果如下：

## westd-38929 诊断结果

### 已完成实验（旧批次已全部结束）

| 实验 | SR | 耗时 | 结果文件 |
|---|---|---|---|
| **Random k=0.75 Goal s42** | **72.0% (360/500)** | 228.8 min | `openvla_random_prune_k075_goal_seed42.json` |
| L2norm k=0.5 Long s42 | 16.4% (82/500) | 666.6 min | `openvla_l2norm_prune_k05_10_seed42.json` |
| Random k=0.85 Long s42 v3 | 45.0% (225/500) | 559.8 min | `openvla_random_prune_k085_10_seed42.json` |
| Attn k=0.85 Long s42 v3 | 45.8% (229/500) | 548.6 min | `openvla_attention_prune_k085_10_seed42.json` |
| Attn k=0.7 Goal s42 | 66.4% (332/500) | 251.7 min | `openvla_attention_prune_k07_goal_seed42.json` |

### 当前运行中实验（新批次）

| GPU | PID | 实验 | 进度 | 状态 |
|---|---|---|---|---|
| 0 | 949253 | **Attn k=0.95 Goal** s42 | Task 1/10, Ep 30 | running |
| 1 | 949447 | **L2norm k=0.95 Long** s42 | Task 1/10, Ep 10 | running |
| 2 | 732931 | **L2norm k=0.75 Long** s42 | Task 9/10, Ep 20 | running (从01:30开始，近完成) |
| 3 | 950007 | **Attn k=0.95 Long** s42 | Task 1/10, Ep 10 | running |

### 关键发现

1. **Random k=0.75 Goal 已正常完成**，SR = 72.0%。进程消失是因为实验跑完了，不是崩溃。日志在 `/root/autodl-tmp/importance_margin_vla_compress/logs/eval_openvla_random_k075_goal_seed42.log`，需要补录 registry。

2. **GPU 2 的 L2norm k=0.75 Long** 已跑到 Task 9/10，预计很快完成。

3. GPU 0/1/3 上新启动了 3 个 k=0.95 实验（约 09:11 启动），都刚开始 Task 1。

---
