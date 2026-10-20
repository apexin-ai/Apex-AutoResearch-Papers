# Reference Audit — Related Work Outline

**Date**: 2026-05-14
**Scope**: 4 citations flagged by reviewer in `section6_relwork_outline.tex`

---

## 1. `zhou2026snowballing`

- **Status**: ✅ 已确认存在
- **真实信息**:
  - **Title**: From Hallucination to Structure Snowballing: The Alignment Tax of Constrained Decoding in LLM Reflection
  - **Author**: Hongxu Zhou
  - **Year**: 2026 (arXiv preprint, April 2026)
  - **Venue**: arXiv:2604.06066 (preprint, 无正式 venue)
  - **URL**: https://arxiv.org/abs/2604.06066
- **内容摘要**: 研究 constrained decoding 在 LLM 自我反思中引发的新失败模式 "structure snowballing"——强制格式约束不但不能抑制幻觉传播，反而将模型推入格式陷阱和死循环。在 Qwen3-8B 上验证。
- **建议操作**: **保留**。论文真实存在，与 constrained decoding 的质量问题直接相关。注意 bib 条目中 venue 应标注为 arXiv preprint。

---

## 2. `upadhyay2023openie`

- **Status**: ✅ 已确认存在
- **真实信息**:
  - **Title**: Open Information Extraction with Entity Focused Constraints
  - **Authors**: Prajna Upadhyay, Oana Balalau, Ioana Manolescu
  - **Year**: 2023
  - **Venue**: Findings of EACL 2023
  - **URL**: https://aclanthology.org/2023.findings-eacl.95/
- **内容摘要**: 在 OpenIE 中注入实体约束（constrained inference + constraint-aware training），基于 OpenIE6，CaRB F1 提升 29.17%，WIRe57 F1 提升 24.37%。
- **建议操作**: **保留**。信息准确，无需修改。

---

## 3. `regino2025kgcurator`

- **Status**: ✅ 已确认存在
- **真实信息**:
  - **Title**: Can LLMs be Knowledge Graph Curators for Validating Triple Insertions?
  - **Authors**: André Gomes Regino, Julio Cesar dos Reis
  - **Year**: 2025
  - **Venue**: GenAIK 2025 Workshop (co-located with COLING 2025), pp. 87–99, Abu Dhabi, UAE
  - **URL**: https://aclanthology.org/2025.genaik-1.10/
- **内容摘要**: 探索 LLM 作为 KG 自动验证器来校验 RDF triple 插入，评估了 Llama-3-70B-Instruct 等模型的准确性和一致性。
- **建议操作**: **保留**。信息准确。注意 bib 中 venue 应写 `Proceedings of the Workshop on Generative AI and Knowledge Graphs (GenAIK)`，booktitle 不要简写为 "KGCurator"（这不是论文中的系统名）。

---

## 4. `qi2024adelie`

- **Status**: ✅ 已确认存在
- **真实信息**:
  - **Title**: ADELIE: Aligning Large Language Models on Information Extraction
  - **Authors**: Yunjia Qi, Hao Peng, Xiaozhi Wang, Bin Xu, Lei Hou, Juanzi Li
  - **Year**: 2024
  - **Venue**: EMNLP 2024 (main conference)
  - **URL**: https://aclanthology.org/2024.emnlp-main.419/
- **内容摘要**: 构建 IE 对齐语料 IEInstruct，通过 SFT + DPO 训练 ADELIE 模型，覆盖 closed IE / open IE / on-demand IE，在开源模型中达到 SOTA。
- **建议操作**: **保留**。信息准确，无需修改。

---

## 总结

| Bib Key | 状态 | 操作 |
|---------|------|------|
| `zhou2026snowballing` | ✅ 真实存在 | 保留，bib 标注为 arXiv preprint |
| `upadhyay2023openie` | ✅ 真实存在 | 保留，无需修改 |
| `regino2025kgcurator` | ✅ 真实存在 | 保留，确认 venue 全称 |
| `qi2024adelie` | ✅ 真实存在 | 保留，无需修改 |

**幻觉引用数量: 0/4**

`literature_map.yaml` 在项目配置中不存在（仅在 artifacts 目录有一份），无需清理。
