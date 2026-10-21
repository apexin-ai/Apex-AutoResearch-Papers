# data k5 aggregation table extract

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_k5-aggregation-table-extract_20260523T101302_result.json`
- **Structured JSON:** [`a45571b5e93395a4dadc.json`](../../sessions/a4/a45571b5e93395a4dadc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已写入 `docs/paper/data/k5_aggregation_table_data.txt`。

汇总校验与用户提供的一致：
- Majority: K_eff 7/12, eta 0/12, R²=0.256
- Weighted: K_eff 9/12, eta 1/12, R²=0.249
- Threshold: K_eff 10/12, eta 6/12, R²=0.506
- Bayesian: K_eff 0/12, eta 1/12, R²=0.081

文件包含三部分：
1. **Summary table** — 4 行 LaTeX 可直接复制
2. **OLS vs Bootstrap 对比表** — 显示 bootstrap 如何收紧显著性
3. **48 条 per-condition 明细** — 含 β_std、FDR p、R²、显著性标记

---
