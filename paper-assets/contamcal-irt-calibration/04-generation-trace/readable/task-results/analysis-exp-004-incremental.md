# analysis exp 004 incremental

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp-004-incremental_20260514T123017_result.json`
- **Structured JSON:** [`7f891fd43697689a32cf.json`](../../sessions/7f/7f891fd43697689a32cf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

更新完成。v3→v4 变化：

- **auc0.80_n50**: 9→10 seeds，bias 从 +0.009 降至 +0.006，RMSE 从 0.031 降至 0.030，CI95 coverage 保持 100%
- **auc0.80_n100**: 新增 1 seed — γ̂=0.508, bias=+0.008, CI95 width=0.116, θ_corr=0.962。CI width ratio (AUC=0.80/0.55) 在 N=100 为 1.81×，与 N=20/50 的 1.87–1.95× 一致，继续支持 multiplicative 无交互结论
- 1/√N scaling 新增两个 AUC=0.80 数据点（n20→100, n50→100），偏差 < 1%
- 总 runs: 46→48，所有核心 findings 不变

报告写入 `artifacts/exp004_incremental_analysis.md`。

---
