# fix d041 neg difficulty check

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_d041-neg-difficulty-check_20260515T021009_result.json`
- **Structured JSON:** [`ba3d2b8eb120b94de99e.json`](../../sessions/ba/ba3d2b8eb120b94de99e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修改完成。

**discussion_v2.md §5.2** — 在分析开头增加了一句，明确区分三种策略的 *选样本方法* 和 *评估难度方法*：

> "the three strategies differ in *selection method*—random sampling, cosine-similarity ranking in the pretrained embedding space (embedding-distance), and BM25 lexical ranking within CodeQL-identified structurally connected files (dataflow-aware)—while the analysis *evaluates* the resulting negatives' difficulty uniformly via pretrained encoder cosine similarity as a common metric."

**related_work_v1.md** — 无混淆问题（描述为 "structure-grounded negatives derived from inter-procedural data-flow analysis"，准确且不涉及选样本机制细节）。

两个文件均已添加 `&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->` 标记，Claim 2 修改未被回退。`_project/paper/` 副本已同步。

---
