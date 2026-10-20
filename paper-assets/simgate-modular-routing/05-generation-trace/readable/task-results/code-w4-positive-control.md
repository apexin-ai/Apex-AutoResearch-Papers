# code w4 positive control

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_w4-positive-control_20260521T210506_result.json`
- **Structured JSON:** [`9c8b4e3534121f1194b1.json`](../../sessions/9c/9c8b4e3534121f1194b1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**实验结果**：
- **5-fold CV**: LogReg 和 MLP 均达到 **64.7% BA**，仅用 task-type one-hot 就超过所有 step-level Qwen3 routers（最高 59.3%）
- **LOTO**: 4 个 mixed task types 全部掉到 **50.0% BA**（随机水平），7 个 pure task types trivially 100%
- 数据结构：7/11 task types 是纯 det-preferred，仅 4 个有 mixed labels

**核心结论**：routing signal 是 task-type-level property，step-level router 的 56–59% 本质是在用 observation 间接推断 task type identity，且推断效果还不如直接看 task type。这支撑 "signal-limited, not architecture-limited" 的 rebuttal narrative。

产出文件：
- 远程：`artifacts/w4_task_type_positive_control.json`（完整 JSON 结果）
- 本地：`artifacts/w4_task_level_router_results.md`（对比表 + 分析）

---
