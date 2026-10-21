# compute lofo importance

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_compute_lofo-importance_20260519T183649_result.json`
- **Structured JSON:** [`9f9342118f200898d6cb.json`](../../sessions/9f/9f9342118f200898d6cb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。输出文件：

- `lofo_results.json` (105KB) — 完整 JSON 结果
- `lofo_ranking.txt` — 按 1v2 delta AUC 排序的 feature importance
- `lofo_cross_domain_summary.txt` — 跨域 × 全部 depth pairs 汇总
- `lofo_table.tex` — LaTeX 表格

**1v2 LOFO 关键发现：**

| Feature | C4 | arXiv | Wiki | 跨域趋势 |
|---|---|---|---|---|
| **freq_entropy** | +0.0048 | +0.0085 | **+0.0134\*\*** | 3/3 正贡献，Wiki 显著 |
| **surp_std** | +0.0023 | **+0.0183\*\*** | +0.0008 | arXiv 上最重要的单特征 |
| **surp_mean** | -0.0001 | **+0.0036\*** | **+0.0055\*** | arXiv/Wiki 显著 |
| **surp_d2_std** | +0.0020 | **+0.0023\*** | -0.0017 | arXiv 显著 |
| **surp_d1_mean** | -0.0028 | **+0.0021\*** | +0.0001 | arXiv 显著 |

核心结论：
1. **freq_entropy** 是跨域最稳定有用的特征（3 个 domain 都正贡献）
2. **surp_std** 在 arXiv 上贡献最大（delta=+0.018, p=0.003）
3. 1v2 boundary 上大多数单特征的 LOFO delta 不显著——说明特征间有冗余，信息量由组合携带
4. C4 的 1v2 (baseline AUC=0.607) 基本没有单特征显著——这是真正的 hard boundary

---
