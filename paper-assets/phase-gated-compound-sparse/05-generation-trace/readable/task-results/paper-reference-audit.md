# paper reference audit

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_reference_audit_20260514T094550_result.json`
- **Structured JSON:** [`c58fa8788dba89e8a7f9.json`](../../sessions/c5/c58fa8788dba89e8a7f9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

31 个 bib 条目，与 31 个唯一引用 key 完全匹配。

## 审计结果

**31/31 引用全部验证通过 ✅** — 无虚假引用、无 placeholder、无幻觉。

产出文件：
- **references.bib**: `/artifacts/_project/paper/references.bib` — 31 条完整 BibTeX 条目，acl_natbib 兼容
- **审计报告**: `/artifacts/_project/paper/citation_audit_report.md` — 每条引用的验证状态、作者、venue、arXiv ID

关键发现：
- `snapkv-neurips2024` 和 `snapkv2024` 是同一篇论文的两个 key（已分别建条目）
- `h2o2024` cite key 写的 2024，实际论文发表于 NeurIPS 2023（bib 中已用正确年份）
- 2026 论文（如 `retentivekv-2026`、`decision-repr-transition-2026`）均为最近几天发布的 arXiv 预印本，已验证存在

---
