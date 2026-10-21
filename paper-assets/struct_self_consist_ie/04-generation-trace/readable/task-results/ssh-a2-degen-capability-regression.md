# ssh a2 degen capability regression

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_a2-degen-capability-regression_20260520T090113_result.json`
- **Structured JSON:** [`893c5422be358f12e2e6.json`](../../sessions/89/893c5422be358f12e2e6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。30 个数据点（6 个 model-regime 组合 × 3 个数据集）的回归分析结果：

| 方法 | R² | 备注 |
|------|------|------|
| Linear | 0.414 | degen = 129.5 × F1 − 56.9, p=1.3e-4 |
| Quadratic | 0.592 | U 型曲线，高 F1 端陡升 |
| Spearman ρ | 0.519 | p=3.3e-3 |

关键发现：degeneracy 与 F1 正相关，但主要由**数据集难度**驱动——CoNLL（简单任务，F1>0.90）degeneracy 极高（58-90%），SciERC（难任务，F1~0.64）degeneracy 低（10-27%）。同一数据集内不同模型的 degeneracy 差异较小，说明 degeneracy 更多反映的是任务本身的 entropy ceiling 而非模型能力。

输出文件：
- `artifacts/a2_degen_regression/degen_capability_scatter.png` / `.pdf`
- `artifacts/a2_degen_regression/regression_results.json`

---
