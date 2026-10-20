# analysis 410m s44 d102

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_410m_s44_d102_20260522T230052_result.json`
- **Structured JSON:** [`d0d22e098358eeb335fb.json`](../../sessions/d0/d0d22e098358eeb335fb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**D102 5-method 分析已存在**，无需重新运行。JSON 位于 17855 上 `results/alpha_sweep/a050_s44_fp32/analysis/5method_leadlag.json`，使用了正确参数（`threshold_criterion: true_3sigma_d105`，downstream 含 mauve，n_perm=5000）。

## s44 D102 结果

### Summary

| Method | Forward sig (/8) | Reverse sig (/8) |
|--------|-----------------|-----------------|
| **Perm Granger (FDR)** | **6/8** | **0/8** |
| Diff XCorr (FDR) | 8/8 | 8/8 |
| Naive XCorr | varies | - |
| Threshold Onset (D105) | 0/8 | - |
| TY Granger | 3/8 | - |

### K≥3 Consensus: **4/8 pairs**

| Pair | Votes | Methods |
|------|-------|---------|
| token_entropy → distinct_1 | 3/5 | diff, perm, ty |
| token_entropy → distinct_2 | 2/5 | diff, perm |
| token_entropy → distinct_3 | 2/5 | diff, perm |
| token_entropy → mauve | 2/5 | naive, diff |
| ece → distinct_1 | **4/5** | naive, diff, perm, ty |
| ece → distinct_2 | **4/5** | naive, diff, perm, ty |
| ece → distinct_3 | **3/5** | naive, diff, perm |
| ece → mauve | 2/5 | naive, diff |

### 三 Seed 对比 (α=0.50, mauve downstream)

| Metric | s42 | s43 | **s44** |
|--------|-----|-----|---------|
| PermG fwd | 6/8 | 0/8 | **6/8** |
| PermG rev | 0/8 | 0/8 | **0/8** |
| K≥3 robust | ? | ? | **4/8** |

### Seed Variance 判断

**s44 站 s42**。PermG forward 6/8 与 s42 完全一致，远离 s43 的 0/8。α=0.50 的 tie-breaker 结果：2/3 seed 支持 6/8 forward causation，s43 是 outlier。

值得注意：ECE 是 s44 最强的 canary（4 个 ece pair 中 PermG 全部 FDR-significant，而 token_entropy 只有 2/4），与之前的 cross-seed 观察一致。方向性完美：3 seed 均为 0/8 reverse。

---
