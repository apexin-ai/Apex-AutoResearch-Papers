# research pruning rl stability literature

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_pruning-rl-stability-literature_20260515T185938_result.json`
- **Structured JSON:** [`03b61ceb68557ed6ab8a.json`](../../sessions/03/03b61ceb68557ed6ab8a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已保存至 `memory.md`。以下是核心结论：

---

## 搜索结果总结

### 1. 是否有直接先例（pruning → RL collapse）

**没有。** 这是文献空白。现有工作分布在两个不相交的方向：
- GRPO/RL 本身的 instability 研究（GSPO, DVP）—— 不涉及 pruning
- Pruning → recovery 研究 —— 只考察 SFT/perplexity，不涉及后续 RL 阶段
- Sparsity helps RL 研究（ICML 2024/2025）—— 方向相反，发现 sparsity **有利于** RL

**"structured pruning → GRPO collapse，且不同 pruning strategy 有不同 RL stability"在文献中完全没有。**

### 2. "Pruning for Plasticity" Framing 新颖性

**中高。** "Pruning plasticity"术语已存在（NeurIPS 2021），"sparsity → plasticity in RL"有扎实支撑（ICML 2024/2025）。但组合为 **"pruning strategy determines LLM's RL plasticity"** 是新的，特别是 RASP vs Standard 的差异行为。

### 3. Top 3 推荐引用

| # | 论文 | 理由 |
|---|------|------|
| 1 | **Obando-Ceron et al. (ICML 2024)** "In value-based deep RL, a pruned network is a good network" | 建立 pruning → plasticity → RL 因果链 |
| 2 | **Ma et al. (ICML 2025 Oral)** "Network Sparsity Unlocks the Scaling Potential of Deep RL" | sparsity helps RL 的最强证据；我们补充 nuance |
| 3 | **Zheng et al. (2025)** "GSPO" | 解释 GRPO collapse 算法根因；我们 show pruned models 更 susceptible |

共发现 14 篇相关论文，详细分析已保存。最关键的 insight：现有文献一致发现 sparsity **有利于** RL plasticity，但没有人区分过 pruning **strategy** 的影响 —— 这正是 RASP 的贡献空间。

---
