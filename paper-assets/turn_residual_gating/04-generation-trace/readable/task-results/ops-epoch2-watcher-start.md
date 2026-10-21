# ops epoch2 watcher start

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_epoch2_watcher_start_20260524T122043_result.json`
- **Structured JSON:** [`ea20614cfff1d41f6613.json`](../../sessions/ea/ea20614cfff1d41f6613.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**Watcher 已启动（PID 170077）**，日志确认正常运行：

- Watcher 日志：已检测到当前 Epoch 1 Step 3500/~7200，进入轮询
- 训练进度：Epoch 1 Step 3500，约 49% 完成第二个 epoch
- 触发条件：检测到 `Checkpoint saved to runs/p1_llama_ss_s42/epoch_1` 后自动 kill 训练

预计 epoch_1 完成还需约 ~5 小时（按当前速度），届时 watcher 会自动终止训练。

---
