# analysis threshold sweep

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_threshold_sweep_20260521T062444_result.json`
- **Structured JSON:** [`1f90aa500727281b8baf.json`](../../sessions/1f/1f90aa500727281b8baf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个文件已保存：

- **结果表**: `artifacts/_project/analysis/threshold_sweep_results.txt`
- **附录段落**: `artifacts/_project/analysis/threshold_sweep_paragraph.tex`

核心发现：整个 [0.10, 0.80] 范围内只存在 3 个不同的 partition，说明分组是自然聚类而非阈值选择的产物。论文使用的 3-drifting partition 对应 peak silhouette = 0.6603，在 |d| ∈ [0.50, 0.75] 范围内完全稳定。唯一会切换分组的 feature 是 entropy_std (d=0.4914)，它两侧分别有 0.40 和 0.29 的 gap，所以无论哪种 partition 都是稳健的。

---
