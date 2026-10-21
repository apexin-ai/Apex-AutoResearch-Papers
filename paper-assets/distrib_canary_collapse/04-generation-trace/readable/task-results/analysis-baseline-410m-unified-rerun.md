# analysis baseline 410m unified rerun

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_baseline_410m_unified_rerun_20260518T003545_result.json`
- **Structured JSON:** [`128af322aa28a0e31e8b.json`](../../sessions/12/128af322aa28a0e31e8b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果与旧 registry 值有显著差异，主要原因是统一参数（xcorr max_lag 从 3→5、n_perm 从 1000→5000、不做 FDR）。

---

## 结果

**Raw p<0.05 计数**（统一参数：n_perm=5000, xcorr_lag=5, granger_lag=1, no FDR）：

| 方法 | X/8 | 旧值 | 差异 |
|------|-----|------|------|
| naive_xcorr | 8/8 | 7/8 | +1（max_lag 5 更宽，token_entropy→perplexity 边际显著 p=0.0455） |
| diff_xcorr | 8/8 | 6/8 | +2（同上原因） |
| threshold_onset | 8/8 | 6/8 | +2（可能旧分析用了 4 canary × 4 downstream 不同 pair 集） |
| permg_fwd | 6/8 | 6/8 | 一致 |
| permg_rev | 3/8 | 0/8 | +3（ece→distinct_{1,2,3} 反向 p≈0.027-0.031，n_perm=5000 下刚过阈值） |
| ty_granger | 4/8 | 6/8 | -2（受 C003 约束，TY 在短序列不稳定） |
| K≥3 | 8/8 | — | — |
| K≥4 | 6/8 | 6/8 | 一致 |

**Per-pair PG raw p-values**：

| Pair | PG_fwd_p | PG_rev_p |
|------|----------|----------|
| token_entropy→perplexity | 0.5841 | 0.9658 |
| token_entropy→distinct_1 | 0.0002 | 0.4921 |
| token_entropy→distinct_2 | 0.0012 | 0.4805 |
| token_entropy→distinct_3 | 0.0012 | 0.5047 |
| ece→perplexity | 0.8040 | 0.1418 |
| ece→distinct_1 | 0.0002 | 0.0274 |
| ece→distinct_2 | 0.0006 | 0.0286 |
| ece→distinct_3 | 0.0006 | 0.0306 |

**差异原因汇总**：
- `naive_xcorr`/`diff_xcorr` 增加：max_lag 从 3→5 捕获了更多滞后相关
- `permg_rev` 增加 3 个：ece→distinct_{1,2,3} 反向因果刚过 0.05 阈值（0.027-0.031），n_perm=5000 精度更高
- `ty_granger` 减少 2 个：旧分析可能用了不同 pair 集（4 canary 而非 2）；ece→distinct_{2,3} 和 ece→perplexity 的 TY p 值在 0.09-0.13 区间

结果已保存至 `results/generalize/pythia410m_wiki_a100_s42/analysis/pythia410m_8pair_5method_analysis.json`。

---
