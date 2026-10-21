# code occ gt pipeline continue

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_occ-gt-pipeline-continue_20260520T065536_result.json`
- **Structured JSON:** [`b89759f606edfe286a5e.json`](../../sessions/b8/b89759f606edfe286a5e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

下载因 AutoDL 代理无法稳定连接 XET CDN 而极慢。脚本会在后台持续重试。让我整理当前已完成的 9/10 任务的报告。

## 当前状态汇总

### Step 1-2: 已完成的工作

**Pipeline 代码** (`/root/occsafe_vla/occ_pipeline/`): 完整
- `extract_occupancy.py` — 主提取脚本，支持 `--all`/`--task_id` + `--max_demos`
- `occupancy_3d.py` — 3D 体素占据计算（64³），支持 BOX/SPHERE/CYLINDER/CAPSULE/ELLIPSOID/MESH
- `geom_classifier.py` — 语义分类：0=free, 1=table, 2=robot, 3=target
- `bev_projection.py` — 3D→BEV 投影 (any-axis=2, max-axis=2)
- `visualize_bev.py` — BEV 可视化工具

**已完成提取 (9/10)**:

| 任务 | Demo数 | 帧数 | 占据率 | 语义分布 (free/table/robot/target) | avg ms/帧 | 文件大小 | 异常帧 |
|------|--------|------|--------|-----------------------------------|-----------|----------|--------|
| between_plate_ramekin | 1 | 98 | 42.4% | 57.6/17.3/14.1/10.9 | 1287 | 84K | 无 |
| from_table_center | 1 | 103 | 40.6% | 59.4/16.6/12.2/11.8 | 1252 | 86K | 无 |
| in_top_drawer_cabinet | 1 | 153 | 45.5% | 54.5/19.3/14.5/11.8 | 1243 | 123K | 无 |
| next_to_cookie_box | 1 | 123 | 42.8% | 57.2/13.2/16.1/13.5 | 1253 | 111K | 无 |
| next_to_plate | 1 | 115 | 39.1% | 60.9/16.1/12.6/10.4 | 1202 | 91K | 无 |
| next_to_ramekin | 1 | 152 | 37.9% | 62.1/17.0/8.8/12.1 | 1255 | 122K | 无 |
| on_cookie_box | 1 | 99 | 40.6% | 59.4/13.7/14.5/12.3 | 1251 | 84K | 无 |
| on_ramekin | 1 | 137 | 40.1% | 59.9/16.4/12.9/10.9 | 1273 | 110K | 无 |
| on_stove | 1 | 155 | 34.2% | 65.8/11.9/9.7/12.6 | 1248 | 119K | 无 |

**质量验证**:
- 无全零帧，无全一帧
- 占据率 34-46%，合理
- 语义分布：robot/target/table 均有合理占比，target 10-14%
- 速度：~1250 ms/帧
- 9 个 BEV 可视化已保存到 `/root/occsafe_vla/artifacts/bev_*.png`

### Step 3: 缺失任务

**Task 9: `on_the_wooden_cabinet`** — demo HDF5 文件（688MB）从 HuggingFace XET CDN 下载中，AutoDL 代理连接不稳定。后台脚本持续重试中：
- 下载脚本 PID: 50093 (`/tmp/dl_fast_retry.py`)，日志 `/tmp/dl_fast_retry.log`
- 提取脚本 PID: 49895 (`/tmp/extract_and_validate.sh`)，自动等待文件就绪后提取
- 当前已下载：42MB/689MB

### 数据路径
- 占据数据：`/root/occsafe_vla/occ_data/occ_*.hdf5`（每文件含 `data/demo_0/bev_binary` (T,64,64) bool + `bev_semantic` (T,64,64) uint8）
- 可视化：`/root/occsafe_vla/artifacts/bev_*.png`
- 源 demo：`/root/autodl-tmp/libero_datasets/libero_spatial/*.hdf5`

### 注意
- 每个任务当前只提取了 **demo_0**（1/50 demos），源文件各含 50 个 demo
- 如需全部 50 demos，每任务额外需 ~100 分钟（50 demos × 100帧 × 1.25s/帧）
- 第 10 个任务下载完成后会自动提取（后台脚本处理中）

---
