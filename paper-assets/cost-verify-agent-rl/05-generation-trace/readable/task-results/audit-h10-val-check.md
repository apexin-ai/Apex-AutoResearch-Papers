# audit h10 val check

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_h10_val_check_20260523T193623_result.json`
- **Structured JSON:** [`0b7ecb69d607ca6da57e.json`](../../sessions/0b/0b7ecb69d607ca6da57e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结论：

**step 5 的 val success rate = 6.25% (2/32)**，与 Figure 3(b) 一致。

数据来源：W&B run `x09p5xd0` (hsweep-h10-seed1), metric `val-env/AlfworldSG/success`, `_step=5`, value = 0.0625。

两次 val eval（step 0 和 step 5）都是 0.0625。run 状态为 crashed（只跑到 step 7，共 15 步），但 step 5 的 val 已完整记录。

registry 中 `step5_val_success: SFT_baseline` (12.5%) 的描述不准确——实际值是 SFT baseline 的一半（6.25% vs 12.5%）。

---
