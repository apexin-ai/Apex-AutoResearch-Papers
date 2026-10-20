# review ref audit A

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_review_ref-audit-A_20260526T104656_result.json`
- **Structured JSON:** [`096c4aa9059ca0c5fca7.json`](../../sessions/09/096c4aa9059ca0c5fca7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

37 条引用逐条核查完成，结果写入 `artifacts/ref_audit_worker_A.md`。

**3 条有问题：**
- `hans2024binoculars` — 标题截断，缺副标题 ": Zero-Shot Detection of Machine-Generated Text"
- `sadasivan2023detect` — 已发表在 TMLR 2025，bib 仍标为 arXiv preprint 2023
- `liang2023gpt` — `related_work.tex:11` 将其作为 GPTZero 引用，但该论文是关于 GPT 检测器对非母语写作者偏见的研究，不是 GPTZero

其余 34 条均验证通过。

---
