# analysis experiment summary table

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_experiment_summary_table_20260515T082124_result.json`
- **Structured JSON:** [`fdde423586455a6fff75.json`](../../sessions/fd/fdde423586455a6fff75.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已生成并注册 `experiment_summary.md`。核心结论：

- **Grid-best**: b=0.5 在所有 seed 上最优，PPL 随 b 单调递增
- **Adaptive_fix vs Uniform**: 平均改善 0.0423 PPL，恢复 grid-best 改善量的 91.0%
- **Adaptive_fix vs Grid-best**: PPL 差距仅 0.005，无需网格搜索
- **b\* 分布**: 跨 seed 高度稳定（CV < 2.5%），中位数 0.88
- seed456 的 b=2.0/3.0/5.0 仍在 RUNNING，已在表中标注

---
