# analysis mmct bugfix expand v3

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mmct_bugfix_expand_v3_20260518T155459_result.json`
- **Structured JSON:** [`f45abdc77973f969897e.json`](../../sessions/f4/f45abdc77973f969897e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。结果总结：

### 验证清单

| # | 检查项 | 结果 |
|---|--------|------|
| 1 | Bug fix 后 bidirectional 结果变化 | ✅ weighted_pair: fwd 87.5% vs bidir 62.5%；weighted_global: fwd 12.5% vs bidir 8.3% |
| 2 | α=0.00 所有 6 模式 FPR=0 | ✅ 全部 0/24 |
| 3 | α=1.0 检测率 ≥ α=0.75 | ⚠️ 见下方分析 |
| 4 | Table 7 全部 7 条件出结果 | ✅ 7 conditions × 6 modes |
| 5 | Global vs pair 有区别 | ✅ pair 87.5% vs global 12.5% (α=0.75) |

### α=0.75 检测率 (6-way)

| Mode | 检测率 |
|------|--------|
| weighted_pair_forward | **21/24 = 87.5%** |
| weighted_pair_bidirectional | 15/24 = 62.5% |
| uniform_forward | 8/24 = 33.3% |
| uniform_bidirectional | 8/24 = 33.3% |
| weighted_global_forward | 3/24 = 12.5% |
| weighted_global_bidirectional | 2/24 = 8.3% |

### Table 7 (α=1.0, weighted_pair_forward 最优模式)

Baseline 5/8, GPT-2m **7/8**, OPT 5/8, 1.4B-s42 4/8, 1.4B-s43 4/8, C4-s42 5/8, C4-s43 4/8

### 关键发现

**Global weighting 过于保守。** 原因：global FPR pooling 将 naive_xcorr 的 95.8% FPR 应用于所有 pairs，使其权重仅 1.04（几乎忽略）。在 24 个 null observations 中，已有 ~5 个 null scores ≥ 0.3966（naive+diff+perm 的组合），导致大量 α=1.0 的真阳性无法通过 p<0.05 阈值。Per-pair weighting 因为可以针对不同 pair 的 FPR 特征自适应调节权重而表现更好。

### 输出文件

`artifacts/mmct_results/` 下 5 个文件全部生成：`mmct_results.json` (838KB), `null_distribution.json`, `mmct_report.md`, `fpr_fnr_comparison.md`, `mmct_table7.md`

---
