# harvest k20 object metrics

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_k20-object-metrics_20260521T050359_result.json`
- **Structured JSON:** [`73a602ecb69b288822ba.json`](../../sessions/73/73a602ecb69b288822ba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

5 个实验 metrics 全部补录完成。

## 结果汇总

**CRM Object K=20:**

| exp_id | seed | SR |
|--------|------|----|
| eval-crm-object-k20-seed42 | 42 | 0.20 |
| eval-crm-object-k20-seed43 | 43 | 0.18 |
| eval-crm-object-k20-seed44 | 44 | 0.18 |
| **mean ± std** | | **0.187 ± 0.009** |

**obs_only Object K=20:**

| exp_id | seed | SR |
|--------|------|----|
| eval-k20-obs-only-object-seed42 | 42 | 0.20 |
| eval-k20-obs-only-object-seed43 | 43 | 0.18 |
| eval-k20-obs-only-object-seed44 | 44 | 0.18 |
| **mean ± std** | | **0.187 ± 0.009** |

两组结果完全一致（相同 checkpoint、相同 mode `crm_obs_only`、相同 norm=0.2），K=20 相比 K=10 没有显著提升。

---
