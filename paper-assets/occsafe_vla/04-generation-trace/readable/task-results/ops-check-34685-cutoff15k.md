# ops check 34685 cutoff15k

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_34685_cutoff15k_20260525T020829_result.json`
- **Structured JSON:** [`f0c760f4ddba95c92d8f.json`](../../sessions/f0/f0c760f4ddba95c92d8f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## cutoff_15k_s1 状态报告

**状态：仍在训练中，接近完成**

| 指标 | 值 |
|------|-----|
| 当前 step | 49,158 / 50,005 |
| 进度 | 98% |
| 速度 | ~1.08 it/s |
| 剩余 steps | ~847 |
| 预估剩余时间 | **~13 分钟** |
| 最新 loss (step 49100) | occ=0.0331, depth=0.0000, action=0.0574 |

**GPU 状态：** 4× GPU 全部 85-99% 利用率，各占用 62GB/98GB 显存

**Checkpoints（已保存 4 个）：**

| Checkpoint | 大小 |
|------------|------|
| 10000_chkpt | 15G |
| 20000_chkpt | 15G |
| 30000_chkpt | 15G |
| 40000_chkpt | 15G |
| **合计** | **60G** |

**磁盘：** `/root/autodl-tmp/` 350G 用了 245G，剩余 106G (70%)

---

训练约 13 分钟后完成，届时会生成 50000_chkpt（额外 15G）。完成后可清理中间 checkpoint（10K/20K/30K/40K），释放约 **60G** 空间。

---
