# paper research rl alignment

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_research_rl_alignment_20260517T154253_result.json`
- **Structured JSON:** [`1644b58658bb5425bc15.json`](../../sessions/16/1644b58658bb5425bc15.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 8 篇论文验证完成。以下是结果：

---

## Must-cite 论文（3篇）

## [GRPO / DeepSeekMath]
- title: DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models
- authors: Shao et al. (Zhihong Shao)
- venue: arXiv preprint (2024)
- year: 2024
- arxiv: 2402.03300
- doi: —
- bibtex_key: shao2024deepseekmath
- verified: true
- relevance: 提出 GRPO 算法，本论文直接使用 GRPO 训练 DocRE 模型
- verification_note: 确认 GRPO 在此论文中首次提出，作为 PPO 的变体用于数学推理。title/authors/arXiv ID 均与预期一致。

## [DPO]
- title: Direct Preference Optimization: Your Language Model is Secretly a Reward Model
- authors: Rafailov et al. (Rafael Rafailov, Archit Sharma, Eric Mitchell, Stefano Ermon, Christopher D. Manning, Chelsea Finn)
- venue: NeurIPS 2023
- year: 2023
- arxiv: 2305.18290
- doi: 10.5555/3666122.3668460
- bibtex_key: rafailov2023dpo
- verified: true
- relevance: 本论文使用 DPO 作为对比方法训练 DocRE 模型，发现渐进退化现象
- verification_note: 确认 NeurIPS 2023（非 2024）。arXiv ID 2305.18290。

## [Gao et al. 2023 — Reward Overoptimization]
- title: Scaling Laws for Reward Model Overoptimization
- authors: Gao et al. (Leo Gao, John Schulman, Jacob Hilton)
- venue: ICML 2023
- year: 2023
- arxiv: 2210.10760
- doi: 10.5555/3618408.3618845
- bibtex_key: gao2023scaling
- verified: true
- relevance: 本论文发现 GRPO QLoRA catastrophic decoupling 与 reward hacking 相关，此文提供 reward overoptimization 理论基础
- verification_note: 确认 ICML 2023 (40th ICML)。arXiv 提交于 2022-10，发表于 2023。

---

## Gap-fill 论文（5篇）

## [Adjali et al. 2026 — GRPO for Event Extraction]
- title: Aligning Instruction-Tuned LLMs for Event Extraction with Multi-objective Reinforcement Learning
- authors: Adjali et al. (O. Adjali, S. Liang, O.S. Bhatti, D. Sonntag)
- venue: ECIR 2026 (Advances in Information Retrieval)
- year: 2026
- arxiv: —（无 arXiv 预印本）
- doi: 10.1007/978-3-032-21300-6_50
- bibtex_key: adjali2026aligning
- verified: true
- relevance: 直接使用 GRPO + 多目标 reward（format/BM25/task-specific）做 IE 任务，与本论文方法高度相似
- verification_note: 仅在 Springer 发表，无 arXiv 版本。ECIR 2026 确认。

## [R1-RE — RLVR for Relation Extraction]
- title: R1-RE: Cross-Domain Relation Extraction with RLVR
- authors: Dai et al. (Runpeng Dai, Tong Zheng, Run Yang, Kaixian Yu, Hongtu Zhu)
- venue: arXiv preprint (2025)
- year: 2025
- arxiv: 2507.04642
- doi: —
- bibtex_key: dai2025r1re
- verified: true
- relevance: 首个将 RLVR 用于关系抽取的工作，证明 RL 可提升 RE 跨域泛化能力，与本论文 GRPO-for-DocRE 直接可比
- verification_note: arXiv 2025-07-07。标题中 "Relation Extraction" 有时显示为 "Relationship Extraction"，同一论文。

## [Jin et al. 2025 — RL vs SFT Analysis]
- title: RL Is Neither a Panacea Nor a Mirage: Understanding Supervised vs. Reinforcement Learning Fine-Tuning for LLMs
- authors: Jin et al. (Hangzhan Jin, Sicheng Lv, Sifan Wu, Mohammad Hamdaqa)
- venue: arXiv preprint (2025)
- year: 2025
- arxiv: 2508.16546
- doi: —
- bibtex_key: jin2025rl_panacea
- verified: true
- relevance: 分析 SFT→RL 时表征变化与 OOD 性能，为本论文 catastrophic decoupling 分析提供理论支撑（SFT 严重过拟合时 RL 无法完全恢复）
- verification_note: Polytechnique Montreal / Mila。2025-08-22 提交。

## [E-GRPO — Entity-Aware Rewards in GRPO]
- title: Repurposing Synthetic Data for Fine-grained Search Agent Supervision
- authors: Zhao et al. (Yida Zhao, Kuan Li, Xixi Wu, Liwen Zhang, et al.)
- venue: arXiv preprint (2025)
- year: 2025
- arxiv: 2510.24694
- doi: —
- bibtex_key: zhao2025egrpo
- verified: true
- relevance: 提出 E-GRPO（entity-aware dense reward in GRPO），用实体匹配作为细粒度 reward，与本论文 evidence-level reward 设计思路一致
- verification_note: 论文主题为搜索代理，但核心贡献 E-GRPO 的 entity-aware reward 机制对本论文有直接参考价值。阿里巴巴团队。

## [Moskovitz et al. 2024 — Constrained RLHF]
- title: Confronting Reward Model Overoptimization with Constrained RLHF
- authors: Moskovitz et al. (Ted Moskovitz, Aaditya Singh, DJ Strouse, Tuomas Sandholm, Ruslan Salakhutdinov, Anca Dragan, Stephen McAleer)
- venue: ICLR 2024
- year: 2024
- arxiv: 2310.04373
- doi: —
- bibtex_key: moskovitz2024constrained
- verified: true
- relevance: 研究 composite RM 的 overoptimization 及约束方法，为本论文多维度 reward (faithfulness + evidence + format) 的平衡问题提供理论支撑
- verification_note: 确认 ICLR 2024 poster。OpenReview ID: gkfUvn0fLU。

---

**总结**: 8/8 全部验证通过。3 篇 must-cite 信息与预期一致（DPO 是 NeurIPS 2023 非 2024）。5 篇 gap-fill 覆盖了 GRPO-for-IE (Adjali, R1-RE)、RL 理论分析 (Jin)、entity-aware reward (E-GRPO)、multi-objective reward hacking (Moskovitz) 四个维度。

---
