# ssh deep cleanup restart baselines

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_deep_cleanup_restart_baselines_20260520T143541_result.json`
- **Structured JSON:** [`432be1d7c5dbfdfd6060.json`](../../sessions/43/432be1d7c5dbfdfd6060.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 完成总结

### 1. Checkpoint 清理
- **baseline_spatial_bowl_seed0**: 删除 6000/8000/10000，保留 12000/14000
- **baseline_object_pudding_seed0**: 删除 6000/8000/10000/12000，保留 14000/16000
- tmp_* 残留已清理

### 2. Kill 结果
- PID 100319 (spatial_bowl) → KILLED
- PID 95429 (object_pudding) → KILLED

### 3. Restart
| 实验 | 新 PID | GPU | Resume from |
|------|--------|-----|-------------|
| baseline_spatial_bowl_s0_v2 | 222903 | cuda:0 | step 14000 |
| baseline_object_pudding_s0_v2 | 222982 | cuda:2 | step 16000 |

### 4. 磁盘
`/root/autodl-tmp`: 121G/350G (35%) — 目标达成

### 5. 实验状态
| GPU | 实验 | 状态 | 显存 |
|-----|------|------|------|
| 0 | baseline_spatial_bowl_s0_v2 | training from 14000 | 19.5GB |
| 1 | 空闲 | — | 0 |
| 2 | baseline_object_pudding_s0_v2 | training from 16000 | 19.5GB |
| 3 | a1_sdf_spatial_bowl_s0_v3 | running | 13.4GB |

SAVE_TOTAL_LIMIT=2 已生效，后续新 checkpoint 保存时会自动清理旧的。

---
