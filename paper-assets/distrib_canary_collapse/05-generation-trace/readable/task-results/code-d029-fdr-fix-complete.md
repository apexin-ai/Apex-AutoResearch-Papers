# code d029 fdr fix complete

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d029_fdr_fix_complete_20260515T093153_result.json`
- **Structured JSON:** [`7bef7743b475530efc4d.json`](../../sessions/7b/7bef7743b475530efc4d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 完成汇报

### P0: FDR 显式修复 + 重跑

**a. 6 个 robust pairs 是否变化？**

不变。同样 6 对：token_entropy→distinct_{1,2,3}、ece→distinct_{1,2,3}。但内部数字有移动：
- ece→distinct_1: TY 从 5/5→4/5 methods（seeds 3→2），仍满足 ≥4/5
- token_entropy→distinct_3: permG seeds 4→3，仍 5/5 methods

**b. FPR/FNR 新旧对比**

| Method | FPR old→new | FNR old→new | 原因 |
|--------|:---:|:---:|------|
| naive_pearson | 100%→100% | 0%→0% | 不变 |
| differenced_xcorr | 0%→0% | 0%→0% | sig_seed 55→53 |
| threshold_onset | 11.1%→**9.1%** | 0%→0% | N_neg 增大 9→11 |
| toda_yamamoto | 0%→0% | 20.8%→**25.0%** | FDR 砍掉更多 borderline seeds |
| permutation_granger | 11.1%→**0.0%** | 0%→**4.2%** | FDR 消除了唯一 FP，引入 1 FN |
| consensus | 0%→0% | 0%→0% | 不变 |

N_neg 从 9→11（differenced_xcorr 自身丢失 2 个 seed-level significance）。

**c. Sensitivity: token_entropy→distinct 稳定性**

- token_entropy→distinct_1: 仍 9/9 stable
- token_entropy→distinct_2: 仍 9/9 stable
- token_entropy→distinct_3: **9/9→8/9**（permG 在最严格配置 ≥5/5,≥4/4 下 3/4 seeds 不够）

### P1: LOO FPR/FNR

新增 `compute_fpr_fnr_loo()`，输出已保存到 `fpr_fnr_loo.json`。核心发现：permutation_granger 综合最优（FPR_loo=12.5%, FNR_loo=28.1%），naive_pearson 在任何 ground truth 下都是 FPR≈100%，LOO 消除了 differenced_xcorr 做裁判的循环性。

---
