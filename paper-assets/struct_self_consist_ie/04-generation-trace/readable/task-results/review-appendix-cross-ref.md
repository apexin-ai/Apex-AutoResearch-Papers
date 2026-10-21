# review appendix cross ref

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_review_appendix-cross-ref_20260524T023114_result.json`
- **Structured JSON:** [`1d0ef4fd4d2190c2a222.json`](../../sessions/1d/1d0ef4fd4d2190c2a222.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审查完成。

**结果：所有 33 个唯一 appendix label 均存在，64 处主文引用全部有对应内容，无缺失或内容不足。**

3 个需注意的潜在问题：
1. `sec:mechanistic` 用了 `sec:` 前缀但实际位于 appendix 中，且 mechanistic.tex 主文文件与 appendix 内容重复——需确认编译时无 duplicate label
2. diagnostic.tex 与 method.tex 内容重叠（均定义 `sec:method`），需确认只编译其中一个
3. theoretical.tex 与 theory.tex 均定义 `thm:degeneracy_bound`，同理

报告已写入 `artifacts/appendix_crossref_review.md` 并注册。

---
