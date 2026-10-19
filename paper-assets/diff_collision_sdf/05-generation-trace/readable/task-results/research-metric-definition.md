# research metric definition

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_metric_definition_20260524T055031_result.json`
- **Structured JSON:** [`1bbe75ee4d5232af87bd.json`](../../sessions/1b/1bbe75ee4d5232af87bd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文档已写入 `artifacts/metric_definitions.md`。核心决策：

**safe_rate → SSR (Safe Success Rate)**
- 公式：`(success ∧ ¬collided) / total`
- 选 Definition A。`success=True` 隐式排除 frozen episode，所以不需要显式加 `¬frozen`（Definition C 等价）。Definition B 不要求成功，语义弱。SSR 直接回答"能否安全完成任务"，且 SSR = TSR × P(¬collided|success)，分析价值高。

**min_obs → MinObs (Min. Obstacle Clearance)**
- 公式：成功 episode 的 `min_ee_obstacle_distance` 均值，单位 cm
- 仅对成功 episode 计算（frozen/失败轨迹无意义）。用均值（样本量够大，可加性好，便于报 mean±std）。可选补充 P10 作为 worst-case。

文档包含数学公式、字段映射、Python 计算脚本、论文表格列名建议、以及为什么主表不报 CAR 的论证。

---
