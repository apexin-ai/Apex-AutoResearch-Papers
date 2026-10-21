# paper retrain appendix table update

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_retrain-appendix-table-update_20260519T035307_result.json`
- **Structured JSON:** [`951b977a563709490341.json`](../../sessions/95/951b977a563709490341.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

表格 `tab:retrain_ci`（lines 55-61）和 Extended Limitations 段落（line 39）中的所有数据与提供的 registry 数据完全一致，无需修改。

逐项核对结果：

**表格数据**（全部匹配）：
- 7 行 Qwen 数据：AUC 和 CI 均一致
- 7 行 Pythia 数据：AUC 和 CI 均一致

**正文引用**（line 39，全部匹配）：
- "1v2: 0.947 vs. 0.897" → 0.9470 vs 0.8971 的三位四舍五入，正确
- "4v5: 0.691 vs. 0.746" → 0.6907 vs 0.7459 的三位四舍五入，正确
- "6v7: Qwen 0.641, Pythia 0.634" → 0.6410 和 0.6340 的三位四舍五入，正确

---
