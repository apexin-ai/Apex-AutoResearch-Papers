# research r5 citation verification

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_r5-citation-verification_20260520T090806_result.json`
- **Structured JSON:** [`27e65ca1b1d8ce5fae67.json`](../../sessions/27/27e65ca1b1d8ce5fae67.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

10 篇全部核实完毕。以下是结果：

---

## 1. JBShield
- **存在性**: Y
- **arXiv ID**: 2502.07557
- **完整标题**: JBShield: Defending Large Language Models from Jailbreak Attacks through Activated Concept Analysis and Manipulation
- **Venue**: USENIX Security 2025
- **与本文相关性**: 高 — 直接竞品，做 representation-level jailbreak detection（concept-activation vectors），F1=0.94
- **建议引用**: 是 — 最直接的 representation-level detection baseline

## 2. Latent Adversarial Detection
- **存在性**: Y
- **arXiv ID**: 2604.28129
- **完整标题**: Latent Adversarial Detection: Adaptive Probing of LLM Activations for Multi-Turn Attack Detection
- **Venue**: arXiv preprint (April 2026)
- **与本文相关性**: 高 — 同样做多轮攻击的 activation-level 检测，提出"adversarial restlessness"轨迹特征，conversation-level detection 93.8%
- **建议引用**: 是 — 与我们工作高度对标的并行工作（concurrent work）

## 3. How Do LLMs Persuade?
- **存在性**: Y
- **arXiv ID**: 2508.05625
- **完整标题**: How Do LLMs Persuade? Linear Probes Can Uncover Persuasion Dynamics in Multi-Turn Conversations
- **Venue**: arXiv preprint (Aug 2025)
- **与本文相关性**: 高 — 用 linear probes 研究多轮对话说服动态，直接支撑我们的理论基础
- **建议引用**: 已引用 — 已在 paper_framing.md、literature_map.yaml、paper.tex 中引用（bibkey: `howdollms2025`）

## 4. Guarding the Guardrails
- **存在性**: Y
- **arXiv ID**: 2510.13893
- **完整标题**: Guarding the Guardrails: A Taxonomy-Driven Approach to Jailbreak Detection
- **Venue**: arXiv preprint (Oct 2025, revised Feb 2026)
- **与本文相关性**: 中 — 提出 jailbreak 策略分类法（含 persuasion 类别）和意大利语多轮数据集，分类视角有参考价值
- **建议引用**: 是 — 其 taxonomy 中 persuasion 作为独立 jailbreak family 的分类与我们工作互补

## 5. Computational Persuasion Survey
- **存在性**: Y
- **arXiv ID**: 2505.07775
- **完整标题**: Must Read: A Comprehensive Survey of Computational Persuasion
- **Venue**: arXiv preprint (May 2025)
- **与本文相关性**: 中 — 150+ 篇论文的 computational persuasion 综述，覆盖 AI as Persuader/Persuadee/Judge，可作为 persuasion 背景引用
- **建议引用**: 是 — 适合 Related Work 中定位 persuasion 研究背景

## 6. Active Honeypot Guardrail System
- **存在性**: Y
- **arXiv ID**: 2510.15017
- **完整标题**: Active Honeypot Guardrail System: Probing and Confirming Multi-Turn LLM Jailbreaks
- **Venue**: arXiv preprint (Oct 2025)
- **与本文相关性**: 中 — 多轮 jailbreak 的主动防御（honeypot bait），与我们的被动检测互补
- **建议引用**: 是 — Related Work 中展示多轮 jailbreak 防御的不同范式

## 7. Revisiting JBShield
- **存在性**: Y
- **arXiv ID**: 2605.03095
- **完整标题**: Revisiting JBShield: Breaking and Rebuilding Representation-Level Jailbreak Defenses
- **Venue**: arXiv preprint (May 2026)
- **与本文相关性**: 高 — 对 JBShield 的攻击性评估，JB-GCG 将 JBShield-D 的 ASR 从 0% 打到 46.2%，说明 representation-level defense 仍有脆弱性
- **建议引用**: 是 — 与 #1 配合引用，展示 representation-level detection 的攻防态势

## 8. Detecting Language Model Attacks with Perplexity
- **存在性**: Y
- **arXiv ID**: 2308.14132
- **完整标题**: Detecting Language Model Attacks with Perplexity
- **Venue**: arXiv preprint (Aug 2023)；也见 OpenReview
- **与本文相关性**: 中 — 用 perplexity 检测 adversarial suffix 攻击，属于经典的 detection baseline
- **建议引用**: 是 — Related Work 中作为 perplexity-based detection baseline

## 9. Red Teaming Language Models with Language Models
- **存在性**: Y
- **arXiv ID**: 2202.03286
- **完整标题**: Red Teaming Language Models with Language Models
- **Venue**: EMNLP 2022
- **与本文相关性**: 中 — 用 LM 自动化 red teaming 的开创性工作，与我们检测端不直接对标但属于必要背景
- **建议引用**: 是 — 经典引用，红队攻击生成的标准参考

## 10. A StrongREJECT for Empty Jailbreaks
- **存在性**: Y
- **arXiv ID**: 2402.10260
- **完整标题**: A StrongREJECT for Empty Jailbreaks
- **Venue**: NeurIPS 2024 (Datasets and Benchmarks Track)
- **与本文相关性**: 中 — jailbreak 评估标准化 benchmark（313 forbidden prompts），ASR 评估方法论参考
- **建议引用**: 是 — 如果讨论 jailbreak 评估方法论或 ASR 度量标准

---

## 总结

| # | 名称 | 存在 | arXiv ID | Venue | 相关性 | 建议 |
|---|------|------|----------|-------|--------|------|
| 1 | JBShield | Y | 2502.07557 | USENIX Sec'25 | **高** | 引用 |
| 2 | Latent Adversarial Detection | Y | 2604.28129 | preprint'26 | **高** | 引用(concurrent) |
| 3 | How Do LLMs Persuade? | Y | 2508.05625 | preprint'25 | **高** | **已引用** |
| 4 | Guarding the Guardrails | Y | 2510.13893 | preprint'25 | 中 | 引用 |
| 5 | Computational Persuasion Survey | Y | 2505.07775 | preprint'25 | 中 | 引用 |
| 6 | Active Honeypot Guardrail | Y | 2510.15017 | preprint'25 | 中 | 引用 |
| 7 | Revisiting JBShield | Y | 2605.03095 | preprint'26 | **高** | 引用 |
| 8 | Perplexity Detection | Y | 2308.14132 | preprint'23 | 中 | 引用 |
| 9 | Red Teaming with LMs | Y | 2202.03286 | EMNLP'22 | 中 | 引用 |
| 10 | StrongREJECT | Y | 2402.10260 | NeurIPS'24 | 中 | 引用 |

**10/10 全部真实存在。** 关键发现：
- **#1 + #7 构成直接竞品线**：JBShield 做 representation-level detection（USENIX Sec'25），Revisiting JBShield 已证明其脆弱性（ASR 46.2%）。我们应在论文中讨论这一攻防态势，突出我们方法（turn-level sequence classification）的互补优势。
- **#2 是最重要的 concurrent work**：同样做多轮攻击的 activation-level 检测，但依赖模型内部表示（24B-70B），我们的 DeBERTa + BiGRU 方案更轻量且模型无关。
- **#3 已引用**，无需额外操作。

Sources:
- [JBShield](https://arxiv.org/abs/2502.07557)
- [Latent Adversarial Detection](https://arxiv.org/abs/2604.28129)
- [How Do LLMs Persuade?](https://arxiv.org/abs/2508.05625)
- [Guarding the Guardrails](https://arxiv.org/abs/2510.13893)
- [Computational Persuasion Survey](https://arxiv.org/abs/2505.07775)
- [Active Honeypot Guardrail](https://arxiv.org/abs/2510.15017)
- [Revisiting JBShield](https://arxiv.org/abs/2605.03095)
- [Detecting LM Attacks with Perplexity](https://arxiv.org/abs/2308.14132)
- [Red Teaming LMs with LMs](https://arxiv.org/abs/2202.03286)
- [StrongREJECT](https://arxiv.org/abs/2402.10260)

---
