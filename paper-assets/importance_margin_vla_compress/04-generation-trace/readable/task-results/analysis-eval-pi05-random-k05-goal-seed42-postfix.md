# analysis eval pi05 random k05 goal seed42 postfix

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_pi05_random_k05_goal_seed42_postfix_20260524T103524_result.json`
- **Structured JSON:** [`931063af9a48a4244c12.json`](../../sessions/93/931063af9a48a4244c12.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE (success)。

## 结果汇总

**overall_sr = 73.6%** (368/500)

### Per-task breakdown

| Task | Description | SR |
|------|-------------|-----|
| T0 | open the middle drawer of the cabinet | 78% |
| T1 | put the bowl on the stove | 44% |
| T2 | put the wine bottle on top of the cabinet | 86% |
| T3 | open the top drawer and put the bowl in | 76% |
| T4 | put the bowl on top of the cabinet | 92% |
| T5 | push the plate to the front of the stove | 70% |
| T6 | put the cream cheese in the bowl | 62% |
| T7 | turn on the stove | 100% |
| T8 | put the bowl on the plate | 86% |
| T9 | put the wine bottle on the rack | 42% |

### 对比

| 条件 | Goal SR |
|------|---------|
| Baseline (no pruning) | 88.4% |
| Random k=0.7 | 78.0% |
| **Random k=0.5** | **73.6%** |
| Object k=0.5 | 69.4% |

**conclusion = success**

Random k=0.5 Goal SR=73.6%，相对 baseline 88.4% 下降 14.8pp（保留率 83.3%）。Disruption curve 在 Goal suite 上呈现平缓下降趋势：k=0.7→78.0%, k=0.5→73.6%，说明 Random pruning 在 Goal 上对 50% token 移除仍有较好鲁棒性。值得注意的是 Goal k=0.5 (73.6%) 反而高于 Object k=0.5 (69.4%)，表明 Goal suite 对视觉 token 压缩更鲁棒。

---
