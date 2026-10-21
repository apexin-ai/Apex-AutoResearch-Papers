# research sdf extraction

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_sdf_extraction_20260519T160713_result.json`
- **Structured JSON:** [`7d6f865bfa1f800cb8c8.json`](../../sessions/7d/7d6f865bfa1f800cb8c8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/report_sdf_extraction.md`。核心结论：

**MVP 方案**：`pysdf`（sxyu/sdf）离线预计算 GT SDF，Kaolin 作为 GPU 加速备选。

- **pysdf** 胜出原因：C++ 并行快（100K 点 < 1s）、API 极简、无 GPU 依赖、对 watertight mesh 精度可靠
- **MuJoCo native SDF** 不推荐用于 MVP——Python API 缺失、需 C wrapper、工程复杂度高
- **采样策略**：建议 4096 点/scene（80% 双尺度近表面 + 20% 均匀），2048 对多物体偏少
- **SDF Decoder**：4-6 层 MLP，输入 [VLA_feature, xyz]，L1 clamped loss + Eikonal 正则化
- **主要风险**：mesh 非 watertight（用 trimesh.repair 缓解）

---
