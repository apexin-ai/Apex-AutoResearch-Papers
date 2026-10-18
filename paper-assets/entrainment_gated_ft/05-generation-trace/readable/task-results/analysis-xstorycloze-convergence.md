# analysis xstorycloze convergence

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_xstorycloze-convergence_20260519T163303_result.json`
- **Structured JSON:** [`fa4afda020dac24b7900.json`](../../sessions/fa/fa4afda020dac24b7900.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已出。核心结论：

**xstorycloze_en 不是第二个 significant anchor。**

| 指标 | 值 |
|---|---|
| Spearman ρ (std vs attention_ratio) | **-0.60** (方向正确：更多 attention → 更收敛) |
| Exact permutation p | **0.35** (远不显著) |
| 10-benchmark Bonferroni | p=1.0 |
| 2-benchmark Bonferroni (与 LAMBADA) | p=0.70 |

**10 个主要 benchmark 统一校正后，无一显著**——包括 LAMBADA（raw p=0.0167，Bonferroni 10 校正后 p=0.167）。LAMBADA 仅在 2-benchmark Bonferroni 下勉强存活（p=0.0334）。

数据细节：xstorycloze_en 的 cross-arch std 从 pure 的 0.0082 → h3-1 的 0.0055，趋势方向正确但幅度太小，5 个点无法达到统计显著。

输出文件：
- CSV: `/root/entrainment_gated_ft/analysis/xstorycloze_convergence_results.csv`
- JSON: `/root/entrainment_gated_ft/analysis/all_benchmark_convergence_summary.json`

---
