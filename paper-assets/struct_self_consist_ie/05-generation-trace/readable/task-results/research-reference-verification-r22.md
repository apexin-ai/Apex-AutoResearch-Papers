# research reference verification r22

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_reference_verification_r22_20260519T040634_result.json`
- **Structured JSON:** [`4278bf0b6571ac6e4bd4.json`](../../sessions/42/4278bf0b6571ac6e4bd4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

BibTeX entries 已追加。以下是完整汇报。

---

## Part A: 新引用查找结果

### 1. Xie et al. 2023

找到两篇匹配的论文，均相关：

**主匹配（匹配 "self-evaluation" + "beam search"）：**
- **Title**: Self-Evaluation Guided Beam Search for Reasoning
- **Authors**: Xie, Yuxi et al.
- **Venue**: NeurIPS 2023
- **Year**: 2023
- **BibKey**: `xie2023selfevaluation`

**次匹配（匹配 "self-consistency" + "NER"，与项目主题直接相关）：**
- **Title**: Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models
- **Authors**: Xie, Tingyu et al.
- **Venue**: NAACL 2024（arXiv preprint 2023.11）
- **Year**: 2024
- **BibKey**: `xie2024selfimproving`

### 2. Wan et al. 2024 — IE survey

**未找到。** 经多轮搜索（变换关键词、扩大范围），未找到以 "Wan" 为第一作者的 2024 年 IE survey。最接近的匹配：
- Xu et al. 2024, "Large Language Models for Generative Information Extraction: A Survey" (arXiv:2312.17617, Frontiers of Computer Science 2024) — 第一作者是 Xu Derong，非 Wan
- Wan et al. 2023, "GPT-RE: In-context Learning for Relation Extraction" (EMNLP 2023) — 2023 年且非 survey

请确认作者名或提供更多线索。

### 3. Ensemble-based NER methods（3 篇）

| BibKey | Title | Authors | Venue | Year |
|---|---|---|---|---|
| `xiao2025el4ner` | EL4NER: Ensemble Learning for NER via Multiple Small-Parameter LLMs | Xiao, Yuzhen et al. | arXiv:2505.23038 | 2025 |
| `sarcinelli2025local` | Local LLM Ensembles for Zero-shot Portuguese NER | Sarcinelli et al. | arXiv:2512.10043 | 2025 |
| `naderi2021ensemble` | Ensemble of Deep Masked Language Models for Effective NER in Health and Life Science Corpora | Naderi, Nona et al. | Frontiers in Research Metrics and Analytics | 2021 |

三篇均涉及多模型 + 实体级聚合/投票机制。EL4NER 最相关（两阶段 pipeline：span 提取 + 实体类型投票）。

---

## Part B: 9 条现有引用验证

| # | BibKey | 当前 Year | 当前 Venue | 正确? | 备注 |
|---|---|---|---|---|---|
| 1 | `wang2023selfconsistency` | 2023 | ICLR 2023 | ✅ | — |
| 2 | `cobbe2021verifiers` | 2021 | arXiv preprint | ✅ | 始终为 arXiv preprint，未正式发表于会议/期刊 |
| 3 | `eikema2022sampling` | 2022 | EMNLP 2022 | ✅ | pages 10978–10993，DOI 正确 |
| 4 | `venktesh2025trust` | 2025 | arXiv preprint | ✅ | arXiv:2508.16665 |
| 5 | `snell2025scaling` | 2025 | ICLR 2025 | ✅ | — |
| 6 | `willard2023guided` | 2023 | arXiv preprint | ✅ | 未正式发表于会议，arXiv:2307.09702 |
| 7 | `zheng2024llamafactory` | 2024 | ACL 2024 System Demos | ✅ | pages 400–410，DOI 正确 |
| 8 | `luan2018scierc` | 2018 | EMNLP 2018 | ✅ | DOI 正确 |
| 9 | `derczynski2017wnut` | 2017 | W-NUT 2017 workshop | ✅ | — |

**9 条引用全部验证通过，年份和 venue 均正确。**

---
