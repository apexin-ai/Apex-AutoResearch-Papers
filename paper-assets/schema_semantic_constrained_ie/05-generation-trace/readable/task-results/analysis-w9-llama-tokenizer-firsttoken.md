# analysis w9 llama tokenizer firsttoken

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_w9_llama_tokenizer_firsttoken_20260515T085711_result.json`
- **Structured JSON:** [`b204b4711646eeead11a.json`](../../sessions/b2/b204b4711646eeead11a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 4 个组合（Llama/Qwen × SciERC/DocRED）first-token 唯一性 **全部 PASS**，无冲突。

**关键发现**：
- SciERC 6 types：Llama/Qwen 均 6/6 unique（raw + space-prefix）。`OtherScientificTerm` 是 4-token，但首 token `Other` 在类型集合内仍唯一
- DocRED 6 types：Llama/Qwen 均 6/6 unique。`MISC`→`M`+`ISC`（首 id=44），`ORG`(space)→` OR`+`G`，但首 token 在类型集合内仍唯一
- Llama 与 Qwen 在低频字节 token 上 id 完全一致（`M`=44, ` M`=386），同属 byte-level BPE 家族
- **唯一注意点**：DocRED 的 `MISC` 首 token 是单字节 `M`，若 schema 扩展加入其他 `M*` 类型会冲突；当前 6 类安全

报告已写到 `artifacts/rebuttal/w9_tokenizer_firsttoken_report.md`。

---
