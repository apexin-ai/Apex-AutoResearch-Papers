# audit gpu health 34685 urgent

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_gpu-health-34685-urgent_20260527T211223_result.json`
- **Structured JSON:** [`452cd624d2fc3bddc237.json`](../../sessions/45/452cd624d2fc3bddc237.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
[2026-05-28 ~05:12 UTC]

GPU 0 (detach_ln_v2_s2): 崩溃 — step 20000/50005 — 04:52 UTC
GPU 1 (vanilla_object_s0): 崩溃 — step 15000/50005 — 04:53 UTC
GPU 2 (full_occ_ln_v2_s3): 存活 — step 16604/50005 — 正在跑 1.08it/s
GPU 3 (detach_ln_v2_s3):  存活 — step 16566/50005 — 正在跑 1.09it/s
```

**崩溃原因**: 两个实验都是 `No space left on device (os error 28)` — 在保存 checkpoint 时磁盘满。
- detach_ln_v2_s2: 保存 step 20000 checkpoint 时模型权重写入失败
- vanilla_object_s0: 保存 step 15000 checkpoint 时 tokenizer 写入失败

**最新可用 checkpoint**:
- detach_ln_v2_s2: **step 15000** (20000 checkpoint 不完整)
- vanilla_object_s0: **step 10000** (15000 checkpoint 不完整)

**磁盘现状**: `/root/autodl-tmp` 291G/350G (60G 可用)，根分区 12G/30G (19G 可用)。当时可能因 4 个实验同时写 checkpoint 导致瞬时磁盘满，现在进程退出后部分临时文件已释放。

**DDL 分析** (~6h48m 剩余):
| 实验 | 恢复点 | 剩余 steps | 预计耗时 | 能否在 DDL 前完成 |
|------|--------|-----------|---------|----------------|
| detach_ln_v2_s2 | step 15000 | 35005 | ~9h | **不能** |
| vanilla_object_s0 | step 10000 | 40005 | ~10.3h | **不能** |
| full_occ_ln_v2_s3 | 在跑 16604 | 33601 | ~8.6h | **略超** (~13:48 UTC) |
| detach_ln_v2_s3 | 在跑 16566 | 33439 | ~8.5h | **略超** (~13:42 UTC) |

**关键问题**: 崩溃的两个实验即使立刻 resume 也无法在 DDL 前跑完。存活的两个实验预计超 DDL 约 1.5-2h。需要你决定：
1. 崩溃实验是否仍需重启（接受超时）？
2. 是否需要先清理不完整的 checkpoint 释放磁盘空间，防止存活实验在 step 20000 保存时再次撞满？

---
