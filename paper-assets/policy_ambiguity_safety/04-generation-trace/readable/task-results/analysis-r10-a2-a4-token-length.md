# analysis r10 a2 a4 token length

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r10_a2_a4_token_length_20260521T192257_result.json`
- **Structured JSON:** [`ad79cde9dd54d184629a.json`](../../sessions/ad/ad79cde9dd54d184629a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果已保存。

**Per-type token delta (unambiguous − ambiguous):**

| Type | Ambiguous | Unambiguous | Delta |
|------|-----------|-------------|-------|
| authorization_scope | 19.0 ± 3.3 | 55.0 ± 8.1 | **+36.1 ± 8.6** |
| incompleteness | 12.2 ± 2.4 | 46.8 ± 9.1 | **+34.6 ± 8.4** |
| lexical | 11.4 ± 2.3 | 37.0 ± 5.8 | +25.7 ± 5.2 |
| scopal | 15.7 ± 3.0 | 33.5 ± 8.5 | +17.8 ± 7.7 |
| conditional_precedence | 41.1 ± 7.0 | 58.6 ± 8.6 | +17.5 ± 9.8 |

**Incompleteness 分析**: delta 34.6 词，是整体均值 26.3 的 1.31 倍。authorization_scope 的 delta 更大（36.1），两者都系统性偏高。incompleteness 的高 delta 符合预期——缺失信息型歧义的消歧需要补充大量缺失条件/细节。

**A2 vs A4 等价性**: 两者使用相同的空格分词定义，且每个 clause 是单句或短段落，无更细粒度的句子划分。两个输出文件内容实质相同，A4 文件中注明了等价关系。

---
