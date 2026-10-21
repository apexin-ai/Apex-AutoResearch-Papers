# research adaptive shrinkage

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_adaptive-shrinkage_20260523T071542_result.json`
- **Structured JSON:** [`889a871e69c581af9996.json`](../../sessions/88/889a871e69c581af9996.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。结果汇总：

### 核心发现：Centered EB 全面优于 Original HB

| Config | Method | RMSE_z0 | RMSE_z1 | \|bias\|_z0 | \|bias\|_z1 |
|--------|--------|---------|---------|------------|------------|
| **K2 moderate** | global_corrected | 0.0684 | 0.0783 | 0.0080 | 0.0014 |
| | hb_original | 0.0703 | 0.0787 | 0.0109 | 0.0039 |
| | **hb_centered** | **0.0691** | **0.0781** | 0.0083 | 0.0014 |
| **K2 extreme** | global_corrected | 0.0912 | 0.1022 | 0.0496 | 0.0569 |
| | hb_original | 0.0879 | 0.0942 | 0.0134 | 0.0041 |
| | **hb_centered** | **0.0839** | **0.0909** | 0.0070 | 0.0068 |
| **K4 moderate** | global_corrected | 0.0978 | 0.1070 | 0.0089 | 0.0078 |
| | hb_original | 0.1006 | 0.1089 | 0.0131 | 0.0096 |
| | **hb_centered** | **0.0983** | **0.1070** | 0.0100 | 0.0081 |
| **K4 extreme** | global_corrected | 0.1040 | 0.1140 | 0.0277 | 0.0314 |
| | hb_original | 0.1081 | 0.1158 | 0.0163 | 0.0094 |
| | **hb_centered** | **0.1027** | **0.1117** | 0.0094 | 0.0066 |

### 关键结论

1. **Moderate heterogeneity**: `hb_centered` RMSE ≈ Global（不更差）— 目标达成
2. **Extreme heterogeneity**: `hb_centered` RMSE 低于 Global 和 original HB — 优势保持并增强
3. **原因**: 原始 HB 用 Dir(α/2, α/2) 向 (0.5, 0.5) 收缩（错误目标），Centered EB 向 global CM 收缩（正确目标），允许更强 pooling 而不引入偏差
4. **Pre-test**: moderate 下 79% 选 Global，extreme 下 97-100% 选 stratified — 决策合理
5. **意外发现**: K4 extreme 下原始 HB 的 RMSE 比 Global 还高，Centered EB 修复了这个问题

脚本：`/home/ubuntu/ec_hte_llm_annotation/exp_adaptive_shrinkage.py`
结果：`results/exp_adaptive_shrinkage.csv` (聚合) / `results/exp_adaptive_shrinkage_raw.csv` (原始)

---
