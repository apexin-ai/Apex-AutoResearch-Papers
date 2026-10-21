# ops fix step sync

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix-step-sync_20260513T065713_result.json`
- **Structured JSON:** [`c0395ee2a81c8c2111b8.json`](../../sessions/c0/c0395ee2a81c8c2111b8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

action_repeat=2。所以 metrics 中的 step=56000 是环境步数，而 WorldModel._step = 56000 / 2 = 28000。28000 < 50000，所以 gate_scale=0.0 是**正确的行为**。

Phase 2 阈值 50000 是 raw steps，对应 metrics step = 100000（50000 * action_repeat）。当前 metrics step=56000，实际 raw step=28000，还没到 Phase 2。

**修复已生效，Phase 2 尚未到达。** 

## 汇报

| 项目 | 值 |
|------|------|
| 新 PID | 25923 |
| 续训起始 step | ~52000 (env steps) |
| 当前 step | 56000 (env steps) = 28000 raw steps |
| gate_scale | 0.0 (正确：raw step 28000 < 50000 阈值) |
| gate_dt_mean | 1.0 (正确：Phase 1 未激活 gate) |

**结论**：`self._wm._step = self._step` 修复已正确应用，语法通过，训练正常进行。Phase 2 会在 raw step 达到 50000（即 metrics step=100000）时激活，预计还需 ~72000 env steps（约 1 小时）。届时 gate_scale 会从 0 开始线性增长。

---
