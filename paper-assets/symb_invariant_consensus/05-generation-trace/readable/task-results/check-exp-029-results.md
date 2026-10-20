# check exp 029 results

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp-029-results_20260518T153603_result.json`
- **Structured JSON:** [`b3f53efcdebb3ce572aa.json`](../../sessions/b3/b3f53efcdebb3ce572aa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。

## exp-029 结果：**负结果**

| Metric | Value |
|---|---|
| **Contrastive accuracy** | 72.53% (132/182) |
| **SC baseline** | 73.63% (134/182) |
| **Delta** | **-1.10pp** |
| **Discriminative rate** | 6.04% (11/182) — 目标 >20%, baseline 8.2%, 更差 |
| **Recovery rate** | **-8.3%** (vs oracle 13.24pp gap) |
| **McNemar p-value** | 0.7518 (不显著) |

**Disagree breakdown** (11 cases): contrastive wins 4, SC wins 6, both wrong 1

**Constraint distribution**: Supporting 43.2%, Opposing 56.8%, avg 24.4 extracted / 10.4 unique per problem

**结论**: 假设被证伪。Contrastive constraint extraction 在全量 FOLIO 204 上不仅没有提升，反而略低于 SC baseline。discriminative rate (6.04%) 甚至低于之前的 baseline (8.2%)。早期 n=14 的 +14.3pp 增益是小样本偏差。opposing constraints 虽然数量略多 (56.8%)，但未能转化为有效的区分信号。

---
