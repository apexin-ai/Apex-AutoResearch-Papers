# analysis d033 regression slope

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d033_regression_slope_20260516T015657_result.json`
- **Structured JSON:** [`e471d2ecacb1fe98c480.json`](../../sessions/e4/e471d2ecacb1fe98c480.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已保存到 `regression_slope.json`。汇总：

**D033 16-rel pool BCS-accuracy 回归分析 (n=100 batches)**

| 指标 | 值 |
|------|-----|
| BCS 范围 | [0.653, 0.900] |
| Accuracy 范围 | [0.712, 0.952] |
| **Slope** | **-0.449** |
| Bootstrap 95% CI | [-0.556, -0.349] |
| R² | 0.406 |
| r | -0.637 |
| p-value | 1.01e-12 |

**解读**：每 +0.1 BCS → **-4.49pp accuracy**。斜率显著为负（p < 1e-12），CI 不跨零。

这意味着在 16-rel pool 中，BCS 越高（类型间越相似）accuracy 越低，方向与 80-pool 一致。斜率绝对值可直接与 80-pool 回归斜率做标准化比较。

---
