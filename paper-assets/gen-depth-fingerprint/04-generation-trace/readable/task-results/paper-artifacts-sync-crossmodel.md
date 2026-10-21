# paper artifacts sync crossmodel

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_artifacts-sync-crossmodel_20260515T225301_result.json`
- **Structured JSON:** [`8270bb41debf73005227.json`](../../sessions/82/8270bb41debf73005227.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个任务全部完成：

**任务 1 — artifacts ← docs 同步**：conclusion.tex、results.tex、discussion.tex、limitations.tex 已从 docs/paper/ 覆盖到 artifacts/_project/paper/。

**任务 2 — 评估协议修正**：`docs/paper/results.tex:28` 中 cross-model chains 段落的 "LOGO cross-validation" 已改为 **"5-fold stratified cross-validation"**（同步到 artifacts 的副本也包含此修正）。

**任务 3 — conclusion.tex 更新**：
- artifacts 旧版将 "mixed-generator chains" 列为 future work → 已删除
- 新增已完成结论句：`Cross-model chains---where each generation step uses a different generator---yield comparable performance (3-class F1=0.809, binary F1=0.764), confirming that depth signal persists under the generator heterogeneity typical of real-world contamination.`
- future work 仅保留 instruct/RLHF、70B+、multilingual 三项

---
