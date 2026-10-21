# paper iclr reframe p0

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_iclr-reframe-p0_20260528T233554_result.json`
- **Structured JSON:** [`0c391a0296f610ccb539.json`](../../sessions/0c/0c391a0296f610ccb539.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

编译成功，42页，无错误。

### Diff 汇总

**introduction.tex** (2处)：
1. 第1句：`directly on physical hardware` → `in complex continuous control tasks`
2. 第2句整句重写：删除 `Real robotic tasks` / `manipulation requires fast reactive grasping` / `sim-to-real transfer`，替换为 `Continuous control demands temporal abstraction: locomotion with heterogeneous gait phases, contact-rich tasks with variable sensing rates, and multi-rate decision-making across planning horizons all require handling $\dt$ mismatches.`
3. 末段尾句：`As world-model RL moves toward real systems with variable-rate sensing, understanding when temporal conditioning fails is essential for safe deployment.` → `...incorporates variable-rate decision-making...essential for the architectural design of variable-rate model-based RL.`

**abstract_body.tex** (2处)：
1. 首句：`increasingly deployed for robot control, where temporal abstraction` → `increasingly targets continuous control tasks where temporal abstraction`
2. 尾句：`whose mechanism requires further study` → `highlighting open challenges in the architectural design of variable-rate model-based RL`

**main.tex**：Keywords 无需修改，已无 robotics 措辞。`DreamerV3` 保留。

---
