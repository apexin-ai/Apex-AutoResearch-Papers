# paper bib audit

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_bib-audit_20260515T203516_result.json`
- **Structured JSON:** [`7d2af4cfe382d72c4d6e.json`](../../sessions/7d/7d2af4cfe382d72c4d6e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 6 个 not_found 条目 + diveye 年份均已通过 WebSearch 验证。现在整理审计结果。

## 引用审计报告

**总数**: 49 条引用
**已验证**: 49 条（全部真实存在）
**Orphan**: 0 | **Missing**: 0 | **Duplicate**: 0
**需修复**: 0

---

### OpenAlex 未找到但 WebSearch 确认真实（6 条）

| # | Key | 原因 | WebSearch 验证 |
|---|-----|------|---------------|
| 1 | `detectgpt` | OpenAlex 搜索匹配度低 (0.38) | [ICML 2023 proceedings](https://proceedings.mlr.press/v202/mitchell23a.html) ✅ 标题/作者/年份/venue 全部正确 |
| 2 | `reliable_detection` | OpenAlex 搜索匹配度低 (0.34) | [OpenReview TMLR](https://openreview.net/forum?id=OOgsAZdFOt) ✅ Sadasivan et al., TMLR 2025 正确 |
| 3 | `detection_possibilities` | OpenAlex 搜索匹配度低 (0.25) | [PMLR v235](https://proceedings.mlr.press/v235/chakraborty24a.html) ✅ Chakraborty et al., ICML 2024 正确 |
| 4 | `aaronson_watermark` | 技术演讲非正式出版物，不在学术数据库中 | [Aaronson blog](https://scottaaronson.blog/?p=6823) ✅ 2022 Technical Talk 正确 |
| 5 | `pythia` | OpenAlex 搜索匹配度低 (0.50) | [DBLP](https://dblp.org/rec/conf/icml/BidermanSABOHKP23.html) ✅ Biderman et al., ICML 2023 正确 |
| 6 | `xgboost` | OpenAlex 搜索匹配度低 (0.30) | [ACM DL](https://dl.acm.org/doi/10.1145/2939672.2939785) ✅ Chen & Guestrin, KDD 2016 正确 |

### OpenAlex Mismatch（2 条）

| # | Key | Mismatch | 判定 |
|---|-----|----------|------|
| 1 | `self_consuming_mad` | first_author: bib=Alemohammad vs api=Casco-Rodriguez | **Bib 正确**。[arXiv:2307.01850](https://arxiv.org/abs/2307.01850) 第一作者为 Alemohammad，OpenAlex 数据有误 |
| 2 | `qwen3` | first_author: bib=Team vs api=Yang | **Bib 正确**。技术报告以 `{Qwen Team}` 署名是标准做法 |

### 2026 年 arXiv Preprint 验证（6 条）

| Key | arXiv ID | OpenAlex | 状态 |
|-----|----------|----------|------|
| `ld_score` | 2605.01647 | verified, year=2026 | ✅ 真实 |
| `diveye` | — (TMLR) | verified, year=2025 | ✅ 真实。[GitHub](https://github.com/IBM/diveye) 标记 [TMLR '26]，bib year=2026 正确 |
| `generator_barrier` | 2604.13692 | verified, year=2026 | ✅ 真实 |
| `feat_aug_transformer` | 2605.03969 | verified, year=2026 | ✅ 真实 |
| `chainwash` | 2605.05503 | verified, year=2026 | ✅ 真实 |
| `markovian_chains` | 2603.11228 | verified, year=2026 | ✅ 真实 |

### 年份说明

部分 OpenAlex matched_year 与 bib year 差 1 年（如 `dna_gpt` bib=2024/OA=2023, `fast_detectgpt` bib=2024/OA=2023 等）。这是 arXiv 首发年 vs 会议出版年的正常差异。Bib 中使用会议/期刊出版年是学术标准做法，**无需修改**。

---

**结论**: 49/49 条引用全部验证为真实存在。标题、作者、年份、venue 均正确。无幻觉引用，无需修改 `references.bib`。

Sources:
- [DetectGPT - ICML Proceedings](https://proceedings.mlr.press/v202/mitchell23a.html)
- [Reliable Detection - OpenReview TMLR](https://openreview.net/forum?id=OOgsAZdFOt)
- [Detection Possibilities - PMLR](https://proceedings.mlr.press/v235/chakraborty24a.html)
- [Aaronson Watermark Talk](https://www.scottaaronson.com/talks/watermark.ppt)
- [Pythia - DBLP](https://dblp.org/rec/conf/icml/BidermanSABOHKP23.html)
- [XGBoost - ACM DL](https://dl.acm.org/doi/10.1145/2939672.2939785)
- [DivEye GitHub (TMLR '26)](https://github.com/IBM/diveye)

---
