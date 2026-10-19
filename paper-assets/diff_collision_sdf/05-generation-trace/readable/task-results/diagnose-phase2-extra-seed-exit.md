# diagnose phase2 extra seed exit

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_phase2_extra_seed_exit_20260527T223620_result.json`
- **Structured JSON:** [`684d38fd06d7d597a99d.json`](../../sessions/68/684d38fd06d7d597a99d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

**Stage 1: SUCCESS**
- 10K checkpoint 完整：`/root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/phase2_stage1_seed0_l005/10000/model.safetensors` (7.5GB)
- best_loss = 0.0307 @ step 10000
- wandb summary: action_loss=0.0364, loss=0.0368, sdf_l1=0.0338
- 日志：`~/runs/diff_collision_sdf/train_phase2_lambda0_extra_seed.log`

**Stage 2: 已自动启动，运行中**
- Sentinel 于 22:35:26 UTC 验证 10K checkpoint 后自动启动 Stage 2
- PID 892014，cuda:1，100% GPU 利用率
- 进度：16325/30000 (54%)，预计剩余 ~17.5h
- 日志：`~/runs/diff_collision_sdf/train_phase2_lambda0_s2_v3.log`

Registry 已更新为 DONE/success。

---
