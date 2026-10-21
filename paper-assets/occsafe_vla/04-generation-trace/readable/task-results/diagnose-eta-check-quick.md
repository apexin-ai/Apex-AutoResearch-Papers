# diagnose eta check quick

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eta_check_quick_20260527T181019_result.json`
- **Structured JSON:** [`0f8c89eb1ed5b2d6d2d1.json`](../../sessions/0f/0f8c89eb1ed5b2d6d2d1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

10894 上 `detach_ln_v2_s0c_r3.log` 和 `full_occ_ln_s4.log` **不存在**。当前 UTC ≈ 18:11。

```
实验                  | step/50005 (XX%)    | it/s | ETA (UTC)
─────────────────────────────────────────────────────────────────
detach_ln_v2_s2  ★   | 10284/50005 (20.6%) | 1.09 | 2026-05-28 04:18 ✅
detach_ln_v2_s3      |  5511/50005 (11.0%) | 1.09 | 2026-05-28 05:31 ✅
full_occ_ln_v2_s3    |  5524/50005 (11.0%) | 1.08 | 2026-05-28 05:37 ✅
vanilla_object_s0    |  5120/50005 (10.2%) | 1.08 | 2026-05-28 05:44 ✅
vanilla_object_s1    |  1204/50005 ( 2.4%) | 1.10 | 2026-05-28 06:30 ✅
detach_ln_v2_s0c_r3  |  ❌ LOG NOT FOUND (10894)
full_occ_ln_s4       |  ❌ LOG NOT FOUND (10894)
```

DDL = 2026-05-28 12:00 UTC。5 个正在跑的实验全部预计在 DDL 前 6-8 小时完成，无风险。

10894 上 `detach_ln_v2_s0c_r3` 和 `full_occ_ln_s4` 这两个名字在 runs 目录里不存在。相近的有 `detach_ln_v2_s0c.log`（12h 前停止更新，~1.2MB）和 `full_occ_ln_v2_s0d.log`（11h 前停止更新，~1.2MB），看起来已中止。需要确认是否要重启这两个。

---
