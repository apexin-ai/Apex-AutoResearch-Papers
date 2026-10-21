# ssh fix eval collision norm

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fix_eval_collision_norm_20260521T061444_result.json`
- **Structured JSON:** [`a970cb888a4aa93bc555.json`](../../sessions/a9/a970cb888a4aa93bc555.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

语法通过。修改汇报：

**修改前（行 389-391）：**
```python
            displacement = np.linalg.norm(
                current_positions[name] - initial_positions[name]
            )
```

**修改后（行 389-391）：**
```python
            displacement = np.sum(np.abs(
                current_positions[name] - initial_positions[name]
            ))
```

碰撞位移计算从 L2 范数改为 L1 范数，仅此一处修改，语法验证通过。

---
