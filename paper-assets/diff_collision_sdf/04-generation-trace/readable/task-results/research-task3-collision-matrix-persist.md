# research task3 collision matrix persist

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_task3_collision_matrix_persist_20260524T045955_result.json`
- **Structured JSON:** [`1afa74b682aadbf6effc.json`](../../sessions/1a/1afa74b682aadbf6effc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Artifact 已生成并验证，数据一致性确认通过。

文件：`artifacts/task3_collision_matrix_step10k.md`

关键发现：

| Metric | Baseline | A1 l005 | A1 l01 |
|--------|----------|---------|--------|
| TSR | 0.78 | 0.60 | 0.52 |
| CAR | 0.24 | 0.26 | 0.28 |
| n_collision_free | 12 | 13 | 14 |

- **碰撞总数**几乎不变（38→37→36），CAR 提升极微（+2/+4 pct）
- **碰撞转移效应**：yellow_book 碰撞减少（8→4/6），但 wine_bottle 碰撞增加（8→11/9）——障碍物间碰撞发生了重分布而非整体减少
- **TSR 代价巨大**：success+safe 从 11 降到 2-3，大量转为 fail+safe（1→11）——模型学会了回避但同时丧失了完成任务的能力
- **moka_pot 碰撞完全不变**（12/12/12），SDF loss 对该障碍物无效
- Baseline 的 min_ee_dist 字段缺失（baseline eval 版本不含该字段），标记为 "-"

---
