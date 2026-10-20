# paper bib audit m7

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_bib-audit-m7_20260515T221406_result.json`
- **Structured JSON:** [`1a709f956f5a17b6d53c.json`](../../sessions/1a/1a709f956f5a17b6d53c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成。下面是完整审计报告：

---

## 引用审计报告

**总数**: 49 条 bib 条目  
**正文引用**: 49 unique keys, 72 次 `\cite` 调用  
**交叉检查**: 0 orphan, 0 missing — 完全匹配  
**在线验证 (OpenAlex)**: 41 verified, 5 not_found (API限制), 3 mismatch

---

### 修复列表

| # | Key | 问题 | 原始 | 修正 | 验证来源 |
|---|-----|------|------|------|----------|
| 1 | `curse_of_recursion` | 作者顺序错误 | `...Zhao, Yiren and Gal, Yarin and Papernot, Nicolas and Anderson, Ross` | `...Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin` | [Nature](https://www.nature.com/articles/s41586-024-07566-y) |
| 2 | `reliable_detection` | 标题不完整（缺 TMLR 发表版副标题） | `Can AI-Generated Text be Reliably Detected?` | `Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks` | [OpenReview TMLR](https://openreview.net/forum?id=OOgsAZdFOt) |

---

### OpenAlex not_found（已人工确认无误）

| Key | 原因 | 人工验证结果 |
|-----|------|-------------|
| `detectgpt` | API 检索限制 | [ICML 2023 confirmed](https://proceedings.mlr.press/v202/mitchell23a.html) |
| `detection_possibilities` | API 检索限制 | [ICML 2024 confirmed](https://proceedings.mlr.press/v235/chakraborty24a.html) |
| `pythia` | API 检索限制 | ICML 2023, authors/year correct |
| `xgboost` | API 检索限制 | KDD 2016, authors/year correct |
| `aaronson_watermark` | Blog post, not indexed | 技术演讲, `@misc` 类型正确 |

### OpenAlex mismatch（已人工确认 bib 正确）

| Key | OpenAlex 报告 | 人工结论 |
|-----|--------------|----------|
| `reliable_detection` | year: bib=2025 vs api=2023 | arXiv 2023→TMLR 2025 正式发表。**year=2025 正确** |
| `self_consuming_mad` | first_author: bib=alemohammad vs api=casco-rodriguez | [ICLR 2024 proceedings](https://proceedings.iclr.cc/paper_files/paper/2024/file/ebc042e767de551803ccfcc45e2454f5-Paper-Conference.pdf) 确认 Alemohammad 为一作。**bib 正确** |
| `qwen3` | first_author: bib=team vs api=yang | 集体署名 `{Qwen Team}` 是该技术报告的标准引用方式。**bib 正确** |

---

### 无 CRITICAL 级问题

未发现幻觉引用（作者/标题/年份完全对不上的情况）。所有 49 条引用均为真实存在的论文，作者和标题准确。

**修改文件**: `docs/paper/references.bib`（2 处修复）  
**artifacts 版本**: 已经是正确的，无需修改。

---
