# probe v7 step10000 monitor

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_probe_v7-step10000-monitor_20260516T134042_result.json`
- **Structured JSON:** [`89e5d11332e9ba68b6b1.json`](../../sessions/89/89e5d11332e9ba68b6b1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

35 分钟后回来检查 checkpoint-10000。当前确认的状态：

1. **训练输出目录**：✅ 在数据盘 `/dev/md0` (250G)
2. **v7 训练**：Step 5800/20000, 1.8 steps/s — checkpoint-10000 预计 ~22:20 UTC 到达
3. **v5 eval**：❌ 已崩溃，无结果产出（log 56680 行全是 progress bar，停在 rollout 277/280）
4. **GPU 1**：完全空闲，可用于 seed2
5. **seed2 启动计划**：等 Probe A 完成确认后，用 `CUDA_VISIBLE_DEVICES=1` 启动（脚本原文写的是 0，需要覆盖）

---
