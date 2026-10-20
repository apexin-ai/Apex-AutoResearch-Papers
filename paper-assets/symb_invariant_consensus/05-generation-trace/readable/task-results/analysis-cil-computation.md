# analysis cil computation

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cil-computation_20260523T010151_result.json`
- **Structured JSON:** [`d6af7d57f6cc0efd4eb9.json`](../../sessions/d6/d6af7d57f6cc0efd4eb9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心结论：

**CIL (Task 1)**:
- Self CIL 均值 0.028 bits（近零），Cross-ZS 均值 0.108 bits（3.9×），Cross-FT 均值 1.177 bits（42.5×）
- 层级清晰：Self ≪ Cross-ZS < Cross-FT，架构独立性是信息增益的必要条件
- Self CIL 技术上 > 0（MI 非负），但量级远小于跨架构条件，且 5/6 自提取条件 SICA 不优于 SC

**Q5 (BR on SC-correct)**:
- 6/6 条件 BR_correct > 1（范围 1.84–18.00）
- 4/6 条件 BR_correct > BR_wrong：SC 正确时约束偏差更强（推理路径连贯，约束更一致地确认多数答案）

**Q6 (raw p < 0.05)**:
- 12/36 条件显著，全部 Δ > 0
- 共同特征：11/12 涉及 Mistral-7B（最弱生成器），12/12 在 PW-600 上，w3/w5 占 10/12
- 显著性集中于生成器-验证器能力差距最大的地方

报告已写入 `artifacts/cil_analysis.md`。

---
