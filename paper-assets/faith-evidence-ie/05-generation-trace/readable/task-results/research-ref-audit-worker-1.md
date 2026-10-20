# research ref audit worker 1

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_ref-audit-worker-1_20260526T101554_result.json`
- **Structured JSON:** [`a693055582ddaba71af7.json`](../../sessions/a6/a693055582ddaba71af7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

引用审计完成。报告已写入 `artifacts/ref_audit_worker1.md`。

**核心结论：所有 52 篇论文均真实存在，无虚构引用。**

9 条有问题需修复：

| 严重性 | cite_key | 问题 |
|--------|----------|------|
| 高 | wang2025relprior | 标题错误（添加 "RelPrior:" 前缀、改写措辞） |
| 高 | tang2025rsftppo | 缺少 2 位作者（Shaan Ul Haque, Nithish Kannen） |
| 中 | li2026qurl | Venue 过时：arXiv → 已被 ICLR 2026 接收 |
| 中 | wang2025rullm | 标题添加虚假 "Ru-LLM:" 前缀；@article→@inproceedings |
| 中 | gulcehre2023rest | @inproceedings 但 booktitle 是 arXiv preprint → 应改 @article |
| 中 | ma2023dreeam | Venue "Findings of EACL 2023" 可能应为 "EACL 2023 main" |
| 低 | xu2024lmrc | 标题添加 "LMRC:" 前缀 |
| 低 | ito2025mogrpo | cite key "ito" 但第一作者是 Ichihara |
| 低 | liu2026gdpo | 标题大小写微差 |

另有 17 条 bib 条目未在正文引用（可清理）。7 个 cite key 与第一作者姓氏不匹配（不影响渲染）。

---
