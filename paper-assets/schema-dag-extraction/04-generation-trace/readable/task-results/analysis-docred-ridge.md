# analysis docred ridge

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_docred_ridge_20260522T045710_result.json`
- **Structured JSON:** [`70fbd74f4b52eac6033c.json`](../../sessions/70/70fbd74f4b52eac6033c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果摘要：

**Ridge Regression (110 DocRED batches)**
- GCV 选择 λ = 0.001（极小正则化即可稳定）
- 标准化系数：β_BCS = **-1.53**, β_centrality = 0.78, R² = 0.594
- OLS 系数：β_BCS = -1.68, β_centrality = 0.93（VIF≈50.9 下轻度膨胀）
- **BCS 系数在所有 λ ≥ 0 下均为负**（解析证明：分子 = −0.033 − λ×0.760，单调递减）

注意事项：
- `semipartial_r2_verification.json` 中 `zero_order_r_cent: 0.7344` 有符号错误，实际应为 **-0.7344**（已通过 R²=0.5949 和 partial_r=-0.3476 交叉验证）
- 由于 SSH 密钥未配置在此环境，分析使用相关矩阵解析计算（数学等价于 RidgeCV on standardized data）
- 产出已注册：`docred_ridge_regression.json` + `docred_ridge_appendix.tex`

---
