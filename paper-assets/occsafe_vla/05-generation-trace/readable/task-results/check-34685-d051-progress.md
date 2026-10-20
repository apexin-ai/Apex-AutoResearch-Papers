# check 34685 d051 progress

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_34685_d051_progress_20260525T192245_result.json`
- **Structured JSON:** [`5497f68c26c8590f3418.json`](../../sessions/54/5497f68c26c8590f3418.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 GPU 全部满载运行，全部存活。

| 实验 | GPU | Step | 进度 | 速度 | 剩余时间 | 预计完成 |
|------|-----|------|------|------|---------|---------|
| detach_bn_v2_s0 | cuda:0 (99%, 62GB) | 6406/50005 | 12.8% | ~1.08 it/s | ~11h16m | ~5/26 早晨 |
| detach_bn_v2_s1 | cuda:1 (97%, 62GB) | 6452/50005 | 12.9% | ~1.08 it/s | ~11h11m | ~5/26 早晨 |
| detach_bn_v2_s2 | cuda:2 (96%, 62GB) | 6445/50005 | 12.9% | ~1.07 it/s | ~11h18m | ~5/26 早晨 |
| full_occ_bn_v2_s1 | cuda:3 (99%, 62GB) | 4909/50005 | 9.8% | ~1.08 it/s | ~11h37m | ~5/26 早晨 |

**最新 loss (step 6400)**:
- s0: occ=0.0113, action=0.1318
- s1: occ=0.0242, action=0.1475
- s2: occ=0.0123, action=0.1357
- full_occ (step 4900): occ=0.0116, action=0.1729

full_occ_bn_v2_s1 比其他 3 个晚启动约 1500 步（~25min），但都将在明早完成。

---
