# research verify gu2025 citation

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_verify_gu2025_citation_20260520T091932_result.json`
- **Structured JSON:** [`5692c1715d573814c956.json`](../../sessions/56/5692c1715d573814c956.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完成。汇报如下：

---

## 引用验证结果

### 1. Gu et al. (2025) "On the Emergence of Cross-Lingual Alignment..." ICLR Spotlight

**判定：幻觉 (HALLUCINATED)**

该论文不存在。标题、venue、年份均无法对应任何真实论文。这是一个**嵌合体幻觉**，混合了两篇真实论文：

| 属性 | 幻觉引用 | 真实来源 A | 真实来源 B |
|------|---------|-----------|-----------|
| 第一作者 | Gu | **Jiawei Gu** | Wang et al. |
| 标题关键词 | "Emergence of Cross-Lingual Alignment" | "Critical Mixture Ratios" | **"Probing the Emergence of Cross-lingual Alignment during LLM Training"** |
| 内容 | "critical mixing ratio power law" | **CMR Scaling Law** | cross-lingual neuron overlap |
| Venue | ICLR 2025 Spotlight | **EMNLP 2024** | ACL Findings 2024 |
| arXiv | — | 2407.17467 | 2406.13229 |

**好消息：该引用未进入论文 LaTeX 文件。** 仅出现在内部分析 artifact (`artifacts/phase_transition_analysis/report.md`)。`docs/paper/` 中无任何 `gu2025` 引用。

如需引用 CMR 相关工作，正确引用为：
> Gu, J., Yang, Z., Ding, C., Zhao, R., & Tan, F. (2024). CMR Scaling Law: Predicting Critical Mixture Ratios for Continual Pre-training of Language Models. *EMNLP 2024*. arXiv:2407.17467

---

### 2. Truong & Truong (2025) "Entropy Collapse: A Universal Failure Mode of Intelligent Systems"

**判定：真实 (VERIFIED) ✓**

- arXiv: **2512.12381**（2025-12-13 v1, 2026-03-13 v2）
- 作者：Truong Xuan Khanh, Truong Quynh Hoa
- Venue：arXiv preprint (无正式会议发表)
- 论文中正确引用于 `references.bib:62`、`related_work.tex:49`、`discussion.tex:155`
- 两个 universality classes 确认存在：
  - **Class 1 (Convex, Irreversible)**：κ > 0, power-law feedback, ν = 1
  - **Class 2 (Linear, Reversible)**：κ = 0, linear feedback, ν = 1/2
- bib 条目与 arXiv 元数据一致，无需修改

---

### 3. Dakos et al. (2012) "Methods for Detecting Early Warnings of Critical Transitions..."

**判定：真实 (VERIFIED) ✓**

- 完整标题：*Methods for Detecting Early Warnings of Critical Transitions in Time Series Illustrated Using Simulated Ecological Data*
- 作者：Vasilis Dakos, Stephen R. Carpenter, William A. Brock, Aaron M. Ellison, Vishwesha Guttal, Anthony R. Ives, Sonia Kéfi, et al.
- Venue：**PLoS ONE** 7(7): e41010, 2012
- DOI: 10.1371/journal.pone.0041010
- **注意：该论文未直接被 LaTeX 论文引用。** `docs/paper/references.bib` 中无 `dakos2012` 条目。Dakos 仅作为 Scheffer et al. (2009, 2012) 的共同作者出现。该引用出现在 `consensus_framework.md` 等内部 artifact 中。如需在论文中引用需手动添加 bib entry。

---
