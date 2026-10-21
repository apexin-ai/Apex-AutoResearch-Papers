# ops check gpu utilization

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-gpu-utilization_20260521T183341_result.json`
- **Structured JSON:** [`00e52d0c437339bb69ec.json`](../../sessions/00/00e52d0c437339bb69ec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据收集完毕。汇总如下：

---

## GPU 资源清查报告

### bjb1-18228 (4x RTX 4090)

| GPU | Util | VRAM | 状态 |
|-----|------|------|------|
| 0 | 10% | 557/24564 MiB | ✅ **crm-train-pi05-object-full** (epoch 2, batch 1400/1950) |
| 1 | 0% | 0 MiB | 空闲 |
| 2 | 0% | 0 MiB | 空闲 |
| 3 | 0% | 0 MiB | 空闲 |

磁盘: 根 53% (16G/30G), 数据盘 65% (161G/250G) — 数据盘偏满

### bjb1-32546 (6x RTX 4090)

| GPU | Util | VRAM | 状态 |
|-----|------|------|------|
| 0 | 29% | 9874/24564 MiB | ⚠️ **precompute-pi05-object shard1** (7100/7251, ~5min 即完成) |
| 1-5 | 0% | ~1 MiB | 空闲 |

磁盘: 根 33%, 数据盘 21% — 充裕

### bjb2-28827 (6x RTX 4090)

| GPU | Util | VRAM | 状态 |
|-----|------|------|------|
| 0-5 | ~20% | ~9874/24564 MiB | ⚠️ **precompute-pi05-spatial shards 0-5** (进度 ~7400/8607, ~45min 剩余) |

磁盘: 根 44%, 数据盘 21% — 充裕

### bjb2-40593 (1x RTX 4090 D)

| GPU | Util | VRAM | 状态 |
|-----|------|------|------|
| 0 | 14% | 9830/24564 MiB | 🔴 **残留进程** PID 872656 — 之前 precompute 尝试已失败(shard0 被 Terminated, obj-s0-r2 OOM 崩溃), 但进程仍占 GPU 显存 |

磁盘: 根 39%, 数据盘 44% (109G/250G)

---

### 总结

| 指标 | 数值 |
|------|------|
| 总 GPU | 17 |
| 正在训练 | 1 (bjb1-18228 cuda:0) |
| 正在 precompute | 7 (bjb1-32546 cuda:0 + bjb2-28827 cuda:0-5) |
| 残留需清理 | **1** (bjb2-40593 cuda:0, PID 872656) |
| 当前空闲 | **8** (bjb1-18228 cuda:1-3, bjb1-32546 cuda:1-5) |
| ~5min 后释放 | +1 (bjb1-32546 cuda:0) |
| ~45min 后释放 | +6 (bjb2-28827 cuda:0-5) |

### 需要操作

1. **bjb2-40593**: `kill 872656` 清理残留进程，释放 1 GPU
2. precompute 任务即将完成后会自动释放，不需要干预
3. bjb1-18228 数据盘 65% 偏高，后续注意清理旧 checkpoint

---
