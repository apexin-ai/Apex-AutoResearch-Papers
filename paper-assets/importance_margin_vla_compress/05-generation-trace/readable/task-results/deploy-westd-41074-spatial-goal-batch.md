# deploy westd 41074 spatial goal batch

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_westd-41074-spatial-goal-batch_20260524T060754_result.json`
- **Structured JSON:** [`0929535e9388722c8ad2.json`](../../sessions/09/0929535e9388722c8ad2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**发现：GPU 并非全空闲。** 3 个 eval 实验正在运行（已跑约 54 分钟）：

| GPU | PID | 实验 | 状态 |
|-----|-----|------|------|
| 0 | 664277 | l2norm k=0.925 goal | 运行中 ≈ 与你的实验4重复 |
| 1 | — | — | **空闲** |
| 2 | 664353 | random k=0.85 spatial | 运行中（不在本次任务列表） |
| 3 | 664491 | l2norm k=0.85 spatial | 运行中 ≈ 与你的实验1重复 |

对比你要部署的 4 个实验：
- **实验1** (l2norm k=0.85 spatial) → **已在 GPU 3 运行**
- **实验2** (random k=0.95 spatial) → 可部署到 GPU 1
- **实验3** (random k=0.925 goal) → **无空闲 GPU**
- **实验4** (l2norm k=0.925 goal) → **已在 GPU 0 运行**

另外，`submit_training_job` 工具不在可用 MCP 工具列表中，需要用 `ssh_execute` + tmux 方式启动。

请确认：
1. 实验1和4已在跑，是否跳过？
2. 实验3是否等 GPU 空出后再部署，还是先只部署实验2？

---
