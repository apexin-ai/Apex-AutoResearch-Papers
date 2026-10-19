# code sdf pipeline validation

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_sdf_pipeline_validation_20260519T174452_result.json`
- **Structured JSON:** [`fb5fb86d43e0769f1e45.json`](../../sessions/fb/fb5fb86d43e0769f1e45.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Pipeline 完成，所有质量检查通过。

**结果汇总：**

| 场景 | Mesh总数 | Watertight | 梯度准确率 | 符号验证 | 状态 |
|------|---------|-----------|-----------|---------|------|
| spatial_bowl | 68 | 21 (30.9%) | **98.7%** | PASS | PASS |
| object_chocolate | 60 | 17 (28.3%) | **99.7%** | PASS | PASS |

**产出文件：**
- `data/sdf_gt_spatial_bowl.npz` / `data/sdf_gt_object_chocolate.npz` — SDF GT (4084 点, 含 query_points + sdf_values)
- `artifacts/sdf_slice_*.png` — 2D 切面可视化 (SDF 等值线 + 梯度箭头)
- `artifacts/report_sdf_pipeline.md` — 完整报告
- `sdf_pipeline.py` — 可复用的 pipeline 脚本

**关键确认：**
- pysdf 符号翻转已正确应用（`sdf = -pysdf_output`）
- collision cost `ReLU(-SDF + margin)` 在物体内部正确产生正惩罚
- 梯度方向验证均 ≥ 90%，无 blocker
- 非 watertight mesh 主要是机器人臂部件，不影响场景障碍物 SDF

---
