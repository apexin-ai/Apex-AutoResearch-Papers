# ops harvest 1 7b 2048 final

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_harvest_1_7b_2048_final_20260519T200859_result.json`
- **Structured JSON:** [`0531b57c3f36319f7f69.json`](../../sessions/05/0531b57c3f36319f7f69.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/negative，无活跃 cron 需要清理。

## 结果摘要

| 指标 | 1024 tokens | 2048 tokens | 变化 |
|------|------------|------------|------|
| **Ign-F1** | 0.4349 | 0.4344 | -0.05pp |
| **Truncation** | 583/985 (59.2%) | 568/985 (57.7%) | -1.5pp |
| **Format OK** | — | 958/985 (97.3%) | — |
| **Evidence Tax** | -7.70pp | **-7.75pp** | 基本一致 |

**结论：1.7B evidence tax 是真实效应，非截断 artifact。**

将 max_new_tokens 翻倍后，ign_f1 几乎不变（0.4349→0.4344），截断率仅微降 1.5pp（59.2%→57.7%）。说明 1.7B 模型在 no-evidence 条件下截断的主因不是 token 不够，而是模型本身生成冗余重复内容——即便给更多空间也无法提升质量。

1.7B 真实 evidence tax = **-7.75pp**（ign_f1: 0.4344 vs with-evidence 0.5119）。对比 4B 的 evidence tax +0.94pp，1.7B 的 evidence 依赖性远高于 4B，这支持 "小模型更需要 evidence 作为推理线索" 的假设。

---
