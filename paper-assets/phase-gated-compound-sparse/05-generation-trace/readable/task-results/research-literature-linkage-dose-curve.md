# research literature linkage dose curve

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_literature-linkage-dose-curve_20260516T041915_result.json`
- **Structured JSON:** [`ded19c19e25ffd8f68cc.json`](../../sessions/de/ded19c19e25ffd8f68cc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。

**直接可比的 accuracy dose-response 数据：无。** 文献 map 中的 direct-competitor 论文（SparK、GRASPrune、DefensiveKV）均不报告 15-30% sparsity range 下 MATH-500 的 accuracy dose curve。SparK 关注 compound degradation 但未报告逐级 accuracy；MUSTAFAR 在 70% sparsity 下报告"无损"但范围不同；R-KV 在 90% reduction 下评估推理模型但机制不同（token selection vs compound channel sparsity）。

**缺失项识别：**
- Map 缺少经典 KV cache eviction 论文的 accuracy baseline（H2O、SnapKV、ScissorHands），这些论文有 accuracy vs budget 曲线但 sparsity 类型不同（token eviction vs channel pruning），且未在 reasoning model 上评估
- 缺少 **KIVI**（KV quantization accuracy curve）和 **Quest**（query-aware token sparsity），两者都有多点 accuracy 数据
- 但上述缺失与本项目关系有限——我们的 sparsity 机制是 compound channel pruning，与 token eviction 不在同一维度

**结论：不需要补充文献搜索。** Map 中无论文提供可直接对比的 accuracy dose-response 数据点（相同模型、相同 sparsity 类型、相同 benchmark）。这反而支撑了本工作的 novelty——首次系统报告 compound channel sparsity 在 reasoning task 上的 accuracy dose curve。经典 KV eviction 论文（H2O/SnapKV）可在 Related Work 中作为 context 引用，但不构成 direct comparison。

无重要缺失项需写入 memory.md，不追加。

---
