# diagnosis 29046 training status

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnosis_29046-training-status_20260521T074814_result.json`
- **Structured JSON:** [`2457647f0270004b1dbd.json`](../../sessions/24/2457647f0270004b1dbd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 训练状态汇总

### seed1 (exp-003, GPU 1, PID 70649)

| 项目 | 值 |
|------|-----|
| 估算当前 step | **~7690/8000** |
| 速度 | ~31s/step（ckpt-7000→7500 用了 4h17m） |
| ETA 完成 | **~18:30 CST 今天**（约 2h40m 后） |
| 已有 checkpoints | 500, 1000, 1500, ..., 7000, **7500** |
| ckpt-7500 | adapter_model.safetensors **245MB** ✓ 可 SCP |
| ckpt-8000 | **尚未生成** |

> 没有独立 log 文件（只有 tmux session），step 通过 ckpt 时间戳推算：ckpt-7500 在 14:10 保存，距今 1h38m ≈ 190 步。

### seed2 (exp-003-s2, GPU 0, PID 237437)

| 项目 | 值 |
|------|-----|
| 当前 step | **3592/8000 (45%)** |
| 速度 | ~30s/step |
| ETA 完成 | **~May 23 06:00 CST**（约 38h 后） |
| 已有 checkpoints | 500, 1000, 1500, 2000, 2500, 3000, 3500 |

两个训练都在正常跑，GPU 各占 ~38GB VRAM。seed1 的 ckpt-7500 已就绪可 SCP。

---
