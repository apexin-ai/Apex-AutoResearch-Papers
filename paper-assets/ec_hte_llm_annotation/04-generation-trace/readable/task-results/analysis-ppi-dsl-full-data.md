# analysis ppi dsl full data

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_ppi-dsl-full-data_20260522T044421_result.json`
- **Structured JSON:** [`da1cf1838adad94ec8f6.json`](../../sessions/da/da1cf1838adad94ec8f6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已保存至 `artifacts/ppi_dsl_full_analysis.md`。核心发现：

**数据不支持之前的结论。** 完整数据（3 regime × 3 budget × 8 cell 平均）显示：

1. **Naive 在所有条件下 RMSE 最低**（~0.105），击败所有纠偏方法——该模拟中误分类 bias 较小（|Bias|≈0.026），纠偏方差代价远超 bias 收益
2. **Global 是最优纠偏方法**（n≤250），PPI-global 在 n=500 胜出（0.116 vs 0.124）
3. **EC-HTE 在 9/9 条件下 RMSE 均劣于 Global**，n=100 时差距最大（0.500 vs 0.138）
4. **EC-HTE vs Strat.MLE**: partial pooling 有效（8/9 条件 EC-HTE 更优），但远不足以追上 Global
5. **"Debiasing hurts" 确认**: Global 在 S₀(π=0.05) 的 |bias| 一致大于 Naive
6. 高噪声子群 S₃(π=0.25) 是 EC-HTE/Strat.MLE 的灾难区——z=1 n=100 时 RMSE 爆炸到 2.0

论文叙事需要调整：要么重新定位 EC-HTE 的卖点（bias correctness 而非 RMSE），要么修改实验参数使 bias-variance tradeoff 更有利。

---
