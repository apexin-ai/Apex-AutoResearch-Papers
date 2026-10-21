# audit 34685 survival check

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_34685-survival-check_20260527T213221_result.json`
- **Structured JSON:** [`256955c090d66a402c68.json`](../../sessions/25/256955c090d66a402c68.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-34685 全部实验状态

```
GPU 0: detach_ln_v2_s2   — ✅ 存活 — step 704/50005 (1%)   — 1.09 it/s — 刚 resume，运行 ~11min
GPU 1: vanilla_object_s0  — ✅ 存活 — step 702/50005 (1%)   — 1.10 it/s — 刚 resume，运行 ~11min
GPU 2: full_occ_ln_v2_s3  — ✅ 存活 — step 17846/50005 (36%) — 1.08 it/s — 运行 4h52m
GPU 3: detach_ln_v2_s3    — ✅ 存活 — step 17808/50005 (36%) — 1.08 it/s — 运行 4h53m
```

**关键实验：**
- **full_occ_ln_v2_s3** (Cell 2): 正常，step 17800 处 occ_loss=0.0135, action_loss=0.1216
- **detach_ln_v2_s3** (Cell 4): 正常，step 17800 处 occ_loss=0.0099, action_loss=0.1147

**resume 实验：**
- detach_ln_v2_s2: step 700 处 occ_loss=0.0000 (detach 模式正常), action_loss=0.0962
- vanilla_object_s0: step 700 处 occ_loss=0.0000, action_loss=0.1475

**ETA 估算：** 4 个实验都以 ~1.08-1.10 it/s 运行。GPU 2/3 剩余 ~32200 steps ≈ 8.2h（约 05-28 14:00 UTC 完成）。GPU 0/1 剩余 ~49300 steps ≈ 12.5h（约 05-28 18:00 UTC 完成）。

**磁盘：** 110GB 可用，充足。

⚠️ GPU 0/1 的 ETA（18:00 UTC）超过 C003 截止时间 12:00 UTC 约 6 小时。GPU 2/3 也会超约 2 小时。

---
