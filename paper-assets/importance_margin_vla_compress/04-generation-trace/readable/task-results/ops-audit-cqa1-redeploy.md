# ops audit cqa1 redeploy

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_audit_cqa1_redeploy_20260522T150615_result.json`
- **Structured JSON:** [`306b3091284fd725d847.json`](../../sessions/30/306b3091284fd725d847.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇报

### 服务器 westd-27271 只有 2 个 GPU，不是 4 个

| GPU | 显卡 | 显存占用 | 当前任务 |
|-----|------|---------|---------|
| 0 | RTX PRO 6000 Blackwell (98GB) | 4914 MiB | X-VLA Spatial L2norm k=0.95 |
| 1 | RTX PRO 6000 Blackwell (98GB) | 4856 MiB | X-VLA Goal L2norm k=0.95 |

**不存在 cuda:2,3。cuda:1 不空闲。**

### 4 个 tmux session

| Session | GPU | 当前进度 | 后续排队 |
|---------|-----|---------|---------|
| `xvla_spatial` | 0 | k=0.95, 某task Ep 37/50（大量SUCCESS） | → k=0.9 → k=0.7 |
| `xvla_goal` | 1 | k=0.95, Task 5 Ep 7/50（Task 4=18.0%，Task 5 全FAIL） | → k=0.9 → k=0.7 |
| `xvla_long` | 0 | "Waiting for xvla_spatial to finish..." | 排在 spatial 后面 |
| `xvla_random` | 1 | "Waiting for xvla_goal to finish..." | 排在 goal 后面 |

### 已完成的 X-VLA Baseline 结果
- **Spatial baseline**: 93.0% (465/500), max_steps=800
- **Goal baseline**: 98.4% (492/500), max_steps=800

### Goal k=0.95 实时观察
Task 4 "put the bowl on top of the cabinet" 从 baseline 100% 骤降到 18.0%（k=0.95 only 去掉 5% token）。Task 5 正在跑，前 7 个全 FAIL。**X-VLA 对 token pruning 极度敏感，和 π0.5 形成鲜明对比。**

### 之前的 Goal seed43 结果
eval_results 中**没有** pi05 goal seed43 的结果文件。

### SUITE_CONFIG
`eval_pi05_pruning_libero.py` 中 `libero_goal` max_steps=**400**，需要改为 300。

### 无法部署 π0.5 Goal Random
两个 GPU 都被 X-VLA 实验占满，每个 GPU 后面还排着 xvla_long / xvla_random。需要等 X-VLA 全部完成或手动 kill 才能腾出 GPU。

**建议**: 先把 SUITE_CONFIG 的 max_steps 修好，等 X-VLA 实验完成后再部署 π0.5 Goal Random。或者如果 X-VLA 优先级低于 π0.5，可以 kill 掉某个 session 腾 GPU。请指示。

---
