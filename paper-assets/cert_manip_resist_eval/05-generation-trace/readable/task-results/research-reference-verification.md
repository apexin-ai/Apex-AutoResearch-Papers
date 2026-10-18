# research reference verification

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_reference-verification_20260524T033647_result.json`
- **Structured JSON:** [`90bc8a23d6948fb700ff.json`](../../sessions/90/90bc8a23d6948fb700ff.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 篇论文全部验证完毕。

---

### Paper 1: Investigating the Vulnerability of LLM-as-a-Judge Architectures to Prompt-Injection Attacks
- **arXiv ID**: 存在 — [2505.13348](https://arxiv.org/abs/2505.13348)
- **标题**: Investigating the Vulnerability of LLM-as-a-Judge Architectures to Prompt-Injection Attacks
- **作者**: Narek Maloyan, Bislan Ashinov, Dmitry Namiot
- **年份**: 2025 (May 19)
- **Abstract 摘要**: 研究 LLM-as-a-Judge 系统对 prompt injection 攻击的脆弱性，提出两种攻击策略（CUA 和 JMA），使用 GCG 优化生成对抗后缀，在 MT-Bench 上 ASR 超过 30%。
- **与审稿人描述匹配**: **是** — 审稿人描述 "prompt injection on LLM-as-Judge" 完全准确
- **与本项目相关性**: 本项目研究 certification manipulation resistance，该论文展示了 LLM 评估器可被 prompt injection 操纵，是攻击面的直接相关工作
- **状态**: **verified** ✓

---

### Paper 2: TAMAS: Benchmarking Adversarial Risks in Multi-Agent LLM Systems
- **arXiv ID**: 存在 — [2511.05269](https://arxiv.org/abs/2511.05269)
- **标题**: TAMAS: Benchmarking Adversarial Risks in Multi-Agent LLM Systems
- **作者**: Ishan Kavathekar, Hemang Jain, Ameya Rathod, Ponnurangam Kumaraguru, Tanuja Ganu
- **年份**: 2025 (November 7)
- **Abstract 摘要**: 提出多智能体 LLM 系统的对抗风险评估基准，包含 5 个场景、300 个对抗实例、6 种攻击类型，在 10 个 LLM 和 Autogen/CrewAI 框架上评测，引入 Effective Robustness Score (ERS) 指标。
- **与审稿人描述匹配**: **是** — 审稿人描述 "multi-agent adversarial benchmark" 完全准确
- **与本项目相关性**: 作为多智能体系统对抗评估的 benchmark，与本项目的评估框架构成互补/对比关系
- **状态**: **verified** ✓

---

### Paper 3: An Adversary-Resistant Multi-Agent LLM System via Credibility Scoring
- **arXiv ID**: 存在 — [2505.24239](https://arxiv.org/abs/2505.24239)
- **标题**: An Adversary-Resistant Multi-Agent LLM System via Credibility Scoring
- **作者**: Sana Ebrahimi, Mohsen Dehghankar, Abolfazl Asudeh
- **年份**: 2025 (May 30)；已发表于 AACL-IJCNLP 2025 ([ACL Anthology](https://aclanthology.org/2025.ijcnlp-long.90/))
- **Abstract 摘要**: 提出基于 credibility scoring 的对抗鲁棒多智能体 LLM 框架，将协作问答建模为迭代博弈，根据历史贡献学习可信度分数进行输出聚合，即使在对抗方占多数时仍有效。
- **与审稿人描述匹配**: **是** — 审稿人描述 "adversary-resistant multi-agent system" 完全准确
- **与本项目相关性**: 该论文提出的 credibility scoring 防御机制与本项目的 manipulation resistance 评估直接相关，是防御方法的关键 baseline
- **状态**: **verified** ✓

---

**总结**: 3 篇论文全部真实存在，arXiv ID、标题、作者、内容均与审稿人描述一致，无幻觉引用。

Sources:
- [arXiv:2505.13348 - Maloyan et al.](https://arxiv.org/abs/2505.13348)
- [arXiv:2511.05269 - TAMAS](https://arxiv.org/abs/2511.05269)
- [arXiv:2505.24239 - Credibility Scoring](https://arxiv.org/abs/2505.24239)
- [ACL Anthology - Ebrahimi et al.](https://aclanthology.org/2025.ijcnlp-long.90/)

---
