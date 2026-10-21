# analysis per generator silhouette

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_per_generator_silhouette_20260521T075851_result.json`
- **Structured JSON:** [`44214d6540a5d24f9c35.json`](../../sessions/44/44214d6540a5d24f9c35.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

- **8/8 generator 分区完全一致**：全部恢复 {entropy_mean, ttr, hapax_ratio} vs {entropy_std, entropy_max, entropy_min, tail_decay}
- **Silhouette 范围**：0.505 (Pythia-1B) ~ 0.760 (Mistral-7B-v0.3)，均值 0.651，全部 ≥ 0.5
- **结论**：pooled silhouette=0.660 不是 pooling artifact，每个 generator 独立复现相同分区

结果已保存到 `per_generator_silhouette.txt`，LaTeX 段落已插入 `appendix_ddr_validation.tex` 的 exhaustive enumeration 之后。

---
