# ops harvest westd41074

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_harvest-westd41074_20260524T081702_result.json`
- **Structured JSON:** [`5d6dc77d2f1d4a5c6aee.json`](../../sessions/5d/5d6dc77d2f1d4a5c6aee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已收集。汇总如下：

---

## westd-41074 实验状态 (2026-05-24 16:19)

**所有 4 GPU 均在运行，无空闲，无完成，无失败。**

### GPU 0 — `eval_pi05_random_k0925_object_seed42_postfix`
- **Status**: RUNNING
- **Progress**: T6/10 进行中，T5 结束后累计 84/300 = **28.0%** SR
- **各 task SR**: T0=60%, T1=36%, T2=22%, T3=28%, T4=8%, T5=44%, T6=50%@ep10
- **速度**: ~10.4 min/task
- **剩余**: ~4.8 tasks → **ETA ~17:08**

### GPU 1 — `eval_pi05_random_k0925_goal_seed42_v3`
- **Status**: RUNNING
- **Progress**: T9/10 进行中，T8 结束后累计 347/450 = **77.1%** SR
- **各 task SR**: T4=94%, T5=88%, T6=88%, T7=96%, T8=86%, T9=0%@ep20 (wine bottle on rack 极难)
- **剩余**: ~1.6 tasks → **ETA ~16:33**

### GPU 2 — `eval_pi05_random_k095_spatial_seed42_postfix_v2`
- **Status**: RUNNING
- **Progress**: T9/10 进行中，T8 结束后累计 365/450 = **81.1%** SR
- **各 task SR**: T4=50%, T5=80%, T6=92%, T7=76%, T8=94%, T9=20%@ep10
- **剩余**: ~1.8 tasks → **ETA ~16:33**

### GPU 3 — `eval_pi05_l2norm_k085_goal_seed42_postfix`
- **Status**: RUNNING（是 postfix 版本，日志写在 `/root/autodl-tmp/.../logs/eval_pi05_l2norm_k085_goal_seed42_postfix.log`）
- **Progress**: T7/10 进行中，T6 结束后累计 323/350 = **92.3%** SR
- **各 task SR**: T0=90%?, T1=92%?, T2=98%, T3=84%, T4=100%, T5=94%, T6=88%, T7=100%@ep10
- **剩余**: ~3.8 tasks → **ETA ~16:45**
- **注意**: 已有同配置旧结果 `pi05_l2norm_k0.85_libero_goal_seed42.json`（SR=88.0%, 440/500），当前是 postfix 版本重跑

---

**修正用户预期**：GPU 2 并非空闲/已完成，仍在 T9 积极运行中。GPU 1 和 GPU 2 预计最先完成（~16:33），GPU 3 次之（~16:45），GPU 0 最晚（~17:08）。

---
