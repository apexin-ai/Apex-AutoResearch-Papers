# ops 10894 progress check

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_10894-progress-check_20260526T191723_result.json`
- **Structured JSON:** [`62ad9b7b6ba8c7ad452a.json`](../../sessions/62/62ad9b7b6ba8c7ad452a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下：

## GPU 状态

| GPU | 利用率 | 显存占用 |
|-----|--------|----------|
| 0 | 99% | 62203 MiB |
| 1 | 41% | 62203 MiB |
| 2 | 99% | 63013 MiB |
| 3 | 31% | 62203 MiB |

## 实验进度

| 实验 | GPU | 当前 step | 总 step | 进度 | 速度 | 已运行 | 剩余预估 | 预计完成 (UTC) |
|------|-----|-----------|---------|------|------|--------|----------|----------------|
| **reverse_cutoff_s2_v2** | 0 | 35566 | 50005 | 71% | ~1.08 it/s | 10h14m | ~3h44m | **5/27 ~00:00** |
| **full_occ_ln_v2_s0** | 1 | 3140 | 50005 | 6% | ~1.07 it/s | 52m | ~12h11m | **5/27 ~14:40** |
| **full_occ_ln_v2_s1** | 2 | 3117 | 50005 | 6% | ~1.07 it/s | 52m | ~12h07m | **5/27 ~14:35** |
| **detach_ln_v2_s0** | 3 | 3137 | 50005 | 6% | ~1.07 it/s | 52m | ~12h08m | **5/27 ~14:35** |

**reverse_cutoff_s2_v2** 预计今天 5/27 00:00 UTC 完成，DDL 前没问题。

**full_occ_ln_v2_s0 / s1 / detach_ln_v2_s0** 三个实验刚启动约 52 分钟，预计 5/27 14:35-14:40 UTC 完成，距 DDL（5/28 12:00 UTC）有 ~21h 余量，也没问题。

---
