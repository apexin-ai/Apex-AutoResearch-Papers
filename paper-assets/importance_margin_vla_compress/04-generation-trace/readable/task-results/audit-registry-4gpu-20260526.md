# audit registry 4gpu 20260526

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_registry-__-4gpu-20260526_20260526T221210_result.json`
- **Structured JSON:** [`ff7b97829af69c14bd81.json`](../../sessions/ff/ff7b97829af69c14bd81.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
westd-27271:0 — [已补录] exp_id=eval_openvla_attn_k075_goal_seed42 status=RUNNING
westd-27271:1 — [已注册] exp_id=eval_openvla_attn_k05_long_seed42 status=RUNNING
cqa1-33015:0 — [已注册] exp_id=eval_pi05_l2norm_k07_long_seed42 status=DEPLOYED (已完成，SR=60%，PID 617566 是re-run)
westd-41074:1 — [已补录] exp_id=eval_openvla_random_k075_long_seed42 status=RUNNING
```

注意：`eval_pi05_l2norm_k07_long_seed42` 已在 DEPLOYED 状态（之前完成，SR=60%）。当前 PID 617566 是同一实验的 re-run，spec 中已记录了当前 server/PID 信息。由于状态机不允许从 DEPLOYED 回退到 RUNNING，如需追踪此 re-run，需要创建一个新的 exp_id（如 `eval_pi05_l2norm_k07_long_seed42_v2`）。

---
