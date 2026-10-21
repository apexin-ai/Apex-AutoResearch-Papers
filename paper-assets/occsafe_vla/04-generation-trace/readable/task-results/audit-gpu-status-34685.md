# audit gpu status 34685

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_gpu-status-34685_20260527T192015_result.json`
- **Structured JSON:** [`c1651fa4a3133f0ba278.json`](../../sessions/c1/c1651fa4a3133f0ba278.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
[服务器本地时间: 2026-05-27 03:20 — AutoDL UTC+8 → UTC约 2026-05-26 19:20]

GPU 0: detach_ln_v2_s2  — step 14636/50005 (29.3%) — 0.93 sec/step — tqdm剩余 9h06m — ETA: ~04:26 UTC May27 — DDL余量 +31.5h ✅
GPU 1: vanilla_object_s0 — step  9504/50005 (19.0%) — 0.94 sec/step — tqdm剩余10h35m — ETA: ~05:55 UTC May27 — DDL余量 +30.1h ✅
GPU 2: full_occ_ln_v2_s3 — step  9884/50005 (19.8%) — 0.92 sec/step — tqdm剩余10h16m — ETA: ~05:36 UTC May27 — DDL余量 +30.4h ✅
GPU 3: detach_ln_v2_s3  — step  9870/50005 (19.7%) — 0.93 sec/step — tqdm剩余10h17m — ETA: ~05:37 UTC May27 — DDL余量 +30.4h ✅

VRAM: 全部 ~62GB/98GB，GPU利用率 99%/52%/99%/99%
（GPU1 利用率52%因 vanilla 无 occ_head，计算量少）

OCC Labels: /root/occsafe_vla/occ_data/libero_object/ 不存在，无相关进程运行。

AUX losses (最近):
  detach_ln_v2_s2 @14600: occ=0.0091, action=0.0957
  vanilla_object_s0 @9500: occ=0.0000, action=0.1201 (无occ head)
```

**总结**: 4个实验全部正常运行，所有ETA在 May 27 上午 UTC 完成，距 DDL (May 28 12:00 UTC) 有 30+ 小时余量，非常安全。`date -u` 被 ssh_read_only 拦截，UTC 时间基于 AutoDL UTC+8 推算。

---
