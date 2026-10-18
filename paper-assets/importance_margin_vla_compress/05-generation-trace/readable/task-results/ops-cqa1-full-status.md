# ops cqa1 full status

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cqa1_full_status_20260517T080638_result.json`
- **Structured JSON:** [`c1a31c2f858d1cde2596.json`](../../sessions/c1/c1a31c2f858d1cde2596.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态检查报告

### 磁盘
- `/root/autodl-tmp/`: 250G 总量，已用 217G，**剩余 34G (87%)**

### GPU 状态
| GPU | 状态 | 显存 | 进程 |
|-----|------|------|------|
| 0 | 空闲 | 0 MiB | 无 |
| 1 | 占用 | 2727 MiB | PID 14927 (batch64_v2) |
| 2 | 空闲 | 0 MiB | 无 (k07 已完成) |
| 3 | 空闲 | 0 MiB | 无 (k03 已完成) |

### train_acis_stage1only_k07 — 成功完成
- 10000/10000 步完成，日志确认 "stage1 complete"
- 最终 margin_loss: 0.1189 (step 9950)
- Checkpoint: `/root/autodl-tmp/importance_margin_vla_compress/checkpoints/libero_acis_stage1only_k07/stage1_done/checkpoint.pt` (878 MB)
- Registry 已更新为 DONE/success

### train_acis_stage1only_k03 — 成功完成
- 10000/10000 步完成，日志确认 "stage1 complete"
- 最终 margin_loss: 0.1879 (step 9950)
- Checkpoint: `/root/autodl-tmp/importance_margin_vla_compress/checkpoints/libero_acis_stage1only_k03/stage1_done/checkpoint.pt` (878 MB)
- Registry 已更新为 DONE/success

### batch64_v2 — 运行中
- PID 14927，运行 32 分钟，GPU 1 上
- 当前 step: **100/100000**，sps=0.1（grad_accum=16, effective_batch=64）
- loss: 1.5052 → 1.3758 → **0.6564**（快速下降中）
- 内存 (step 0): total=1007.5GB, avail=956.3GB, used=51.2GB — 无内存压力
- 预计总训练时间约 290 小时（~12 天），ETA ~5月29日

---
