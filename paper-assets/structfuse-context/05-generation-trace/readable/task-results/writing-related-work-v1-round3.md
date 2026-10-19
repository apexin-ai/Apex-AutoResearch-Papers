# writing related work v1 round3

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_related-work-v1-round3_20260515T103350_result.json`
- **Structured JSON:** [`db767f80d2923de1ce23.json`](../../sessions/db/db767f80d2923de1ce23.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部修正已完成。摘要如下：

---

### Critical #1：四节末尾 StructFuse 定位重写
- **§2.1** → "systematically comparing negative mining strategies...demonstrating that the choice of mining strategy meaningfully affects retrieval quality"
- **§2.2** → "systematically study how negative selection strategy...affects contrastive code retrieval across encoders with distinct representation geometries"
- **§2.3** → 保留原有三层递进结构（已符合 D049），仅做词级修正（见 Warning #2/#3）
- **§2.4** → "construct an additional strategy dimension for systematic comparison, enabling analysis of how structural signals interact with encoder representation geometry"（同时消除了 Warning #4 的 "internalizes cross-function data-flow semantics"）

### Warning #2："consistent" → "reliable"
- §2.3: "provides **reliable** improvement at **zero additional cost**"（原 "consistent retrieval gains at negligible cost"）

### Warning #3："orthogonal" → "complementary"
- §2.3: "data-flow structure as a **complementary** signal"（原 "orthogonal"）

### Warning #4："internalizes cross-function data-flow semantics" 已删除
- §2.4 重写时自然消除，全文无残留

### Info #5：8 篇引用验证
8 篇全部通过 WebSearch 验证，bib 条目均正确，无需修正：
SynCoBERT (arXiv 2021) ✓ | ContraBERT (ICSE 2023) ✓ | RocketQA (NAACL 2021) ✓ | STAR (SIGIR 2021) ✓ | CAPSTONE (EMNLP 2023) ✓ | ProGraML (ICML 2021) ✓ | CrossCodeEval (NeurIPS 2023) ✓ | GRACE (arXiv 2025) ✓

---
