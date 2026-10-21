# audit 10894 survival check

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_10894-survival-check_20260527T213226_result.json`
- **Structured JSON:** [`17e8ec02f596604ccaa1.json`](../../sessions/17/17e8ec02f596604ccaa1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息收集完毕。汇总：

```
GPU 0: vanilla_object_s1    — ✅ 存活 — step 14178/50005 (28%) — 1.07 it/s — ETA ~14:50 UTC May 28
GPU 1: 空闲                  — 0 MiB, 0% util
GPU 2: detach_ln_v2_s0c_r3  — ✅ 存活 — step 45358/50005 (91%) — 1.08 it/s — ETA ~06:45 UTC May 28
GPU 3: full_occ_ln_s4       — ✅ 存活 — step ~43.5k/50005 (≈87%) — ~1.08 it/s — ETA ~07:15-07:30 UTC May 28
```

关键发现：

- **detach_ln_v2_s0c_r3** 没有之前预计那么快完成（当前91%），原来的"22:42 UTC完成"估计有误。日志写到 `/root/autodl-tmp/checkpoints/detach_ln_v2_s0c_r3.log`（不在标准 runs 目录）。剩余 ~4647 步 ≈ **1h12min**
- **full_occ_ln_s4** stdout 走 pipe（tmux），无独立日志文件。根据启动时间推算（比 detach 晚 ~31min），当前约 step 43.5k。剩余 **~1h42min**
- **vanilla_object_s1** 只到 28%，剩余 ~35800 步 ≈ **9.3h**

**⚠️ DDL 风险**：C003 要求 2026-05-28 12:00 UTC 前完成。
- detach_ln_v2_s0c_r3: ~06:45 UTC ✅
- full_occ_ln_s4: ~07:30 UTC ✅
- **vanilla_object_s1: ~14:50 UTC ❌ 超 DDL 近 3 小时**

cuda:1 空闲，但 vanilla_object_s1 是单 GPU 实验，无法利用。

---
