# research cdr gda dataset

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_cdr_gda_dataset_20260518T100115_result.json`
- **Structured JSON:** [`7ec876eab17b53f22cdd.json`](../../sessions/7e/7ec876eab17b53f22cdd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GDA agent 的详细结果确认了关键发现：**GDA 同样无 evidence sentence annotations**（SAIS 论文明确指出 "Since neither CDR nor GDA annotates evidence sentences"）。

报告已在上一条消息中完整给出，GDA 部分的结论一致，无需修正。核心结论不变：

**CDR 和 GDA 均无 evidence 标注，但仍可作为 RE-only 跨领域评估基准。** 这两个是 DocRE 领域最广泛使用的生物医学 benchmark（ATLOP、DocuNet、SAIS 等论文均报告了两者的结果），可直接与已有 SOTA 对比。

---
