# paper exp041 appendix update

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_exp041-appendix-update_20260524T131222_result.json`
- **Structured JSON:** [`4fd91d2b749c7c2ceefe.json`](../../sessions/4f/4fd91d2b749c7c2ceefe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

编译通过，0 errors，0 undefined refs，33 页。

修改摘要：

**appendix.tex 两处修改：**

1. **L462 cherry-pick 限定**：原文 "EC-HTE reduces |bias| ... a 4× improvement" 前加 "In these three selected high-disparity configurations,"，末尾加 "; however, this advantage does not generalize across all asymmetric settings (see below)."

2. **新增 "Comprehensive grid evaluation" 段落**（原 L478 后，`\section{Supplementary Main Results}` 前）：
   - **R² 表格** (`tab:asym_r2_grid`)：6 ratios × 4 Δπ × 2 K panels，含说明 Δπ≥0.10 时 R²>0.73，Δπ=0.05 低 R² 是因 near-zero bias 导致回归 ill-conditioned
   - **Method comparison 表格** (`tab:asym_method_grid`)：Oracle/Naive/Global/EC-HTE 的 |Bias|/RMSE/Coverage，caption 明确写 "EC-HTE does not outperform global correction at n_expert=250"
   - **解释段**：EC-HTE RMSE > Global in all 48 configs (0.125 vs 0.109)，原因是 asymmetric CM 参数量翻倍导致 variance 增大，建议 n_expert ≥ 500

---
