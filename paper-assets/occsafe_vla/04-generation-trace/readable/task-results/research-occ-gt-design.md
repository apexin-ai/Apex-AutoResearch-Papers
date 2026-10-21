# research occ gt design

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_occ-gt-design_20260520T040550_result.json`
- **Structured JSON:** [`3a72d47b612f006201b7.json`](../../sessions/3a/3a72d47b612f006201b7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文档已写入 `artifacts/occ_gt_design.md`。核心要点：

**推荐方案**：直接从 MuJoCo sim state 提取（Method A）。遍历所有 geom，用解析 point-in-shape 测试填充体素网格。64³ 网格 + ~20 geom 约 <10ms/帧，精确且快。

**关键参数**：
- 分辨率 64³，体素 1cm，工作空间 0.64m³
- 5 类语义标签（free/table/robot/target/obstacle）+ binary 版本
- HDF5 + gzip 存储，单 episode ~2.5MB（压缩后）

**工作量**：~3.5 人天（环境探索 → 实现 → 可视化验证 → 数据集生成 → DataLoader 集成）

**主要风险**：SafeLIBERO 的 geom 命名是否规范到足以自动区分 target/obstacle——需要实际加载环境确认。

---
