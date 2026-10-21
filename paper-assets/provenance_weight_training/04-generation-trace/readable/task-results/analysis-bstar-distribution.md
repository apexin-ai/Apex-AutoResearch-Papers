# analysis bstar distribution

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bstar-distribution_20260514T234358_result.json`
- **Structured JSON:** [`979587c429a7e54a24ed.json`](../../sessions/97/979587c429a7e54a24ed.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心发现：

1. **之前 registry 的聚合统计有误导** — mean=0.71/median=0 是因为混入了 checkpoint 评估步的 8400+ 条 b*=0 记录。排除后真实训练 b* 的 mean=1.42, median=0.88。

2. **分布特征**: 强右偏、重尾。55% batch 在温和区间 (b*∈[0,1])，40% 在中强区间 (1-5)，3.6% 被激进降权 (>5)。

3. **完全稳定**: 训练全程无漂移（b* 只依赖 batch 的 q_score 分布），三 seed 间 CV<2%。

4. **b*=0 仅占 1.8%**: 只在 mean_q≤0.2 的干净 batch 触发（理论精确阈值 1−τ=0.2），意味着 98% 的 batch 都接受了非零降权。

5. **论文启示**: 高 b* 不对应"更脏"的 batch，而是"污染更均匀分散"的 batch — 这种非单调关系值得在论文中讨论。

报告已注册到 artifacts (art_20260514_ac7785)。

---
