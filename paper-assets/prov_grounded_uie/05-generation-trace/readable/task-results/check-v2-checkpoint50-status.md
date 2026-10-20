# check v2 checkpoint50 status

**prov grounded uie** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_v2_checkpoint50_status_20260513T074357_result.json`
- **Structured JSON:** [`5097f2df38f85b90a2cf.json`](../../sessions/50/5097f2df38f85b90a2cf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**grpo_pilot_v2 状态：**

| 项目 | 状态 |
|------|------|
| 当前进度 | **Step 47/100** (47%), 已运行 2h10m，预计还需 ~2h15m |
| checkpoint-50 | **未生成**，约 7-8 min 后到达 (≈152s/step) |
| 最新指标 | reward=**0.763**, loss=0.107, kl=0.004, clipped_ratio=0.0 |
| Watcher | 已启动，正在轮询等待 checkpoint-50 (attempt 2) |
| GPU | GPU 0 空闲; **GPU 1 活跃** 63%, 35.8/95.6 GB |

训练正常运行中，reward 从 step 46 的 0.689 上升到 step 47 的 0.763，趋势向好。checkpoint-50 预计约 7-8 分钟后生成，届时 watcher 会自动触发 eval。

---
