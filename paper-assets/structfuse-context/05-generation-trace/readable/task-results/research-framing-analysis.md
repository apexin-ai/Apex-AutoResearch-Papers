# research framing analysis

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_framing_analysis_20260513T184429_result.json`
- **Structured JSON:** [`e6f0682bbbb42aa1c13b.json`](../../sessions/e6/e6f0682bbbb42aa1c13b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## Paper Framing 分析

### 1. 论文价值排序

按重要性：

1. **embedding > random 跨编码器一致**（Qwen +2.0pp, StarCoder +1.6pp）— 最稳健信号，两个编码器方向一致，是任何 framing 下都可用的核心结果。
2. **M1 全量 Z%=78.0%**（条件）— 证明 CodeQL 结构信号在大规模下有效分离 connected-but-not-gold，支撑 Claim 3（scalability）且是 Claim 1 的前提。
3. **MVP P2b embedding harm（-27pp）**— 戏剧性强但有 confound：BM25 proxy ≠ true embedding mining（D017）。价值在于引出"mining method matters"的叙事，但不能直接作为 Claim 2。
4. **P1 CodeQL feasibility**（timeout 0→4%）+ **P2a AUC=0.78** — 基础设施贡献，支撑 Claim 3。
5. **dataflow pilot 结果** — 方向不一致（Qwen +0.8pp, StarCoder -0.5pp），checkpoint 依赖高，当前价值最低，需 full M2 定论。

两个 negative（plan_013_starcoder dataflow 负向、MVP embedding harm 在 true mining 下不复现）反而有高叙事价值——前者引出 architecture interaction discussion，后者揭示 proxy vs true mining 的差异。

### 2. Conditional Go 叙事方向

如果 full M2 确认 embedding > random 跨编码器一致，但 dataflow 不稳定：

**Title**: "Hard Negative Mining for Code Retrieval: When Embedding Distance Helps and Structure Falls Short"

**Headline Claim**: "True embedding-distance hard negatives consistently improve contrastive code retrieval across encoder architectures, while structure-grounded negatives show architecture-dependent effects."

**Story spine 调整**:
- Problem 不变：repo-level retrieval 需要更好的 negative mining
- Gap 重构：从 "structure > embedding > random" 变为 "negative mining strategy 的选择对检索质量影响显著，但最优策略取决于信号来源"
- 核心贡献变为：(1) 首次系统比较三种 negative mining 策略在 code retrieval 的效果；(2) 发现 true embedding mining 稳健有效（对比 MVP 的 BM25 proxy 有害）；(3) 结构信号有潜力但受 encoder architecture 调制，需进一步研究
- Discussion 收尾：structure-grounded negatives 不是银弹，但 CodeQL pipeline 作为可复用基础设施的贡献独立成立

实质上从 "structure wins" 论文变为 "mining strategy comparison" 论文，venue 目标降为 Findings。

### 3. Cross-encoder Consistency 作为独立贡献

embedding > random 跨编码器一致（+2pp / +1.6pp）**不足以作为 EMNLP Main 的独立贡献**。原因：

- **效应量小**：<2pp 在 n=3 seeds 下统计显著性存疑（D020 明确指出 df=2 时 t 临界值 4.303）
- **不够新颖**：hard negative mining 改善对比学习是已知结论（CoCoHaNeRe 等），cross-encoder consistency 是 robustness check 而非 novelty
- **竞争力**：EMNLP Main 期望方法级创新或大规模 empirical insight，单纯 "+2pp cross-encoder" 更适合 workshop/short paper

但作为论文中的 **supporting evidence** 价值很高——它将 "mining method matters" 从单编码器观察升级为方法论层面的结论，是 Conditional Go framing 的骨架。

---
