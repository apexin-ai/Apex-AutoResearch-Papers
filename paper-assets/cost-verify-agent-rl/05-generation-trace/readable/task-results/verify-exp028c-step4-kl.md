# verify exp028c step4 kl

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_exp028c_step4_kl_20260516T025830_result.json`
- **Structured JSON:** [`9fe56c3975e09b7ae823.json`](../../sessions/9f/9fe56c3975e09b7ae823.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完成。结论：

**step 4 的 kl_loss=0.031 没有误录。** W&B 原始数据确认 actor/kl_loss=0.031226，actor/ppo_kl=0.015264，两者是不同的值。

所有 step 的 registry 值与 W&B 一致：
- step 2: kl_loss=0.1706 ✅, pg_loss=0.007 ✅
- step 3: kl_loss=0.1118 ✅
- step 4: kl_loss=0.031 ✅, ppo_kl=0.015 ✅

kl_loss 的完整轨迹是 0.013 → 0.171 → 0.112 → 0.031 → 0.824，非单调波动，step 4 的低值是真实训练动态，不需要修正。

报告已写入 `artifacts/exp028c_selfguide_recipe/intermediate/step4_kl_verification.md`。

---
