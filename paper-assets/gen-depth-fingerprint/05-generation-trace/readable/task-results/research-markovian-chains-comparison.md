# research markovian chains comparison

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_markovian_chains_comparison_20260521T030007_result.json`
- **Structured JSON:** [`271adc6c7761debfd686.json`](../../sessions/27/271adc6c7761debfd686.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已写入。关键区分点：

| 维度 | Broken Telephone (ACL 2025) | Markovian Chains (arXiv 2026) | Ours |
|---|---|---|---|
| **Chain operator** | 保义改写（back-translation） | 保义改写（rephrasing + translation） | 开放续写（无语义保持约束） |
| **分析视角** | 事实准确性衰减速率 | 收敛行为 / 循环态 | 深度分类 + DDR分解 |
| **互补性** | 关注"丢了什么信息" | 关注"稳态长什么样" | 关注"统计指纹如何随深度变化" |

三篇出自两个独立团队（Broken Telephone 和 Markovian Chains 共享作者），研究同一现象的不同侧面。我们的 continuation chain 设定与它们的 meaning-preserving chain 形成方法论互补——它们固定语义观察形式漂移，我们固定形式（续写 prompt）观察语义统计漂移。

`\citet` 引用键 `mohamed2025broken` 和 `geng2026markovian` 需要在 `.bib` 中补充对应条目。

---
