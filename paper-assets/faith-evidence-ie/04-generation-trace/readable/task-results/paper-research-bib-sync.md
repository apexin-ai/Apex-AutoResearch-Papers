# paper research bib sync

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_research_bib_sync_20260517T174600_result.json`
- **Structured JSON:** [`4f95e075fa96553e2ac7.json`](../../sessions/4f/4f95e075fa96553e2ac7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

20 个 BibTeX entries 已写入 `references.bib`。

关键信息来源说明：
- 14 个从 literature_map.yaml 获取了完整的 title/authors/venue/url
- 4 个不在 lit map 中的知名论文（LoRA, DPO, DeepSeekMath, Scaling Laws）使用了任务补充信息 + 已知作者列表
- 2 个 lit map 中 authors 为 Anonymous/Unknown 的（autore2024, zhao2025egrpo）保留 `{Anonymous}`
- SAIS 和 EIDER 的 lit map 作者信息有误，已用任务补充信息修正
- 年份/venue 均按 Director 指令修正（LMRC=2024, DocKS-RAG=ICML 2025, DREEAM=EACL 2023, Re-DocRED=EMNLP 2022, GenRES=NAACL 2024）

---
