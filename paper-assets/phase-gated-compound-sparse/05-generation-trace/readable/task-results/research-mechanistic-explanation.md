# research mechanistic explanation

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_mechanistic-explanation_20260514T024934_result.json`
- **Structured JSON:** [`afb8abc1746c872d0088.json`](../../sessions/af/afb8abc1746c872d0088.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已写入 `artifacts/mechanistic_explanation.md`。核心结构：

**四段机制叙事，可直接用于 Discussion：**

1. **Entropy–Discrimination Collapse** — head pruning 使存活 head 的 attention 分布变均匀（高 entropy），importance score 区分度崩溃，退化为带系统偏差的伪随机，比真 random 更差。低 sparsity phase 天然 attention 更分散，所以 compound penalty 集中在此。

2. **Gradient Amplification** — 解释为什么 gradient 随 s 增大（12.8× → 52.9×）：更高 sparsity 意味着更多 head 被剪，存活 head 负荷更重，low-phase entropy 被推得更远过阈值。类比 Ma et al. (npj AI 2026) 的 phase transition point 理论——low phase 在 compound 下更接近 PTP。

3. **Super-Additivity 的循环依赖** — head pruning 改变了 eviction 赖以打分的 attention pattern，eviction 又移除了存活 head 需要的 context token。SLiM (ICML'25) 正式证明 compound error 非加性。

4. **Random Baseline 预测** — random 也应 super-additive（循环依赖仍在），但 gradient 更小（无 discrimination collapse）。若实验确认，则证明 gradient 来自 importance metric failure 而非架构脆弱性，直接支撑 phase-gated strategy switching 的价值。

**每个 claim 已标注 [MEASURED] / [LITERATURE] / [HYPOTHESIS]，15 篇文献对照表附在末尾。**

---
