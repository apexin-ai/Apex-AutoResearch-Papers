# fix related work info

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_related-work-info_20260514T224433_result.json`
- **Structured JSON:** [`cd2c7d22d2c866c40784.json`](../../sessions/cd/cd2c7d22d2c866c40784.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三处修改完成：

1. **§2.1**: "all graph-guided methods" → "these graph-guided methods"
2. **§2.2**: 开头插入 Sentence-BERT 引用（`\cite{reimers2019sentencebert}`），自然衔接到对比学习在代码表示上的应用
3. **§2.3**: "consistently improves" 后加 "(pilot evidence; pending M2 full confirmation)"

注：Sentence-BERT 已在 literature_map.yaml 的 `hard_negative_mining` 类目下（category/role/year/venue/authors 均匹配），无需重复录入。

---
