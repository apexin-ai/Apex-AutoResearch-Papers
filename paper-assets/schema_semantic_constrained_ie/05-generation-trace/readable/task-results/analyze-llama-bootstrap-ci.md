# analyze llama bootstrap ci

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_llama_bootstrap_ci_20260514T222348_result.json`
- **Structured JSON:** [`eb5480211c684c756648.json`](../../sessions/eb/eb5480211c684c756648.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。注意：DocRED 的 E-F1 计算值（57.92 vs 58.18）与任务描述的预期值（55.65 vs 55.01）有差异——可能是对齐后评估逻辑或数据版本不同。以下是实际 bootstrap 结果：

| Comparison | Delta | 95% CI | p-value | Significant? |
|---|---|---|---|---|
| Llama SciERC R-F1 | -0.04pp | [-0.10, -0.01] | 0.0106 | Yes (p<0.05) |
| Llama SciERC E-F1 | +0.03pp | [-0.18, +0.22] | 0.7618 | No |
| Llama DocRED R-F1 | +0.37pp | [+0.12, +0.62] | 0.0044 | Yes (p<0.01) |
| Llama DocRED E-F1 | +0.27pp | [-0.11, +0.65] | 0.1684 | No |

**关键发现**：
- **Llama DocRED E-F1**：delta=+0.27pp，p=0.1684，**不显著**（CI 跨零）
- **两个 R-F1 比较都显著**：SciERC R-F1 下降 0.04pp (p=0.011)，DocRED R-F1 上升 0.37pp (p=0.004)
- **两个 E-F1 比较都不显著**

注意 E-F1 绝对值与预期不一致（DocRED: 57.92/58.18 vs 预期 55.65/55.01），delta 方向也反了（+0.27 vs 预期 -0.64）。这可能涉及数据对齐、entity type 归一化差异等。结果 JSON 已保存在 `outputs/bootstrap_ci_results_llama.json`。

---
