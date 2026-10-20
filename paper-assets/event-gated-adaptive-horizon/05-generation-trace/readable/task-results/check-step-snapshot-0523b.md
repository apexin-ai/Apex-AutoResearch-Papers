# check step snapshot 0523b

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_step-snapshot-0523b_20260523T050630_result.json`
- **Structured JSON:** [`9fdf6bcf613ac59f2de0.json`](../../sessions/9f/9fdf6bcf613ac59f2de0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 4 个实验 target 均为 **210,000 steps**。

| exp_id | server | current_step | target | eval_return | ve_ratio | 进度% |
|--------|--------|-------------|--------|-------------|----------|-------|
| exp_050 (PegInsertion CIVO s0) | bjb1-40020 | 165,000 | 210,000 | 9.01 (@162.5K) | 1.94 (@162.5K) | **78.6%** |
| exp_051 (StackCube frozen s0) | bjb1-40020 | 166,600 | 210,000 | 27.87 (@162.5K) | 0.186 (@162.5K) | **79.3%** |
| exp_052 (StackCube CIVO s1) | bjb1-45299 | 166,400 | 210,000 | 39.87 (@162.5K) | 0.095 (@162.5K) | **79.2%** |
| exp_053 (PegInsertion frozen s0) | bjb1-45299 | 18,200 | 210,000 | — (太早) | — | **8.7%** |

要点：
- exp_050/051/052 进度一致 ~79%，最近一次 eval 均在 162.5K 步
- exp_050 PegInsertion CIVO ve_ratio 仍高企 (1.94)，eval_return 仅 9.01，与 StackCube 形成鲜明对比
- exp_052 StackCube s1 ve_ratio 已收敛至 0.095，eval_return 39.87，与 exp_049 s0 一致
- exp_051 frozen StackCube ve_ratio 0.186，eval 27.87，低于 trained 的 39.87
- exp_053 刚启动约 4 小时，尚无 eval 数据

---
