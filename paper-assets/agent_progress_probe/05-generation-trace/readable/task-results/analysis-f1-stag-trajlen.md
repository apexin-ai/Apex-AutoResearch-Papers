# analysis f1 stag trajlen

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_f1-stag-trajlen_20260514T220654_result.json`
- **Structured JSON:** [`e41daa17f2cff57e1ccd.json`](../../sessions/e4/e41daa17f2cff57e1ccd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

| Tercile | Trajectories | Windows | Length Range | Stag Ratio | F1_stag | F1_prog | Macro F1 |
|---------|-------------|---------|-------------|-----------|---------|---------|----------|
| Short   | 186         | 348     | 1-5         | 4.3%      | 0.4615  | 0.9791  | 0.7203   |
| Medium  | 186         | 530     | 5-11        | 17.9%     | 0.8065  | 0.9588  | 0.8826   |
| Long    | 186         | 946     | 11-103      | 35.5%     | 0.8873  | 0.9309  | 0.9091   |

F1_stag 与 trajectory 长度强正相关，但主要是 stagnation prevalence 的 confound：短 trajectory 只有 15 个 stagnation 窗口（4.3%），F1 估计不稳定；长 trajectory 有 336 个（35.5%），F1_stag=0.89。

---
