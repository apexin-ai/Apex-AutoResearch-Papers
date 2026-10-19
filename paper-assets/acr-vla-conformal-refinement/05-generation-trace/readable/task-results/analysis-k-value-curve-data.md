# analysis k value curve data

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_k-value-curve-data_20260518T033836_result.json`
- **Structured JSON:** [`139048f38b364e2e2eb4.json`](../../sessions/13/139048f38b364e2e2eb4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

JSON 已创建并注册 (`art_20260518_aea319`)。

数据摘要：

| K | Mean SR | Std | 95% CI | Seeds |
|---|---------|-----|--------|-------|
| 1 | 10.3% | 1.53% | [8.6%, 12.1%] | 3 (multiscale) |
| 5 | 14% | — | — | 0 (unverified) |
| 10 | 17.5% | 2.81% | [15.3%, 19.8%] | 6 |

Baselines: VLA-only 10.8% (4 seeds), Argmin 12.4% (5 seeds).

K=5 注意：registry 中 `eval-obs-only-object-norm02-k5-seed42` 状态为 failed，无指标记录，服务器上也无 JSON 日志。14% 为用户报告值，标记为 `data_status: "unverified"`。K=1 同时收录了 multiscale 和 accg 两种方法的数据（accg 放在 `alt_method` 中）。

---
