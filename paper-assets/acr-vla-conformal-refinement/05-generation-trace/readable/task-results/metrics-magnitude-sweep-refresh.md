# metrics magnitude sweep refresh

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_metrics_magnitude-sweep-refresh_20260515T121354_result.json`
- **Structured JSON:** [`fb37e59a09ee29cf01bd.json`](../../sessions/fb/fb37e59a09ee29cf01bd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

6 个 registry 全部更新完成。汇总：

| Experiment | Norm | Tasks | Avg SR | 状态 |
|---|---|---|---|---|
| perdof-norm003 | 0.03 | 7/10 | 40.0% | alive |
| perdof-norm005 | 0.05 | 7/10 | 40.0% | alive |
| perdof-norm02 | 0.2 | 6/10 | 28.3% | alive |
| perdof-norm03 | 0.3 | 7/10 | 32.9% | alive |
| obsonly-norm005 | 0.05 | 7/10 | 42.9% | alive |
| obsonly-norm02 | 0.2 | 7/10 | 45.7% | alive |

初步趋势：obs_only 模式整体优于 perdof，且 norm=0.2 的 obs_only 目前领先（45.7%）。perdof 在大 norm（0.2, 0.3）时性能下降明显，T2（table_center）和 T5（on_ramekin）对所有配置都是 0%。预计再 ~3 小时可全部跑完。

---
