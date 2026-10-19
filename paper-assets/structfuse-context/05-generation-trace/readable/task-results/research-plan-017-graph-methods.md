# research plan 017 graph methods

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_plan_017_graph_methods_20260513T212612_result.json`
- **Structured JSON:** [`4de6a46c4883cbf2748b.json`](../../sessions/4d/4de6a46c4883cbf2748b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。产出已保存到项目 `memory.md`，包含：

**1. 对比表** — 覆盖 8 个方法 + StructFuse，对比维度包括 graph type、usage stage、inter-proc data-flow support、task、scalability、key difference。

**2. Discussion 要点（5 点）**：
- Cost-accuracy tradeoff：StructFuse 零推理开销 vs 其他方法每次查询都要建图/遍历
- Data-flow depth：其他方法最多 intra-procedural，StructFuse 是唯一做 inter-procedural 的
- Complementarity：StructFuse encoder 可作为 inference-time 方法的 embedding backbone
- Scalability model：前置一次性投入 vs 随 QPS 线性增长
- Task generality：轻量 first-stage retriever vs 依赖 LLM 的 task-agnostic agent

**3. Related Work 段落** — ~200 words，定位 StructFuse 在 graph-based code understanding 中的独特位置（training-time + inter-procedural + zero inference cost）。

核心发现：ARISE 和 GraphCoder 是最接近 StructFuse 的工作（都用了 data/control flow），但它们都局限于 intra-procedural 且在 inference-time 使用图。这是 StructFuse 的两个关键区分点。

---
