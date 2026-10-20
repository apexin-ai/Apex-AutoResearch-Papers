# analysis review p1c instruct

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_review-p1c-instruct_20260515T152812_result.json`
- **Structured JSON:** [`52a88c90805a6d3a9e64.json`](../../sessions/52/52a88c90805a6d3a9e64.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

---

## 总结

**review-p1c-instruct 实验完成，结论：success（有强 depth signal，方向相反）。**

关键发现：
1. **Instruct 模型有极显著的 depth signal**（所有 7 个特征 p < 1e-38），证实 instruction tuning 不会消除深度响应
2. **方向完全反转**：base model 多样性随深度递减（坍缩），instruct model 多样性随深度递增（发散），三个核心 drift 特征 Δρ 均超过 +1.0
3. **形式 DDR = false**：因为 shape 特征（entropy_std, tail_decay）也在漂移（|ρ| = 0.30, 0.18），不满足"shape 稳态"条件
4. **无分类器 F1**：analyze_instruct.py 仅做相关性分析，未训练分类器。如需与 base model binary F1=0.723 直接对比，需额外跑分类评估

对论文的意义：instruction tuning 从根本上改变了递归生成的深度响应特性——不是消除了 depth fingerprint，而是翻转了它。这是比简单的"有/无"更有故事性的结果。

---
