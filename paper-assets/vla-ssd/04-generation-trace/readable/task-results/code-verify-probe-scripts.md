# code verify probe scripts

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_verify-probe-scripts_20260515T110030_result.json`
- **Structured JSON:** [`f21bad763b53f6afd896.json`](../../sessions/f2/f21bad763b53f6afd896.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All checks complete. Here's the summary:

```
兼容性：✅ 全部通过，无需修复

  数据加载：
    ✅ HDF5 格式正确处理 (glob *.h5)
    ✅ OpenVLA: demo_X → last_preaction (T,33,4096) fp16 / image_mean (T,33,4096) fp16
    ✅ DINO-V2: traj_X → cls_token (T,1024) / patch_mean (T,1024)
    ✅ AGG_MAP fallback 机制: last_preaction→cls_token, image_mean→patch_mean

  Feature key / Shape：
    ✅ is_3d 标志正确区分 3D(T,33,4096) vs 2D(T,1024)
    ✅ 层索引: ds[:,layer,:] (3D) / ds[:] (2D)

  Pair sampling：
    ✅ Distance-stratified (n_bins=10, pairs_per_bin=50)
    ✅ Cross-trajectory (Control B) 单独实现

  Split：
    ✅ 按 task 分组，每 task 内 80/20 trajectory 划分（非 frame-level）

已修复：无（脚本与实际格式完全兼容）

Smoke test（DINO-V2 temporal_distance）：
  ✅ 500 trajs, 1 layer, dim=1024
  ✅ 400 train / 100 val
  ✅ rho = 0.8331 (7.5s)

已提取 trained 特征：4/10 tasks (24GB)
  KITCHEN_SCENE3 (5.1G), KITCHEN_SCENE4 (4.8G),
  KITCHEN_SCENE6 (5.9G), KITCHEN_SCENE8 (6.6G)

Sub-task predicate：❌ LIBERO HDF5 中无标注
  Demo 数据只有: actions, dones, obs, rewards, robot_states, states
  Demo attrs 只有: init_state, model_file, num_samples
  → 需要 LIBERO simulator 回放提取 predicate ground truth

建议下一步：
  1. 等 trained 特征提取完成（剩余 6/10 tasks）
  2. Sub-task predicate 需写 LIBERO env 回放脚本，在 simulator 中逐帧 evaluate predicates 并导出标注 JSON
```

---
