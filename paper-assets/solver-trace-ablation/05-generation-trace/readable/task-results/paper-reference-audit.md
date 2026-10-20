# paper reference audit

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_reference-audit_20260514T194405_result.json`
- **Structured JSON:** [`4c751285c31299f940f9.json`](../../sessions/4c/4c751285c31299f940f9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。结果摘要：

**无缺失引用** — 33 个 .tex 中的 citation key 全部在 .bib 中找到。

**4 个 CRITICAL 问题**：
1. `rubric-grpo` — author 是 `{Various}` 占位符，需补真实作者
2. `reward-hacking-survey` — author 是 `{Various}` 占位符
3. `lorp` — author 是 `{Various}` 占位符
4. `logic-rl` — author 字段只有 `Xian and others`，首作者名不完整

**23 个 orphan 条目**（在 .bib 中但从未被引用），其中 `proofwriter` 值得注意——论文正文多次提到 ProofWriter 数据集但未 cite。

报告已写入 `artifacts/reference_audit_report.md`。

---
