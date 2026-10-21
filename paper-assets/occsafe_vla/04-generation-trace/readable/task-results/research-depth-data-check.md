# research depth data check

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_depth-data-check_20260522T022003_result.json`
- **Structured JSON:** [`df7b1560a40852e3c5eb.json`](../../sessions/df/df7b1560a40852e3c5eb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有信息已收集完毕。

---

## 汇总报告

### 1. 现有数据中是否已有 depth 信息

**否。**

RLDS 数据集 (`libero_spatial_no_noops`) 的 observation 只有：
- `image`: 256×256×3 uint8 (agent view RGB)
- `wrist_image`: 256×256×3 uint8 (wrist camera RGB)
- `state`: float32 [8] (EEF state)
- `joint_state`: float32 [7]

`regenerate_libero_dataset.py` 也只保存了 `agentview_rgb` 和 `eye_in_hand_rgb`，无 depth。

OCC 数据同样无 depth，只有 `bev_binary` (T,64,64) bool 和 `bev_semantic` (T,64,64) uint8。

### 2. LIBERO/robosuite/MuJoCo 是否支持 depth rendering

**是。** 两种方式：

**robosuite 方式**（最简单）：
```python
env_args = {
    "bddl_file_name": bddl_file,
    "camera_heights": 256, "camera_widths": 256,
    "camera_depths": True,   # 加这一个参数即可
}
env = OffScreenRenderEnv(**env_args)
obs = env.reset()
# obs 中会有 "agentview_depth", "robot0_eye_in_hand_depth"
```

**MuJoCo 原生方式**：
```python
renderer = mujoco.Renderer(model, height, width)
renderer.enable_depth_rendering()
renderer.update_scene(data, camera="agentview")
depth = renderer.render()  # float32 depth map
```

### 3. 离线生成 depth GT 方案

**方案 A: 修改 regenerate_libero_dataset.py（推荐，~1-2h 代码改动）**
- `env_args` 加 `"camera_depths": True`
- replay 循环中收集 `obs["agentview_depth"]`
- 保存到 HDF5
- 需要重新 replay 全部 demo（耗时取决于数据量）

**方案 B: 仿照 extract_occupancy.py 写 depth 提取脚本（~2-3h）**
- 复用已有的 state replay 框架：`sim.set_state_from_flattened(states[t])` → `sim.forward()` → MuJoCo renderer 取 depth
- 不需要完整 replay action，直接从 states 恢复即可
- 更灵活（可指定任意相机内参/外参）

### 4. OCC 数据生成流程

`occ_pipeline/extract_occupancy.py` 核心流程：
1. `OffScreenRenderEnv` 创建环境
2. 从原始 HDF5 读 `states` 序列
3. 逐帧 `sim.set_state_from_flattened(states[t])` + `sim.forward()`
4. `build_occupancy_3d()` — **不用 rendering**，而是直接判断 3D grid 点是否在 MuJoCo geom 内（box/sphere/cylinder/mesh AABB）
5. `voxel_to_bev()` — Z 轴 max-projection 得到 64×64 BEV
6. 保存 `bev_binary` + `bev_semantic`（语义：0=free, 1=table, 2=robot, 3=target）

**可复用部分**：环境创建和 state replay 框架完全通用，depth 生成只需替换 step 4 为 MuJoCo depth rendering 即可。

---
