# code prep spatial a1 training

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep_spatial_a1_training_20260523T051216_result.json`
- **Structured JSON:** [`91bb816531a2d523aba8.json`](../../sessions/91/91bb816531a2d523aba8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证结果：**spatial_bowl A1 SDF 训练全部就绪，零缺失项。**

| 检查项 | 状态 |
|--------|------|
| 脚本 `SCENE_CONFIG` 含 `spatial_bowl` | 已支持，无需改动 |
| SDF GT (`sdf_gt_spatial_bowl.npz`) | 两台服务器均有，4076 点，114KB |
| 训练数据 (`safelibero_spatial`) | 两台均有，50 episodes，~434MB |
| Eval assets (`baseline_spatial_bowl/norm_stats.json`) | 就绪 |

启动命令模板已写入 `artifacts/prep_spatial_a1.md`，`{LAMBDA}` 和 `{GPU}` 待填。

---
