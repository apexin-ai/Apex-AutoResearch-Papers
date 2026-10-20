# analysis feature importance kendall

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_feature-importance-kendall_20260517T231929_result.json`
- **Structured JSON:** [`0a5a63de01c81f8e8945.json`](../../sessions/0a/0a5a63de01c81f8e8945.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果：

**Kendall W = 0.9632** (p = 2.66e-08), feature importance 在 8 个 LOGO fold 之间极其稳定。

关键发现：
- `hapax_ratio` 在全部 8 个 fold 中均排名 #1
- `entropy_mean` 和 `ttr` 稳定占据 #2-3（偶有交换）
- `entropy_min` 和 `tail_decay` 固定在最后两位

输出已保存：
- 服务器: `results/feature_importance_stability.json`
- 本地 artifact: `artifacts/_project/analysis/feature_importance_stability.md`

---
