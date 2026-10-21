# deploy cqa1 goal random and investigate

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_cqa1_goal_random_and_investigate_20260522T154618_result.json`
- **Structured JSON:** [`e6444c247f5010076022.json`](../../sessions/e6/e6444c247f5010076022.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

cuda:1 还在加载模型（π0.5 模型较大，加载需要几分钟）。进程正常运行中，VRAM 还没上来是因为模型权重还在 CPU → GPU 传输阶段。

## 汇报

### cuda:1 — 部署完成
- **实验**: `eval_pi05_random_k085_goal_seed42_v2` — π0.5 Random k=0.85 on LIBERO-Goal
- **状态**: RUNNING，模型加载中（tmux session 正常，log 输出正常）
- **Registry**: 已注册

### cuda:2 — 已识别，不动
- **进程**: PID 435351, `eval_pi05_pruning_libero.py --suite libero_10 --prune_mode none --seed 43 --n_episodes 50`
- **身份**: **π0.5 baseline (no pruning) on LIBERO-Long, seed=43**
- **运行时间**: 2h18m，GPU-Util 19-23%，活跃运行中
- **决定**: 这是有意义的 baseline 实验，保留不动

### 四卡当前状态

| GPU | VRAM | Util | 实验 |
|-----|------|------|------|
| 0 | 15437 MiB | 62% | π0.5 Long baseline（不动） |
| 1 | 4 MiB (loading) | 0% | **新部署** π0.5 Random k=0.85 Goal seed42 |
| 2 | 10137 MiB | 19% | π0.5 baseline none Long seed43（不动） |
| 3 | 10298 MiB | 14% | 在跑（不动） |

---
