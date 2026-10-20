# research reference audit

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_reference_audit_20260514T185731_result.json`
- **Structured JSON:** [`917d408bc254de21766b.json`](../../sessions/91/917d408bc254de21766b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。结果如下：

**总计**: 31 条 bib 条目，26 条被正文引用，8 条经 WebSearch 验证真实性（全部通过，无幻觉引用）。

**发现 7 个问题**：

| 严重度 | 数量 | 概要 |
|--------|------|------|
| Critical | 1 | `deepseek-r1-2025` DOI 错误：bib 中 `10.1038/s41586-025-08636-z`，正确应为 `10.1038/s41586-025-09422-z` |
| Warning | 3 | (1) 同条目 Nature 标题与 bib 标题不一致；(2) author 用 `{DeepSeek-AI}` 但 Nature 列出个人作者；(3) 5 个 orphan bib 条目未被引用 |
| Info | 3 | (1) PyramidKV 可能已发表但仍标为 arXiv；(2) paper_framing 提到的 3 篇定位参考文献（Physics of KV Cache Compression / HIES / R-KV）未出现在 Related Work 中；(3) DOI 字段不一致 |

**最优先修复**：`deepseek-r1-2025` 的 DOI 需立即更正，否则读者/审稿人点击 DOI 链接无法到达正确论文。

报告已写入 `artifacts/reference_audit_report.md` 并注册。

---
