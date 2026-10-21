# analysis control b results

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_control-b-results_20260515T141104_result.json`
- **Structured JSON:** [`8cae02654d6ec065651e.json`](../../sessions/8c/8cae02654d6ec065651e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均已更新为 DONE。

**Control B 结果总结：**

| | trained + shuffled | untrained + shuffled |
|---|---|---|
| best layer | 8 | 1 |
| per_task_mean_ρ | 0.0125 | 0.0093 |
| pooled_ρ | 0.0123 | 0.0085 |
| R² | -0.0014 | -0.0031 |
| 所有层 max \|ρ\| | 0.0125 | 0.0093 |

**结论：Control B 通过。** 两个实验的 ρ 均 ≈ 0（远低于 0.1 红旗线），R² 为负，probe 在 shuffled labels 上完全无法学到有意义的 temporal distance 信息。这验证了原始 probe 实验中观测到的 ρ 确实来自 label-feature 对应关系，而非数据中的伪信号。

---
