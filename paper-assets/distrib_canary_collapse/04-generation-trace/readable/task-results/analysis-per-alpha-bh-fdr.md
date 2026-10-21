# analysis per alpha bh fdr

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_per_alpha_bh_fdr_20260519T033513_result.json`
- **Structured JSON:** [`eb2cbd69e91f89744df7.json`](../../sessions/eb/eb2cbd69e91f89744df7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。核心结果：

**Per-alpha BH FDR vs per-experiment BH FDR 主要差异**：

| 方法 | 变化 |
|------|------|
| naive_xcorr, diff_xcorr, threshold_onset | 无变化 |
| **perm_granger @ α=0.50** | **大幅下降: 3.00→0.67/8** (borderline p-values 在更大 pool 下失去显著性) |
| perm_granger @ α=0.75 | 微增: 6.33→6.67/8 |
| perm_granger @ α=1.00 | 微增: 4.62→4.88/8 |
| **ty_granger** | 各 α 普遍下降 1-2 个 sig count |

**对 dose-response 叙事的影响**：反而**加强**了。perm_granger 在 α=0.50 从 3.0/8 降至 0.67/8，α=0.75 维持 6.67/8，使 0.50→0.75 的跳跃更剧烈（0.67→6.67 vs 之前 3.0→6.33）。

n_perm=5000 已确认，无需升级。脚本在 westd-19828，报告在 `artifacts/per_alpha_fdr_results.md`。

---
