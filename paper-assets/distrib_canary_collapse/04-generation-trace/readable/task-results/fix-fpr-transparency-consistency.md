# fix fpr transparency consistency

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_fpr_transparency_consistency_20260524T065102_result.json`
- **Structured JSON:** [`dd708fac65c22eb47fd2.json`](../../sessions/dd/dd708fac65c22eb47fd2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 最终汇总

### 1. 脚本逻辑对比结果

**无差异。** `extract_fpr_pvalues.py` 直接 `from batch_d102_6pair import ...`，consensus 逻辑完全一致：
- naive_xcorr: `significant AND peak_lag < 0`
- diff_xcorr: `sig_fdr AND peak_lag < 0`
- threshold_onset: `significant`
- perm_granger: `sig_fdr`
- ty_granger: `significant`

### 2. D102 重跑验证 (s45, s47)

在 westd-17855 用 `batch_d102_6pair.py` 重跑，结果与透明度 JSON 完全一致：

| Seed | PermG fwd FDR | K≥3 | K≥3 pairs | K≥3 methods | PermG? |
|------|:---:|:---:|-----------|-------------|:---:|
| s45 | 2/6 | 1/6 | ece→d2 | naive,threshold,ty | No |
| s46 | 0/6 | 1/6 | ece→d2 | naive,threshold,ty | No |
| s47 | 0/6 | 2/6 | ece→d1, ece→d2 | naive,threshold,ty | No |
| s48 | 0/6 | 0/6 | — | — | — |
| s49 | 0/6 | 0/6 | — | — | — |
| s50 | 2/6 | 2/6 | te→d1, te→d2 | naive,perm,ty | **Yes** |
| **合计** | **4/36** | **6/36** | | | |

PermG FPR: 4/36 = 11.1%  
K≥3 FPR: 6/36 = 16.7%

### 3. 差异原因

- **s47 K≥3 = 0/8 vs 2/6**: 旧 D160 用 8-pair basis（含 MAUVE 等），新分析用 6-pair basis（仅 distinct_1/2/3），pair 组成不同导致数值不同，**不是脚本逻辑差异**
- **PermG 声明错误**: Worker 声称 "6个K≥3假阳全部无PermG参与" 是错误的——s50 的 2 个 K≥3 FP 包含 PermG（consensus=[naive,perm,ty]）。正确分解：4/6 无 PermG，2/6 含 PermG

### 4. 已修正内容

- `fpr_transparency_all_seeds.json`: 修正 methods 描述（`lag<0` for consensus），添加 `threshold_criterion`、`pair_basis`、`K_ge_3_permg_breakdown`、`per_seed_permg_fwd_fdr` 字段
- `appendix_fpr_transparency_table.tex`: 表注添加参数说明（n_perm=5000, true_3sigma_d105, 6-pair basis, BH FDR），修正 PermG 参与声明

---
