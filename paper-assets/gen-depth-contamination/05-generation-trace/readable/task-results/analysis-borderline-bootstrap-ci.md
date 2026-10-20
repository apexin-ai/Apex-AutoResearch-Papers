# analysis borderline bootstrap ci

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_borderline_bootstrap_ci_20260516T165531_result.json`
- **Structured JSON:** [`12ee2a5d057587e750ab.json`](../../sessions/12/12ee2a5d057587e750ab.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

| Case | Depth Pair | AUC (OOF) | 95% CI | Perm p-value | Verdict |
|------|-----------|-----------|--------|-------------|---------|
| **exp-021 512tok** | 1v2 | 0.6073 | [0.5979, 0.6166] | 0.0001 | **BORDERLINE** |
| **exp-020 t07** | 2v3 | 0.5939 | [0.5855, 0.6025] | 0.0001 | **BORDERLINE** |
| **exp-020 t12** | 1v2 | 0.6170 | [0.6071, 0.6270] | 0.0001 | **PASS** |

### 判定分析

1. **exp-021 512tok 1v2**: CI lower = 0.5979 < 0.60，mean > 0.60 → **BORDERLINE**。需要在论文中注明 CI 跨越 θ=0.60 阈值。

2. **exp-020 t07 2v3**: CI upper = 0.6025 > 0.60，mean < 0.60 → **BORDERLINE**。虽然 point estimate 低于阈值，但 CI 上界越过 0.60，需在论文中注明不能完全排除 depth 2→3 可区分。

3. **exp-020 t12 1v2**: CI lower = 0.6071 > 0.60 → **PASS**。尽管有 1 个 fold (0.5961) 低于阈值，整体 CI 仍稳固地在 0.60 以上，无需 borderline 注释。

所有 3 个 case 的 permutation p-value = 0.0001（即 10000 次置换中从未超过观测值），分类器显著优于随机。

**论文建议**：Case 1 和 Case 2 需加 borderline 注释（footnote 或括号标注 CI 跨阈值），Case 3 无需。

---
