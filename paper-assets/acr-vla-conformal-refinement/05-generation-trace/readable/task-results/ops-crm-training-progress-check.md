# ops crm training progress check

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_crm-training-progress-check_20260521T185311_result.json`
- **Structured JSON:** [`318826aa9023e344b5d2.json`](../../sessions/31/318826aa9023e344b5d2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## π0.5 CRM Object Training 进度报告

### Object CRM Training (PID 800111 存活，已运行 38 分钟)
- **当前进度**: epoch 4, batch 1800/1950（约 3.92/50 epochs）
- **速度**: ~8.2 min/epoch
- **ETA**: 剩余 ~46 epochs × 8.2 min ≈ **6.3 小时**（约今天 09:00 完成）
- **Loss 趋势**: epoch 3 train=0.0103, val=0.005706（持续下降，单调收敛）
- **Checkpoint 目录**:
  - `checkpoint_epoch0001.pt`, `epoch0002.pt`, `epoch0003.pt`
  - `crm_best.pt`（2.5MB，对应 epoch 3 best val=0.005706）

### Spatial Precompute 状态
- **已完成 shards**: s0–s6（7 个 shard，s6 含 18 个 partial 至 8607）
- **未启动**: 没有 spatial precompute 进程，也没有 spatial training 进程
- **最后写入时间**: `partial_s6_8500_8607.pt` 在 02:17（~40 分钟前），之后无新文件
- **⚠️ 异常**: 任务描述说 "shards 在 15-16/18"，但当前文件仅到 s6。要么 precompute 进程崩溃停在 s6 后未启动 s7+，要么 shard 总数实际就是 7（spec 已变更）。需要确认 precompute 是否需要重新拉起处理 s7–s17

### GPU 使用情况（bjb1-18228，4× 24GB GPU）
| GPU | Mem | Util | 状态 |
|-----|-----|------|------|
| 0 | 557 MiB | 10% | object training（CRM head 小，利用率低正常） |
| 1 | 0 MiB | 0% | **空闲** |
| 2 | 0 MiB | 0% | **空闲** |
| 3 | 0 MiB | 0% | **空闲** |

GPU 1–3 完全空闲，可在 spatial precompute 重启或 spatial training 启动时使用。

---
