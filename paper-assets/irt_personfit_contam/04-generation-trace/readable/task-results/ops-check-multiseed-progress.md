# ops check multiseed progress

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-multiseed-progress_20260522T140531_result.json`
- **Structured JSON:** [`8ddfcc17da0b48519f53.json`](../../sessions/8d/8ddfcc17da0b48519f53.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Multi-seed 训练进度汇报

### 正在训练
| 条件 | 进度 | GPU | ETA |
|------|------|-----|-----|
| `contam_25_s3` | **65%** (1049/1596 steps), epoch 1.90 | GPU 0 (27GB, 96%) | ~11 min |

### 已完成（checkpoint + results 齐全）

**Contam 条件：**
| 条件 | Seeds 完成 |
|------|-----------|
| `contam_5` | s1 |
| `contam_15` | s1, s2 |
| `contam_25` | s1, s2 (s3 训练中) |
| `contam_50` | s1 |

**Clean 条件：** s1-s10 全部完成

### GPU 状态
- GPU 0: `contam_25_s3` 占用 27GB/98GB
- GPU 1-3: **空闲**

### 无错误
训练日志正常，loss ~1.4，token accuracy ~0.65，无异常。`contam_25_s3` 预计约 11 分钟后完成。

3 张 GPU 空闲，如果需要启动更多 seed 的训练可以并行跑。

---
