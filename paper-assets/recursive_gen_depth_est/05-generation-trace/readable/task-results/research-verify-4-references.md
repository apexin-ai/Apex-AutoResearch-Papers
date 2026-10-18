# research verify 4 references

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_verify_4_references_20260515T225303_result.json`
- **Structured JSON:** [`9a9c141e108e43b5ee6e.json`](../../sessions/9a/9a9c141e108e43b5ee6e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

搜索完成，以下是验证报告。

---

## wu2025_detection_survey
- **搜索查询**: `"machine-generated text detection" survey Computational Linguistics 2025`; `Junchao Wu "LLM-Generated Text Detection" Computational Linguistics authors`
- **搜索结果**: 在 ACL Anthology 和 MIT Press 找到论文
- **标题匹配**: ✅ "A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions"
- **作者匹配**: ✅ Junchao Wu, Shu Yang, Runzhe Zhan, Yulin Yuan, Lidia Sam Chao, Derek Fai Wong（第一作者 Wu，末位 Wong）
- **Venue匹配**: ✅ Computational Linguistics, Vol. 51, Issue 1, March 2025（arXiv: 2310.14724）
- **验证结论**: **verified**
- **修正建议**: 无。注意该论文有 arXiv 版本 (2310.14724)，可补充。

## bevendorff2025_two_paradigms
- **搜索查询**: `Bevendorff "two paradigms" authorship detection ACL 2025`
- **搜索结果**: 在 ACL Anthology 找到论文（[aclanthology.org/2025.findings-acl.194](https://aclanthology.org/2025.findings-acl.194/)）
- **标题匹配**: ✅ "The Two Paradigms of LLM Detection: Authorship Attribution vs. Authorship Verification"
- **作者匹配**: ✅ Janek Bevendorff, Matti Wiegmann, Emmelie Richter, Martin Potthast, Benno Stein
- **Venue匹配**: ✅ Findings of ACL 2025, pages 3762–3787, Vienna, Austria
- **内容验证**: ✅ 论文确实提出了"两个范式"的二分法——将 LLM 检测区分为 authorship attribution（归因）和 authorship verification（验证）两种范式，并系统分析了当前研究对此的混淆
- **验证结论**: **verified**
- **修正建议**: 无

## he2025_closer_look
- **搜索查询**: `arXiv 2509.16499 "closer look"`; `"A Closer Look at Model Collapse" NeurIPS 2025 Shi authors`
- **搜索结果**: 在 arXiv 和 NeurIPS 官网找到论文（NeurIPS 2025 Spotlight）
- **标题匹配**: ✅ "A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective"
- **作者匹配**: ❌ bib key 暗示第一作者姓 "He"，但**实际第一作者是 Lianghe Shi**（石良赫），完整作者：Lianghe Shi, Meng Wu, Huijie Zhang, Zekai Zhang, Molei Tao, Qing Qu
- **Venue匹配**: ✅ NeurIPS 2025 (Spotlight)
- **arXiv ID**: ✅ 2509.16499 正确
- **验证结论**: **corrected** — 论文存在且 venue/arXiv ID 正确，但 bib key 的作者归属有误
- **修正建议**: bib key 应从 `he2025_closer_look` 改为 `shi2025_closer_look`；bib 条目中 author 字段第一作者应为 "Shi, Lianghe"，末位作者 "Qu, Qing"

## feng2025_escaping_collapse
- **搜索查询**: `arXiv 2510.16657 "escaping collapse"`; `Bingji Yi "Escaping Model Collapse" accepted venue`; `"Escaping Model Collapse via Synthetic Data Verification" ICLR 2026 DATA-FM workshop`
- **搜索结果**: 在 arXiv 和 OpenReview 找到论文
- **标题匹配**: ✅ "Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence"
- **作者匹配**: ❌ bib key 暗示第一作者姓 "Feng"，但**实际第一作者是 Bingji Yi**，完整作者：Bingji Yi, Qiyuan Liu, Yuwei Cheng, Haifeng Xu
- **Venue匹配**: ❌ 声称 NeurIPS 2025，但**实际发表于 3rd DATA-FM Workshop @ ICLR 2026**（巴西）。无任何证据表明被 NeurIPS 2025 主会接收。
- **arXiv ID**: ✅ 2510.16657 正确
- **验证结论**: **corrected** — 论文存在，但作者和 venue 均有误
- **修正建议**:
  1. bib key 从 `feng2025_escaping_collapse` 改为 `yi2025_escaping_collapse`
  2. author 字段第一作者 "Yi, Bingji"，末位 "Xu, Haifeng"
  3. venue 从 "NeurIPS 2025" 改为 "3rd DATA-FM Workshop @ ICLR 2026"
  4. year 从 2025 改为 2026

---

## 汇总

| bib key | 标题 | 作者 | Venue | 结论 |
|---------|------|------|-------|------|
| wu2025_detection_survey | ✅ | ✅ | ✅ | **verified** |
| bevendorff2025_two_paradigms | ✅ | ✅ | ✅ (+内容verified) | **verified** |
| he2025_closer_look | ✅ | ❌ 应为Shi | ✅ | **需修正** — 作者错误 |
| feng2025_escaping_collapse | ✅ | ❌ 应为Yi | ❌ 应为ICLR 2026 workshop | **需修正** — 作者+venue均错 |

**第 3、4 篇的作者和 venue 错误是典型的 LLM 幻觉特征**——标题和 arXiv ID 正确但作者姓氏被替换、venue 被虚构。建议在整合前修正 bib 条目，并重新审查这两篇论文在正文中的引用上下文是否与论文实际内容一致。

Sources:
- [Wu et al. 2025 - ACL Anthology](https://aclanthology.org/2025.cl-1.8/)
- [Wu et al. 2025 - MIT Press](https://direct.mit.edu/coli/article/51/1/275/127462/A-Survey-on-LLM-Generated-Text-Detection-Necessity)
- [Bevendorff et al. 2025 - ACL Anthology](https://aclanthology.org/2025.findings-acl.194/)
- [Shi et al. 2025 - arXiv](https://arxiv.org/abs/2509.16499)
- [Shi et al. 2025 - NeurIPS Poster](https://neurips.cc/virtual/2025/poster/119754)
- [Yi et al. 2025 - arXiv](https://arxiv.org/abs/2510.16657)
- [Yi et al. - OpenReview](https://openreview.net/forum?id=yfk6c39omW)
- [DATA-FM Workshop @ ICLR 2026](https://data-fm-iclr2026.github.io/)

---
