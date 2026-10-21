# research eval collision analysis enhancement

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_eval_collision_analysis_enhancement_20260524T050014_result.json`
- **Structured JSON:** [`2c1f3223bcf8dd5861b2.json`](../../sessions/2c/2c1f3223bcf8dd5861b2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

方案已写入 `artifacts/eval_collision_enhancement_plan.md`。

核心发现：

**现有字段**：`collision_obstacle`（首碰障碍物名）和 `collision_step` 已经可以做基础碰撞分布对比，但不够。

**必须新增**：
- `per_obstacle_displacement` — 当前 `max_displacement` 是跨所有障碍物的聚合值，无法区分哪个障碍物被撞移
- `all_collided_obstacles` — 碰撞检测在首次命中后停止（`if not collided:` guard），只记录第一个
- `per_obstacle_min_ee_distance` — 同样是聚合值

**代码改动量**：约 15 行 diff，合并了原来重复的 `get_obstacle_positions` 调用（实际还快了一点），完全向后兼容。

**不需要**：EE trajectory 存储、碰撞方向向量 — per-obstacle displacement + collision distribution 已足够验证碰撞转移假说。

---
