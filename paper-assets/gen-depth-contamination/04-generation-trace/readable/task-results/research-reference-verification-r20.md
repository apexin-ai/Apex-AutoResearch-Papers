# research reference verification r20

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_reference_verification_r20_20260520T140250_result.json`
- **Structured JSON:** [`40092506b2a0f4366748.json`](../../sessions/40/40092506b2a0f4366748.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部搜索完成，汇总结果如下。

---

## 论文 1: Mohamed et al.

- **arXiv ID**: [2502.20258](https://arxiv.org/abs/2502.20258) — **存在，匹配**
- **实际 title**: "LLM as a Broken Telephone: Iterative Generation Distorts Information" — **完全匹配**
- **实际作者**: Amr Mohamed, Mingmeng Geng, Michalis Vazirgiannis, Guokan Shang
- **Abstract 摘要**: 研究 LLM 在迭代生成中是否像 "broken telephone" 一样扭曲信息。发现失真随链长度累积，受中间语言选择和链复杂度影响；更长的链和更多模型会放大退化。
- **发表状态**: **ACL 2025 Main Conference**（已有 [ACL Anthology 条目](https://aclanthology.org/2025.acl-long.371/)和 [GitHub 代码](https://github.com/amr-mohamedd/LLM-as-a-Broken-Telephone)）
- **结论**: 全部信息验证通过 ✓

---

## 论文 2: Geng et al.

- **arXiv ID**: [2603.11228](https://arxiv.org/abs/2603.11228) — **存在，匹配**
- **实际 title**: "Markovian Generation Chains in Large Language Models" — **完全匹配**
- **实际作者**: Mingmeng Geng, Amr Mohamed, Guokan Shang, Michalis Vazirgiannis, Thierry Poibeau
- **Abstract 摘要**: 定义 Markovian generation chains 为迭代推理过程（每步仅使用前一步输出，无记忆）。在迭代改写和往返翻译实验中，输出要么收敛到小的循环集，要么在有限范围内持续产生新句子。多样性变化取决于温度参数和初始输入。
- **发表状态**: 2026年3月提交，preprint（[OpenReview 页面](https://openreview.net/forum?id=nTDn4OMiym)存在）
- **结论**: 全部信息验证通过 ✓

---

## 论文 3: Gillman et al.

- **arXiv ID**: [2402.07087](https://arxiv.org/abs/2402.07087) — **存在，匹配**
- **实际 title**: "Self-Correcting Self-Consuming Loops for Generative Model Training" — **完全匹配**
- **实际作者**: Nate Gillman, Michael Freeman, Daksh Aggarwal, Chia-Hong Hsu, Calvin Luo, Yonglong Tian, Chen Sun
- **Abstract 摘要**: 用合成数据训练生成模型会形成 self-consuming loops，可能导致训练不稳定或崩溃。提出引入 idealized correction function 使 self-consuming loops 指数级更稳定，并用模拟器中的专家知识实现近似校正。
- **发表状态**: **ICML 2024**（camera-ready 版本已确认）
- **结论**: 全部信息验证通过 ✓

---

## Youden's J Statistic 经典引用

- **完整引用**: Youden, W. J. (1950). Index for rating diagnostic tests. *Cancer*, 3(1), 32–35. doi: [10.1002/1097-0142(1950)3:1<32::AID-CNCR2820030106>3.0.CO;2-3](https://acsjournals.onlinelibrary.wiley.com/doi/10.1002/1097-0142(1950)3:1%3C32::AID-CNCR2820030106%3E3.0.CO;2-3)
- **BibTeX key 建议**: `youden1950index`
- **用途**: Youden's J = Sensitivity + Specificity − 1，用于选择最优分类阈值。在 ML Method section 中引用此文作为 threshold selection criterion 的经典出处即可。

---

## Bib 条目检查

1. **Alemohammad et al.**: "Self-Consuming Generative Models Go MAD" 的 first author 是 **Sina Alemohammad**（不是 Casco-Rodriguez）。Josue Casco-Rodriguez 是第二作者。arXiv: [2307.01850](https://arxiv.org/abs/2307.01850)。

2. **Roger Levy**: MIT 官方页面、Google Scholar、所有学术数据库一致使用 **Roger Levy**（无重音符号）。不是 "Lévy"。

---
