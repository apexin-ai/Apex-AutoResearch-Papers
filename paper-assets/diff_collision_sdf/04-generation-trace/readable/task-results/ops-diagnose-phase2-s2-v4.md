# ops diagnose phase2 s2 v4

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_diagnose-phase2-s2-v4_20260528T033147_result.json`
- **Structured JSON:** [`623ddba46c2ad5e7b57b.json`](../../sessions/62/623ddba46c2ad5e7b57b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. No cron jobs exist in this session to delete. Here's the diagnosis report:

---

## `train_phase2_lambda0_s2_v4` 诊断结果

**结论：训练失败 — 磁盘满**

| 项目 | 详情 |
|------|------|
| **失败原因** | `/root/autodl-tmp` 100% 满 (350G/350G, 仅剩 2.6MB)。在 step 20000 保存 checkpoint 时触发 `No space left on device (os error 28)` |
| **最后成功 step** | 19999 (目标 30000，完成 67%) |
| **最后完整 checkpoint** | step 18000 — `/root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/a1_sdf_pi05_object_pudding_seed2_l0/18000` |
| **损坏的 checkpoint** | `tmp_20000/` 仅有 `model.safetensors` (4.5GB)，缺少 config/optimizer，不可用 |
| **训练时长** | ~13h (May 27 22:25 → May 28 11:22) |
| **日志文件** | `/root/runs/diff_collision_sdf/train_phase2_lambda0_s2_v3.log` |
| **GPU** | cuda:2 已释放 (进程已退出) |

**要恢复训练**需要先清理磁盘空间，然后从 step 18000 checkpoint resume 到 30K（剩余 12K steps，约 ~15.5h）。`tmp_20000/` 目录可以安全删除以回收 ~4.5GB。

---
