# fix r15 claude likert discrepancy

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_r15-claude-likert-discrepancy_20260523T064124_result.json`
- **Structured JSON:** [`e7023fcb92e0baac96e7.json`](../../sessions/e7/e7023fcb92e0baac96e7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。核心发现：

**Table 1 和 Appendix U 的 Claude Likert 数值不一致，根因是两处使用了不同的计算方法，而非计算错误：**

| 差异 | Table 1 | Appendix U |
|------|---------|------------|
| ATE 方向 | 极向对齐（formal−casual） | 条件对齐（orig−cf） |
| p-value | Wilcoxon signed-rank | paired t-test |
| d 公式 | ATE(pole_a−pole_b) / pooled_sd | ATE(orig−cf) / pooled_sd |

两套数值都从同一数据（`scored_claude_formality/verbosity.jsonl`，NLI≥0.90）正确计算得出。BT 值一致是因为 BT 来自 pairwise 数据，与 Likert 方法无关。

**结论**：Table 1 的极向对齐方法（d=−0.021/−0.039）对 style bias 研究更恰当，因为它直接回答"judge 是否偏好 formal/verbose 风格"。Appendix U 应更新 `claude_crossbench_analysis.py` 的 `likert_analysis()` 函数，改为极向对齐 + Wilcoxon，与 Table 1 保持一致。

审计结果已写入 `artifacts/r15_analysis/claude_likert_audit.json`。

---
