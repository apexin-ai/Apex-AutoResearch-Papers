# writing related work v1 reviewer2

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_related-work-v1-reviewer2_20260515T095827_result.json`
- **Structured JSON:** [`02b29bca900f4f871bc6.json`](../../sessions/02/02b29bca900f4f871bc6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

四项修改完成，摘要如下：

**修正 1 (§2.4)** — GraphCoder/ARISE scope：WebSearch 确认两者的 data-flow 分析确实是 intra-procedural（GraphCoder 用 CFG/CDG/DDG，ARISE 明确描述为 "intra-procedural definition-use edges"）。保留 intra-procedural 断言，但改写为更精确的表述，区分了两者各自的 data-flow 类型（control/data dependence vs. definition-use chains），并明确是 "data-flow analysis" 而非整个系统受限于 intra-procedural。

**修正 2 (§2.4)** — "all these methods" → "these methods primarily leverage structural graphs at inference time"，软化了全称断言。

**修正 3 (§2.3)** — CoCoHaNeRe 句后新增一句，说明该工作同时评估了多种非梯度策略（BM25 和 embedding-based），消除与 Introduction（批评 embedding negatives）的表述不一致。

**修正 4 (§2.2)** — 在 StructFuse 定位句前插入半句 "While GraphCodeBERT uses structural edges as a pretraining objective"，明确区分 pretraining objective vs. training-time negative selection。

---
