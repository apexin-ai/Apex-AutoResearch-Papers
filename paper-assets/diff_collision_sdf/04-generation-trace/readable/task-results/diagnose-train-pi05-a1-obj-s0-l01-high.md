# diagnose train pi05 a1 obj s0 l01 high

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_train_pi05_a1_obj_s0_l01_high_20260527T091410_result.json`
- **Structured JSON:** [`e92befb809d4c45f31cc.json`](../../sessions/e9/e92befb809d4c45f31cc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 不存在（可能已在之前的 session 中清理）。无影响。

## 诊断结果

**状态: 训练成功完成 ✓**

| 项目 | 值 |
|------|-----|
| 最终步数 | 30000/30000 (100%) |
| 最终 loss | 0.0153 (action=0.0116, sdf=0.0369, ee=0.0035) |
| 训练时长 | ~33h 54m |
| Checkpoint | `/root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/a1_sdf_pi05_object_pudding_seed0_l1/30000` |
| Checkpoint 文件 | model.safetensors, optimizer.pt, metadata.pt, sdf_decoder.pt, ee_extractor.pt, aux_metadata.pt, norm_stats.json |
| 保留的 checkpoints | 29999, 30000, best |
| 错误 | 无 |

Registry 已更新: status=DONE, conclusion=success, checkpoint_path 和 log_path 已设置。

---
