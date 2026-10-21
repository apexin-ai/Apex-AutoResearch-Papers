# ssh status check 10894

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_status-check-10894_20260528T232349_result.json`
- **Structured JSON:** [`33b4cd0a04651f6f601c.json`](../../sessions/33/33b4cd0a04651f6f601c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-10894 状态报告

### 训练进度: random_occ_v2_s0_r4 (PID 49565)

| 指标 | 值 |
|------|-----|
| 当前 step | **900 / 50,005** (1.8%) |
| 已运行 | 15h 02m |
| 速度 | ~1.01 s/it |
| 剩余 | ~49,105 steps ≈ **13.8h** |
| 预计完成 | ~05/30 05:00 UTC (北京 ~13:00) |
| Checkpoint | 目录已建，尚无 checkpoint（首次保存在 step 10,000）|

### Loss 趋势

| Step | occ_loss | action_loss |
|------|----------|-------------|
| 0 | 0.1068 | 0.6094 |
| 800 | 0.0428 | 0.2578 |
| 900 | 0.0417 | 0.2344 |

occ_loss ↓61%，action_loss ↓62%，两者持续下降，趋势正常。depth_loss 始终 0.0000（未启用）。

### GPU

| GPU | 型号 | 显存使用 | 显存空闲 | 总显存 | 占用进程 |
|-----|------|----------|----------|--------|----------|
| cuda:0 | RTX PRO 6000 Blackwell SE | 62 GB | 35 GB | 98 GB | PID 49565 |

**仅 1 张 GPU 可见**（cgroup 限制），无空闲 GPU。

### ⚠️ 时间风险

C003 deadline（2026-05-28 12:00 UTC）**已过**。此实验预计还需 ~13.8h 才能完成。

---
