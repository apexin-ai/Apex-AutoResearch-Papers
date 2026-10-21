# analysis d102 t25 a060 v3 star

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d102-t25-a060-v3-star_20260522T070336_result.json`
- **Structured JSON:** [`a7e39737c659f071b806.json`](../../sessions/a7/a7e39737c659f071b806.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。结果汇总：

## t25_a060_s42_fp32_v3 — Scenario A Confirmed ✓

| 指标 | 值 |
|------|-----|
| **perm_granger_fdr_forward** | **5/8** |
| perm_granger_fdr_reverse | 0/8 |
| diff_xcorr_fdr_forward | 8/8 |
| threshold_forward | 6/8 |
| ty_forward | 4/8 |
| robust_pairs K≥3 | 6/8 |
| robust_pairs K≥4 | 3/8 |

**Sync-dip dissolution confirmed**：T=10/15/20 α=0.60 全部 PermG=0/8，但 T=25 α=0.60 跳升至 PermG=5/8（强前向不对称，reverse=0/8）。延长训练代数打破了 sync-dip，canary lead-lag 信号在 26 代后显现。

Registry 已更新为 DONE/success，artifact 已注册。

---
