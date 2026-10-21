# code fix displacement metric

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_displacement_metric_20260525T185321_result.json`
- **Structured JSON:** [`fd86d5e36df525a98382.json`](../../sessions/fd/fd86d5e36df525a98382.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修改完成，语法验证通过。变更汇总：

| 行号 | 变更 |
|------|------|
| L933 | `initial_eef_pos = obs.get("robot0_eef_pos", ...).copy()` — warmup 结束后记录 EE 初始位置 |
| L941 | `max_ee_displacement = 0.0` — 初始化 |
| L1025-1026 | 每 step 计算 `ee_disp = np.linalg.norm(eef_pos - initial_eef_pos)`，更新 `max_ee_displacement` |
| L1057 | `ep_result` 新增 `"max_ee_displacement"` 字段 |
| L1098 | 汇总新增 `avg_max_ee_disp` |
| L1110 | summary dict 新增 `"avg_max_ee_displacement"` |

原有 `max_displacement`（障碍物位移）字段完整保留。备份在 `eval_safelibero.py.bak`。

---
