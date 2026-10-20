# diagnose seed robustness core

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_seed-robustness-core_20260515T134359_result.json`
- **Structured JSON:** [`cbcf9c62c9cb0cb9155a.json`](../../sessions/cb/cbcf9c62c9cb0cb9155a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

seed-robustness-core 诊断完成：

**结果：成功。** 4 个 seed 全部完成，registry 已更新为 DONE，cron 已清除。

**Router 跨 seed 稳定性：**
| Seed | balanced_acc | internal_recall | eval_loss |
|------|-------------|----------------|-----------|
| 42 | 0.5761 | 0.5152 | 0.240 |
| 43 | 0.4852 | 0.3667 | 0.436 |
| 44 | 0.6074 | 0.600 | 0.400 |
| 45 | 0.5467 | 0.600 | 0.356 |
| **Mean±Std** | **0.554±0.052** | **0.520±0.110** | **0.358±0.085** |

**Decomposition bootstrap (1000 resamples)：**
- DAF: 90.6% ± 4.2%, CI [81.6%, 98.8%]
- Pearson r: 0.975 ± 0.011, CI [0.952, 0.995]
- Jackknife: no single task dominates

---
