# code fix m024 eval coordinate bug

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_m024_eval_coordinate_bug_20260522T165121_result.json`
- **Structured JSON:** [`4815f047462465a01f97.json`](../../sessions/48/4815f047462465a01f97.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两台服务器修复完成。

### 修改内容

**Line 317** (`_refine_action_a3` 函数)：

```python
# 原代码
next_ee = action[:3]  # openpi AbsoluteActions: action is absolute target position

# 修复后
next_ee = current_ee + action[:3]  # M024: delta -> absolute for SDF query
```

`current_ee = obs.get("robot0_eef_pos", np.zeros(3))` 已在上一行（316行）存在，无需额外修改函数签名或调用者——`obs` 已作为参数传入。

### 两台服务器状态

| 服务器 | 修改 | 语法验证 |
|--------|------|---------|
| westd-35807 | OK | SYNTAX OK |
| westd-45947 | OK | SYNTAX OK |

### 其他相关坐标问题

A1 logging 部分（~line 775）使用 `ee_pos = obs.get("robot0_eef_pos")` 作为 SDF 查询位置——这是当前 EE 位置（不是 next），用于 logging 是合理的，但与 A3 的语义（查询 next EE）不完全一致。如果需要 A1 logging 也查询 next EE，同样需要加 `+ action[:3]`，但这不影响 A1 的 action 输出（A1 不做 refinement），所以优先级低。

---
