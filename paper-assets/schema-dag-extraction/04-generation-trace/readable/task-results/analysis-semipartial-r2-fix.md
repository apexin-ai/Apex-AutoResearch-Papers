# analysis semipartial r2 fix

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_semipartial_r2_fix_20260521T220639_result.json`
- **Structured JSON:** [`8b6d5d831a4dbe1d60a9.json`](../../sessions/8b/8b6d5d831a4dbe1d60a9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果汇总：

### 原始错误确认
`r1_statistical_supplements.py:167` 用了 `bcs_unique_r2 = r_partial**2`（squared partial correlation），不是 true semipartial R²（ΔR²）。

### DocRED (110 batches, VIF=50.9, 高共线性)

| 指标 | 值 |
|------|-----|
| R²_full (BCS+cent) | 0.5949 |
| R²_BCS_only | 0.5779 (= 0.7602² ✓) |
| R²_cent_only | 0.5393 |
| **True ΔR²_BCS** | **0.0557** |
| Old partial r² | 0.1208 |
| **高估倍数** | **2.17x** |
| Shared variance | 87.8% of R²_full |

### FewRel (204 batches, VIF=1.18, 低共线性)

| 指标 | 值 |
|------|-----|
| R²_full (BCS+cent) | 0.3253 |
| R²_BCS_only | 0.3253 (= 0.5703² ✓) |
| R²_cent_only | 0.0524 |
| **True ΔR²_BCS** | **0.2729** |
| Old partial r² | 0.2880 |
| **高估倍数** | **1.06x** |
| Shared variance | 16.1% of R²_full |

### 关键发现
- DocRED 问题严重：因 BCS 与 centrality 相关性极高（r=0.99），87.8% 的解释方差是共享的，BCS 的 unique contribution 仅 5.6%（被高估 2.17 倍）
- FewRel 影响轻微：低共线性下 partial r² ≈ ΔR²，误差仅 6%
- Degree centrality 对 FewRel accuracy 几乎无独立预测力（ΔR²_cent ≈ 0）

---
