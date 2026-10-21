# paper limitations dof boundary

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_limitations-dof-boundary_20260529T091446_result.json`
- **Structured JSON:** [`96fe68daac235e3717c4.json`](../../sessions/96/96fe68daac235e3717c4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

段落已插入 `conclusion.tex` 第13行，紧接在原有 Limitations 段落之后。~197词，覆盖：

- 6-DoF 为 CIVO 唯一确认发生区间（Walker 60%, Cheetah 75%）
- 低 DoF 不触发（Cartpole: non-value-driven degradation; Hopper: transient delay + recovery，标注 $n{=}1$）
- 高 DoF baseline 自身不稳定（Quadruped NVE=6.6×, Humanoid NVE=12.97×），无法隔离 gate-induced CIVO
- Future direction: 改善 base algorithm stability 可能上移 onset boundary

---
