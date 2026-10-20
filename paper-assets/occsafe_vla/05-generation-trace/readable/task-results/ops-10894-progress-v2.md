# ops 10894 progress v2

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_10894-progress-v2_20260526T212413_result.json`
- **Structured JSON:** [`44e9ee3cedce3132ae5f.json`](../../sessions/44/44e9ee3cedce3132ae5f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下：

| 实验 | GPU | 当前 step | 进度 | 速度 | 已运行 | ETA |
|------|-----|----------|------|------|--------|-----|
| **reverse_cutoff_s2_v2** | cuda:0 | 43075/50005 | **86.1%** | ~1.07 it/s | 12h22m | **~1h48m** (≈07:13 UTC) |
| **full_occ_ln_v2_s0** | cuda:1 | 10753/50005 | **21.5%** | ~1.00 it/s | 3h00m | **~10h51m** (≈16:16 UTC) |
| **full_occ_ln_v2_s1** | cuda:2 | 10716/50005 | **21.4%** | ~1.01 it/s | 3h00m | **~10h46m** (≈16:11 UTC) |
| **detach_ln_v2_s0** | cuda:3 | 10762/50005 | **21.5%** | ~1.01 it/s | 3h00m | **~10h45m** (≈16:10 UTC) |

**Checkpoints:**
- reverse_cutoff_s2_v2: 30000_chkpt, 40000_chkpt ✓
- full_occ_ln_v2_s0: 10000_chkpt ✓
- full_occ_ln_v2_s1: 10000_chkpt ✓
- detach_ln_v2_s0: 10000_chkpt ✓

**关键信息：**
- 4 张 GPU 满载（99%/99%/81%/99%），4 个进程全部健康
- reverse_cutoff_s2_v2 预计 ~07:13 UTC 完成（DDL 前约 29 小时）
- 其余 3 个实验预计 ~16:10-16:16 UTC 完成（DDL 前约 20 小时）
- 全部 4 个实验在 5/28 12:00 UTC DDL 前完成，无风险

---
