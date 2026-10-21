# eval seed robustness extended

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_seed-robustness-extended_20260515T192102_result.json`
- **Structured JSON:** [`d06ae08e6cd4e40f4576.json`](../../sessions/d0/d06ae08e6cd4e40f4576.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。汇总结果：

## 8-Seed Robustness 汇总

| | balanced_acc | internal_recall | eval_loss |
|---|---|---|---|
| **Core (42-45)** | 0.5538 ± 0.052 | 0.5205 ± 0.110 | 0.358 ± 0.085 |
| **Extended (46-49)** | 0.5282 ± 0.068 | 0.4416 ± 0.193 | 0.396 ± 0.012 |
| **Combined (8-seed)** | **0.541 ± 0.058** | **0.481 ± 0.152** | **0.377 ± 0.060** |

逐 seed 明细：

| Seed | balanced_acc | internal_recall | eval_loss |
|------|-------------|----------------|-----------|
| 42 | 0.5761 | 0.5152 | 0.2400 |
| 43 | 0.4852 | 0.3667 | 0.4363 |
| 44 | 0.6074 | 0.6000 | 0.3996 |
| 45 | 0.5467 | 0.6000 | 0.3562 |
| 46 | 0.4463 | 0.2333 | 0.3941 |
| 47 | 0.5185 | 0.4333 | 0.4051 |
| 48 | 0.5370 | 0.4000 | 0.3788 |
| 49 | 0.6111 | 0.7000 | 0.4051 |

Extended seeds 与 core seeds 表现一致（balanced_acc 差异 ~2.5pp，在 std 范围内）。8-seed combined std=0.058 略大于 4-seed 的 0.052，internal_recall 方差较大（0.23–0.70 range），是主要不稳定来源。

---
