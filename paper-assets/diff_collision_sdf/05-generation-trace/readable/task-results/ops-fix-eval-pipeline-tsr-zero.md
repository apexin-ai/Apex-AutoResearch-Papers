# ops fix eval pipeline tsr zero

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix_eval_pipeline_tsr_zero_20260522T023143_result.json`
- **Structured JSON:** [`ad7342c2f67492b20965.json`](../../sessions/ad/ad7342c2f67492b20965.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已完成，写入 `artifacts/report_eval_tsr_zero_fix.md`。

---

## 汇总

**根因**：`eval_safelibero.py` 的 `get_action_from_policy` 构建 state 向量时，用了4维四元数+1维gripper（`[pos(3), quat(4), grip[:1]]`），但训练数据是3维旋转向量+2维gripper（`[pos(3), rotvec(3), grip(2)]`）。两者碰巧都是8维不报错，但 z-score normalization 后产生极端 OOD 输入，模型输出垃圾动作。

**修复**：用 `scipy.spatial.transform.Rotation.from_quat().as_rotvec()` 将四元数转为旋转向量，gripper 取完整2维。

**验证**：dry-run 中机器人从完全静止（displacement≈1e-10）恢复为正常运动（displacement=0.659m），执行了合理的 pick-and-place 动作序列。修复已部署到 westd-45947、westd-35807 和本地代码。

**下一步**：需要重跑全量 eval（4 task × 20 episodes）获取真实 TSR 数据。

---
