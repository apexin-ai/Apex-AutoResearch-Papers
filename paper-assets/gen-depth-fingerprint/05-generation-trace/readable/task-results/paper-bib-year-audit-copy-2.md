# paper bib year audit

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_bib-year-audit_20260515T174748_result.json`
- **Structured JSON:** [`55befa54fbc430df5fb1.json`](../../sessions/55/55befa54fbc430df5fb1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已修复并同步。

**修复：**
- `self_consuming_mad`: 2023 → 2024，`@article` → `@inproceedings`，venue 改为 ICLR（两个 bib 文件均已更新）

**可疑：**
- `reliable_detection`: bib 标为 ICLR 2024，但无法在 ICLR 2024 proceedings 中确认收录。扩展版 "Stress Testing" 发表于 TMLR 2025。原文可能仅为 arXiv preprint（首发 2023）。建议手动确认后决定是否改为 arXiv preprint 2023 或 TMLR 2025。

**其他非年份问题（供参考）：**
- `munir_looking_glass`: 作者名与 EACL 2021 论文实际作者不匹配
- `wu_survey_2025`: 除第一作者外，后续作者列表与 CL 2025 实际作者不匹配
- `mapping_llm_science`: 已正式发表于 COLM 2024，可考虑更新 venue

---
