# ops deploy pipeline script

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_deploy_pipeline_script_20260518T235812_result.json`
- **Structured JSON:** [`9c20684ae2adc347c50f.json`](../../sessions/9c/9c20684ae2adc347c50f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已部署并启动：

- **PID**: 22667（实际执行脚本的进程）
- **日志**: 已创建，输出 `Pipeline started at Tue May 19 07:58:50 CST 2026`，当前状态 `Waiting for v7...`（每 60 秒轮询 v7 训练完成标志）

v7 训练完成后会自动依次执行 eval GAR-ours、eval GAR-Dongre、启动 UG baseline 训练。

---
