# Reference Audit: Related Work Citations

**Date**: 2026-05-14
**Scope**: 4 citations flagged as potentially hallucinated in `section6_relwork_outline.tex`

---

## 1. zhou2026snowballing
- **Status**: VERIFIED
- **Search queries**: `structure snowballing constrained decoding LLM format compliance 2025 2026`, `arxiv 2604.06066 "structure snowballing" constrained decoding authors`
- **Findings**: Paper exists on arXiv (2604.06066), submitted April 7, 2026. Title: "From Hallucination to Structure Snowballing: The Alignment Tax of Constrained Decoding in LLM Reflection". Author: Hongxu Zhou (Saarland University). The paper investigates constrained decoding in LLM self-correction and identifies "structure snowballing" — a failure mode where format compliance cognitive load traps models in formatting patterns rather than improving reasoning. Evaluated on Qwen3-8B with Outlines-based constrained decoding.
- **Action**: 保留。论文真实存在，描述准确。Bib 条目中 venue 应标注为 arXiv preprint（尚无正式 venue）。
- **URL**: https://arxiv.org/abs/2604.06066

## 2. upadhyay2023openie
- **Status**: VERIFIED
- **Search queries**: `Upadhyay 2023 Open IE entity type constraints CaRB`
- **Findings**: Paper exists on ACL Anthology. Title: "Open Information Extraction with Entity Focused Constraints". Authors: Prajna Upadhyay, Oana Balalau, Ioana Manolescu. Venue: Findings of EACL 2023. The paper injects entity-type knowledge as constraints into Open IE via constrained inference and constraint-aware training (based on OpenIE6), achieving 29.17% F1 improvement on CaRB and 24.37% on WIRe57.
- **Action**: 保留，无需修改。描述与论文内容完全一致。
- **URL**: https://aclanthology.org/2023.findings-eacl.95/

## 3. regino2025kgcurator
- **Status**: VERIFIED
- **Search queries**: `Regino 2025 KG curator RDF triple validation domain range`, `"Can LLMs be Knowledge Graph Curators" Regino 2025 authors venue`
- **Findings**: Paper exists on ACL Anthology (2025.genaik-1.10). Title: "Can LLMs be Knowledge Graph Curators for Validating Triple Insertions?". Authors: André Gomes Regino, Julio Cesar dos Reis. Venue: GenAIK 2025 Workshop (co-located with COLING 2025), pp. 87–99, Abu Dhabi, UAE. The paper evaluates LLMs on four RDF triple validation tasks: class/property alignment, URI standardization, semantic consistency, and syntactic correctness. Tested on Llama-3-70B-Instruct among other models.
- **Action**: 保留。Outline 中描述 "multi-stage LLM pipeline for validating RDF triple insertions against domain/range constraints" 基本准确——"domain/range constraints" 对应论文中的 class/property alignment 验证任务，"multi-stage" 对应四个验证阶段。注意 bib 中 venue 应写 `Proceedings of the Workshop on Generative AI and Knowledge Graphs (GenAIK)`，"KGCurator" 并非论文中的系统名称，仅为 cite key 简写。
- **URL**: https://aclanthology.org/2025.genaik-1.10/

## 4. qi2024adelie
- **Status**: VERIFIED
- **Search queries**: `ADELIE 2024 information extraction SFT DPO alignment`, `"ADELIE" "Aligning Large Language Models on Information Extraction" authors Qi EMNLP 2024`
- **Findings**: Paper exists on ACL Anthology. Title: "ADELIE: Aligning Large Language Models on Information Extraction". Authors: Yunjia Qi, Hao Peng, Xiaozhi Wang, Bin Xu, Lei Hou, Juanzi Li (THU-KEG). Venue: EMNLP 2024 (main conference), Miami, Florida, USA. The paper constructs IE alignment corpus IEInstruct, trains ADELIE via SFT + DPO on closed/open/on-demand IE tasks, achieving SOTA among open-source models while preserving general capabilities. Models available: ADELIE-SFT/DPO variants based on LLaMA-2-7B, LLaMA-3.2-3B, Qwen2.5-1.5B.
- **Action**: 保留，无需修改。描述与论文内容完全一致。
- **URL**: https://aclanthology.org/2024.emnlp-main.419/

## Summary
- Verified: **4/4**
- Need replacement: **0**
- Recommended deletions: **0**

所有 4 篇引用均为真实论文，描述与原文内容一致，无幻觉。仅需注意：
1. `zhou2026snowballing` 的 bib 条目应标注为 arXiv preprint（无正式 venue）
2. `regino2025kgcurator` 的 bib 条目 venue 应使用 GenAIK Workshop 全称
