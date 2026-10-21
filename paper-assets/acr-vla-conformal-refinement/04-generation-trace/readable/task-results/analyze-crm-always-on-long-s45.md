# analyze crm always on long s45

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_crm-always-on-long-s45_20260528T032552_result.json`
- **Structured JSON:** [`497d25af09eab194117b.json`](../../sessions/49/497d25af09eab194117b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE (conclusion=success)。

## 总结

**s45 = 43.5%**，与已有 3 seeds 高度一致：

| Seed | Success Rate |
|------|-------------|
| s42 | 41.0% |
| s43 | 45.5% |
| s44 | 43.0% |
| **s45** | **43.5%** |
| **4-seed 均值** | **43.25 ± 1.9%** |

vs VLA-only Long baseline: **58.0 ± 1.5%**

关键指标：trigger_rate=100%，mean_uncertainty=0.1292。无 OOM/CUDA 错误，200 episodes 全部正常完成。

s45 结果进一步巩固了假说：CRM always-on (τ=0.001) 在 Long suite 造成 ~14.8pp 性能下降，方差极小（1.9%），说明这个负面效应是稳定可复现的。

---
