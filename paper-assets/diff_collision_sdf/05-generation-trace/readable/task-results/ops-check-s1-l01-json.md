# ops check s1 l01 json

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_s1_l01_json_20260525T151902_result.json`
- **Structured JSON:** [`e9611adcdefa3d8d61b7.json`](../../sessions/e9/e9611adcdefa3d8d61b7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据完整，结论如下：

**JSON 包含完整的 per-episode displacement 数据。**

| 项目 | 结果 |
|------|------|
| 文件大小 | 64KB, 2067 行 |
| 修改时间 | **May 25 20:41**（今天） |
| Checkpoint | `a1_sdf_pi05_object_pudding_seed1_l01/30000/` — 确认是 s1_l01 |
| Task 数 | **4** 个 task |
| Episode 总数 | **200**（4 × 50），完整 |
| Per-episode 字段 | 每个 episode 均含 `max_displacement`, `collision_step`, `collision_obstacle`, `success`, `collided`, `total_steps`, `smoothness` |

**4 个 task 汇总指标：**

| Task | TSR | CAR | avg_max_displacement |
|------|-----|-----|---------------------|
| orange_juice | 0.04 | 0.54 | 0.0462 |
| chocolate_pudding | 0.26 | 0.48 | 0.0619 |
| milk | 0.00 | 0.94 | 0.0040 |
| bbq_sauce | 0.00 | 0.14 | 0.0962 |

第一轮 eval 的 200 episode per-episode displacement 数据完整保存，无需重跑。

---
