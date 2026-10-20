# analysis metrics consolidation

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_metrics-consolidation_20260515T041953_result.json`
- **Structured JSON:** [`e0f91710b8806a2000d6.json`](../../sessions/e0/e0f91710b8806a2000d6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个文件已生成并注册：

| 文件 | 行数 | 说明 |
|------|------|------|
| `learning_curves.csv` | 106 rows | 14个实验的 eval_return vs step |
| `nve_trajectories.csv` | 74 rows | v/e ratio 轨迹 + baseline 归一化 |
| `summary_table.csv` | 14 rows | 每个实验的最终指标汇总 |

所有文件在 `artifacts/figures_data/` 目录下，UTF-8 编码，已通过 `register_artifact` 注册。

---
