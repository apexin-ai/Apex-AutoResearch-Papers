# deploy westd38929 cuda2 goal random

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_westd38929_cuda2_goal_random_20260522T184557_result.json`
- **Structured JSON:** [`34c8fd0fe3f368f4d7b1.json`](../../sessions/34/34c8fd0fe3f368f4d7b1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成。

## 汇报

### cuda:2 部署结果
- **实验**: `eval_pi05_random_k085_goal_seed42_v3` — π0.5 Random k=0.85 LIBERO-Goal
- **PID**: 960809，VRAM 已升至 ~7.9 GB（模型加载中）
- **Registry**: RUNNING

### 四卡身份表

| GPU | VRAM | PID | 实验 |
|-----|------|-----|------|
| cuda:0 | 10506 MiB | 781071 | π0.5 L2Norm k=0.85 libero_10 (LONG) |
| cuda:1 | 10005 MiB | 892027 | π0.5 L2Norm k=0.7 libero_10 |
| cuda:2 | 3167→加载中 | 960809 | **π0.5 Random k=0.85 libero_goal** ← 刚部署 |
| cuda:3 | 10364 MiB | 781144 | π0.5 Random k=0.95 libero_10 (LONG) |

### 需确认
- cuda:1 的 `eval_pi05_l2norm_k070_long_seed42` 是否已在 Registry 中注册？（PID 892027, l2norm k=0.7 libero_10）

---
