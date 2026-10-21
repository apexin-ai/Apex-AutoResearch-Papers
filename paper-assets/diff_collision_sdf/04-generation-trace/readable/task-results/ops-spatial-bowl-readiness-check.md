# ops spatial bowl readiness check

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_spatial_bowl_readiness_check_20260525T045522_result.json`
- **Structured JSON:** [`a7fc82e41fdce63c1642.json`](../../sessions/a7/a7fc82e41fdce63c1642.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
Part 1 - spatial_bowl:
1. 训练代码: ready — 支持 --scene spatial_bowl（line 53-57 有 SCENE_CONFIG，line 74 有 choices 校验）
2. 数据: 存在 — /root/autodl-tmp/colliforce_data/safelibero_spatial/（含 data/images/meta）
3. SDF ground truth: 存在 — /root/colliforce-vla/data/sdf_gt_spatial_bowl.npz
4. 磁盘: 211G 可用（350G 盘用了 140G），足够

Part 2 - s0 checkpoint:
- s0_l005: /root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/a1_sdf_pi05_object_pudding_seed0_l005/
  - 子目录: 30000/ （仅此一个，无 best/）
  - 大小: 7.2G（完整 checkpoint）
- s0_l01:  /root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/a1_sdf_pi05_object_pudding_seed0_l01/
  - 子目录: 30000/ （仅此一个，无 best/）
  - 大小: 7.2G（完整 checkpoint）
```

spatial_bowl 训练所有前置条件就绪。两个 s0 checkpoint 均只有 `30000/` 步，无 `best/` 目录，各 7.2G，是完整 checkpoint。

---
