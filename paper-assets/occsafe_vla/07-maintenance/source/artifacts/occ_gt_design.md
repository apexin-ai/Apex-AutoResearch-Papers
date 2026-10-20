# 占据 GT 生成方案

> 最后更新: 2026-05-20 | 状态: 设计完成，待实现

## 1. 推荐方案：直接 Sim State 提取（Method A）

**核心思路**：遍历 MuJoCo 场景中所有 geom，根据 geom 类型（box/sphere/cylinder/capsule/ellipsoid/mesh）+ 世界坐标位姿，对 3D 体素网格做解析 point-in-shape 测试，生成占据标签。

**选择理由**：
- 仿真环境可直接访问完整场景几何，无遮挡、无噪声——这是仿真独有的优势
- robosuite 场景以原始几何体（box, cylinder, sphere, capsule）为主，解析测试精确且向量化
- 少量 mesh geom 用 trimesh 库的 `contains()` 兜底
- 64³ 网格 + ~20 geom 约 <10ms/帧，远快于 raycasting（~720ms）和 depth-TSDF（~200ms+渲染）

### 方案对比

| 方案 | 精度 | 速度 (64³) | 实现难度 | 备注 |
|------|------|-----------|---------|------|
| **A: Sim State 提取** | 精确 | <10ms/帧 | 中 | **推荐** |
| B: Raycasting (mj_ray) | 精确 | ~720ms/帧 | 中 | mj_ray 不支持批量不同起点 |
| C: Multi-view Depth→TSDF | 近似 | ~200ms+ | 高 | 有遮挡、量化误差 |

---

## 2. 体素网格参数

### 工作空间

```
坐标系: world frame (MuJoCo 默认)
范围: 0.64m × 0.64m × 0.64m
中心: 桌面中心上方 0.32m (robosuite 桌面高度 ~0.8m → z 中心 ~1.12m)
具体: x ∈ [-0.32, 0.32], y ∈ [-0.32, 0.32], z ∈ [0.80, 1.44]
```

选择依据：robosuite 默认桌面 0.8m × 0.8m，实际操作区域集中在中心 ~0.6m 范围。0.64m 覆盖主要操作空间并留余量。Z 轴从桌面起始，覆盖机械臂末端可达高度。

### 分辨率

| 分辨率 | 体素数 | 体素尺寸 | 内存 (bool) | 内存 (uint8 semantic) |
|--------|--------|---------|------------|---------------------|
| 32³ | 32K | 2cm | 32KB | 32KB |
| **64³** | **262K** | **1cm** | **32KB** | **256KB** |
| 128³ | 2M | 0.5cm | 2MB | 2MB |

**推荐 64³**：1cm 分辨率足以区分典型操作物体（杯子 ~7cm、罐头 ~6cm），与 PerAct (100³/1cm) 量级一致，计算和存储开销可控。

### 语义类别

| 类别 ID | 含义 | 说明 |
|---------|------|------|
| 0 | free (空闲) | 无物体占据的体素 |
| 1 | table (桌面) | 桌子及固定装置 |
| 2 | robot (机器人) | 机械臂全部 link + gripper |
| 3 | target (目标物体) | 当前任务需操作的物体 |
| 4 | obstacle (障碍物) | SafeLIBERO 中的安全约束物体 |

同时输出 binary 版本（0=free, 1=occupied）。训练时可根据需要选用 binary 或 semantic。

---

## 3. 实现方案

### 3.1 MuJoCo 数据访问

```python
# robosuite 环境中访问 MuJoCo 原始对象
env = robosuite.make("SafeLift", robots="Panda", ...)
obs = env.reset()

model = env.sim.model._model   # mujoco.MjModel
data = env.sim.data._data      # mujoco.MjData

# 关键数据
# model.ngeom          — geom 总数
# model.geom_type[i]   — geom 类型 (BOX=6, SPHERE=2, CYLINDER=5, ...)
# model.geom_size[i]   — (3,) 尺寸参数（含义取决于类型）
# model.geom_bodyid[i] — 所属 body ID
# data.geom_xpos[i]    — (3,) 世界坐标位置
# data.geom_xmat[i]    — (9,) 世界坐标旋转矩阵 (展平的 3×3)
```

### 3.2 核心算法

```python
import numpy as np
import mujoco

def build_occupancy(model, data, grid_origin, grid_extent, resolution,
                    geom_class_map):
    """
    从 MuJoCo sim state 构建 3D 语义占据网格。

    Args:
        model: mujoco.MjModel
        data: mujoco.MjData (已调用 mj_forward)
        grid_origin: (3,) 网格下角世界坐标
        grid_extent: (3,) 网格范围 (米)
        resolution: int, 每轴体素数
        geom_class_map: dict[int, int], geom_id → 语义类别

    Returns:
        semantic: (R, R, R) uint8, 语义标签
        binary: (R, R, R) bool, 是否被占据
    """
    voxel_size = grid_extent / resolution
    lin = [np.linspace(grid_origin[ax] + voxel_size[ax] / 2,
                       grid_origin[ax] + grid_extent[ax] - voxel_size[ax] / 2,
                       resolution) for ax in range(3)]
    xx, yy, zz = np.meshgrid(*lin, indexing='ij')
    centers = np.stack([xx, yy, zz], axis=-1).reshape(-1, 3)  # (R³, 3)

    semantic = np.zeros(len(centers), dtype=np.uint8)  # 0 = free

    for gi in range(model.ngeom):
        cls = geom_class_map.get(gi, None)
        if cls is None:
            continue

        gtype = model.geom_type[gi]
        gsize = model.geom_size[gi]
        pos = data.geom_xpos[gi]
        rot = data.geom_xmat[gi].reshape(3, 3)

        # 变换到 geom 局部坐标
        local = (centers - pos) @ rot

        inside = _point_in_geom(gtype, gsize, local, model, gi)
        semantic[inside] = cls

    semantic = semantic.reshape(resolution, resolution, resolution)
    binary = semantic > 0
    return semantic, binary


def _point_in_geom(gtype, gsize, local, model, geom_id):
    """向量化 point-in-shape 测试"""
    if gtype == mujoco.mjtGeom.mjGEOM_BOX:
        return np.all(np.abs(local) <= gsize, axis=1)

    elif gtype == mujoco.mjtGeom.mjGEOM_SPHERE:
        return np.sum(local ** 2, axis=1) <= gsize[0] ** 2

    elif gtype == mujoco.mjtGeom.mjGEOM_CYLINDER:
        r2 = local[:, 0] ** 2 + local[:, 1] ** 2
        return (r2 <= gsize[0] ** 2) & (np.abs(local[:, 2]) <= gsize[1])

    elif gtype == mujoco.mjtGeom.mjGEOM_CAPSULE:
        r = gsize[0]
        h = gsize[1]
        r2 = local[:, 0] ** 2 + local[:, 1] ** 2
        in_cyl = (r2 <= r ** 2) & (np.abs(local[:, 2]) <= h)
        d_top = local.copy(); d_top[:, 2] -= h
        d_bot = local.copy(); d_bot[:, 2] += h
        return in_cyl | (np.sum(d_top ** 2, axis=1) <= r ** 2) | \
               (np.sum(d_bot ** 2, axis=1) <= r ** 2)

    elif gtype == mujoco.mjtGeom.mjGEOM_ELLIPSOID:
        return np.sum((local / gsize) ** 2, axis=1) <= 1.0

    elif gtype == mujoco.mjtGeom.mjGEOM_MESH:
        import trimesh
        mesh_id = model.geom_dataid[geom_id]
        va = model.mesh_vertadr[mesh_id]
        vn = model.mesh_vertnum[mesh_id]
        fa = model.mesh_faceadr[mesh_id]
        fn = model.mesh_facenum[mesh_id]
        verts = model.mesh_vert[va:va + vn]
        faces = model.mesh_face[fa:fa + fn]
        mesh = trimesh.Trimesh(vertices=verts, faces=faces)
        return mesh.contains(local)

    return np.zeros(len(local), dtype=bool)
```

### 3.3 Geom 分类映射

需要在初始化时建立 geom_id → 语义类别 的映射：

```python
def build_geom_class_map(env):
    """
    根据 robosuite 环境信息，将每个 geom 映射到语义类别。
    """
    model = env.sim.model._model
    geom_class_map = {}

    for gi in range(model.ngeom):
        name = mujoco.mj_id2name(model, mujoco.mjtObj.mjOBJ_GEOM, gi)
        if name is None:
            continue

        gtype = model.geom_type[gi]
        if gtype == mujoco.mjtGeom.mjGEOM_PLANE:
            continue  # 跳过无限平面

        # 根据 geom 名称前缀判断类别（robosuite 命名规范）
        if 'table' in name or 'arena' in name:
            geom_class_map[gi] = 1  # table
        elif 'robot' in name or 'gripper' in name or 'link' in name:
            geom_class_map[gi] = 2  # robot
        # target/obstacle 需要根据 SafeLIBERO 任务定义确定
        # 这里需要接入 SafeLIBERO 的任务元数据
        else:
            geom_class_map[gi] = 4  # 默认为 obstacle，target 单独标注

    return geom_class_map
```

**注意**：target vs obstacle 的区分需要查看 SafeLIBERO 的任务定义。每个任务应明确指定哪些物体是操作目标、哪些是障碍物。这部分需要在实现时根据 SafeLIBERO 代码确认。

### 3.4 集成到数据收集 Pipeline

```python
def collect_episode_with_occupancy(env, policy, max_steps=500):
    """在数据收集时同步生成占据标签"""
    obs = env.reset()
    model = env.sim.model._model
    data = env.sim.data._data

    grid_origin = np.array([-0.32, -0.32, 0.80])
    grid_extent = np.array([0.64, 0.64, 0.64])
    resolution = 64

    geom_map = build_geom_class_map(env)

    occ_semantic_list = []
    occ_binary_list = []

    for step in range(max_steps):
        mujoco.mj_forward(model, data)
        sem, binary = build_occupancy(
            model, data, grid_origin, grid_extent, resolution, geom_map
        )
        occ_semantic_list.append(sem)
        occ_binary_list.append(binary)

        action = policy(obs)
        obs, reward, done, info = env.step(action)
        if done:
            break

    return {
        'occupancy_semantic': np.stack(occ_semantic_list),  # (T, 64, 64, 64) uint8
        'occupancy_binary': np.stack(occ_binary_list),      # (T, 64, 64, 64) bool
    }
```

---

## 4. 更新频率与存储

### 更新频率

- **建议每帧生成**：物体和机械臂每步都在运动，占据标签需跟踪
- 可选降采样：如果训练时只用每 N 帧的占据标签，可在存储时降采样（如每 2 帧存一帧）
- 生成速度 <10ms/帧，不会成为瓶颈

### 数据量估算

| 格式 | 单帧 | 500 步 episode | 100 episodes |
|------|------|---------------|-------------|
| binary (bool, 64³) | 32KB | 16MB | 1.6GB |
| semantic (uint8, 64³) | 256KB | 128MB | 12.8GB |
| binary + gzip (~95% 稀疏) | ~2KB | 1MB | 100MB |
| semantic + gzip | ~5KB | 2.5MB | 250MB |

占据网格高度稀疏（约 5-15% 被占据），gzip 压缩效果极好。

### 存储格式

采用 HDF5，与 LIBERO/robomimic 现有数据格式一致：

```
dataset.hdf5
├── data/
│   ├── demo_0/
│   │   ├── obs/              # 现有观测数据
│   │   ├── actions/          # 现有动作数据
│   │   └── occupancy/        # 新增
│   │       ├── semantic      # uint8 (T, 64, 64, 64), chunked=(1,64,64,64), gzip
│   │       └── binary        # bool  (T, 64, 64, 64), chunked=(1,64,64,64), gzip
│   ├── demo_1/
│   ...
```

按时间轴 chunk，方便逐帧读取。gzip compression_opts=4 平衡压缩率和速度。

---

## 5. 训练时的辅助损失

### 损失函数

推荐 **Focal Loss + Lovász-Softmax** 组合：

- **Focal Loss**：处理严重类别不平衡（~90% free 体素），γ=2.0
- **Lovász-Softmax**：IoU 的可微代理，增强空间一致性
- 加权：`L_occ = α * L_focal + β * L_lovasz`，建议 α=1.0, β=0.5

```python
L_total = L_action + λ * L_occ   # λ 为辅助损失权重，建议从 0.1 开始调
```

### 辅助头设计要点

- 在 OpenVLA-OFT 的 visual encoder 输出后接轻量 3D 卷积解码器
- 输入: visual features → project to 3D volume → 3D conv layers → occupancy logits
- 具体架构设计属于模型实现阶段，此处不展开

### 参考：OccVLA 的做法

- OccVLA (arXiv:2509.05578) 在自动驾驶 VLA 中证明占据辅助监督有效
- 关键发现：**推理时可跳过占据预测，不影响性能**——占据仅作为训练信号
- 这意味着辅助头不增加推理开销

---

## 6. 实现步骤与工作量

### Step 1: 环境探索（0.5 天）
- 在 SafeLIBERO 中加载几个任务，打印所有 geom 信息（名称、类型、尺寸、body）
- 确认 geom 命名规范，建立 geom → 语义类别映射规则
- 确认工作空间范围是否覆盖所有任务场景

### Step 2: 占据生成器实现（1 天）
- 实现 `build_occupancy()` 函数，支持所有 primitive geom 类型
- 实现 mesh geom 的 trimesh fallback
- 单元测试：手动构造简单场景验证正确性

### Step 3: 可视化验证（0.5 天）
- 用 matplotlib 3D scatter 或 Open3D 可视化占据网格
- 与渲染图像对照，确认空间对应关系正确
- 检查各语义类别标注是否合理

### Step 4: 数据集生成（1 天）
- 集成到 SafeLIBERO 数据收集 pipeline
- 为已有的 demo 数据补充占据标签（或重新收集）
- 写入 HDF5，验证读写正确性

### Step 5: DataLoader 集成（0.5 天）
- 修改 OpenVLA-OFT 的 DataLoader，加载占据标签
- 确保 occupancy 与 obs/action 时间对齐

**总计：~3.5 人天**

---

## 7. 潜在风险与缓解

| 风险 | 影响 | 缓解方案 |
|------|------|---------|
| SafeLIBERO geom 命名不规范，难以区分 target/obstacle | 语义标签不准确 | 查看 SafeLIBERO 任务定义代码，可能需要按任务硬编码映射 |
| 部分物体使用 mesh geom 而非 primitive | 生成速度变慢 | trimesh.contains() 兜底；如果 mesh 数量多考虑预计算 SDF |
| 工作空间范围不适用所有任务 | 部分物体超出网格 | 初始化时检查所有 geom 位置，动态调整网格范围 |
| 占据标签与 visual observation 不完全对齐（相机视角遮挡） | 辅助信号与视觉输入矛盾 | 这是 feature 不是 bug——占据提供超越视觉的完整空间信息 |
| 64³ 分辨率不足以区分精细结构 | 小物体丢失细节 | 先用 64³ 验证 MVP，效果好再考虑提升到 96³ |
| robosuite 版本差异（mujoco-py vs mujoco） | API 不兼容 | 确认 SafeLIBERO 使用的 robosuite 版本，锁定 API 调用方式 |

---

## 8. 相关工作速查

| 论文 | arXiv | 关键点 |
|------|-------|--------|
| OccVLA | 2509.05578 | 占据辅助监督 VLA（自动驾驶），推理时可跳过占据头 |
| SPA | 2410.08208 | 3D 空间感知预训练（ICLR 2025），SDF 表示 |
| VolumeDP | 2603.17720 | 体积表示用于操纵策略，88.8% LIBERO 成功率 |
| PerAct | 2209.05451 | 100³ 体素操纵策略，1cm 体素 |
| Elasto-Plastic Occ | 2505.16249 | **从仿真生成占据 GT 用于操纵**，100×100×40 体素 |
| Occ3D | 2304.14365 | 占据 GT 生成 pipeline（自动驾驶基准） |
| SurroundOcc | 2303.09551 | 稠密占据 GT 生成，Focal + Lovász 损失 |

**关键差异化**：目前无人在操纵领域用仿真 GT 占据作为 VLA 辅助监督。OccVLA 做了自动驾驶版本，我们做操纵版本，且有仿真提供的完美标签优势。
