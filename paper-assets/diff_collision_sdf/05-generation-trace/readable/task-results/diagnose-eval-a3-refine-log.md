# diagnose eval a3 refine log

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_a3_refine_log_20260521T194744_result.json`
- **Structured JSON:** [`1638dbe40d39925e048f.json`](../../sessions/16/1638dbe40d39925e048f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### Refine eval 结果：**完全失败**
- **TSR = 0%**, **CAR = 0%**（50 episodes）
- 所有 episode 在 step 0 就碰撞（`collision_step=0`），`refine_count=0`——refinement 机制从未激活
- 碰撞对象：主要是 `moka_pot_obstacle_1`，少量 `white_storage_box_obstacle_1`
- 根因：初始动作立即触发碰撞，refinement 来不及介入

### No_refine eval 状态：**正在运行**
- PID 235230，GPU 1，已运行约 2.5 分钟
- 日志：`a3_object_pudding_no_refine_v5.log`（目前只有模型加载阶段）
- 注：此前有一次 no_refine 尝试因 `CUDA error: invalid device ordinal` 崩溃，当前是重试

### Registry 已更新
- `eval_a3_object_pudding_refine` → DONE (negative)，metrics 已写入
- cron 已删除

---
