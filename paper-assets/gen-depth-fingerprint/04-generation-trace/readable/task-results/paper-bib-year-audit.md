# paper bib year audit

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_bib-year-audit_20260515T235806_result.json`
- **Structured JSON:** [`e9a0ff3a38ba3d7fda3e.json`](../../sessions/e9/e9a0ff3a38ba3d7fda3e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

artifacts 版本比 docs 版本多了一些 doi/volume/pages 字段，但核心信息（title/author/year/venue）完全一致，无需修复。

---

## 引用审计报告

**总数**: 49 条引用（`docs/paper/references.bib`）
**正文引用**: 72 处 `\cite`/`\citet`/`\citep`，覆盖 49 个唯一 key
**交叉检查**: 0 孤立条目，0 缺失条目，0 重复 key
**已验证**: 49 条全部通过 ✓
**需修复**: 0 条

### 验证详情

| 验证方式 | 条目数 | 结果 |
|---------|--------|------|
| OpenAlex 自动验证 | 41 | 标题+年份匹配 |
| WebSearch 人工复核（OpenAlex not_found） | 6 | detectgpt, reliable_detection, detection_possibilities, aaronson_watermark, pythia, xgboost — 全部确认存在且信息正确 |
| WebSearch 人工复核（OpenAlex mismatch） | 2 | self_consuming_mad（Alemohammad 确为第一作者，OpenAlex 索引错误）、qwen3（{Qwen Team} 是标准引用形式）|

### OpenAlex 年份差异说明

13 条 OpenAlex 返回年份与 bib 不同（如 dna_gpt bib=2024 vs OA=2023），全部核实为 **OpenAlex 使用 arXiv preprint 日期**，bib 使用会议/期刊出版年份，bib 写法正确。

### 2024-2026 近期论文重点核查

11 条 2024-2026 论文逐条 WebSearch 验证，标题、作者、年份、venue 全部准确，未发现 hallucinated 作者或编造条目。

### artifacts 同步

`artifacts/_project/paper/references.bib` 与 `docs/paper/references.bib` 核心信息一致，artifacts 版本额外包含部分 doi/volume/pages 字段，无冲突。

---
