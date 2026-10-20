# review paper number consistency

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_review_paper_number_consistency_20260515T192821_result.json`
- **Structured JSON:** [`02b720ff97b8a43cd7f5.json`](../../sessions/02/02b720ff97b8a43cd7f5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/paper_number_consistency_check.md`。

核心发现：

**Llama SciERC Zero-shot** — Table 5 和 §5.4 正文中全部 6 个数字 + ΔDR/ΔR-F1 完全正确，无需修改。

**Llama SciERC Fine-tuned LoRA** — **完全缺失**。全文 grep 零命中，8 个数字（DR=1.11%/0.09%, R-F1=45.45%/45.47%, E-F1=67.76%/67.76%, ΔDR=-91.9%, ΔR-F1=+0.02pp）不在论文任何位置。Table 3（composability matrix）仅有 Qwen 4 行，无 Llama 行。§5.2 composability 段落、Appendix B 均只讨论 Qwen LoRA。

**下游影响**：如果加入 Llama LoRA 数据，Abstract、Introduction、Limitations 中 "DR=0%" 的表述需改为 "DR≤0.09%"，因为 Llama LoRA constrained DR 不为零。Composability claim 需从 "complete DR elimination" 弱化为 "91.9–100% DR reduction"。

---
