# harvest deploy bjb1 18228 batch

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest-deploy_bjb1-18228-batch_20260520T130446_result.json`
- **Structured JSON:** [`0109e576800a601245a8.json`](../../sessions/01/0109e576800a601245a8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个实验全部部署成功。

## 收割结果

| 实验 | SR | 关键指标 |
|------|-----|---------|
| eval-adaptive-k-spatial-p90-seed43 | **0.32** | avg_K=3.586, fast_path=80.2%, mean_l2=0.0905 |
| eval-random-selection-spatial-seed43 | **0.26** | — |
| eval-perdof-object-norm02-seed45-r3 | **0.12** | — |

## 部署实验

| exp_id | GPU | PID |
|--------|-----|-----|
| eval-adaptive-k-spatial-p90-seed44 | cuda:0 | 384493 |
| eval-random-selection-spatial-seed42-r2 | cuda:1 | 384767 |
| eval-obs-only-spatial-norm02-seed48 | cuda:2 | 385298 |
| eval-vla-only-spatial-seed48 | cuda:3 | 385639 |

---
