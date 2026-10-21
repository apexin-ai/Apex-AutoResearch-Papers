# research diveye citation check

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_diveye_citation_check_20260514T171717_result.json`
- **Structured JSON:** [`2323dd2598096ed2598d.json`](../../sessions/23/2323dd2598096ed2598d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结论：NOT fake，但 venue 错误。**

- **DivEye 是真实论文**：Advik Raj Basani & Pin-Yu Chen，"Diversity Boosts AI-Generated Text Detection"，arXiv 2509.18880
- **Venue 标注有误**：实际发表于 **TMLR '26**（Transactions on Machine Learning Research），不是 ICLR 2026。可能曾投稿 ICLR 2026（OpenReview 有对应 submission），但最终收录于 TMLR
- **方法本身作为 baseline 合理**：DivEye 的 surprisal diversity 特征与 recursive generation depth estimation 任务相关

**需要修正**：`src/baselines.py` 中 `(Basani & Chen, ICLR 2026)` → `(Basani & Chen, TMLR 2026)`

报告已写入 `artifacts/diveye_citation_audit.md`。

---
