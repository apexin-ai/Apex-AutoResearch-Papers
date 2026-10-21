# research scan all cite keys

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_scan_all_cite_keys_20260514T185439_result.json`
- **Structured JSON:** [`9282c0e2460e4a379128.json`](../../sessions/92/9282c0e2460e4a379128.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 交叉对比结果

### 1. 各 .tex 文件引用数

| 文件 | cite keys 数 |
|------|-------------|
| section6_related_work.tex | 35 |
| section6_relwork_outline.tex | 30 |
| section1_introduction_draft.tex | 9 |
| section6_relwork_additions.tex | 9 |
| section2_background.tex | 5 |
| section3_violation_landscape.tex | 3 |
| discussion_paragraphs.tex | 2 |
| discussion_paragraphs_cf83d1.tex | 2 |
| section3_method_draft.tex | 1 |
| 其余 11 个文件 | 0 |
| **合计（去重）** | **44** |

### 2. Bib 已有条目（17 个）

relwork_new_entries.bib 定义了：synchromesh_iclr2022, mgd_neurips2023, pldi2025_type_constrained_codegen, roth_yih_2004, adakgc_emnlp2023, knowcoder_acl2024, spires_2024, ontologx_2025, ekaw2024_ontology_beam, scholak2021picard, olasunkanmi2025relate, zhou2026ontologytools, eberts2020spert, yan2021pfn, zhong2021frustratingly, ye2022packed, zhou2026snowballing

### 3. 缺失 key 列表（27 个，按来源分组）

#### 非 §6 文件缺失（12 个去重 — 需要优先补充）

| 文件 | 缺失 keys |
|------|-----------|
| **section1_introduction_draft.tex** | `beurer-kellner2023lmql`, `dong2025xgrammar`, `li2023codeie`, `lu2022uie`, `luan2018scierc`, `sainz2024gollie`, `wei2023zeroshot`, `willard2023outlines`, `yao2019docred` |
| **section2_background.tex** | `dong2025xgrammar`, `luan2018scierc`, `willard2023outlines`, `yao2019docred`, `zheng2024sglang` |
| **section3_method_draft.tex** | `xgrammar` |
| **section3_violation_landscape.tex** | `luan2018scierc`, `qwen2025qwen3`, `yao2019docred` |

去重后 12 个：`beurer-kellner2023lmql`, `dong2025xgrammar`, `li2023codeie`, `lu2022uie`, `luan2018scierc`, `qwen2025qwen3`, `sainz2024gollie`, `wei2023zeroshot`, `willard2023outlines`, `xgrammar`, `yao2019docred`, `zheng2024sglang`

#### §6 文件额外缺失（15 个 — 另有 worker 处理中）

`banerjee2025crane`, `beurer-kellner2024domino`, `decao2021genre`, `geng2023gcd`, `josifoski2022genie`, `khorshidi2025odke`, `lu2021neurologic`, `park2024grammar`, `qi2024adelie`, `regino2025kgcurator`, `schall2025hiddencost`, `synchromesh_neurips2022`, `tam2024letmespeak`, `upadhyay2023openie`, `zaratiana2024enrico`

### 4. 孤立 bib 条目

**无。** 全部 17 个 bib 条目均被至少一个 .tex 文件引用。

### 5. 需注意的问题

- **`xgrammar`** (section3_method_draft.tex) — 疑似应为 `dong2025xgrammar`，key 命名不一致
- **`synchromesh_neurips2022`** (section6_relwork_additions.tex) — bib 中已有 `synchromesh_iclr2022`（正确 venue 是 ICLR 2022），应统一为 `synchromesh_iclr2022`
- **discussion_paragraphs.tex** — `zhong2021frustratingly` 和 `ye2022packed` 均已在 bib 中，无缺失

---
