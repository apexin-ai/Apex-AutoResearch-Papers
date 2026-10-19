# ops diagnose s0 l005 exit

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_diagnose_s0_l005_exit_20260524T102119_result.json`
- **Structured JSON:** [`f531c36b2c27adb2af56.json`](../../sessions/f5/f531c36b2c27adb2af56.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**train_pi05_a1_obj_s0_l005：训练成功完成**
- 30000/30000 步全部完成
- best_loss = 0.00786（step 26000）
- Checkpoint 完整：best/、29999/、30000/（每个含 model.safetensors ~7GB + optimizer + sdf_decoder）
- wandb_id: umjcftxp
- Registry 已更新为 DONE/success，cron 已删除

**s0_l01 状态（额外检查）：也已完成**
- 30000/30000 步完成（首次检查时 `tmp_30000` 正在写入，几秒后重命名为 `30000`，说明刚刚完成）
- best_loss = 0.00801（step 26000）
- Checkpoint 完整：best/、28000/、29999/、30000/
- 两个进程均已退出，无残留进程

---
