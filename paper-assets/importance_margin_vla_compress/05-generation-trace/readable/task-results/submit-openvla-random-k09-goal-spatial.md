# submit openvla random k09 goal spatial

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_openvla_random_k09_goal_spatial_20260524T230009_result.json`
- **Structured JSON:** [`f54ea3d782be15fd7d34.json`](../../sessions/f5/f54ea3d782be15fd7d34.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验**已经在运行中**，无需重复提交。

当前状态：
- **GPU0** `eval_openvla_random_k09_goal_seed42` — PID 936689，已运行约42分钟，GPU显存占用 15946 MiB
- **GPU1** `eval_openvla_random_k09_spatial_seed42` — PID 937175，已运行约38分钟，GPU显存占用 16028 MiB
- 两个 tmux session 均存活，进程 CPU 使用率 ~700%（正常）
- Registry 状态已为 RUNNING，hypothesis 已设置

日志目前只显示启动信息（模型加载 + Task 1 开始），episode 级别进度更新尚未刷出（tee 管道缓冲导致），但进程在正常运行。

同服务器 GPU2/GPU3 上还有 Attn k=0.85 Goal/Spatial 正在并行执行。

---
