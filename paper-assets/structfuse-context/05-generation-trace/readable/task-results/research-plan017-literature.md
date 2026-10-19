# research plan017 literature

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_plan017_literature_20260514T092026_result.json`
- **Structured JSON:** [`e76875a3197f904e28f5.json`](../../sessions/e7/e76875a3197f904e28f5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文档已写入 `artifacts/analysis/plan017_literature_comparison.md`。

核心结论：

1. **方法论差异**：StructFuse 将图信息"蒸馏"到模型参数中（training-time negative mining），inference-time 方法（CodexGraph/LocAgent/RANGER 等）在每次查询时显式遍历图。StructFuse 是唯一使用 **inter-procedural** data-flow 的方法——其他方法最多到 intra-procedural（GraphCoder、ARISE）。

2. **计算开销**：StructFuse 的 CodeQL 提取成本是一次性的（~110h for 44K instances），推理零额外开销。Inference-time 方法的成本随查询量线性增长（每次查询需图遍历 + LLM 调用），RANGER 的 MCTS 最重。

3. **互补性**：两种范式正交可组合——StructFuse 训练的 encoder 可作为高效 first-stage retriever，缩小 inference-time graph agent 的搜索空间。这是一个自然的 future work 方向。

4. **Reviewer 应对**：核心策略是"不同范式 + 不同任务接口 → 直接对比不恰当"，同时将组合使用框架为建设性的 future work。

---
