# research jaccard literature

**Transformer Model EAP-IG** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_jaccard-literature_20260512T231931_result.json`
- **Structured JSON:** [`23889441a15687642a13.json`](../../sessions/23/23889441a15687642a13.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调研完成，文件已写入 `artifacts/literature_jaccard_overlap.md`。

核心结论：

- **文献中无论文直接报告 EAP-IG × EP × ACDC 的 pairwise Jaccard**，但可从间接证据拼出基准
- **跨方法边级 Jaccard 典型范围 0.05–0.25**。节点级更高（0.25–0.60）
- 即使是**同一方法不同超参**，Jaccard 也能低至 0.02–0.07（arXiv 2510.00845）
- Bootstrap 重采样同方法的 Jaccard 均值仅 **0.561**
- EP 和 ACDC 在同等 faithfulness 下边数差 2.65×，暗示边集差异极大
- **关键叙事支撑**: Hanna et al. (COLM 2024) 证明 overlap ≠ faithfulness，支持我们 CSS 取交集做鲁棒编辑的思路

---
