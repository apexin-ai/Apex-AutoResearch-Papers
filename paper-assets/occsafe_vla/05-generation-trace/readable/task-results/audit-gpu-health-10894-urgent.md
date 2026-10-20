# audit gpu health 10894 urgent

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_gpu-health-10894-urgent_20260527T211232_result.json`
- **Structured JSON:** [`956963c3c374332c4a58.json`](../../sessions/95/956963c3c374332c4a58.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
[UTC ~05:12, 2026-05-28]

GPU 0 (vanilla_object_s1): ✅ 存活 — step 12886/50005 (25.8%) — ~1.08 it/s
  ETA: 剩余 37119 steps ÷ 1.08 it/s ≈ 9.5h → 完成约 ~14:45 UTC
  ⚠️ 超 DDL (12:00 UTC) 约 2h 45min

GPU 1: ✅ 空闲 — 0% util, 0 MiB — 符合预期（待命 Batch A eval）

GPU 2 (detach_ln_v2_s0c_r3): ✅ 存活 — step 44020/50005 (88%) — ~1.08 it/s
  ETA: 剩余 5985 steps ≈ 1h 32min → 完成约 ~06:44 UTC ✅

GPU 3 (full_occ_ln_s4): ✅ 存活 — step 42233/50005 (84.5%) — ~1.07 it/s
  ETA: 剩余 7772 steps ≈ 2h 01min → 完成约 ~07:13 UTC ✅

Batch A 就绪状态:
  detach_ln_v2_s0c_r3: ckpt 30k ✓, 40k ✓ (50k 预计 ~06:44 UTC)
  full_occ_ln_s4:      ckpt 30k ✓, 40k ✓ (50k 预计 ~07:13 UTC)
  → Batch A eval 最早可在 ~07:15 UTC 启动（GPU 1 已空闲待命）

vanilla_object_s1:    ckpt 5k ✓, 10k ✓ (下一个 15k 预计 ~06:10 UTC)
```

**关键风险: vanilla_object_s1 预计 ~14:45 UTC 完成，超 DDL 约 2h 45min。** 这是目前唯一的问题——GPU 2/3 的实验都会在 DDL 前顺利完成。

---
