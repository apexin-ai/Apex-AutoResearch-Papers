# SDF GT 提取方案调研报告

> 调研日期：2026-05-19 | 项目：ColliForce-VLA

## 1. SDF 提取库功能对比

| 库 | 输入格式 | 算法 | 批量查询 2048 pts | 速度 | 精度 | 可微分 | GPU |
|---|---|---|---|---|---|---|---|
| **trimesh** | STL/OBJ/PLY/GLTF/3MF/OFF 等 | BVH 最近点 + ray casting 判符号 | 支持但慢 | 慢（纯 CPU） | 高（需 watertight） | 否 | 否 |
| **pysdf** (sxyu/sdf) | vertices+faces NumPy 数组 | BVH + ray casting（C++ 并行） | 快，100K pts < 1s | **快** | 高（需 watertight） | 否 | 否 |
| **mesh-to-sdf** (marian42) | trimesh 对象 | 100 虚拟深度渲染 + KNN | 可用但慢（~秒级） | 慢 | 中（~60% ShapeNet 成功率） | 否 | 仅 OpenGL 渲染 |
| **Kaolin** (NVIDIA) | OBJ/USD/OFF/GLTF | `check_sign` (ray hash) + `point_to_mesh_distance` (最近三角形) | 原生批量+batch | **快（CUDA）** | 高 | **部分**（距离可微，符号不可微） | **是** |
| **point-cloud-utils** | vertices+faces | signed_distance_to_mesh | 支持 | 中 | 高 | 否 | 否 |
| **libigl** | vertices+faces | winding number 判符号 | 支持 | 中 | **最高**（鲁棒 winding number） | 否 | 否 |
| **PyTorch3D** | vertices+faces tensor | point_mesh_face_distance | 原生批量 | 快（CUDA） | 高（仅无符号距离） | **是** | **是** |
| **TorchSDF** (wrc042) | vertices+faces tensor | GPU SDF | 原生批量 | 快（CUDA） | 高 | **是** | **是** |

### 各库详细评估

**trimesh** — 最通用的 mesh 处理库。API: `trimesh.proximity.signed_distance(mesh, points)`。算法为 BVH 最近点投影 + ray casting fallback 判内外。纯 CPU/NumPy，2048 点可用但不快。适合原型验证，不适合大规模离线预计算。

**pysdf (sxyu/sdf)** — C++ 核心 + Cython 绑定，多线程并行。API: `SDF(vertices, faces)` 返回 callable，支持 `sdf(points)`、`contains()`、`sample_surface()` 等。100K 点查询 < 1s。**MVP 首选：快、API 简洁、可靠。** 缺点：需 watertight mesh，无 GPU。

**mesh-to-sdf (marian42)** — 通过虚拟渲染重建表面点云再 KNN 查询。优点是能处理非 watertight mesh。缺点：依赖 OpenGL/pyrender（headless 服务器需 EGL）、ShapeNet 只有 ~60% 成功率、自 2021 年基本停止维护、有 pyglet 版本冲突。**不推荐用于 MVP。**

**Kaolin** — NVIDIA 官方库，CUDA 原生。`check_sign` 用空间 hash 加速 ray casting，`point_to_mesh_distance` 返回无符号距离²且可微分。组合即得 SDF。批量+batch 维度原生支持。**如果需要 GPU 加速或可微分距离，Kaolin 是最佳选择。** 缺点：安装重（依赖特定 CUDA/PyTorch 版本组合），sign 不可微。

**TorchSDF (wrc042)** — 社区 GPU SDF 库，专为可微分 SDF 查询设计。文档较少但值得关注。

## 2. MuJoCo Native SDF 支持

### MuJoCo 3.0+ SDF Plugin

MuJoCo 3.0 引入了 SDF 碰撞插件系统，支持将 mesh 在编译时体素化为多分辨率 SDF。插件接口提供：
- `Distance(point[3])` → signed distance
- `Gradient(grad[3], point[3])` → SDF 梯度（解析导数）

### 相关 API

| API | 功能 | 限制 |
|---|---|---|
| `mj_geomDistance(m, d, geom1, geom2, distmax, fromto)` | 两个 geom 间的有符号距离 | **geom-to-geom only**，不支持 point-to-geom |
| `mj_ray(m, d, pnt, vec, ...)` | 从任意点发射射线，返回最近表面距离 | 单射线查询，非 SDF |
| SDF plugin `Distance()` | 任意点到 mesh 的 SDF | **仅 C plugin 接口，无 Python API** |

### 评估

- **优点**：SDF plugin 的 `Distance()` 理论上完美匹配需求，且提供解析梯度。
- **缺点**：
  1. SDF plugin 仅通过 C 接口暴露，Python 端无直接调用 `Distance(point)` 的 API
  2. `mj_geomDistance` 是 geom-to-geom，要查询任意点需创建临时 sphere geom（workaround 不优雅）
  3. SDF-vs-SDF 碰撞有已知 bug（GitHub #1425，物体穿透）
  4. 需要深入 MuJoCo 内部接口，增加工程复杂度

### Native vs 外部库对比

| 维度 | MuJoCo Native SDF | pysdf / Kaolin |
|---|---|---|
| 精度 | 高（多分辨率体素） | 高（精确几何） |
| Python 可用性 | 差（需 C wrapper） | **好** |
| 批量查询 | 需逐点调用 | **原生批量** |
| 可微分 | 有梯度但非 PyTorch | Kaolin 部分可微 |
| 工程复杂度 | 高 | **低** |

**结论：MVP 阶段不建议用 MuJoCo native SDF。** 外部库（pysdf/Kaolin）更实用。未来如果需要与 MuJoCo 仿真深度集成，可以考虑写 C 扩展调用 SDF plugin。

## 3. 推荐 MVP SDF 提取方案

### 方案：pysdf 离线预计算 + Kaolin 备选

```
Pipeline:
1. trimesh 加载 MuJoCo visual meshes (OBJ/STL)
2. 检查 watertight，必要时 trimesh.repair
3. pysdf 批量计算 SDF query points 的 GT 值
4. 保存为 .npz (query_points, sdf_values, object_ids)
```

**选择 pysdf 的理由：**
- C++ 并行，100K 点 < 1s，足以处理 LIBERO 全部场景的离线预计算
- API 极简：`f = SDF(verts, faces); sdf_vals = f(points)`
- 无 GPU 依赖，服务器/本地均可运行
- 对 watertight mesh（MuJoCo visual mesh 通常是）精度可靠

**Kaolin 作为备选/升级路径：**
- 如果 pysdf 速度不够（大量场景 × 大量 timestep），切换 Kaolin GPU 加速
- 训练阶段如果需要 on-the-fly SDF 计算（data augmentation），Kaolin 的 CUDA batch 更合适
- `point_to_mesh_distance` 可微分，未来可用于端到端训练

### 多物体场景 SDF 合并

对于 workspace 中 5-10 个物体：
```python
# per-object SDF 取 min
sdf_values = []
for obj_mesh in scene_meshes:
    f = SDF(obj_mesh.vertices, obj_mesh.faces)
    sdf_values.append(f(query_points))
workspace_sdf = np.min(np.stack(sdf_values), axis=0)  # 取最近物体的距离
```

与 "Differentiable Composite Neural SDFs" (2025) 的思路一致：per-object SDF 通过 min 操作组合为场景 SDF。

## 4. SDF 采样策略建议

### 文献标准做法

| 方法 | 近表面比例 | 均匀采样比例 | 总点数 | 近表面 sigma |
|---|---|---|---|---|
| DeepSDF (2019) | 95% | 5% | 500K+ (训练集) | 双尺度: 0.05, 0.016 (单位球) |
| Occupancy Networks | 50% | 50% | 100K | 0.05 (单位球) |
| 推荐 (本项目) | **80%** | **20%** | **4096-8192/scene** | 双尺度: 2.5cm, 8mm |

### 具体采样方案

**采样空间**：LIBERO 桌面 workspace ~0.5×0.5×0.3m，四周 pad 5cm → **0.6×0.6×0.4m bounding box**。

**采样数量**：
- 2048 点对 5-10 个物体**偏少**。DeepSDF 单物体用 16K-32K/batch。
- **MVP 建议 4096 点/scene**（3276 近表面 + 820 均匀），如效果不够升到 8192。
- 训练时每 batch 随机采样不同点集（不固定），增加覆盖率。

**近表面采样实现**：
```python
# 1. 在每个物体表面均匀采样点（按面积加权）
surface_points = mesh.sample(n_surface)  # trimesh
# 2. 双尺度高斯扰动
sigma1, sigma2 = 0.025, 0.008  # meters
near_points_1 = surface_points + np.random.randn(*surface_points.shape) * sigma1
near_points_2 = surface_points + np.random.randn(*surface_points.shape) * sigma2
# 3. 均匀采样
uniform_points = np.random.uniform(bbox_min, bbox_max, (n_uniform, 3))
# 4. 合并
query_points = np.concatenate([near_points_1, near_points_2, uniform_points])
```

**每个物体的采样预算**：按物体表面积比例分配近表面采样点，确保小物体也有足够覆盖。

### SDF 值截断

遵循 DeepSDF 做法，截断 SDF 值到 [-delta, delta]：
- delta = 0.05m (5cm) 对桌面场景合适
- 远离表面的 SDF 值对碰撞避免不重要
- 截断使网络聚焦学习表面附近的精细 SDF 结构

## 5. 可微分 SDF 表示方案综述

### DeepSDF (Park et al., 2019)

- **架构**：8 层 MLP，512 hidden，第 4 层 skip connection（重新注入输入）
- **输入**：latent code z (256d) + query point xyz (3d) → scalar SDF
- **Auto-decoder**：无 encoder，每个 shape 一个可学习 latent code z_i，与网络权重联合优化
- **训练 loss**：L1 on clamped SDF，`|clamp(pred, -δ, δ) - clamp(GT, -δ, δ)|`
- **推理**：固定 decoder，梯度下降优化 z 拟合新 shape

### 适配 ColliForce-VLA 的方案

**关键区别**：不需要 auto-decoder 的 per-shape latent code。VLA backbone 的 intermediate features 直接替代 latent code。

```
VLA Backbone → intermediate features (e.g., 256d)
                         ↓
              SDF Decoder MLP
                         ↓
Input: [VLA_feature, xyz_query] → Output: scalar SDF value
```

**推荐 MLP 架构（MVP）**：
- 4-6 层 MLP，256 hidden units，ReLU
- 输入：`[vla_feature (256d), query_xyz (3d)]` = 259d
- 输出：scalar SDF（截断到 [-0.05, 0.05]）
- Skip connection at layer 2（重新注入 xyz）
- Loss: L1 on clamped SDF values

**SDF 梯度用于 action refinement**：
- 前向：SDF decoder 预测 query points 的 SDF 值
- 碰撞 cost：`collision_cost = ReLU(-SDF(x) + margin)`，margin ~1-2cm
- 反向：梯度 ∇_action collision_cost 通过 SDF decoder 回传到 action tokens
- 效果：将预测 action 推离碰撞区域（SDF < 0 的位置）

### 相关工作

| 论文 | 方法 | 与本项目关联 |
|---|---|---|
| DeepSDF (2019) | Auto-decoder, per-shape latent | 架构参考 |
| Differentiable Composite Neural SDFs (2025) | Per-object neural SDF + min 组合 | 多物体场景 SDF 组合策略 |
| Prof. Robot (CVPR 2025) | Eikonal-regularized neural SDF | SDF 梯度一致性正则化 |
| Parallel MPPI + SDF Cost (2024) | SDF 梯度调制 MPPI | SDF 梯度用于实时避障 |
| Neural NMPC through SDF (2025) | SDF encoding for MPC | SDF 作为碰撞约束 |

### Eikonal 正则化

建议在训练 SDF decoder 时加入 Eikonal loss：
```
L_eikonal = (||∇_x SDF(x)|| - 1)^2
```
确保 SDF 梯度范数接近 1（真实 SDF 的性质），提供更一致的碰撞梯度信号。

## 6. Blockers 与风险

| 风险 | 严重度 | 缓解措施 |
|---|---|---|
| MuJoCo visual mesh 非 watertight | 中 | trimesh.repair 或 mesh-to-sdf fallback |
| pysdf 不支持 GPU，大规模预计算可能慢 | 低 | Kaolin GPU 加速备选；离线预计算只需跑一次 |
| 2048 点不够表征多物体 SDF | 中 | 提升到 4096-8192，训练时随机采样不同点集 |
| SDF decoder 梯度不稳定影响 action refinement | 中 | Eikonal 正则化 + gradient clipping |
| Kaolin 安装依赖复杂 | 低 | MVP 先用 pysdf，Kaolin 作为升级路径 |
| 多物体场景 min 操作不可微（argmin 处） | 低 | 实际训练中用 soft-min 或逐物体监督 |

## 7. MVP 实施路线

```
Phase 1: GT SDF 预计算（1-2 天）
├── trimesh 加载 LIBERO/SafeLIBERO 场景 meshes
├── pysdf 计算每个场景的 workspace SDF
├── 4096 点/scene，双尺度近表面 + 均匀采样
└── 保存 .npz 文件

Phase 2: SDF Decoder 训练（2-3 天）
├── 4 层 MLP，256 hidden，输入 [VLA_feature, xyz]
├── L1 clamped loss + Eikonal 正则化
└── 验证 SDF 预测精度（MAE < 1cm near surface）

Phase 3: Action Refinement 集成（2-3 天）
├── SDF 梯度 → collision cost → action token 修正
├── collision_cost = ReLU(-SDF + margin)
└── 端到端微调或 inference-time optimization
```
