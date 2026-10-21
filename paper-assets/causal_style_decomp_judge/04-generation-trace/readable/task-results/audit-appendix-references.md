# audit appendix references

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_appendix-references_20260525T090643_result.json`
- **Structured JSON:** [`9936b7c6c43b6522c1bf.json`](../../sessions/99/9936b7c6c43b6522c1bf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`register_artifact` 工具不可用，跳过注册步骤。审计和修复已完成。

**结果总结**：

- **附录盘点**：27 个 section/subsection，23 个 table，0 个 figure
- **引用问题**：仅 1 项 — `app:nli_ablation`（NLI 门控消融）在正文中讨论了结果数字但缺少 `\ref` 引用
- **修复**：在 `experiments.tex:190` 的 amplification controls 列表项 (i) 中添加 `Appendix~\ref{app:nli_ablation}`，指向完整消融表
- **删除**：无。所有附录内容均支撑主文 claims
- **审计报告**：已写入 `artifacts/audit_appendix_references.md`

这篇论文的附录引用整体质量很高，26/27 个附录 section 均已在正文中有明确的 `\ref` 引用且说明了读者去看能获得什么信息。

---
