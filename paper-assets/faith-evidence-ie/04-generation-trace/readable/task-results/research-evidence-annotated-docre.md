# research evidence annotated docre

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_evidence_annotated_docre_20260518T104347_result.json`
- **Structured JSON:** [`b2633bd9dac5f58c1309.json`](../../sessions/b2/b2633bd9dac5f58c1309.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== Evidence-Annotated DocRE 数据集调研 ===

| 数据集 | 领域 | Evidence 标注 | 规模 | 与 DocRED 跨领域 | 推荐 |
|--------|------|--------------|------|-----------------|------|
| BioRED | 生物医学 (PubMed) | 无。标注了 intra/cross-sentence 及 novelty，但无 supporting sentence 标注 | 600 篇摘要，10.8 rel/doc | 是 | - |
| SciREX | 科学论文 (CS) | 无。仅有 salient entity + N-ary relation | 438 篇全文 | 是 | - |
| DWIE | 新闻 (Deutsche Welle) | 无。有 relation + coref + entity linking，无 evidence sentence | 802 篇新闻 | 是 | - |
| DialogRE | 对话 (Friends) | 部分。49.6% triple 有 trigger span（非完整 evidence sentence） | 1,788 段对话 | 是 | - |
| CDR | 生物医学 | 无 | 1,500 篇 | 是 | - |
| CodRED | Wikipedia（跨文档） | 无 | ~30K doc pairs | 否 | - |
| JacRED | Wikipedia（日语） | 有 evidence sentence 标注 | 日语 Wikipedia | 否（同 Wikipedia 领域） | - |

结论: **未找到**同时满足"跨领域 + evidence sentence 标注"的数据集。

- DocRED/Re-DocRED 的 evidence 标注设计在现有 DocRE 数据集中几乎是独有的
- BioRED 领域最合适但无 evidence 标注（600 篇摘要，补标工作量可控）
- DialogRE 有 trigger span 但粒度不同且覆盖率仅半数
- JacRED 有 evidence 标注但仍是 Wikipedia 领域，不算跨领域

推荐: **无现成合适选项**。如需跨领域验证，最可行路线是对 BioRED 补标 evidence sentence（摘要短，每篇约 12 句，600 篇规模可控）。

---
