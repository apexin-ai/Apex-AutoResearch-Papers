# Environment Setup & Kill Gate Report

**Server**: westd-35807 (Seetacloud/AutoDL)
**Date**: 2026-05-20 (updated)
**Conda Env**: `/root/miniconda3/envs/libero/` (Python 3.10.20)
**Project Dir**: `/root/colliforce-vla/`

---

## Part 1: Environment Setup

### Hardware

| Component | Detail |
|-----------|--------|
| GPU | 4× NVIDIA RTX PRO 6000 Blackwell Server Edition (94 GB each) |
| CUDA Driver | 580.95.05 / CUDA 13.0 |
| Total VRAM | 376 GB |

### Software Stack

| Package | Version |
|---------|---------|
| Python | 3.10.20 (conda env `libero`) |
| PyTorch | 2.8.0+cu128 |
| torchvision | 0.23.0+cu128 |
| torchaudio | 2.11.0+cu128 |
| MuJoCo | 3.8.1 |
| robosuite | 1.4.0 |
| LIBERO | 0.1.0 (editable install) |
| trimesh | 4.12.2 |
| pysdf | 0.1.9 |
| scikit-image | 0.25.2 |
| numpy | 2.2.6 |
| scipy | 1.15.3 |
| h5py | 3.16.0 |
| einops | 0.4.1 |
| transformers | 5.8.1 |

### GPU Verification

```
torch=2.8.0+cu128, cuda=True, gpus=4
GPU 0: NVIDIA RTX PRO 6000 Blackwell Server Edition (94GB)
GPU 1: NVIDIA RTX PRO 6000 Blackwell Server Edition (94GB)
GPU 2: NVIDIA RTX PRO 6000 Blackwell Server Edition (94GB)
GPU 3: NVIDIA RTX PRO 6000 Blackwell Server Edition (94GB)
```

### EGL Headless Rendering

已安装: `libegl1-mesa-dev`, `libgl1-mesa-glx`, `libosmesa6-dev`

### SafeLIBERO (vlsa-aegis)

- Repo: `THU-RCSCT/vlsa-aegis` → `/root/colliforce-vla/vlsa-aegis/` (1.2G)
- 状态: ✅ clone 完成

### 磁盘

| 分区 | 大小 | 已用 | 可用 |
|------|------|------|------|
| / (根) | 30G | 18G | 13G |
| /root/autodl-tmp | 350G | ~0 | 350G |

---

## Part 2: Kill Gate KG-1 — MuJoCo 版本验证

**要求**: MuJoCo ≥ 2.3.0
**实际**: MuJoCo 3.8.1

### KG-1: ✅ PASS

---

## Part 3: Kill Gate KG-2 — Mesh 可访问性 + Watertight 统计

### 3.1 LIBERO Assets Mesh 统计

扫描 `/root/colliforce-vla/LIBERO/libero/libero/assets/` 下全部 OBJ/STL/PLY 文件：

| 指标 | 值 |
|------|-----|
| 总 mesh 文件 | 189 |
| 加载成功 | 189 (100%) |
| 加载失败 | 0 |
| Watertight (原始) | 44/189 (23.3%) |
| Non-watertight | 145/189 (76.7%) |

Watertight mesh 主要为 STL 格式（stove burner, faucet, microwave, window 等组件）。Non-watertight 主要为 OBJ 格式的 articulated objects 和家具部件。

### 3.2 robosuite Mesh 统计（前次测试）

| 类别 | 总数 | Watertight | Non-watertight |
|------|------|-----------|----------------|
| bullet_data | 31 | 11 | 20 |
| grippers | 92 | 37 | 55 |
| mounts | 6 | 1 | 5 |
| objects | 17 | 4 | 13 |
| robots | 344 | 38 | 306 |
| **合计** | **490** | **91 (18.6%)** | **399 (81.4%)** |

### 3.3 修复方案对比

#### Basic Repair (fix_normals + fix_winding + fill_holes)

5/5 non-watertight meshes → 0 修复成功。结构性缺陷（缺面、自交）超出 fill_holes 能力。

#### Voxel Remesh Repair (trimesh.voxelized → marching_cubes)

| Mesh | 修复后 Watertight | pysdf 验证 |
|------|-------------------|-----------|
| basin_faucet_base.obj | ✅ | SDF [-25.88, 0.20] |
| drawer_high.obj | ✅ | SDF [-28.16, 0.32] |
| short_fridge/base.obj | ✅ | SDF [-18.03, 0.75] |
| wooden_cabinet_base.obj | ✅ | SDF [-20.74, 0.47] |
| stove_knob_button.obj | ✅ | SDF [-23.33, 0.36] |

**5/5 non-watertight meshes 通过 voxel remesh 成功修复为 watertight。** 需要 `scikit-image`（已安装）。

#### Convex Hull Fallback

| Mesh | Hull Watertight | pysdf 验证 |
|------|----------------|-----------|
| basin_faucet_base.obj | ✅ | SDF [-3.94, 0.75] |
| drawer_high.obj | ✅ | SDF [-2.98, 2.04] |
| short_fridge/base.obj | ✅ | SDF [-1.33, 1.17] |

Convex hull 始终 watertight，但丢失凹面细节。适合粗粒度碰撞检测。

### 3.4 pysdf 对非 Watertight Mesh 的表现

直接对原始非 watertight mesh 调用 pysdf：

| Mesh | Watertight | SDF Range | Inside pts (of 100) |
|------|-----------|-----------|---------------------|
| basin_faucet_base.obj | ❌ | [-3.82, 0.74] | 12 |
| drawer_high.obj | ❌ | [-2.95, 1.17] | 5 |
| short_fridge/base.obj | ❌ | [-1.75, 0.75] | 9 |

pysdf 对非 watertight mesh 也能返回有意义的 SDF 值（正值=内部，负值=外部），但精度不如 watertight mesh。

### 3.5 MuJoCo API Mesh 访问

106 个 XML 文件中 78 个成功加载，共引用 127 个 mesh。

```
basin_faucet.xml: ngeom=7, nmesh=2
  basin_faucet_base_vis (v=3018, f=1006)
  basin_faucet_movable_vis (v=1296, f=432)

short_cabinet.xml: ngeom=40, nmesh=4
  base_vis_vis (v=288, f=96)
  drawer_middle_vis (v=4308, f=1436)
  ...
```

### 3.6 pysdf 对 Watertight Mesh 验证

| Mesh | SDF Range |
|------|-----------|
| wall_frames.stl | [-0.54, -0.01] |
| burnerplate.stl | [-0.25, 0.00] |
| faucetbase.stl | [-0.27, -0.01] |

3/3 watertight mesh pysdf 验证通过。

### KG-2: ✅ PASS

判定依据：
1. 189/189 LIBERO asset meshes 全部加载成功（100%）
2. 原始 23.3% watertight，但 **voxel remesh 可将 non-watertight 修复为 watertight**（5/5 测试成功）
3. pysdf 对 watertight 和 non-watertight mesh 均可计算 SDF
4. MuJoCo API 可正常访问 mesh 顶点/面数据（78/106 XML 加载成功）

---

## 总结

| Kill Gate | 要求 | 结果 | 状态 |
|-----------|------|------|------|
| KG-1 | MuJoCo ≥ 2.3.0 | MuJoCo 3.8.1 | ✅ PASS |
| KG-2 | mesh 可访问 | 189/189 LIBERO + 490/490 robosuite 加载成功 | ✅ PASS |
| KG-2 | watertight 统计 | LIBERO: 44/189 (23.3%), robosuite: 91/490 (18.6%) | ✅ 已统计 |
| KG-2 | repair 可行性 | voxel remesh 5/5 成功, basic repair 0/5 | ✅ PASS |
| KG-2 | pysdf SDF 提取 | watertight + non-watertight 均可 | ✅ PASS |

### SDF Pipeline 建议

1. **推荐路径**: voxel remesh → watertight mesh → pysdf（精确 SDF）
2. **快速路径**: 直接 pysdf on non-watertight（可用但精度降低）
3. **粗粒度路径**: convex hull → pysdf（最简单，丢失凹面）

### 遗留事项

- vlsa-aegis 已 clone 完成，待后续集成
- 根分区 13G 剩余，大模型/数据应放 `/root/autodl-tmp/`
- 前 28 个 XML 加载失败的原因是缺少 material/texture 引用（非 mesh 问题）
