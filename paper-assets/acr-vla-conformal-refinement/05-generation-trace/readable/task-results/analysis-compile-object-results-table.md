# analysis compile object results table

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_compile-object-results-table_20260515T183808_result.json`
- **Structured JSON:** [`0cb5f14e44fa47ca14e6.json`](../../sessions/0c/0cb5f14e44fa47ca14e6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。汇总保存在 `artifacts/object_results_summary.md`（`art_20260515_d37b7a`）。

核心数据：

- **8 个有效实验**，81 个 DONE 实验中筛出 14 个 object 相关，6 个 killed/failed 无可用结果
- **最优方法**：ACR obs_only norm=0.2，SR=22%，+10pp over argmin
- **模式排序** (norm=0.1)：obs_only (19%) >> perdof (11%) > scalar (9%)
- **所有 baseline 聚集在 12-13%**：argmin、vla_mean、vla_only 无显著差异
- **obs_only 0.2 vs argmin 逐任务**：赢 6 平 4 输 0，chocolate_pudding 上差距最大 (+30pp)

缺口：perdof norm=0.2 和 obs_only norm=0.3 尚未跑，magnitude sweep 不完整。

---
