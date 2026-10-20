# check mvp seed0 replication r2 progress

**collapse aware mixing** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_mvp_seed0_replication_r2_progress_20260514T054653_result.json`
- **Structured JSON:** [`3128fdd649e762b70a44.json`](../../sessions/31/3128fdd649e762b70a44.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告：mvp_seed0_replication_r2

### 进程状态
- PID 122208 **仍在运行**，日志最后更新 13:47 CST（刚刚）

### 当前阶段
- **G0 训练** ✅ 完成（305 steps, ~20M tokens, 21min）
- **G0 评估** ✅ 完成（6 checkpoints 全部评估完毕）
- **G1 合成数据生成** 🔄 进行中：**135/306 batches (44%)**
  - 速度：~78.5s/batch
  - 已耗时：~2h58m
  - 剩余：~171 batches → **~3h43m**

### G0 指标摘要
| 指标 | checkpoint-76 (5M) | final (20M) |
|------|-------------------|-------------|
| Perplexity | 13.53 | 13.27 |
| Spectral Effective Rank | 679.7 | 676.9 |
| Vocab Coverage | 46.8% | 46.8% |

训练过程中 perplexity 稳步下降，effective rank 略降（正常）。

### 预计剩余时间
| 阶段 | 预计耗时 |
|------|---------|
| G1 生成（剩余） | ~3h43m |
| G1 训练 | ~21m |
| G1 评估 | ~1h40m |
| G2 生成 | ~6h40m |
| G2 训练 | ~21m |
| G2 评估 | ~1h40m |
| **合计** | **~14h05m** |

**预计完成时间：~05/15 03:50 CST（UTC 19:50）**

### 磁盘空间
- output_seed0 当前占用：**31GB**
- 数据盘剩余：**117GB / 250GB (46% 空闲)**
- 每代约 30GB（含 checkpoints），3 代总计 ~90GB，空间充足

### 异常
- 无。生成速度稳定（~78.5s/batch），无报错。
- padding_side 警告可忽略（不影响结果）。

---
