# ops check phase2 lambda0 s2 exit

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_phase2_lambda0_s2_exit_20260526T111441_result.json`
- **Structured JSON:** [`98673f9023dd4bb7fff3.json`](../../sessions/98/98673f9023dd4bb7fff3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**诊断结果：训练成功完成。**

| 项目 | 值 |
|------|-----|
| 状态 | 正常完成 10000/10000 步 |
| Final action loss | 0.0113 |
| Best loss | 0.00651 @ step 4000 |
| 耗时 | ~12h 53min (4.64 s/step) |
| Checkpoint | `/root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/a1_sdf_pi05_object_pudding_seed2_l0/10000` |
| 可用 ckpts | 9999, 10000, best |

注意：实际 output_dir 为 `...seed2_l0/` 而非 spec 中指定的 `...seed2_phase2_lambda0/`（训练脚本自动按 lambda 值命名）。Cron 不存在，无需删除。Registry 已更新为 DONE/success。

---
