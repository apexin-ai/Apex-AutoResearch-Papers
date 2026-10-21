# train resume ablation detach s0 retrain

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_resume_ablation_detach_s0_retrain_20260524T175934_result.json`
- **Structured JSON:** [`56adf40a470e8a2f31f9.json`](../../sessions/56/56adf40a470e8a2f31f9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

- **30000 步损坏 checkpoint** 已删除
- **从 20000 步恢复训练**，PID=775880，~1.10 it/s 稳定运行
- 配置：`--occ_detach true`（BN 默认），seed=42，cuda:0，max_steps=50005
- wandb 未配置，已用 `WANDB_MODE=disabled` 跳过
- 日志：`/root/autodl-tmp/logs/ablation_occ_detach_s0_retrain_resume.log`
- Registry 已更新为 RUNNING

注意：max_steps=50005 是从 resume 点开始的额外步数，log_step 从 20000 起算，实际训练到 step 70005。如果目标总量是 50005 步，需要改为 max_steps=30005。

---
