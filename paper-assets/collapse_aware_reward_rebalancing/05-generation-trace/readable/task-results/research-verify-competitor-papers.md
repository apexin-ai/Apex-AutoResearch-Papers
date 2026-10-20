# research verify competitor papers

**Does Reward Curation Kill Diversity? Systematic Evidence of Surprising Resilience in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_verify_competitor_papers_20260517T012158_result.json`
- **Structured JSON:** [`618e03800457856920ed.json`](../../sessions/61/618e03800457856920ed.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 5 篇论文验证完毕，结果如下：

---

## 验证结果

### 1. DIVE: Diversified Iterative Self-Improvement — arXiv 2501.00747
**✅ 真实**

- 实际标题：*DIVE: Diversified Iterative Self-Improvement*（完全匹配）
- 作者：Yiwei Qin, Yixiu Liu, Pengfei Liu
- 日期：2025年1月
- Venue：也见于 OpenReview
- 相关性：直接竞品——解决迭代自改进中多样性丧失问题，通过 Sample Pool Expansion + Data Selection 平衡多样性与质量

### 2. DARLING: Jointly Reinforcing Diversity and Quality — arXiv 2509.02534
**✅ 真实**

- 实际标题：*Jointly Reinforcing Diversity and Quality in Language Model Generations*（DARLING = Diversity-Aware Reinforcement Learning）
- 来源：Facebook Research（有官方 GitHub: facebookresearch/darling）
- 日期：2025年9月（当前2026年5月，时间合理）
- 相关性：**最直接的竞品**——在 online RL 阶段联合优化质量和语义多样性，用 learned partition function 度量多样性

### 3. CD-RLHF: Curiosity-Driven RLHF — arXiv 2501.11463
**✅ 真实**

- 实际标题：*Curiosity-Driven Reinforcement Learning from Human Feedback*（完全匹配）
- 来源：Ernie Research (Baidu)，有官方 GitHub: ernie-research/CD-RLHF
- 日期：2025年1月
- 相关性：直接竞品——用 intrinsic curiosity reward 在 RLHF 中保持多样性，同时维持对齐质量

### 4. GEM: Preserving Diversity in Supervised Fine-Tuning — arXiv 2408.16673
**⚠️ 真实，但标题表述略有出入**

- 实际标题 v2：*Preserving Diversity in Supervised Fine-Tuning of Large Language Models*
- 实际标题 v1：*Entropic Distribution Matching in Supervised Fine-tuning of LLMs: Less Overfitting and Better Diversity*
- GEM 是算法名称，非论文标题的一部分
- 有官方 GitHub: liziniu/GEM
- 日期：2024年8月
- 相关性：高度相关——game-theoretic formulation 用 reverse KL + entropy regularization 在 SFT 阶段保留多样性

### 5. Kirk et al.: Understanding Effects of RLHF on Diversity — arXiv 2310.06452
**✅ 真实**

- 实际标题：*Understanding the Effects of RLHF on LLM Generalisation and Diversity*（完全匹配）
- 作者：Robert Kirk, Ishita Mediratta, Christoforos Nalmpantis, Jelena Luketina, Eric Hambro, Edward Grefenstette, Roberta Raileanu
- 日期：2023年10月，发表于 ICLR（见 OpenReview）
- 相关性：基础性分析论文——实证发现 RLHF 显著降低输出多样性，建立了 generalisation vs. diversity 的 tradeoff，是我们工作的动机来源之一

---

## 总结

5/5 论文均真实存在，无幻觉。仅 GEM 的标题表述需微调（GEM 是算法名而非论文标题的一部分）。DARLING 的 2509 时间戳确认合理（2025年9月，Facebook Research 出品）。

Sources:
- [DIVE](https://arxiv.org/abs/2501.00747)
- [DARLING](https://arxiv.org/abs/2509.02534)
- [CD-RLHF](https://arxiv.org/abs/2501.11463)
- [GEM](https://arxiv.org/abs/2408.16673)
- [Kirk et al.](https://arxiv.org/abs/2310.06452)

---
