# analysis d102 t10 a050 s43

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d102-t10-a050-s43_20260522T064304_result.json`
- **Structured JSON:** [`7834a1ccd9ad8657e78b.json`](../../sessions/78/7834a1ccd9ad8657e78b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## T=10 α=0.50 s43 D102 分析结果

| 指标 | s43 | s42 基准 |
|------|-----|----------|
| **perm_granger_fdr_forward_sig** | **0/8** | 6/8 |
| diff_xcorr_fdr_forward_sig | 8/8 | — |
| threshold_forward_sig | 0/8 | — |
| ty_forward_sig | 0/8 | — |
| **robust_pairs K≥3** | **0/8** | — |

### 关键发现

**s43 与 s42 严重不一致。** PermG 从 6/8 跌至 0/8。

根因：PermG 原始 p 值多数在 0.05 附近（如 token_entropy→distinct_1 p=0.049），但 8-pair BH FDR 校正后全部升至 >0.05（FDR p≈0.098）。threshold onset 全部为 None（canary 或 downstream onset 缺失），TY 全部不显著。只有 diff_xcorr 8/8 通过 FDR，但仅靠单一方法，consensus 最高仅 2/5。

**结论：T=10 α=0.50 cross-seed robustness 不成立。** s42 的 6/8 PermG 结果是 seed-specific 的，不可推广。

JSON 已保存至服务器 `results/phase_diagram/t10_a050_s43_fp32/analysis/5method_leadlag.json`。

---
