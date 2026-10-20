# analysis dof dependency table

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_dof-dependency-table_20260529T083118_result.json`
- **Structured JSON:** [`61d83c5258206d933cd8.json`](../../sessions/61/61d83c5258206d933cd8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已写入 `artifacts/dof_dependency_analysis.md` 并注册 (`art_20260529_1ba48e`)。

核心发现：

| DoF | 环境 | CIVO Rate | 模式 |
|-----|------|-----------|------|
| 1 | Cartpole | 0/3 | 非 value-driven 退化 |
| 4 | Hopper | 0/1 | learning delay→自恢复 |
| 6 | Walker | 3/5 (60%) | **CIVO** |
| 6 | Cheetah | 3/4 (75%) | **CIVO** |
| 12 | Quadruped | — | baseline 自身不稳定 (NVE=6.6×) |
| 21 | Humanoid | — | baseline 自身不稳定 (NVE=12.97×) |

CIVO 存在 "Goldilocks zone"：仅在 6-DoF 多关节运动中稳定出现。低 DoF 不触发，高 DoF baseline 本身已有 value overestimation 无法隔离。Discussion 段落已包含在文件末尾。

---
