# ssh check exp003 training progress

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-exp003-training-progress_20260521T081216_result.json`
- **Structured JSON:** [`762099a9c5450b0a458c.json`](../../sessions/76/762099a9c5450b0a458c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### exp-003 (seed1) — PID 70649, cuda:1, westd-29046

| 指标 | 值 |
|------|-----|
| 运行时长 | 2d 15h 21m |
| 最新 checkpoint | **7500** (May 21 14:10) |
| 估算当前 step | ~7740 (基于 checkpoint 间隔推算) |
| 每 500 步耗时 | ~4h17m (ckpt-7000→7500) |
| 预计完成 (step 8000) | **今天 ~18:25** (~2h 后) |

> 无直接训练日志（log 文件只有 HF 下载记录），进度从 checkpoint 时间戳推算。

### exp-003-s2 (seed2) — PID 237432, cuda:0, westd-29046

| 指标 | 值 |
|------|-----|
| 运行时长 | 1d 7h 55m |
| 当前 step | **3641 / 8000** (45.5%) |
| 速度 | ~29.5s/step |
| 最新 checkpoint | **3500** (May 21 15:00) |
| 预计完成 | **May 23 ~04:00** (~35.7h 后) |

### Checkpoint 可用性

| Checkpoint | westd-29046 seed1 | westd-29046 seed2 | westd-28034 (eval) |
|:----------:|:-----------------:|:-----------------:|:------------------:|
| 500–3500   | ✅ (每500一个)     | ✅ (500–3500)     | ❌                  |
| 4000       | ✅                 | —                 | ✅                  |
| 4500       | ✅                 | —                 | ✅                  |
| 5000       | ✅                 | —                 | ✅                  |
| 5500       | ✅                 | —                 | ✅                  |
| 6000       | ✅                 | —                 | ✅                  |
| 6500       | ✅                 | —                 | ✅                  |
| **7000**   | ✅                 | —                 | ✅                  |
| **7500**   | ✅                 | —                 | ❌ 未同步           |
| **8000**   | ❌ 未生成          | —                 | ❌ 未生成           |

### 关键结论

- **checkpoint-7000**: 两台服务器都有 ✅
- **checkpoint-7500**: 仅在 westd-29046 训练机上，**未同步到 westd-28034 eval 服务器**
- **checkpoint-8000**: **尚未生成**，seed1 预计 ~2h 后产出（今天 18:25 左右）
- seed2 进度约 45%，与 seed1 差距约 4000 步，预计后天凌晨完成

---
