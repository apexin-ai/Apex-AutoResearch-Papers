# paper reference audit full

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_reference_audit_full_20260523T070604_result.json`
- **Structured JSON:** [`0f765ba5105891d4be71.json`](../../sessions/0f/0f765ba5105891d4be71.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。36 条 bib entry 全部核查，发现 **8 个条目共 10 处错误**，全部已修正。

### 严重错误（作者完全编造）
- **zhang2024minkpp**: 作者、venue (EMNLP→ICLR)、年份 (2024→2025) 全错
- **hao2025rewrite**: 作者全错，venue 从 Findings 改为 Main
- **alemohammad2024selfconsuming**: 8 个作者中 4 个名字是编造的，还漏了 1 个

### 高严重度
- **xie2023dsir**: 标题缺 "for Language Models"，venue ICML→NeurIPS
- **tirumala2023d4**: 4 个作者中 2 个是错的 (Markosyan/Zettlemoyer → Simig/Morcos)
- **schaeffer2025position**: venue ICML→arXiv (NeurIPS 2025 under review)，作者名 Anirudh→Alvan Caleb

### 中等严重度
- **dohmatob2024model**: "Pin-Yu Yang"→"Pu Yang"
- **wang2024semeval**: 漏了 5 个作者

报告已写入 `artifacts/reference_audit_report.txt`。

---
