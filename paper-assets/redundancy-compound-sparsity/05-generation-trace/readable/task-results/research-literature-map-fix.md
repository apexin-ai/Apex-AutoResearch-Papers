# research literature map fix

**When Does KV Redundancy Predict MLP Sparsity? Architecture Dependence of Cross-Axis Signals in Reasoning Inference** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_literature-map-fix_20260511T225754_result.json`
- **Structured JSON:** [`3a511d35a851d19de8bb.json`](../../sessions/3a/3a511d35a851d19de8bb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。新增 11 篇论文：

**第一批（MVP 必补，已详细描述 relation_to_carc）：**
- **Token Filtering** (arXiv:2512.07090) → `redundancy-signal`，标注为 CARC EMA KV similarity 信号的直接前驱
- **CLADA** (arXiv:2502.19078) → `activation-sparsity`，标注为 "surprisal → MLP sparsity" 假设的文献支撑

**第二批（Research 阶段，core_method 标注 needs verification）：**
- **R-KV**, **LazyEviction**, **LongFlow** → `kv-eviction`
- **Polar Sparsity**, **WiSparse** → `activation-sparsity`
- **TriAttention**, **FASA** → `cross-axis`
- **Q-Infer** → `direct-competitor`
- **EMA Is Not All You Need** → `redundancy-signal`

所有新增条目均标注 `verified: false`，第二批论文的 authors/venue/core_method 均标注 needs verification。

---
